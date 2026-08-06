# Build status

**Programme:** `FORTUNE_INT_PWOC_SQUAREFREE_V0_1`  
**Date:** 6 August 2026  
**Branch:** `gpt56/fortune-int-pwoc-sf-v01-20260806`  
**State:** `BUILT_VALIDATION_PENDING`

## Completed

- exact target ladder frozen;
- source-weight admissibility and no-hand-selection rule frozen;
- squarefree collision row norm identified as the primary arithmetic object;
- exact finite additive-character/kernel regressions implemented;
- divisor-subset count regressions implemented for support orders one and two;
- inverse and inverse-square diagnostic profiles implemented;
- Lean deterministic bridge added and imported at package root;
- targeted and full-package CI workflow added;
- claim matrix, terminal outcomes and forbidden overclaims frozen.

## Lean claims awaiting kernel validation

- `totalCollision_le_of_rowBudget`;
- `weightedEnergy_le_of_collisionBudget`;
- `weightedEnergy_le_of_rowCollisionBudget`.

No analytic theorem is represented by these claims. They formalise only finite aggregation under explicit assumptions.

## Execution frontier

The programme is ready to execute from P0. The first substantive decision is P4: identify and freeze one actual squarefree coefficient family that arises in a local-factor or source block and determine whether its absolute collision kernel can be subcritical.

The unrestricted and surrogate profiles are falsification controls only.

## Explicit nonclaims

No squarefree-composite energy estimate has yet been proved.  
No source-compatible coefficient contract has yet passed P4.  
No transfer to RUHL-FM or INT-SOCG has yet been proved.  
No proof of INT-AOD or Fortune is claimed.
