# Compiled artifact quality assurance

## Reviewed source

- Path: `publications/fortune-papers-ii-vi-20260724/paper4_random_order/manuscript.md`.
- Git blob: `1a3d39d974bfa37d31c100f536dcaa1b74f6d688`.
- SHA-256: `548460849cc9c6125fbe59d0a4f2f37ec680761174c25556b5e781a8ae9372f1`.

The source included in the release artifact is byte-identical to this reviewed object.

## Canonical GitHub build

- Workflow: `Build Paper IV release artifacts`.
- Workflow run: `30085400790`.
- Publication branch commit: `af9350f06e41e94d79f583b2e8fca45b55b92852`.
- Actions artifact ID: `8593522378`.
- Actions artifact digest: `sha256:1875d3965d611cffa0a70afc223caf0e3119d93f79183f3f7a9be214f3486a51`.
- Result: every workflow step passed, including source-hash enforcement, compilation, audit-record assembly, normalised DOCX/PDF extraction checks, manifest generation and artifact upload.

## PDF

- Filename: `paper4_random_order.pdf`.
- SHA-256: `dc5ff454826f605d5fd4db4ba02f6a35df1013bde1cfe9a9d9e26a6c8fc6f1a3`.
- Toolchain: Pandoc plus XeLaTeX directly from the exact reviewed Markdown.
- Format: A4, 12 pages, 24 mm margins.
- Extraction: passed.
- Preflight: openable, unencrypted, text-native, no XFA and no warnings.
- Visual QA: all 12 pages rendered at 180 dpi and inspected; no clipping, overlap, missing glyphs, raw TeX, malformed equations or page-boundary defects. Equation tags are preserved at the right margin.
- Control: the final green artifact is pixel-identical across all 12 pages to the previously inspected canonical XeLaTeX rendering.

## DOCX

- Filename: `paper4_random_order.docx`.
- SHA-256: `3ecac48465573b9305cafb119779a5e17c65b2bd2fc05f7d376ec55895b3b61b`.
- Toolchain: Pandoc OMML plus python-docx A4 page setup.
- Render-only normalisations: the two `\Bigl`/`\Bigr` pairs become `\left`/`\right`, and each of the 48 TeX `\tag` commands becomes an appended equation label because Pandoc's DOCX writer does not preserve TeX equation tags. These changes are documented in `TYPESETTING_NORMALISATIONS.md` and do not change mathematical content.
- Format: A4, 15 rendered pages, 24 mm horizontal and 23 mm vertical margins.
- Extraction: passed.
- Accessibility: zero high-, medium- or low-severity findings.
- Heading structure: 12 Heading 1 and 18 Heading 2 paragraphs, with no skipped level.
- Visual QA: all 15 pages rendered and inspected; no clipping, overlap, missing glyphs, raw TeX, blank contents field or duplicated section numbering. All 48 equation labels are present.

## Release archive

- Canonical GitHub-generated internal ZIP: `paper4_random_order_release.zip`.
- SHA-256: `19c790caa196cf6374f62f90e4d9da4ea2dfc559a4894fd8e7dfdb4a62b5ec43`.
- The archive includes the exact source, PDF, DOCX, extracted text, typesetting-normalisation record, audit reports, hostile-review archive and disposition, independent ledger reconstruction, clean-room JSON, build manifest and per-file `SHA256SUMS`.
- Every checksum in `SHA256SUMS` verified successfully after download.

## Gate decision

Compiled-artifact integrity, source-to-binary extraction checks, PDF preflight, DOCX accessibility, checksum verification and page-by-page visual QA all pass. The only remaining scientific gate is external human specialist review. This technical pass is not human peer review and is not publication acceptance.
