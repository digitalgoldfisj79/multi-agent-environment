---
title: "Collision Geometry and Spectral Laws for Consecutive-Prime Partial Products"
subtitle: "Low transport, integral rank, and the centered two-run energy problem"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "24 July 2026 - Original reproducibility archive DOI 10.5281/zenodo.21426465"
abstract: |
  Let \(q_1<\cdots<q_N\) be the primes in a dyadic interval \([X,2X]\), let \(Q_0=1\), and let \(Q_j=\prod_{u=1}^j q_u\). We study multiplicative collisions among the deterministic path \((Q_j)_{0\le j\le N}\) modulo primes \(r\asymp X^2\). We prove an exact fourth-moment identity; an averaged low-transport collision bound; a weighted offset-slice large-divisor incidence estimate; average almost-injectivity and local second-factorial collision bounds; and an interval endpoint-graph classification of affine rank and Smith invariants. For the two-run kernel we give an exact pair-overlap decomposition, prove that the three-shared-endpoint sector is negligible at the target scale, reduce the disjoint sector to four centered median channels, and derive an exact independent-prefix mean, variance, and cross-median covariance law. We also determine the non-Gaussian fourth-moment law of the two-run spectrum. Further sections close sparse block-composition families, give a conditional edge reduction, and identify rank and zero-frequency losses in common-translation differencing. The unconditional estimates use character orthogonality, integral linear algebra, unique factorisation, and large-divisor counting. The centered rank-two estimate required for the remaining disjoint and low-overlap sectors is open; no prime-offset theorem is claimed.
---

# 1. Scope and motivation

Let

\[
X\le q_1<q_2<\cdots<q_N\le 2X
\]

be all primes in a dyadic block, and define

\[
Q_0=1,
\qquad
Q_j=\prod_{u=1}^{j}q_u
\quad(1\le j\le N).
\]

Write

\[
V=N+1.
\]

Thus \(Q_0,\ldots,Q_N\) are the vertices of a deterministic cumulative-product path. For every prime modulus \(r>2X\), all vertices are units modulo \(r\). The central questions are how often interval products collide modulo such \(r\), what integral rank is carried by families of interval equations, and whether the fourth-order two-run kernel has random-scale centered energy when averaged over \(r\asymp X^2\).

The established results are structural. They prove exact identities, remove low-transport and sparse-support collision geometries, give diagonal-dominant large-divisor incidence estimates, show average almost-injectivity of the cumulative path, classify the Smith form of arbitrary interval families, and isolate the remaining centered rank-two obstruction in the two-run problem. The paper also derives exact independent-prefix null laws against which the deterministic path can be compared. No long-range character-sum cancellation is assumed or claimed.

One motivation comes from Fortunate numbers. If \(P_n=\prod_{p\le p_n}p\) and \(F_n\) is the least \(m>1\) for which \(P_n+m\) is prime, then every prime factor of \(F_n\) exceeds \(p_n\); consequently, \(F_n<p_{n+1}^2\) is a sufficient condition for \(F_n\) to be prime. The present paper does not reduce this prime-offset problem to the energy estimates studied here. The motivation is therefore contextual only.

## 1.1. Relation to existing work

The endpoint-graph formulation is a specialization of additive gain graphs and lifted-graphic matroids [2,3]. Assigning gain \(1\) to each oriented interval edge gives the field-level rank criterion in terms of balanced cycles. The additional result used here is integral: for the affine-difference matrix of interval exponent vectors, the complete Smith form has at most one nonunit invariant, equal to the gcd of signed cycle imbalances and bounded by the number of intervals. We have not located this exact interval-specific Smith-form refinement in [2,3].

Known large-sieve and dispersion frameworks address different coefficient structures. Sparse-sequence large sieves [4,5], general Barban--Davenport--Halberstam estimates [7], and spectral exceptional-form large sieves [8] require hypotheses not presently verified for the exponentially large nested products \(Q_j\). Results for freely selected products of primes [6] do not preserve the deterministic prefix ordering. Kloosterman-fraction estimates [9,10] require an explicit reciprocal phase and independent coefficient variables; complete CRT orthogonality for the present two-run kernel does not produce such a phase.

# 2. Exact fourth-moment identity

For a multiplicative character \(\chi\bmod r\), put

\[
F_r(\chi)=\sum_{j=0}^{N}\chi(Q_j).
\]

For \(1\le h\le N\) and \(0\le i\le N-h\), define the sliding interval product

\[
U_{h,i}=Q_{i+h}Q_i^{-1}
       =\prod_{i<u\le i+h}q_u
       \pmod r
\]

and

\[
C_h(\chi)=\sum_{i=0}^{N-h}\chi(U_{h,i}).
\]

Then

\[
|F_r(\chi)|^2
=V+\sum_{h=1}^{N}\bigl(C_h(\chi)+\overline{C_h(\chi)}\bigr).
\]

Define

\[
A_{h,k}
=
\operatorname{card}\{(i,j):U_{h,i}\equiv U_{k,j}\pmod r\},
\]

\[
B_{h,k}
=
\operatorname{card}\{(i,j):U_{h,i}U_{k,j}\equiv1\pmod r\},
\]

and

\[
D_h=\operatorname{card}\{i:U_{h,i}\equiv1\pmod r\}.
\]

## Proposition 2.1 (exact energy identity)

For every prime \(r>2X\),

\[
\boxed{
\frac1{r-1}\sum_{\chi\bmod r}|F_r(\chi)|^4
=
V^2+4V\sum_{h=1}^{N}D_h
 +2\sum_{h,k=1}^{N}(A_{h,k}+B_{h,k}).
}
\]

The identical interval pairs in \(A_{h,h}\) contribute

\[
V^2+2\sum_{h=1}^{N}(V-h)=2V^2-V.
\]

### Proof

Character orthogonality gives

\[
\frac1{r-1}\sum_\chi C_h(\chi)\overline{C_k(\chi)}=A_{h,k},
\]

\[
\frac1{r-1}\sum_\chi C_h(\chi)C_k(\chi)=B_{h,k},
\]

and

\[
\frac1{r-1}\sum_\chi C_h(\chi)=D_h.
\]

Expanding the square of the displayed expression for \(|F_r(\chi)|^2\) proves the identity. The diagonal count follows because there are \(V-h\) intervals of length \(h\). \(\square\)

# 3. Low-transport collisions

Represent an unordered pair of walk vertices by

\[
\nu=(a,b),
\qquad 0\le a\le b\le N,
\]

with weight \(1\) when \(a=b\) and weight \(2\) when \(a<b\). For

\[
\nu=(a,b),
\qquad
\nu'=(c,d),
\]

define the endpoint transport

