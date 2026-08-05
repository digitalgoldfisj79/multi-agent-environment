# M9 — closeout

**Status:** `PASSED`

The terminal outcome is

`METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE`.

The exact conditional anatomy retained is

\[
INT\text{-}SCVAR+INT\text{-}SCPT
\Longrightarrow INT\text{-}SCME.
\]

Validation record:

1. corrected exact Python regressions passed, including the unconditional large-sieve obstruction;
2. finite factor profiles and the all-composite control passed without promotion;
3. inherited `INT-SOCG`, `INT-AOD`, `INT-PFLI`, factor-band, `INT-ISC` and mainline verifiers passed;
4. targeted Lean job `6a72edc6a00abefd4b293482` passed with 8,655 jobs;
5. full Lean 4.32 package and formal trust audit passed in job `6a72efa0a00abefd4b2934a2` with 8,685 jobs;
6. GitHub Actions static and Lean jobs passed;
7. terminal sentinel `FORTUNE_INT_SCME_FULL_CLEANROOM_PASS` was emitted.

The initial unconditional M5 claim is excluded from evidence, as are the pre-correction execution job and the wording-only validator failure. A final frozen branch re-clone remains the final governance check.