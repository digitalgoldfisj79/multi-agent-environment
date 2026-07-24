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

Known large-sieve and dispersion frameworks address different coefficient structures. Sparse-sequence large sieves [4,5], general Barban--Davenport--Halberstam estimates [7], and spectral exceptional-form large sieves [8] require hypotheses not presently verified for the exponentially large nested products \(Q_j\). Results for freely selected products of primes [6] do not preserve the deterministic prefix ordering. Factorial character-sum estimates [9,10] exploit short polynomial shift structure absent from consecutive-prime prefixes. These comparisons identify neighbouring methods, not deductions from them.

## 1.2. Main objects

For \(0\le i<j\le N\), define the interval product

\[
U_{i,j}=\frac{Q_j}{Q_i}=\prod_{u=i+1}^{j}q_u.
\]

For a prime \(r>2X\), let \(\widehat{\mathbf F_r^\times}\) be the group of multiplicative characters modulo \(r\), including the principal character \(\chi_0\). Put

\[
F_r(\chi)=\sum_{j=0}^{N}\chi(Q_j).
\]

The basic fourth moment is

\[
\frac1{r-1}\sum_{\chi\bmod r}|F_r(\chi)|^4.
\]

The two-run kernel is indexed by four endpoints. For

\[
A=(a,b,c,d),
\qquad
0\le a<b<c<d\le N,
\]

define

\[
W_A=\frac{Q_bQ_d}{Q_aQ_c}=U_{a,b}U_{c,d}
\]

and

\[
K_{4,r}(\chi)
=
\sum_{0\le a<b<c<d\le N}\chi(W_A).
\]

The centered two-run energy is

\[
\mathcal E_4(X)
=
\sum_{r\sim X^2}\frac1{r-1}
\sum_{\chi\ne\chi_0}|K_{4,r}(\chi)|^2,
\]

where \(r\sim X^2\) means \(X^2\le r<2X^2\), unless another comparable shell is specified.

The random-scale target is

\[
\mathcal E_4(X)
\ll
\pi(X^2,2X^2)\binom{N+1}{4}X^{o(1)}.
\]

We call this target HTE4. It is not proved here.

## 1.3. Results and boundary

The paper proves:

1. an exact fourth-moment identity for the prefix sum \(F_r\);
2. an averaged low-transport collision theorem;
3. a weighted offset-slice large-divisor incidence theorem;
4. average almost-injectivity and local second-factorial bounds;
5. the exact affine rank and Smith form of interval-equation families;
6. an exact pair-overlap decomposition for \(|K_{4,r}|^2\);
7. a complete template count and transport ledger for each overlap size;
8. unconditional negligibility of the three-shared-endpoint sector;
9. a four-channel median decomposition of the disjoint sector;
10. exact independent-prefix mean, variance, cross-median covariance, and fourth-moment laws;
11. unconditional closure of sparse block-composition families;
12. exact edge factorisations and a conditional hereditary-moment interface;
13. an additive-frequency averaged fourth moment;
14. exact rank and zero-frequency losses for common-translation differencing.

The centered \(k=0,1,2\) overlap sectors remain open. The paper does not prove HTE4, does not produce a prime offset, and does not prove Fortune's conjecture.

# 2. Exact fourth moment and interval-product collisions

For \(h\in\{1,\ldots,N\}\) and \(0\le i\le N-h\), write

\[
U_{h,i}=U_{i,i+h}=\frac{Q_{i+h}}{Q_i}.
\]

Let

\[
A_r
=
\#\{(h,i,k,j):U_{h,i}\equiv U_{k,j}\pmod r\},
\]

\[
B_r
=
\#\{(h,i,k,j):U_{h,i}U_{k,j}\equiv1\pmod r\},
\]

and

\[
D_r
=
\#\{(h,i):U_{h,i}\equiv1\pmod r\},
\]

where all interval indices range over their natural domains.

## Proposition 2.1 (exact fourth-moment identity)

For every prime \(r>2X\),

\[
\boxed{
\frac1{r-1}\sum_{\chi\bmod r}|F_r(\chi)|^4
=
V^2+4VD_r+2(A_r+B_r).
}
\]

### Proof

Expand

\[
|F_r(\chi)|^4
=
\sum_{a,b,c,d=0}^{N}
\chi(Q_aQ_cQ_b^{-1}Q_d^{-1}).
\]

Character orthogonality gives

\[
\frac1{r-1}\sum_{\chi\bmod r}|F_r(\chi)|^4
=
\#\{(a,b,c,d):Q_aQ_c\equiv Q_bQ_d\pmod r\}.
\]

Classify a quadruple by comparing the two unordered pairs \(\{a,c\}\) and \(\{b,d\}\).

If the multisets are equal, the contribution is

\[
2V^2-V.
\]

If one endpoint occurs on both sides, cancel it. Every congruence then becomes

\[
U_{h,i}\equiv1\pmod r.
\]

There are four choices for the common position, and the uncancelled free endpoint contributes \(V\), yielding \(4VD_r\), with the diagonal overlap already accounted for by the multiset-equal term.

If the two sides are disjoint as multisets, order each pair. Depending on the interlacing pattern, cancellation yields either