\[
\kappa(\nu,\nu')=|a-c|+|b-d|.
\]

## Lemma 3.1 (exact transport identity)

After cancelling common prime factors in

\[
\frac{Q_aQ_b}{Q_cQ_d}=\frac{A}{B},
\qquad (A,B)=1,
\]

the total number of uncancelled dyadic-block prime factors in \(AB\), counted with multiplicity, is exactly

\[
|a-c|+|b-d|.
\]

### Proof

The exponent of \(q_t\) in the reduced ratio is

\[
e_t=\mathbf 1_{t\le a}+\mathbf 1_{t\le b}
    -\mathbf 1_{t\le c}-\mathbf 1_{t\le d}.
\]

For two ordered pairs on a line, monotone matching is optimal in \(\ell^1\), and hence

\[
\sum_{t=1}^{N}|e_t|=|a-c|+|b-d|.
\]

\(\square\)

Let

\[
\mathcal M=\frac{V(V+1)}2
\]

be the number of unordered pair coordinates. Fix

\[
R=4X^2,
\]

and let \(E_r^{(\le H)}\) denote the weighted non-identical collision count

\[
Q_aQ_b\equiv Q_cQ_d\pmod r,
\qquad
0<\kappa((a,b),(c,d))\le H.
\]

## Theorem 3.2 (averaged low-transport energy)

Uniformly for \(1\le H\le 2N\),

\[
\sum_{\substack{R<r\le2R\\ r\ \mathrm{prime}}}
E_r^{(\le H)}
\ll
\mathcal M\frac{\log(2X)}{\log R}
\sum_{k\le H}k^2.
\]

Consequently,

\[
\sum_{r\sim R}E_r^{(\le H)}
=o\!\left(\pi(R,2R)V^2\right)
\]

whenever

\[
H^3\log X=o(X^2).
\]

In particular this holds for

\[
H=o\!\left(\frac{X^{2/3}}{(\log X)^{1/3}}\right).
\]

### Proof

Fix distinct pair coordinates at transport \(k\). By Lemma 3.1, after cancellation their ratio is \(A/B\), where \(AB\) contains exactly \(k\) block-prime factors. The congruence is equivalent to

\[
r\mid A-B.
\]

The integer \(A-B\) is nonzero, because unique factorisation distinguishes distinct exponent vectors, and

\[
\log|A-B|\le k\log(2X)+O(1).
\]

It therefore has at most

\[
\frac{k\log(2X)+O(1)}{\log R}
\]

prime divisors \(r\) satisfying \(R<r\le2R\). For a fixed pair coordinate, the number of coordinates at \(\ell^1\)-distance \(k\) is \(O(k)\). Restoring the pair weights and summing over the \(\mathcal M\) starting coordinates gives \(O(\mathcal M k)\) weighted coordinate pairs at distance \(k\). Summing over \(k\le H\) proves the first assertion.

Finally,

\[
V\asymp\frac{X}{\log X},
\qquad
\pi(R,2R)\asymp\frac{X^2}{\log X},
\]

so the ratio of the preceding bound to \(\pi(R,2R)V^2\) is

\[
O\!\left(\frac{H^3\log X}{X^2}\right).
\]

\(\square\)


## 3.1. Offset-slice large-divisor incidence

Let

\[
A=\prod_{p<X}p,
\qquad
P_j=AQ_j
\quad(0\le j<N).
\]

Let \(\mathcal I\) be an interval of \(L\) consecutive integers and let \(\mathcal R\) be the primes in \([R,2R]\), where

\[
R>\max(L,2X).
\]

For coefficients \(c_0,\ldots,c_{N-1}\in\mathbb C\), put

\[
T_{r,m}(c)
=
\sum_{j=0}^{N-1}c_j\mathbf 1_{r\mid P_j+m}.
\]

## Theorem 3.3 (weighted offset-slice large-divisor incidence bound)

One has

\[
\boxed{
\sum_{r\in\mathcal R}
\sum_{m\in\mathcal I}
|T_{r,m}(c)|^2
\le
\left(
|\mathcal R|
+
\frac{N(N-1)}2\frac{\log(2X)}{\log R}
\right)
\sum_{j=0}^{N-1}|c_j|^2.
}
\]

### Proof

After expanding the square, the diagonal terms contribute at most

\[
|\mathcal R|\sum_j|c_j|^2,
\]

because for fixed \((r,j)\) the interval \(\mathcal I\), of length smaller than \(r\), contains at most one solution to \(P_j+m\equiv0\pmod r\).

For \(j<k\), write \(h=k-j\). If the same \((r,m)\) contributes to both centres, then

\[
r\mid P_k-P_j
=P_j\left(\frac{P_k}{P_j}-1\right).
\]

Since \(r>2X\), it divides no factor of \(P_j\). Hence

\[
r\mid U_{j,k}-1,
\qquad
U_{j,k}=\frac{P_k}{P_j}=\prod_{j<u\le k}q_u.
\]

The integer \(U_{j,k}-1\) has at most

\[
h\frac{\log(2X)}{\log R}
\]

prime divisors in \([R,2R]\). For every such prime there is at most one compatible \(m\in\mathcal I\). Thus the off-diagonal kernel is bounded by

\[
K_{j,k}\le |j-k|\frac{\log(2X)}{\log R}.
\]

Using \(2|c_jc_k|\le |c_j|^2+|c_k|^2\), the off-diagonal contribution is at most

\[
\left(\max_j\sum_{k\ne j}K_{j,k}\right)
\sum_j|c_j|^2.
\]

Finally,

\[
\max_j\sum_{k\ne j}|j-k|=\frac{N(N-1)}2.
\]

This proves the theorem. \(\square\)

For unweighted occupancies

\[
B_{r,m}=\operatorname{card}\{0\le j<N:r\mid P_j+m\},
\]

the sharper direct count gives

\[
\sum_{r\in\mathcal R}\sum_{m\in\mathcal I}B_{r,m}^2
\le
N|\mathcal R|
+
\frac{N(N^2-1)}3\frac{\log(2X)}{\log R}.
\]

When \(R\asymp X^2\), the off-diagonal term is smaller than the diagonal benchmark by \(O(1/\log X)\). Thus the incidence matrix is diagonal-dominant at this modulus scale. The theorem controls large-divisor collisions rather than the parity-sensitive signed coefficients required to detect shifted primes.


## 3.2. Average almost-injectivity of the cumulative path


For a prime \(r>2X\), define

\[
\nu_r(a)=\#\{0\le j\le N:Q_j\equiv a\pmod r\},
\qquad
D_r=\#\{a:\nu_r(a)>0\},
\]

and

\[
C_r=\sum_a\binom{\nu_r(a)}2.
\]

### Theorem 3.4

Let \(\mathcal R\) be the primes in \([R,2R]\), where \(R>2X\), and put \(M=N+1\). Then

\[
\sum_{r\in\mathcal R}C_r
\le
\frac{M(M^2-1)}6\frac{\log(2X)}{\log R}.
\]

Consequently,

\[
\sum_{r\in\mathcal R}(M-D_r)
\le
\frac{M(M^2-1)}6\frac{\log(2X)}{\log R},
\]

and

\[
\sum_{r\in\mathcal R}\sum_a\nu_r(a)^2
\le
M|\mathcal R|
+
\frac{M(M^2-1)}3\frac{\log(2X)}{\log R}.
\]

#### Proof

For \(j<k\), the congruence \(Q_j\equiv Q_k\pmod r\) is equivalent to

\[
r\mid \prod_{j<u\le k}q_u-1,
\]

because \(r>2X\) divides none of the block primes. The integer on the right has logarithm less than \((k-j)\log(2X)\), and hence at most

\[
(k-j)\frac{\log(2X)}{\log R}
\]

prime divisors in \([R,2R]\). Summing over \(0\le j<k<M\) and using

\[
\sum_{0\le j<k<M}(k-j)=\frac{M(M^2-1)}6
\]

proves the collision bound. The support deficit satisfies

\[
M-D_r=\sum_{a:\nu_r(a)>0}(\nu_r(a)-1)\le C_r,
\]

and \(\sum_a\nu_r(a)^2=M+2C_r\). \(\square\)

### Corollary 3.5

If \(R\asymp X^2\), then

\[
\frac1{|\mathcal R|}\sum_{r\in\mathcal R}\frac{M-D_r}{M}
\ll \frac1{\log X}.
\]

For every fixed \(\varepsilon>0\), all but

\[
O\!\left(\frac{|\mathcal R|}{\varepsilon\log X}\right)
\]

primes \(r\in\mathcal R\) satisfy

\[
D_r\ge(1-\varepsilon)M.
\]

This settles the pair-collision or distinct-residue problem for the cumulative path. It does not control the fourth-order two-run energy HTE4.


## 3.3. Nearby pairs of collision intervals

Let

\[
\mathscr I_M=\{(a,b):0\le a<b<M\},
\qquad
U_{a,b}=Q_bQ_a^{-1},
\]

so that

\[
C_r=\#\{I\in\mathscr I_M:U_I\equiv1\pmod r\}.
\]

For intervals \(I=(a,b)\) and \(J=(c,d)\), set

\[
\kappa(I,J)=|a-c|+|b-d|.
\]

### Proposition 3.6

For \(R>2X\),

\[
\sum_{r\sim R}\binom{C_r}{2}
\le
\frac{M(M-1)(M-2)(M+1)(2M-1)}{30}
\frac{\log(2X)}{\log R}.
\]

More locally, if

\[
F_r(H)=\#\left\{\{I,J\}:U_I\equiv U_J\equiv1\pmod r,
\ 1\le\kappa(I,J)\le H\right\},
\]

