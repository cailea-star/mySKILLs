---
name: scientific-code-review-and-minimal-fix
description: Review or minimally fix scientific and numerical code changes. Use when the user asks to inspect a diff, staged changes, recent edits, failing builds, failing tests, or suspicious numerical behavior in code; when they say "检查", "review", "先不要修改", "跑通", "修复", "尽可能少改"; or when Codex needs to find real behavior risks, establish a narrow feedback loop, and make the smallest safe code fix only when requested.
---

# Scientific Code Review and Minimal Fix

## Purpose

Use this skill to review or minimally fix scientific, numerical, or research-code changes while preserving the user's work.

The core questions are:

```text
Does this code change introduce a real behavior risk?
If a fix is requested, what is the smallest correct change?
What is the narrowest runnable feedback loop that verifies the risk or fix?
How can the fix be verified with targeted tests?
```

## Mode Decision

Choose the work mode from the user's wording before editing files.

Use review mode when the user says:

- "检查"
- "看看有没有问题"
- "review"
- "检查 staged diff"
- "先不要修改"
- "只分析"

In review mode, do not edit files. Report findings first, ordered by severity, with file and line references.

Use minimal-fix mode when the user says:

- "修复"
- "跑通"
- "整一下"
- "尽可能少改"
- "让它能运行"
- "直接改"

In minimal-fix mode, edit only the directly relevant code and tests, then verify.

If the user asks a theory-level question, route to a theoretical audit before touching code.

## Review Workflow

### 1. Inspect state and scope

Start with the repository state:

- Read `git status`.
- Distinguish staged, unstaged, and untracked changes.
- Identify files touched by the user.
- Avoid reverting or overwriting user changes.
- Read nearby context, not only the diff.

When reviewing staged changes, use staged diff commands first. When the worktree is clean, inspect the current implementation directly.

### 2. Establish the narrowest feedback loop

Before reasoning deeply, build the smallest runnable signal that can confirm or reject the suspected risk:

- A focused build target when the concern is compile-time or link-time behavior.
- The smallest test that reaches the changed numerical path.
- A direct executable, fixture, or CLI run when runtime assertions, dynamic matrix shapes, or input parsing matter.
- A reference comparison when the change affects formulas, observables, normalization, or decomposed numerical terms.
- A downstream caller run when a reusable utility's public contract may have changed.

Prefer a loop that is fast, deterministic, and specific to the user's reported symptom. If no useful loop exists, say what was tried and keep the risk classification conservative.

Reconfigure first when build-system source lists may be stale.

### 3. Prioritize real behavior risks

Look first for issues that can break correctness or execution:

- Compile errors.
- Runtime crashes or assertions.
- Matrix, tensor, or array shape mismatches.
- Out-of-bounds access, division by zero, NaN, infinities.
- Real/complex type mismatches and template-instantiation failures.
- Incorrect units, normalization, coefficients, signs, or reference frames.
- Wrong inner product convention for complex numerical methods.
- Cached parameters or stale generated data during scans.
- Public APIs whose preconditions are enforced only by `assert`.
- New code paths not reached by existing tests.

Avoid spending review space on style unless it affects correctness, maintainability of the changed logic, or future bug risk.

### 4. Report findings first

For review mode, lead with findings:

```text
Findings
- P1 file:line - Problem. Explain the failure mode and why it matters. Suggest a concrete fix.
- P2 file:line - Problem. Explain residual risk or missing test coverage.

Validation
Commands run and outcomes.

Open questions
Any assumptions needed to finish safely.
```

If no issues are found, say that clearly and mention the tests run and remaining test gaps.

## Minimal-Fix Workflow

### 1. Establish the blocking feedback loop

Before editing, reproduce the failure or build the narrowest useful command that exercises the blocking path. The loop should prove that the current behavior fails and later prove that the fix addresses the same behavior.

If reproduction is expensive, minimize the loop before changing code. If the issue is non-deterministic, raise the reproduction rate with repeated runs, fixed seeds, smaller fixtures, or isolated inputs until the result is useful for debugging.

### 2. Make the smallest scoped change

Edit only what is needed to fix the verified problem:

- Prefer local fixes over broad refactors.
- Keep existing APIs and style unless they are the source of the bug.
- Do not rewrite surrounding code for taste.
- Do not fold unrelated cleanup into the fix.
- Preserve user changes and staged state.

If the problem is actually a theory mismatch rather than an implementation bug, stop and explain the mismatch instead of forcing a code patch.

### 3. Add or adjust focused tests

Scale tests to risk:

- For a utility function, add or adjust a local unit test.
- For matrix or numerical code, run a path that actually constructs and uses the object.
- For reference comparisons, verify the key observables or decomposed terms.
- For shared logic, run at least one adjacent regression test.

Prefer tests that would have caught the bug.

### 4. Verify and inspect the diff

After edits:

- Rerun the original feedback loop.
- Run any added or adjusted regression tests.
- Inspect the diff to confirm no unrelated changes were introduced.
- Report any tests that could not be run.

## Response Shape

For minimal fixes, close with:

```text
Changed:
- file: what changed and why

Verified:
- command/result

Residual risk:
- any remaining uncertainty
```

Keep the final explanation concise. Include exact numerical outcomes when they matter.

## Boundaries

Do not use this skill to decide whether a scientific theory is correct; use a theoretical correctness audit first.

Do not use this skill as a broad refactoring mandate. If a larger redesign is needed, explain why and ask for direction unless the user has already requested it.

Do not silently change generated files, build artifacts, formatting, or unrelated metadata.

## Common Patterns

### Staged diff review

Inspect staged changes, run a focused build/test if feasible, then report findings first. Do not modify files unless the user asks.

### "It does not run"

Reproduce the build or runtime failure, fix the first blocking issue minimally, then rerun the narrow target. Continue only if the next failure is on the same requested path.

### Numerical output changed

Compare current output to the previous expected behavior, identify which component changed, and decide whether this is implementation behavior or a theory/model change.

### Header-only numerical utility

Check template instantiation for real and complex types, release behavior without `assert`, minimum sizes, uniform-grid assumptions, and API compatibility.
