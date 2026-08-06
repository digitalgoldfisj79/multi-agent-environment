# Build status

**Programme:** `FORTUNE_INT_AOD_OCCUPANCY_DUAL_V0_1`  
**State:** BUILT AND STATICALLY VALIDATED; RESEARCH NOT EXECUTED  
**Branch:** `gpt56/fortune-int-aod-occupancy-dual-v01-20260805`

## Build validation

Hugging Face job `6a72b306a00abefd4b29302e` completed with failure count zero.

Terminal sentinel:

`FORTUNE_INT_AOD_OCCUPANCY_DUAL_BUILD_PASS`

Validated components:

- weighted detector finite implication;
- Bernoulli and hypergeometric cover identities;
- detector scale and exact-cover degree ledger;
- factorial moment/cumulant recurrence;
- even/odd zero-row adversaries through `K=12`;
- matching private-column degree and overlap statistics for every `K>=1`;
- required-file, claim, gate, and no-promotion checks.

## Boundary correction found by validation

The first adversarial version incorrectly asserted matching total private columns at `K=0`. At that order the panels match only the zeroth moment. The column-statistics strengthening is valid from `K>=1`; the regression and its description were corrected before the passing build.

## Not yet done

- no O0–O9 research gate has been executed;
- no new Lean module has been compiled;
- no exact primorial panel has been generated;
- neither `INT-CCB`, `INT-AOD`, nor Fortune is claimed;
- no programme compute job remains active after build validation.
