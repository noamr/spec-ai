#!/usr/bin/env python3
"""
Verification runner for a whatwg/html PR branch during the multi-review loop.

Unlike running check_algorithms.py / check_webidl.py on raw `git diff` hunks
(which truncates enclosing `<div algorithm>` blocks and causes false positives
for variable scope/lifecycle checks) or on the entire 166k-line `source` file
(which flags pre-existing issues in untouched sections), this script:

1. Computes the modified line ranges in `source` between `<base>` and `<head>`.
2. Extracts every complete `<div algorithm>...</div>` and `<pre class="idl">...</pre>`
   block in `source` that overlaps at least one modified line, preserving exact
   `source` line numbers.
3. Runs `WebIDLAnalyzer` and `AlgorithmAnalyzer` (from `../html-spec-review/scripts`)
   on those complete blocks.
4. Optionally runs the local Wattsi build (if available) and `check_wpt_coverage.py`
   (if a WPT directory is provided).
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
REVIEW_SCRIPTS_DIR = SCRIPT_DIR.parent.parent / "html-spec-review" / "scripts"
sys.path.insert(0, str(REVIEW_SCRIPTS_DIR))

import check_algorithms  # type: ignore
import check_webidl  # type: ignore
import check_wpt_coverage  # type: ignore


def run_git(repo_dir: Path, args: List[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=str(repo_dir),
        capture_output=True,
        text=True,
        check=False,
    )


def get_changed_line_ranges(
    repo_dir: Path, base_ref: str, head_ref: str = "HEAD", file_rel: str = "source"
) -> List[Tuple[int, int]]:
    """Return 1-based inclusive (start, end) line ranges in `head_ref:file_rel` modified since `base_ref`."""
    res = run_git(repo_dir, ["diff", "-U0", f"{base_ref}...{head_ref}", "--", file_rel])
    if res.returncode != 0:
        # Fallback to two-dot diff if merge-base fails
        res = run_git(repo_dir, ["diff", "-U0", base_ref, head_ref, "--", file_rel])
        if res.returncode != 0:
            raise RuntimeError(f"git diff failed: {res.stderr.strip()}")

    ranges: List[Tuple[int, int]] = []
    hunk_re = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")
    for line in res.stdout.splitlines():
        m = hunk_re.match(line)
        if m:
            start = int(m.group(1))
            count = int(m.group(2)) if m.group(2) is not None else 1
            if count > 0:
                ranges.append((start, start + count - 1))
    return ranges


def ranges_overlap(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    return a[0] <= b[1] and b[0] <= a[1]


def extract_touched_containers(
    lines: List[str], changed_ranges: List[Tuple[int, int]]
) -> Tuple[str, List[Tuple[int, int]]]:
    """
    Build a masked copy of `source` (preserving exact line numbers by keeping blank lines
    outside touched containers) containing every complete `<div algorithm>...</div>` block,
    `<pre ... class="idl">...</pre>` block, and directly modified line that overlaps
    `changed_ranges`.
    """
    n = len(lines)
    keep_line = [False] * (n + 1)  # 1-based indexing

    # Mark all directly changed lines first
    for start, end in changed_ranges:
        for ln in range(max(1, start), min(n, end) + 1):
            keep_line[ln] = True

    # Find complete <div algorithm>...</div> blocks and <pre class="idl">...</pre> blocks
    div_open_re = re.compile(r"<div\b[^>]*>", re.IGNORECASE)
    div_algo_re = re.compile(r"<div\s+algorithm[\s>]", re.IGNORECASE)
    div_close_re = re.compile(r"</div\s*>", re.IGNORECASE)

    pre_idl_open_re = re.compile(r'<pre\b[^>]*class=["\']?[^"\'>]*\bidl\b[^>]*>', re.IGNORECASE)
    pre_close_re = re.compile(r"</pre\s*>", re.IGNORECASE)

    container_ranges: List[Tuple[int, int]] = []

    i = 1
    while i <= n:
        line = lines[i - 1]
        if div_algo_re.search(line):
            start_ln = i
            depth = 0
            j = i
            while j <= n:
                l_text = lines[j - 1]
                depth += len(div_open_re.findall(l_text))
                depth -= len(div_close_re.findall(l_text))
                if depth <= 0:
                    break
                j += 1
            end_ln = min(n, j)
            if any(ranges_overlap((start_ln, end_ln), r) for r in changed_ranges):
                container_ranges.append((start_ln, end_ln))
                for ln in range(start_ln, end_ln + 1):
                    keep_line[ln] = True
            i = end_ln + 1
            continue

        if pre_idl_open_re.search(line):
            start_ln = i
            j = i
            while j <= n:
                if pre_close_re.search(lines[j - 1]):
                    break
                j += 1
            end_ln = min(n, j)
            if any(ranges_overlap((start_ln, end_ln), r) for r in changed_ranges):
                container_ranges.append((start_ln, end_ln))
                for ln in range(start_ln, end_ln + 1):
                    keep_line[ln] = True
            i = end_ln + 1
            continue

        i += 1

    masked_lines = [
        lines[ln - 1] if keep_line[ln] else "\n"
        for ln in range(1, n + 1)
    ]
    return "".join(masked_lines), container_ranges


def is_false_positive_duplicate_let(issue: check_algorithms.AlgorithmIssue) -> bool:
    """
    check_algorithms.py scans the entire line containing `Let ` for `<var>name</var>`,
    which accidentally matches `<var>name</var>` on the right-hand side of `be`
    (e.g. `Let <var>x</var> be <var>el</var>'s ...`). Filter out cases where the
    variable does not appear between `Let` and `be`.
    """
    if issue.rule != "ALGO-DUPLICATE-LET":
        return False
    m_var = re.search(r"Variable '<var>([^<]+)</var>'", issue.message)
    if not m_var:
        return False
    var_name = m_var.group(1)
    let_lhs_matches = re.findall(r"\bLet\s+(.*?)\s+be\b", issue.snippet)
    if not let_lhs_matches:
        return False
    return not any(
        re.search(rf"<var(?:\s+[^>]*)?>{re.escape(var_name)}</var>", lhs)
        for lhs in let_lhs_matches
    )


def is_line_near_changes(
    line_num: int, changed_ranges: List[Tuple[int, int]], margin: int = 2
) -> bool:
    for start, end in changed_ranges:
        if (start - margin) <= line_num <= (end + margin):
            return True
    return False


def find_wattsi_build_script(repo_dir: Path, explicit_build_dir: Optional[Path]) -> Optional[Path]:
    if explicit_build_dir:
        candidate = explicit_build_dir / "build.sh"
        if candidate.is_file():
            return candidate
    # Check if repo_dir is inside an html-build directory (e.g., .../html-build/html)
    parent_build = repo_dir.parent / "build.sh"
    if parent_build.is_file():
        return parent_build
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify a whatwg/html branch with static analyzers, Wattsi build, and WPT coverage."
    )
    parser.add_argument(
        "repo_dir",
        type=Path,
        help="Path to the whatwg/html git checkout or worktree.",
    )
    parser.add_argument(
        "--base",
        default="main",
        help="Base git ref to diff against (default: main).",
    )
    parser.add_argument(
        "--head",
        default="HEAD",
        help="Head git ref to analyze (default: HEAD).",
    )
    parser.add_argument(
        "--all-in-touched-containers",
        action="store_true",
        help="Report findings anywhere in touched <div algorithm> blocks, not just near changed lines.",
    )
    parser.add_argument(
        "--build",
        action="store_true",
        help="Run html-build/build.sh if available.",
    )
    parser.add_argument(
        "--build-dir",
        type=Path,
        default=None,
        help="Explicit path to html-build directory.",
    )
    parser.add_argument(
        "--wpt-dir",
        type=Path,
        default=None,
        help="Optional path to a local WPT checkout for check_wpt_coverage.py.",
    )
    args = parser.parse_args()

    repo_dir = args.repo_dir.resolve()
    source_path = repo_dir / "source"
    if not source_path.is_file():
        print(f"Error: {source_path} does not exist.", file=sys.stderr)
        return 2

    # Ensure split_source/ is not left behind
    split_dir = repo_dir / "split_source"
    if split_dir.exists():
        print(
            f"[VERIFY-SPLIT-DIR] WARNING: {split_dir} exists! Run `split_html.py concat` and remove `split_source/` before verifying.",
            file=sys.stderr,
        )
        return 1

    changed_ranges = get_changed_line_ranges(repo_dir, args.base, args.head)
    if not changed_ranges:
        print(f"No changes in `source` between {args.base} and {args.head}.")
        return 0

    raw_text = source_path.read_text(encoding="utf-8")
    lines = raw_text.splitlines(keepends=True)
    masked_content, container_ranges = extract_touched_containers(lines, changed_ranges)

    total_changed_lines = sum(end - start + 1 for start, end in changed_ranges)
    print(
        f"Analyzing {len(changed_ranges)} diff hunk(s) ({total_changed_lines} added/modified lines) "
        f"across {len(container_ranges)} complete <div algorithm>/<pre class='idl'> block(s)..."
    )

    idl_analyzer = check_webidl.WebIDLAnalyzer()
    idl_blocks = idl_analyzer.extract_idl_blocks(masked_content)
    for _, block_text in idl_blocks:
        idl_analyzer.analyze_dictionaries(block_text)
    for line_no, block_text in idl_blocks:
        idl_analyzer.check_block(str(source_path), line_no, block_text)

    algo_analyzer = check_algorithms.AlgorithmAnalyzer()
    algo_analyzer.check_formatting_and_markup(str(source_path), masked_content)
    for line_no, block_text in algo_analyzer.extract_algorithms(masked_content):
        algo_analyzer.check_algorithm_block(str(source_path), line_no, block_text)

    # Filter findings: keep any finding on/near changed lines (excluding RHS Let false positives)
    filtered_algo_errors = []
    for issue in algo_analyzer.issues:
        if is_false_positive_duplicate_let(issue):
            continue
        if args.all_in_touched_containers or is_line_near_changes(issue.line_no, changed_ranges):
            filtered_algo_errors.append(issue)

    filtered_idl_errors = [
        issue
        for issue in idl_analyzer.issues
        if args.all_in_touched_containers or is_line_near_changes(issue.line_no, changed_ranges)
    ]

    exit_code = 0
    if filtered_idl_errors:
        exit_code = 1
        print(f"\nFound {len(filtered_idl_errors)} WebIDL issue(s):")
        for issue in sorted(filtered_idl_errors, key=lambda x: x.line_no):
            print(f"  {issue}")
    else:
        print("WebIDL static check: PASS (0 issues).")

    if filtered_algo_errors:
        exit_code = 1
        print(f"\nFound {len(filtered_algo_errors)} Algorithm/Markup issue(s):")
        for issue in sorted(filtered_algo_errors, key=lambda x: x.line_no):
            print(f"  {issue}")
    else:
        print("Algorithm & Markup static check: PASS (0 issues).")

    if args.wpt_dir:
        print(f"\nRunning WPT coverage check against {args.wpt_dir}...")
        diff_res = run_git(repo_dir, ["diff", f"{args.base}...{args.head}", "--", "source"])
        wpt_files = (
            list(args.wpt_dir.rglob("*.html")) + list(args.wpt_dir.rglob("*.js"))
            if args.wpt_dir.is_dir()
            else [args.wpt_dir]
        )
        wpt_analyzer = check_wpt_coverage.WPTCoverageAnalyzer()
        wpt_issues = wpt_analyzer.audit_coverage(diff_res.stdout, wpt_files)
        if wpt_issues:
            print(f"  Found {len(wpt_issues)} WPT coverage warning(s):")
            for w_issue in wpt_issues:
                print(f"    {w_issue}")
        else:
            print("  WPT coverage check: PASS (all modified sinks and thrown exceptions covered).")

    if args.build:
        build_script = find_wattsi_build_script(repo_dir, args.build_dir)
        if build_script:
            print(f"\nRunning Wattsi build via {build_script}...")
            build_res = subprocess.run(
                [str(build_script), "--fast"],
                cwd=str(build_script.parent),
                capture_output=True,
                text=True,
                check=False,
            )
            if build_res.returncode != 0:
                exit_code = 1
                print("Wattsi build: FAILED")
                print(build_res.stdout)
                print(build_res.stderr, file=sys.stderr)
            else:
                print("Wattsi build: PASS")
        elif shutil.which("wattsi"):
            print("\n`wattsi` binary found on PATH, but no html-build/build.sh wrapper configured; skipping full build.")
        else:
            print("\nNo html-build/build.sh or wattsi found; skipping Wattsi build.")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
