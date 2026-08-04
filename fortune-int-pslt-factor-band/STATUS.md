# Current status

**Programme:** `FORTUNE_INT_PSLT_BUCHSTAB_FACTOR_BAND_V0_1`  
**Branch:** `gpt56/fortune-int-pslt-buchstab-factor-band-v01-20260804`  
**State:** CLOSED  
**Terminal outcome:** `REDUCED_TO_CRITICAL_FACTOR_INCIDENCE`

## Gate rulings

- B0: passed — source and lower-tail spine frozen.
- B1: passed — explicit threshold compressed to order `X log X`.
- B2: closed — natural recurrence cannot propagate admissible offsets inside `H`.
- B3: passed — exact least-factor partition derived.
- B4: closed at explicit scale — first factor lies beyond the `s=2` lower-sieve boundary.
- B5: passed as reduction — isolated `INT-PFLI`.
- B6: passed as implication — `INT-PFLI` implies compressed `INT-PSLT` and eventual Fortune.
- B7: passed — clean-room static, regression, formal and inherited audits completed.

## Validation

- static/regression sentinel: `6a724dbca00abefd4b29284e`;
- targeted Lean build: `6a724ddda00abefd4b292854`, 8,657 jobs;
- full clean-room closeout: `6a724e7a6b79c09949c22885`, 8,682 jobs, failure count zero.

## Remaining open theorem

`INT-PFLI`, the signed selected-centre post-level factor-incidence theorem in `B5_CRITICAL_FACTOR_INCIDENCE.md`.

The programme does not claim `INT-PFLI`, `INT-PSLT`, or Fortune.
