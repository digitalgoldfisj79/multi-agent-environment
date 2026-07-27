# Replacement Paper V release checklist

## Mathematical/source gates

- [x] Superseded Paper V quarantined for provenance.
- [x] Series bridge from Papers III--IV fixed.
- [x] Complete proof-source manifest.
- [x] Claim-status ledger.
- [x] Independent orbit, hook and singular-locus reconstruction.
- [x] Self-contained theorem manuscript.
- [x] Initial manuscript-only review archived and disposed.
- [x] Proof exposition strengthened after initial review.
- [x] Final exact-hash manuscript-only review passed and disposed.
- [x] Final manuscript Git blob and SHA-256 recorded.

Final reviewed source:

- commit: `4869f63e72f4e17078fa3e43fc18e60fcd6ff8ac`;
- manuscript Git blob: `89794e9337eaf328dfb13a627b9616a1e3a9553c`;
- manuscript SHA-256: `2a7df97840babfd4f92007f0fcdc70fe67faada264019cb3f396c1d05237c965`;
- referee job: `6a6708d47ef3c0846496a42b`;
- verdict: **PROVED AS STATED**.

## Build/QA gates

- [x] Canonical XeLaTeX A4 PDF.
- [x] Editable-prose A4 DOCX with exact TeX equation images and documented normalisations.
- [x] LaTeX source.
- [x] PDF/DOCX semantic and end-marker comparison.
- [x] PDF qpdf/preflight/font audit.
- [x] DOCX heading/metadata/A4/equation-package audit.
- [x] Independent LibreOffice DOCX-to-PDF render.
- [x] Every canonical PDF and rendered DOCX page visually inspected.
- [x] Per-file SHA-256 manifest.
- [x] Release ZIP downloaded and checksum-verified.
- [x] Build status and compiled-artifact QA record frozen.

The final page-level inspection covered the 11-page canonical PDF and the 16-page independent office render. No missing equation, broken glyph, literal source token, clipping, blank page or edge collision was found.

## Release boundary

- [x] Mark **INTERNAL TECHNICAL PASS — HUMAN SPECIALIST REVIEW OPEN**.
- [ ] External finite-field/algebraic-geometry review.
- [ ] External arithmetic-number-theory/prescribed-coefficient review.
- [ ] Human findings disposed; any source change resets downstream gates.
- [ ] Final Zenodo decision and DOI reservation.

The function-field crown and integer Fortune conjecture remain open.
