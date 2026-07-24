# Fidelity and external-review gates

## Current state

The technical questions are now separated and answered as follows:

1. Is there a continuous proof in the frozen research source? **Yes.**
2. Do independent finite checks reproduce selected structural identities? **Yes.**
3. Does the exact rebuilt manuscript reproduce the frozen proof at dependency level? **Yes, editorially.**
4. Has a fresh manuscript-only hostile review left an unresolved fatal or major issue? **No.**
5. Do the compiled PDF, DOCX and release archive faithfully preserve the cleared source and pass technical QA? **Yes.**

Final reviewed source:

- manuscript SHA-256: `548460849cc9c6125fbe59d0a4f2f37ec680761174c25556b5e781a8ae9372f1`;
- Git blob: `1a3d39d974bfa37d31c100f536dcaa1b74f6d688`;
- fidelity matrix: `REBUILT_MANUSCRIPT_FIDELITY_MATRIX.md`;
- ledger reconstruction: `INDEPENDENT_LEDGER_RECONSTRUCTION.md`;
- hostile-review archive: `FRESH_HOSTILE_REVIEW_FINAL_QWEN3_14B_AWQ.md`;
- issue disposition: `FINAL_HOSTILE_REVIEW_DISPOSITION.md`;
- compiled-artifact record: `COMPILED_ARTIFACT_QA.md`.

All internal technical gates are closed. Human specialist review remains open.

## Gate F1 — frozen-source fidelity: passed

The manuscript was checked against:

- `RQM_PROOF.md`: `53f63f662f5a9d6e750a592ba8bcba6cf4bc9095`;
- `PAPER2_ADDENDUM.md`: `71a9ad70c7164bcd94b92743fff3d8088c9a158b`;
- `CONDITIONAL_HL_BLOCK.md`: `41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef`;
- archived Paper II definitions: `79da1c81b57b051cf8527889e84a6fe1161eb3fe`.

Every load-bearing row in `REBUILT_MANUSCRIPT_FIDELITY_MATRIX.md` is classified as verbatim-equivalent, expanded without claim change, or a precisely identified external dependency. The sole imported mathematical result is the cited Paper II Frobenius comparison.

The rebuilt manuscript includes the quantitative frame hypotheses, theorem quantifiers, exact configuration taxonomy and multiplicities, ordered partition identity, contour estimate, Gauss/CRT expansion, bad-character count, coordinate bijection, matching, pattern domination, complete ledger, harmonic assembly and scope limitation.

## Gate F2 — independent ledger reconstruction: passed

`INDEPENDENT_LEDGER_RECONSTRUCTION.md` independently enumerates the ordered-pair configurations for `N=3,...,10`, without calling the original audit code. It verifies:

- total multiplicity `M(M-1)`;
- type-S multiplicity `N` and all other multiplicities `1`;
- no missing or duplicate ledger assignment; and
- the declared exponent scales.

All panels pass. The binding classes remain `C2a`, `C2b`, and `C2d`, each at `M(log X)^9` with no positive power-of-`X` cushion.

## Gate F3 — fresh hostile manuscript-only review: passed after disposition

The exact final manuscript was reviewed alone by `Qwen/Qwen3-14B-AWQ` in Hugging Face job `6a6325e7db23d7a7ec1ca14a`.

- manuscript SHA-256: `548460849cc9c6125fbe59d0a4f2f37ec680761174c25556b5e781a8ae9372f1`;
- prompt SHA-256: `1bb3ba966a21ee69bd24c589aea778f3b4c326329e924585323ffd1b3bb77b67`;
- headline verdict: **proved**.

The raw response also listed three objections. They are rebutted in `FINAL_HOSTILE_REVIEW_DISPOSITION.md`:

1. equation (3.3) equals `M(M-1)` exactly;
2. Lemma 5.2 explicitly assumes `X>8/eta^2`; and
3. Lemma 6.3 explicitly bounds the contour prefactor, edge ratios and all 15 non-all-bad patterns.

No fatal or major model-review issue remains unresolved.

## Gate F4 — compiled package integrity: passed

Canonical build:

- GitHub Actions workflow run: `30085400790`;
- publication commit: `af9350f06e41e94d79f583b2e8fca45b55b92852`;
- artifact ID: `8593522378`;
- artifact digest: `sha256:1875d3965d611cffa0a70afc223caf0e3119d93f79183f3f7a9be214f3486a51`.

All workflow steps passed. The final files are:

- PDF SHA-256: `dc5ff454826f605d5fd4db4ba02f6a35df1013bde1cfe9a9d9e26a6c8fc6f1a3`;
- DOCX SHA-256: `3ecac48465573b9305cafb119779a5e17c65b2bd2fc05f7d376ec55895b3b61b`;
- canonical internal ZIP SHA-256: `19c790caa196cf6374f62f90e4d9da4ea2dfc559a4894fd8e7dfdb4a62b5ec43`.

The package includes the exact reviewed source, compiled documents, audit files, extracted text, clean-room JSON, typesetting-normalisation record, build manifest and `SHA256SUMS`. Every checksum verified after download.

The 12-page PDF passed extraction, openability, encryption, text-native and XFA checks and was inspected page by page at 180 dpi. The 15-page DOCX passed extraction, accessibility and heading-hierarchy checks and was inspected page by page. No clipping, overlap, raw TeX, missing glyph, malformed equation, blank contents field or duplicated heading numbering remains. Details are in `COMPILED_ARTIFACT_QA.md`.

The canonical clean-room result file is `independent_audit_results.json`; the final package contains no stale reference to a nonexistent `independent_audit_results.txt`.

## Gate F5 — human specialist review: open

Send the technically cleared package to:

- an analytic/probabilistic number theorist for the random-order conditioning and contour mechanism; and
- a character-sum specialist for Gauss/CRT normalisation, the sixth moment and the no-cushion ledger.

The request should ask them to verify the contour/coordinate/matching/ledger chain, assess novelty and publication value, and confirm the precise Paper II dependency. LLM assistance must be disclosed before review begins.

## Consultation sequencing

Paper IV should lead the external consultation sequence. The Airy package requires a different, narrower specialist pool and should be sent later or separately.
