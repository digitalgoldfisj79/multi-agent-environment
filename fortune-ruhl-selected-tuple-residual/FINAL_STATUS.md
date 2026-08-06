# Final status — RUHL selected-tuple residual

**Programme:** `FORTUNE_RUHL_SELECTED_TUPLE_RESIDUAL_V0_1`  
**Date:** 6 August 2026  
**Branch:** `gpt56/fortune-ruhl-selected-tuple-residual-v01-20260806`  
**State:** `EXECUTED_AND_VALIDATED`

## Terminal outcomes

- `SOURCE_IDENTITY_LOSES_BONFERRONI_CANCELLATION`
- `SELECTED_CENTRE_RESIDUAL_BEYOND_CURRENT_METHODS`
- `NO_NEW_UNCONDITIONAL_PROGRESS`

## Decisive findings

1. The signed RUHL residual is exactly the difference between the actual even-Bonferroni occupancy polynomial and the deterministic model Taylor polynomial. Without a new jointly signed prime-tuple theorem, it is close to the detector target itself.

2. The independent absolute RUHL theorem already forces

\[
|E_{b,1}|<\Delta_b/q_b=O(1),
\]

although the selected-centre mean is of order `X`. It therefore requires additive constant accuracy for the first moment, which is stronger than `INT-SCME`.

3. The one admitted exact Heath--Brown identity has a source-scale dichotomy. At `J=Theta(log X)` its cutoff is exponentially larger than `H=X^2`. Forcing the cutoff below `H` requires `J~X/(2 log X)` and absolute coefficient mass `2^J-1=exp(Theta(X/log X))`.

4. The existing elementary prime-power correction becomes `O(log X)` after count normalization and does not fit the constant first-order allowance.

## Frontier ruling

No smaller explicit bilinear estimate was isolated whose proof would immediately establish RUHL. The direct integer route is now at the selected-centre growing-order prime-tuple theorem itself. Further divisor-identity expansion without a genuinely new signed theorem would be mechanism churn rather than progress toward Fortune.

## Validation

Workflow run `31085980195` at head `60f27ff3dee98f0761da361bc7856f588dec9163` passed:

- exact signed-discrepancy and Heath--Brown finite regressions;
- detector-margin and source-scale panels;
- targeted build of `RuhlSelectedTupleResidualCriterion`;
- full `FortuneFormal` package build;
- scan for `sorry`, `admit`, `axiom` and `unsafe`;
- Lean `4.32.0`.

## Explicit nonclaims

No proof or disproof of RUHL-FM is claimed.  
No proof of INT-AOD or Fortune is claimed.  
The source audit is a closure of the frozen Heath--Brown termwise/absolute implementation, not a universal impossibility theorem for every future signed prime-tuple method.
