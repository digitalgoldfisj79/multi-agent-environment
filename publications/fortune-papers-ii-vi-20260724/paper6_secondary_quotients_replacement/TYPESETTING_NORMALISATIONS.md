# Replacement Paper VI typesetting normalisations

The reviewed Markdown source is authoritative.

The publication artefacts are generated from that exact source after only the notation- and structure-preserving converter normalisations listed below. No mathematical rewriting is permitted.

Documented notation normalisations:

1. Paper V's `N_{\mathrm{sq}}`, `N_{\mathrm{ns}}` notation is retained throughout.
2. Cardinalities use `\operatorname{card}` rather than `\#` or `\lvert\cdot\rvert`; early DOCX renders displayed those alternatives as invalid equation glyphs in several contexts.
3. The two cyclic groups are named in prose rather than distinguished by unsupported decorative glyphs.
4. Artin--Schreier and Kummer dashes are typographic in prose; algebraic minus signs remain equation objects.
5. One missing blank line between the final display in Theorem 9.3 and its `### Proof` heading is inserted in the temporary typesetting source. The reviewed words, equations and ordering are unchanged; the insertion prevents Pandoc from printing the Markdown heading marker literally in PDF and DOCX.
6. Display equations remain native OMML in DOCX and native TeX in PDF. The runner installs LibreOffice Math before rendering the DOCX, and the build rejects both literal TeX leakage and an abnormally short rendered-text extraction.
7. Page breaks may differ between formats; theorem numbering, symbols and mathematical content must not.

Any additional conversion must be documented and re-audited.