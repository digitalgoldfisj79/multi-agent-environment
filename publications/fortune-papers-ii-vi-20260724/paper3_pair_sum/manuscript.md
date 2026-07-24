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

# References

1. E. S. A. Bozzard, *Prime Detection at Primorial Centres*, Paper II.
2. G. H. Hardy and J. E. Littlewood, *Some problems of Partitio Numerorum*.
3. Standard references on additive energy, moment methods, and Barban--Davenport--Halberstam theory.
