# Replacement Paper VI typesetting normalisations

The reviewed Markdown source is authoritative.

The canonical PDF and LaTeX source are generated from that exact source. The DOCX is an editable-prose publication copy generated after only the notation- and structure-preserving converter normalisations below. No theorem statement, equation content, proof text or mathematical ordering is changed.

Documented normalisations:

1. Paper V's `N_{\mathrm{sq}}`, `N_{\mathrm{ns}}` notation is retained throughout.
2. Cardinalities use `\operatorname{card}` rather than `\#` or `\lvert\cdot\rvert`; early office renders displayed those alternatives inconsistently.
3. The two cyclic groups are named in prose rather than distinguished by unsupported decorative glyphs.
4. One missing blank line between the final display in Theorem 9.3 and its `### Proof` heading is inserted in the temporary typesetting source. The reviewed words, equations and ordering are unchanged; this prevents Pandoc from printing the Markdown heading marker literally.
5. For DOCX only, every Pandoc math node is rendered from its exact TeX by a single deterministic LaTeX/preview batch and embedded as a transparent 300-dpi equation image. There are 394 equation occurrences (315 inline and 79 display) representing 272 unique TeX expressions. Each occurrence carries the exact TeX as alternative text. Prose, headings, citations and lists remain editable.
6. This all-equation image route supersedes the OMML route. Manual page QA showed that LibreOffice could silently omit valid inline OMML even when package-level and text-extraction checks passed. The image route renders every equation consistently in Word-compatible and LibreOffice-compatible output.
7. Every DOCX section is set to A4 portrait with 25 mm margins. The geometry utility modifies section properties only and must not reconstruct paragraph runs, because assigning to `paragraph.text` destroys embedded equation images.
8. The build verifies the exact equation counts, image/drawing counts, alternative text, A4 geometry, canonical PDF font embedding, independent LibreOffice rendering, page counts, absence of source-token leakage, checksums and page-level visual QA.
9. Artin--Schreier and Kummer dashes may be typographic in prose; algebraic minus signs remain inside exact TeX equation images.
10. Page breaks may differ between the canonical PDF and editable-prose DOCX, but theorem numbering, symbols and mathematical content must match the authoritative source.

A change to mathematical source text resets source-fidelity and exact-hash review gates. These normalisations are build-only and leave the reviewed Markdown hash unchanged.
