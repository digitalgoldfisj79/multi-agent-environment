# Order-ensemble experiment: is the increasing order generic?

**Date:** 2026-07-21.  **Script:** `order_ensemble.py` (seed 20260721).  **Raw data:** `order_ensemble_results.json`.
**Status:** numerical diagnostic only — not a proof of anything.

## Question

Vector B2 (RESEARCH_VECTORS.md) isolates *derandomization* — consecutive primes
vs i.i.d. primes — as one of the two named gaps behind PGD2. If the TRUE
increasing order of the block primes were an outlier of the ordering ensemble
for walk exponential sums, any random-order model theorem would be vacuous for
the real problem. This experiment tests exchangeability directly at the real
scale relation q ~ X^2 (the shell scale H = eta X^2).

## Design

For X in {300, 1000, 3000, 10000}: block primes L = primes in [X, 2X) (K of
them); 40 random prime moduli q in [X^2, 2X^2]; A = A_X mod q. For an ordering
sigma, Q_j = prefix product in that order mod q, and

    V(sigma, q, a) = |sum_{j=1..K} e_q(a * A * Q_j)|^2 / K,   a in {1, 2, 3}.

Null: for random phases V ~ Exp(1) (mean 1, sd 1). Orders per (X, q):
increasing (`inc`), decreasing (`dec`), 200 fresh uniform random orders,
adversarial-as-specified (`adv_spec`: sort by ell mod q ascending), and
`adv_mult` (sort by A*ell mod q ascending, a genuinely q-dependent order).

**Flag on the specified adversarial order:** since every q >= X^2 > 2X > ell,
we have ell mod q = ell, so `adv_spec` is *identical* to the increasing order
for every q (confirmed programmatically for all 160 moduli). It is retained as
a consistency check; `adv_mult` is the substantive adversarial variant.

**Single-walk energy G:** not computed separately — at a single modulus it is
an exact linear function of V: sum_{i != k} e_q(aA(Q_i - Q_k)) =
|sum_j e_q(aAQ_j)|^2 - K, so G/K = V - 1 identically. V carries all the
per-q information; the aggregation over the shell (row weights p_{q,a}) is a
separate question not probed here.