then, with \(K=\binom M2\),

\[
\boxed{
\sum_{r\sim R}F_r(H)
\le
\frac{K H(H+1)(2H+1)}3
\frac{\log(2X)}{\log R}.
}
\]

#### Proof

For distinct intervals \(I=(a,b)\) and \(J=(c,d)\), cancel common prime factors in

\[
\frac{U_I}{U_J}=\frac AB.
\]

The reduced numerator and denominator contain exactly

\[
\kappa(I,J)=|a-c|+|b-d|
\]

block-prime factors in total. If both interval products are congruent to \(1\pmod r\), then \(r\mid A-B\). Hence the number of shell primes producing this pair of collisions is at most

\[
\kappa(I,J)\frac{\log(2X)}{\log R}.
\]

Summing over all interval pairs and using

\[
\sum_{\{I,J\}\subset\mathscr I_M}\kappa(I,J)
=
\frac{M(M-1)(M-2)(M+1)(2M-1)}{30}
\]

proves the first bound.

For fixed \(I\), at most \(4h\) interval coordinates lie at \(\ell^1\)-distance \(h\). Thus there are at most \(2Kh\) unordered interval pairs at transport \(h\). Multiplying by the preceding prime-divisor bound and summing \(h^2\) proves the local estimate. \(\square\)

### Corollary 3.7

If \(R\asymp X^2\) and

\[
H=o((\log X)^{1/3}),
\]

then

\[
\frac1{\pi(R,2R)}\sum_{r\sim R}F_r(H)=o(1).
\]

Consequently, for almost all shell primes, any two collision intervals are separated by endpoint transport exceeding \(H\).

This does not prove the random-scale all-transport second factorial moment. In the independent-residue model, if \(K=\binom M2\), then

\[
\mathbb E C_r=\frac K{r-1},
\qquad
\mathbb E\binom{C_r}{2}=\frac{\binom K2}{(r-1)^2}.
\]


# 4. Endpoint graphs, affine rank, and Smith forms

For an interval \(I=\{a+1,\ldots,b\}\subseteq\{1,\ldots,N\}\), let \(v_I\in\mathbb Z^N\) be its \(0\)-\(1\) exponent vector. The discrete derivative sends

\[
v_I\longmapsto e_a-e_b,
\]

where the endpoint coordinates are indexed by \(0,\ldots,N\). This identifies interval vectors, integrally and unimodularly, with oriented edges on their endpoint set.

Let \(\mathcal F=\{I_1,\ldots,I_k\}\) be a family of distinct intervals. Its endpoint graph \(G_{\mathcal F}\) has one vertex for every endpoint used by the family and one edge, oriented from the left endpoint to the right endpoint, for every interval. Let \(v\) be the number of graph vertices and \(c\) its number of connected components.

For an undirected cycle \(C\), traverse it in either direction and put

\[
\sigma(C)=\sum_{e\in C}\varepsilon_e,
\]

where \(\varepsilon_e=1\) if the traversal follows the orientation of \(e\), and \(-1\) otherwise. Define

\[
g(\mathcal F)=\gcd_C|\sigma(C)|,
\]

with \(g(\mathcal F)=0\) when every cycle imbalance vanishes.

## Theorem 4.1 (affine rank and Smith form)

The affine rank \(d(\mathcal F)\) of the interval exponent vectors is

\[
d(\mathcal F)=
\begin{cases}
 v-c-1,&g(\mathcal F)=0,\\
 v-c,&g(\mathcal F)>0.
\end{cases}
\]

If \(g(\mathcal F)=0\), every nonzero Smith invariant of an affine difference matrix is \(1\). If \(g(\mathcal F)>0\), the nonzero invariants are

\[
1,\ldots,1,g(\mathcal F).
\]

Moreover,

\[
1\le g(\mathcal F)\le k
\]

whenever \(g(\mathcal F)>0\).

### Proof

Let \(B\) be the oriented vertex-edge incidence matrix of \(G_{\mathcal F}\), and append a row of ones:

\[
C=\begin{pmatrix}B\\ \mathbf1^T\end{pmatrix}.
\]

The affine rank of the edge columns is \(\operatorname{rank}C-1\). The incidence matrix has rank \(v-c\). Its row span contains the all-ones edge vector precisely when there is a potential \(h\) on the vertices satisfying

\[
h(a)-h(b)=1
\]

for every oriented edge \(a\to b\). Such a potential exists if and only if every signed cycle imbalance is zero. Appending the ones row therefore either preserves the rank or raises it by one, proving the rank formula.

We next compute the Smith form of \(C\). Choose a spanning forest. By unimodular row operations, transform one redundant incidence row in each connected component to a zero row; discarding those zero rows does not change the nonzero Smith invariants. The resulting square forest submatrix is unimodular. Using it as a pivot block, reduce the forest columns to an identity matrix and clear the incidence entries of every nonforest column. If \(e\) is a nonforest edge, the remaining entry in its last row is, up to sign, the signed imbalance of the corresponding fundamental cycle. Clearing the last-row entries under the forest columns therefore gives an integral equivalence

\[
C\sim_{\mathbb Z}
\begin{pmatrix}
I_{v-c}&0\\
0&\sigma_1\ \cdots\ \sigma_{k-v+c}
\end{pmatrix},
\]

where the \(\sigma_j\) are the fundamental-cycle imbalances. Consequently the nonzero Smith invariants of \(C\) are \(v-c\) unit invariants, together with one further invariant \(g(\mathcal F)\) when this gcd is nonzero.

It remains to pass from the augmented columns to affine differences without appealing only to rank. Choose one edge column \(c_1=(b_1,1)^T\). For every \(j>1\), perform the unimodular column operation \(c_j\mapsto c_j-c_1\). The last row becomes \((1,0,\ldots,0)\). Using that unit entry, clear the incidence entries above the first column by unimodular row operations. The resulting matrix is

\[
\begin{pmatrix}
1&0\\
0&D
\end{pmatrix},
\]

where the columns of \(D\) are \(b_j-b_1\), an affine-difference matrix. Hence

\[
\operatorname{SNF}(C)=1\oplus\operatorname{SNF}(D).
\]

Removing this explicit unit invariant yields the stated Smith form for affine differences. Finally, every cycle uses at most \(k\) edges, so \(|\sigma(C)|\le k\), and therefore \(g(\mathcal F)\le k\). \(\square\)

## Corollary 4.2 (independent-step occupancy probability)

Let the prime increments be independent uniform elements of a cyclic group of order \(n\). Then

\[
\Pr(U_{I_1}=\cdots=U_{I_k})
=
\begin{cases}
n^{-d(\mathcal F)},&g(\mathcal F)=0,\\
\gcd(g(\mathcal F),n)n^{-d(\mathcal F)},&g(\mathcal F)>0.
\end{cases}
\]

Thus the torsion correction is at most \(k\), rather than exponential in the family size.

# 5. The centered two-run energy problem

For

\[
0\le a<b<c<d<V,
\]

define

\[
W_{a,b,c,d}
=
\frac{Q_bQ_d}{Q_aQ_c}
=
\left(\prod_{a<u\le b}q_u\right)
\left(\prod_{c<u\le d}q_u\right).
\]

Let

\[
\mathcal A_2=\{(a,b,c,d):0\le a<b<c<d<V\},
\qquad
P=|\mathcal A_2|=\binom V4,
\]

and

\[
K_{4,r}(\chi)=\sum_{A\in\mathcal A_2}\chi(W_A).
\]

If

