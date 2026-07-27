# Replacement Paper V typesetting normalisations

The reviewed Markdown source is authoritative.

The PDF is generated directly with Pandoc, citeproc and XeLaTeX on A4 paper. The editable DOCX is generated from the same source. No mathematical rewriting is permitted in either branch.

Documented notation normalisations:

1. The cubic class counts use `N_{\mathrm{sq}}` and `N_{\mathrm{ns}}`, not unbraced `N_+` and `N_-`, because the latter produced ambiguous OMML subscripts in an early DOCX render.
2. Cardinalities use `\operatorname{card}` rather than `\#`; an early LibreOffice render displayed `#` as an invalid equation glyph.
3. Display equations remain native OMML in DOCX and native TeX in PDF.
4. Straight ASCII hyphens in source titles may render typographically as en/em dashes; mathematical minus signs remain equation objects.
5. Line wrapping and page breaks may differ between PDF and DOCX, but theorem numbering, symbols and mathematical content must match the authoritative source.

Any additional conversion must be added to this file and triggers the source/build QA reset if it changes mathematical text.
