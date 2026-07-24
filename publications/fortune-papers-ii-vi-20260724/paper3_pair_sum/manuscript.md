---
title: |
  Pair-Sum Rigidity, Exceptional Sets, and Conditional Prime Detection at Primorial Centres
subtitle: |
  An unconditional kernel theory and an exact conditional boundary
author:
  - "Edward Stewart Anthony Bozzard"
date: "24 July 2026"
lang: en-GB
abstract: |
  For the superincreasing primorial-prefix walk, we prove an exact
  difference-multiplicity dichotomy for the pair-sum set: every nonzero
  difference has multiplicity either one or exactly the walk length. This gives
  a two-scale decomposition of all harmonic energies and exposes a necessary
  single-walk subproblem. We then prove high-moment bounds and a sub-Weibull
  Lebesgue tail for the centred pair-sum kernel, including exact sixth and third
  centred moments. The resulting Lebesgue theory is exponentially stronger
  than the level-set estimate needed by the reciprocal prime-sampling
  architecture.

  The remaining obstruction is therefore arithmetic concentration on sparse
  exceptional sets. We formulate that transfer gap exactly and complement it
  with a truncated-singular-series calculation. Under block-averaged first
  moments and block-averaged Hardy--Littlewood pair correlations with relative
  error \(o(\log X/X)\), the variance criterion from the preceding paper closes
  and Fortune's conjecture follows for all sufficiently large indices. No
  unconditional prime-detection claim is made.
keywords: ["superincreasing sequences", "pair-sum sets", "additive energy", "sub-Weibull tails", "Hardy--Littlewood", "Fortune's conjecture"]
---

# 1. Setting

Let \(P_0,\ldots,P_{N-1}\) be a positive sequence satisfying
\[
P_{j+1}\ge XP_j.
\]
For the primorial-prefix walk this holds with \(X\) equal to the dyadic block
parameter. Let
\[
\mathcal P_2=\{\{j,k\}:0\le j\le k<N\},\quad
M=\frac{N(N+1)}2,\quad S_{\{j,k\}}=P_j+P_k.
\]
Define
\[
H_2(\theta)=\sum_{u\in\mathcal P_2}e(\theta S_u),\qquad
K(\theta)=|H_2(\theta)|^2-M.
\]

# 2. Bounded-coefficient rigidity

## Lemma 2.1

Let \(B\ge1\) and \(X>B+1\). If
\[
\sum_{t<N}c_tP_t=0,\qquad |c_t|\le B,
\]
then every \(c_t=0\).

### Proof

Let \(t\) be the largest index with \(c_t\ne0\). Superincrease gives
\[
\sum_{i<t}P_i\le \frac{P_t}{X-1}.
\]
Hence
\[
\left|\sum_{i<t}c_iP_i\right|
\le \frac{B}{X-1}P_t<P_t\le |c_t|P_t,
\]
a contradiction. \(\square\)

This one lemma drives both the finite multiplicity classification and all
moment counts up to order \(k<(X-1)/2\).

# 3. Difference-multiplicity dichotomy

For nonzero \(D\), define
\[
r(D)=\#\{(u,v)\in\mathcal P_2^2:u\ne v,\ S_u-S_v=D\}.
\]

## Theorem 3.1

Assume \(X>5\). For every nonzero \(D\):

1. if \(D=P_i-P_k\) with \(i\ne k\), then \(r(D)=N\), and its representations are exactly
   \[
   (u,v)=(\{i,t\},\{k,t\}),\qquad 0\le t<N;
   \]
2. otherwise \(r(D)=1\).

There are exactly \(N(N-1)\) differences of the first kind.

### Proof

If two representations satisfy
\[
S_u-S_v=S_{u'}-S_{v'},
\]
then
\[
S_u+S_{v'}=S_{u'}+S_v.
\]
The resulting relation has coefficients bounded by four, so rigidity forces
the endpoint multiset identity
\[
u\uplus v'=u'\uplus v.
\]
If \(u\) and \(v\) share an index, the difference is a single-walk difference
and the shared index is the only free parameter. If they are disjoint, the
multiset identity forces \(u'=u\) and \(v'=v\). \(\square\)

# 4. Exact two-scale energy decomposition

For any nonnegative function \(T\) on the nonzero integers,
\[
\sum_{u\ne v}T(S_u-S_v)
=
N\sum_{i\ne k}T(P_i-P_k)
+
\sum_{D\in\mathcal D_1}T(D),
\]
where every \(D\in\mathcal D_1\) has multiplicity one.

For the reciprocal characteristic function,
\[
\mathcal E_a=N\mathcal G_a+\mathcal S_a,\qquad \mathcal S_a\ge0,
\]
where
\[
\mathcal G_a=\sum_{i\ne k}|\Psi_a(P_i-P_k)|^2.
\]
Therefore the pair-sum target \(\mathcal E_a\ll MX^{o(1)}\) necessarily implies
\[
\mathcal G_a\ll \frac{M}{N}X^{o(1)}\asymp NX^{o(1)}.
\]
There is no intermediate multiplicity scale.

# 5. High moments

## Lemma 5.1

If \(X>2k+1\), then
\[
\int_0^1|H_2(\theta)|^{2k}\,d\theta
\le \frac{(2k)!}{2^k}M^k.
\]

### Proof

Orthogonality counts two ordered \(k\)-tuples of unordered pairs with equal
endpoint sum. Rigidity forces equality of the total endpoint multiset. For a
fixed labelled \(2k\)-set, the number of ordered decompositions into \(k\)
unordered pairs is
\[
(2k-1)!!\,k!=\frac{(2k)!}{2^k}.
\]
There are \(M^k\) choices on the first side. \(\square\)

# 6. Sub-Weibull Lebesgue tails

## Theorem 6.1

For all sufficiently large \(X\) and \(s\ge2M\),
\[
\operatorname{meas}\{|H_2|^2\ge s\}
\le e^3(2s/M)^{1/4}\exp\!\left(-\sqrt{2s/M}\right).
\]
Consequently, for \(121M\le\lambda\le M^2\),
\[
\boxed{
\operatorname{meas}\{K\ge\lambda\}
\le \exp\!\left(-\sqrt{\lambda/M}\right).
}
\]

