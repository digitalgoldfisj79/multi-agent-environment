# Disposition of final hostile reviews — Papers II and III

## Exact review objects

- Model: `Qwen/Qwen3-14B-AWQ`
- Publication commit: `4866d113898a48f23feb9752576c350af97c6985`
- Paper II SHA-256: `0b9d8c96b0185827085955084507f7c1099803a4a1de46c0db2e3b81f3cdbb7a`
- Paper III SHA-256: `7275ba02e7ae7a60d4bd3e524a2f1fd4d9fed639589b7d1ab7f08dd80f5fe675`
- Paper II review job: `6a63765c7ef3c08464967898`
- Paper III review job: `6a63743ddb23d7a7ec1ca9cb`

Model review is evidence rather than authority. Every objection was checked against the exact manuscripts and frozen proof basis.

# Paper II

## II.1 Theorem 2.4 is a proved implication, not a proved variance estimate

**Review objection.** The review treats Theorem 2.4 as if it claimed the displayed direct variance bound unconditionally.

**Disposition: rejected.** Theorem 2.4 has the logical form:

> If the displayed block variance estimate holds with `L(X)=o(log X)`, then every centre in the block contains a prime in the target interval.

The proof derives the conclusion from that hypothesis. It does not derive or claim the hypothesis. Calling the implication a proved criterion is standard and logically distinct from claiming the open variance estimate. Section 12 again lists the direct variance estimate as an open target.

## II.2 Imported source-to-frame transference

**Review objection.** The imported bridge is not reproved.

**Disposition: not a defect in a claimed theorem.** Immediately after (3.6), the manuscript states that it does not reprove the source-to-frame transference step and does not assert equivalence with Theorem 2.4. The structural reciprocal-frame results that follow are exact internal identities and obstructions. The bridge remains an explicit programme dependency, not a hidden premise presented as proved.

## II.3 Semiprime singular-series lower bound

**Review objection.** The lower bound is not explicitly justified.

**Disposition: already repaired in the reviewed source.** The proof displays

\[
\mathfrak S(d)=2C_2\prod_{\substack{p\mid d\\p>2}}\frac{p-1}{p-2}
\]

for even `d`, and hence `\mathfrak S(d)>=2C_2`. The resonant semiprimes divide every centre because `P_j=A_XQ_j` and both prime factors are below `X`.

## II.4 Composite-modulus Gauss factorisation

**Review objection.** The squarefree composite-modulus case is allegedly not addressed.

**Disposition: rejected.** Section 7 defines `m` as squarefree, expands characters modulo `m`, and obtains the kernel as the product of its prime-modulus factors by CRT. The simplified collision-free formula is explicitly conditional; the general kernel formula remains exact without it.

## II.5 Moving-interval proper prime powers

**Review objection.** Uniformity in the moving interval is allegedly missing.

**Disposition: already repaired in the reviewed source.** Theorem 8.1 explains that for each exponent `k>=2`, consecutive `k`-th powers near `P_n` are separated by more than the interval length, so at most one occurs; summing their von Mangoldt weights gives `O(log P_n log log P_n)=o(h_n)` uniformly in the integration variable.

## II.6 Final notation change

The replacement of `a in Z setminus {0}` by `a in Z` with `a!=0` defines the identical harmonic index set. It changes no hypothesis or inference.

## Paper II conclusion

No fatal or major objection survives. Paper II proves the implications, identities and obstructions that it labels proved. The source-to-frame bridge, direct variance estimate, reciprocal sampling theorem and Fortune's conjecture remain open exactly as stated.

# Paper III

The final exact-hash review gives the unconditional theory and conditional implication a **proved** verdict and reports no fatal or major defect.

## III.1 Atom-size condition

**Review note.** Corollary 8.1 uses the stated atom-count and maximum-atom-mass condition.

**Disposition: accepted as a stated hypothesis, not an omitted proof.** The corollary is a failure certificate conditional on those measure properties. It does not claim to derive the reciprocal-prime-pair measure construction. This is part of the explicitly identified arithmetic transference boundary.

## III.2 Appendix B

The final review checked the local factors, finite Euler expansion, exact divisor identity, `W_H` formula, cancellation, tail, error and beta estimates. It accepted the inference

\[
|T_j(H)|\le2H\log X
\]

and confirmed that no sign assertion remains. The Dickman--de Bruijn refinement is explicitly non-load-bearing.

## Paper III conclusion

No repair is required. The rigidity, multiplicity, energy, moment, tail and finite singular-series results are proved. The Hardy--Littlewood implication is proved under H1 and H2. H1, H2 and the exceptional-set transference theorem remain open.

# Overall gate

The fresh exact-hash hostile-review gate is **passed after disposition** for both papers. This is not human peer review and does not promote any open or conditional statement to an unconditional theorem.
