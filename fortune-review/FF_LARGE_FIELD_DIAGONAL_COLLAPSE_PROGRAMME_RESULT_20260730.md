# Large-field bilateral diagonal-collapse programme — execution result

**Date:** 30 July 2026  
**Programme:** `FF_LARGE_FIELD_DIAGONAL_COLLAPSE_PROGRAMME_V0_1_20260730.md`  
**Authoritative theorem note:** `FF_BILATERAL_DEFECT_DICHOTOMY_AND_ROUND12_CORRECTION_20260730.md`

## Verdict

The programme terminated at a registered decisive condition: **falsification**.

The proposed theorem

`q>k => empty cross-distinct bilateral incidence`

is false, as is universal `c+d=0`.

The falsification is independently verified from the original local-frequency definitions at `(q,k)=(11,3)`, and extended by a complete orbit-reduced cubic census through prime `q=59`.

## Gate ledger

| Gate | Result |
|---|---|
| 0 — intake and branch audit | **PASS.** Round 12 was treated as divergent external work; accepted pieces were rederived on the current PR branch. |
| 1 — correspondence and known-family audit | **PASS.** Correspondence, transpose, reflection and translation inclusions survive. |
| 2 — universal scalar coupling `CD0_FF` | **FALSIFIED.** Exact `(11,3)` incidence has `c=2`, `d=8`, hence `c+d=10 mod 11`. |
| 3 — `QGT_K_EMPTY` | **FALSIFIED.** There are 220 exact incidences at `(11,3)` and further nonzero panels through `q=59`. |
| 4 — complete small-field classification | **PROVED in the full zero-defect range.** Reflection/translation are exactly the zero-defect components; degree forces zero defect whenever `q<2k`, hence completeness for every `k>=q`. |
| 5 — corrected exceptional amplitude | **NOT REACHED as originally formulated.** A new nonzero-defect component must first be classified. |
| 6 — diagonal-only centred identity | **CLOSED.** Large-field support is not diagonal-only. |
| 7 — endpoint `FFPR` | **OPEN.** The target must include nonzero-defect components. |

## New exact boundary

Every incidence has a unique common defect polynomial `h` with

`rho C-lambda B = h P S'`,

`rho A-lambda D = h S P'`,

`deg h<=q-2k`.

- `h=0` gives exactly reflection or translation and forces `c+d=0`.
- `q<2k` forces `h=0`.
- `k<q<2k` is therefore genuinely empty.
- `k>=q` has the complete Round-12 two-family classification, with transpose at `k=q`.
- `q>=2k` admits nonzero `h`; this is the true large-field frontier.

## Replacement gate

The programme is replaced by

`NDC_FF`: classify and bound the nonzero-defect components in `q>=2k`, retaining their literal corrected `Delta_PS` amplitudes.

The cubic panels indicate a finite number of full `AGL(1,q)` orbits, but this is finite evidence only.

## Committed verification

- `fortune-review/scripts/ff_large_field_explicit_counterexample.py`
- `fortune-review/scripts/ff_large_field_cubic_falsification.cpp`
- `fortune-review/data/ff_large_field_cubic_falsification.txt`
- `.github/workflows/ff-large-field-bilateral-defect.yml`

## Remaining causal boundary

`NDC_FF -> corrected CBI_FF -> corrected FFPR -> theta restoration -> conductor coupling -> thinning`.

There remains no function-field-to-integer transfer theorem. Fortune's conjecture remains open.
