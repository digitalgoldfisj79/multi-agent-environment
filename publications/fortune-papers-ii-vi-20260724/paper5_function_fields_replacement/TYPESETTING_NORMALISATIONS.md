# Replacement Paper V typesetting normalisations

The reviewed Markdown source is authoritative.

The canonical PDF and LaTeX source are generated directly from that exact reviewed Markdown. The editable DOCX is generated from the same source after only the notation- and structure-preserving converter normalisations listed below. No theorem statement, equation content, proof text or mathematical ordering is changed.

Documented notation normalisations:

1. The cubic class counts use `N_{\mathrm{sq}}` and `N_{\mathrm{ns}}`, not unbraced `N_+` and `N_-`, because the latter produced ambiguous OMML subscripts in an early DOCX render.
2. Cardinalities use `\operatorname{card}` rather than `\#`; an early LibreOffice render displayed `#` as an invalid equation glyph.
3. For the DOCX branch only, the inline domain condition `q\in\mathbf F_p^*\setminus\{2\}` is written equivalently as `q\in\mathbf F_p^\times,\ q\ne2`. The set and its mathematical meaning are unchanged.
4. Ordinary inline and display mathematics remain native editable OMML. Four q-line displays that LibreOffice Math mistranslates are converted from their exact TeX expressions to centred transparent 300-dpi PNG equation images. Each image carries the exact TeX expression as alternative text; the authoritative Markdown and generated LaTeX remain in the release package.
5. Blank lines are inserted around display delimiters in the temporary DOCX source so each targeted equation image occupies a separate centred paragraph. This changes only Markdown block parsing, not mathematical content.
6. The conversion is deterministic and guarded: exactly four displays must be converted; the build fails on any Pandoc `Could not convert TeX math` warning, insufficient OMML objects, insufficient equation images, literal TeX leakage, literal Markdown headings, or an abnormally short LibreOffice render extraction.
7. Straight ASCII hyphens in source titles may render typographically as en/em dashes; mathematical minus signs remain equation objects.
8. Line wrapping and page breaks may differ between PDF and DOCX, but theorem numbering, symbols and mathematical content must match the authoritative source.

Any additional conversion must be added to this file. A change to mathematical source text would reset source-fidelity and exact-hash review gates; the normalisations above are build-only and leave the reviewed Markdown hash unchanged.