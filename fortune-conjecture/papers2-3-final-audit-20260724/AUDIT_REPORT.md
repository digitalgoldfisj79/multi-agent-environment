# Adversarial audit — Papers II and III

## Current decision

**SOURCE-LEVEL PASS — COMPILED-ARTIFACT AND HUMAN-REVIEW GATES OPEN.**

The original structural drafts did not contain the complete load-bearing proof record. Paper II has been rebuilt from its four-part archived manuscript. Paper III retains its concise narrative and now includes publication-quality continuous proofs of the complete frozen kernel, singular-series and conditional-theorem sources.

## Exact reviewed objects

Publication commit: `4866d113898a48f23feb9752576c350af97c6985`.

### Paper II

- Path: `publications/fortune-papers-ii-vi-20260724/paper2_revised/manuscript.md`
- Git blob: `745d262aee6ffb41de580c866246c99a34144c13`
- SHA-256: `0b9d8c96b0185827085955084507f7c1099803a4a1de46c0db2e3b81f3cdbb7a`
- Size: 43,952 bytes

### Paper III

- Path: `publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md`
- Git blob: `06fe9116d42fd056bf9727dfbaa63ccb7398562d`
- SHA-256: `7275ba02e7ae7a60d4bd3e524a2f1fd4d9fed639589b7d1ab7f08dd80f5fe675`
- Size: 36,285 bytes

## Paper II result boundary

Paper II proves the structural integer-side results it labels proved: the Fortunate-number barrier, prime-power contamination bound, deterministic variance-to-detection criterion, exact reciprocal-frame identities, weighted harmonic reduction, fourth moment, cumulative Möbius truncation and Frobenius tail, semiprime resonance obstruction, character identities, density-one failure certificate, phase coherence, conductor migration, harmonic aggregation, Fourier conservation and divisor-pinning obstruction.

It does **not** prove the source-to-frame transference step, reciprocal sampling target, direct block-variance estimate or Fortune's conjecture. The displayed variance bound in Theorem 2.4 is a hypothesis of a proved implication, not a theorem asserted unconditionally.

The reconstruction repaired reciprocal-weight admissibility, zero-mass quotients, a missing diagonal estimate, an invalid fixed-`epsilon` level-set cutoff, an implicit singular-series lower bound, the moving-interval prime-power justification and one unsupported typesetting glyph.

## Paper III result boundary

Paper III proves unconditionally the rigidity lemma, exact `N`-or-`1` multiplicity dichotomy, two-scale energy decomposition, high-moment bounds, the stated uniform sub-Weibull tail, exact computer-assisted sixth and centred third moments, the exceptional-set failure certificate subject to its stated atom conditions, the finite singular-series local factors and divisor identity, and `|T_j(H)|<=2H log X`.

It proves conditionally that H1 and H2 imply the deterministic variance criterion and hence Fortune's conjecture for sufficiently large indices. H1, H2 and the reciprocal exceptional-set transference theorem remain open.

Appendix B was rewritten from the frozen machine proof into publication mathematics. An unused infinite-tail assertion and an unsupported sign inference were removed. The exact absolute estimate used by the conditional theorem was preserved and independently rechecked.

## Independent reconstruction

- From-scratch finite reconstruction job `6a6359807ef3c0846496771d` — all multiplicity, moment, Möbius and divisor panels passed.
- Extended final Appendix B panels job `6a6371fe7ef3c08464967840` — `APPENDIX_B_EXACT_PANELS_PASS`.
- Paper II shipped suite job `6a635a7bdb23d7a7ec1ca79c` — `ALL_CHECKS_PASS`.
- Paper III shipped addendum suite job `6a6359807ef3c0846496771d` — `ADDENDUM_CHECKS_PASS`.

## Fresh exact-hash hostile reviews

Both final source objects were reviewed by `Qwen/Qwen3-14B-AWQ`.

- Paper II job: `6a63765c7ef3c08464967898`; prompt SHA-256 `9e62bc7052f6bc04260d7c751771c01bf1f9bd34a2be42ab2a0220ecbba7fe77`.
- Paper III job: `6a63743ddb23d7a7ec1ca9cb`; prompt SHA-256 `7f0cf6a96f143c0ac223ffad55866f148a7b24f575bc5b318e1661cac93e1762`.

Paper III received a proved verdict with no fatal or major issue. Paper II's objections confuse the proved implication in Theorem 2.4 with proof of its open hypothesis and overlook explicit repairs already present in the exact text. `HOSTILE_REVIEW_DISPOSITION.md` resolves every objection. No fatal or major issue survives disposition.

## Gate ledger

1. Frozen-source fidelity — **passed**.
2. Independent finite reconstruction — **passed**.
3. Fresh exact-hash hostile review — **passed after disposition**.
4. Compiled PDF/DOCX/ZIP integrity and page-level QA — **open**.
5. External human specialist review — **open**.

This is an internal technical audit, not human peer review, publication acceptance or a proof of Fortune's conjecture.