\[
\eta_r(x)=\operatorname{card}\{A\in\mathcal A_2:W_A\equiv x\pmod r\},
\]

then character orthogonality gives

\[
\frac1{r-1}\sum_{\chi\ne\chi_0}|K_{4,r}(\chi)|^2
=
\sum_x\eta_r(x)^2-\frac{P^2}{r-1}.
\]

The target estimate is the following.

## HTE4 (open)

Prove, for \(R\asymp X^2\),

\[
\boxed{
\sum_{r\sim R}\frac1{r-1}
\sum_{\chi\ne\chi_0}|K_{4,r}(\chi)|^2
\ll
\pi(R,2R)P X^{o(1)}.
}
\]

No proof of HTE4 is claimed.

## 5.1. Exact pair-overlap decomposition

For \(A,B\in\mathcal A_2\), write \(A\sim_kB\) when their endpoint sets have exactly \(k\) common elements. Define

\[
C_{r,k}
=
\operatorname{card}\{(A,B)\in\mathcal A_2^2:
A\sim_kB,\ W_A\equiv W_B\pmod r\}
\]

and

\[
N_k
=
P\binom4k\binom{V-4}{4-k}.
\]

### Proposition 5.1 (pair-overlap identity)

For every prime \(r>2X\),

\[
\boxed{
\frac1{r-1}\sum_{\chi\ne\chi_0}|K_{4,r}(\chi)|^2
=
\sum_{k=0}^{4}
\left(C_{r,k}-\frac{N_k}{r-1}\right).
}
\]

The diagonal sector is

\[
C_{r,4}-\frac{N_4}{r-1}
=
P\left(1-\frac1{r-1}\right).
\]

### Proof

Expand the character square and apply multiplicative orthogonality:

\[
\frac1{r-1}\sum_{\chi\bmod r}
\chi(W_A)\overline{\chi(W_B)}
=
\mathbf 1_{W_A\equiv W_B\pmod r}.
\]

Removing the principal character subtracts \(1/(r-1)\) for every ordered support pair. Partitioning the pairs by \(|A\cap B|\) gives the formula. When \(k=4\), the supports coincide, so \(C_{r,4}=N_4=P\). \(\square\)

## 5.2. Pair-overlap transport bounds

For a non-diagonal pair \((A,B)\) with \(|A\cap B|=k\), let

\[
t_1<\cdots<t_{8-k}
\]

be its ordered endpoint union. Write \(e=(e_j)\) for the difference of the two alternating endpoint vectors, and set

\[
\tau(e)
=
\sum_{i=1}^{7-k}
\left|\sum_{j\le i}e_j\right|.
\]

After cancellation, the reduced quotient \(W_A/W_B=C/D\) contains

\[
\sum_{i=1}^{7-k}
\left|\sum_{j\le i}e_j\right|(t_{i+1}-t_i)
\]

block-prime factors, counted with multiplicity.

### Theorem 5.2 (pair-overlap large-divisor bounds)

Let \(\mathcal R\) be the primes in \([R,2R]\), with \(R>2X\). Then, for \(0\le k\le3\),

\[
\boxed{
\sum_{r\in\mathcal R}C_{r,k}
\le
T_k\binom{V+1}{9-k}
\frac{\log(2X)}{\log R},
}
\]

where

\[
(T_0,T_1,T_2,T_3)=(280,480,252,40).
\]

### Proof

Fix a non-diagonal ordered pair and write the reduced quotient as \(C/D\). A shell prime supporting the congruence divides the nonzero integer \(C-D\). Hence the number of such primes is at most

\[
\frac{\log|C-D|}{\log R}
\le
\frac{\log(2X)}{\log R}
\sum_{i=1}^{7-k}
\left|\sum_{j\le i}e_j\right|(t_{i+1}-t_i).
\]

For every fixed endpoint template and every internal gap,

\[
\sum_{0\le t_1<\cdots<t_{8-k}<V}
(t_{i+1}-t_i)
=
\binom{V+1}{9-k}.
\]

There are respectively \(70,140,90,20\) ordered templates. Summing their cumulative transport coefficients gives \(280,480,252,40\). Summation over placements and templates proves the claim. The finite template table is included in the supplementary archive. \(\square\)

### Corollary 5.3 (three-shared-endpoint closure)

At

\[
V\asymp\frac{X}{\log X},
\qquad
R\asymp X^2,
\]

the \(k=3\) sector contributes

\[
O\left(\frac{\pi(R,2R)P}{\log X}\right)
\]

to the positive off-diagonal collision count. It is therefore negligible at the HTE4 scale.

### Proof

Theorem 5.2 gives \(O(V^6)\) up to logarithmic factors for \(k=3\), whereas \(\pi(R,2R)P\asymp X^2V^4/\log X\). Substitution of \(V\asymp X/\log X\) gives the stated relative factor \(O(1/\log X)\). \(\square\)

## 5.3. Median decomposition of the disjoint sector

For \(k=0\), order the eight endpoints as

\[
t_1<\cdots<t_8
\]

and split after \(t_4=m\). Across the \(70\) assignments of four endpoints to each support, each half has two positive and two negative prefix exponents. Only four half-patterns occur:

\[
W=(-,+,-,+),\quad \bar W=(+,-,+,-),
\]

\[
X=(-,+,+,-),\quad \bar X=(+,-,-,+).
\]

For each median \(m\), let \(L_m(\chi)\) and \(R_m(\chi)\) be the four-component vectors of left and right half-sums indexed by these patterns.

### Proposition 5.4 (exact median bilinear identity)

The centered disjoint sector

\[
\mathcal D_0(r)=C_{r,0}-\frac{N_0}{r-1}
\]

has the exact representation

\[
\boxed{
\mathcal D_0(r)
=
\frac1{r-1}
\sum_{\chi\ne\chi_0}\sum_m
L_m(\chi)^{\mathsf T}M R_m(\chi),
}
\]

where

\[
M=
\begin{pmatrix}
3&4&4&4\\
4&3&4&4\\
4&4&8&4\\
4&4&4&8
\end{pmatrix}.
\]

The eigenvalues of \(M\) are

\[
-1,\qquad
\frac{19-\sqrt{281}}2,\qquad
4,\qquad
\frac{19+\sqrt{281}}2.
\]

### Proof

For each of the \(70\) interleavings, restrict the alternating endpoint signs of \(W_A/W_B\) to the first and last four ordered endpoints. Direct classification gives one of the four displayed patterns on each side. Counting the resulting ordered pattern pairs gives the matrix \(M\). Character orthogonality with the principal character removed preserves the exact centering term. The characteristic polynomial of \(M\) gives the four eigenvalues. \(\square\)

Every half-pattern has exponent sum zero. Hence the common prefix \(Q_m\) cancels: the left vector depends only on increment primes at or before \(m\), and the right vector only on increment primes after \(m\). This is a genuine separation into disjoint arithmetic blocks.

Nevertheless, even ideal square-root estimates for the separate half-kernels are insufficient. Since

\[
\sum_m\binom m3=\binom V4=P,
\qquad
\sum_m\binom{V-1-m}{4}=\binom V5,
\]

Cauchy--Schwarz gives

\[
|\mathcal D_0(r)|
\lesssim
4\|M\|\sqrt{\binom V4\binom V5}
=
4\|M\|P\sqrt{\frac{V-4}{5}}.
\]

Thus separate half-energy control loses a factor \(\asymp\sqrt V\) relative to HTE4. Any successful argument must obtain cancellation in the median variable or between the four channels.

## 5.4. Exact independent-prefix median law

The median decomposition has an exact null model. Let \(G\) be a finite abelian group of order \(q\), let \(Z_0,\ldots,Z_{V-1}\) be independent uniform elements of \(G\), and let \(C_m\) count ordered disjoint-support two-run equalities whose eight-point union has fourth endpoint \(m\). Put

\[
S_m=\binom m3\binom{V-1-m}{4},
\qquad
\tau=|G[2]|.
\]

