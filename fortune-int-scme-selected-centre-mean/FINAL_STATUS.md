# INT-SCME selected-centre mean closeout — review corrected

**Programme:** `FORTUNE_INT_SCME_SELECTED_CENTRE_MEAN_V0_1`  
**Date:** 5 August 2026  
**Branch:** `gpt56/fortune-int-scme-selected-centre-mean-v01-20260805`  
**Outcome:** `SELECTED_RESIDUE_VARIANCE_ROUTE_OBSTRUCTED`  
**Review:** `claude/fortune-int-programme-review-u8wgpx`, commit `029cc8c`

## Correct final ruling

The programme does not prove or reduce `INT-SCME` to a smaller prime-detection theorem. It proves that the tested unconditional selected-residue variance mechanism cannot reach any post-terminal polynomial divisor band at the required scale.

The earlier description of two independent subordinate targets is retracted. With

\[
D_Q(n)=\sum_{2X<q\le Q,\ q\mid n}\log q,
\qquad R_Q(n)=\Lambda(n)-D_Q(n),
\]

`D_Q` vanishes on prime outputs. Once `INT-SCVAR` evaluates the band average, the registered `INT-SCPT` inequality beats the trivial bound by exactly the positive prime mass required by `INT-SCME`. Thus

\[
INT\text{-}SCPT\iff INT\text{-}SCME
\quad\text{given }INT\text{-}SCVAR,
\]

up to the registered asymptotic normalization.

The earlier chain `INT-SCME -> INT-SOCG` is also retracted. `INT-SCME` supplies only the first-cumulant input. The all-orders targets `INT-LCSK` and `INT-PWOC` remain unresolved at the same frontier level.

## Retained exact results

- deterministic microblock aggregation;
- weighted-mean implication to the first cumulant after proper prime-power subtraction;
- selected-residue collision energy
  \[
  \sum_{2X<q\le Q}\sum_a r_q(a)^2\ll RQ/\log Q+R^3;
  \]
- conditional exponent region `2 delta < rho < 1-delta`, with conditional optimum `rho=2/3`, `delta<1/3`;
- correction of the invalid `HQ log H` BDH use at `Q=H^(2/3)`;
- direct Friedlander–Iwaniec output-scale gap;
- unconditional large-sieve relative error exponent
  \[
  1/2+3\delta/2-\rho/2>0
  \]
  for every post-terminal `delta>0`, `rho<=1`.

## Honest frontier

\[
INT\text{-}SCME+INT\text{-}LCSK+INT\text{-}PWOC
\Longrightarrow INT\text{-}SOCG
\Longrightarrow INT\text{-}AOD
\Longrightarrow \text{eventual Fortune}.
\]

`INT-SCVAR` is an auxiliary GRH-hard/Montgomery-type variance conjecture. It is not a programme-sized substitute for prime detection. `INT-SCME` itself concerns primes in `(log P)^2` windows at exponentially sparse selected centres and is beyond current GRH-scale technology.

## Validation interpretation

The Python regressions validate exact algebra, exponent bookkeeping and finite diagnostics. The Lean artefact validates only the elementary real-number band-plus-tail implication; the large Lean job count is primarily dependency compilation and is not evidence for the open analytic inputs.

All prior validation records remain valid for the low-level statements. They do not validate the retracted high-level reduction language.
