# Applicability audit: norm--trace estimates after the exact Salié cancellation

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Classification:** published external theorem plus exact applicability boundary.

## 1. Published estimates

For a degree-`n` finite field extension, Katz's trace--norm theorem and its refinements give square-root errors with a coefficient of order `n`. A recent uniform formulation is:

- Daqing Wan, *Norm-trace and Kloosterman sums in finite semi-simple algebras*, 2026, arXiv:2603.18511.

In the field case, the stated trace--norm error is bounded by

\[
(n-1)q^{(n-2)/2},
\]

and the corresponding Kloosterman estimate is bounded by

\[
nq^{(n-1)/2}.
\]

The paper obtains these results through Hasse--Davenport reduction to the split geometric case. It also observes that analogous product--trace estimates lead to a further conjectural problem.

## 2. Exact overlap with the present programme

The all-line projective sum

\[
\mathcal R_{\mathrm{all}}(p)
=
\sum_{[h]}
\chi_E(h)\chi(\operatorname{Tr}(h^{-1}))
\]

is a quadratic norm--reciprocal-trace sum. The branch evaluates it exactly by a finite-field Salié transform:

\[
\mathcal R_{\mathrm{all}}(p)
=
\chi(-1)^{(p-1)/2}p^{(p-1)/2}.
\]

Thus the norm--trace-type main contribution is not merely bounded; it is completely removed from the Airy second moment.

## 3. Why the published bound does not finish the theorem

In the present application

\[
q=p,
\qquad n=p.
\]

A general trace--norm or Kloosterman estimate with coefficient `n` therefore loses a factor `p`. After taking the square root in the Airy second-moment identity, this is a loss of `sqrt(p)`, precisely beyond the required absolute-constant theorem.

More importantly, the remaining sum is not a plain trace--norm count. It is

\[
\mathcal K_p
=
\chi(-1)\mathcal R_0(p)+\chi(3)\mathcal D(p),
\]

where:

- `R_0` restricts the polar norm character to the cubic power-trace section `Tr(h^3)=0`;
- `D` is the correction on the reciprocal-trace degeneracy divisor.

This is a power-trace/polar-norm boundary combination. It is not covered by the cited norm--trace theorem.

## 4. Exact applicability boundary

Published norm--trace theory supplies:

1. the correct square-root scale for fixed extension degree;
2. Hasse--Davenport comparison mechanisms;
3. bounds with constants growing at least linearly in the degree in the general theorem.

The `d=1` programme requires the stronger characteristic-boundary statement

\[
\boxed{
\mathcal K_p\ll p^{(p-3)/2}
}
\]

with an absolute constant while the extension degree itself equals the characteristic.

The exact Salié cancellation proves that the most obvious degree-sized contribution cancels. What remains is a refinement beyond the currently applicable published theorem, closely aligned with the paper's stated product--trace frontier but with an additional cubic power-trace constraint and boundary correction.

## 5. Ruling

A citation to generic norm--trace or Kloosterman square-root cancellation is insufficient. A valid proof must establish an absolute-constant refinement for the combined projective sum, or exploit an additional characteristic-`p` cancellation not present in the general degree-`n` estimate.
