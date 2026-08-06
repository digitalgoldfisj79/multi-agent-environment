# Final status — RUHL selected-tuple residual

**Programme:** `FORTUNE_RUHL_SELECTED_TUPLE_RESIDUAL_V0_1`  
**Date:** 6 August 2026  
**State:** `EXECUTED_VALIDATED_AND_REVIEW_CORRECTED`

## Terminal outcomes

- `SOURCE_IDENTITY_REQUIRES_EXPONENTIALLY_WEIGHTED_RESIDUAL_CONTROL`
- `SELECTED_CENTRE_RESIDUAL_BEYOND_CURRENT_METHODS`
- `NO_NEW_UNCONDITIONAL_PROGRESS`

## Decisive findings

1. The signed RUHL residual is exactly the difference between the actual even-Bonferroni occupancy polynomial and the deterministic model Taylor polynomial. Without a new jointly signed prime-tuple theorem, it remains close to the detector target itself.

2. The independent absolute RUHL envelope forces

\[
|E_{b,1}|<\Delta_b/q_b=O(1)
\]

in the frozen geometry `n_bB\asymp X/log X`. Since the mean is of order `X`, this requires additive constant model accuracy and is strictly stronger than the linear lower-bound target `INT-SCME`.

3. The weakest signed criterion is one-sided at first order. Writing

\[
\mathcal E_{b,K}=-q_bE_{b,1}+R_{b,\ge2},
\]

excess actual mean helps; only a deficit must be controlled together with the higher-order signed remainder. This slack is intentionally discarded by the absolute envelope.

4. The exact Heath--Brown identity has a scale dichotomy. At `J=Theta(log X)` its cutoff exceeds `H=X^2`; forcing the cutoff below `H` requires `J~X/(2 log X)` and binomial coefficient mass `2^J-1=exp(Theta(X/log X))`. A termwise absolute proof must therefore establish the explicitly weighted residual bound

\[
\sum_r {J\choose r}|R_r|<\Delta_b.
\]

Coefficient growth alone does not prove that such a bound is impossible. The earlier universal method-closure wording is withdrawn.

## Frontier ruling

No smaller explicit bilinear estimate was isolated whose proof would immediately establish RUHL. The direct integer route remains the jointly signed selected-centre growing-order prime-tuple theorem. Further divisor-identity expansion is admissible only when accompanied by a concrete residual estimate that implies the frozen margin.

## Validation scope

The exact residual identity, first-order absolute implication, finite Heath--Brown identity, source-scale ledger and elementary Lean lemmas were validated. The corrected source ruling is a scope correction: no residual lower bound or universal impossibility theorem was validated or is now claimed.

## Explicit nonclaims

No proof or disproof of RUHL-FM is claimed.  
No proof of INT-AOD or Fortune is claimed.  
No universal impossibility theorem for Heath--Brown, Vaughan or future signed prime-tuple methods is claimed.
