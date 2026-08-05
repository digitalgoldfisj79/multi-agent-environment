# INT-SCME selected-centre mean closeout

**Programme:** `FORTUNE_INT_SCME_SELECTED_CENTRE_MEAN_V0_1`  
**Date:** 5 August 2026  
**Branch:** `gpt56/fortune-int-scme-selected-centre-mean-v01-20260805`  
**Outcome:** `METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE`  
**Primary frontier:** issue #58, `INT-SCME`

## Final mathematical ruling

The programme does not prove `INT-SCME`, `INT-SOCG`, `INT-AOD`, or Fortune's conjecture.

It proves that the tested selected-residue route requires two independent missing inputs:

\[
INT\text{-}SCVAR+INT\text{-}SCPT
\Longrightarrow INT\text{-}SCME.
\]

`INT-SCVAR` is a post-terminal prime-progression variance theorem at `Q=H^(2/3-o(1))`. `INT-SCPT` is the signed prime-versus-composite parity-tail lower bound after that divisor band is extracted.

## Exact results

### Weighted implication

The inherited prime-power subtraction and the formal band-plus-tail bridge show that a positive weighted mean of order `X^2 log X` implies the mandatory first-cumulant lower bound `c_1>=cX`.

### Direct asymptotic-sieve scale gap

The outputs have size

\[
P_j=\exp((1+o(1))X),
\]

whereas ordinary offset distribution is polynomial in `X`. The direct Friedlander–Iwaniec hypotheses require output-scale remainder and bilinear ranges exponentially beyond the available offset information.

### Selected-residue collision energy

For a deterministic microblock with `R` rows,

\[
\sum_{2X<q\le Q}\sum_a r_q(a)^2
\ll RQ/\log Q+R^3.
\]

The estimate follows from the exact primorial recurrence and the fact that a row-pair collision at distance `d` can occur for fewer than `d` prime moduli above `2X`.

### Conditional variance frontier

Under

\[
INT\text{-}SCVAR:\quad
V(H,Q)\ll HQ(\log H)^C,
\]

selected-residue Cauchy gives lower-order errors exactly when

\[
2\delta<\rho<1-\delta,
\qquad Q=X^{1+\delta},\ R=X^\rho.
\]

The conditional optimum is `rho=2/3`, every fixed `delta<1/3`.

### Unconditional obstruction

The standard large-sieve variance

\[
V(H,Q)\ll(H+Q^2)H(\log H)^C
\]

produces relative error exponent

\[
\frac12+\frac{3\delta}{2}-\frac\rho2.
\]

For every post-terminal `delta>0` and every admissible `rho<=1`, this is positive. Thus the standard unconditional selected-residue variance route cannot enter any polynomial band above `2X`, even under a fictitious collision-free model.

## Correction record

The first execution draft incorrectly invoked the classical `HQ log H` Barban–Davenport–Halberstam scale at `Q=H^(2/3)`. The literature range audit rejected that step. The unconditional divisor-band promotion was retracted, the programme was rewritten around `INT-SCVAR`, and all accepted validation evidence postdates the correction. See `CORRECTION_RECORD.md`.

## Diagnostics

Exact scripts verified microblock aggregation, collision multiplicity, the conditional `1/3` exponent frontier, the unconditional large-sieve obstruction, the band-plus-tail identity and an adversarial all-composite control. Small factor profiles were diagnostic only.

## Governance

- issue #58 remains the sole primary integer frontier;
- issue #60 records the subordinate `INT-SCVAR` target;
- issue #61 records the subordinate `INT-SCPT` target;
- draft PR #59 contains the programme closeout.

## Validation

- corrected static sentinel `6a72ed956b79c09949c22ddf`: passed;
- targeted Lean `6a72edc6a00abefd4b293482`: passed, 8,655 jobs;
- GitHub Actions run `30987825241`: static and targeted Lean jobs passed;
- full clean room `6a72efa0a00abefd4b2934a2`: passed in 222 seconds;
- full Lean 4.32 package: 8,685 jobs;
- all inherited integer verifiers, mainline verifier and formal trust audit passed;
- terminal sentinel: `FORTUNE_INT_SCME_FULL_CLEANROOM_PASS`.

The pre-correction job `6a72eaf2a00abefd4b293438` and the wording-validator failure `6a72ef3ca00abefd4b29349a` are excluded from mathematical evidence.

No new Lean axiom, `sorry`, `admit`, or unsafe declaration is introduced.