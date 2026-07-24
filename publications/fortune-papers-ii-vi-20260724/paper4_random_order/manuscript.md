---
title: |
  Prime Detection Along Random Primorial-Product Paths
subtitle: |
  An unconditional reciprocal-frame theorem in the random-order model
author:
  - "Edward Stewart Anthony Bozzard"
date: "24 July 2026"
lang: en-GB
abstract: |
  We replace the increasing order of the primes in a dyadic block by a uniformly
  random ordering and study the resulting nested product path. For the
  reciprocal-frame energy introduced in the preceding papers, we prove an
  unconditional expectation bound of order \(M(\log X)^9\), uniformly in every
  harmonic in the natural range. The same estimate holds for the weighted
  aggregate and the associated Frobenius energy.

  The proof does not use GRH or pointwise cancellation in prime character sums.
  Conditioning on the rank positions of the endpoints turns the random path
  into an exact ordered set-partition problem. Cauchy-contour estimates create
  decay in ratio characters, while a sixth-moment orthogonality count bounds the
  number of characters with large block-prime bias. A complete configuration
  ledger closes the estimate. The theorem is a model result: random-order
  centres are not primorials. Its significance is to show that the analytic
  target is generically true at critical length and that the Fortune-relevant
  wall is derandomisation to the unique increasing order.
keywords: ["random permutations", "primorial products", "reciprocal frames", "character sums", "order entropy", "derandomisation"]
---

# 1. Random product paths

Let \(\mathcal L=\{\ell_1,\ldots,\ell_K\}\) be the primes in \([X,2X)\) and let \(\sigma\) be uniform on the symmetric group \(S_K\). Put
\[
Q_0^\sigma=1,\qquad
Q_j^\sigma=\prod_{i\le j}\ell_{\sigma(i)},\qquad
P_j^\sigma=A_XQ_j^\sigma.
\]
Let \(N=K+1\), \(M=N(N+1)/2\), and define the pair sums
\[
S_{\{j,k\}}^\sigma=P_j^\sigma+P_k^\sigma.
\]
The reciprocal-frame quantities \(\Psi_a\), \(\mathcal E_a^\sigma\), \(\mathcal R_a^\sigma\), and \(\mathfrak F_X^\sigma\) are exactly those of Paper II, evaluated along the \(\sigma\)-path.

# 2. Main theorem

## Theorem 2.1 (random-order model)

Assume the frame is nondegenerate and \(\rho\) is an admissible nonnegative even Schwartz function. For all sufficiently large \(X\),
\[
\mathbb E_\sigma[\mathcal E_a^\sigma]
\le C(\eta,\rho)M(\log X)^9
\]
uniformly for every \(1\le |a|<H\). Moreover
\[
\mathbb E_\sigma\left[\sum_{a\ge1}
\frac{\mathcal R_a^\sigma}{m_a}\right]
\le C M(\log X)^9
\]
and
\[
\mathbb E_\sigma[\mathfrak F_X^\sigma]
\le C M(\log X)^9.
\]

By Markov, all but an \(\omega^{-1}\) fraction of the \(K!\) orderings satisfy the aggregate reciprocal-frame target with loss \((\log X)^9\omega(X)\).

# 3. Exact conditioning by rank cells

Fix an ordered pair \(u\ne v\) of pair indices. The difference has the form
\[
D_{u,v}^\sigma=\sum_sc_sP_{t_s}^\sigma,
\]
where \(2\le m\le4\), \(t_1<\cdots<t_m\), \(c_s\in\{-2,-1,1,2\}\), and \(\sum_sc_s=0\).

The rank gaps split the block primes into ordered cells
\[
W_0,W_1,\ldots,W_m.
\]
Conditioned on the cell sizes, the cell contents are an exactly uniform ordered set partition of \(\mathcal L\). Hence expectations of products of characters over the cells are coefficient extractions from
\[
\prod_{\ell\in\mathcal L}
\left(\sum_sx_s\psi_s(\ell)\right).
\]
No Poissonisation or approximate jump-time model is used.

# 4. Complete coefficient-pattern classification

The possible nonzero coefficient vectors are exactly:

- \(m=2\): \((1,-1)\), \((-1,1)\), \((2,-2)\), \((-2,2)\);
- \(m=3\): the six signed permutations of \((1,1,-2)\);
- \(m=4\): the six vectors with two \(+1\)'s and two \(-1\)'s.

The \(m=2\), coefficient-\((1,-1)\) class has multiplicity \(N\), the sliding family. Every other configuration has multiplicity one. The exact count is
\[
M(M-1)=N^2(N-1)+N(N-1)+6\binom N3+6\binom N4.
\]

# 5. Ratio-character decay

For distinct reciprocal moduli \(q,r\), CRT and Gauss inversion reduce the phase to character slots on the cells. The common character direction is irrelevant; decay depends on ratio characters.