### Proof

Choose \(k=\lfloor\sqrt{s/(2M)}\rfloor\). Markov's inequality and Lemma 5.1 give
\[
\operatorname{meas}\{|H_2|^2\ge s\}
\le \frac{(2k)!}{2^k}\left(\frac Ms\right)^k.
\]
Stirling's inequality and the choice of \(k\) yield the displayed bound. The centred form follows by taking \(s=M+\lambda\) and checking the elementary one-variable inequality for \(\lambda/M\ge121\). \(\square\)

The exponent constant \(\sqrt2\) is sharp in the fixed-level limiting law: \(H_2/\sqrt M\) has the moments of \(g^2/\sqrt2\) to leading order, with \(g\) standard complex Gaussian.

# 7. Exact higher moments

Rigidity also makes fixed moments polynomial in \(N\). Exhaustive classification gives
\[
\int_0^1|H_2|^6\,d\theta
=
\frac{45N^6-189N^5+438N^4-597N^3+443N^2-136N}{4},
\]
and
\[
\int_0^1K^3\,d\theta
=
\frac{N(N-1)^2(37N^3-115N^2+174N-136)}4
=
74M^3(1+O(N^{-1})).
\]
More generally, for fixed \(k\),
\[
\int_0^1|H_2|^{2k}
=\frac{(2k)!}{4^k}N^{2k}(1+O_k(N^{-1})).
\]

# 8. The arithmetic transfer gap

Let \(\mu_{X,a}\) be the reciprocal prime-pair sampling measure. It is supported on \(X^{4+o(1)}\) atoms, each of mass at most \(X^{-4+o(1)}\). The target required by the reciprocal architecture is
\[
\mu_{X,a}\{K\ge\lambda\}
\ll \frac{M X^{o(1)}}{\lambda}.
\]

## Corollary 8.1

If this target fails at \(\lambda=tM\), \(121\le t\le M\), then at least
\[
X^{4+o(1)}t^{-1}
\]
sampling atoms lie in a set of Lebesgue measure at most
\[
e^{-\sqrt t}.
\]

The missing theorem is a sparse exceptional-set statement forbidding polynomially many arithmetic atoms from concentrating on exponentially small sets.

# 9. Truncated singular series at a primorial centre

Let
\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m)
\]
and
\[
\pi_{2,j}(H;d)=
\sum_{\substack{2\le m\\m+d\le H}}
\Lambda(P_j+m)\Lambda(P_j+m+d).
\]
For primes up to the block endpoint, the local pair factor is
\[
\frac{p(p-2)}{(p-1)^2}\quad(p\nmid d),\qquad
\frac{p}{p-1}\quad(p\mid d),
\]
and it vanishes for odd \(d\).

Let \(\mathfrak S_j(d)\) be the resulting truncated singular series and
\[
T_j(H)=\sum_{0<|d|<H}(H-|d|)(\mathfrak S_j(d)-1).
\]

## Theorem 9.1

Uniformly in the block,
\[
|T_j(H)|\le2H\log X
\]
for all sufficiently large \(X\).

The truncation at the block prime scale changes the natural logarithm from \(\log H\) to \(\log X\). This is the exact scale needed by the block variance argument.

# 10. A corrected conditional Hardy--Littlewood criterion

Assume the block-averaged hypotheses
\[
\sum_{j<N}\Psi_j(H)=NH+O(NH\varepsilon)
\tag{H1}
\]
and, uniformly for \(0<|d|<H\),
\[
\sum_{j<N}\pi_{2,j}(H;d)
=(H-|d|)\sum_{j<N}\mathfrak S_j(d)+O(NH\varepsilon).
\tag{H2}
\]

## Theorem 10.1

If
\[
\varepsilon=o(\log X/X),
\]
then
\[
\sum_{j<N}(\Psi_j(H)-H)^2
\le \bigl(2+O(\eta X\varepsilon)+o(1)\bigr)NHX.
\]
Hence the deterministic criterion from Paper II holds and Fortune's conjecture follows for all sufficiently large \(n\).

### Proof

Expand the variance. The diagonal satisfies
\[
\sum_j\sum_m\Lambda(P_j+m)^2
\le(2+o(1))NHX(1+O(\varepsilon)).
\]
For the off-diagonal, sum (H2) over \(d\). The constant part contributes \(N(H^2-H)\), while Theorem 9.1 contributes \(O(NH\log X)\). The total hypothesis error is \(O(NH^2\varepsilon)\). The \(NH^2\) main terms cancel, leaving
\[
\sum_jE_j(H)^2
\le(2+o(1))NHX+O(NH\log X)+O(NH^2\varepsilon).
\]
Divide by \(NHX\) and use \(H=\eta X^2\). \(\square\)

Neither (H1) nor (H2) alone forces a prime at every centre. Their block-averaged nature is essential; the earlier pointwise formulation was vacuously too strong.

# 11. Boundary and research direction

The unconditional kernel theory is much stronger than the required Lebesgue-level estimate. The conditional theorem shows exactly how accurate a block-averaged arithmetic model would have to be. Current technology gives neither the exceptional-set transfer nor (H1)--(H2) at the required strength.

The next integer problem is therefore a transference or derandomisation theorem, not another moment computation.

## AI-assistance disclosure

The research programme used large language models for structured literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. Every mathematical claim included as a theorem was checked against an explicit proof or an independently reproducible exact computation. Conjectural, conditional, computational, and negative results are labelled separately. The named author takes responsibility for the content, citations, code, and final presentation.

## Data, code, and reproducibility

The source record for this draft is the public repository `https://github.com/digitalgoldfisj79/multi-agent-environment` on branch `gpt56/d1-gate-bridge-terminal-20260724`. The Zenodo package accompanying this manuscript contains the manuscript source, compiled PDF, a claim-status ledger, a source-file manifest, machine-readable metadata, and checksums.


