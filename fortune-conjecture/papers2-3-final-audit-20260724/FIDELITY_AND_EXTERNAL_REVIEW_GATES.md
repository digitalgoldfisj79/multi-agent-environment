# Fidelity and external-review gates — Papers II and III

## Exact objects

- Publication commit: `4866d113898a48f23feb9752576c350af97c6985`
- Paper II SHA-256: `0b9d8c96b0185827085955084507f7c1099803a4a1de46c0db2e3b81f3cdbb7a`
- Paper III SHA-256: `7275ba02e7ae7a60d4bd3e524a2f1fd4d9fed639589b7d1ab7f08dd80f5fe675`

## F1 — frozen-source fidelity: passed

Paper II was reconstructed from its four archived manuscript parts. Paper III combines its concise narrative with the complete frozen kernel, singular-series and conditional-theorem proofs, with Appendix B rewritten into publication mathematics. The detailed maps are recorded in the two fidelity matrices.

## F2 — independent finite reconstruction: passed

The independent implementation, extended final Appendix B panels and shipped validators reproduce the declared finite multiplicity, moment, Möbius and singular-series identities. `INDEPENDENT_CHECKS.md` records the exact panels and limits.

## F3 — fresh exact-hash hostile review: passed after disposition

- Paper II: Qwen3-14B-AWQ job `6a63765c7ef3c08464967898`.
- Paper III: Qwen3-14B-AWQ job `6a63743ddb23d7a7ec1ca9cb`.

Paper III received a proved verdict with no fatal or major defect. Paper II's listed objections confuse the proof of a criterion with proof of its displayed hypothesis or overlook explicit text already present. All objections are resolved in `HOSTILE_REVIEW_DISPOSITION.md`.

## F4 — compiled package integrity: passed

Canonical visual-QA build:

- GitHub Actions run: `30103406901`.
- Workflow artifact: `8600618293`.
- Artifact digest: `sha256:4c159708bda053c5d5288d8933f9dd2534a5286eb7e1e79af28c988e7de44ed7`.

Passed checks:

1. PDFs built directly from the exact Markdown sources with XeLaTeX;
2. editable DOCX files generated with documented notation-only conversions;
3. extracted mathematical text and claim-boundary statements verified;
4. A4, embedded-font and zero-missing-glyph PDF preflight passed;
5. DOCX heading and structural checks passed;
6. every rendered PDF and DOCX page inspected;
7. every per-file, per-package and artifact SHA-256 checksum verified; and
8. separate Paper II, Paper III and combined release archives created.

The page-level inspection covered 19 Paper II PDF pages, 20 Paper II DOCX pages, 15 Paper III PDF pages and 16 Paper III DOCX pages. A clipped raw URL found in an earlier Paper III PDF was repaired at the build layer and re-inspected. `VISUAL_QA_REPORT.md` records the complete result and binary hashes.

Any source edit changes the hash and reopens F1 through F4.

## F5 — external human review: open

Paper II should now be read by an analytic-number-theory specialist familiar with prime-detection variance reductions and character sums. Paper III should be read by an analytic or probabilistic number theorist familiar with additive energy, singular series and conditional Hardy--Littlewood arguments.

## Claim boundary

- Paper II leaves the source-to-frame bridge, reciprocal sampling target, direct variance estimate and Fortune's conjecture open.
- Paper III leaves its block-averaged Hardy--Littlewood hypotheses and exceptional-set transference theorem open.
- Internal audit and model review are not peer review.
