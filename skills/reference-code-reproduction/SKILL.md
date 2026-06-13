---
name: reference-code-reproduction
description: Reproduce a trusted reference or legacy scientific code module by module, extracting intermediate diagnostics, implementing matching calculations in a new codebase, and building layered reference tests from low-level kernels to full-run observables. Use when porting, rewriting, validating, or incrementally reproducing standard scientific software; when the user asks which module to reproduce next; or when Codex needs to turn a reference implementation into a staircase of stable tests.
---

# Reference Code Reproduction

## Purpose

Use this skill to reproduce a trusted reference or legacy scientific code in a new implementation, one verifiable module at a time.

The core questions are:

```text
Which smallest reference-code module should be reproduced next?
What reference output proves that module is reproduced correctly?
How should that output become a stable test in the new codebase?
```

This skill is proactive. It is not only for explaining why two implementations differ after the fact; it is for planning and executing a reproduction ladder from low-level deterministic calculations to full-run observables.

## Workflow

### 1. Map the reference computation

Build a compact map of the reference code path before implementing:

- Input parsing and option switches.
- Derived parameters and constants.
- Grids, basis functions, quadrature, and normalization.
- Local kernels, nonlocal kernels, densities, fields, and matrix elements.
- Traces, energy components, residuals, and update equations.
- Iteration or solver state.
- Final observables and printed output.

Prefer dependency order over file order. The goal is to understand how information flows from input to output.

### 2. Choose the next reproducible module

Choose the next module by dependency and test value:

- Prefer deterministic low-level modules first.
- Prefer input-derived constants and geometry before iterative solvers.
- Prefer grids, basis, weights, and normalization before kernels.
- Prefer local kernels, traces, and matrix elements before full observables.
- Prefer one-step update tests before full self-consistent or full-run tests.
- Defer broad end-to-end reproduction until enough lower layers are pinned down.

Avoid reproducing a large coupled workflow when a smaller upstream module is still unverified.

### 3. Define the reference observable for that module

For each module, identify a concrete comparable output:

- What should the reference code print, dump, or expose?
- Where in the reference code is the value computed?
- What is the corresponding value or data structure in the new code?
- What tolerance is physically and numerically justified?
- Is the comparison scalar, vector, matrix, field, trace, or final observable?

If the reference code only prints final values, add a minimal diagnostic output or gated debug print that exposes the intermediate value without changing the calculation.

### 4. Extract reference data without changing semantics

When adding diagnostics to the reference implementation:

- Print only the values needed for the current module.
- Do not alter the computation path.
- Keep output stable enough for test fixtures or golden references.
- Prefer feature flags, environment variables, debug switches, or temporary patches that can be reverted.
- Record the exact input, reference version, and diagnostic location.

Treat reference data as evidence with provenance, not as anonymous hard-coded numbers.

### 5. Implement the matching module

In the new codebase:

- Match the reference module's mathematical object first.
- Preserve index ordering, units, normalization, boundary conventions, and sign conventions.
- Avoid compensating for upstream discrepancies inside a downstream module.
- Keep implementation scope limited to the chosen module.
- Add only the abstraction needed to express the matched calculation cleanly.

If a mismatch is discovered in the theory definition, pause and route to a theoretical correctness audit instead of forcing parity.

### 6. Build layered reference tests

Organize tests as a ladder:

```text
Level 0: input parsing and derived-parameter tests
Level 1: grid, basis, quadrature, and normalization tests
Level 2: local kernels, densities, fields, and nonlocal kernels
Level 3: matrix elements, traces, and energy-component tests
Level 4: one-step update or solver-state tests
Level 5: full-run observable and regression tests
```

Each new layer should make failures easier to localize than a full-run comparison alone.

### 7. Diagnose differences by layer

When values disagree, classify the first layer where divergence appears:

- Different input interpretation.
- Different derived constants or units.
- Different grid, basis, quadrature, or normalization.
- Different index ordering or tensor shape.
- Different integration weights or symmetry factors.
- Different real/complex, Hermitian, phase, or sign convention.
- Different state of the iteration or solver.
- Different observable or output convention.
- Different approximation or theory object.

Do not guess from final observables when an upstream module can be compared directly.

### 8. Promote tests carefully

Before calling a test a strict reference or golden test, confirm:

- The reference input is identical.
- Required physics or model switches are supported in the new implementation.
- The module comparison is at the same abstraction level.
- The tolerance is justified and documented.
- No unrelated error cancellation is hiding in the final value.

If a case uses unsupported options or intentionally different approximations, label it as smoke, diagnostic, or run-style reference rather than strict golden.

### 9. Record reproduction state

After each reproduced module, record:

- Reference code location.
- New implementation location.
- Reference data source and command.
- Test name and tolerance.
- Confirmed formulas, coefficients, units, signs, and conventions.
- Accepted differences, if any.
- Remaining uncovered modules or boundary cases.

Write short durable notes to the project agent document or a skill reference when the result will matter in future sessions.

## Response Shape

For planning the next reproduction step:

```text
Reference-code map:
    ...

Best next module:
    ...

Why this module:
    ...

Reference output needed:
    ...

Test to add:
    ...

Risks or prerequisites:
    ...
```

For implementation work:

```text
Reproduced module:
    ...

Reference data:
    ...

New implementation:
    ...

Tests:
    ...

Remaining reproduction ladder:
    ...
```

## Boundaries

Do not treat the reference implementation as automatically theoretically correct. If the reference workflow itself may be solving the wrong problem, route to a theoretical correctness audit.

Do not use final-observable agreement alone as proof of reproduction. Check decomposed or intermediate quantities when practical.

Do not broaden the task into a full rewrite without a module-by-module test plan.

## Common Patterns

### Standard-code port

Map the standard code, choose a low-level deterministic module, extract diagnostic output, implement the matching module, then add a reference test.

### Selecting the next test

Prefer the next unverified module that unlocks the most downstream checks while requiring the fewest unsupported features.

### Full-run mismatch

Move backward through the ladder until the first mismatching layer is found. Add a test at that layer before changing downstream code.

### Unsupported reference feature

Label the test as smoke or diagnostic. Do not claim strict golden parity until the missing feature is implemented and its lower-level tests pass.