Let
\[
t_\chi=\frac1K\left|\sum_{\ell\in\mathcal L}\chi(\ell)\right|.
\]
A multivariate Cauchy-contour estimate gives
\[
|\mathbb E_\sigma \prod_s\psi_s(W_s)|
\le CK^2
\exp\!\left(
-\sum_{s<s'}\frac{n_sn_{s'}}K
(1-t_{\psi_s\bar\psi_{s'}})
\right).
\]
Large cells therefore manufacture exponential decay unless a ratio character has unusually large block-prime bias.

# 6. Counting exceptional characters

The proof needs only a count of characters with \(t_\chi\ge3/4\). Sixth-moment orthogonality gives
\[
\sum_{\chi\bmod qr}
\left|\sum_{\ell\in\mathcal L}\chi(\ell)\right|^6
=
\varphi(qr)\,
\#\{\ell_1\ell_2\ell_3=\ell_4\ell_5\ell_6\bmod qr\}.
\]
Because products of three block primes are smaller than \(qr\), congruence is equality and unique factorisation controls the collision count. Chebyshev then yields
\[
\#\{\chi:t_\chi\ge3/4\}\ll X(\log X)^3.
\]
This is the only arithmetic input controlling bad characters. No zero-density theorem or GRH is required.

# 7. The configuration ledger

Choose a micro-cell threshold \(w_0=600\log X\). Configurations with at least two micro cells are counted trivially. The remaining configurations are handled by ratio-character decay.

The binding class has four endpoint ranks and one interior micro cell. It contains \(O(N^3w_0)\) configurations. Three exceptional-character slots produce a factor
\[
\beta^3,\qquad \beta\ll X(\log X)^3,
\]
while two free ratio coordinates contribute \(X^{-4}\). The net contribution is
\[
O\!\left(M(\log X)^9\right).
\]
All other classes have more decay or fewer configurations. Summing the complete ledger proves the per-modulus-pair estimate
\[
\sum_{u\ne v}
\left|\mathbb E_\sigma e_{qr}(bD_{u,v}^\sigma)\right|
\ll M(\log X)^9.
\]

# 8. Assembly of the theorem

Insert the last bound into the exact dual-row decomposition:
\[
\mathbb E_\sigma[\mathcal E_a^\sigma]
=
M(M-1)\kappa_{2,a}
+
\sum_{q\ne r}p_{q,a}p_{r,a}
\mathbb E_\sigma\sum_{u\ne v}e_{qr}(bD_{u,v}^\sigma).
\]
Frame nondegeneracy gives
\[
M(M-1)\kappa_{2,a}\ll M/\log X.
\]
The distinct-modulus part is \(O(M(\log X)^9)\). Summing over \(a\) with weights \(1/m_a\) uses \(\sum_am_a=1/2\) and Schwartz decay outside \(|a|<H\). The Frobenius estimate follows from the Paper II comparison.

# 9. Verification

The supporting package records the following exact checks:

1. the ordered-partition identity against all \(7!\) orderings of a seven-prime block;
2. the complete coefficient-pattern count;
3. the contour bound and Gauss/CRT normalisations;
4. symbolic exponent arithmetic in every ledger class;
5. sixth-moment orthogonality;
6. an end-to-end comparison of the direct permutation average with the full character expansion.

These checks validate the assembly but are not substitutes for its proof.

# 10. Scope and derandomisation

The identity ordering is the true increasing primorial order, but averaging over \(S_K\) creates the entropy used at every decisive step. The theorem does not imply Fortune's conjecture or the reciprocal-frame target for the identity ordering.

It does establish three points.

1. The reciprocal-frame target is correctly scaled: it holds generically at critical length without GRH.
2. The obstruction is not the pair-sum architecture itself.
3. The next problem is derandomisation, plausibly through a variance or concentration theorem over orderings followed by a mechanism identifying the increasing order as nonexceptional.

## AI-assistance disclosure

The research programme used large language models for structured literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. Every mathematical claim included as a theorem was checked against an explicit proof or an independently reproducible exact computation. Conjectural, conditional, computational, and negative results are labelled separately. The named author takes responsibility for the content, citations, code, and final presentation.

## Data, code, and reproducibility

The source record for this draft is the public repository `https://github.com/digitalgoldfisj79/multi-agent-environment` on branch `gpt56/d1-gate-bridge-terminal-20260724`. The Zenodo package accompanying this manuscript contains the manuscript source, compiled PDF, a claim-status ledger, a source-file manifest, machine-readable metadata, and checksums.

# References

1. E. S. A. Bozzard, *Prime Detection at Primorial Centres*.
2. E. S. A. Bozzard, *Pair-Sum Rigidity, Exceptional Sets, and Conditional Prime Detection at Primorial Centres*.
3. Standard references on character orthogonality, Gauss sums, and random permutations.
