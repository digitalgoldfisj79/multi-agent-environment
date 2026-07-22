# Growing-cutoff threshold calibration

**Date:** 2026-07-22  
**Status:** numerical evaluation of the explicit bounds in
`GROWING_CUTOFF_BONFERRONI.md`; not an additional theorem.

The degree and Cafure--Matera constants are deliberately conservative.  The
resulting point-count thresholds are therefore astronomical.

For each K, L is the least odd integer at least

`6(H_K-1)`.

The table reports the decimal logarithm of the sufficient geometric
point-count threshold, before testing the finite `(K,L)` good-reduction
condition.

| K | L | log Delta | log10 P_geom |
|---:|---:|---:|---:|
| 2 | 3 | 14.2182 | 43.42 |
| 3 | 5 | 26.5907 | 77.45 |
| 5 | 9 | 63.4219 | 176.94 |
| 10 | 13 | 163.724 | 444.59 |
| 20 | 17 | 406.648 | 1086.67 |
| 50 | 21 | 1220.96 | 3224.67 |
| 100 | 27 | 3089.80 | 8114.59 |

Thus the explicit theorem is not a practical verification method.  Its value
is structural:

1. the full splitting compositum is avoided;
2. only `O(log K)` marked factors are needed;
3. the geometric point-count cost is `exp(O(K log K))`;
4. the resulting good-prime distribution level is
   `K << log p/log log p`;
5. moving-period bad reduction is exposed as a separate arithmetic
   obstruction.

The script checked the Taylor lower bound

`P_L(H_K-1) >= (1/2) exp(-(H_K-1))`

for every `2<=K<=10000`.  Over `3<=K<=10000`, the maximum observed value of

`log P_geom(K)/(K log K)`

was `54.112274...`, attained at `K=3`; it decreases toward the asymptotic
constant `36 log 3=39.5500...`, with small oscillations caused by the odd
integer choice of L.

The rounded criterion

`log p >= 100 K log K`

therefore contains a substantial numerical safety margin in this range.  The
proof should continue to use the exact definition of `P_geom(K)`; the rounded
criterion is only a readable corollary.
