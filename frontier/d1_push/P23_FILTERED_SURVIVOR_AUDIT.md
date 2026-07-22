# Exact p=23 audit of the Cartier survivor boundary

**Date:** 2026-07-22  
**Status:** exact finite computation.  
**Scope:** verifies the actual Cartier determinant coefficients above the proposed survivor boundary at `p=23`. It does not yet identify a unique tropical assignment or prove the general filtered-minor lemma.

## 1. Why p=23 is the first nontrivial audit point

For `p=23`, the proposed support boundary is

`(p^2-1)/2 = 264`.

The raw maximum-weight assignment bound for the full Cartier minor is `344`. Orthogonality survivors have

`K=alpha(p-1), L=beta(p-1), alpha,beta>=1`,

so their `(1,2)`-weights are multiples of `22`. The only possible survivor weights strictly above `264` and at most `344` are

`286, 308, 330`.

The proved `a`-grading law gives every individual survivor coefficient the form

`a(A+B chi(a))`.

It is therefore sufficient to test one square and one nonsquare value of `a`; the audit uses `a=1` and `a=5`.

## 2. Exact coefficient extraction

Work over

`F_529 = F_23[s]/(s^2-5)`.

Its multiplicative group has order `528`. The determinant has

`deg_t <= 344 < 528`,

under the substitution

`c=c0*t, d=t^2`,

and has

`deg_c <= 253 < 528`.

Thus multiplicative Fourier inversion has no aliasing.

For each nonzero `c0`, the code evaluates the complete `22 x 22` Cartier minor for every nonzero `t in F_529` and extracts the exact coefficient of `t^w` by

`[t^w]P(t) = -sum_(t!=0) P(t)t^(-w)`.

A second Fourier inversion in `c0` extracts

`[c^(22 alpha)d^(22 beta)] det(I-H)`

for every pair satisfying

`22 alpha + 44 beta = w`.

All field arithmetic and Gaussian elimination are exact.

## 3. Result

For both `a=1` and `a=5`, every candidate coefficient at weights

`286, 308, 330`

is zero. There are `38` independent coefficient checks in total:

- `19` for the square class;
- `19` for the nonsquare class.

Therefore:

### Theorem P23A.1 — finite p=23 support verification

At `p=23`, every orthogonality-surviving Cartier coefficient with

`alpha+2 beta > 12`

vanishes. Equivalently, the proposed support law

`alpha+2 beta <= 12 = (p+1)/2`

holds exactly for both nonzero square classes of `a`.

## 4. What this does and does not prove

This audit establishes the substantive p=23 cancellation directly at the level of the full determinant polynomial. It is stronger than checking one selected alternant, because it includes every permutation, identity choice, and `w=1,2,3,4` contribution.

It does **not** yet reconstruct the specific leading assignment/alternant that motivated the original status sentence. That witness remains useful for the intended general proof through binomial determinants and factorial Schur functions, but it is no longer needed to decide whether the p=23 cancellation itself is real.

The general modular filtered-minor lemma remains open.

## 5. Reproducibility

Files:

- `p23_filtered_survivor_audit.cpp`
- `p23_filtered_survivor_audit_results.json`

The committed run used Hugging Face job `6a61048b13e6ef894d54c19f` on `cpu-xl`. Compilation plus the full exact audit completed successfully; the compute phase took approximately seven seconds.
