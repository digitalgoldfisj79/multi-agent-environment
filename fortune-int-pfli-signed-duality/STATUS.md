# Current status

**Programme:** `FORTUNE_INT_PFLI_SIGNED_DUALITY_V0_1`  
**Branch:** `gpt56/fortune-int-pfli-signed-duality-v01-20260804`  
**State:** CLOSED  
**Outcome:** `REDUCED_TO_GROWING_ARITY_GENERATING_FUNCTION`

## Gate rulings

- D0: passed — source and one-defect definitions frozen.
- D1: passed formally — `INT-PFLI` collapses exactly to the prime-pair lower tail.
- D2: passed as reduction — isolated the strictly softer adaptive occupancy detector `INT-AOD`.
- D3: passed — exact factorial generating-function expansion and Bonferroni bounds derived.
- D4: passed exactly — fixed-order moment data cannot distinguish a failed panel from a nonfailed panel when `2^K<=N`.
- D5: passed — moment-only resolution requires coupled prime-correlation arity `Omega(log X)`.
- D6: closed as direct application — audited asymptotic-sieve, switching, and finite Buchstab frameworks lack the required row-uniform post-level parity-breaking input.
- D7: passed — full clean-room validation completed with zero failures.

## Remaining open theorem

`INT-AOD`, equivalently the all-orders adaptive occupancy generating-function estimate in `D2_ADAPTIVE_OCCUPANCY.md`.

## Validation

- static job: `6a7253f86b79c09949c228e4`;
- targeted Lean job: `6a7254e06b79c09949c228e8`, 8,658 jobs;
- full clean-room job: `6a7255a96b79c09949c228f0`, 8,683 jobs;
- failure count: zero.