### Theorem 5.5 (exact median-cut mean and covariance)

For every active median \(m\),

\[
\boxed{\mathbb E C_m=\frac{70S_m}{q},}
\]

\[
\boxed{
\operatorname{Var}(C_m)
=
S_m\left(
\frac{676}{q}
+
\frac{4224\tau-4900}{q^2}
\right),
}
\]

and, for \(m\ne n\),

\[
\boxed{\operatorname{Cov}(C_m,C_n)=0.}
\]

Consequently,

\[
\boxed{
\operatorname{Var}\left(\sum_m C_m\right)
=
\binom V8
\left(
\frac{676}{q}
+
\frac{4224\tau-4900}{q^2}
\right).
}
\]

### Proof

On a fixed ordered eight-set, the \(70\) templates collapse, after identifying an equation with its negative, to eight primitive equations with multiplicities

\[
6,8,8,8,8,8,8,16.
\]

Each equation holds with probability \(1/q\), giving the mean. Distinct unoriented equations on the same eight-set have two-row Smith form \(\operatorname{diag}(1,2)\), so their joint probability is \(\tau/q^2\). Combining diagonal and off-diagonal weighted event pairs yields

\[
676/q+(4224\tau-4900)/q^2
\]

per eight-set.

If two equations have different eight-point supports, one row has a nonzero coordinate where the other is zero. Pairing that coordinate with a nonzero coordinate of the second row gives a \(2\times2\) minor equal to \(\pm1\). Their two-row Smith form is therefore \(\operatorname{diag}(1,1)\), and the equations are exactly independent over every finite abelian group. Different medians necessarily use different eight-point supports, proving zero covariance. Finally,

\[
\sum_mS_m=\binom V8,
\]

which gives the total variance. \(\square\)

The theorem explains exact median dispersion in the independent-prefix model. It does not provide the corresponding arithmetic estimate for consecutive-prime prefixes; that would require a centered rank-two common-divisor theorem.

## 5.5. Exact fourth-moment law of the two-run spectrum

The fourth moment over individual character values is a different object from HTE4, but it supplies the correct spectral benchmark. Let \(Z_0,\ldots,Z_{V-1}\) be independent uniform roots of unity and define

\[
K_V
=
\sum_{0\le a<b<c<d<V}
\overline{Z_a}Z_b\overline{Z_c}Z_d.
\]

### Proposition 5.6 (non-Gaussian spectral law)

For root order at least three,

\[
\mathbb E|K_V|^2=\binom V4
\]

and

\[
\boxed{
\mathbb E|K_V|^4
=
\binom V4
+40\binom V5
+420\binom V6
+1736\binom V7
+2556\binom V8.
}
\]

In particular,

\[
\frac{\mathbb E|K_V|^4}{2\binom V4^2}
\longrightarrow
\frac{639}{35}.
\]

### Proof

Process the phases in increasing index and define the iterated sums

\[
A=\sum_a\overline{Z_a},\qquad
B=\sum_{a<b}\overline{Z_a}Z_b,
\]

\[
C=\sum_{a<b<c}\overline{Z_a}Z_b\overline{Z_c},
\qquad
D=K_V.
\]

On adjoining a new phase \(z\),

\[
A'=A+\overline z,\qquad
B'=B+zA,\qquad
C'=C+\overline zB,\qquad
D'=D+zC.
\]

Expanding all mixed moments of total degree at most four and averaging over \(z\) gives a closed finite recurrence. Starting at \(A=B=C=D=0\) and iterating \(V\) times yields the displayed polynomial. Equivalently, the coefficient of \(\binom Vk\) counts balanced ordered quadruples of alternating four-endpoint exponent vectors whose union has exactly \(k\) vertices; the counts are \(1,40,420,1736,2556\). Both finite derivations are included in the supplementary verification code. The asymptotic follows from the leading \(\binom V8\) term. \(\square\)

Only \(140\) of the \(2556\) leading eight-vertex configurations are ordinary Wick pairings. Thus sparse large individual-character values and a normalized fourth moment far above the complex-Gaussian value are intrinsic to the ordered kernel; they are not by themselves evidence against HTE4.

## 5.6. The remaining arithmetic target

The pair-overlap bounds close the \(k=3\) sector. The unresolved burden lies in the centered \(k=0,1,2\) sectors, principally disjoint supports and one-shared-endpoint pairs. The median identity shows that the disjoint sector is a four-channel centered bilinear form with disjoint prime blocks, but standard Cauchy--Schwarz loses \(\sqrt V\). Theorem 5.5 shows what random median dispersion should look like, but its arithmetic analogue requires new input: a centered rank-two Barban--Davenport--Halberstam-type estimate for common large prime divisors of two interval-product differences.

# 6. A support-family divisor estimate

## Theorem 6.1

Let \(\mathcal F\subseteq\mathcal A_2\) be a family of \(M\) distinct two-run supports. Then

\[
\sum_{r\sim R}\frac1{r-1}
\sum_{\chi\bmod r}
\left|\sum_{A\in\mathcal F}\chi(W_A)\right|^2
\le
\pi(R,2R)M
+
\frac{N\log(2X)+O(1)}{\log R}M(M-1).
\]

### Proof

Orthogonality turns the left side into the number of ordered triples \((r,A,B)\) with

\[
W_A\equiv W_B\pmod r.
\]

The \(A=B\) terms contribute \(\pi(R,2R)M\). For \(A\ne B\), cancel common prime factors and write

\[
\frac{W_A}{W_B}=\frac{C}{D},
\qquad (C,D)=1.
\]

Each two-run support is a \(0\)-\(1\) exponent vector on the \(N\) prime increments. Their difference has entries in \(\{-1,0,1\}\), and hence the reduced ratio contains at most \(N\) uncancelled prime factors. Therefore

\[
\log|C-D|\le N\log(2X)+O(1).
\]

For one ordered pair \((A,B)\), the number of prime divisors \(r\) of \(C-D\) satisfying \(R<r\le2R\) is at most the displayed logarithmic ratio. Summing over the \(M(M-1)\) ordered off-diagonal pairs proves the theorem. \(\square\)

Since \(N\asymp V\) and \(\pi(R,2R)\asymp V^2\log X\), this theorem controls any family of size

\[
M\le V^{5/2-o(1)}
\]

at the global HTE4 scale.

# 7. Block compositions and unconditional closure

Partition the \(V\) walk vertices into \(B\) consecutive blocks \(I_1<\cdots<I_B\), with block sizes at most \(m\) and \(Bm\asymp V\). Define

\[
S_i=\sum_{u\in I_i}\chi(Q_u),
\]

\[
T_i=\sum_{\substack{u<v\\u,v\in I_i}}
\overline{\chi(Q_u)}\chi(Q_v),
\]

and

\[
U_i=\sum_{\substack{u<v<w\\u,v,w\in I_i}}
\overline{\chi(Q_u)}\chi(Q_v)\overline{\chi(Q_w)}.
\]

For equal block size \(m\), the endpoint-composition masses are

\[
P_{1111}=\binom B4m^4,
\]

\[
P_{211}=P_{121}=P_{112}
=\binom B3\binom m2m^2,
\]

\[
P_{22}=\binom B2\binom m2^2,
\]

\[
P_{31}=P_{13}=\binom B2\binom m3m,
\]

and

\[
P_4=B\binom m4.
\]

They satisfy the exact packing identity

\[
P_{1111}+3P_{211}+P_{22}+2P_{31}+P_4
=\binom{Bm}{4}.
\]

## Theorem 7.1 (sparse-composition closure)

Take

\[
m=V^{1/5},
\qquad
B=V^{4/5},
\]

up to integer rounding. Then the composition families

\[
22,\qquad31,\qquad13,\qquad4
\]

are controlled unconditionally at the global HTE4 scale by Theorem 6.1. The unresolved root quartet is

\[
1111+211+121+112.
\]

### Proof

The four family sizes satisfy

