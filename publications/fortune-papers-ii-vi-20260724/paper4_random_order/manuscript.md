---
title: |
  Prime Detection Along Random Primorial-Product Paths
subtitle: |
  An unconditional reciprocal-frame theorem in the random-order model
author:
  - "Edward Stewart Anthony Bozzard (ORCID 0009-0002-4052-0994)"
date: "24 July 2026"
lang: en-GB
abstract: |
  Let the primes in a dyadic block be placed in a uniformly random order and
  form the associated nested product path. For the reciprocal pair-sum frame
  introduced in the preceding paper, we prove an effective expectation bound
  of order M(log X)^9, uniformly in every harmonic in the natural range. The
  same estimate holds for the weighted distinct-modulus aggregate and, through
  a precise comparison theorem from the preceding paper, for its Frobenius
  energy. The cancellation is supplied by expectation over the random
  permutation; no corresponding pointwise statement is claimed for the unique
  increasing primorial order. The proof conditions exactly on endpoint ranks,
  converts the random path into a uniform ordered set partition, obtains
  exponential ratio-character decay by a multivariate Cauchy estimate, bounds
  exceptional characters by sixth-moment orthogonality and unique
  factorisation, and closes a complete configuration ledger. The binding
  classes meet the target without a positive power-of-X cushion. The result is
  therefore a model theorem locating the remaining Fortune-relevant obstacle
  in derandomisation, not a proof of Fortune's conjecture.
keywords: ["random permutations", "primorial products", "reciprocal frames", "character sums", "ordered set partitions", "derandomisation"]
---

# 1. Introduction

Let \(0<\eta<1\), let \(X\) be large, and let
\[
\mathcal L=\{\ell:X\le \ell<2X,\ \ell\text{ prime}\},
\qquad K=|\mathcal L|.
\]
Instead of multiplying the block primes in increasing order, choose a uniformly
random permutation \(\sigma\in S_K\) and form the nested product path
\[
Q_0^\sigma=1,
\qquad
Q_j^\sigma=\prod_{i\le j}\ell_{\sigma(i)},
\qquad
P_j^\sigma=A_XQ_j^\sigma,
\qquad
A_X=\prod_{p<X}p.
\]
The identity permutation gives the genuine increasing primorial path. The
present paper averages over all \(K!\) orderings and does not establish a
pointwise estimate for that identity ordering.

The reciprocal-frame target comes from the pair sums
\[
S_{\{j,k\}}^\sigma=P_j^\sigma+P_k^\sigma,
\qquad 0\le j\le k\le K.
\]
There are
\[
N=K+1,
\qquad
M=\frac{N(N+1)}2
\]
such pair indices. The principal theorem proves that the off-diagonal
reciprocal energy of these pair sums is generically of the expected order at
the critical scale \(H=\eta X^2\).

The mechanism is not a disguised GRH argument. Expectation over the uniformly
random ordering creates an exact ordered-set-partition law. A contour estimate
then converts large rank cells into exponential decay unless certain ratio
characters have unusually large bias on the block primes. Sixth-moment
orthogonality shows that only \(O(X(\log X)^3)\) characters can be exceptional.
A path-coordinate matching argument and a complete configuration ledger then
close the estimate.

The binding ledger classes close at exactly \(M(\log X)^9\), up to constants.
There is no positive power-of-\(X\) reserve. This makes the completeness of the
configuration classification and the exact multiplicities part of the proof,
not merely bookkeeping.

# 2. Frame, hypotheses, and theorem

Put
\[
H=\eta X^2,
\qquad
\mathcal Q_X=\{q:H\le q<2H,\ q\text{ prime}\}.
\]
Let \(\rho\) be a nonnegative even Schwartz function. For \(a\ne0\) define
\[
w_{q,a}=\rho(Ha/q),
\qquad
D_X=\sum_{q\in\mathcal Q_X}\sum_{a\ne0}w_{q,a},
\qquad
p_{q,a}=\frac{w_{q,a}}{D_X},
\]
\[
\Psi_a(L)=\sum_{q\in\mathcal Q_X}p_{q,a}e(aL/q),
\qquad
m_a=\sum_{q\in\mathcal Q_X}p_{q,a},
\qquad e(x)=e^{2\pi i x}.
\]
Since \(\rho\) is even,
\[
\sum_{a\ge1}m_a=\frac12.
\]
For pair indices \(u,v\), define
\[
D_{u,v}^\sigma=S_u^\sigma-S_v^\sigma
\]
and the fixed-harmonic energy
\[
\mathcal E_a^\sigma
 =\sum_{u\ne v}|\Psi_a(D_{u,v}^\sigma)|^2.
\]
Write
\[
\kappa_{2,a}=\sum_{q\in\mathcal Q_X}p_{q,a}^2.
\]
Expanding the square and separating equal and unequal moduli gives the exact
decomposition
\[
\mathcal E_a^\sigma=M(M-1)\kappa_{2,a}+\mathcal R_a^\sigma,
\tag{2.1}
\]
where
\[
\mathcal R_a^\sigma
 =\sum_{\substack{q,r\in\mathcal Q_X\\q\ne r}}
 p_{q,a}p_{r,a}
 \sum_{u\ne v}e_{qr}\!\left(a(r-q)D_{u,v}^\sigma\right),
\qquad e_{qr}(x)=e(x/(qr)).
\tag{2.2}
\]
Let \(\mathfrak F_X^\sigma\) denote the reciprocal-frame Frobenius energy of
[1, Definition 3.5]. The only result imported from [1] is its precise comparison
[1, Proposition 3.1]:
\[
\mathfrak F_X^\sigma
 \le 2\sum_{a\ge1}\frac{\mathcal E_a^\sigma}{m_a}.
\tag{2.3}
\]
All other estimates used below are proved in this paper.

