---
name: html-review-loop
description: >-
  Multi-agent review, implementation, option-branching, and fresh-context re-review loop for WHATWG HTML Standard (`whatwg/html`) pull requests and spec changes. Use when reviewing and polishing an HTML spec PR or draft so that fixes do not introduce new review issues, when comparing multiple spec design options across branches, or when preparing a `whatwg/html` PR for human editor review.
---

# Agent Skill: HTML Spec Multi-Review & Implementation Loop

This skill defines an iterative, multi-agent workflow for reviewing, fixing, branching, and re-reviewing changes to the [WHATWG HTML Standard (`whatwg/html`)](https://github.com/whatwg/html) until a fresh reviewer finds zero remaining issues.

It builds directly on [`../html-spec-review/SKILL.md`](../html-spec-review/SKILL.md) and [`../html-spec-review/html-style-guide.md`](../html-spec-review/html-style-guide.md).

---

## 1. Purpose & Core Principles

Fixing a specification review comment frequently introduces a *new* issue: a dangling variable reference, a broken `data-x` cross-reference, an unintended interaction with another algorithm step, or a house-style violation. Furthermore, an agent that authored or suggested a fix suffers from confirmation bias when checking its own work.

To prevent sending a PR to a human reviewer only to uncover new issues, this workflow enforces five rules:

1. **Role Separation with Fresh Contexts**:
   - **Orchestrator**: Coordinates subagents, manages git branches/worktrees, runs verification gates, and asks the user when judgment calls are required.
   - **Reviewer (`Reviewer_N`)**: A read-only subagent that reviews the PR using `html-spec-review`.
   - **Implementer (`Implementer_N`)**: A write-enabled subagent that applies fixes, creates git branches/worktrees for competing options, updates companion WPT tests, and runs static/build checks.
   - **Re-Reviewer (`Reviewer_N+1`)**: A **brand-new** read-only subagent instance with **zero conversation history from prior rounds**. Never reuse `Reviewer_N` to check `Implementer_N`'s work.
2. **Full Cumulative Diff Review (`base..head`)**:
   - Every Re-Reviewer must inspect the **entire PR diff against the base branch** (`base..branch_head`), not just the incremental fix commit from the previous round. Incremental diffs hide interactions between the new fix and earlier changes in the PR.
3. **Branch Viable Options, Then Re-Review**:
   - When a review finding has multiple plausible solutions (e.g., a localized guard vs. refactoring a shared algorithm, or two ways to structure state), the Implementer implements each viable option on its own git branch/worktree. A fresh Re-Reviewer evaluates every branch before pruning or escalating to the user.
4. **Automated Verification Gates on Every Iteration**:
   - Every candidate branch must pass:
     1. Static analyzers (`check_webidl.py` and `check_algorithms.py`) on complete enclosing `<div algorithm>` and `<pre class="idl">` blocks via [`scripts/verify_branch.py`](scripts/verify_branch.py).
     2. Local Wattsi spec build (when `html-build` / `wattsi` is available).
     3. Companion Web Platform Tests (WPT) updates and coverage checks (when a local WPT checkout is linked and normative behavior changes).
5. **Escalate Genuine Judgment Calls to the User**:
   - Never silently guess on controversial web-exposed semantics, unresolved trade-offs between surviving branches, or disagreements between Reviewer rounds. Present the surviving options, their concrete spec diffs, and the Re-Reviewer's assessment to the user.

---

## 2. Workflow Overview

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 0: Setup & Baseline Verification                      │
│   Identify base_ref, html repo, html-build, and WPT repo.   │
│   Run verify_branch.py on base_ref..HEAD.                   │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Phase 1: Initial Review (Fresh Subagent: Reviewer_1)        │
│   Reviews full diff (base_ref..HEAD) via html-spec-review.  │
│   Categorizes each finding:                                 │
│     • CANONICAL (1 obvious fix)                             │
│     • MULTI_OPTION (2+ viable spec/algorithmic approaches)  │
│     • USER_JUDGMENT_UPFRONT (pure product/API intent call)  │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
            ┌────────────────────────────────────┐
            │ Zero substantive / high-confidence │───Yes──► DONE
            │ editorial or style issues?         │
            └──────────────────┬─────────────────┘
                               │ No
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Phase 2: Implementation & Branching (Implementer_N)         │
│   1. If USER_JUDGMENT_UPFRONT exists, ask user first.       │
│   2. Apply all CANONICAL fixes to shared round base commit. │
│   3. For MULTI_OPTION findings, branch into isolated        │
│      git branches/worktrees (opt-a, opt-b, ...), implement  │
│      each option, update WPTs if needed, and run            │
│      verify_branch.py + Wattsi build on each branch.        │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Phase 3: Fresh Re-Review (Brand-New Subagent: Reviewer_N+1) │
│   Reviews full cumulative diff (base_ref..opt_head) of      │
│   each candidate branch with zero prior-round bias.         │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Phase 4: Prune & User Judgment Gate                         │
│   • Auto-prune branches that introduce new bugs or fail     │
│     re-review when another branch passes cleanly.           │
│   • If 2+ branches survive with trade-offs, or agents       │
│     disagree (ping-pong), ask user with diffs & verdicts.   │
│   • Advance working branch to selected branch; repeat loop. │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Protocol

### Phase 0: Setup & Baseline Verification

1. **Locate Repositories & Base Ref**:
   - Identify the `whatwg/html` checkout directory (`<html-dir>`), the current branch (`<orig-branch>`), and the PR base commit or branch (`<base-ref>`, e.g. `origin/main` or the PR's `baseRefOid`).
   - Check if `<html-dir>` lives inside an `html-build` workspace (e.g. `<html-dir>/../build.sh`) and whether a companion WPT checkout exists (e.g. sibling `wpt/` directory or linked WPT PR).
   - Ensure the working tree is clean (`git status --porcelain`) and no leftover `<html-dir>/split_source/` directory exists.

2. **Run Baseline Verification**:
   Run [`scripts/verify_branch.py`](scripts/verify_branch.py) to run `check_webidl.py` and `check_algorithms.py` on all complete `<div algorithm>` and `<pre class="idl">` blocks touched by `<base-ref>..HEAD`:
   ```bash
   python3 <loop-skill-dir>/scripts/verify_branch.py <html-dir> \
     --base <base-ref> \
     --head HEAD \
     --build \
     --wpt-dir <wpt-dir>
   ```
   *(Omit `--build` or `--wpt-dir` if not present locally.)*

---

### Phase 1: Initial Review (`Reviewer_1` Subagent)

Spawn a **fresh read-only Reviewer subagent** (`Reviewer_1`). Pass it:
- The paths to [`../html-spec-review/SKILL.md`](../html-spec-review/SKILL.md) and [`../html-spec-review/html-style-guide.md`](../html-spec-review/html-style-guide.md) (instructing it to read both first).
- The `<html-dir>`, `<base-ref>`, `<head-ref>`, any companion `<wpt-dir>`, and the output of `verify_branch.py`.
- Instructions to return findings in the following structured format:

#### Reviewer Finding Schema
For each finding, `Reviewer_N` must provide:
- **`id`**: Short identifier (e.g., `R1-1`, `R1-2`).
- **`severity`**:
  - `SUBSTANTIVE`: Normative logic bug, security/sanitizer bypass, crash/assertion failure, broken edge case, race/reentrancy bug, or WPT mismatch.
  - `EDITORIAL_HIGH`: Broken `data-x` cross-reference, variable lifecycle/scope defect (`Let` vs. `Set`, unbound variable in outer scope, unused variable), invalid Web IDL markup, inaccurate/stale note, or clear violation of an `html-style-guide.md` rule on new normative text.
  - `NIT`: Minor wording or formatting suggestion.
- **`location`**: File and line range in `source` (plus algorithm/section name).
- **`problem`**: Step-by-step trace or explanation of why the current spec text fails.
- **`resolution_type`**:
  - `CANONICAL`: There is one clear, non-controversial way to fix this issue. Provide the exact proposed edit.
  - `MULTI_OPTION`: There are 2+ viable technical/structural ways to resolve this issue (e.g., Option A: localized check at call site; Option B: refactor shared algorithm primitive), and implementing them will clarify their complexity and side effects. Describe each option clearly.
  - `USER_JUDGMENT_UPFRONT`: The issue cannot be resolved without a product/API design decision from the user (e.g., whether an API should throw vs. no-op, or what web-exposed order of events is desired).

> **Scope Discipline**: Remind `Reviewer_N` of `html-spec-review` §4 and `calibration/2026-10-13.md`: style rules apply **only to new or rewritten normative text** in `<base-ref>..HEAD`, not to unchanged context, notes/examples, or legacy algorithms where a single step was inserted matching existing local style.

---

### Phase 2: Implementation & Option Branching (`Implementer_N` Subagent)

1. **Upfront User Judgment Calls (if any)**:
   - If `Reviewer_N` flagged any `USER_JUDGMENT_UPFRONT` items where web-exposed behavior intent is ambiguous, ask the user before implementing.

2. **Apply `CANONICAL` Fixes First**:
   - Create a round base branch from the current head:
     ```bash
     git -C <html-dir> checkout -B review-loop/round-N-base <current-head>
     ```
   - Have the `Implementer_N` subagent apply all `CANONICAL` fixes onto `review-loop/round-N-base`:
     - For edits in `source`, use `split_html.py` from `../html-spec-review/scripts/split_html.py` when working on large sections, and **always** run `split_html.py concat` and remove `split_source/` afterward.
     - Run `verify_branch.py` (with `--build` and `--wpt-dir` if applicable) and commit the canonical fixes to `review-loop/round-N-base`.

3. **Branch & Implement `MULTI_OPTION` Findings**:
   - If there are no `MULTI_OPTION` findings, `review-loop/round-N-base` is the single candidate branch for Phase 3.
   - If there are `MULTI_OPTION` findings with options $A, B, \dots$:
     - Create an isolated branch (and, if running parallel Implementer subagents, a separate git worktree or subagent `Workspace: "share"` / `"branch"`) for each option starting from `review-loop/round-N-base`:
       ```bash
       git -C <html-dir> worktree add /tmp/html-opt-a -B review-loop/round-N-opt-a review-loop/round-N-base
       git -C <html-dir> worktree add /tmp/html-opt-b -B review-loop/round-N-opt-b review-loop/round-N-base
       ```
     - In each branch, the Implementer subagent:
       1. Implements the option cleanly in `source`, following all rules in `html-spec-review`.
       2. Updates or adds WPT tests in `<wpt-dir>` if the option affects web-exposed normative behavior or adds a newly discovered edge case.
       3. Runs `verify_branch.py` (static analyzers + Wattsi build + WPT coverage check) and resolves any analyzer or Wattsi build errors before committing.

---

### Phase 3: Blind Fresh-Context Re-Review (`Reviewer_N+1` Subagent)

Spawn a **brand-new read-only Reviewer subagent** (`Reviewer_N+1`).

- **Why a brand-new subagent?**
  - `Reviewer_N` is anchored to its own suggestions and may overlook bugs in the fix it proposed.
  - `Implementer_N` is anchored to the code it just wrote.
  - `Reviewer_N+1` starts with a clean slate and reviews the PR as if a new human editor just opened it on GitHub.

- **What to pass `Reviewer_N+1`**:
  - The paths to `../html-spec-review/SKILL.md` and `../html-spec-review/html-style-guide.md`.
  - The **full cumulative diff** from `<base-ref>` to each candidate branch head (`<base-ref>..review-loop/round-N-opt-a`, etc.), **plus** the list of original findings from Round $N$ so it can verify each was resolved.
  - Ask `Reviewer_N+1` to evaluate each candidate branch on:
    1. **Resolution completeness**: Are all Round $N$ findings fully resolved?
    2. **Zero regressions / new issues**: Does the cumulative diff `<base-ref>..branch_head` have *any* substantive, algorithmic, cross-reference, or house-style issues (whether newly introduced by the fix or previously missed)?
    3. **Comparative quality (when multiple option branches exist)**: Compare the candidate branches on correctness, minimal invasiveness, readability, and adherence to HTML Standard idioms.

---

### Phase 4: Pruning, Judgment Calls, and User Escalation

1. **Auto-Prune Dominated Branches**:
   - If Option A passes `Reviewer_N+1` with zero new issues and clean spec prose, while Option B introduces new edge-case bugs, fails Wattsi/static checks, or requires convoluted state tracking flagged by `Reviewer_N+1`, automatically discard Option B and select Option A.

2. **Ask the User When a Judgment Call Remains**:
   Consult the user whenever any of the following hold:
   - **Multiple candidate branches survive re-review with genuine trade-offs**:
     - For example, Option A is a minimal 3-line guard at the call site, while Option B refactors a shared parser algorithm to enforce the invariant structurally; or Option A and Option B have subtly different web-exposed edge-case behavior.
     - Present the user with:
       1. A brief summary of the trade-off.
       2. The concrete diff (or key snippet) from each surviving branch.
       3. `Reviewer_N+1`'s assessment of each branch.
       4. A recommended choice (`(Recommended)`).
   - **Agent Disagreement / Ping-Pong Detected**:
     - If `Reviewer_N+1` flags a change that `Implementer_N` made specifically to satisfy `Reviewer_N` (or recommends reverting back toward the Round $N-1$ state), **stop immediately and ask the user**. Never let subagents ping-pong across rounds.
   - **Scope Expansion Questions**:
     - If fixing an issue properly requires touching an algorithm outside the PR's original scope or changing existing WPT expectations, confirm with the user.

---

### Phase 5: Convergence & Cleanup

1. **Check Stopping Criteria**:
   - The loop converges when a fresh `Reviewer_K` reviews `<base-ref>..selected_branch` and reports:
     - **0 `SUBSTANTIVE` issues**
     - **0 `EDITORIAL_HIGH` issues**
     - **`verify_branch.py` (WebIDL + Algorithm static checks + Wattsi build + WPT check) passes with 0 errors**
   - Cap the loop at a maximum of **3 review-implement-rereview rounds**. If any issue remains unresolved after 3 rounds, stop and present the remaining item(s) to the user.

2. **Finalize & Clean Up**:
   - Update `<orig-branch>` to the winning branch state (either as clean incremental fixup commits or as requested by the user).
   - Remove any temporary git worktrees (`git worktree remove ...`) and temporary `review-loop/*` branches (`git branch -D ...`).
   - Verify `git status` is clean and no `split_source/` directory remains.
   - Present a concise final report summarizing:
     - All issues fixed across rounds
     - Any multi-option branches explored and how they were resolved
     - Verification status (`check_webidl.py`, `check_algorithms.py`, Wattsi build, WPT tests)
