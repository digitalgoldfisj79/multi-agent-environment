# Build status

**Programme:** `FORTUNE_INT_PWOC_SQUAREFREE_V0_1`  
**Date:** 6 August 2026  
**Branch:** `gpt56/fortune-int-pwoc-sf-v01-20260806`  
**State:** `BUILT_AND_VALIDATED_READY_FOR_P0`

## Completed

- exact target ladder frozen;
- source-weight admissibility and no-hand-selection rule frozen;
- squarefree collision row norm identified as the primary arithmetic object;
- exact finite additive-character/kernel regressions implemented and passed;
- divisor-subset count regressions passed for support orders one and two;
- inverse and inverse-square diagnostic profiles passed;
- Lean deterministic bridge added and imported at package root;
- targeted and full-package CI workflow added and passed;
- claim matrix, terminal outcomes and forbidden overclaims frozen.

## Kernel-checked deterministic bridge

The module

`FortuneFormal.Integer.SquarefreeCompositeEnergyCriterion`

kernel-checks:

- `totalCollision_le_of_rowBudget`;
- `weightedEnergy_le_of_collisionBudget`;
- `weightedEnergy_le_of_rowCollisionBudget`.

Every analytic input remains visible in the theorem signatures. No character-sum estimate, divisor estimate, source decomposition or prime-correlation theorem is represented by these claims.

## Validation record

Workflow run `31077264106`:

- static trust audit and exact regressions: **PASS**;
- targeted Lean build: **PASS**;
- full formal package build: **PASS**;
- new-file scan for `sorry`, `admit`, `axiom` and `unsafe`: **PASS**;
- Lean version: `4.32.0`.

The first targeted Lean run failed because an `add_le_add_left` application had its additive term on the wrong side. The proof was corrected to use the actual inequality orientation; no assumption or theorem statement was weakened. The complete rerun then passed.

## Execution frontier

The programme is ready to execute from P0. The first substantive decision is P4: identify and freeze one actual squarefree coefficient family arising in a local-factor or source block, then determine whether its absolute collision kernel is subcritical.

The unrestricted, inverse and inverse-square profiles are falsification or regression controls only. They are not substitutes for the actual source weights.

## Explicit nonclaims

No squarefree-composite energy estimate has yet been proved.  
No source-compatible coefficient contract has yet passed P4.  
No transfer to RUHL-FM or INT-SOCG has yet been proved.  
No proof of INT-AOD or Fortune is claimed.
