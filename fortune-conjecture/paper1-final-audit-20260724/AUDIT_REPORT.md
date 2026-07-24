# Adversarial audit — Paper I

## Current decision

**SOURCE-LEVEL PASS — COMPILED-ARTIFACT AND HUMAN-REVIEW GATES OPEN.**

Paper I has been reconstructed directly from the live Zenodo-deposited reviewed source and taken through exact archive verification, the full portable validator suite, an independent finite reconstruction and a fresh exact-hash hostile review.

## Exact reviewed object

- Publication commit: `401dff3b96525cdef6bd1b54d18f4450e5785ac8`
- Path: `publications/fortune-papers-ii-vi-20260724/paper1_collision_geometry/manuscript.md`
- Git blob: `1734d956dc10ce2c48ddd7c11b1df625ebdba0be`
- SHA-256: `0e0f8a0d89209b8f4dd8c589526a89d57bd536f4889fdcd9c902a09b1a62f157`
- Length: 1,909 lines

The final source is a deterministic metadata/disclosure-only transformation of the anonymous reviewed manuscript deposited under DOI `10.5281/zenodo.21426465`.

## Result boundary

Paper I proves the results it labels proved, including:

1. the exact character fourth-moment identity;
2. the exact endpoint-transport identity and averaged low-transport theorem;
3. the weighted offset-slice large-divisor incidence theorem;
4. average almost-injectivity and nearby collision bounds;
5. the complete endpoint-graph affine rank and Smith-form classification;
6. finite-group occupancy probabilities;
7. exact pair-overlap and transport decompositions;
8. closure of the three-shared-endpoint sector;
9. the disjoint median-channel identity and independent-prefix covariance laws;
10. the exact non-Gaussian fourth-moment polynomial;
11. the support-family divisor estimate;
12. sparse block-composition closure;
13. square-function comparison and local within-block correction;
14. the conditional edge implication under HWF4;
15. the additive-frequency fourth moment; and
16. common-translation boundary shortening, primitive rank loss and zero-frequency multiplier obstruction.

It does **not** prove HTE4, HWF4, FBHE4 or RQHE4. It does not provide the signed sieve or von Mangoldt bridge, a prime-offset theorem or Fortune's conjecture.

## Zenodo fidelity

The live Zenodo API exposes exactly the portable archive and checksum file. The archive SHA-256 is

`651b17c92371b73eae5f224fdea78f85c6ea82bb94da6514d2b482a6b441a166`.

Workflow run `30107291339` downloaded those live bytes, verified the archive, its 61-file manifest and the frozen source hash before producing the final manuscript. The full mapping is in `FIDELITY_MATRIX.md`.

## Independent and shipped checks

Hugging Face job `6a638a047ef3c0846496797f` downloaded the live Zenodo files into a clean container and ran the complete Python and C++ validation sequence. The result was:

`ALL REQUESTED CHECKS PASSED`.

This included all shipped production validators, the separately written independent audit and both C++ production drivers. The detailed panels and exact residuals are recorded in `INDEPENDENT_CHECKS.md`.

## Fresh exact-hash hostile review

The exact final manuscript was supplied alone to `Qwen/Qwen3-14B-AWQ` in Hugging Face job `6a638c45db23d7a7ec1cabd8`.

- Prompt SHA-256: `682d904cd27d09c2d4bd665a969c6115ae8ab683e0375cf9a514cce5a31ef6b7`
- Completion timestamp: `2026-07-24T16:04:30.820081+00:00`

The review reports high confidence in the validity of the results and no fatal or major defect. Its two minor reservations concern finite constants and matrix eigenvalues not expanded line by line in the paper; both are independently reconstructed exactly in the deposited audit and are resolved in `HOSTILE_REVIEW_DISPOSITION.md`.

## Fidelity incident

An initial manual repository commit contained a compressed derivative rather than the complete reviewed manuscript. The mismatch was caught by the line-count and hash audit before hostile review or release. The deterministic Zenodo reconstruction replaced it. It is superseded and has no audit or release status.

## Gate ledger

1. Live Zenodo archive integrity — **passed**.
2. Frozen-source fidelity — **passed**.
3. Complete portable validation suite — **passed**.
4. Independent finite reconstruction — **passed**.
5. Fresh exact-hash hostile review — **passed after disposition**.
6. Compiled PDF/DOCX/ZIP integrity and page-level QA — **open**.
7. External human specialist review — **open**.

This is an internal technical audit, not peer review, publication acceptance or proof of any open theorem.