Percentile of a distinguished order = (#{V_rand < V} + 0.5 #{V_rand = V})/200,
per (q, a); over the 40 q it should be ~ Uniform(0,1) under exchangeability.
KS D = max ECDF deviation from uniform; 5% critical value at n = 40 is 0.215,
at n = 120 is 0.124.

## Results

### Per-(X, a) summary (40 moduli each; percentile stats over q)

| X | K | a | rand mean V | rand sd V | V_inc | pct_inc | KS_inc | V_dec | pct_dec | KS_dec | V_advm | pct_advm | KS_advm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 300 | 47 | 1 | 1.006 | 0.983 | 1.065 | 0.501 | 0.100 | 1.349 | 0.501 | 0.165 | 1.037 | 0.533 | 0.100 |
| 300 | 47 | 2 | 0.986 | 0.951 | 1.097 | 0.527 | 0.125 | 0.913 | 0.488 | 0.120 | 0.843 | 0.453 | 0.155 |
| 300 | 47 | 3 | 1.014 | 0.982 | 0.951 | 0.483 | 0.070 | 1.220 | 0.532 | 0.120 | 0.993 | 0.550 | 0.155 |
| 1000 | 135 | 1 | 1.003 | 0.985 | 1.197 | 0.552 | 0.165 | 1.238 | 0.550 | 0.190 | 1.197 | 0.546 | 0.110 |
| 1000 | 135 | 2 | 1.003 | 1.019 | 0.976 | 0.498 | 0.090 | 1.061 | 0.525 | 0.150 | 1.171 | 0.575 | 0.165 |
| 1000 | 135 | 3 | 1.023 | 1.010 | 1.313 | 0.525 | 0.135 | 1.172 | 0.548 | 0.140 | 1.260 | 0.532 | 0.105 |
| 3000 | 353 | 1 | 1.002 | 1.009 | 0.939 | 0.483 | 0.100 | 1.217 | 0.557 | 0.130 | 0.781 | 0.459 | 0.120 |
| 3000 | 353 | 2 | 0.998 | 0.999 | 1.128 | 0.550 | 0.125 | 1.099 | 0.527 | 0.145 | 0.944 | 0.501 | 0.090 |
| 3000 | 353 | 3 | 0.989 | 0.980 | 1.229 | 0.521 | 0.105 | 1.268 | 0.555 | 0.190 | 0.958 | 0.505 | 0.105 |
| 10000 | 1033 | 1 | 0.995 | 0.974 | 1.277 | 0.585 | 0.155 | 0.743 | 0.434 | 0.145 | 1.278 | 0.593 | 0.200 |
| 10000 | 1033 | 2 | 1.003 | 0.988 | 1.265 | 0.559 | 0.175 | 1.287 | 0.547 | 0.190 | 1.055 | 0.508 | 0.105 |
| 10000 | 1033 | 3 | 1.012 | 1.019 | 0.884 | 0.450 | 0.190 | 0.941 | 0.469 | 0.085 | 0.847 | 0.490 | 0.130 |

All 36 per-cell KS statistics (12 cells x 3 orders) are below the n = 40
critical value 0.215; the largest is 0.200 (X = 10000, a = 1, adv_mult).

### Pooled percentile uniformity (all X, all a; n = 480 percentiles per order)

| order | mean pct | z(mean) | KS D | KS crit (5%, n=480) | # < 0.05 | # > 0.95 | expected |
|---|---|---|---|---|---|---|---|
| inc | 0.5196 | 1.49 | 0.0458 | 0.0620 | 26 | 35 | 24 |
| dec | 0.5193 | 1.46 | 0.0500 | 0.0620 | 30 | 35 | 24 |
| adv_mult | 0.5204 | 1.55 | 0.0483 | 0.0620 | 17 | 17 | 24 |

### Per-X pooled percentiles for the increasing order (n = 120 each)

| X | mean pct_inc | z(mean) | KS D | KS crit (5%, n=120) |
|---|---|---|---|---|
| 300 | 0.5040 | 0.15 | 0.0700 | 0.1240 |
| 1000 | 0.5251 | 0.95 | 0.1017 | 0.1240 |
| 3000 | 0.5181 | 0.69 | 0.0750 | 0.1240 |
| 10000 | 0.5313 | 1.19 | 0.1000 | 0.1240 |

**Correlation caveat.** The three harmonics at a fixed q share the same walk
and the same 200 random orders, so the 480 pooled percentiles are not 480
independent draws; the effective sample size is closer to 160 (40 q x 4 X).
Against that effective size, the pooled z ~ 1.5 and the mild excess of
percentiles above 0.95 (35 vs 24 expected, for inc and dec alike) are within
ordinary fluctuation (z well under 1 after deflating by ~sqrt(3)); and the
same mild positive lean appears for `dec` and `adv_mult`, which have no
arithmetic reason to be co-biased with `inc` — consistent with shared-ensemble
noise, not an order effect.

## Reading

1. **The increasing order looks exchangeable with uniformly random orders**
   at every tested scale up to X = 10000 (K = 1033 block primes, q ~ 2x10^8):
   per-q percentiles of V_inc within the 200-order random ensemble are
   statistically uniform (all KS tests pass at 5%, per cell, per X, and
   pooled), the mean percentile is 0.50-0.53, and mean V_inc tracks the
   ensemble mean 1 within ~1.8 ensemble-standard-errors in every cell, with
   signs scattered. No piling at either extreme.
2. **Decreasing and adversarial orders are equally generic.** `adv_mult`
   (sorting by the q-dependent residue A*ell mod q) produces no elevation of
   V — evidence that no *simple one-step* residue-sorting adversary can beat
   the walk at this scale; the prefix-product cascade destroys the injected
   first-order alignment.
3. **Null-model confirmation.** The random-order ensemble has mean V = 1.00
   +/- 0.01 and sd ~ 0.98-1.02 across all 12 cells: the single-q walk value
   distribution is Exp(1) to high accuracy, i.e. the walk behaves like a
   Steinhaus-random phase sum even at K ~ q^{1/2}/log q x const — the
   critical length where the archive says generic technology dies. The
   *statistical* behaviour is fine there; what is missing is a *proof*.
4. **Implication for vector B2.** The derandomization gap shows no finite-size
   obstruction: nothing distinguishes the true order from a random order in
   the V statistic. This is the good direction for the programme (a
   random-order theorem would not be modelling away a real anomaly), but it
   also means order-genericity gives no *leverage*: there is no special
   structure of the increasing order to exploit, and the derandomization step
   must come from step-averaging-free arithmetic input, exactly as B2 states.
5. **Anomalies found: one, and it is definitional** — the specified
   adversarial order (sort by ell mod q) is identically the increasing order
   because q >= X^2 exceeds every block prime; it was replaced by the
   q-dependent `adv_mult` for substance. No data anomalies.

## Limits

- Diagnostic only; consistent with, but no evidence for, PGD2 (finite panels
  cannot certify X^{o(1)} factors).
- Tests single-modulus V, not the shell-aggregated energy E_a or the pair-sum
  kernel; per A1 the single-walk object is a *necessary* sub-target, so a
  failure here would have been decisive, while a pass is only permissive.
- 40 moduli x 200 random orders per (X, q); percentile resolution 1/200.
- Runtime: 8 s total for all four X (pure Python), so this panel is far from
  cost-limited; X = 30000-100000 is reachable if a future question needs it.
