# Current status

**Programme:** `FORTUNE_INT_AOD_OCCUPANCY_DUAL_V0_1`  
**Branch:** `gpt56/fortune-int-aod-occupancy-dual-v01-20260805`  
**State:** BUILT; NOT YET EXECUTED  
**Primary target:** `INT-AOD`  
**Primary candidate reduction:** `INT-CCB`

## Gate state

- O0: ready — source freeze.
- O1: blocked — detector admissibility and formal weighted criterion.
- O2: blocked — Bernoulli/hypergeometric cover dual.
- O3: blocked — finite-degree and coefficient-cost audit.
- O4: blocked — connected-cumulant compression.
- O5: blocked — arithmetic connected-correlation expansion.
- O6: blocked — conditional row-uniform Hardy–Littlewood benchmark.
- O7: blocked — rowwise parity-breaking bilinear lane.
- O8: blocked — adversarial and exact small-panel diagnostics.
- O9: blocked — closeout.

## Execution order

1. Run O0–O3 without expensive external compute.
2. Build exact small panels and adversarial controls in O8 early enough to select between O4 and O7.
3. Open O4/O5 only if connected quantities show genuine compression and the analytic convergence criterion has a plausible scale.
4. Open O7 if the connected lane fails or if the exact decomposition exposes a lower-arity rowwise bilinear target.
5. Use O6 to state the sharp conditional benchmark, never as a substitute for the unconditional programme.

No programme compute job is currently registered.