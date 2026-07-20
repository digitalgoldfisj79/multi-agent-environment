# Manuscript summary

## Abstract

Let \(P_n=\prod_{p\le p_n}p\) and let \(F_n\) be the least integer \(m>1\) for which \(P_n+m\) is prime. Since every prime factor of \(F_n\) exceeds \(p_n\), a composite \(F_n\) is at least \(p_{n+1}^2\). This sequel studies the analytic interface between consecutive-prime partial products and prime detection at primorial centres. It proves a direct block-variance criterion, an exact one-sided reciprocal-frame decomposition, an exact pair-sum fourth moment, a growing-degree Möbius truncation, and several exact obstruction theorems. No proof of Fortune's conjecture is claimed.

## Positive results

1. **Direct block-variance criterion.** A bound
   \[
   \sum_{j<N}\left|\sum_{2\le m\le H}(\Lambda(P_j+m)-1)\right|^2
   \ll NHX L(X),\qquad L(X)=o(\log X),\quad H\asymp X^2,
   \]
   forces every centre in the dyadic block to contain a prime below the square threshold.

2. **Exact weighted harmonic aggregation.** The principal-cancelled Frobenius energy is bounded by a positive weighted sum of one-harmonic energies, without an artificial truncation parameter.

3. **One-sided PGD2 correction.** For each harmonic,
   \[
   \mathcal E_a=M(M-1)\kappa_{2,a}+\mathcal R_a.
   \]
   Only an upper bound for \(\mathcal R_a\) is load-bearing; the lower side is automatic.

4. **Exact pair-sum moment.** For the pair-sum polynomial \(H_2\),
   \[
   \int_0^1|H_2(\theta)|^4\,d\theta
   =\frac{N(3N^3-2N^2+2N-1)}2,
   \]
   and the centred \(L^2\)-mass is \(5M^2(1+O(N^{-1}))\).

5. **Growing-degree Möbius truncation.** Degrees above
   \[
   k\sim(1+\eta)\frac{\log X}{\log\log X}
   \]
   have negligible Frobenius contribution, although the retained degrees must remain signed and globally coupled.

6. **Density-one failure certificate.** Fortune failure forces a cubic local Selberg-energy contribution.

## Exact obstruction results

- Resonant semiprimes make a positive Hardy--Littlewood density surrogate polynomially too large.
- The equal-character CRT diagonal is explicit, but the unequal-character ratio sector reconstructs the original additive reciprocal kernel.
- Primorial-index phases are macroscopically coherent at the natural zero-pair scale.
- The effective explicit-formula conductor migrates by a factor asymptotic to \(p_{n+1}\) between successive centres.
- Narrowing the physical interval and summing translates reconstructs the original Fourier transform exactly; it does not create a growing independent harmonic average.
- Power-scale large values allow diffuse phase bias and do not provide the exponentially precise alignment required for determinant or divisor pinning.

## Open theorem boundaries

The paper ends with two complementary open targets:

1. the direct complete shifted-prime block variance above;
2. a weighted one-sided reciprocal sampling theorem for the consecutive-prime prefix-product walk.

The exact equivalence of these targets is not asserted.