We impose the following explicit standing hypotheses.

**(N1) Frame admissibility.** There is \(\delta_\rho>0\) such that
\[
\rho(t)\ge\delta_\rho\qquad(1/2\le t\le1).
\]
Then the harmonic \(a=1\) populates every row and
\[
D_X\ge\delta_\rho|\mathcal Q_X|>0.
\]
Any equivalent positivity condition on the sampled set \(\{Ha/q\}\) would
suffice; some condition of this kind is necessary because otherwise the frame
may be empty.

**(N2) Effective block bounds.** For all sufficiently large \(X\),
\[
\frac{X}{2\log X}\le K\le\frac{3X}{\log X},
\qquad
\frac{X^2}{8(\log X)^2}\le M\le\frac{16X^2}{(\log X)^2}.
\tag{2.4}
\]
These are standard effective consequences of the prime number theorem.

## Theorem 2.1 (random-order reciprocal-frame theorem)

Under (N1)--(N2), for all sufficiently large \(X\), with \(\sigma\) uniform on
\(S_K\):

1. uniformly for every integer \(1\le |a|<H\),
   \[
   \mathbb E_\sigma[\mathcal E_a^\sigma]
   \le C(\eta,\rho)M(\log X)^9;
   \tag{2.5}
   \]
2. the distinct-modulus aggregate satisfies
   \[
   \mathbb E_\sigma\!\left[
   \sum_{a\ge1}\frac{\mathcal R_a^\sigma}{m_a}
   \right]
   \le C(\eta,\rho)M(\log X)^9;
   \tag{2.6}
   \]
3. the Frobenius energy satisfies
   \[
   \mathbb E_\sigma[\mathfrak F_X^\sigma]
   \le C(\eta,\rho)M(\log X)^9.
   \tag{2.7}
   \]

All constants are effective. The logarithmic exponent \(9\) is absolute.
Consequently, Markov's inequality applied to the nonnegative Frobenius energy
shows that for every \(\omega(X)\to\infty\), all but an
\(O(\omega(X)^{-1})\) fraction of the \(K!\) orderings satisfy the corresponding
aggregate target with loss \((\log X)^9\omega(X)\).

The theorem follows from the following uniform estimate.

## Proposition 2.2 (per-modulus-pair bias sum)

For distinct \(q,r\in\mathcal Q_X\), every integer \(1\le|a|<H\), and
\(b=a(r-q)\),
\[
\sum_{u\ne v}
\left|\mathbb E_\sigma e_{qr}(bD_{u,v}^\sigma)\right|
\le C(\eta)M(\log X)^9.
\tag{2.8}
\]

Sections 3--8 prove Proposition 2.2; Section 9 assembles Theorem 2.1.

# 3. Arithmetic preliminaries and complete configuration enumeration

## Lemma 3.1 (path rigidity)

Every \(\sigma\)-path satisfies \(P_{j+1}^\sigma\ge XP_j^\sigma\). If
\(|c_t|\le B\), \(X>B+1\), and
\[
\sum_t c_tP_t^\sigma=0,
\]
then every \(c_t=0\).

**Proof.** Let \(t\) be the largest index with \(c_t\ne0\). The geometric
separation gives
\[
\sum_{i<t}P_i^\sigma\le \frac{P_t^\sigma}{X-1}.
\]
Hence the top term has magnitude at least \(P_t^\sigma\), whereas the lower
terms have total magnitude at most \(BP_t^\sigma/(X-1)<P_t^\sigma\), a
contradiction. \(\square\)

In particular, \(u\ne v\) implies \(D_{u,v}^\sigma\ne0\), because its
coefficients are bounded by \(2\).

