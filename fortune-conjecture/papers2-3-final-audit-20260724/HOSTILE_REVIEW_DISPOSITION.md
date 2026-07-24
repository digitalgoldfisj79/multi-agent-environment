# Disposition of the final hostile reviews — Papers II and III

## Review objects

- Model: `Qwen/Qwen3-14B-AWQ`
- Hugging Face job: `6a6365fedb23d7a7ec1ca8a6`
- Publication commit: `00d2a67d9963848e35596ea153917e73c2dfeb17`
- Paper II SHA-256: `632bb8f4fd89a51020069327a11fe57f8ae882e57bd4ae1a9ed0829030c32ce1`
- Paper III SHA-256: `1753e5991ccab15142d9bd076554c283a69bfa3bd8aa9448b2edf62f50c4c7cb`

The reviews are evidence, not authority. Each objection is checked against the exact reviewed text and the frozen proof basis.

# Paper II

The review's opening verdict is that the manuscript's actually claimed theorems are proved. Its later classification of the imported transference step as a fatal or major defect conflicts with both the review prompt and the manuscript's explicit boundary.

## II.1 Imported source-to-frame transference

**Review objection.** The manuscript allegedly assumes that (3.6) is equivalent to the direct variance theorem and invalidly treats the source-to-frame bridge as proved.

**Disposition: rejected.** Immediately after (3.6), the manuscript says:

> “This manuscript does not reprove the source-to-frame transference step and does not assert that (3.6) is equivalent to Theorem 2.4.”

It then distinguishes the unconditional direct von Mangoldt variance implication from the separate harmonic target. Section 12 repeats that the exact equivalence of the two open targets is not asserted. No inference in the manuscript uses the imported bridge as a theorem proved in Paper II.

The bridge is a declared external dependency of the reciprocal architecture, not a hidden premise of the proved structural results. Requiring Paper II to prove an explicitly excluded open dependency would change the paper's stated scope rather than repair an invalid inference.

## II.2 Semiprime resonance and block alignment

**Review objection.** A semiprime `pr` in the resonant family might fail to divide every centre unless the dyadic parameter is aligned with a primorial index.

**Disposition: algebraically false.** Equation (2.1) defines

`A_X = product_{p<X} p` and `P_j = A_X Q_j`.

The resonant family in (6.3) has `p,r<X`. Hence `pr | A_X | P_j` for every block centre by definition. No additional relation between `X` and a separately named `p_n` is needed.

## II.3 Character-diagonal collision hypothesis

**Review objection.** The no-collision condition in Theorem 7.1 is not universally true.

**Disposition: not a defect.** The theorem states the condition as a hypothesis and gives both the general exact kernel formula (7.4) and its simplified value (7.5) under that hypothesis. It does not assert universal no-collision.

## II.4 Fourier-scale conservation is tautological

**Review objection.** Proposition 9.1 is an identity and therefore allegedly provides no new insight.

**Disposition: irrelevant to correctness.** The proposition is deliberately an exact conservation identity. Its purpose is to rule out a proposed proof strategy by showing that subdivision creates no new cancellation. Being elementary or tautological is not a mathematical defect.

## Paper II conclusion

No fatal or major issue survives disposition. The exact manuscript proves the structural theorems it labels proved, clearly identifies its imported dependency and leaves both the reciprocal transference target and Fortune's conjecture open.

# Paper III

The review labels the manuscript “not proved” because it counts the explicitly open exceptional-set theorem and the explicitly assumed Hardy--Littlewood hypotheses as missing proofs. That applies the wrong claim boundary. The manuscript claims an unconditional kernel theory and a conditional implication, not an unconditional proof of Fortune's conjecture.

## III.1 Exceptional-set transfer gap

**Review objection.** Corollary 8.1 allegedly assumes a missing sparse exceptional-set theorem.

**Disposition: rejected.** Corollary 8.1 is a proved failure certificate:

- assume the desired reciprocal sampling estimate fails at level `lambda=tM`;
- use the atom-mass upper bound to infer that at least `X^{4+o(1)}t^{-1}` atoms occur there;
- use the already proved Lebesgue tail to place those atoms in a set of measure at most `e^{-sqrt(t)}`.

The manuscript then identifies the theorem that would forbid this concentration as the remaining open research problem. The open theorem is the conclusion sought after the corollary, not a premise used to prove it.

## III.2 Hardy--Littlewood hypotheses H1 and H2

**Review objection.** H1 and H2 are not proved.

**Disposition: claim-status error.** The title, abstract, Section 10, Appendix C and final boundary all identify Theorem 10.1 as conditional. H1 and H2 are introduced with “Assume”; the manuscript explicitly says current technology supplies neither at the required strength and makes no unconditional prime-detection claim.

A conditional theorem is proved when its conclusion follows from its stated hypotheses. Appendix C provides that variance expansion and tracks the diagonal, off-diagonal, singular-series and error terms through the required threshold `epsilon=o(log X/X)`.

## III.3 Uniform sub-Weibull bound versus sharpness

**Review objection.** Fixed-level sharpness is not extended uniformly to `lambda<=M^2`, allegedly undermining the tail theorem.

**Disposition: conflation of two different statements.** Theorem 6.1 and Appendix A.4 prove the upper bound uniformly for the stated range `121M <= lambda <= M^2`. The manuscript separately remarks that the exponent constant `sqrt(2)` is sharp in the fixed-level limiting law. Uniform sharpness is not claimed and is not needed for the conditional theorem, which uses the proved upper bound.

## III.4 Dickman--de Bruijn constant

**Review objection.** The non-load-bearing Dickman sketch is allegedly used by the theorem.

**Disposition: rejected.** Appendix B explicitly separates:

- the exact divisor identity;
- the proved bound `|T_j(H)| <= 2H log X`; and
- a sharper constant described as a non-load-bearing sketch.

The conditional variance proof uses only the proved `O(H log X)` bound. No theorem depends on the sketched constant.

## III.5 Computational validation

**Review objection.** The exact moment checks are insufficiently detailed.

**Disposition: package-level request, not an invalid inference.** Appendix A states the interpolation degree, finite validation range and validator. The audit package additionally records a from-scratch reconstruction and the complete shipped-validator panels. The exact moment formulas were checked independently for `N=2,...,8`, and the shipped validator checks the sixth moment through `N=11` together with the centred third moment and tail range.

## III.6 Lack of effective constants

**Review objection.** The conditional theorem contains `o(1)` terms rather than explicit constants.

**Disposition: not a correctness defect.** The result is an asymptotic conditional theorem and does not claim effectivity. The scale and required relative error are explicit. An effective version could be a later refinement but is not needed for the claimed implication.

## Paper III conclusion

No fatal or major issue survives disposition. The unconditional rigidity, multiplicity, energy, moment, tail and truncated-singular-series results are proved. The Hardy--Littlewood implication is proved conditionally on H1 and H2. The exceptional-set transference theorem and the hypotheses H1--H2 remain open exactly as stated.

# Overall gate

The fresh manuscript-only hostile-review gate is **passed after disposition** for both papers. This is not human peer review and does not promote any open or conditional statement to an unconditional theorem.
