# O3 — degree and coefficient-cost audit

The previous programme proved only a lower bound: an arbitrary `N`-row panel cannot have its zero rows determined from moments of order `K<=log_2 N`. This gate asks how much degree is actually required by natural positive detectors.

## Constant-density occupancy is intrinsically high degree

The exponential detector is

\[
(1-q_X)^Z,
\qquad q_X=\Theta(1)
\]

at the registered scale. Its exact hypergeometric analogue samples

\[
K=q_XM_X+O(1)
=\Theta(X^2/\log X)
\]

candidate offsets. As a polynomial in `Z`, the hypergeometric miss probability has degree `K`. Thus direct finite inclusion–exclusion at the natural cover density is vastly longer than `Theta(log X)`.

## Candidate polynomial families

Every family must be written in the factorial basis

\[
P_R(Z)=\sum_{k=0}^{R}c_k\binom{Z}{k}
\]

because the `k`th coefficient couples to the `k`th factorial prime-pair correlation.

The programme may test:

1. even Bonferroni majorants of `1_{Z=0}`;
2. hypergeometric miss polynomials;
3. squared interpolation kernels such as `prod_{r=1}^R(1-Z/r)^2`;
4. optimized linear-programming majorants on a finite integer range;
5. rational or Laplace-mixture kernels only when converted to a rigorous positive representation.

## Required ledger

For each proposed kernel, record:

- degree `R`;
- positivity domain;
- value at zero;
- supremum on `1<=Z<=Z_max`;
- growth for `Z>Z_max`;
- factorial-basis `l1` norm `sum |c_k|`;
- maximal correlation arity;
- arithmetic error budget after coefficients are applied.

## Kill rules

A finite-degree lane is closed if any of the following is proved:

- positivity fails on an attainable row count;
- the uncontrolled tail can exceed one row's full defect mass;
- coefficient amplification makes the available tuple error exceed `1/N` after summation;
- the required degree reaches `Theta(M_X)` without a non-moment summation mechanism;
- the argument uses moment matching alone at degree `<=log_2 N`.

The desired result is either a viable logarithmic- or sublinear-complexity positive kernel, or a rigorous obstruction explaining why connected rather than raw expansion is mandatory.