## Lemma 3.2 (unit multipliers)

For distinct \(q,r\in\mathcal Q_X\), \(1\le|a|<H\), \(b=a(r-q)\), and
\(0<|c|\le2\),
\[
b\ne0,
\qquad 0<|b|<H^2\le qr,
\qquad (bcA_X,qr)=1.
\tag{3.1}
\]
Every product of block primes is also a unit modulo \(qr\).

**Proof.** Since \(q,r\ge H>|a|\), neither shell prime divides \(a\). Also
\(0<|r-q|<H\le q,r\), all prime factors of \(A_X\) are below \(X<H\), and
\(|c|\le2<q,r\). The same inequalities apply to every \(\ell\in\mathcal L\).
\(\square\)

Fix an ordered pair \((u,v)\), where \(u=\{i,j\}\), \(v=\{k,l\}\), and
\(u\ne v\) as multisets. Let \(c(t)\) be the multiplicity of \(t\) in \(u\)
minus its multiplicity in \(v\). Let
\[
t_1<\cdots<t_m
\]
be the indices with \(c(t_s)\ne0\), and put \(c_s=c(t_s)\). Then
\[
2\le m\le4,
\qquad c_s\in\{-2,-1,1,2\},
\qquad \sum_sc_s=0.
\]
The ranks divide the ordered block primes into cells
\[
W_0,W_1,\ldots,W_m,
\]
where \(W_0\) consists of positions \(1,\ldots,t_1\), \(W_s\) consists of
positions \((t_s,t_{s+1}]\) for \(1\le s<m\), and \(W_m\) consists of
positions \((t_m,K]\). Write \(n_s=|W_s|\) and
\[
R_s=\prod_{\ell\in W_s}\ell.
\]
Then
\[
D_{u,v}^\sigma
=A_X\Bigl(\prod W_0\Bigr)
\left(c_1+c_2R_1+c_3R_1R_2+\cdots+c_mR_1\cdots R_{m-1}\right).
\tag{3.2}
\]

## Lemma 3.3 (complete coefficient-pattern list)

The possible nonzero coefficient vectors are exactly:

- \(m=2\): \((1,-1),(-1,1),(2,-2),(-2,2)\);
- \(m=3\): the six signed permutations of \((1,1,-2)\);
- \(m=4\): the six vectors with two entries \(+1\) and two entries \(-1\).

**Proof.** The entries are nonzero, sum to zero, and have total absolute value
at most four. For \(m=4\), every absolute value is one and the signs split two
and two. For \(m=3\), one entry has absolute value two and the other two have
absolute value one with the opposite sign. For \(m=2\), the vector is
\((c,-c)\) with \(c\in\{\pm1,\pm2\}\). Every listed vector is realised by an
ordered pair of two-element multisets. \(\square\)

Call the \(m=2\), coefficient-\((\pm1,\mp1)\) configurations **type S**, and
the coefficient-\((\pm2,\mp2)\) configurations **type D**.

## Lemma 3.4 (exact multiplicities)

For a fixed rank configuration and coefficient vector, the multiplicity is
\(N\) for type S and \(1\) for every other configuration. Moreover
\[
M(M-1)
=N^2(N-1)+N(N-1)+6\binom N3+6\binom N4.
\tag{3.3}
\]

**Proof.** In every non-S configuration, the positive coefficients determine
\(u\) and the negative coefficients determine \(v\) uniquely. In type S, the
cancelled common index is free over all \(N\) path indices, so the multiplicity
is exactly \(N\). Summing the classes gives
\[
2\binom N2N+2\binom N2+6\binom N3+6\binom N4.
\]
Direct expansion equals \(M(M-1)\). \(\square\)

Therefore
\[
\sum_{u\ne v}
\left|\mathbb E_\sigma e_{qr}(bD_{u,v}^\sigma)\right|
=
\sum_{\text{configurations}}
\operatorname{mult}(\mathcal C)
\left|\mathbb E_\sigma e_{qr}(bD_{\mathcal C}^\sigma)\right|.
\tag{3.4}
\]

# 4. Exact ordered partitions and contour decay

## Lemma 4.1 (rank-conditioning identity)

Let \(\psi_0,\ldots,\psi_m:\mathcal L\to\mathbb C\) be unimodular functions,
extended completely multiplicatively to products. Conditional on the cell
sizes \(n=(n_0,\ldots,n_m)\), the cells form a uniformly random ordered set
partition of \(\mathcal L\), and
\[
\Phi(\psi;n)
:=\mathbb E_\sigma\prod_{s=0}^m\psi_s\!\left(\prod W_s\right)
=
\binom{K}{n_0,\ldots,n_m}^{-1}
[x_0^{n_0}\cdots x_m^{n_m}]
\prod_{\ell\in\mathcal L}
\left(\sum_{s=0}^m x_s\psi_s(\ell)\right).
\tag{4.1}
\]

