# C0 — source freeze

## Frozen references

- parent branch: `gpt56/fortune-int-aod-occupancy-dual-v01-20260805`;
- parent head: `1d6ace4553bb88492dfceb894abd9e5d6713d426`;
- parent PR: #55;
- primary issue: #56;
- inherited formal bridge: `FortuneFormal.Integer.AdaptiveOccupancyCriterion`;
- inherited terminal result: `INT-SOCG => INT-AOD => eventual Fortune`.

## Required checks

1. Re-run the parent occupancy-dual static verifier.
2. Verify the ordinary-cumulant identity uses all ordered column tuples including repetitions.
3. Verify the rejected factorial/distinct-column identity is absent from executable claims.
4. Record exact hashes before C1.

## Pass condition

All inherited results reproduce with zero failures and no statement drift.

## Non-claim

C0 proves no new arithmetic estimate.