# Appendix A. Complete kernel-theory proof

This appendix reproduces the frozen proof source formerly issued as the Paper II addendum. Its `A.*` numbering is retained deliberately so that the circulation manuscript can be checked line by line against frozen blob `71a9ad70c7164bcd94b92743fff3d8088c9a158b`.

## A.1 Notation and the rigidity lemma

As in Paper II, Section 2, fix a large parameter \(X\), let
\(X\le\ell_1<\cdots<\ell_N<2X\) be the primes of the dyadic block, and let

\[
Q_0=1,\qquad Q_j=\prod_{u\le j}\ell_u,\qquad P_j=A_XQ_j,
\]

so that

\[
P_{j+1}=\ell_{j+1}P_j\ge XP_j
\qquad(0\le j<N-1).
\tag{A.1}
\]

Let \(\mathcal P_2=\{\{j,k\}:0\le j\le k<N\}\) (index pairs as multisets),
\(M=|\mathcal P_2|=N(N+1)/2\), \(S_{\{j,k\}}=P_j+P_k\), and

\[
H_2(\theta)=\sum_{u\in\mathcal P_2}e(\theta S_u),
\qquad
K(\theta)=|H_2(\theta)|^2-M.
\]

All constants below are absolute. The only structural input is (A.1).
Scope note: the dichotomy (Section A.2) holds verbatim for any
superincreasing sequence with ratio at least \(X\), of any length \(N\).
The tail theorem (Section A.3) additionally uses \(N\ll X\) — automatic in
the prime-block setting, where \(N\asymp X/\log X\) — since the optimal
moment order at top levels is \(k\asymp N\), which must stay below the
rigidity threshold \((X-1)/2\); for an arbitrary superincreasing sequence
with \(N\gtrsim X\), (A.10) holds only for \(\lambda\lesssim(X/N)^2M^2\)-type
restricted ranges.

**Lemma A.1 (\(B\)-rigidity).** Let \(B\ge1\) be an integer and suppose
\(X>B+1\). If \(c_0,\ldots,c_{N-1}\) are integers with \(|c_t|\le B\) and

\[
\sum_{t<N}c_tP_t=0,
\]

then every \(c_t=0\).

**Proof.** Suppose not, and let \(t\) be the largest index with
\(c_t\ne0\). By (A.1), \(P_i\le P_{t-1}X^{-(t-1-i)}\) for \(i\le t-1\), so

\[
\sum_{i<t}P_i\le P_{t-1}\sum_{s\ge0}X^{-s}
=P_{t-1}\frac X{X-1}\le\frac{P_t}{X-1}.
\]

Hence

\[
\Bigl|\sum_{i<t}c_iP_i\Bigr|\le\frac{B}{X-1}P_t<P_t\le|c_t|P_t,
\]

a contradiction. \(\square\)

Taking \(B=4\) recovers Paper II, Lemma 4.1 (four-copy rigidity) with the
explicit threshold \(X>5\); we use general \(B\) in Section A.3.

**Lemma A.2 (linkage of representations).** Let \(X>5\). If
\(u,v,u',v'\in\mathcal P_2\) satisfy \(S_u-S_v=S_{u'}-S_{v'}\), then

\[
u\uplus v'=u'\uplus v
\tag{A.2}
\]

as multisets of four indices, where \(\uplus\) denotes multiset union.

**Proof.** The relation \(S_u+S_{v'}=S_{u'}+S_v\) is an integer relation
\(\sum_tc_tP_t=0\) in which each coefficient is the multiplicity of \(t\) in
\(u\uplus v'\) minus its multiplicity in \(u'\uplus v\); hence
\(|c_t|\le4\). Lemma A.1 with \(B=4\) forces every \(c_t=0\), which is
(A.2). \(\square\)

## A.2 The difference-multiplicity dichotomy

For a nonzero integer \(D\) let

\[
r(D)=\#\{(u,v)\in\mathcal P_2^2:\ u\ne v,\ S_u-S_v=D\}.
\]

**Theorem A.3 (dichotomy).** Let \(X>5\). Then for every nonzero \(D\):

1. If \(D=P_i-P_k\) for some \(i\ne k\), then \(r(D)=N\), and the
   representations are exactly the *sliding family*

   \[
   (u,v)=\bigl(\{i,t\},\{k,t\}\bigr),\qquad t=0,1,\ldots,N-1.
   \tag{A.3}
   \]

2. Otherwise \(r(D)\le1\).

Moreover the values in case 1 are pairwise distinct, there are exactly
\(N(N-1)\) of them, and the number of ordered pairs \((u,v)\), \(u\ne v\),
whose difference is of the second kind is \(M(M-1)-N^2(N-1)\).

**Proof.** *Case 1: representations of \(D=P_i-P_k\).* Each pair in (A.3)
satisfies \(S_{\{i,t\}}-S_{\{k,t\}}=P_i-P_k\), the pairs are distinct for
distinct \(t\) (as unordered pairs), and \(u\ne v\) throughout since
\(i\ne k\). So \(r(D)\ge N\).

Conversely, let \((u',v')\) be any representation and apply Lemma A.2 to
the pair of representations \((\{i,i\},\{k,i\})\) — which lies in (A.3)
with \(t=i\) — and \((u',v')\):

\[
\{i,i\}\uplus v'=u'\uplus\{k,i\}.
\tag{A.4}
\]

