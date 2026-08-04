# INT-PFLI signed-duality closeout

**Programme:** `FORTUNE_INT_PFLI_SIGNED_DUALITY_V0_1`  
**Date:** 4 August 2026  
**Branch:** `gpt56/fortune-int-pfli-signed-duality-v01-20260804`  
**Outcome:** `REDUCED_TO_GROWING_ARITY_GENERATING_FUNCTION`

## Final ruling

The programme did not prove `INT-PFLI`, `INT-AOD`, or Fortune.

The exact partition `|A_j|=Z_j+C_j` gives

\[
(C_j-|\mathcal A_j|+\gamma_j)_+=(\gamma_j-Z_j)_+.
\]

Thus `INT-PFLI` is exactly a prime-pair count lower-tail theorem after complete factor coverage is recombined.

## Successor theorem — INT-AOD

Let

\[
\gamma_{\min}=\min_{j<N}\gamma_j,
\qquad
\tau_X=\frac{2\log N}{\gamma_{\min}},
\]

and put

\[
\mathcal O_X=\sum_{j<N}e^{-\tau_XZ_j}.
\]

The successor theorem is

\[
\boxed{\mathcal O_X<1}
\]

for every sufficiently large registered block. A failed row has `Z_j=0` and contributes exactly `1`, so this condition excludes every failure. The inherited lower-tail theorem would imply `O_X=o(1)`, while this detector permits positive rows below `gamma_j`.

`INT-AOD` remains open.

## All-orders expansion

With `q_X=1-e^{-tau_X}`,

\[
e^{-\tau_XZ_j}=(1-q_X)^{Z_j}
=\sum_{k=0}^{Z_j}(-q_X)^k\binom{Z_j}{k}.
\]

## Moment barrier

For every `K>=0`, the even and odd binomial panels

\[
E_K=\bigsqcup_{r\text{ even}}\binom{K+1}{r}\{r\},
\qquad
O_K=\bigsqcup_{r\text{ odd}}\binom{K+1}{r}\{r\}
\]

have `2^K` rows and agree in ordinary and factorial moments through order `K`. The even panel contains one zero row; the odd panel contains none. Padding preserves this for every `N>=2^K`.

Therefore a moment-only one-defect argument requires

\[
K>\log_2N=\Theta(\log X).
\]

The `k`th factorial moment is a coupled `2k`-prime correlation, so the corresponding arity must grow as `Omega(log X)`. No fixed-order moment extension reaches the target.

## Sieve audit

Direct use of the asymptotic sieve requires a separate row-uniform bilinear hypothesis in addition to divisor-sum information. Weighted switching requires verified distribution in both coordinates. No audited theorem supplies those inputs in the post-level range beginning beyond `sqrt(H)` while retaining one-row resolution.

## Remaining input

A future proof must provide an all-orders occupancy estimate, a rowwise parity-breaking theorem, or a selected-centre bilinear/duality estimate that retains information beyond every fixed moment order.

## Explicitly not claimed

- `INT-AOD`;
- `INT-PFLI`;
- `INT-PSLT`;
- Fortune's conjecture;
- a function-field-to-integer transfer.

## Validation

Research and targeted formal validation are complete. Full clean-room validation is pending.