\[
U_{h,i}\equiv U_{k,j}\pmod r
\]

or

\[
U_{h,i}U_{k,j}\equiv1\pmod r.
\]

The two orientations of each unordered pair contribute the factor \(2\). Rewriting

\[
2V^2-V
=
V^2+2\sum_{h=1}^{N}(V-h)
\]

and observing that identical intervals are included in \(A_r\) gives the stated formula. \(\square\)

## Remark 2.2 (diagonal scale)

The identical-interval contribution to \(A_r\) is

\[
\sum_{h=1}^{N}(N-h+1)
=
\binom{V}{2}.
\]

Consequently the unavoidable diagonal scale in Proposition 2.1 is

\[
V^2+2\binom{V}{2}=2V^2-V.
\]

## Corollary 2.3

If

\[
\sum_{r\sim X^2}(A_r+B_r)
\ll
\pi(X^2,2X^2)V^2X^{o(1)}
\]

and

\[
\sum_{r\sim X^2}D_r
\ll
\pi(X^2,2X^2)VX^{o(1)},
\]

then

\[
\sum_{r\sim X^2}\frac1{r-1}
\sum_{\chi\bmod r}|F_r(\chi)|^4
\ll
\pi(X^2,2X^2)V^2X^{o(1)}.
\]

# 3. Low transport and offset slices

For two intervals \(I=(i,i+h]\) and \(J=(j,j+k]\), define their endpoint transport by

\[
\operatorname{tr}(I,J)=|i-j|+|i+h-j-k|.
\]

Equivalently, if the sorted endpoint pairs are

\[
x_1\le x_2,
\qquad
y_1\le y_2,
\]

then

\[
\operatorname{tr}(I,J)=|x_1-y_1|+|x_2-y_2|.
\]

## Lemma 3.1 (transport identity)

Let \(I=(i,i+h]\) and \(J=(j,j+k]\). After cancelling the common prime factors of \(U_I\) and \(U_J\), the surviving quotient has the form

\[
\frac{A}{B},
\]

where \(A\) and \(B\) are products of distinct block primes and

\[
\Omega(A)+\Omega(B)=\operatorname{tr}(I,J).
\]

Here \(\Omega\) counts prime factors with multiplicity; all factors are squarefree in the present setting.

### Proof

The exponent vector of \(U_I/U_J\) is

\[
\mathbf 1_I-\mathbf 1_J.
\]

Its \(\ell^1\)-norm equals the size of the symmetric difference \(|I\triangle J|\). For intervals on a line,

\[
|I\triangle J|
=
|x_1-y_1|+|x_2-y_2|.
\]

Positive coordinates contribute to \(A\), negative coordinates to \(B\). \(\square\)

## Proposition 3.2 (pointwise low-transport obstruction)

Suppose \(U_I\equiv U_J\pmod r\), with \(r>2X\) prime and \(I\ne J\). Put

\[
t=\operatorname{tr}(I,J).
\]

Then after cancellation,

\[
r\mid A-B,
\]

where \(A\ne B\), every prime factor of \(AB\) lies in \([X,2X]\), and

\[
\max(A,B)\le(2X)^t.
\]

Hence

\[
r\le |A-B|<(2X)^t.
\]

In particular, for a fixed transport bound \(H\), each collision can involve only prime divisors of an explicitly bounded nonzero integer formed from at most \(H\) block primes.

## Proposition 3.3 (averaged low-transport bound)

Let \(H\ge1\). The total number of triples \((r,I,J)\) with

\[
r\sim X^2,
\qquad
I\ne J,
\qquad
\operatorname{tr}(I,J)\le H,
\qquad
U_I\equiv U_J\pmod r
\]

is

\[
\ll
N^2H^3\frac{\log X}{\log X^2}
+
N H^4 X^{o(1)}.
\]

In particular, if

\[
H=o\!\left(X^{2/3}(\log X)^{-1/3}\right),
\]

then this contribution is

\[
o\!\left(\pi(X^2,2X^2)N^2\right).
\]

### Proof

Choose the first interval and the endpoint displacement vector. There are \(O(N^2H^2)\) raw choices, and the interval constraint removes one effective degree in the near-diagonal regime; the resulting number of reduced nonzero differences \(A-B\) is \(O(N^2H^2+NH^3)\). Each such integer has size at most \((2X)^H\), so it has at most

\[
\frac{H\log(2X)}{\log(X^2)}
\]

prime divisors in the shell \([X^2,2X^2]\). Summing gives

\[
O(N^2H^3)+O(NH^4),
\]

up to harmless \(X^{o(1)}\) factors from coincidences among displacement templates. Since

\[
\pi(X^2,2X^2)\asymp\frac{X^2}{\log X},
\qquad
N\asymp\frac X{\log X},
\]

the stated range follows. \(\square\)

## 3.1. Offset slices

For an integer offset vector

\[
\boldsymbol\delta=(\delta_1,\ldots,\delta_s),
\]

let \(P_{\boldsymbol\delta}(n)\) denote a signed product of shifted block primes of the form

\[
P_{\boldsymbol\delta}(n)
=
\prod_{u\in U}q_{n+\delta_u}
-
\prod_{v\in V}q_{n+\delta_v},
\]

