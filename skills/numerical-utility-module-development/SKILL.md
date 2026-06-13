---
name: numerical-utility-module-development
description: Add, extend, review, or minimally fix reusable numerical and scientific utility modules in a C++ tools library. Use when implementing derivative, integration, root-finding, minimization, shooting, ODE, basis, kernel, interpolation, or math-helper functionality; when designing scalar/vector/function/template API variants; or when validating module-local tests plus downstream numerical callers.
---

# Numerical Utility Module Development

## Purpose

Use this skill to add or extend reusable numerical utility modules in a scientific C++ tools library.

The core workflow is:

```text
Assess whether the module needs a concise mathematical formula-summary Markdown note.
Define the mathematical object and API semantics.
Work in feature micro-slices before committing to abstractions.
Implement the smallest module consistent with the existing library style.
Add focused module tests and downstream caller tests.
Check templates, complex support, boundary behavior, and API compatibility.
```

This is not a generic "write a function" workflow. Treat each utility as a reusable numerical component with explicit assumptions and tests.

## Workflow

### 0. Assess documentation need

Before designing or editing code, decide whether the module needs a new or updated `.md` formula-summary note.

Write or update documentation when any of these are true:

- The implementation has nontrivial mathematical formulas, physical conventions, or numerical assumptions behind it.
- The public API encodes physical conventions, normalization, boundary conditions, quantum labels, selection rules, transforms, or units that are easy to misuse.
- The module wraps several lower-level algorithms into a higher-level workflow, such as shooting, basis construction, kernels, matrix elements, or samplers.
- The code contains formula-heavy comments that would be clearer as a module-level explanation.
- Existing nearby modules already have `.md` formula-summary notes and the new module is comparable in complexity.

Usually skip a standalone `.md` note for simple glue, constants, string utilities, or short wrappers whose behavior is fully obvious from function-level comments.

When documentation is needed:

- Read existing `.md` files first and match their style.
- Write a concise mathematical formula summary, not a broad theory tutorial.
- Make the first screen show the module's main implemented formulas and the mathematical objects they map between.
- Prefer formulas, symbol definitions, physical/numerical conventions, selection rules, normalization factors, and boundary assumptions that are directly implemented by the code.
- Avoid long derivations, elementary numerical-method explanations, API tables, build instructions, and examples unless they are needed to prevent misuse.
- Mention class or function names lightly, inline with the formulas they compute. Do not add a separate interface mapping section unless the user asks for it.
- For simple formula modules, document only the few formulas already implicit in comments. For deeper modules, include only enough intermediate algebra to justify non-obvious reductions, then return to the final implemented formulas.

Formula-summary document style:

- Optimize for recognition, not teaching. A reader should see within the first screen what formulas the code implements.
- Start with the module scope, then show the 2-5 central equations or mappings.
- Define only the symbols and conventions needed to use those equations correctly.
- Put function or class names next to the formulas they compute, instead of creating a separate interface table.
- Mention elementary numerical methods, such as Simpson, trapezoidal, bisection, or RK4, in one sentence when the formula already makes the computation obvious.
- Do not expand standard derivations, examples, build commands, or API inventories unless the user explicitly asks for them.

### 1. Define the mathematical object

Before editing code, state what the module computes:

- The mathematical object: derivative, integral, root, minimum, ODE step, matching residual, basis value, kernel, interpolation, transform, etc.
- Inputs and outputs.
- Scalar, vector/list, function-object, and matrix variants.
- Real, complex, and template type requirements.
- Assumptions about grids, spacing, normalization, boundary conditions, and convergence.
- Whether discrete labels such as node count, angular momentum, order, or mode index are hard constraints.

If the user asks for formal theory first, provide symbols, indices, definitions, and the numerical method before implementing code.

### 2. Read the existing library style

Inspect nearby modules before designing the new one:

- Naming conventions in `source/`.
- Header-only vs `.cpp` implementation style.
- Test style in `test/`.
- Existing helper aliases, constants, matrix/vector types, and function typedefs.
- CMake behavior, especially whether source files are globbed or explicitly listed.
- Current downstream callers that may depend on the old API.

Use existing patterns unless the requested feature truly requires a new one.

### 3. Feature Micro-Slice Gate

For each new numerical feature, work in small vertical slices.

Keep each feature slice under 100 lines of new production code:

- Exclude tests, fixtures, and formula-summary documentation from this limit.
- If the feature needs more than 100 lines, split it into smaller vertical slices before implementing.
- After each slice, explicitly decide whether to add, update, or skip tests, and state why.

Test public behavior, not implementation details:

- Prefer tests against public APIs, analytic functions, invariants, conservation or normalization properties, reference values, and downstream caller behavior.
- Avoid tests that duplicate private helper logic or assert internal step ordering unless that behavior is part of the public contract.

