# Replacement Paper V typesetting normalisations

The reviewed Markdown source is authoritative.

The canonical PDF and LaTeX source are generated directly from that exact reviewed Markdown. The DOCX is an editable-prose publication copy generated from the same source after only the notation- and structure-preserving converter normalisations below. No theorem statement, equation content, proof text or mathematical ordering is changed.

Documented normalisations:

1. The cubic class counts use `N_{\mathrm{sq}}` and `N_{\mathrm{ns}}`, not unbraced `N_+` and `N_-`, because the latter produced ambiguous subscripts in early office renders.
2. Cardinalities use `\operatorname{card}` rather than `\#`; an early LibreOffice render displayed `#` as an invalid equation glyph.
3. Blank lines are inserted around display delimiters in a temporary converter source so Pandoc parses every display as a separate block. The reviewed Markdown file itself is unchanged.
4. For DOCX only, every Pandoc math node is rendered from its exact TeX by a single deterministic LaTeX/preview batch and embedded as a transparent 300-dpi equation image. There are 359 equation occurrences (277 inline and 82 display) representing 273 unique TeX expressions. Each occurrence carries the exact TeX as alternative text. Prose, headings, citations and lists remain editable.
5. This all-equation image route supersedes the mixed OMML route. Manual page QA showed that LibreOffice could silently omit valid inline OMML even when package-level and text-extraction checks passed. The image route renders every equation consistently in Word-compatible and LibreOffice-compatible output.
6. Every DOCX section is set to A4 portrait with 25 mm margins. The geometry utility modifies section properties only and must not reconstruct paragraph runs, because assigning to `paragraph.text` destroys embedded equation images.
7. The build verifies the exact equation counts, image/drawing counts, alternative text, A4 geometry, canonical PDF font embedding, independent LibreOffice rendering, page counts, absence of source-token leakage, checksums and page-level visual QA.
8. Straight ASCII hyphens in source titles may render typographically as en/em dashes; mathematical minus signs are inside the exact TeX equation images.
9. Line wrapping and page breaks may differ between the canonical PDF and editable-prose DOCX, but theorem numbering, symbols and mathematical content must match the authoritative source.

A change to mathematical source text resets source-fidelity and exact-hash review gates. These normalisations are build-only and leave the reviewed Markdown hash unchanged.
