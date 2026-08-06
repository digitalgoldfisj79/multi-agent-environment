# Focused integer Fortune programme

**Programme:** `FORTUNE_INT_ISC_FOCUSED_V0_1`  
**Date:** 4 August 2026  
**Base:** `deb6bb5468a951bc5485514c5848abcfcf386594`  
**Parent closeout:** PR #47  
**Primary issue:** #48  
**Outcome:** `REDUCED_TO_SMALLER_NEW_THEOREM`

## Purpose

This programme executed the corrected integer Fortune route against one target only. It
started from `INT-ISC`, audited whether that covariance theorem was unnecessarily strong,
and stopped only after every admitted proof lane reached a theorem or a reproducible scale
obstruction.

Paper VII cubic incidence, direct function-field `d=1`, random-order derandomisation and
unsupported reciprocal-frame extensions remained out of scope.

## Final target

For the registered primorial centres and `H=eta X^2`, put

\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m),
\qquad
B_X=c_0X(\log X)^2,
\]

where `c_0>0` is fixed, and define

\[
\mathcal D_{\Psi}^-(X)=\sum_{j<N}(B_X-\Psi_j(H))_+^2.
\]

The terminal theorem is

\[
\boxed{
\text{INT-PSLT: }\mathcal D_{\Psi}^-(X)=o(B_X^2).}
\]

At a failed centre the shifted source is only `O(X log X)=o(B_X)`, because all nonzero
von Mangoldt terms are proper prime powers. One failure therefore contributes
`(1+o(1))B_X^2`, so INT-PSLT implies no failures and hence eventual Fortune by candidate
collapse.

INT-PSLT remains unproved.

## Programme result

- full variance was reduced to a one-sided lower-tail criterion;
- the mandatory sparse first moment was removed;
- the direct four-prime route was closed at an `X/L(X)` loss;
- the shifted source reduced the problem to INT-PSLT;
- source/orbit geometry was closed at exact smooth-modulus coherence;
- adversarial models proved that first moments, relative moments and dense averages cannot
  resolve one failed centre.

`FINAL_STATUS.md` gives the closeout ruling. `PREREGISTERED_GATES.json` and
`EXPONENT_LEDGER.json` are the machine-readable execution record.

## Honesty boundary

The programme is a completed reduction and obstruction analysis. It is not a proof of
INT-PSLT, INT-ISC or Fortune's conjecture.
