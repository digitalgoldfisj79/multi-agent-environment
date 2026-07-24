# Fidelity and external-review gates — Papers II and III

## Exact objects

- Publication commit: `4866d113898a48f23feb9752576c350af97c6985`
- Paper II SHA-256: `0b9d8c96b0185827085955084507f7c1099803a4a1de46c0db2e3b81f3cdbb7a`
- Paper III SHA-256: `7275ba02e7ae7a60d4bd3e524a2f1fd4d9fed639589b7d1ab7f08dd80f5fe675`

## F1 — frozen-source fidelity: passed

Paper II was reconstructed from its four archived manuscript parts. Paper III combines its concise narrative with the complete frozen kernel, singular-series and conditional-theorem proofs, with Appendix B rewritten into publication mathematics. The detailed maps are recorded in the two fidelity matrices.

## F2 — independent finite reconstruction: passed

The independent implementation, extended final Appendix B panels and shipped validators reproduce the declared finite multiplicity, moment, Möbius and singular-series identities. `INDEPENDENT_CHECKS.md` records the exact panels and limits.

## F3 — fresh exact-hash hostile review: passed after disposition

- Paper II: Qwen3-14B-AWQ job `6a63765c7ef3c08464967898`.
- Paper III: Qwen3-14B-AWQ job `6a63743ddb23d7a7ec1ca9cb`.

Paper III received a proved verdict with no fatal or major defect. Paper II's listed objections confuse the proof of a criterion with proof of its displayed hypothesis or overlook explicit text already present. All objections are resolved in `HOSTILE_REVIEW_DISPOSITION.md`.

## F4 — compiled package integrity: open

Required before circulation:

1. build PDFs directly from the exact Markdown sources with XeLaTeX;
2. generate editable DOCX files with documented notation-only conversions;
3. verify extracted mathematical text and claim boundaries;
4. run PDF page-size, font and missing-glyph preflight checks;
5. run DOCX heading and structural checks;
6. inspect every rendered PDF and DOCX page;
7. verify every packaged SHA-256 checksum; and
8. create separate Paper II, Paper III and combined release archives.

Any source edit changes the hash and reopens F1 through F4.

## F5 — external human review: open

After F4 closes, Paper II should be read by an analytic-number-theory specialist familiar with prime-detection variance reductions and character sums. Paper III should be read by an analytic or probabilistic number theorist familiar with additive energy, singular series and conditional Hardy--Littlewood arguments.

## Claim boundary

- Paper II leaves the source-to-frame bridge, reciprocal sampling target, direct variance estimate and Fortune's conjecture open.
- Paper III leaves its block-averaged Hardy--Littlewood hypotheses and exceptional-set transference theorem open.
- Internal audit and model review are not peer review.