\[
P_{22},P_{31},P_{13}\ll B^2m^4\asymp V^{12/5}
\]

and

\[
P_4\ll Bm^4\asymp V^{8/5}.
\]

All four exponents are below \(5/2\), so Theorem 6.1 supplies a fixed power saving relative to the global HTE4 scale. \(\square\)

More generally, the same argument closes these four families whenever

\[
m\le V^{1/4-o(1)}.
\]

In particular it remains available for the fine-block choice \(m=(\log X)^A\).

# 8. Edge factorisation and the correct conditional interface

The three mixed edge terms factor exactly. Define

\[
H_i^{\mathrm R}=\sum_{i<j<k}\overline{S_j}S_k,
\qquad
H_i^{\mathrm L}=\sum_{j<k<i}\overline{S_j}S_k,
\]

and

\[
P_i=\sum_{j<i}S_j,
\qquad
R_i=\sum_{k>i}S_k.
\]

Then

\[
G_{211}=\sum_iT_iH_i^{\mathrm R},
\]

\[
G_{112}=\sum_iH_i^{\mathrm L}T_i,
\]

and

\[
G_{121}=\sum_i\overline{T_i}\,\overline{P_i}R_i.
\]

These identities alone do not make the full edge energies equal to a hereditary fourth moment. Squaring \(G_{211}\), for example, creates cross terms in the block index \(i\). The valid bridge is a two-stage argument: weighted Cauchy reduces the full edge energy to a square function, and a separate comparison relates that square function to hereditary cumulative-walk fourth moments.

Let

\[
L_i=\binom{|I_i|}{2}.
\]

Since \(|T_i|\le L_i\), weighted Cauchy gives

\[
|G_{211}|^2
\le
\left(\sum_iL_i\right)
\left(\sum_iL_i|H_i^{\mathrm R}|^2\right),
\]

with analogous bounds for \(G_{112}\) and \(G_{121}\).

## 8.1. Suffix square function

For a cut after block \(i\), let

\[
F_i^{\mathrm R}=\sum_{j>i}\sum_{u\in I_j}\chi(Q_u),
\qquad
N_i^{\mathrm R}=\sum_{j>i}|I_j|.
\]

Let \(J_i^{\mathrm R}\) be the ordered-pair sum with both endpoints in one later block, and let \(H_i^{\mathrm R}\) be the ordered-pair sum with endpoints in two distinct later blocks. Then

\[
C_i^{\mathrm R}=H_i^{\mathrm R}+J_i^{\mathrm R}
\]

is the complete ordered-pair sum in the suffix, and

\[
\boxed{
2\operatorname{Re}C_i^{\mathrm R}=|F_i^{\mathrm R}|^2-N_i^{\mathrm R}.
}
\]

Define

\[
\mathcal W_{\mathrm R}=\sum_iL_i\bigl(|F_i^{\mathrm R}|^2-N_i^{\mathrm R}\bigr)^2,
\]

\[
\mathcal H_{\mathrm R}=\sum_iL_i|H_i^{\mathrm R}|^2,
\qquad
\mathcal J_{\mathrm R}=\sum_iL_i|J_i^{\mathrm R}|^2.
\]

## Proposition 8.1 (square-function comparison)

Pointwise in \(\chi\),

\[
\mathcal W_{\mathrm R}\le8(\mathcal H_{\mathrm R}+\mathcal J_{\mathrm R}).
\]

Suppose additionally that

\[
3\binom{N_i^{\mathrm R}}{2}\le r-1
\]

for every suffix under consideration. Then, after averaging over the nonprincipal characters,

\[
\frac1{r-1}\sum_{\chi\ne\chi_0}\mathcal H_{\mathrm R}
\le
2\frac1{r-1}\sum_{\chi\ne\chi_0}\mathcal W_{\mathrm R}
+2\frac1{r-1}\sum_{\chi\ne\chi_0}\mathcal J_{\mathrm R}.
\]

For \(r\asymp X^2\) and \(N_i^{\mathrm R}\le V\asymp X/\log X\), the support-size condition holds for all sufficiently large \(X\).

### Proof

The pointwise inequality follows from

\[
4(\operatorname{Re}(H_i^{\mathrm R}+J_i^{\mathrm R}))^2
\le8(|H_i^{\mathrm R}|^2+|J_i^{\mathrm R}|^2).
\]

For the converse, fix \(i\), put \(s_i=\binom{N_i^{\mathrm R}}{2}\), and write \(C_i^{\mathrm R}\) as a sum of \(s_i\) character values. Let \(e_i\) and \(\rho_i\) be the equality and reciprocal incidence counts for those \(s_i\) support values. Character orthogonality gives

\[
\frac1{r-1}\sum_{\chi\ne\chi_0}|C_i^{\mathrm R}|^2
=e_i-\frac{s_i^2}{r-1},
\]

and

\[
\frac1{r-1}\sum_{\chi\ne\chi_0}
\bigl(|F_i^{\mathrm R}|^2-N_i^{\mathrm R}\bigr)^2
=2(e_i+\rho_i)-\frac{4s_i^2}{r-1}.
\]

Since \(e_i\ge s_i\) from the identical pairs and \(\rho_i\ge0\), the second expression minus the first is at least

\[
s_i-\frac{3s_i^2}{r-1},
\]

which is nonnegative under the stated support-size condition. Hence the nonprincipal average of \(|C_i^{\mathrm R}|^2\) is bounded by that of \((|F_i^{\mathrm R}|^2-N_i^{\mathrm R})^2\). Finally,

\[
|H_i^{\mathrm R}|^2=|C_i^{\mathrm R}-J_i^{\mathrm R}|^2
\le2|C_i^{\mathrm R}|^2+2|J_i^{\mathrm R}|^2.
\]

Multiplying by \(L_i\) and summing over \(i\) proves the result. \(\square\)

## Lemma 8.2 (local within-block correction)

For balanced blocks of size at most \(m\),

\[
\boxed{
\sum_{r\sim R}\frac1{r-1}\sum_{\chi\bmod r}\mathcal J_{\mathrm R}
\ll
\pi(R,2R)V^2m^2
+
V^4m^3\frac{\log(2X)}{\log R}.
}
\]

### Proof

For a fixed cut \(i\), let \(\mathcal S_i\) be the family of interval supports whose two endpoints lie in one block strictly to the right of \(i\). Its cardinality satisfies

\[
M_i=|\mathcal S_i|
=\sum_{j>i}\binom{|I_j|}{2}
\ll (B-i)m^2.
\]

The quantity \(J_i^{\mathrm R}\) is the character sum over \(\mathcal S_i\). Character orthogonality and the same one-run prime-divisor count used in Theorem 6.1 give, after multiplication by \(L_i\),

\[
\sum_{r\sim R}\frac1{r-1}\sum_{\chi\bmod r}L_i|J_i^{\mathrm R}|^2
\ll
L_i\pi(R,2R)M_i
+
L_i\frac{N\log(2X)}{\log R}M_i(M_i-1).
\]

Since \(L_i\ll m^2\), summing the diagonal terms over the cuts yields

\[
\sum_iL_iM_i
\ll
m^4\sum_{t\le B}t
\ll B^2m^4
\ll V^2m^2.
\]

Similarly,

\[
\sum_iL_iM_i^2
\ll
m^6\sum_{t\le B}t^2
\ll B^3m^6
\ll V^3m^3.
\]

Using \(N\asymp V\) proves the displayed estimate. \(\square\)

At fine scale \(m=X^{o(1)}\), this correction is negligible, up to a subpolynomial factor, relative to the natural hereditary square-function scale \(\pi(R,2R)V^3m\).

## 8.2. HWF4 and conditional edge closure

The hereditary weighted fourth-moment estimate needed here is the following open statement, together with its reflected prefix version:

## HWF4 (open)

For balanced fine blocks of maximum size \(m=X^{o(1)}\), prove