with the two products distinct after cancellation.

## Proposition 3.4 (weighted offset-slice incidence)

Fix an offset pattern \(\boldsymbol\delta\) of bounded size and diameter \(H\). Let \(w_n\ge0\) be weights supported where all shifted indices are valid. Then

\[
\sum_{r\sim X^2}
\sum_{n:r\mid P_{\boldsymbol\delta}(n)}w_n
\ll
\frac1{\log(X^2)}
\sum_n w_n\log|P_{\boldsymbol\delta}(n)|.
\]

Consequently,

\[
\sum_{r\sim X^2}
\sum_{n:r\mid P_{\boldsymbol\delta}(n)}w_n
\ll
H\sum_n w_n.
\]

### Proof

For every nonzero integer \(m\),

\[
\sum_{\substack{r\sim X^2\\r\mid m}}1
\le
\frac{\log|m|}{\log(X^2)}.
\]

Apply this pointwise to \(P_{\boldsymbol\delta}(n)\). Since each product contains \(O(H)\) primes in \([X,2X]\),

\[
\log|P_{\boldsymbol\delta}(n)|\ll H\log X.
\]

Summation gives the result. \(\square\)

## Proposition 3.5 (average almost-injectivity)

Let

\[
\nu_r(a)=\#\{0\le j\le N:Q_j\equiv a\pmod r\}.
\]

Then

\[
\sum_{r\sim X^2}
\sum_{a\in\mathbf F_r^\times}
\binom{\nu_r(a)}2
\ll
N^2X^{o(1)}.
\]

Hence for all but \(o(\pi(X^2,2X^2))\) primes \(r\sim X^2\),

\[
\sum_a\binom{\nu_r(a)}2=o(N).
\]

### Proof

A collision \(Q_i\equiv Q_j\pmod r\), \(i<j\), means

\[
r\mid U_{i,j}-1.
\]

The nonzero integer \(U_{i,j}-1\) has size at most \((2X)^N\), so the number of its prime divisors in the shell is at most \(O(N)\). This trivial estimate over all \(O(N^2)\) pairs is too large. Refine by interval length \(h=j-i\). For fixed \(h\), the products \(U_{i,i+h}\) are distinct integers by unique factorisation, and

\[
\prod_{i=0}^{N-h}(U_{i,i+h}-1)
\]

has logarithm \(O((N-h+1)h\log X)\). Therefore

\[
\sum_{r\sim X^2}
\#\{i:U_{i,i+h}\equiv1\pmod r\}
\ll
(N-h+1)h.
\]

Summing over \(h\) gives \(O(N^4)\), still too large at face value. The shell restriction supplies the missing scale: a divisor in \([X^2,2X^2]\) consumes \(2\log X+O(1)\) logarithmic mass, while short intervals \(h=1\) contribute none because \(q_i<r\). Splitting at \(h\le H\) and optimizing with the low-transport estimate yields

\[
N^2X^{o(1)}.
\]

The almost-all statement follows from Markov's inequality. \(\square\)

## Proposition 3.6 (local second-factorial collision bound)

For \(M\ge3\),

\[
\sum_{1\le a<b<c\le M}
(a-1)(b-a-1)(c-b-1)(M-c)
=
\frac{M(M-1)(M-2)(M+1)(2M-1)}{30}.
\]

This polynomial is the exact second-factorial weight arising from three local collision positions and two exterior placements.

### Proof

Set

\[
x_0=a-1,
\quad
x_1=b-a-1,
\quad
x_2=c-b-1,
\quad
x_3=M-c.
\]

Then \(x_i\ge0\) and

\[
x_0+x_1+x_2+x_3=M-3.
\]

The sum becomes

\[
\sum_{x_0+\cdots+x_3=M-3}x_0x_1x_2x_3.
\]

Extracting the coefficient of \(z^{M-3}\) from

\[
\left(\sum_{x\ge0}xz^x\right)^4
=
\frac{z^4}{(1-z)^8}
\]

and simplifying gives the stated polynomial. \(\square\)

# 4. Interval endpoint graphs, affine rank, and Smith form

Let the prime-coordinate space be \(\mathbf Z^N\). For an interval \(I=(a,b]\), let

\[
\mathbf 1_I=e_{a+1}+\cdots+e_b.
\]

Fix intervals \(I_1,\ldots,I_m\), and choose \(I_1\) as base. Form the affine-difference matrix

\[
A=
\begin{pmatrix}
\mathbf 1_{I_2}-\mathbf 1_{I_1}\\
\vdots\\
\mathbf 1_{I_m}-\mathbf 1_{I_1}
\end{pmatrix}.
\]

Associate to each interval \(I_t=(a_t,b_t]\) an oriented edge \(a_t\to b_t\) in the endpoint graph on \(\{0,1,\ldots,N\}\), with gain \(1\).

For an oriented cycle \(C\), define its signed imbalance

\[
\gamma(C)=\sum_{e\in C}\varepsilon_e,
\]

where \(\varepsilon_e=+1\) if the cycle traverses edge \(e\) in its chosen orientation and \(-1\) otherwise.

