# Final compiled-artifact and page-level QA — Papers II and III

## Exact source objects

- Publication commit: `4866d113898a48f23feb9752576c350af97c6985`
- Paper II source SHA-256: `0b9d8c96b0185827085955084507f7c1099803a4a1de46c0db2e3b81f3cdbb7a`
- Paper III source SHA-256: `7275ba02e7ae7a60d4bd3e524a2f1fd4d9fed639589b7d1ab7f08dd80f5fe675`

## Canonical visual-QA build

- GitHub Actions run: `30103406901` (`Build Papers II and III release artifacts`, run number 5)
- Workflow artifact: `8600618293`
- Artifact digest: `sha256:4c159708bda053c5d5288d8933f9dd2534a5286eb7e1e79af28c988e7de44ed7`
- Toolchain: Pandoc, XeLaTeX, LibreOffice Writer, Poppler and python-docx on Ubuntu 24.04
- PDF URL handling: inline-code URLs were converted to `\url{...}` for PDF layout and typeset with `xurl`; visible URL content was unchanged.

All workflow gates passed: exact source hashes, source-marker scan, PDF and DOCX generation, missing-glyph check, text extraction, key-claim checks, A4 preflight, embedded-font check, DOCX heading check and internal checksum verification.

## Final binary objects

| File | Pages | SHA-256 |
|---|---:|---|
| `Paper_II_Prime_Detection_at_Primorial_Centres.pdf` | 19 | `1e6c5a65e33ae0ab1f46dacf56ac845b87338efc180e884438731e6a42743336` |
| `Paper_II_Prime_Detection_at_Primorial_Centres.docx` | 20 rendered pages | `32da59889a824794bdd5aa142ff971518ecc3b32c4dfad21f79e3634e14d2d7b` |
| `Paper_III_Pair_Sum_Rigidity.pdf` | 15 | `1c7bd70d06ddf1088f8d19493119a78040bd5dd02a4cee57de18f4aaa8cfa468` |
| `Paper_III_Pair_Sum_Rigidity.docx` | 16 rendered pages | `039cf37d5886271d71d98b9b78669293f7002b391abccda2ae030d32d0b132cc` |

Both PDFs are A4. Every listed PDF font is embedded and subsetted. Both XeLaTeX logs contain zero missing-character warnings.

## Page-by-page inspection

Every rendered page was inspected at readable zoom:

- Paper II PDF: pages 1–19 — passed.
- Paper II DOCX: pages 1–20 — passed.
- Paper III PDF: pages 1–15 — passed.
- Paper III DOCX: pages 1–16 — passed.

The inspection covered title and metadata, abstracts, all theorem and proof blocks, displayed equations, tables, appendices, references, long URLs, page boundaries and final-page whitespace. No clipped text, overlap, black square, broken glyph, missing page, orphaned heading, truncated equation or right-margin overflow remains.

## Defect found and repaired during QA

The first otherwise successful canonical build displayed the raw GitHub repository URL past the right margin on Paper III PDF page 5. The source had represented the URL as inline code, so adding `xurl` alone did not affect it. The final build applies a PDF-only Pandoc filter that converts inline-code strings beginning with `http://` or `https://` to `\url{...}`, after which `xurl` provides safe line breaking. Page 5 was re-rendered and inspected; the complete URL now wraps inside the text block. The DOCX rendition already wrapped correctly.

This was a build-layer repair. It did not alter either reviewed Markdown source or any mathematical statement.

## Checksum result

The downloaded GitHub artifact digest matched exactly. Every per-paper checksum, combined-package checksum and release-ZIP checksum in the artifact verified successfully.

## Gate conclusion

**COMPILED-ARTIFACT PASS.**

Papers II and III have now passed source fidelity, independent finite reconstruction, exact-hash hostile review with disposition, automated binary preflight, checksum verification and page-by-page visual QA.

The only remaining external gate is review by human specialists. This report is not peer review, publication acceptance or a proof of Fortune's conjecture.
