# d=1 collapse integration branch — terminal status

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-collapse-integration-20260723`  
**Base:** Claude branch head `7049d2b3b00b6f69ad22eafebe800be094b8f42d`  
**Scope:** function-field `d=1` Fortune sibling only.

## Selective integration

The histories were not merged wholesale. The following exact GPT-side notes were selectively preserved with provenance:

- `frontier/d1_push/WILD_TRACE_CUBIC_KUMMER_REDUCTION_THEOREM.md` from commit `2c7ad4018c6084e0f05888d66b43a0dd63892556`;
- `frontier/d1_halftheorem/FAST_COLLAPSE_AND_FERMAT_AUDIT.md` from commit `88c760155643045f1ffe74bb584a8eab1bb0cc1f`.

## Strongest new theorem

**PROVED:** for the rank-two cubic Airy sheaf `A`, the `p`-th Adams virtual representation

\[
\Psi^p(A)=\operatorname{Sym}^p A-\det(A)\otimes\operatorname{Sym}^{p-2}A
\]

has zero Swan conductor at infinity. On the quadratic inertia cover the two wild characters have order `p`, so the `p`-th Adams operation kills them exactly; the resulting local virtual character is an actual tame rank-two induced representation.

This proves genuine local virtual cancellation and exactly explains the equality of the two separate Swan conductors `(3p-3)/2`.

## Exact obstruction

**PROVED:** the local tame rank-two representative cannot be globalized naively. The geometric monodromy is `SL_2`, and the global Adams class is

\[
[\operatorname{Sym}^p]-[\operatorname{Sym}^{p-2}],
\]

which has a negative irreducible multiplicity. Thus virtual rank two and Swan zero imply only bounded virtual Euler characteristic, not bounded total global cohomology or bounded first Frobenius trace.

## Focused exact computation

**VERIFIED COMPUTATIONALLY:** `virtual_quotient_probe.py` reconstructs the two global Airy `L`-polynomials modulo split coefficient primes, using exact finite-field arithmetic, an exact finite Fourier transform and Newton identities.

Results:

- `p=5`: residual total degree `2`;
- `p=7`: residual total degree `4`;
- `p=11`: common-factor degree at most `1`, hence residual total degree at least `6`.

Therefore the proposed strengthening “at most four residual eigenvalues after common-factor cancellation” is false at `p=11`.

## Terminal classification

The absolute-constant estimate

\[
|T_p|\le C p^{(p-1)/2}
\]

is **OPEN**.

The smallest remaining theorem is the global cross-symmetric-power correlation estimate

\[
|\operatorname{Tr}(F_p|V_p)-\operatorname{Tr}(F_p|W_p)|
\le C p^{(p+1)/2}.
\]

Neither local monodromy, separate functional equations, GOS degrees, purity nor common-factor cancellation through four residual eigenvalues can supply it.

This branch therefore reaches terminal output category 4: a precise failure certificate identifying the smallest remaining theorem and why the attempted mechanism fails.

The function-field half-theorem remains **CONDITIONAL** even after that analytic estimate until the original endpoint/main/Tate/Artin–Schreier and nearby-cycle application ledger is completed.