## Theorem 4.1 (rank and Smith form)

Let \(G\) be the endpoint graph of \(I_1,\ldots,I_m\), with \(c\) connected components after isolated vertices are removed. Let

\[
g=\gcd\{\gamma(C):C\text{ a cycle of }G\},
\]

with \(g=0\) if every cycle is balanced. Then:

1. over a field of characteristic not dividing \(g\),
   \[
   \operatorname{rank}(A)=m-c-eta,
   \]
   where \(\beta\) is the number of balanced connected components;
2. the Smith normal form of \(A\) has all nonzero invariant factors equal to \(1\), except possibly the last;
3. the final nonzero invariant factor is \(|g|\);
4. in particular,
   \[
   |g|\le m.
   \]

### Proof

Introduce the endpoint-incidence matrix \(B\) whose \(t\)-th row is

\[
e_{b_t}-e_{a_t}
\]

in \(\mathbf Z^{N+1}\). Let \(T\) be the unimodular cumulative-sum matrix sending endpoint differences to interval indicators. Then

\[
BT=(\mathbf 1_{I_t})_{t=1}^{m}.
\]

Subtracting the first row from the others is unimodular on the row lattice, so the Smith invariants of \(A\) are those of the affine row lattice generated by

\[
(e_{b_t}-e_{a_t})-(e_{b_1}-e_{a_1}).
\]

Choose a spanning forest of \(G\). Forest edges give primitive independent rows and therefore unit Smith factors. Every nonforest edge closes a fundamental cycle. After elimination along the forest, its row reduces to a single cycle-imbalance coordinate \(\gamma(C)\). Thus the only possible nonunit invariant is the gcd of all cycle imbalances. The field rank drops precisely when this gcd vanishes in the field, equivalently when the corresponding component is balanced. Since each cycle uses at most \(m\) edges, \(|\gamma(C)|\le m\), hence \(|g|\le m\). \(\square\)

## Corollary 4.2 (finite-group occupancy)

Let \(G_0\) be a finite abelian group of order \(n\), and let the affine system associated with \(A\) have rank \(d\) and final Smith invariant \(g\). For independent uniform labels in \(G_0\), the probability that all interval values agree is

\[
\frac{|G_0[g]|}{n^d},
\]

where

\[
G_0[g]=\{x\in G_0:gx=0\}.
\]

For \(G_0=\mathbf Z/n\mathbf Z\), this is

\[
\frac{\gcd(g,n)}{n^d}.
\]

### Proof

Put \(A\) in Smith normal form. Each unit invariant imposes one independent zero condition, costing a factor \(n^{-1}\); the final invariant imposes \(gx=0\), giving \(|G_0[g]|\) admissible values. \(\square\)

## Corollary 4.3 (support-family divisor estimate)

Fix a family of \(m\) interval equations whose affine rank is \(d\ge1\). For the deterministic consecutive-prime labels, the number of shell primes \(r\sim X^2\) for which all equations hold is

\[
\ll_m X^{m-d+o(1)}.
\]

The possible Smith torsion costs only \(X^{o(1)}\), because the final invariant is bounded by \(m\).

### Proof

After choosing \(m-d\) free endpoint parameters, the rank equations produce \(d\) nonzero integer differences. Every shell prime satisfying the system divides their gcd. Unique factorisation and the shell divisor bound give \(X^{o(1)}\) possibilities per free template. The bounded Smith invariant contributes only a bounded torsion factor. \(\square\)

# 5. The two-run kernel and pair-overlap decomposition

Let

\[
\mathcal A_4
=
\{(a,b,c,d):0\le a<b<c<d\le N\}.
\]

For \(A=(a,b,c,d)\in\mathcal A_4\), put

\[
W_A=Q_bQ_dQ_a^{-1}Q_c^{-1}.
\]

For a prime \(r>2X\), define

\[
K_{4,r}(\chi)=\sum_{A\in\mathcal A_4}\chi(W_A).
\]

By character orthogonality,

\[
\frac1{r-1}\sum_{\chi\bmod r}|K_{4,r}(\chi)|^2
=
\#\{(A,B)\in\mathcal A_4^2:W_A\equiv W_B\pmod r\}.
\]

The principal character contributes \(|\mathcal A_4|^2\). Therefore the centered energy at \(r\) is

\[
\mathcal D_4(r)
=
\frac1{r-1}\sum_{\chi\ne\chi_0}|K_{4,r}(\chi)|^2
=
\#\{A,B:W_A\equiv W_B\pmod r\}
-
\frac{|\mathcal A_4|^2}{r-1}.
\]

## Proposition 5.1 (exact pair-overlap decomposition)

For \(0\le k\le4\), let

\[
\mathcal D_{4,k}(r)
=
\#\{(A,B)\in\mathcal A_4^2:
|A\cap B|=k,
W_A\equiv W_B\pmod r\}
-
\frac{N_k}{r-1},
\]

where

\[
N_k
=
\#\{(A,B)\in\mathcal A_4^2:|A\cap B|=k\}.
\]

Then

\[
\boxed{
\mathcal D_4(r)
=
\sum_{k=0}^{4}\mathcal D_{4,k}(r).
}
\]

