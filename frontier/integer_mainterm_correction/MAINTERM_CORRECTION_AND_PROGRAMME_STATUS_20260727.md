# Fortune integer programme after main-term correction

Date: 27 July 2026  
Status: exact correction completed; first corrected source theorem proved; transference reconstruction open.

## Accepted correction

Below the square threshold, a prime value `P_j+m` forces `m` to be prime. Therefore the direct detector is a prime-pair detector. The old centring

\[
\sum_{m\le H}\Lambda(P_j+m)-H
\]

is a valid hypothetical failure certificate but is not the standard Hardy--Littlewood fluctuation variable.

The corrected baselines are

\[
\lambda_j(H)=\mathfrak S(P_j)
\int_{\ell_j}^{H}\frac{dt}{\log t\log(P_j+t)}
\]

for the unweighted pair count, and

\[
\mu_j(H)=\mathfrak S(P_j)
\int_{\ell_j}^{H}\frac{dt}{\log t}
\]

for the output-weighted count. A double-von-Mangoldt source has baseline

\[
\nu_j(H)=\mathfrak S(P_j)H.
\]

All three calibrations are conjectural; the block implications require only baselines of the corresponding orders.

## Exact results added in this correction

1. Exact candidate-collapse decomposition of the shifted von Mangoldt detector.
2. Correct unweighted, weighted and double-von-Mangoldt all-centres variance criteria.
3. Failure contamination bound `O(X(log X)^2)` for the double source.
4. Exact Fourier source-to-single-walk identity.
5. Exact identification of the corrected second moment as a four-linear-form prime correlation.
6. Quarantine of the old pair-sum frame as an independent model until a new signed transference is proved.

## Finite calibration run

The exact prime-pair count was measured at

`p = 29, 43, 59, 79, 101, 131, 167, 211, 263, 331, 419`

with `H = floor(0.9 p_next^2)`. Each candidate prime offset was tested and the Hardy--Littlewood singular-series integral was evaluated independently.

| p | Z | lambda | Z/lambda | weighted/H | weighted/mu |
|---:|---:|---:|---:|---:|---:|
| 29 | 31 | 40.25 | 0.770 | 0.811 | 0.770 |
| 43 | 54 | 56.09 | 0.963 | 1.008 | 0.963 |
| 59 | 61 | 70.68 | 0.863 | 0.893 | 0.863 |
| 79 | 83 | 91.04 | 0.912 | 0.940 | 0.912 |
| 101 | 121 | 110.64 | 1.094 | 1.120 | 1.094 |
| 131 | 138 | 146.46 | 0.942 | 0.954 | 0.942 |
| 167 | 186 | 178.86 | 1.040 | 1.049 | 1.040 |
| 211 | 232 | 230.59 | 1.006 | 1.005 | 1.006 |
| 263 | 259 | 267.57 | 0.968 | 0.967 | 0.968 |
| 331 | 300 | 332.16 | 0.903 | 0.898 | 0.903 |
| 419 | 378 | 406.31 | 0.930 | 0.921 | 0.930 |

The panel is consistent with the corrected model but is too small to establish an asymptotic. The convergence of `mu/H` to `e^gamma/2` is very slow: the conjectural ratio is about `1.024` at `p=101`, `0.976` at `p=1009`, `0.952` at `p=10007`, `0.938` at `p=100003`, and `0.929` at `p=1000003`, tending to `0.890536...`.

## Programme execution result

### Phase A: calibration — completed

The corrected main terms and exact block implications are established as mathematical statements. Finite tests reproduce the predicted scale.

### Phase B: source reconstruction — first gate completed

The exact circle identity shows that the corrected source is the product of two von Mangoldt Fourier transforms and that the first path kernel is the single-walk sum `F_X`. This is a substantive change from the prior pair-sum-first architecture.

### Phase C: two-sided signed divisor frame — open

The next task is to expand both von Mangoldt factors while retaining their coupling and subtracting the singular-series main term before absolute values. The old one-sided frame cannot simply be reused.

### Phase D: deterministic energy — deferred

HTE4, the pair-sum exceptional-set theorem and Paper IV derandomisation become relevant only if Phase C produces the old frame or a provable domination by its single-walk component.

## Current theorem-level stopping point

The immediate open theorem is not yet a cancellation estimate. It is the exact signed two-prime transference identity. Until it is derived, there is no well-defined load-bearing reciprocal energy to attack.

The function-field Papers V--VI remain separate and are unaffected by this integer correction.