**Proof.** A uniform permutation induces the uniform distribution on ordered
set partitions with the prescribed sizes. Expanding the product on the right
indexes assignments of every block prime to a cell. The indicated coefficient
sums the required character product over all assignments of those sizes, and
the multinomial coefficient is the number of assignments. \(\square\)

If \(n_s=0\), delete that cell. The identity remains valid for the nonempty
cells.

For a character \(\chi\) modulo \(qr\), put
\[
t_\chi=\frac1K\left|\sum_{\ell\in\mathcal L}\chi(\ell)\right|.
\]

## Lemma 4.2 (multivariate contour bound)

After empty cells are deleted, there are at most five cells and
\[
|\Phi(\psi;n)|
\le
\min\left\{1,
C_*K^2
\exp\left[-\sum_{s<s'}\frac{n_sn_{s'}}K
\left(1-t_{\psi_s\overline{\psi_{s'}}}\right)\right]
\right\},
\tag{4.2}
\]
where
\[
C_*=\frac{e^5}{\sqrt{2\pi}}<60.
\]

**Proof.** The trivial bound is \(|\Phi|\le1\). For the other bound, apply
Cauchy's coefficient formula on the polydisc \(|x_s|=\varrho_s=n_s/K\):
\[
|\Phi|
\le
\left(\binom K{n_0,\ldots,n_m}\prod_s\varrho_s^{n_s}\right)^{-1}
\max_\theta
\prod_{\ell\in\mathcal L}
\left|\sum_s\varrho_se^{i\theta_s}\psi_s(\ell)\right|.
\tag{4.3}
\]
If \(j\le5\) cells are nonempty, Stirling's inequalities give
\[
\binom K{n_0,\ldots,n_m}\prod_s\varrho_s^{n_s}
\ge \sqrt{2\pi}e^{-5}K^{-2}.
\tag{4.4}
\]
For unimodular \(z_s\) and weights \(\varrho_s\) summing to one,
\[
\left|\sum_s\varrho_sz_s\right|^2
=1-\sum_{s<s'}\varrho_s\varrho_{s'}|z_s-z_{s'}|^2.
\tag{4.5}
\]
Using \(\log y\le(y^2-1)/2\) and
\(z_s=e^{i\theta_s}\psi_s(\ell)\),
\[
\sum_{\ell\in\mathcal L}|z_s-z_{s'}|^2
\ge2K\left(1-t_{\psi_s\overline{\psi_{s'}}}\right)
\]
uniformly in the phases. Substitution into (4.3) proves (4.2). \(\square\)

# 5. Gauss expansion and exceptional characters

For the configuration (3.2), let
\[
m_s=bc_sA_X,
\qquad
V_s=\Bigl(\prod W_0\Bigr)R_1\cdots R_{s-1}.
\]
Lemma 3.2 gives
\[
e_{qr}(bD_{u,v}^\sigma)=\prod_{s=1}^m e_{qr}(m_sV_s).
\tag{5.1}
\]

## Lemma 5.1 (Gauss coefficients and norms)

For \((m,qr)=1\) and \(v\in(\mathbb Z/qr\mathbb Z)^\times\),
\[
e_{qr}(mv)=\sum_{\chi\bmod qr}c_\chi(m)\chi(v),
\qquad
c_\chi(m)=\frac{\chi(m)\tau(\overline\chi)}{\varphi(qr)}.
\tag{5.2}
\]
The coefficients satisfy
\[
\|c(m)\|_\infty\le\frac{2}{\eta X^2},
\qquad
\|c(m)\|_2=1,
\qquad
\|c(m)\|_1\le2\eta X^2.
\tag{5.3}
\]

**Proof.** Formula (5.2) is multiplicative Fourier inversion on the unit group.
For \(\chi=\chi_q\chi_r\), CRT gives
\[
\tau_{qr}(\chi)
=\chi_q(r)\chi_r(q)\tau_q(\chi_q)\tau_r(\chi_r).
\]
For a nonprincipal character modulo a prime \(p\), the standard calculation
\[
|\tau_p(\chi)|^2
=\sum_{x,y\bmod p}\chi(x)\overline{\chi(y)}e_p(x-y)=p
\]
uses the substitution \(x=ty\) and character orthogonality; for the principal
character, \(\tau_p(\chi_0)=-1\). Hence
\(|\tau_{qr}(\chi)|\le\sqrt{qr}\), and
\[
\|c(m)\|_\infty
\le\frac{\sqrt{qr}}{\varphi(qr)}
\le\frac2{\sqrt{qr}}
\le\frac2{\eta X^2}.
\]
Parseval gives \(\|c(m)\|_2=1\), and Cauchy--Schwarz gives
\(\|c(m)\|_1\le\sqrt{\varphi(qr)}\le\sqrt{qr}\le2\eta X^2\).
\(\square\)

Expanding every active slot gives
\[
\mathbb E_\sigma e_{qr}(bD_{u,v}^\sigma)
=
\sum_{\chi^{(1)},\ldots,\chi^{(m)}}
\left(\prod_{s=1}^m c_{\chi^{(s)}}(m_s)\right)
\Phi(\psi;n),
\tag{5.4}
\]
where the cell characters are
\[
\psi_i=\prod_{s>i}\chi^{(s)},
\qquad 0\le i\le m,
\qquad \psi_m=1.
\tag{5.5}
\]
Thus
\[
\psi_{i-1}\overline{\psi_i}=\chi^{(i)}.
\tag{5.6}
\]
If \(n_0=0\), then \(V_1=1\), slot \(1\) is the deterministic unimodular
constant \(e_{qr}(m_1)\), and it is not expanded. The tail slot never collapses,
even when the tail cell is empty.

For a two-slot group define
\[
B(\omega)=
\sum_{\chi\chi'=\omega}|c_\chi(m_s)||c_{\chi'}(m_{s'})|.
\]
Cauchy--Schwarz and (5.3) give
\[
\sup_\omega B(\omega)\le1,
\qquad
\sum_\omega B(\omega)\le4\eta^2X^4.
\tag{5.7}
\]
For a one-slot group the corresponding bounds are
\[
\sup\le\frac2{\eta X^2},
\qquad
\ell^1\text{-sum}\le2\eta X^2.
\tag{5.8}
\]

Call \(\chi\) **bad** if \(t_\chi\ge3/4\), and let \(\beta\) be the number of
bad characters modulo \(qr\).

## Lemma 5.2 (sixth-moment exceptional-character bound)

For \(X>8/\eta^2\),
\[
\beta
\le6\left(\frac43\right)^6\frac{\varphi(qr)}{K^3}
\le1100\eta^2X(\log X)^3.
\tag{5.9}
\]

**Proof.** Character orthogonality gives
\[
\sum_{\chi\bmod qr}
\left|\sum_{\ell\in\mathcal L}\chi(\ell)\right|^6
=
\varphi(qr)\,
\#\{\ell_1\ell_2\ell_3\equiv\ell_4\ell_5\ell_6\pmod{qr}\}.
\tag{5.10}
\]
Both products are positive integers below
\((2X)^3=8X^3<\eta^2X^4\le qr\). The congruence is therefore equality. Unique
factorisation forces equality of the two three-element multisets, so there are
at most \(6K^3\) solutions. Chebyshev's inequality at level \((3K/4)^6\)
gives
\[
\beta(3K/4)^6\le6\varphi(qr)K^3.
\]
Use \(\varphi(qr)\le4\eta^2X^4\) and the lower bound for \(K\) in (2.4).
\(\square\)

This orthogonality count is the only arithmetic input controlling exceptional
characters. Good characters have deficit \(1-t_\chi>1/4\).

# 6. Ratio coordinates and matching

Set
\[
w_0=600\log X.
\tag{6.1}
\]
A cell is **big** if its size is at least \(w_0\). Consider a configuration
with at most one non-big cell. Since at most five cells have total size \(K\),
there is a macro cell \(s_*\) with
\[
n_{s_*}\ge K/5\ge w_0
\]
for sufficiently large \(X\). List the big cells as
\[
i_0<i_1<\cdots<i_p.
\]
Consecutive big cells differ by at most two in index.

For every big cell \(i\ne s_*\), define the ratio coordinate
\[
\sigma_i=\psi_i\overline{\psi_{s_*}},
\qquad \sigma_{s_*}=1.
\tag{6.2}
\]
Slots between consecutive big cells form a group
\[
G_j=\{s:i_{j-1}<s\le i_j\}.
\]
Its size is one, except that it is two when the unique micro cell lies between
the two big cells, and
\[
\prod_{s\in G_j}\chi^{(s)}
=\sigma_{i_{j-1}}\overline{\sigma_{i_j}}.
\tag{6.3}
\]
An active slot outside all groups is an **orphan**. There is at most one: a
front orphan when \(0<n_0<w_0\), or a back orphan when \(n_m<w_0\). The front
slot is absent, rather than orphaned, when \(n_0=0\).

## Lemma 6.1 (triangular coordinate bijection)

Choose one designated slot in every group. The map from all active slot
characters to

1. the ratio coordinates \(\sigma_i\), \(i\ne s_*\);
2. the non-designated characters inside two-slot groups; and
3. the orphan character, if present,

is a bijection of finite character groups.

**Proof.** In additive notation on the dual group, order the coordinates by
distance from \(s_*\). Each new ratio coordinate is the product on the adjacent
group times the preceding ratio coordinate. The designated slot is then solved
from the group product and the non-designated slot. The resulting integer
matrix is triangular with diagonal entries \(\pm1\), hence invertible. \(\square\)

Partition character tuples according to whether each \(\sigma_i\) is bad or
good. Let \(f\) be the number of good coordinates. In the contour estimate,
retain only the pairs \((i,s_*)\) for good \(\sigma_i\). Each contributes at
least
\[
\frac{n_in_{s_*}}K(1-t_{\sigma_i})
\ge\frac{w_0}{5}\cdot\frac14=30\log X.
\]
Therefore
\[
|\Phi|\le1\quad(f=0),
\qquad
|\Phi|\le C_*K^2X^{-30f}\quad(f\ge1).
\tag{6.4}
\]

## Lemma 6.2 (path matching lemma)

Root the path of big cells at \(s_*\). For each non-root vertex \(v\), let
\(e_v\) be its inner edge towards the root. For a fixed good/bad pattern,
\[
\Sigma(P)
\le
\operatorname{Orph}
\prod_{v\text{ bad}}\bigl(\beta\,\operatorname{SUP}(e_v)\bigr)
\prod_{v\text{ good}}\operatorname{L1}(e_v)
D(f),
\tag{6.5}
\]
where
\[
D(0)=1,
\qquad D(f)=C_*K^2X^{-30f}\ (f\ge1),
\]
\[
\operatorname{Orph}\le2\eta X^2,
\]
and, for group size one or two respectively,
\[
\operatorname{SUP}(1)=\frac2{\eta X^2},
\quad \operatorname{L1}(1)=2\eta X^2,
\qquad
\operatorname{SUP}(2)=1,
\quad \operatorname{L1}(2)=4\eta^2X^4.
\tag{6.6}
\]

**Proof.** Sum the orphan character first, at cost at most its \(\ell^1\)-norm.
For fixed ratio coordinates, sum the internal free slot in each two-slot group;
this produces the group function \(B\). Now sum ratio coordinates arm by arm,
from the outermost vertex towards the root. When \(v\) is processed, its inner
neighbour remains fixed. A good coordinate is summed over the full character
group and costs \(\operatorname{L1}(e_v)\); a bad coordinate has at most
\(\beta\) choices and costs
\(\beta\operatorname{SUP}(e_v)\). Every edge is consumed once. \(\square\)

## Lemma 6.3 (all-bad pattern domination)

For sufficiently large \(X\), the sum over all patterns is at most twice the
all-bad bound.

**Proof.** Relative to the all-bad pattern, changing a vertex to good introduces
\[
\frac{\operatorname{L1}(e)}{\beta\operatorname{SUP}(e)}
\]
and the decay \(X^{-30}\), together with a share of the prefactor
\(C_*K^2\). Since \(\beta\ge1\), \(K\le3X/\log X\), and (6.6) holds, each
changed vertex gains at least \(X^{-23}\), for either group size. There are at
most four ratio coordinates, so the total of all non-all-bad patterns is at
most \(16X^{-23}\) times the all-bad bound. \(\square\)

Combining Lemmas 5.1 and 6.1--6.3 gives the master estimate.

## Proposition 6.4 (per-configuration bound)

For any configuration with at most one cell of size below \(w_0\),
\[
\left|\mathbb E_\sigma e_{qr}(bD)\right|
\le
\min\left\{1,
2\operatorname{Orph}\,\beta^p
\prod_{e}\operatorname{SUP}(e)
\right\},
\tag{6.7}
\]
where \(p\) is the number of non-root big cells.

# 7. Complete configuration ledger

Use
\[
\beta\le C_bX(\log X)^3,
\qquad C_b=1100\eta^2,
\qquad
N\le\frac{4X}{\log X}.
\tag{7.1}
\]
We assign configurations disjointly as follows. First place every configuration
with at least two micro cells into T1. Among configurations with exactly one
micro cell, place \(m=2\) in T2 and \(m=3\) in T3; the remaining \(m=4\)
configurations are C2a--C2d according to the micro-cell position. Configurations
with no micro cell are C1, C3, or C4 according to \(m=4,3,2\).

## Trivial classes

**T1: at least two micro cells.** Choose the constrained cells, their sizes,
the remaining at most two rank parameters, and the coefficient pattern. Including
the type-S multiplicity gives
\[
O(N^2w_0^2)
\]
ordered pairs. Their total contribution is
\[
O(M(\log X)^2).
\tag{7.2}
\]

**T2: \(m=2\), exactly one micro cell.** There are
\(O(N^2w_0)\) ordered pairs after the type-S multiplicity. Their contribution
is
\[
O(M\log X).
\tag{7.3}
\]

**T3: \(m=3\), exactly one micro cell.** There are
\(O(N^2w_0)\) configurations, all of multiplicity one. Their contribution is
\[
O(M\log X).
\tag{7.4}
\]

## Character classes

**C1: \(m=4\), all five cells big.** There are four one-slot edges and no
orphan, so
\[
|\mathbb E e_{qr}(bD)|
\ll_\eta \beta^4X^{-8}
\ll_\eta X^{-4}(\log X)^{12}.
\]
There are \(O(N^4)\) configurations. The contribution is
\[
O_\eta((\log X)^8).
\tag{7.5}
\]

**C2a: \(m=4\), one interior micro cell.** There are four big cells, one
two-slot edge, two one-slot edges, and no orphan. Thus
\[
|\mathbb E e_{qr}(bD)|
\ll_\eta \beta^3X^{-4}
\ll_\eta X^{-1}(\log X)^9.
\]
The count is \(O(N^3w_0)\), so the contribution is
\[
O_\eta(X^2(\log X)^7)
=O_\eta(M(\log X)^9).
\tag{7.6}
\]
This is a binding class.

**C2b: \(m=4\), \(0<n_0<w_0\).** There are three one-slot edges and a front
orphan. The bound is again
\[
O_\eta(X^{-1}(\log X)^9),
\]
and the count is \(O(N^3w_0)\). Hence
\[
O_\eta(M(\log X)^9).
\tag{7.7}
\]
This is binding.

**C2c: \(m=4\), \(n_0=0\), all other cells big.** Slot one collapses. There
are three one-slot edges and no orphan, giving
\[
|\mathbb E e_{qr}(bD)|
\ll_\eta \beta^3X^{-6}
\ll_\eta X^{-3}(\log X)^9.
\]
With \(O(N^3)\) configurations, the contribution is
\[
O_\eta((\log X)^6).
\tag{7.8}
\]

**C2d: \(m=4\), the tail cell is micro or empty.** There are three one-slot
edges and a back orphan, including when the tail itself is empty. The bound and
count are as in C2b, so the contribution is
\[
O_\eta(M(\log X)^9).
\tag{7.9}
\]
This is binding.

**C3: \(m=3\), all four cells big.** There are three one-slot edges and no
orphan. The bias is
\[
O_\eta(X^{-3}(\log X)^9),
\]
and there are \(O(N^3)\) configurations. The contribution is
\[
O_\eta((\log X)^6).
\tag{7.10}
\]

**C4: \(m=2\), all three cells big.** There are two one-slot edges. Including
multiplicity \(N\) for type S, there are \(O(N^3)\) ordered pairs. Since
\[
|\mathbb E e_{qr}(bD)|
\ll_\eta \beta^2X^{-4}
\ll_\eta X^{-2}(\log X)^6,
\]
the contribution is
\[
O_\eta(X(\log X)^3)=O_\eta(M).
\tag{7.11}
\]

These classes exhaust all configurations. Summing (7.2)--(7.11) proves
Proposition 2.2.

# 8. Why the logarithmic exponent is binding

The three binding classes C2a, C2b, and C2d have raw size
\[
X^2(\log X)^7.
\]
Because
\[
M\asymp\frac{X^2}{(\log X)^2},
\]
this is exactly \(M(\log X)^9\). The exponent \(9\) comes from the three bad
ratio coordinates, each carrying the factor \((\log X)^3\) in (5.9). A missing
rank parameter, an omitted configuration family, or the loss of one
one-slot-edge saving would exceed the target by a power of \(X\). The proof
therefore has only a polylogarithmic margin.

# 9. Assembly of the theorem

For \(1\le|a|<H\), (2.1), (2.2), and Proposition 2.2 give
\[
\mathbb E_\sigma\mathcal E_a^\sigma
\le
M(M-1)\kappa_{2,a}
+m_a^2C(\eta)M(\log X)^9.
\tag{9.1}
\]
By (N1),
\[
D_X\ge\delta_\rho|\mathcal Q_X|,
\qquad
\max_qp_{q,a}
\le\frac{\|\rho\|_\infty}{\delta_\rho|\mathcal Q_X|}.
\]
The prime number theorem in the shell gives
\[
|\mathcal Q_X|\ge\frac{\eta X^2}{8\log X}
\]
for large \(X\). Since
\[
\kappa_{2,a}\le m_a\max_qp_{q,a},
\]
we obtain
\[
M(M-1)\kappa_{2,a}
\le C(\eta,\rho)\frac{Mm_a}{\log X}.
\]
This proves (2.5).

For \(1\le a<H\), Proposition 2.2 gives
\[
\mathbb E_\sigma\mathcal R_a^\sigma
\le m_a^2C(\eta)M(\log X)^9.
\]
Therefore
\[
\sum_{1\le a<H}
\frac{\mathbb E_\sigma\mathcal R_a^\sigma}{m_a}
\le C(\eta)M(\log X)^9\sum_{a\ge1}m_a
\le\frac12C(\eta)M(\log X)^9.
\tag{9.2}
\]
For \(a\ge H\), the trivial bound is
\[
|\mathcal R_a^\sigma|\le M^2m_a^2.
\]
Schwartz decay and (N1) imply \(m_a\ll_\rho a^{-6}\), so
\[
\sum_{a\ge H}M^2m_a\ll X^4H^{-5}=o(1).
\tag{9.3}
\]
Equations (9.2)--(9.3) prove (2.6).

Finally, use the precise comparison (2.3). Termwise,
\[
\frac{\mathcal E_a^\sigma}{m_a}
\le M^2\max_qp_{q,a}+rac{\mathcal R_a^\sigma}{m_a}.
\]
Moreover
\[
\sum_{a\ge1}\max_qp_{q,a}
\le
\frac1{D_X}\sum_{a\ge1}\sup_{a/2<t\le a}\rho(t)
\ll_\rho D_X^{-1}.
\]
Thus the total diagonal contribution is \(O_{\eta,\rho}(M/\log X)\), while the
distinct-modulus contribution is bounded by (2.6). This proves (2.7) and
Theorem 2.1. \(\square\)

# 10. Effective constants and verification

One admissible constants ledger is
\[
w_0=600\log X,
\qquad C_*<60,
\qquad
\beta\le1100\eta^2X(\log X)^3.
\]
Each good ratio coordinate supplies \(X^{-30}\) before the contour prefactor
and at least \(X^{-23}\) after all group-norm costs. The largeness conditions
are effective and depend only on \(\eta\) and \(\rho\): they include
\(X>8/\eta^2\), \(K/5\ge600\log X\), the effective prime-number-theorem shell
bounds, and the final pattern-domination absorption.

The supporting code performs exact finite checks of the ordered-partition
identity, the coefficient taxonomy and multiplicities, Gauss/CRT coefficient
norms, the sixth-moment identity, the declared ledger exponents, and an
end-to-end comparison between direct permutation averaging and the complete
character expansion. These checks validate implementation and bookkeeping;
they are not used as proofs of the asymptotic statements above.

# 11. Scope and derandomisation

The expectation over \(S_K\) is the source of the decisive cancellation. The
identity ordering has no order entropy, and the proof supplies no mechanism for
showing that it is nonexceptional. Consequently:

1. the theorem does not prove Fortune's conjecture;
2. it does not prove the reciprocal-frame target for increasing primorials;
3. it shows that the pair-sum architecture is generically compatible with the
   critical-length target; and
4. it relocates the remaining problem to derandomisation or concentration.

A natural next question is whether the same machinery can control a second
moment over orderings, such as
\[
\mathbb E_\sigma[(\mathcal E_a^\sigma)^2]
\ll M^2X^{o(1)},
\]
and whether any arithmetic principle can then identify the increasing order as
nonexceptional. Neither statement is claimed here.

## AI-assistance disclosure

The research programme used large language models for structured literature
triage, symbolic and computational cross-checking, adversarial review, software
drafting, and editorial assembly. The manuscript was rebuilt from a frozen
proof source after a manuscript-only hostile review correctly found that an
earlier synopsis omitted load-bearing arguments. The named author takes
responsibility for the mathematical claims, citations, code, and final
presentation.

## Data, code, and reproducibility

The frozen mathematical source is `RQM_PROOF.md`, blob
`53f63f662f5a9d6e750a592ba8bcba6cf4bc9095`, in the public repository
`digitalgoldfisj79/multi-agent-environment`. The supporting audit records the
exact source-to-manuscript fidelity matrix, clean-room finite checks, external
model-review input hashes, and unedited review output. Compiled artifacts are
not cleared until regenerated from this source and checked against their
recorded hashes.

# References

1. E. S. A. Bozzard, *Prime Detection at Primorial Centres: Reciprocal Frames,
   Exact Moments, and Structural Obstructions*, Zenodo DOI
   `10.5281/zenodo.21457113`, especially Definition 3.5 and Proposition 3.1.
2. H. Davenport, *Multiplicative Number Theory*, 3rd ed., revised by H. L.
   Montgomery, Springer, 2000, Chapter 9.
3. Standard effective forms of the prime number theorem for dyadic intervals.