Prefer one vertical slice before abstraction:

- First run one real calculation path from input to observable output.
- Make the streaming or data-flow computation work in the simplest direct form.
- Only after the behavior is verified, extract wrappers, abstractions, or reusable layers.

### 4. Design layered APIs

Sketch clear target layers, but do not implement every wrapper up front:

```text
core single-point computation
vector/list wrapper
function-object wrapper
convenience double wrapper
legacy compatibility wrapper, when needed
```

Run one real vertical slice first, then add only the layer needed by the next public use case. For example, implement or verify the scalar derivative behavior before adding a full-vector wrapper, and make the vector routine call the scalar routine so endpoint and stencil logic lives in one place.

Keep old APIs working unless the user explicitly asks to remove or rename them.

### 5. Make assumptions executable

Keep precondition checks basic, local, and lightweight. Use `assert` for core developer-facing assumptions:

- Minimum input size.
- Equal vector lengths.
- Uniform-grid assumptions.
- Nonzero step sizes or denominators.
- Valid endpoint or boundary-mode requirements.

Keep constraint checks out of the main mathematical body when practical:

- Put compact assertions at the top of the function.
- Prefer a small local validation helper when several overloads share the same checks.
- Do not spread repetitive checks through the calculation loop.
- Do not build a broad runtime validation layer unless the public API explicitly requires it.

The function body should make the numerical formula easy to see. Preconditions should protect the formula, not obscure it.

### 6. Implement the smallest coherent change

Edit only the target module, direct callers, and focused tests:

- Put template implementations in headers.
- Use typed constants such as `T(8.0)` when supporting `std::complex<T>` or generic `T`.
- Avoid duplicated formulas across overloads.
- Avoid broad refactors, unrelated cleanup, or new abstractions that are not needed for the module.
- Preserve user changes and staged state.

If a build fails because CMake cached a deleted or moved source file, reconfigure before treating the source as broken.

### 7. Test locally and downstream

Test the module itself and at least one relevant downstream caller when the utility is shared:

- Compile the module test target.
- Run the module test executable.
- Compile and run downstream tests that instantiate the new templates or use the new API.
- Include real and complex/template paths when relevant.
- Include endpoint, boundary, or invalid-input behavior when relevant.

After each feature slice, explicitly decide whether to add, update, or skip tests, and state the reason.

Test public behavior, not implementation details:

- Prefer analytic functions, invariants, conservation or normalization properties, reference values, and downstream caller behavior.
- Avoid tests that mirror private helper logic or assert internal step ordering unless that ordering is part of the public contract.
- When testing invalid inputs, use the project's existing assert or death-test style if available. If not available, do not add heavy runtime error handling only for testability; state that invalid inputs are developer preconditions guarded by `assert`.

For example, after changing a derivative utility used by shooting methods, test both derivative and shooting paths.

### 8. Review the diff and report risk

Before finishing:

- Inspect the diff for unintended API breaks or unrelated edits.
- Confirm that compatibility wrappers remain if needed.
- Report commands run and outcomes.
- State residual risk, especially if only debug assertions protect a public API or if release behavior remains unchecked.

## Common Patterns

### Adding a vector/list interface

Implement or verify the single-point routine first, then make the vector routine call it for each index. Keep endpoint logic centralized.

### Supporting templates and complex values

Avoid integer-left multiplication with generic complex types. Prefer:

```cpp
T(8.0) * value
```

over:

```cpp
8 * value
```

Also verify that tests instantiate the complex path, not only `double`.

### Handling node counts or mode labels

Treat node count and similar discrete labels as hard constraints, not soft penalties mixed into a continuous loss unless there is a strong reason. Restrict the search interval or candidate set first, then optimize the continuous residual inside it.

### Preserving convenience calls

When a template function breaks old function-pointer or `double` calls, add a non-template wrapper or overload if the user has not asked to remove the old API.

### Uniform-grid utilities

If the implementation uses uniform finite-difference formulas, add checks for equal spacing, equal lengths, minimum size, and nonzero spacing. If nonuniform grids are required, use local interpolation weights instead.

## Response Shape

For planning:

```text
Documentation need:
    ...

Mathematical object:
    ...

API layers:
    ...

Feature slice:
    ...

Existing style:
    ...

Tests needed:
    ...

Risks:
    ...
```

For implementation:

```text
Changed:
    ...

Documentation:
    ...

Test decision:
    ...

Verified:
    ...

Residual risk:
    ...
```

Keep explanations focused on the module's numerical semantics, API compatibility, and verification.

## Boundaries

Use a theoretical correctness audit first if the requested module's mathematical formulation is unclear or contested.

Use scientific code review mode if the user asks only to inspect a change and explicitly says not to modify files.

Use reference-code reproduction when the module is being ported from a standard implementation and intermediate reference tests need to be extracted first.
