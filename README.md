# spec-ai

AI tooling and agent skills for working with WHATWG standards.

## Skills

- **[`html-spec-review`](skills/html-spec-review/SKILL.md)**: Authoring and review guide for the [HTML Standard](https://github.com/whatwg/html). Covers Web IDL cross-references, Infra data structures, variable lifecycle (`Let` vs. `Set`), parser and tree construction edge cases, cross-spec companion PR review, PR scope discipline, and house style (rule IDs). Includes bundled helper scripts in [`skills/html-spec-review/scripts/`](skills/html-spec-review/scripts/):
  - `split_html.py`: Splits `whatwg/html`'s monolithic `source` file at `<h2>` boundaries into section files for targeted reading and editing, and concatenates them back.
  - `check_webidl.py`: Static analyzer for `<pre class="idl">` blocks.
  - `check_algorithms.py`: Static analyzer for `<div algorithm>` blocks and specification markup.
  - `check_wpt_coverage.py`: Audits modified specification sinks and thrown `DOMException`s against Web Platform Tests (WPT).

  Also includes [`html-style-guide.md`](skills/html-spec-review/html-style-guide.md), a de-facto house style guide for the HTML Standard's `source` with stable rule IDs, spec examples, and Modern/Accepted/Legacy/Obsolete rankings where the spec uses competing styles.

- **[`html-review-loop`](skills/html-review-loop/SKILL.md)**: Multi-agent review, implementation, option-branching, and fresh-context re-review loop for `whatwg/html` PRs and spec drafts. Orchestrates separate Reviewer, Implementer, and blind Re-Reviewer subagents so fixes do not introduce new review issues, branches competing design options into isolated git branches/worktrees for comparative re-review, and escalates genuine trade-offs or judgment calls to the user. Includes [`verify_branch.py`](skills/html-review-loop/scripts/verify_branch.py), which runs `check_webidl.py` and `check_algorithms.py` on complete enclosing `<div algorithm>` and `<pre class="idl">` blocks touched by a branch diff alongside optional local Wattsi builds and WPT coverage checks.

## Usage

Install the skills into your AI coding agent, e.g. using [`skills`](https://www.npmjs.com/package/skills):

```bash
npx skills add whatwg/spec-ai
```

Or reference [`skills/html-spec-review/SKILL.md`](skills/html-spec-review/SKILL.md) directly in your agent's project rules or system instructions.
