# Verification record for the actual Pascal and terminal quantum-bar theorems

**Date:** 2026-07-25  
**Branch:** `gpt56/airy-gaussian-independent-audit-20260725`  
**Classification:** independent exact arithmetic regression.

## Actual Pascal graph oscillator

An independent implementation, separate from `pascal_actual_oscillator_verify.py`, checked every odd prime `p` from `11` through `199` (`42` primes):

- the upper-to-upper block is zero;
- the lower-to-upper block is triangular and invertible;
- `C=B^{-t}`;
- `B^{-1}A` is symmetric.

At `p=11`, where `m=2`, direct enumeration of all `11^4` pairs `(x,y)` gave cyclotomic exponent multiplicities

```
[1441, 1320, 1320, 1320, 1320, 1320, 1320, 1320, 1320, 1320, 1320]
```

so the exact complete exponential sum is

\[
1441-1320=121=11^2,
\]

and the punctured sum is `120=11^2-1`.

## Terminal order-p quantum bar complex

A second independent implementation constructed all composition-basis differentials over an auxiliary finite field containing a primitive `p`-th root of unity and performed exact modular Gaussian elimination.

The nonzero bar homology was:

| `p` | auxiliary field | primitive root | nonzero homology by composition length |
|---:|---:|---:|---|
| 3 | `F_7` | 2 | `{1:1, 2:1}` |
| 5 | `F_11` | 3 | `{1:1, 2:1}` |
| 7 | `F_29` | 7 | `{1:1, 2:1}` |
| 11 | `F_23` | 2 | `{1:1, 2:1}` |

Thus the independently constructed matrices reproduce exactly two adjacent one-dimensional terminal classes and no other homology.

## Scope

These checks certify the finite algebraic identities and regressions implemented by the scripts. They do not certify the still-open geometric comparison between the nonlinear wild Artin--Schreier nearby cycles and the linear Pascal/quantum-bar models.