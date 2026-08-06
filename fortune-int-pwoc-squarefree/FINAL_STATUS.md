# Final status — INT-PWOC-SF execution

**Programme:** `FORTUNE_INT_PWOC_SQUAREFREE_V0_1`  
**Date:** 6 August 2026  
**Branch:** `gpt56/fortune-int-pwoc-sf-v01-20260806`  
**State:** `EXECUTED_VALIDATION_PENDING`

## Terminal outcomes

- `FIXED_ORDER_COMPOSITE_EXTENSION_PROVED`
- `SOURCE_WEIGHT_CONTRACT_NOT_AVAILABLE`
- `NO_TRANSFER_TO_RUHL_OR_SOCG`

## The proved theorem

For squarefree moduli of fixed order `r`, all prime factors exceeding `2X`, and frozen nonnegative weights satisfying

\[
\beta(q)q\le U_r,
\]

the primorial-walk collision radius obeys

\[
R_\beta\le U_r{n-1\choose r+1}.
\]

Consequently

\[
\mathcal E_\beta(a)
\le
\left(D_\beta+U_r{n-1\choose r+1}\right)\|a\|_2^2.
\]

This extends the prime-modulus collision method to every fixed squarefree support order under an explicit bounded-weight contract. The divisor-subset growth is not hidden.

## Negative result for unrestricted weights

The W0 contract is too broad. A weight concentrated on one modulus dividing one primorial gap has `D_beta=1` and `R_beta>=1`, so a uniform `R_beta=o(D_beta)` theorem is impossible for unrestricted nonnegative weights.

## Source audit

The repository does not instantiate an actual source coefficient family. It names admissible source identities but does not freeze the truncations, conductor blocks, signed coefficients, normalization, or source-to-row map needed to define W2. No W3 majorant is therefore available.

PWOC-SF2 remains open.

## Transfer audit

The fixed-order theorem cannot yet be inserted into either:

- the RUHL-FM residual budget, because no exact source inequality maps `A_{b,k}` to the weighted energy; or
- the INT-SOCG dependence radius, because no source-to-connected-frame identity supplies its coefficient masses and losses.

## Finite execution

Exact panels through `X=50`, `Q=50000` verify:

- the pair support cap;
- the fixed-order row cap;
- the exact character/kernel identity on the original panels;
- the W0 adversarial obstruction;
- small diagnostic ratios for inverse and inverse-square surrogate profiles.

The surrogate ratios are not promoted as source evidence.

## Formal boundary

The Lean module already kernel-checks deterministic energy aggregation. This execution adds `fixedOrderChooseSum`, the exact hockey-stick summation used in the fixed-order row budget. Final status is withheld until the targeted and full-package builds recheck the extended module and all exact regressions pass.

## Explicit nonclaims

No actual source-compatible squarefree-composite theorem has been proved.  
No proof of PWOC-SF2 or full INT-PWOC is claimed.  
No transfer to RUHL-FM or INT-SOCG is claimed.  
No proof of INT-AOD or Fortune is claimed.
