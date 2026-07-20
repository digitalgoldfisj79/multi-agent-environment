# Relation to existing analytic methods

The remaining theorem is adjacent to several mature bodies of analytic number theory, but does not fit any of them directly.

The direct criterion in Theorem 2.4 resembles a Selberg-integral or Barban--Davenport--Halberstam statement. Classical BDH theory averages residue classes and moduli [@davenport-halberstam1966], while recent general-sequence versions require regularity or non-concentration hypotheses that are themselves unproved for the modulus-dependent primorial detector [@harper2025]. Pair-correlation methods relate continuous mean squares of primes in short intervals to zero statistics [@goldston-montgomery1987; @chan2003], but Theorems 8.2 and 8.3 show that the primorial centres neither provide a common critical-scale phase average nor a stable conductor ensemble.

Asymptotic-sieve methods can break parity when an additional bilinear axiom is available [@friedlander-iwaniec1998]. In the present problem, exact finite decompositions show strong cancellation between Type-I and Type-II pieces of the complete von Mangoldt detector. Bounding those pieces separately removes the stabilising covariance. Modern multiplicatively structured prime-detecting sieves reach short intervals of polynomial length in the ambient prime size, whereas the present interval has length only \((\log P_j)^2\) [@matomaki-merikoski-teravainen2024].

Sparse large-sieve inequalities, additive-energy refinements, and results for freely selected products of primes control substantially different sampling geometries [@chang-kerr-shparlinski2018; @baker-munsch-shparlinski2022; @matomaki-teravainen2024]. Their generic dependence on frequency diameter or conductor does not exploit the signed cumulative Möbius detector. Kloosterman-fraction and dispersion estimates likewise require explicit independent coefficient variables after a usable reciprocity transform [@bettin-chandee2018; @drappeau2017]. The exact ratio-collapse theorem shows that complete character separation of the present kernel does not create those variables.

Factorial exponential-sum methods are a natural neighbouring subject because factorials and primorial prefixes are both cumulative multiplicative walks. Their principal shift identity,

\[
\frac{(n+k)!}{n!}=\prod_{i=1}^k(n+i),
\]

creates a bounded-degree polynomial in the index and enables Weil-type arguments [@garaev-luca-shparlinski2004; @garaev-luca-shparlinski2005]. The corresponding quotient of primorial prefixes is a product of future primes and has no bounded-degree algebraic dependence on the index. Moreover, the classical individual factorial bounds are non-saving at the critical length \(N\asymp q^{1/2}/\log q\). This analogy therefore identifies the missing structure rather than supplying a theorem.

# Computational verification and reproducibility

All asymptotic statements in this paper are proved symbolically. Computation was used for independent validation of exact identities and for diagnostics that are explicitly excluded from the proofs.

The validation suite includes:

- exhaustive checks of the partial alternating-binomial identity for the Möbius detector;
- direct enumeration of the endpoint-multiset count in Theorem 4.2;
- random complex-vector checks of the one-sided residual identity;
- prime, semiprime, three-prime and four-prime checks of the CRT character diagonal;
- independent verification of the local character-ratio collapse;
- finite Fourier reconstruction tests for Proposition 9.1;
- numerical audits of the critical-scale coherence limit;
- weighted reciprocal-pair samples used only to illustrate the diffuse nature of accessible high values.

Selected checks are shown below.

| Identity or diagnostic | Validation result |
|---|---:|
| Theorem 4.2 at \(N=55\) | exact value \(13{,}562{,}560\) |
| CRT diagonal/full reconstruction | maximum residual below \(2\times10^{-12}\) |
| Character-ratio collapse | maximum residual below \(2.3\times10^{-14}\) |
| One-sided energy identity | maximum residual \(1.30\times10^{-9}\) |
| Fourier-scale reconstruction | maximum residual \(1.31\times10^{-13}\) |
| Coherence diagnostic at \(N=10{,}000\) | correlation \(0.99612\) with limiting sinc profile |

The supplementary archive contains the source manuscript, validators, phase reports, data summaries, a manifest, and checksums. The numerical panels are descriptive and are not used to establish any theorem.

# The remaining theorem boundary

The results above progressively remove non-load-bearing formulations.

- The direct problem does not require a prime offset; any shifted prime below the square threshold suffices.
- A natural block second moment already proves every centre, provided its loss is \(o(\log X)\).
- In the reciprocal frame, the lower side of the centred residual is automatic.
- A weighted aggregate over harmonics is sufficient; uniformity in every harmonic is stronger than necessary.
- The pair-sum kernel has exactly the expected Lebesgue \(L^2\)-mass.
- High Möbius degree is negligible.
- Positive density replacement is invalid because of resonant composites.
- The CRT character diagonal is not load-bearing, and the unequal-character sector reconstructs the original phase.
- Primorial-index averaging is coherent at the critical zero scale and unstable in conductor.
- Long harmonic averaging and finite divisor certificates do not survive exact Fourier accounting.

For the reciprocal architecture, the clean open target is the weighted one-sided estimate

\[
\boxed{
\sum_{a\ge1}\frac1{m_a}
\sum_{\substack{q,r\in\mathcal Q_X\\q\ne r}}
 p_{q,a}p_{r,a}
\left(
\left|H_2\!\left(a\left(\frac1q-\frac1r\right)\right)\right|^2-M
\right)
\ll MX^{o(1)}.
}
\tag{12.1}
\]

The prime support in (12.1) may be replaced by the growing-degree cumulative Möbius detector of Theorem 5.2, but the retained degrees must remain signed and coupled. The theorem is a deterministic transference statement: the reciprocal prime-pair sampling measure must not place excessive mass on the high-value sets of a lacunary pair-sum polynomial generated by one consecutive-prime prefix-product walk.

For the direct architecture, the open target is

\[
\boxed{
\sum_{j<N}
\left|
\sum_{2\le m\le\eta X^2}
(\Lambda(P_j+m)-1)
\right|^2
\ll NHX L(X),
\qquad L(X)=o(\log X).
}
\tag{12.2}
\]

A proof of (12.2) would establish Fortune's conjecture for all sufficiently large indices. A proof of (12.1) would close the reciprocal-frame route to the corresponding principal-cancelled Frobenius estimate. The exact equivalence of these two open targets is not asserted; they are complementary boundaries reached from the same primorial geometry.

# Conclusion

Consecutive-prime partial products carry enough exact structure to support a detailed analytic reduction, but not enough currently known cancellation to prove Fortune's conjecture. The present sequel supplies three kinds of result.

First, it gives positive reductions: a block second moment that forces every centre; an exact harmonic aggregate; an exact one-sided residual; an exact pair-sum fourth moment; and a growing-degree Möbius truncation.

Second, it gives exact obstruction theorems: semiprime resonance defeats positive density replacement; the unequal-character CRT sector reconstructs the additive kernel; the primorial-index average is coherent at critical zero spacing and migrates in conductor; Fourier-scale conservation defeats an artificial long harmonic average; and power-scale large values do not imply divisor-level phase precision.

Third, it identifies the remaining mathematics. The obstacle is not a missing algebraic reformulation. It is a signed arithmetic transference theorem for the consecutive-prime prefix-product walk, or a direct sparse-centre Selberg-integral theorem at interval length \((\log P)^2\). Neither is supplied by current generic sieve, large-sieve, Kloosterman, factorial-sum, or pair-correlation machinery.

No implication beyond the stated conditional criteria is claimed. The value of the analysis is the exact boundary: future progress must create genuinely new cancellation rather than another equivalent decomposition of the same reciprocal kernel.

# References

::: {#refs}
:::
