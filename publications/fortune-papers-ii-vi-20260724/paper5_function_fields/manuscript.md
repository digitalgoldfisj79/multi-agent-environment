---
title: |
  Fortunate Polynomials over Finite Fields
subtitle: |
  General degree barriers, exact \(d=1\) reductions, and an open geometric crown
author:
  - "Edward Stewart Anthony Bozzard"
date: "24 July 2026"
lang: en-GB
abstract: |
  We formulate a function-field analogue of Fortune's conjecture. For the
  polynomial primorial \(P_d\), the least nonconstant offset producing an
  irreducible polynomial is forced to be irreducible whenever an irreducible
  value occurs below degree \(2d+2\). This gives an exact analogue of the
  integer square barrier.

  We establish a general Weil-Riemann-hypothesis window for the degree of the
  least offset and develop the prime-field case \(d=1\) in detail. For
  \(P_1=T^p-T\), degree-one offsets never work and the full conjecture reduces to
  irreducible sparse polynomials with quadratic or cubic tails. We prove an
  exact incidence identity, affine-orbit formulas, a quantised
  Kloosterman-type identity, and a complete irreducibility ledger. The
  conjecture is machine-certified for every odd prime below 1200. The quadratic
  subfamily fails for a positive proportion of tested primes, and the general
  problem is reduced to a precise growing-dimension cancellation or
  characteristic-boundary geometric theorem. No general proof is claimed.
keywords: ["function fields", "irreducible polynomials", "Fortune's conjecture", "Artin--Schreier", "Kloosterman sums", "finite fields"]
---

# 1. Polynomial primorials and Fortunate offsets

Let \(\mathbf F_q[T]\) be a polynomial ring. Define
\[
P_d=\prod_{\substack{f\ \text{monic irreducible}\\ \deg f\le d}}f
\]
and let \(F(q,d)\) be the nonconstant polynomial of least degree, with a fixed
lexicographic tie-break, such that \(P_d+F(q,d)\) is irreducible.

## Proposition 1.1 (degree barrier)

If \(m\) is reducible and coprime to \(P_d\), then
\[
\deg m\ge2d+2.
\]
Consequently, an irreducible value \(P_d+m\) with
\(\deg m\le2d+1\) forces \(F(q,d)\) to be irreducible.

### Proof

Every irreducible factor of \(m\) is absent from \(P_d\), so its degree is at
least \(d+1\). A reducible \(m\) has at least two such factors. \(\square\)

# 2. A general Weil-RH window

Let \(n=\deg P_d\sim q^d\). Standard prime-polynomial estimates imply that
there are irreducible polynomials in sufficiently long affine coefficient
slices around a fixed monic centre. Tracking the error uniformly in the
centre degree yields the following window statement.

## Theorem 2.1 (Fortunate window)

For fixed \(q\) and all sufficiently large \(d\), \(F(q,d)\) exists and is
either irreducible or satisfies
\[
2d+2\le \deg F(q,d)
\le \frac n2+2\log_qn+O_q(1).
\]

The proof uses the polynomial Riemann hypothesis to compare the number of
monic irreducibles in the available coefficient box with the contribution of
proper factors. The significance is qualitative: in function fields an
unconditional exponent-\(1/2\) window is available, while the full
Fortune-scale window remains coupled to the growing centre degree.

The detailed constant ledger is included in the supplement. The theorem is
separate from the \(d=1\) crown below.

# 3. The \(d=1\) target

For a prime \(p\),
\[
P_1=T^p-T.
\]
No degree-one offset works: \(T^p-T+\alpha T+\beta\) has an
\(\mathbf F_p\)-rational root because the associated additive-affine map is
surjective in the relevant cases.

Hence the \(d=1\) Fortune statement is equivalent to finding an irreducible
polynomial
\[
T^p+aT^3+bT^2+cT+d,\qquad (a,b)\ne(0,0).
\]
A minimal offset of degree two or three is automatically irreducible by the
degree barrier.

# 4. Master incidence identity

Let \(Q=p^p\). A degree-\(p\) polynomial over \(\mathbf F_p\) has roots in
\(\mathbf F_Q\) of degree one or \(p\). Counting root incidences gives
\[
p\,\#\mathrm{irred}_4=C-p^4,
\]
where \(C\) counts
\[
(\theta,a,b,c)\in\mathbf F_Q\times\mathbf F_p^3
\]
such that
\[
\theta^p+a\theta^3+b\theta^2+c\theta\in\mathbf F_p.
\]
The wild term linearises under trace:
\[
\operatorname{Tr}(t\theta^p)
=
\operatorname{Tr}(t^{1/p}\theta).
\]
Thus \(C\) has an exact character expansion in complete cubic Weil sums.

# 5. Affine orbit structure

The affine group \(T\mapsto\lambda T+\alpha\) preserves irreducibility and
acts on the sparse family. Fortune-relevant orbits have trivial stabiliser.

For the quadratic slice,
\[
\#\mathrm{irred}_2=p(p-1)N(p)+(p-1),
\]
where
\[
N(p)=\#\{d:T^p+T^2+d\ \text{irreducible}\}.
\]
The final term is the excluded Artin--Schreier orbit. An involution acts
freely on the nonzero cubic slices, giving the divisibility
\[
2p\mid\#\mathrm{irred}_a.
\]

