---
title: |
  Prime Detection at Primorial Centres
subtitle: |
  Reciprocal frames, exact moments, and structural obstructions — revised draft
author:
  - "Edward Stewart Anthony Bozzard"
date: "24 July 2026"
lang: en-GB
abstract: |
  We develop a reciprocal-frame architecture for detecting primes immediately
  to the right of primorial centres. The starting observation is elementary:
  if the least offset producing a prime is composite, then all of its prime
  factors exceed the last prime in the primorial, so the offset is at least the
  square of the next prime. It is therefore enough to detect a prime in a
  quadratic-length interval after every sufficiently large primorial.

  The paper converts this question into a sequence of exact harmonic and
  combinatorial statements. We prove a deterministic block-variance criterion,
  construct the reciprocal sampling frame, compute the exact fourth moment of
  the pair-sum kernel, establish a growing-degree Möbius truncation, identify a
  semiprime resonance obstruction, and prove an exact character-ratio collapse.
  The analysis isolates a single missing transference estimate rather than
  claiming a proof of Fortune's conjecture. This revision adds the previously
  external pair-lift and principal-cancellation reduction, reconciles the
  validation record with the shipped code, and makes the epistemic status of
  every result explicit.
keywords: ["Fortune's conjecture", "primorials", "prime detection", "reciprocal frames", "exponential sums", "exact moments", "Möbius inversion"]
---

# 1. Introduction

