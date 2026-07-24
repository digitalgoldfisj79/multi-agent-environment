# Quality assurance and package integrity

## Canonical source and result artifacts

The canonical reviewed manuscript source is:

- path: `publications/fortune-papers-ii-vi-20260724/paper4_random_order/manuscript.md`;
- Git blob: `1a3d39d974bfa37d31c100f536dcaa1b74f6d688`;
- SHA-256: `548460849cc9c6125fbe59d0a4f2f37ec680761174c25556b5e781a8ae9372f1`.

The canonical clean-room result artifact is:

- `independent_audit_results.json`.

No file named `independent_audit_results.txt` is canonical, and the final release package does not reference or require one.

## Scope of the result artifact

`independent_audit_results.json` records finite exact or numerical checks of selected identities and exponent calculations. Its `PASS` status means that those declared checks completed successfully. It does not by itself certify manuscript completeness, fidelity, ledger exhaustiveness, novelty, asymptotic correctness, publication suitability or human peer review. Those questions are controlled separately by the fidelity matrix, independent ledger reconstruction, hostile review and compiled-artifact QA.

## Canonical compiled artifacts

The reproducible GitHub build is:

- workflow run: `30085400790`;
- publication commit: `af9350f06e41e94d79f583b2e8fca45b55b92852`;
- artifact ID: `8593522378`;
- artifact digest: `sha256:1875d3965d611cffa0a70afc223caf0e3119d93f79183f3f7a9be214f3486a51`.

All workflow steps passed.

Canonical file hashes:

- PDF: `dc5ff454826f605d5fd4db4ba02f6a35df1013bde1cfe9a9d9e26a6c8fc6f1a3`;
- DOCX: `3ecac48465573b9305cafb119779a5e17c65b2bd2fc05f7d376ec55895b3b61b`;
- internal release ZIP: `19c790caa196cf6374f62f90e4d9da4ea2dfc559a4894fd8e7dfdb4a62b5ec43`.

The release archive contains the exact source, PDF, DOCX, audit records, raw hostile review, issue disposition, independent ledger reconstruction, result JSON, extracted text, typesetting-normalisation record, build manifest and `SHA256SUMS`. All listed hashes verified after download.

## Completed QA

1. Frozen-source fidelity matrix — passed.
2. Independent ledger reconstruction — passed.
3. Fresh manuscript-only hostile review and issue disposition — passed.
4. Source SHA-256 enforcement in clean build environment — passed.
5. DOCX and PDF compilation — passed.
6. Normalised text extraction checks for theorem, matching lemma, disclosure and document scale — passed.
7. PDF preflight — openable, unencrypted, text-native, 12 pages, no XFA and no warnings.
8. DOCX accessibility audit — zero high-, medium- or low-severity findings.
9. DOCX heading hierarchy — 12 Heading 1 and 18 Heading 2 paragraphs, without a skipped level.
10. Page-by-page visual inspection — all 12 PDF pages and 15 DOCX pages passed; no raw TeX, clipping, overlap, missing glyphs, malformed equations, blank contents field or duplicated section numbering.
11. Per-file and ZIP checksum verification — passed.

The final PDF is generated directly from the exact reviewed source using XeLaTeX. The editable DOCX uses two documented notation-only rendering normalisations required by Pandoc's OMML writer; these do not change mathematical content or numbering. See `TYPESETTING_NORMALISATIONS.md` in the release package.

## Gate status

- Frozen-source proof audit: passed at internal technical level.
- Finite clean-room checks: passed for the declared cases.
- Manuscript fidelity: passed.
- Independent ledger reconstruction: passed.
- Fresh manuscript-only hostile review: passed after issue disposition.
- Compiled-artifact integrity and visual QA: passed.
- Human specialist review: not started.
- Journal submission or final Zenodo release: not yet cleared by human review.

## Failure rule

Any source edit, missing referenced file, hash mismatch, binary/source discrepancy, stale gate statement or change to the compilation pipeline reopens package integrity. A changed manuscript must receive a new SHA-256, fidelity update, hostile-review disposition and compiled-artifact QA before circulation.