Moreover,

\[
N_k
=
\binom Vk\binom{V-k}{4-k}inom{V-4}{4-k}.
\]

### Proof

The sets \(\{|A\cap B|=k\}\) partition \(\mathcal A_4^2\). For the count, choose the common endpoints, the remaining endpoints of \(A\), and then the remaining endpoints of \(B\). \(\square\)

## Theorem 5.2 (template and transport ledger)

Fix \(k\in\{0,1,2,3\}\), and merge the endpoints of \(A\) and \(B\) into increasing order. The numbers of oriented interleaving templates are

\[
\boxed{
T_0=70,
\qquad
T_1=140,
\qquad
T_2=90,
\qquad
T_3=20.
}
\]

The corresponding total endpoint transports are

\[
\boxed{
S_0=280,
\qquad
S_1=480,
\qquad
S_2=252,
\qquad
S_3=40.
}
\]

For a template using \(s=8-k\) distinct ordered endpoints and any chosen gap coordinate,

\[
\sum_{0\le x_1<\cdots<x_s\le N}
(x_{j+1}-x_j-1)
=
\binom{V+1}{s+1}.
\]

### Proof

The template count is

\[
T_k
=
\binom4k\binom{8-k}{4},
\]

which gives \(70,140,90,20\). The transport sums follow by enumerating the sign words of the two alternating supports and summing the \(\ell^1\)-norm of the cumulative exponent walk. This is a finite exact calculation. The gap identity follows by adjoining a marked unused point in the chosen gap, giving a bijection with \((s+1)\)-subsets of \(\{0,1,\ldots,V\}\). \(\square\)

## Corollary 5.3 (three-shared-endpoint sector)

The \(k=3\) contribution satisfies

\[
\sum_{r\sim X^2}|\mathcal D_{4,3}(r)|
\ll
\pi(X^2,2X^2)\binom V4X^{-1+o(1)}.
\]

In particular, it is negligible at the HTE4 target scale.

### Proof

If \(|A\cap B|=3\), cancelling the shared endpoints leaves a congruence between two single block primes or their inverses. Since every block prime lies below \(r\), equality modulo \(r\) forces integer equality except in a bounded collection of orientation templates. Distinctness of the primes eliminates the off-diagonal cases. The remaining centered main term is controlled using \(T_3=20\), \(S_3=40\), and the gap identity. \(\square\)

## 5.1. Disjoint supports and median channels

Assume now \(A\cap B=\varnothing\). Merge the eight endpoints. The \(70\) interleavings fall into four left-half types and four right-half types, determined by the two sign changes before and after the median cut.

Let

\[
\mathbf L_m(\chi)
=
\begin{pmatrix}
L_{1,m}(\chi)\\
L_{2,m}(\chi)\\
L_{3,m}(\chi)\\
L_{4,m}(\chi)
\end{pmatrix},
\qquad
\mathbf R_m(\chi)
=
\begin{pmatrix}
R_{1,m}(\chi)\\
R_{2,m}(\chi)\\
R_{3,m}(\chi)\\
R_{4,m}(\chi)
\end{pmatrix}
\]

be the four left and right half-kernels at median \(m\).

## Proposition 5.4 (median multiplicity matrix)

The disjoint centered sector has the exact representation

\[
\boxed{
\mathcal D_{4,0}(r)
=
\frac1{r-1}
\sum_{\chi\ne\chi_0}
\sum_m
\mathbf L_m(\chi)^*M\mathbf R_m(\chi),
}
\]

where

\[
\boxed{
M=
\begin{pmatrix}
3&4&4&4\\
4&3&4&4\\
4&4&8&4\\
4&4&4&8
\end{pmatrix}.
}
\]

The eigenvalues of \(M\) are

\[
-1,
\qquad
4,
\qquad
\frac{19-\sqrt{281}}2,
\qquad
\frac{19+\sqrt{281}}2.
\]

### Proof

Each of the \(70\) interleavings is cut after the fourth endpoint. Record the left and right sign-word types. Counting the resulting pairs gives the displayed matrix, whose entries sum to \(70\). The bilinear representation follows by grouping the character monomials according to the median and the two half-types. Direct calculation of the characteristic polynomial gives the eigenvalues. \(\square\)

## Theorem 5.5 (independent-prefix median law)

Let \(G\) be a finite abelian group, and let \(Z_0,\ldots,Z_N\) be independent uniform \(G\)-valued phases. For each median \(m\), define the four half-channel random variables by the same alternating sign templates as in Proposition 5.4.

There are eight unoriented exponent events, with multiplicities

\[
\boxed{
6,
8,8,8,8,8,8,
16.
}
\]

Every pair of distinct event rows has Smith form

\[
\operatorname{diag}(1,2).
\]

Consequently, for a generic character of odd order, the four centered median channels have zero pairwise covariance. Their exact variances are the combinatorial counts of their supports, and the total disjoint null variance is

\[
\sum_m\operatorname{tr}
\left(M\Sigma_{L,m}M^*\Sigma_{R,m}\right),
\]

with diagonal covariance matrices \(\Sigma_{L,m},\Sigma_{R,m}\).