# 6. Quantised Kloosterman identity

Let \(\eta\) be the quadratic character of \(\mathbf F_Q\) and \(G_Q\) its
Gauss sum. Exact orthogonality gives
\[
N(p)=p^{-p}G_QS(p),
\]
where
\[
S(p)=
\sum_{\tau\in\ker\operatorname{Tr}\setminus\{0\}}
\eta(\tau)
e_p\!\left(-\frac14\operatorname{Tr}(\tau^{2-p})\right).
\]
The hyperplane pieces satisfy
\[
T_u=\eta(-1)G_Q(R(u)-1),
\]
with \(R(u)\in\{0,1,2,p\}\) the root count of \(x^p+x^2+u\).
Consequently
\[
S(p)=\eta(-1)G_QN(p).
\]

The twisted sum is quantised on an exact Gauss-sum lattice. Analytic
estimation alone cannot decide whether \(N(p)\) vanishes.

# 7. Exact cubic ledger

The full count has the form
\[
\#\mathrm{irred}_4
=(p-1)+p(p-1)N(p)
+(p-1)(p^2-p^{3-p})
+p^{2-p}\sum_{a\ne0}R_a,
\]
where \(R_a\) is an explicit incidence character sum over
\[
V_t=\{\theta:
\operatorname{Tr}(t\theta)=
\operatorname{Tr}(t\theta^2)=0\}.
\]
The cardinality of \(V_t\) is exactly \(p^{p-2}\), and the nonzero slices
depend only on the quadratic class of \(a\).

A sufficient condition is
\[
\left|\sum_{a\ne0}R_a\right|<(p-1)(p^p-p).
\tag{L}
\]
Finite data place the aggregate comfortably inside this threshold, but no
uniform proof is known.

# 8. Local rootlessness and the singular-series constant

For \(x\in\mathbf F_p\), the wild term satisfies \(x^p=x\), so a family member
equals its cubic tail at \(x\). Therefore the linear-factor structure is
exactly the root structure of the tail. The number of rootless \((c,d)\)
pairs in a fixed slice is
\[
\frac{p^2-1}{3}.
\]
This deterministic local factor explains the observed positive density of
irreducible fibres and yields the leading singular-series constant.

# 9. Exact certification and negative results

The \(d=1\) statement has been machine-certified for every odd prime
\(p<1200\), using quadratic witnesses where available and explicit cubic
witnesses otherwise.

The quadratic family cannot prove the theorem: \(N(p)=0\) first occurs at
\(p=31\) and occurs for roughly one quarter of tested primes. There is no
stable congruence or standard residue-symbol classification.

Direct Cauchy--Schwarz and complete averaging are circular: they reconstruct
the unknown count or return the trivial square-root scale with no aggregate
saving. General complexity bounds are exponential in the dimension or
degree and miss the required polynomial constant.

# 10. The \(p\equiv2\pmod3\) half-sector

For \(K=\mathbf F_{p^p}\), let
\[
H=\ker\operatorname{Tr}
\]
and
\[
T_p=\sum_{x\in H}\psi(\operatorname{Tr}(x^3)).
\]
When \(p\equiv2\pmod3\), cubing permutes \(\mathbf F_p^\times\). The cubic
fibre deviations satisfy
\[
D_b=-T_p/p\quad(b\ne0),\qquad
D_0=(p-1)T_p/p.
\]
Thus the full nonzero-fibre nonuniformity is one integer per prime.

The analytic candidate theorem is
\[
|T_p|\le Cp^{(p-1)/2}.
\]
Its Airy-sheaf formulation and exact low-rank spectra are developed in the
companion paper. A separate object-level comparison is still required to
transport that estimate into ledger (L).

# 11. Open crown

The full \(d=1\) theorem remains open for two independent reasons.

1. A global characteristic-boundary Frobenius-correlation estimate must
   control \(T_p\) with an absolute constant.
2. An application theorem must identify the Airy boundary object with the
   load-bearing component of the irreducibility ledger, including punctual,
   Tate, Artin--Schreier and boundary terms.

The finite certification, exact reductions and quantised identities are
unconditional. They define a new function-field Fortune programme but do not
complete it.

## AI-assistance disclosure

The research programme used large language models for structured literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. Every mathematical claim included as a theorem was checked against an explicit proof or an independently reproducible exact computation. Conjectural, conditional, computational, and negative results are labelled separately. The named author takes responsibility for the content, citations, code, and final presentation.

## Data, code, and reproducibility

The source record for this draft is the public repository `https://github.com/digitalgoldfisj79/multi-agent-environment` on branch `gpt56/d1-gate-bridge-terminal-20260724`. The Zenodo package accompanying this manuscript contains the manuscript source, compiled PDF, a claim-status ledger, a source-file manifest, machine-readable metadata, and checksums. Repository paths and frozen commit identifiers are listed in `SUPPORTING_MATERIALS_MANIFEST.tsv`.

# References

1. Standard references on prime polynomials and the Weil Riemann hypothesis.
2. L. Bary-Soroker and collaborators on short intervals in function fields.
3. W. Sawin on interval varieties and prescribed coefficients.
4. C. D. Haessig and A. Rojas-León on symmetric powers of Airy families.
