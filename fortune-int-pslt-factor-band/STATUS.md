# Current status

**Programme:** `FORTUNE_INT_PSLT_BUCHSTAB_FACTOR_BAND_V0_1`  
**Branch:** `gpt56/fortune-int-pslt-buchstab-factor-band-v01-20260804`  
**State:** RESEARCH COMPLETE; VALIDATION PENDING  
**Terminal outcome:** `REDUCED_TO_CRITICAL_FACTOR_INCIDENCE`

## Gate rulings

- B0: passed — source and lower-tail spine frozen.
- B1: passed — explicit threshold compressed to order `X log X`.
- B2: closed — natural recurrence cannot propagate admissible offsets inside `H`.
- B3: passed — exact least-factor partition derived.
- B4: closed at explicit scale — first factor lies beyond the `s=2` lower-sieve boundary.
- B5: passed as reduction — isolated `INT-PFLI`.
- B6: passed as implication — `INT-PFLI` implies compressed `INT-PSLT` and eventual Fortune.
- B7: validation pending.

## Remaining open theorem

`INT-PFLI`, the signed selected-centre post-level factor-incidence theorem in `B5_CRITICAL_FACTOR_INCIDENCE.md`.

No programme compute job should remain active after B7 validation.