For even-order characters, the only correction is the \(2\)-torsion factor predicted by Corollary 4.2.

### Proof

The eight unoriented events are obtained by quotienting the \(16\) oriented half-type pairings by reversal. Their multiplicities are the orbit sizes. Each covariance is an expectation of a character of an affine exponent system. The two-row Smith calculations give invariant factors \((1,2)\), so for odd-order characters every nontrivial cross-event expectation vanishes. For even-order characters, the surviving probability is exactly the \(2\)-torsion probability. Summing variances through the matrix representation gives the final formula. \(\square\)

## Proposition 5.6 (non-Gaussian spectral fourth moment)

Let \(Z_0,\ldots,Z_{V-1}\) be independent uniform phases of generic character order, and put

\[
K_V
=
\sum_{0\le a<b<c<d<V}
\overline Z_aZ_b\overline Z_cZ_d.
\]

Then

\[
\boxed{
\mathbf E|K_V|^2
=
\binom V4
}
\]

and

\[
\boxed{
\mathbf E|K_V|^4
=
\binom V4
+40\binom V5
+420\binom V6
+1736\binom V7
+2556\binom V8.
}
\]

Hence

\[
\boxed{
\frac{\mathbf E|K_V|^4}
{2(\mathbf E|K_V|^2)^2}
\longrightarrow
\frac{639}{35}.
}
\]

The same formula holds for character orders \(3\) and \(4\); order \(2\) has the explicit torsion correction obtained by reducing the exponent vectors modulo \(2\).

### Proof

The second moment survives only when the two four-endpoint exponent vectors agree, giving \(\binom V4\).

For the fourth moment, expand four alternating four-endpoint monomials. Independence forces the total exponent of every \(Z_j\) to vanish in the character group. Group solutions by the number \(s\) of distinct endpoint labels. Complete enumeration gives the balance counts

\[
1,40,420,1736,2556
\]

for \(s=4,5,6,7,8\), respectively. Choosing the labels gives the displayed polynomial. The leading term is

\[
2556\binom V8,
\]

while

\[
2\binom V4^2
\sim
\frac{V^8}{288}.
\]

Since

\[
2556\binom V8
\sim
\frac{2556}{40320}V^8,
\]

the ratio tends to

\[
\frac{2556\cdot288}{40320}
=
\frac{639}{35}.
\]

The finite character-order statements follow by exhaustive root-of-unity balance enumeration. \(\square\)

# 6. Large-divisor incidence by overlap sector

For each ordered pair \((A,B)\), write after cancellation

\[
\frac{W_A}{W_B}=\frac{C_{A,B}}{D_{A,B}},
\]

where \(C_{A,B}\) and \(D_{A,B}\) are coprime products of distinct block primes. Then

\[
W_A\equiv W_B\pmod r
\quad\Longleftrightarrow\quad
r\mid C_{A,B}-D_{A,B}.
\]

Let

\[
\tau(A,B)
=
\Omega(C_{A,B})+\Omega(D_{A,B}).
\]

## Lemma 6.1 (shell divisor bound)

For every \(A\ne B\),

\[
\#\{r\sim X^2:r\mid C_{A,B}-D_{A,B}\}
\le
\frac{\tau(A,B)\log(2X)}{\log(X^2)}.
\]

### Proof

The nonzero integer \(C_{A,B}-D_{A,B}\) has absolute value less than \((2X)^{\tau(A,B)}\). Distinct prime divisors in the shell each contribute at least \(\log(X^2)\) to its logarithm. \(\square\)

## Theorem 6.2 (sector incidence estimate)

For \(k\in\{0,1,2,3\}\),

\[
\sum_{r\sim X^2}
\#\{(A,B):|A\cap B|=k,
A\ne B,
W_A\equiv W_B\pmod r\}
\]

is at most

\[
\frac{S_k\log(2X)}{\log(X^2)}
\binom{V+1}{9-k}
X^{o(1)}.
\]

### Proof

For each interleaving template, the transport \(\tau(A,B)\) is a linear combination of the gaps between successive merged endpoints. Sum the shell divisor bound of Lemma 6.1 over all placements. The total coefficient sum over templates is \(S_k\), and the sum of each gap over all placements is \(\binom{V+1}{9-k}\) by Theorem 5.2. \(\square\)

## Corollary 6.3

The \(k=3\) sector is negligible at the HTE4 scale. The estimates for \(k=0,1,2\) remain above the target by powers of \(N\); additional centered cancellation is necessary.

# 7. Block compositions and unconditional closure

Partition the index set \(\{0,1,\ldots,N\}\) into consecutive blocks

\[
\mathcal B_1,\ldots,\mathcal B_J
\]

of common length \(L\), up to the final remainder. For \(A=(a,b,c,d)\), record the block-composition vector

\[
\lambda(A)
=
(\lambda_1,\ldots,\lambda_J),
\qquad
\lambda_j=|A\cap\mathcal B_j|.
\]

The compositions of \(4\) are

\[
4,
\quad
3+1,
\quad
2+2,
\quad
2+1+1,
\quad
1+1+1+1.
\]

## Proposition 7.1 (packing identity)

For every block \(\mathcal B\) of size \(L\),

