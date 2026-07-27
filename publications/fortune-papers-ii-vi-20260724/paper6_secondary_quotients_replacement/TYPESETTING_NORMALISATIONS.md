# Replacement Paper VI typesetting normalisations

The reviewed Markdown source is authoritative.

The PDF is generated directly with Pandoc, citeproc and XeLaTeX on A4 paper. The editable DOCX is generated from the same source. No mathematical rewriting is permitted.

Documented notation normalisations:

1. Paper V's `N_{\mathrm{sq}}`, `N_{\mathrm{ns}}` notation is retained throughout.
2. Cardinalities use `\operatorname{card}` rather than `\#` or `\lvert\cdot\rvert`; early DOCX renders displayed those alternatives as invalid equation glyphs in several contexts.
3. The two cyclic groups are named in prose rather than distinguished by unsupported decorative glyphs.
4. Artin--Schreier and Kummer dashes are typographic in prose; algebraic minus signs remain equation objects.
5. Display equations remain native OMML in DOCX and native TeX in PDF.
6. Page breaks may differ between formats; theorem numbering, symbols and mathematical content must not.

Any additional conversion must be documented and re-audited.
