# Phase Z4 quantized residue status

**Date:** 2026-07-23  
**Status:** exact large-prime counts complete through `p=701`; the quantization gate survives and a stronger square-root-scale target has emerged, but no uniform theorem is proved.

## 1. Exact new counts

For the depressed slice

`X^p+aX^3+cX+d`,

let `N_a(p)` denote the number of irreducible members as `(c,d)` range over `F_p^2`. Exact counts for representatives of the two square classes are:

| p | square | nonsquare |
|---:|---:|---:|
| 401 | 362 | 370 |
| 503 | 480 | 466 |
| 601 | 516 | 488 |
| 701 | 628 | 642 |

All eight counts are even, positive and below `3p/2`, hence below the critical `2p` threshold.

The fast implementation uses FLINT modular composition and computes the `p`-fold Frobenius iterate by binary composition. At `p=101` it was cross-checked against the independent C++ implementation; both returned exactly `(76,116)`.

## 2. Quantization consequence

The exact parity theorem remains:

if `0<=N_a<2p`, then the Cartier residue determines `N_a` uniquely, and

`S_a=0 mod p` iff `N_a=0`.

The new computations do not prove this inequality uniformly, but they materially extend its exact finite support.

## 3. Stronger empirical target

Across the complete committed dataset through `p=293` together with `p=401,503,601,701`,

`max |N_a-p|/sqrt(p) = 4.875086...`,

attained at `p=167` in the square class.

This suggests replacing the coarse target `N_a<2p` by the structurally stronger objective

`N_a=p+O(sqrt(p))`.

A fixed-rank Weil bound of this form would imply positivity and `N_a<2p` for all sufficiently large `p`, leaving only a finite check.

A fingerprint against `1,676` small elliptic curves found no exact or stable short elliptic decomposition. Thus the prospective trace object is not an obvious small direct sum of elliptic curves; a higher-genus or higher-dimensional primitive factor remains plausible.

## 4. Route status

Route Q is currently the strongest conversion route, but the missing theorem is now explicit:

> Construct a fixed-complexity geometric or cohomological object whose Frobenius trace equals `N_a-p`, or otherwise prove a uniform square-root-scale bound.

Finite computation has not proved positivity for every prime, the `2p` bound, the d=1 crown, or the integer Fortune conjecture.