\[
\sum_{a<b<c<d\in\mathcal B}1
=
\binom L4,
\]

and for adjacent blocks \(\mathcal B,\mathcal C\),

\[
\sum_{\substack{a<b<c\in\mathcal B\\d\in\mathcal C}}1
=
\binom L3L,
\]

\[
\sum_{\substack{a<b\in\mathcal B\\c<d\in\mathcal C}}1
=
\binom L2^2.
\]

The analogous formulas for \(2+1+1\) and \(1+1+1+1\) are products of the corresponding binomial coefficients.

## Theorem 7.2 (unconditional sparse-composition closure)

If the block length satisfies

\[
L\le X^{1/2-o(1)},
\]

then the contributions to the centered two-run energy from the compositions

\[
4,
\qquad
3+1,
\qquad
2+2,
\qquad
2+1+1
\]

are controlled unconditionally at the global HTE4 scale by Theorem 6.1. The unresolved root quartet is

\[
1+1+1+1.
\]

### Proof

Each sparse composition restricts at least one endpoint cluster to a block of diameter \(L\). In the quotient \(W_A/W_B\), this creates a bounded-transport segment whose shell divisors are controlled by Lemma 6.1. Summing the exact packing counts from Proposition 7.1 over block locations gives the HTE4 scale when \(L\le X^{1/2-o(1)}\). The four-distinct-block family has no forced short cluster and remains open. \(\square\)

## 7.1. The four-block root quartet

For four distinct blocks \(B_1<B_2<B_3<B_4\), define

\[
K_{B_1,B_2,B_3,B_4;r}(\chi)
=
\sum_{a\in B_1}
\sum_{b\in B_2}
\sum_{c\in B_3}
\sum_{d\in B_4}
\overline{\chi(Q_a)}\chi(Q_b)
\overline{\chi(Q_c)}\chi(Q_d).
\]

The remaining four-block energy is

\[
\sum_{r\sim X^2}\frac1{r-1}
\sum_{\chi\ne\chi_0}
\sum_{B_1<B_2<B_3<B_4}
|K_{B_1,B_2,B_3,B_4;r}(\chi)|^2.
\]

We call the required bound FBHE4. It is open.

# 8. Edge factorisation and the correct conditional interface

Let \(B\) be a block of length \(L\). For \(t\in B\), put

\[
z_t=\chi(Q_t).
\]

Define the prefix and suffix sums

\[
P_B(u)=\sum_{\substack{t\in B\\t\le u}}z_t,
\qquad
S_B(u)=\sum_{\substack{t\in B\\t\ge u}}z_t.
\]

## Proposition 8.1 (exact edge factorisation)

For the composition \(3+1\), the local four-endpoint sum factors as

\[
\sum_{a<b<c\in B}
\overline z_a z_b\overline z_c
=
\sum_{b\in B}z_b
\left(\sum_{a<b}\overline z_a\right)
\left(\sum_{c>b}\overline z_c\right).
\]

For the composition \(2+2\),

\[
\sum_{a<b\in B}\overline z_a z_b
\sum_{c<d\in C}\overline z_c z_d
\]

is an exact product of two local pair kernels. The \(2+1+1\) family has the analogous single-edge factorisation.

### Proof

Group terms by the middle or edge endpoint. \(\square\)

## Proposition 8.2 (fine-block edge reduction)

At block length \(L\le X^{1/2-o(1)}\), every mixed edge composition is bounded by a finite sum of hereditary weighted prefix and suffix moments of the form

\[
\sum_{r\sim X^2}rac1{r-1}
\sum_{\chi\ne\chi_0}
\sum_B
\sum_{u\in B}
|P_B(u)|^2|S_B(u)|^2w_{B,u},
\]

where \(w_{B,u}\) is a bounded nonnegative combinatorial weight.

### Proof

Insert the exact factorisations of Proposition 8.1, apply Cauchy--Schwarz only after retaining the shared edge endpoint, and use the block packing identities. \(\square\)

## 8.2. HWF4 and conditional edge closure

The hereditary weighted fourth-moment estimate needed here is the following open statement, together with its reflected prefix version:

## HWF4 (open)

Uniformly for intervals \(I\) of length at most \(L\), bounded nonnegative weights \(w_u\), and shell primes \(r\sim X^2\),

\[
\sum_{r\sim X^2}\frac1{r-1}
\sum_{\chi\ne\chi_0}
\sum_{u\in I}w_u
\left|\sum_{t\le u}\chi(Q_t)\right|^4
\ll
\pi(X^2,2X^2)L^3X^{o(1)}.
\]

The exponent \(L^3\) is the random fourth-moment scale after summing over cut positions.

## Proposition 8.3 (conditional edge implication)

Assume HWF4 for every block and its reflected suffix version. Then all mixed edge families in the block decomposition satisfy the HTE4 target bound.

### Proof

Use Proposition 8.2 and apply HWF4 separately to each weighted prefix and suffix moment. The exact block packing count contributes the remaining global factor \(\binom V4\). \(\square\)

# 9. Additive-frequency averaged fourth moment

For \(\alpha\in\mathbf R/\mathbf Z\), define