The index \(k\) appears in the right side of (A.4); on the left it can
appear only inside \(v'\) (as \(k\ne i\)). So \(v'=\{k,t\}\) for some
\(t\), and then (A.4) gives \(u'=(\{i,i,k,t\})\setminus\{k,i\}=\{i,t\}\).
Thus \((u',v')\) lies in the family (A.3), and \(r(D)=N\).

*Case 2: all other differences.* Let \((u,v)\) be a representation of a
difference \(D\) not of the form \(P_i-P_k\). We first observe that the
multiset intersection \(u\cap v\) must be empty. Indeed, if \(u\) and \(v\)
share an index \(t\), write \(u=\{i,t\}\), \(v=\{k,t\}\); then
\(D=P_i-P_k\) with \(i\ne k\) (since \(u\ne v\) and \(D\neq0\)),
contradicting the case assumption.

So \(u=\{a,b\}\) and \(v=\{c,d\}\) with \(u\cap v=\varnothing\). Let
\((u',v')\) be any representation of the same \(D\). Lemma A.2 gives
\(u\uplus v'=u'\uplus v\). Each index of \(v\) appears in \(u'\uplus v\)
with its multiplicity in \(v\) plus possibly more; on the left side, since
\(u\cap v=\varnothing\), the indices of \(v\) can be supplied only by
\(v'\). As both \(v\) and \(v'\) are 2-multisets, this forces \(v'=v\), and
then \(u'=u\). Hence \(r(D)=1\).

*Counting.* The values \(P_i-P_k\) (\(i\ne k\)) are pairwise distinct and
nonzero by Lemma A.1 with \(B\le2\) (a coincidence
\(P_i-P_k=P_{i'}-P_{k'}\) is a relation with coefficients bounded by 2),
giving \(N(N-1)\) values of the first
kind, contributing \(N(N-1)\cdot N=N^2(N-1)\) ordered pairs. The total
number of ordered pairs with \(u\ne v\) is \(M(M-1)\); the remainder,
\(M(M-1)-N^2(N-1)\), consists of multiplicity-one differences. \(\square\)

*Validation.* At \(N=9\) the multiplicity histogram of the difference
multiset is exactly \(\{1:1332,\ 9:72\}\) with \(72=N(N-1)\) and
\(1332=M(M-1)-N^2(N-1)\), and the multiplicity-\(N\) representation sets
coincide with (A.3) element by element (`addendum_checks.py`, check 1).

**Corollary A.4 (exact two-scale energy decomposition).** Let \(X>5\).
For any function \(T\) on the nonzero integers (in particular
\(T=|\Psi_a|^2\) or \(T=|\Phi_X|^2\) of Paper II, Section 3),

\[
\sum_{\substack{u,v\in\mathcal P_2\\u\ne v}}T(S_u-S_v)
=
N\sum_{i\ne k}T(P_i-P_k)
+
\sum_{D\in\mathcal D_1}T(D),
\tag{A.5}
\]

where \(\mathcal D_1\) is the set of multiplicity-one differences,
\(|\mathcal D_1|=M(M-1)-N^2(N-1)\). In particular, with
\(\mathcal G_a=\sum_{i\ne k}|\Psi_a(P_i-P_k)|^2\),

\[
\boxed{
\mathcal E_a=N\,\mathcal G_a+\mathcal S_a,\qquad \mathcal S_a\ge0,
}
\tag{A.6}
\]

and therefore

\[
\mathcal E_a\le MX^{o(1)}
\quad\Longrightarrow\quad
\mathcal G_a\le \frac MN X^{o(1)}\ll NX^{o(1)}.
\tag{A.7}
\]

**Remark A.5.** (A.7) is a *necessary* condition inside the sufficient
architecture: any mechanism proposed for the pair-sum target (12.1) must in
particular control the single-walk energy \(\mathcal G_a\) — an object with
\(N^2\asymp X^2/\log^2X\) terms instead of \(M^2\asymp X^4/\log^4X\) — at
scale \(N\). This refines the endpoint-sector collapse recorded in the
archived phase reports into an exact multiplicity statement: there is no
intermediate multiplicity level between \(N\) and \(1\). Conversely (A.6)
splits the target (12.1) into the single-walk part, needed at scale
\(M/N\), and a multiplicity-free (Sidon-type) part, needed at scale \(M\).

## A.3 Moments and the sub-Weibull tail theorem

**Lemma A.6 (moment bound).** Let \(k\ge1\) be an integer with
\(X>2k+1\). Then

\[
\int_0^1|H_2(\theta)|^{2k}\,d\theta
\le
\frac{(2k)!}{2^k}\,M^k.
\tag{A.8}
\]

**Proof.** By orthogonality the integral counts tuples
\((u_1,\ldots,u_k,v_1,\ldots,v_k)\in\mathcal P_2^{2k}\) with
\(\sum_iS_{u_i}=\sum_iS_{v_i}\). Such a relation has integer coefficients
bounded by \(2k\) in absolute value, so Lemma A.1 (with \(B=2k\), legitimate
as \(X>2k+1\)) forces the multiset identity

\[
u_1\uplus\cdots\uplus u_k=v_1\uplus\cdots\uplus v_k=:W.
\]

There are \(M^k\) choices of \((u_1,\ldots,u_k)\). It remains to bound, for
a fixed \(2k\)-multiset \(W\), the number of ordered \(k\)-tuples of
unordered pairs whose union is \(W\), by \((2k)!/2^k\).

Fix a labelled set \(\widetilde W\) of \(2k\) elements together with a
projection \(\pi:\widetilde W\to\operatorname{supp}(W)\) whose fibre over
each index has size equal to its multiplicity in \(W\). Every decomposition
of the multiset \(W\) into an ordered tuple of pairs is the image under
\(\pi\) of at least one decomposition of the labelled set \(\widetilde W\)
(distribute the elements of each fibre among the pair-slots that the
multiset decomposition assigns to that index). Distinct multiset
decompositions have disjoint, nonempty sets of labelled preimages, so their
number is at most the number of decompositions of a labelled \(2k\)-set into
an ordered tuple of \(k\) unordered pairs, which is

\[
(2k-1)!!\cdot k!=\frac{(2k)!}{2^kk!}\cdot k!=\frac{(2k)!}{2^k}.
\]

This proves (A.8). \(\square\)

**Theorem A.7 (sub-Weibull Lebesgue tail).** There is an absolute constant
\(X_0\) such that for all \(X\ge X_0\) the following holds. For every real
\(s\ge2M\),

\[
\operatorname{meas}\{\theta\in[0,1):|H_2(\theta)|^2\ge s\}
\le
e^3\Bigl(\frac{2s}M\Bigr)^{1/4}
\exp\Bigl(-\sqrt{\tfrac{2s}M}\Bigr).
\tag{A.9}
\]

In particular, for every \(\lambda\) with \(121M\le\lambda\le M^2\),

\[
\boxed{
\operatorname{meas}\{\theta:K(\theta)\ge\lambda\}
\le
\exp\Bigl(-\sqrt{\lambda/M}\Bigr).
}
\tag{A.10}
\]

(For \(\lambda>M^2-M\) the level set is empty, since
\(\max K=M^2-M\).)

**Proof.** Fix \(s\ge2M\) and put \(k=\lfloor\sqrt{s/(2M)}\rfloor\ge1\).
Since \(k\le\sqrt{s/(2M)}\le\sqrt{(M^2+M)/(2M)}\ll N\ll X/\log X\), the
hypothesis \(X>2k+1\) of Lemma A.6 holds for all \(X\ge X_0\) with \(X_0\)
absolute, uniformly in \(s\) in the stated range. (For
\(s> M^2+M\ge\max|H_2|^2\) the set is empty and there is nothing to prove.)

Chebyshev's inequality and Lemma A.6 give

\[
\operatorname{meas}\{|H_2|^2\ge s\}
\le
s^{-k}\int_0^1|H_2|^{2k}
\le
\frac{(2k)!}{2^k}\Bigl(\frac Ms\Bigr)^k.
\]

Using \(n!\le e\,n^{n+1/2}e^{-n}\) with \(n=2k\),

\[
\frac{(2k)!}{2^k}\Bigl(\frac Ms\Bigr)^k
\le
e\sqrt{2k}\,\Bigl(\frac{2k^2M}{e^2s}\Bigr)^{k}.
\]

By the choice of \(k\), \(k^2\le s/(2M)\), so the bracket is at most
\(e^{-2}\), and \(2k\ge\sqrt{2s/M}-2\), whence

\[
\operatorname{meas}\{|H_2|^2\ge s\}
\le
e\sqrt{2k}\,e^{-2k}
\le
e^3\,(2s/M)^{1/4}\exp\bigl(-\sqrt{2s/M}\bigr),
\]

which is (A.9).

For (A.10), apply (A.9) with \(s=M+\lambda\) and set \(t=\lambda/M\ge121\).
It suffices that

\[
f(t):=3+\tfrac14\log\bigl(2(t+1)\bigr)-\sqrt{2(t+1)}+\sqrt t\le0
\quad\text{for }t\ge121.
\]

One computes \(f(121)=3+\tfrac14\log244-\sqrt{244}+11<-0.24\), and

\[
f'(t)=\frac1{4(t+1)}-\frac1{\sqrt{2(t+1)}}+\frac1{2\sqrt t}<0
\qquad(t\ge121),
\]

because \(1/(2\sqrt t)<1/\sqrt{2(t+1)}\) for \(t\ge2\) with margin
exceeding \(1/(4(t+1))\) for \(t\ge121\). Hence \(f\le f(121)<0\) on the
range, proving (A.10). \(\square\)

**Remark A.8 (sharpness at fixed levels).** The constant \(\sqrt2\) in
(A.9) cannot be improved *at fixed levels*, in the following iterated-limit
sense. The even moments of \(H_2/\sqrt M\) match those of \(g^2/\sqrt2\)
(\(g\) standard complex Gaussian) to leading order at every fixed order
(Remark A.9); the limit law \(|g|^4/2\) is moment-determinate (its \(k\)-th
moment \((2k)!/2^k\) satisfies Carleman's condition), so for each fixed
\(t>0\),
\(\operatorname{meas}\{K\ge tM\}\to
\Pr\bigl(|g|^2\ge\sqrt{2(t+1)}\bigr)=\exp(-\sqrt{2(t+1)})\)
as \(X\to\infty\). Hence no bound of the form
\(\exp(-c\sqrt{\lambda/M})\) with \(c>\sqrt2\) can hold uniformly at fixed
levels. Sharpness *uniformly over the whole range* \(\lambda\le M^2\)
(the moderate/large-deviation regime) is **not** claimed and would require
a separate argument. Empirically (check 4) the ratio
\(-\log\operatorname{meas}/\sqrt{\lambda/M}\) is stable near \(1.5\) at
\(N=24\) for \(\lambda/M\in[2,64]\), consistent with \(\sqrt2\) plus
finite-size corrections; the measured tail respects (A.9) at every level.

**Remark A.9 (exact sixth moment).** The moment method also yields exact
formulas. By Lemma A.1 with \(B=6\) (valid for \(X>7\)), the sixth-moment
count \(\int_0^1|H_2|^6\) equals
\(\sum_\tau c_\tau(N)d_\tau^2\), where \(\tau\) runs over the partitions of
\(6\), \(d_\tau\) is the (constant) number of ordered triples of unordered
pairs realizing a fixed endpoint multiset of type \(\tau\), and
\(c_\tau(N)\), the number of index multisets of type \(\tau\), is a
polynomial in \(N\) of degree equal to the number of **parts** of
\(\tau\) — equivalently, of distinct endpoint labels: for \(\tau\) with
\(\ell\) parts and part-size multiplicities \(m_r\),
\(c_\tau(N)=N(N-1)\cdots(N-\ell+1)/\prod_r m_r!\) — vanishing at the
integers below \(\ell\). (Note: *parts*, not distinct part-sizes; e.g.
\(\tau=(3,3)\) has \(\ell=2\) and contributes degree 2.) Hence the count is a
single polynomial in \(N\) of degree at most \(6\), valid for all
\(N\ge0\); it is therefore determined by its values at seven points.
Exhaustive counting at \(N=2,\ldots,9\) (eight points) with verification at
the held-out points \(N=10,11\) gives

\[
\int_0^1|H_2(\theta)|^6\,d\theta
=
\frac{45N^6-189N^5+438N^4-597N^3+443N^2-136N}4,
\tag{A.11}
\]

and, combining with Paper II, Theorem 4.2 and \(\int|H_2|^2=M\),

\[
\int_0^1K(\theta)^3\,d\theta
=
\frac{N(N-1)^2\,(37N^3-115N^2+174N-136)}4
=
74M^3\bigl(1+O(N^{-1})\bigr).
\tag{A.12}
\]

The leading coefficients \(45/4=6!/4^3\) and \(74\) equal the
half-squared-Gaussian model values, extending the pattern
\(5M^2\) of Paper II, Theorem 4.2 to the third cumulant. The general law
\(\int|H_2|^{2k}=\bigl((2k)!/4^k\bigr)N^{2k}(1+O_k(N^{-1}))\) follows from
the same classification for every fixed \(k\) with \(X>2k+1\).

## A.4 Consequence for the level-set target

**Corollary A.10 (transfer gap).** Let \(\mu_{X,a}\) be the reciprocal
prime-pair measure of Paper II, Proposition 4.3, supported on at most
\(\pi(2H)^2=X^{4+o(1)}\) atoms of mass at most \(X^{-4+o(1)}\) each. If the
level-set target (4.5) fails at a level \(\lambda=tM\) with
\(121\le t\le M\), then at least

\[
X^{4+o(1)}\,t^{-1}
\]

atoms of \(\mu_{X,a}\) lie in a set of Lebesgue measure at most
\(\exp(-\sqrt t)\).

**Proof.** Immediate from (A.10), the target
\(\mu\{K\ge\lambda\}\ll MX^{o(1)}/\lambda\), and the atom bounds. \(\square\)

Thus the outstanding statement is not a transfer of the Lebesgue bound but
a far weaker sparse exceptional-set property: the arithmetic sampling
points must merely fail to concentrate, with density \(t^{-1}X^{o(1)}\), on
sets whose Lebesgue measure is exponentially small in \(\sqrt t\). The
allowed overshoot of \(\mu_{X,a}\) relative to Lebesgue measure at level
\(tM\) is a factor \(e^{\sqrt t}\,t^{-1}X^{o(1)}\). No mechanism for
proving such a bound is proposed here.

## A.5 Validation summary

`addendum_checks.py` performs:

1. **Dichotomy** (Theorem A.3): at \(N=8,9\), the difference-multiplicity
   histogram is exactly \(\{1:M(M-1)-N^2(N-1),\ N:N(N-1)\}\), and the
   representation set of every multiplicity-\(N\) difference equals the
   sliding family (A.3) element by element.
2. **Moment bound** (Lemma A.6): exact collision counts at
   \(k=2,3,4\), \(N\le9\) satisfy (A.8).
3. **Exact moments** (Remark A.9): (A.11) reproduces exhaustive counts at
   \(N=2,\ldots,11\) and (A.12) at \(N=3,5,7\).
4. **Tail bound** (Theorem A.7): with exact modular phase arithmetic at
   \(N=24\) (200{,}000 samples), the empirical tail respects (A.9) at every
   measurable level \(\lambda/M\in\{2,4,8,16,32,64\}\), and the empirical
   exponent constant is \(\approx1.5\), consistent with Remark A.8.

# Appendix B. Truncated singular-series proof

The sharp Dickman constant discussed below is explicitly a non-load-bearing sketch. The exact divisor identity and the bound `|T_j(H)| <= 2H log X` are the proved inputs used by the conditional theorem.

## B.1 The truncated singular series (Lemma 1 — proved)

**Lemma B.1.** For the pair (P_j + m, P_j + m + d), the Hardy-Littlewood local factor at a prime p <= ell_j (i.e. p | A) is

- delta_p(d) = p(p-2)/(p-1)^2 if p does not divide d,
- delta_p(d) = p/(p-1) if p | d.

In particular delta_2(d) = 0 for odd d and 2 for even d (the formula p(p-2)/(p-1)^2 handles p = 2 automatically). Define the **truncated singular series**

S_j(d) = prod_{p <= ell_j} delta_p(d) = [d even] * 2 * prod_{2<p<=ell_j} (1 - 1/(p-1)^2) * prod_{2<p<=ell_j, p|d} (p-1)/(p-2).

For p > ell_j the local factors have the same classical form. No uniform estimate for the omitted infinite tail is claimed or used; the conditional theorem is formulated for the finite truncated product S_j(d).

*Proof.* The local factor is (number of admissible residues m mod p) * (p/(p-1))^2 / p, the (p/(p-1))^2 being the Lambda-normalisation of the two prime conditions. For p | A: P_j == 0 (mod p), so the excluded residues are m == 0 and m == -d (mod p). If p does not divide d these are distinct: p-2 admissible residues, factor (p-2)/p * p^2/(p-1)^2 = p(p-2)/(p-1)^2. If p | d they coincide: p-1 admissible residues, factor (p-1)/p * p^2/(p-1)^2 = p/(p-1). At p = 2 with d odd both residues are excluded and the factor is 0 (S_j(d) = 0 for odd d — correct: P_j + m prime forces m odd, so m and m+d cannot both be odd). For p > ell_j (p does not divide A) the excluded residues are -P_j and -P_j - d; the count is again p-1 or p-2 according to p | d, **independently of the value of P_j mod p** — so the tail factors coincide with the classical ones. QED

Remark (important bookkeeping fact): the conditioning at the primes p | A does not change the numerical *values* of the local factors relative to the classical singular series — it makes them exact local densities instead of heuristic averages. The truncation, not the conditioning, is what alters the second moment below.

The equivalent forms used later (all proved by direct multiplication): with lambda_p(d) := delta_p(d) - 1 = -1/(p-1)^2 + [p|d] * p/(p-1)^2,

S_j(d) - 1 = sum_{r | A, r > 1} prod_{p|r} lambda_p(d) = sum_{r | A, r>1} (1/phi(r)^2) sum_{s | r} mu(r/s) s [s | d].   (1.1)

---

## B.2 Exact second-moment identity (Lemma 2 — proved; validated in exact arithmetic)

Let H >= 2 be an integer and

T_j(H) := sum_{0 < |d| < H} (H - |d|)(S_j(d) - 1) = 2 sum_{0<d<H} (H-d)(S_j(d)-1).

For s >= 1 put W(s) = sum_{0<d<H, s|d} (H-d); so W(s) = 0 for s >= H, and for 1 <= s < H, writing rho = H mod s,

W(s) = H^2/(2s) - H/2 + E(s),   E(s) = (rho/2)(1 - rho/s),   0 <= E(s) <= s/8.   (2.1)

**Lemma B.2 (exact divisor identity).**

T_j(H) = -H(H-1) + 4 C_j * sum_{u | A', 2u < H} W(2u)/phi2(u).   (2.2)

*Proof.* Insert (1.1), swap the finite sums, and regroup by s: T_j(H) = 2 sum_{s | A} c_s W(s) with c_s = sum_{r: s|r|A, r>1} mu(r/s) s / phi(r)^2. For s = 1: c_1 = prod_{p|A}(1 - 1/(p-1)^2) - 1 = -1, because the p = 2 factor vanishes. For s > 1: c_s = (s/phi(s)^2) prod_{p | A/s} (1 - 1/(p-1)^2), which vanishes unless s is even (else 2 | A/s kills the product). For s = 2u, u | A' odd squarefree: prod_{p|u}(1-1/(p-1)^2) = u phi2(u)/phi(u)^2 and phi(2u) = phi(u) give c_{2u} = 2 C_j / phi2(u). Since W(1) = H(H-1)/2, (2.2) follows. QED

Hand check (P = {2,3}, H = 5): direct sum T = -8; identity: C_j = 3/4, only u = 1 has 2u < 5, W(2) = 4, T = -20 + 12 = -8. Machine check: exact rational match at four configurations (Section 4).

---

## B.3 The second-moment bound (Lemma 3 — main term proved; sharp constant provable-sketch)

**Lemma B.3 (proved bound).** With beta_j(H) := 2 C_j sum_{u | A', u < H/2} 1/phi2(u),

T_j(H) = -beta_j(H) * H + O(H),   (3.1)

with an absolute implied constant, and

2 C_2 <= beta_j(H) <= 2 C_j * prod_{2<p<=ell_j} (p-1)/(p-2) = prod_{p<=ell_j} p/(p-1) = (e^gamma + o(1)) log ell_j.   (3.2)

Consequently T_j(H) < 0 for large H and

|T_j(H)| <= (e^gamma + o(1)) H log ell_j <= 2 H log X for all large X, uniformly in j.   (3.3)

*Proof.* Insert (2.1) into (2.2). Three exact cancellations/bounds:

(a) **The H^2 terms cancel exactly** by the Euler-product identity C_j * sum_{u|A'} 1/(u phi2(u)) = prod_{2<p<=ell_j} [p(p-2)/(p-1)^2] * [(p-1)^2/(p(p-2))] = 1 (this is the statement that the truncated singular series has exact average 1 against the full divisor sum). What survives of the H^2 terms is -H(H-1) + H^2 - H^2 C_j sum_{u >= H/2} 1/(u phi2(u)) = H - H^2 C_j * (tail).

(b) **Tail bound.** Write f(u) = u/phi2(u) = sum_{b|u} h(b) with h multiplicative, squarefree-supported, h(p) = 2/(p-2) >= 0; note h(b) <= 2 for every b (only the p = 3 factor exceeds 1). Then for V >= 1, sum_{u odd squarefree, u >= V} 1/(u phi2(u)) = sum_{u>=V} f(u)/u^2 <= sum_{b<=V} (h(b)/b^2) * (4b/V) + 2 sum_{b>V} h(b)/b^2 <= (4/V) prod_{2<p}(1 + 2/(p(p-2))) + 8/V = O(1/V). With V = H/2 the tail term in (a) is O(H).

(c) **E-term.** 0 <= 4 C_j sum_{2u<H} E(2u)/phi2(u) <= C_j sum_{u <= H/2} f(u) <= sum_{b} h(b) (H/2)/b = O(H), using h >= 0 and sum h(b)/b = prod(1 + 2/(p(p-2))) < infinity.

Combining gives (3.1). For (3.2): the lower bound is the u = 1 term (C_j > C_2); the upper bound is the full divisor sum, telescoping to prod_{p<=ell_j} p/(p-1), which is (e^gamma+o(1)) log ell_j by Mertens. QED

**Remark B.4 (sharp constant — non-load-bearing sketch).** Let theta_j = log H / log ell_j and I(theta) = int_0^theta rho(v) dv with rho the Dickman function (I(2) = 3 - 2 log 2 = 1.61370...; I(infinity) = e^gamma). Then

T_j(H) = -I(theta_j) * H * log ell_j * (1 + o(1)),

and in the Paper II regime H = eta X^2 (theta_j -> 2, log ell_j = (1+o(1)) log X uniformly in j):

**T_j(H) = -(3 - 2 log 2)(1 + o(1)) * H * log X.**

*Sketch.* beta_j(H) is a 1/phi2-weighted count of the ell_j-smooth odd squarefree integers below H/2. The weight 1/phi2(u) = f(u)/u with f = 1*h, h(b) <= 2, sum h(b)/b < infinity, reduces the truncated sum to sum_{a <= y, a ell-smooth} 1/a, whose asymptotic kappa * log(ell) * int_0^{log y/log ell} rho(v) dv follows from de Bruijn's Psi(x,y) ~ x rho(u) by partial summation (standard smooth-number theory; Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Part III — statement standard, not re-verified line-by-line here, hence sketch status). The multiplicative constants recombine against the total mass (3.2) = (e^gamma+o(1)) log ell_j together with int_0^infinity rho = e^gamma, giving beta_j = I(theta_j) log ell_j (1+o(1)). Numerical support: Section 4 (ratios 0.88-0.96 at ell = 29..97, improving with size). *Status: provable-sketch; NOT used in the conditional theorem, which needs only the proved (3.3).*

---

# Appendix C. Corrected conditional Hardy--Littlewood theorem

This appendix reproduces the corrected block-averaged theorem from frozen blob `41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef`. It supersedes the earlier pointwise formulation, which was vacuously strong.

## C.1 Block-averaged conditional criterion

Let \(\varepsilon=\varepsilon(X)\ge0\). Assume, for all sufficiently
large \(X\):

**(H1) block-averaged first moment.**
\[
\sum_{j<N}\Psi_j(H)=NH+O(NH\varepsilon).
\]

**(H2) block-averaged pair correlation, uniformly in the shift.** For
every \(0<|d|<H\),
\[
\sum_{j<N}\pi_{2,j}(H;d)
=(H-|d|)\sum_{j<N}\mathfrak S_j(d)+O(NH\varepsilon).
\]

If \(\varepsilon(X)=o(\log X/X)\), then Paper II hypothesis (2.7) holds
with
\[
L(X)\;\le\;2+O(\eta X\varepsilon)+o(1)\;=\;o(\log X),
\]
and consequently, by Paper II Theorem 2.4, every centre in the block
contains a prime in \([P_j+2,P_j+H]\) for all large \(X\); Fortune's
conjecture holds for all sufficiently large \(n\).

Neither (H1) nor (H2) individually implies the conclusion trivially:
(H1) controls only the block *mean* of the \(E_j\), and (H2) controls
correlations on average over the block — a single centre may a priori
fail while the averages hold, and it is exactly the variance mechanism of
Theorem 2.4 that excludes this.

### Proof

Expand the block variance:
\[
\sum_{j<N}E_j(H)^2
=\sum_j\Psi_j^2-2H\sum_j\Psi_j+NH^2.
\tag{1}
\]

**Diagonal.** \(\Psi_j^2=\sum_m\Lambda(P_j+m)^2
+\sum_{m\ne m'}\Lambda(P_j+m)\Lambda(P_j+m')\). Since
\(\Lambda(P_j+m)\le\log(P_j+H)\le(1+o(1))\,2X\) uniformly in the block
(\(\log P_j\le\vartheta(2X)(1+o(1))\)),
\[
\sum_j\sum_m\Lambda(P_j+m)^2
\le(1+o(1))\,2X\sum_j\Psi_j(H)
\overset{\text{(H1)}}{=}(2+o(1))NHX\,(1+O(\varepsilon)).
\tag{2}
\]

**Off-diagonal.** The \(m\ne m'\) part regroups by \(d=m'-m\):
\(\sum_{m\ne m'}\Lambda\Lambda=\sum_{0<|d|<H}\pi_{2,j}(H;d)\) up to the
boundary convention absorbed in (H2)'s error. Summing (H2) over the
\(2(H-1)\) values of \(d\):
\[
\sum_j\sum_{m\ne m'}\Lambda\Lambda
=\sum_{0<|d|<H}(H-|d|)\sum_j\mathfrak S_j(d)+O(NH^2\varepsilon).
\tag{3}
\]
Write \(\mathfrak S_j=1+(\mathfrak S_j-1)\). The 1-part contributes
\(N\sum_{0<|d|<H}(H-|d|)=N(H^2-H)\). The remainder is
\(\sum_jT_j(H)\) with
\(T_j(H)=\sum_{0<|d|<H}(H-|d|)(\mathfrak S_j(d)-1)\), and the **proved
truncated-singular-series lemma** gives \(|T_j(H)|\le2H\log X\) for all
large \(X\), uniformly in \(j\). Hence
\[
\sum_j\sum_{m\ne m'}\Lambda\Lambda
=N(H^2-H)+O(NH\log X)+O(NH^2\varepsilon).
\tag{4}
\]

**Assembly.** By (H1), \(-2H\sum_j\Psi_j=-2NH^2+O(NH^2\varepsilon)\).
Adding (2), (4), \(-2NH^2+O(NH^2\varepsilon)\), and \(NH^2\) in (1):
\[
\sum_{j<N}E_j(H)^2
\le(2+o(1))NHX
+O(NH\log X)+O(NH^2\varepsilon)-NH.
\]
Dividing by \(NHX\) and using \(H=\eta X^2\):
\[
L(X)\le 2+o(1)+O\!\left(\frac{\log X}{X}\right)+O(\eta X\varepsilon)
=2+O(\eta X\varepsilon)+o(1).
\]
With \(\varepsilon=o(\log X/X)\) this is \(o(\log X)\), so (2.7) holds
and Theorem 2.4 applies. Coverage of every \(n\) by dyadic blocks is as
in Paper II. \(\square\)

## C.2 Remarks

1. **Where each ingredient is load-bearing.** The diagonal (2) needs only
   (H1) and saturates the budget at \(L\approx2\); the constant 2 is the
   block-maximal \(\log P_j/X\le2+o(1)\) and could be refined to
   \(\int\)-averaged form. The off-diagonal needs (H2) *and* the
   singular-series bound \(|T_j|\le2H\log X\): without the latter, (4)
   would carry an uncontrolled \(N\cdot O(H\cdot?)\) term. This is
   exactly the role the truncated-series lemma was built for, restoring
   the intended content of the conditional bridge.
2. **The threshold is genuinely \(\varepsilon=o(\log X/X)\).** At
   \(\varepsilon\asymp\log X/X\) the term \(O(\eta X\varepsilon)\) is
   \(O(\log X)\) and (2.7) fails to improve on trivial; below it, the
   criterion closes. Unlike the superseded pointwise version, no
   sub-hypothesis here forces the conclusion by itself.
3. **Explicit-constant variant.** If (H1)–(H2) are assumed with a named
   constant \(C_0\) (error \(\le C_0NH\varepsilon\)), the argument gives
   the numerical threshold
   \(L\le2+2C_0\eta X\varepsilon+o(1)\), which combined with the
   explicit-margin form of Theorem 2.4
   (\(L\le(\eta/4C-\epsilon)\log X\) suffices) yields fully effective
   statements; with anonymous \(\ll\)-constants only the asymptotic form
   above is available.
4. **What this does not do.** (H1)–(H2) at the required strength are far
   beyond current technology, unconditionally or on GRH, for these
   exponentially sparse prescribed centres; the theorem is a calibration
   of the conditional boundary, not progress toward it.


# References