\[
\boxed{
\sum_{r\sim R}\frac1{r-1}\sum_{\chi\ne\chi_0}
\sum_iL_i\bigl(|F_i^{\mathrm R}(\chi)|^2-N_i^{\mathrm R}\bigr)^2
\ll
\pi(R,2R)V^3mX^{o(1)}.
}
\]

The crossing square function is controlled by the same prefix and suffix estimate, because

\[
|P_i|^2|R_i|^2
\le\frac{|P_i|^4+|R_i|^4}{2}
\]

and

\[
|F|^4\le2(|F|^2-|I|)^2+2|I|^2.
\]

## Proposition 8.3 (conditional edge implication)

Assume HWF4 and its prefix counterpart for a fine partition with \(m=X^{o(1)}\). Then the aggregate nonprincipal hybrid energies of each of

\[
211,\qquad112,\qquad121
\]

are

\[
\ll
\pi(R,2R)V^4X^{o(1)}.
\]

### Proof

For balanced blocks,

\[
\sum_iL_i\ll Vm.
\]

For \(211\), weighted Cauchy and Proposition 8.1, always restricted to \(\chi\ne\chi_0\), give

\[
\begin{aligned}
&\sum_{r\sim R}\frac1{r-1}
\sum_{\chi\ne\chi_0}|G_{211}|^2\\
&\qquad\ll
(Vm)
\left(
\sum_{r\sim R}\frac1{r-1}
\sum_{\chi\ne\chi_0}\mathcal W_{\mathrm R}
+
\sum_{r\sim R}\frac1{r-1}
\sum_{\chi\ne\chi_0}\mathcal J_{\mathrm R}
\right).
\end{aligned}
\]

HWF4 bounds the first term in parentheses by

\[
\pi(R,2R)V^3mX^{o(1)}.
\]

Lemma 8.2 bounds the second, because the nonprincipal sum is no larger than the all-character sum, by

\[
\pi(R,2R)V^2m^2
+
V^4m^3\frac{\log(2X)}{\log R}.
\]

After multiplication by \(Vm\), the HWF4 contribution is \(\pi(R,2R)V^4m^2X^{o(1)}\). The two local contributions are

\[
\pi(R,2R)V^3m^3
\quad\text{and}\quad
V^5m^4\frac{\log(2X)}{\log R},
\]

both absorbed into \(\pi(R,2R)V^4X^{o(1)}\) when \(m=X^{o(1)}\), using \(V\asymp X/\log X\) and \(R\asymp X^2\). This proves the claim for \(211\); reflection proves it for \(112\).

For \(121\), weighted Cauchy gives

\[
|G_{121}|^2
\le
\left(\sum_iL_i\right)
\sum_iL_i|P_i|^2|R_i|^2.
\]

Using

\[
|P_i|^2|R_i|^2
\le\frac{|P_i|^4+|R_i|^4}{2}
\]

and, for a prefix or suffix \(I\),

\[
|F_I|^4
\le
2\bigl(|F_I|^2-|I|\bigr)^2+2|I|^2,
\]

the nonprincipal character average is bounded by the prefix and suffix HWF4 terms plus the deterministic quantity

\[
\pi(R,2R)\sum_iL_i\bigl((N_i^{\mathrm L})^2+(N_i^{\mathrm R})^2\bigr).
\]

For balanced blocks,

\[
\sum_iL_i(N_i^{\mathrm L})^2
+
\sum_iL_i(N_i^{\mathrm R})^2
\ll V^3m.
\]

Multiplying by \(\sum_iL_i\ll Vm\) gives another \(O(\pi(R,2R)V^4m^2)\) contribution, which is absorbed into \(\pi(R,2R)V^4X^{o(1)}\). \(\square\)

The conclusion is deliberately one-way. HWF4 is sufficient for edge closure, and it is quantitatively comparable to the associated edge square functions up to a local correction. It has not been shown equivalent to the complete edge hybrid energies.

# 9. Additive-frequency averaging

Let \(T>2N\), and define

\[
F_{r,\chi}(\xi)
=
\sum_{j=0}^{N}\chi(Q_j)e(j\xi/T),
\qquad
\xi\bmod T.
\]

## Theorem 9.1 (uniform additive-frequency fourth moment)

One has

\[
\sum_{r\sim R}\frac1{r-1}\sum_{\chi\bmod r}
\frac1T\sum_{\xi\bmod T}|F_{r,\chi}(\xi)|^4
\ll
\pi(R,2R)V^2
+
V^4\frac{\log(2X)}{\log R}.
\]

### Proof

Expanding the fourth power and averaging over \(\xi\) imposes

\[
a+b\equiv c+d\pmod T.
\]

Since \(0\le a,b,c,d\le N\) and \(T>2N\), this is the integer equality

\[
a+b=c+d.
\]

Character orthogonality additionally imposes

\[
Q_aQ_b\equiv Q_cQ_d\pmod r.
\]

The identical unordered pairs contribute \(O(\pi(R,2R)V^2)\). For a non-identical solution, write \(h=a-c=d-b\). There are \(O(V^2)\) admissible quadruples for each \(h\), and Lemma 3.1 shows that the reduced ratio has at most \(2|h|\) uncancelled prime factors. The prime-divisor argument therefore contributes

\[
\ll
V^2\frac{\log(2X)}{\log R}
\sum_{|h|\le N}|h|
\ll
V^4\frac{\log(2X)}{\log R}.
\]

\(\square\)

This theorem uses the full uniform average over additive frequencies. It does not control the singularly weighted Fourier expression for an ordered interval sum. In particular, its zero frequency is the untwisted cumulative-walk fourth moment that remains open in HWF4.

# 10. Common-translation second differences

For lengths \(h,k\) and displacement \(\delta\), define

\[
W_t
=
\frac{U_{h,t}}{U_{k,t+\delta}}
=
Q_{t+h}Q_{t+\delta}Q_t^{-1}Q_{t+\delta+k}^{-1}.
\]

For positive shifts \(u,v\), put

\[
\Delta_u\Delta_vW_t
=
\frac{W_{t+u+v}W_t}{W_{t+u}W_{t+v}}.
\]

## Proposition 10.1 (boundary-shell shortening)

The reduced exponent support of \(\Delta_u\Delta_vW_t\) has complexity at most

\[
8\min(u,v).
\]

### Proof

For one endpoint \(x\), the second difference contributes

\[
\frac{Q_{x+u+v}Q_x}{Q_{x+u}Q_{x+v}}.
\]

If \(u\le v\), this equals

\[
\frac{U_{u,x+v}}{U_{u,x}},
\]

a ratio of two shells of length \(u\), and hence has complexity at most \(2u\). There are four endpoint contributions. The case \(v<u\) is symmetric. \(\square\)

## Proposition 10.2 (primitive four-corner system)

Let \(f\) be a nonzero finite Laurent polynomial with a unit outer coefficient. If the shifts

\[
0,\quad u,\quad v,\quad u+v
\]

are distinct, then

\[
f,\quad x^uf,\quad x^vf,\quad x^{u+v}f
\]

span a primitive rank-four lattice. Their Smith invariants are

\[
1,1,1,1.
\]

### Proof

The four monomials are distinct, so the translates are linearly independent over \(\mathbb Q\). Order the shifts and choose the columns occupied by the translated copies of a leftmost unit coefficient of \(f\). The corresponding minor is triangular with diagonal entries \(\pm1\). Thus the row lattice has rank four and is primitive. \(\square\)

In the application to \(W_t\), the exponent polynomial \(f\) vanishes exactly when the two intervals coincide, namely when \(\delta=0\) and \(h=k\). This degenerate family is excluded in what follows. For every nondegenerate choice, \(f\) has coefficients in \(\{-1,0,1\}\) and a unit outer coefficient, so Proposition 10.2 applies.

The derivative exponent row is the single linear combination

\[
(1,-1,-1,1)
\]

of the four corner rows. If the ambient group has order \(n=r-1\), the independent-step probability of satisfying all four primitive corner equations is \(n^{-4}\), whereas the derivative equation alone has probability \(n^{-1}\). Thus **a derivative-only replacement** enlarges the independent benchmark by exactly

