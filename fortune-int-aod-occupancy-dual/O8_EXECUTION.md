# O8 — falsification and exact-panel execution

**Status:** PASSED AS DIAGNOSTIC AND FALSIFICATION GATE

## Exact panels

For diagnostic scales `X`, the programme used actual centres `P_j=ell_j#` for primes `ell_j in [X,2X)`, `H=floor(X^2/2)`, prime offsets `ell_j<m<=H`, and exact primality tests for `P_j+m`.

No failed row occurred in the exact panels through `X=300`. This finite observation is not promoted to an asymptotic theorem.

## Whole-block diagnosis

The whole-block occupancy distribution is strongly heterogeneous. Its factorial and ordinary connected coefficients oscillate, and an absolute order-twelve truncation does not uniformly certify the exact detector. This agrees with the O4 Poisson-mixture zero-radius obstruction.

## Corrected stratified ordinary-cumulant diagnosis

Rows were partitioned deterministically into terminal-prime intervals of width

\[
\lfloor X/(\log X)^{1.25}\rfloor.
\]

Within each stratum the diagnostic temperature was

\[
\tau_b=2\log(n_bB)/\overline Z_b.
\]

Because this temperature uses the observed mean, it is **diagnostic only** and is not an admissible proof parameter.

Job `6a72bdeca00abefd4b29310c` recomputed the detector, Laplace zero radii, and ordinary cumulants:

| X | strata | total exponential detector | worst `tau_b / zero radius` | worst order-12 absolute ordinary-cumulant margin |
|---:|---:|---:|---:|---:|
| 100 | 8 | 0.07618 | 0.62305 | 2.0794 |
| 150 | 8 | 0.05487 | 0.71534 | 2.0794 |
| 200 | 9 | 0.04605 | 0.61033 | 2.1972 |
| 250 | 9 | 0.02966 | 0.61831 | 2.9042 |
| 300 | 9 | 0.02586 | 0.44057 | 3.1019 |

Every tested stratum remained inside its numerical Laplace zero-free disk, and every order-twelve absolute ordinary-cumulant margin was positive.

## Algebraic correction caught by O9

The first O5 verifier incorrectly identified factorial cumulants with common-row joint cumulants over distinct columns. Static validation rejected that identity. The corrected exact identity uses ordinary cumulants and all ordered column tuples, including repetitions. The stratified diagnostics were rerun in the corrected ordinary-cumulant formulation before closeout.

## Adversarial falsification

For every tested `K`, the zero-row and nonzero-row panels have matching factorial moments through order `K`; for `K>=1`, they can also have identical all-one column-degree multisets and zero pairwise column overlaps. These statistics therefore cannot resolve one failed row.

## Ruling

The diagnostics select deterministic stratification and reject whole-block absolute cumulants, fixed-order row moments, column degrees, and pairwise overlaps as sufficient statistics. They establish neither `INT-SOCG`, `INT-AOD`, nor an asymptotic Fortune result.