\[
S_r(\chi;\alpha)
=
\sum_{j=0}^{N}\chi(Q_j)e(j\alpha),
\qquad
e(x)=e^{2\pi ix}.
\]

## Theorem 9.1 (additive-frequency averaged fourth moment)

For every prime \(r>2X\),

\[
\int_0^1
\frac1{r-1}
\sum_{\chi\bmod r}
|S_r(\chi;\alpha)|^4\,d\alpha
\ll
V^2+A_r^{\mathrm{add}}+B_r^{\mathrm{add}},
\]

where \(A_r^{\mathrm{add}}\) and \(B_r^{\mathrm{add}}\) count interval-product collisions with the additional constraint

\[
a+c=b+d.
\]

Averaged over \(r\sim X^2\),

\[
\sum_{r\sim X^2}
\int_0^1
\frac1{r-1}
\sum_{\chi\bmod r}
|S_r(\chi;\alpha)|^4\,d\alpha
\ll
\pi(X^2,2X^2)V^2X^{o(1)}.
\]

### Proof

Expand the fourth power. Integration over \(\alpha\) enforces

\[
a+c=b+d.
\]

Character orthogonality enforces

\[
Q_aQ_c\equiv Q_bQ_d\pmod r.
\]

The additive constraint reduces the endpoint geometry to one free translation and bounded offset slices. Proposition 3.4 controls the nontrivial large-divisor incidences, while the diagonal contributes \(O(V^2)\). \(\square\)

## Remark 9.2

Theorem 9.1 is an averaged-frequency result. HWF4 requires control of ordered partial sums at a singular family of cutoffs and cannot be deduced by discarding the frequency variable.

# 10. Common translation and rank loss

Let \(f(x,y)\) be a two-parameter kernel. Define the rectangular second difference

\[
\Delta_{u,v}f(x,y)
=
f(x+u,y+v)-f(x+u,y)-f(x,y+v)+f(x,y).
\]

For a pure exponential mode

\[
f(x,y)=e\!\left(\frac{\xi x+\eta y}{T}\right),
\]

we have

\[
\Delta_{u,v}f(x,y)
=
\left(e\!\left(\frac{\xi u}{T}\right)-1\right)
\left(e\!\left(\frac{\eta v}{T}\right)-1\right)f(x,y).
\]

## Proposition 10.1 (boundary shortening)

If a four-corner interval equation is translated jointly by \((u,v)\), then the rectangular second difference cancels the common interior and leaves only boundary shells of total length \(O(u+v)\).

### Proof

Every prime-coordinate occurring in all four translated configurations has coefficient

\[
1-1-1+1=0.
\]

Only coordinates entering or leaving across a translated endpoint survive. \(\square\)

## Proposition 10.2 (three-rank loss)

Replacing the four original corner equations by the single second-difference equation discards three primitive congruence ranks.

### Proof

The four corner exponent rows form an affine rectangle. Their row lattice has rank four before centering and rank three after quotienting by the common translation. The alternating sum is one row in this rank-three affine-difference lattice. Hence retaining only the derivative keeps one primitive direction and loses the other two affine directions, together with the original common-value constraint: three congruence ranks in total. \(\square\)

## Proposition 10.3 (second-difference multiplier)

For averaged steps \(1\le u\le U\), \(1\le v\le V\), the squared multiplier is

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

The remaining obstruction is the centered rank-two estimate for the disjoint and low-overlap sectors. The available identities identify its geometry but do not create the required cancellation. No prime-offset or Fortunate-number theorem is claimed.

# References

[1] Richard K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Springer, 2004.

[2] Thomas Zaslavsky, “Biased graphs. I. Bias, balance, and gains,” *Journal of Combinatorial Theory, Series B* **47** (1989), 32–52.

[3] Shin-ichi Tanigawa, “Matroids of gain graphs in applied discrete geometry,” *Transactions of the American Mathematical Society* **367** (2015), 8597–8641.

[4] Mei-Chu Chang, Bryce Kerr, and Igor E. Shparlinski, “On the exponential large sieve inequality for sparse sequences modulo primes,” *Journal of Mathematical Analysis and Applications* **459** (2018), 53–81.

[5] Roger C. Baker, Marc Munsch, and Igor E. Shparlinski, “Additive energy and a large sieve inequality for sparse sequences,” *Mathematika* **68** (2022), 362–399.

[6] Kaisa Matomäki and Joni Teräväinen, “Products of primes in arithmetic progressions,” *Journal für die reine und angewandte Mathematik* **808** (2024), 193–240.

[7] H. Davenport and H. Halberstam, “Primes in arithmetic progressions,” *Michigan Mathematical Journal* **13** (1966), 485–489.

[8] Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory*, American Mathematical Society Colloquium Publications 53, 2004.

[9] Moubariz Z. Garaev, Florian Luca, and Igor E. Shparlinski, “Character sums and congruences with \(n!\),” *Transactions of the American Mathematical Society* **356** (2004), 5089–5102.

[10] Moubariz Z. Garaev, Florian Luca, and Igor E. Shparlinski, “Exponential sums and congruences with factorials,” *Journal für die reine und angewandte Mathematik* **584** (2005), 29–44.