\[
n^3=(r-1)^3.
\]

This statement does not rule out every van der Corput or signed differencing argument. It rules out the specific step of discarding the other three corner constraints and retaining only the shortened second derivative.

## Proposition 10.3 (zero-frequency obstruction to multiplier inversion)

On a periodic translation range of length \(T\), the averaged squared second-difference multiplier is

\[
\mathcal M_{U,V}(\xi)
=
\left(\frac1U\sum_{u=1}^{U}4\sin^2\frac{\pi u\xi}{T}\right)
\left(\frac1V\sum_{v=1}^{V}4\sin^2\frac{\pi v\xi}{T}\right).
\]

It satisfies

\[
\mathcal M_{U,V}(0)=0.
\]

If \(\max(U,V)=o(T)\), then

\[
\boxed{
\mathcal M_{U,V}(1)
\sim
\frac{16\pi^4}{T^4}
\frac{(U+1)(2U+1)}6
\frac{(V+1)(2V+1)}6.
}
\]

Indeed,

\[
\frac1U\sum_{u=1}^{U}4\sin^2\frac{\pi u}{T}
\sim
\frac{4\pi^2}{T^2}\frac{(U+1)(2U+1)}6.
\]

If in addition \(U,V\to\infty\), the first display simplifies to

\[
\mathcal M_{U,V}(1)
\sim
\frac{16\pi^4}{9}\frac{U^2V^2}{T^4}.
\]

Hence this multiplier cannot be inverted at zero frequency, and inversion at the first nonzero mode costs at least order \(T^4/(U^2V^2)\).

The rigorous conclusion of this section is therefore limited but exact: common translation gives genuine boundary shortening, while derivative-only replacement loses three congruence ranks and second-difference multiplier inversion loses the zero mode.

# 11. Computational verification and reproducibility

The paper's asymptotic assertions are proved symbolically. Finite enumeration is used only for the explicit template constants and for independent verification of algebraic identities. A self-contained supplementary archive contains the source code, all validator inputs, exact tables, validation outputs, a portable manifest, and a one-command verification runner.

The verification suite includes:

- the exact fourth-moment identity and transport identities of Sections 2 and 3;
- endpoint-graph ranks, Smith invariants, and the augmented-to-affine unimodular reduction;
- the offset-slice, almost-injectivity, and nearby-collision formulas;
- all endpoint templates and transport constants in Theorem 5.2;
- the complete \(70\)-template median multiplicity matrix in Proposition 5.4;
- the eight unoriented-event multiplicities and Smith minors in Theorem 5.5;
- exhaustive root-of-unity checks of Proposition 5.6 for orders \(2,3,4,5\);
- the block, edge-factorisation, and common-translation identities of Sections 7--10.

The numerical modulus panels reported in the supplement compare deterministic consecutive-prime prefixes with the exact independent-prefix laws. They are descriptive checks and are not used as proofs of HTE4 or of any asymptotic statement.

## 11.1. Data and code availability

The complete reproducibility archive - including source code, validation scripts, production data, independently written verification code, manifests, and the cold-review manuscript - is deposited in Zenodo under DOI [10.5281/zenodo.21426465](https://doi.org/10.5281/zenodo.21426465). The archive can be verified from a fresh extraction using the bundled portable validation runner.

## 11.2. AI-assistance disclosure

The research programme used large language models for structured literature triage, adversarial proof review, validator drafting, computational cross-checking, and editorial assembly. Every mathematical claim presented as a theorem is tied to an explicit proof or an independently reproducible exact computation. Open, conditional, computational, diagnostic, and negative results are labelled separately. The named author takes responsibility for the mathematical content, citations, code, and final presentation.

# 12. Remaining problems

The main open estimate is HTE4. In the exact pair-overlap decomposition, the \(k=3\) sector is negligible, while the centered \(k=0,1,2\) sectors remain open. For the disjoint sector, the immediate target is a median-dispersion estimate of the form

\[
\sum_{r\sim R}\frac1{r-1}
\sum_{\chi\ne\chi_0}\sum_m
\mathcal L_{+,m}(\chi)\mathcal R_{+,m}(\chi)
\ll
\pi(R,2R)P X^{o(1)},
\]

where \(\mathcal L_+,\mathcal R_+\) denote the largest symmetric eigenchannel of Proposition 5.4. The exact null covariance theorem suggests the required scale but does not supply an arithmetic proof.

The block decomposition also leaves the hereditary weighted moment HWF4, the four-distinct-block energy FBHE4, and the root-quartet estimate RQHE4 open. Even a proof of these internal energy estimates would not by itself furnish a prime-detection theorem: a separate signed sieve or von Mangoldt-weighted bridge would still be required.

Factorable moduli do not automatically create a reciprocal bilinear phase. For \(q=rs\), complete CRT orthogonality reparametrizes the frequency variable bijectively and leaves a centered correlation with the same support pair in both modulus factors. Any successful reciprocal approach would therefore need an incomplete transform, an additional independent variable, or a different pre-orthogonality decomposition.

# 13. Conclusion

Cumulative products of consecutive primes generate a deterministic collision problem with a substantial exact structure. Low transport, fixed-offset large-divisor incidences, average almost-injectivity, local repeated-collision geometry, and the integral rank of interval families admit unconditional treatment. For the two-run kernel, the centered energy decomposes into endpoint-overlap sectors; the three-shared-endpoint sector is negligible, and the disjoint sector reduces to four median channels with an exact independent-prefix covariance law. The individual-character spectrum is intrinsically non-Gaussian, with a fourth moment governed by ordered overlap configurations rather than Wick pairings.

These results isolate the remaining barrier sharply. The unresolved problem is not the absence of a useful decomposition, but the absence of a centered rank-two dispersion theorem strong enough to exploit cancellation across the median variable while preserving the full congruence system. No implication for Fortune's conjecture is claimed.

# References

[1] R. K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Springer, 2004.

[2] S. Tanigawa, "Matroids of Gain Graphs in Applied Discrete Geometry," *Transactions of the American Mathematical Society* **367** (2015), 8597--8641; arXiv:1207.3601.

[3] D. Funk, I. Pivotto and D. Slilaty, "Matrix representations of frame and lifted-graphic matroids correspond to gain functions," *Journal of Combinatorial Theory, Series B* **155** (2022), 202--255, doi:10.1016/j.jctb.2022.02.007.

[4] M.-C. Chang, B. Kerr and I. E. Shparlinski, "On the exponential large sieve inequality for sparse sequences modulo primes," *Journal of Mathematical Analysis and Applications* **459** (2018), 53--81; doi:10.1016/j.jmaa.2017.10.070; arXiv:1706.04776.

[5] R. C. Baker, M. Munsch and I. E. Shparlinski, "Additive energy and a large sieve inequality for sparse sequences," *Mathematika* **68** (2022), 362--399; doi:10.1112/mtk.12140; arXiv:2103.12659.

[6] K. Matomäki and J. Teräväinen, "Products of primes in arithmetic progressions," *Journal für die reine und angewandte Mathematik* **808** (2024), 193--240; doi:10.1515/crelle-2023-0096.

[7] A. J. Harper, "Simple Barban--Davenport--Halberstam type asymptotics for general sequences," *Journal of the London Mathematical Society* **112** (2025), e70293; doi:10.1112/jlms.70293.

[8] A. Pascadi, "Large sieve inequalities for exceptional Maass forms and the greatest prime factor of \(n^2+1\)," *Forum of Mathematics, Pi* **14** (2026), e8; arXiv:2404.04239.

[9] S. Bettin and V. Chandee, "Trilinear forms with Kloosterman fractions," *Advances in Mathematics* **328** (2018), 1234--1262; arXiv:1502.00769.

[10] S. Drappeau, "Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method," *Proceedings of the London Mathematical Society* **114** (2017), 684--732; arXiv:1504.05549.
