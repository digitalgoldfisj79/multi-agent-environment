# O8 — falsification and exact-panel execution

**Status:** PASSED AS DIAGNOSTIC AND FALSIFICATION GATE

## Exact panel definition

For each diagnostic scale `X`, the programme used:

- actual increasing primorial centres `P_j=ell_j#` for primes `ell_j in [X,2X)`;
- `H=floor(X^2/2)`;
- prime candidate offsets `ell_j<m<=H`;
- exact primality tests for `P_j+m`;
- occupancy `Z_j` equal to the exact number of prime-prime pairs.

These panels use the same candidate-collapse geometry as the asymptotic target, at one registered diagnostic value `eta=1/2`.

## Whole-block results

Job `6a72b6a8a00abefd4b29309b` completed with failure count zero. Through `X=250`:

| X | rows | min Z | mean Z | max Z | zero rows | detector at `q=2 log N / mean Z` | nearest numerical q-zero |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 4 | 3 | 4.000 | 6 | 0 | 0.06749 | 0.99999 |
| 20 | 4 | 7 | 8.500 | 10 | 0 | 0.15348 | 0.98192 |
| 30 | 7 | 11 | 14.429 | 21 | 0 | 0.12679 | 0.40361 |
| 50 | 10 | 15 | 23.300 | 39 | 0 | 0.12291 | 0.25146 |
| 75 | 14 | 18 | 31.786 | 45 | 0 | 0.10416 | 0.25100 |
| 100 | 21 | 27 | 43.571 | 69 | 0 | 0.09222 | 0.13516 |
| 150 | 27 | 44 | 64.074 | 89 | 0 | 0.04943 | 0.17784 |
| 200 | 32 | 53 | 81.438 | 108 | 0 | 0.05678 | 0.10961 |
| 250 | 42 | 71 | 102.381 | 142 | 0 | 0.04169 | 0.08073 |

The whole-block factorial cumulants oscillate rapidly. At several scales the absolute connected remainder through order twelve is too large to certify the detector even though the exact detector is below one. This is consistent with the O4 heterogeneity obstruction.

## Stratified results

Rows were partitioned deterministically by terminal-prime intervals of width

\[
\lfloor X/(\log X)^{1.25}\rfloor.
\]

Within each stratum the diagnostic parameter was

\[
q_b=2\log(n_bB)/\overline Z_b.
\]

This uses the observed mean and is therefore **diagnostic only**, not an admissible proof parameter.

Jobs `6a72b899a00abefd4b2930b4` and the associated exact scripts gave:

| X | strata | total stratified detector | worst `q_b / zero radius` | worst order-12 absolute connected margin |
|---:|---:|---:|---:|---:|
| 100 | 8 | 0.05108 | 0.62885 | 1.7361 |
| 150 | 8 | 0.04061 | 0.70667 | 1.8881 |
| 200 | 9 | 0.03551 | 0.59789 | 2.0152 |
| 250 | 9 | 0.02251 | 0.61022 | 3.0479 |
| 300 | 9 | 0.02025 | 0.45975 | 3.2444 |

Every tested stratum remained inside its numerical zero-free disk, and every truncated absolute connected margin was positive.

## Adversarial falsification

The inherited even/odd panels and the strengthened private-column realizations were rerun. For every tested order `K`:

- one panel contains a zero row and the other does not;
- row factorial moments agree through order `K`;
- for `K>=1`, both can have identical all-one column-degree multisets;
- pairwise column overlaps vanish in both.

The exact stratified detector sentinel also confirms that inserting one zero row makes the total detector at least one.

## Ruling

The diagnostics select deterministic stratification and reject whole-block absolute cumulants, low-order row moments, column degrees, and pairwise overlaps as sufficient statistics. They do not establish `INT-SCG`, `INT-AOD`, or any asymptotic Fortune statement.
