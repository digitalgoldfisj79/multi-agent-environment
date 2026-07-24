# Final compiled-artifact and page-level QA — Paper I

## Exact source object

- Publication commit: `401dff3b96525cdef6bd1b54d18f4450e5785ac8`
- Source Git blob: `1734d956dc10ce2c48ddd7c11b1df625ebdba0be`
- Source SHA-256: `0e0f8a0d89209b8f4dd8c589526a89d57bd536f4889fdcd9c902a09b1a62f157`

## Canonical visual-QA build

- GitHub Actions run: `30108438561`
- Workflow artifact: `8602624235`
- Artifact digest: `sha256:2ecb9ded8ce3e99d579470d9cfde286c10b5df4c63049a9e5474e1ac4effbdd5`
- Toolchain: Pandoc, XeLaTeX, LibreOffice Writer, Poppler and python-docx on Ubuntu 24.04

All automated gates passed:

- exact source hash and line count;
- claim-boundary markers;
- live Zenodo archive hash and portable manifest;
- PDF and DOCX generation;
- zero XeLaTeX missing-character warnings;
- A4 PDF preflight;
- all PDF fonts embedded and subsetted;
- PDF and DOCX text extraction;
- theorem/open-boundary marker checks;
- native Office Math presence;
- DOCX heading hierarchy checks; and
- per-file, release-ZIP, Zenodo-package and workflow-artifact checksum verification.

## Canonical binary objects

| File | Pages | SHA-256 |
|---|---:|---|
| `Paper_I_Collision_Geometry_and_Spectral_Laws.pdf` | 28 | `35b505c809afc178ced84060d7c67d04239552d42bff4c9a204cb06612757bd4` |
| `Paper_I_Collision_Geometry_and_Spectral_Laws.docx` | 29 rendered pages | `05577ce07d092e1b7113c51c470bdaac4ff36eb74df621dc76c4d0452d14e6ae` |
| `Paper_I_Hardened_Release.zip` | — | `c267ee0cdbcc30ddffdb478b866767bb8bdd5141bb36ad657b8ca6b37b68dbb7` |
| `Paper_I_Zenodo_New_Version_Package.zip` | — | `4d9cd4ca9572e103f36b401da7b58d2ad667b4c5a3fa8f5262ae3995195e3016` |

The downloaded GitHub artifact itself has SHA-256

`2ecb9ded8ce3e99d579470d9cfde286c10b5df4c63049a9e5474e1ac4effbdd5`,

matching the GitHub Actions artifact digest exactly.

## Page-by-page visual inspection

Every rendered page was inspected at readable zoom:

- final PDF pages 1--28 — passed;
- editable DOCX rendered pages 1--29 — passed.

The inspection covered:

- title, author, ORCID, date and DOI metadata;
- abstract and all section boundaries;
- every theorem, proposition, lemma, corollary and proof block;
- all displayed matrices, sums, asymptotic ranges and boxed estimates;
- HTE4 and HWF4 open-status labels;
- data/code availability and AI-assistance disclosure;
- remaining-problems and no-Fortune-claim boundary;
- the full reference list; and
- page breaks, margins and final-page whitespace.

No clipped text, overlap, right-margin overflow, black square, missing glyph, truncated equation, blank content page, orphaned heading or malformed reference remains. The large final whitespace in the DOCX reference-ending page is ordinary final-page whitespace and not a missing-page defect.

## Build transformations

The PDF is generated directly from the exact reviewed Markdown. The LaTeX package `xurl` is loaded solely to permit safe line breaking of the visible Zenodo DOI URL. The DOCX contains editable Office Math equations and A4 geometry. No theorem, hypothesis, exponent, constant, symbol or claim boundary changes in either build.

## Gate conclusion

**COMPILED-ARTIFACT PASS.**

Paper I has passed live-Zenodo fidelity, complete archive reproducibility, independent finite reconstruction, exact-hash hostile review with disposition, automated binary preflight, checksum verification and page-by-page visual QA.

The only remaining external gate is human specialist review. This report is not peer review, journal acceptance, or a proof of HTE4, HWF4, a prime-offset theorem or Fortune's conjecture.