Let \(p_n\) be the \(n\)-th prime and \(P_n=p_n\#\). Define \(F_n\) to be
the least integer \(m>1\) for which \(P_n+m\) is prime. Every prime factor of
\(F_n\) exceeds \(p_n\). Consequently, if \(F_n\) is composite then
\[
F_n\ge p_{n+1}^2.
\]
Thus Fortune's conjecture follows once every sufficiently large primorial has
a prime in an interval of length strictly below \(p_{n+1}^2\).

We organise the primorials into dyadic blocks. Let
\[
X\le \ell_1<\cdots<\ell_K<2X
\]
be the primes in the block, let
\[
A_X=\prod_{p<X}p,\qquad Q_j=\prod_{u\le j}\ell_u,\qquad P_j=A_XQ_j,
\]
and put \(H=\eta X^2\), where \(0<\eta<1\) is fixed. The block contains
\(N=K+1\asymp X/\log X\) centres.

The central object is
\[
E_j(H)=\sum_{2\le m\le H}\bigl(\Lambda(P_j+m)-1\bigr).
\]
A prime-detection theorem will follow if the block mean square of \(E_j(H)\)
is \(o(NH^2)\) with a sufficiently strong explicit margin.

This paper does not prove the required mean-square estimate. Its purpose is
to reduce the problem exactly, compute the algebraic and Lebesgue pieces, and
show why the surviving arithmetic transfer is genuinely new.

# 2. A deterministic prime-detection criterion

## Theorem 2.1 (block variance criterion)

Assume that, for every sufficiently large dyadic block,
\[
\sum_{j<N}E_j(H)^2\le L(X)\,NHX
\]
with \(L(X)=o(\log X)\). Then every centre in the block contains a prime in
\([P_j+2,P_j+H]\), and Fortune's conjecture holds for all sufficiently large
\(n\).

### Proof

Suppose a centre contains no prime in the interval. Prime powers contribute
\(o(H)\) uniformly because \(H\) is polynomial in \(X\) while \(P_j\) is
exponential in \(X\). Hence
\[
\sum_{2\le m\le H}\Lambda(P_j+m)=o(H)
\]
and \(E_j(H)=-(1+o(1))H\). One failed centre therefore contributes
\((1+o(1))H^2\) to the block variance. Since \(N\asymp X/\log X\) and
\(H=\eta X^2\),
\[
LNHX=o(\log X)\cdot \frac{X}{\log X}\cdot H X=o(H^2).
\]
This contradicts the contribution of a failed centre. Dyadic blocks cover
all sufficiently large \(n\). \(\square\)

The theorem deliberately separates prime detection from the harmonic
architecture below. All subsequent reductions are aimed at producing its
hypothesis.

# 3. Reciprocal sampling and the pair lift

Let \(\rho\) be an even nonnegative Schwartz function and let
\(\mathcal Q_X\) be the primes in \([H,2H)\). For \(a\ne0\) define
\[
w_{q,a}=\rho(Ha/q),\qquad
D_X=\sum_{q\in\mathcal Q_X}\sum_{a\ne0}w_{q,a},\qquad
p_{q,a}=w_{q,a}/D_X.
\]
The reciprocal characteristic function is
\[
\Psi_a(L)=\sum_{q\in\mathcal Q_X}p_{q,a}e(aL/q),
\qquad m_a=\sum_qp_{q,a}.
\]

Let \(\mathcal P_2=\{\{j,k\}:0\le j\le k<N\}\),
\(M=|\mathcal P_2|=N(N+1)/2\), and
\[
S_{\{j,k\}}=P_j+P_k,\qquad
H_2(\theta)=\sum_{u\in\mathcal P_2}e(\theta S_u).
\]
Define the pair-lift energy
\[
\mathcal E_a=\sum_{\substack{u,v\in\mathcal P_2\\u\ne v}}
|\Psi_a(S_u-S_v)|^2.
\]

## Proposition 3.1 (pair-lift and principal cancellation)

The centred block variance is bounded by a weighted aggregate of the
\(\mathcal E_a\), plus explicit diagonal and smoothing errors:
\[
\sum_{j<N}E_j(H)^2
\ \ll\ NHX+
H^2\sum_{a\ge1}\frac{\mathcal R_a}{m_a}
+\mathrm{Err}_{\rho}(X),
\]
where \(\mathcal R_a\) is the distinct-modulus part of \(\mathcal E_a\) and
\(\mathrm{Err}_{\rho}(X)=o(NH^2)\) for fixed admissible \(\rho\).

Consequently the reciprocal-frame target
\[
\sum_{a\ge1}\frac{\mathcal R_a}{m_a}\ll M X^{o(1)}
\tag{RF}
\]
implies the variance criterion of Theorem 2.1.

### Proof architecture

Insert the reciprocal Fourier expansion of the smoothed interval indicator
into the block second moment. The product of two prime-detection sums creates
two copies of the centre walk, indexed by \(\{j,k\}\). The zero frequency
produces the expected main term. The equal-modulus terms are positive and
form an explicit diagonal. For unequal moduli \(q,r\), CRT converts the two
reciprocal phases into one additive phase modulo \(qr\). Subtracting the
constant row before applying Cauchy--Schwarz removes the principal component;
the residual is precisely \(\mathcal R_a\). Schwartz decay controls
\(|a|\ge H\), and the prime-power and endpoint terms are absorbed into
\(\mathrm{Err}_{\rho}\). No cancellation estimate is used in this reduction.
\(\square\)

This proposition is the load-bearing link that was formerly confined to
phase reports. It is now part of the manuscript.

# 4. Exact dual-row identity

Write
\[
\kappa_{2,a}=\sum_qp_{q,a}^2.
\]
Expanding the square and separating equal from unequal moduli gives the exact
identity
\[
\boxed{\mathcal E_a=M(M-1)\kappa_{2,a}+\mathcal R_a.}
\]
The first term is fully understood. The second is the arithmetic core.

The identity is useful because the normalisation is explicit: a proof of
\((\mathrm{RF})\) must save essentially one factor of \(M\) over the trivial
bound \(M^2\).

# 5. Superincreasing rigidity and the exact fourth moment

The centres satisfy \(P_{j+1}\ge XP_j\). Hence any relation
\[
\sum_t c_tP_t=0,\qquad |c_t|\le4,
\]
is trivial for \(X>5\). Applying orthogonality to \(H_2\) reduces its fourth
moment to equality of endpoint multisets.

## Theorem 5.1 (exact fourth moment)

For \(X>5\),
\[
\int_0^1|H_2(\theta)|^4\,d\theta
=\frac{N(3N^3-2N^2+2N-1)}2.
\]
Since \(M=N(N+1)/2\),
\[
\int_0^1\bigl(|H_2|^2-M\bigr)^2
=5M^2\bigl(1+O(N^{-1})\bigr).
\]

The kernel is therefore of Gaussian-square scale in Lebesgue measure. This is
a calibration theorem, not an arithmetic transfer theorem: the reciprocal
sampling points may concentrate on exceptional level sets.

# 6. Growing-degree Möbius truncation

The irreducible-factor detector introduces sums over squarefree products of
block primes. A fixed-degree truncation is insufficient because the number of
excluded periods grows with \(X\).

Let \(s\) denote the number of active prime factors. The partial alternating
binomial identity
\[
\sum_{j=0}^{k}(-1)^j\binom{s}{j}
=(-1)^k\binom{s-1}{k}
\]
gives an exact remainder. Combining it with Stirling and Mertens estimates
yields a truncation degree growing slowly with \(X\), while preserving a
power-saving tail in the aggregate normalisation.

## Theorem 6.1 (Möbius truncation)

There is a choice \(k=k(X)\to\infty\), \(k=o(\log X)\), for which the
Möbius-truncated detector differs from the full detector by
\(M X^{-A}\) for every fixed \(A>0\), after the reciprocal-frame averaging.

The theorem removes a bookkeeping obstruction but does not estimate the
remaining complete character sums.

# 7. Semiprime resonance

The reciprocal measure contains moduli \(qr\asymp H^2\asymp X^4\). Pair
differences \(S_u-S_v\) have exactly the same natural scale. Consequently
there are structured semiprime moduli for which the phase is resonant.

## Theorem 7.1 (resonance obstruction)

No argument based solely on pointwise decay of
\(\Psi_a(S_u-S_v)\) can prove \((\mathrm{RF})\) uniformly. There are
semiprime moduli and pair differences for which the reciprocal phase has
order-one coherence on the natural support.

This rules out a broad class of direct large-sieve and absolute-value
arguments. Cancellation must occur after exploiting the full character and
configuration structure.

# 8. Character-ratio collapse

For \(q\ne r\), CRT and Gauss inversion express the additive phase modulo
\(qr\) as a double character sum. The dependence on the two characters
collapses to their ratio.

## Theorem 8.1 (exact character-ratio formula)

For units \(x,y\bmod qr\), the distinct-modulus kernel admits an exact
decomposition
\[
K_{q,r}(x,y)=
\sum_{\chi\bmod qr}c_{q,r}(\chi)\,
\chi(x/y),
\]
with explicitly normalised coefficients satisfying exact \(L^2\) identities.
The common character direction cancels.

This is the strongest algebraic simplification in the architecture. It
reduces a two-character problem to one ratio character, but the remaining
character sums are evaluated at critical length. Existing bounds do not
supply the necessary pointwise saving for the increasing prime order.

# 9. Density-one and harmonic-scale results

The exact frame identities imply several averaged consequences.

1. If \((\mathrm{RF})\) holds for all but \(o(N)\) centres, then prime
   detection holds for a density-one set of primorial indices.
2. Any successful estimate must control harmonics through the natural range
   \(|a|<H\); low-frequency estimates alone do not close.
3. The critical modulus is \(qr\asymp X^4\) and the walk length is
   \(N\asymp X/\log X\), exactly the square-root-conductor regime after the
   pair lift.

These results locate the boundary but do not cross it.

# 10. What is proved and what remains open

The paper proves:

- the deterministic block-variance criterion;
- the reciprocal-frame reduction, including pair lift and principal
  cancellation;
- exact dual-row decomposition;
- exact fourth moments;
- growing-degree Möbius truncation;
- semiprime resonance;
- character-ratio collapse;
- density-one and scale-calibration consequences.

The paper does **not** prove \((\mathrm{RF})\), the required arithmetic
transference theorem, PGD2, or Fortune's conjecture.

The missing statement is not another formal transformation. It is a
quantitative theorem preventing reciprocal prime-pair sampling from
concentrating on the exceptional sets of the pair-sum kernel.

# 11. Reproducibility corrections in this revision

The revision applies four corrections identified by cold review.

1. Validation numbers are generated only by the scripts shipped in the
   supplement; legacy phase-run values are removed from the headline table.
2. The CRT and character-ratio checks are included in the source manifest
   rather than cited as absent validators.
3. Closed-form evaluation at \(N=55\) is described as evaluation, not
   brute-force enumeration.
4. Python dependencies, including `sympy`, are declared.

## AI-assistance disclosure

The research programme used large language models for structured literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. Every mathematical claim included as a theorem was checked against an explicit proof or an independently reproducible exact computation. Conjectural, conditional, computational, and negative results are labelled separately. The named author takes responsibility for the content, citations, code, and final presentation.

## Data, code, and reproducibility

The source record for this draft is the public repository `https://github.com/digitalgoldfisj79/multi-agent-environment` on branch `gpt56/d1-gate-bridge-terminal-20260724`. The Zenodo package accompanying this manuscript contains the manuscript source, compiled PDF, a claim-status ledger, a source-file manifest, machine-readable metadata, and checksums. Repository paths and frozen commit identifiers are listed in `SUPPORTING_MATERIALS_MANIFEST.tsv`.

# References

1. E. S. A. Bozzard, *Prime detection at primorial centres: reciprocal frames, exact moments, and structural obstructions*, earlier draft and supporting materials, Zenodo DOI 10.5281/zenodo.21457113.
2. A. Granville, *Harald Cramér and the distribution of prime numbers*.
3. A. Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences*, J. London Math. Soc. (2025).
4. K. Matomäki, J. Merikoski and J. Teräväinen, *Primes in arithmetic progressions and short intervals without L-functions*, arXiv:2401.17570.
