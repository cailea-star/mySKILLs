---
name: theoretical-correctness-audit
description: Judge whether a scientific model, physics formalism, numerical scheme, or proposed computation is theoretically well-posed before debugging or implementing code. Use when the user asks to reason from theory or formalism, asks "先讨论形式理论" or "理论上是否正确", wants to decide what mathematical problem should be solved, or needs to determine whether surprising numerical results indicate a theoretical problem rather than a code bug.
---

# Theoretical Correctness Audit

## Purpose

Use this skill to audit whether a scientific computation is correctly posed at the theory level before moving into numerical debugging or code review.

Answer the upstream question first:

```text
Is the mathematical or physical problem itself correctly defined?
If implemented perfectly, would this computation produce the observable the user actually wants?
```

Do not start from the existing code structure. Start from the target physical or mathematical question, then compare the proposed workflow or code path against it.

## Workflow

### 1. State the target question

Clarify the intended problem in theory-level terms:

- Identify the desired observable or prediction.
- Identify experimental inputs, model parameters, fitted parameters, and unknowns.
- Identify what should be compared with data.
- Separate quantities that are given from quantities that must be solved for.

If the user has not specified enough information to define the problem, say exactly what is missing and why it matters.

### 2. Write the minimal theoretical object

Express the problem using the smallest adequate formal object:

- Hamiltonian, energy functional, action, transition kernel, likelihood, or response function.
- State space, basis space, channel space, projection space, or model space.
- Boundary conditions, normalization, symmetry constraints, and conserved quantities.
- Observable definition and the mapping from solution to observable.

Keep this formalization compact. The goal is to expose the structure of the problem, not to reproduce a textbook derivation.

### 3. Classify the mathematical problem type

Decide what kind of problem should be solved:

- Eigenvalue problem.
- Fixed-energy boundary-value problem.
- Scattering or decay problem with outgoing boundary conditions.
- Variational or constrained minimization problem.
- Projection-after-variation or variation-after-projection problem.
- Perturbative correction.
- Basis expansion and matrix rediagonalization.
- Inverse problem or parameter-fitting problem.

Many theory errors come from solving the wrong problem type. Call this out directly when it happens.

### 4. Check theoretical closure

Audit whether the theory chain is self-contained:

- Check whether the inputs are sufficient to define the calculation.
- Check whether energy references, thresholds, and zero points are consistent.
- Check whether symmetry assumptions are appropriate.
- Check whether projection, variation, perturbation, and truncation are applied in the right order.
- Check whether the basis or model-space truncation is compatible with the target observable.
- Check whether boundary conditions correspond to the intended physical state.
- Check whether the observable definition follows from the solved object.

This step judges self-consistency, not numerical accuracy.

### 5. Look for object mismatches

Actively search for mismatches between mathematical objects. Common high-risk mismatches include:

- Total energy vs channel energy.
- Scalar potential vs coupled-channel potential matrix.
- Hamiltonian eigenvalues vs experimentally specified decay energies.
- Energy functional vs mean-field potential.
- Unprojected state vs projected expectation value.
- Physical observable vs phase, gauge, or sign convention.
- Local density vs transition density vs projected density.
- Hermitian inner product vs complex-symmetric or Gamow c-product.
- Fixed model parameter vs parameter scanned or refit inside the workflow.

If two objects share a name but not a definition, treat that as a theory-level issue.

### 6. Compare the existing workflow to the target theory

If a code path, algorithm, or proposed workflow already exists, identify what mathematical problem it actually solves:

- Describe the actual solved problem in theory language.
- Compare it to the target problem.
- Decide whether the two are equivalent, approximate, or different.
- Explain whether the difference changes the physical meaning of the output.

Use code only as evidence for the implemented theory. Do not turn this into a line-by-line code review unless the user asks.

### 7. Give a theory-level verdict and route

End with a clear classification:

- The theory is well-posed; the next step is numerical debugging or implementation.
- The theory is plausible only within a stated approximation regime.
- The theory is underdefined; specific missing inputs or definitions are required.
- The theory is misposed; the proposed workflow solves a different mathematical problem.
- The result may be a false agreement due to cancellation between mismatched terms.

Then give the corrected theory workflow, including what existing pieces can remain as diagnostics or auxiliary tools and what should not remain in the main physics pipeline.

## Response Shape

Prefer this structure for substantial audits:

```text
Target theory problem:
    ...

Minimal formal object:
    ...

Current/proposed workflow actually solves:
    ...

Key differences:
    1. ...
    2. ...

Theory-level verdict:
    ...

Recommended theory workflow:
    ...

Next step:
    ...
```

For small questions, compress the same logic into a few paragraphs.

## Boundaries

Use code review only after the theory target is accepted or when the user explicitly asks for code review.

Use numerical debugging only after confirming that the solved mathematical problem is the intended one.

Use paper-reading workflows when the primary task is to summarize a paper. Use this skill when the task is to judge whether a formalism or paper method applies to the user's current problem.

## Common Verdict Patterns

### Theory correct, implementation uncertain

State that the formal problem and observable definition are self-consistent, then route to numerical debugging or code review.

### Approximation valid only in a regime

State the assumptions under which the formalism is valid, then identify which target observables are sensitive to neglected terms.

### Wrong problem type

Explain the mismatch plainly. For example, a fixed-energy decay or scattering problem is not generally equivalent to diagonalizing a small Hamiltonian matrix.

### Object mismatch

Identify the mismatched objects and explain why agreement in one total number is insufficient. Recommend comparing decomposed kernels, terms, or observables.

