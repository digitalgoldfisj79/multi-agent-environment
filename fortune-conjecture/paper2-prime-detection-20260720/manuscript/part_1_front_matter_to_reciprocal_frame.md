---
title: "Prime Detection at Primorial Centres"
subtitle: "Reciprocal frames, exact moments, and structural obstructions"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "20 July 2026"
---

**Abstract.** Let \(P_n=\prod_{p\le p_n}p\) and let \(F_n\) be the least integer \(m>1\) for which \(P_n+m\) is prime. Since every prime factor of \(F_n\) exceeds \(p_n\), a composite \(F_n\) is at least \(p_{n+1}^2\). This paper continues the collision-geometry programme of Paper I and studies the analytic interface between consecutive-prime partial products and prime detection at primorial centres. We first prove that a random-scale second moment for the complete shifted von Mangoldt detector, with only an \(o(\log X)\) loss, already forces every centre in a dyadic block to contain a prime below \(p_{n+1}^2\). We then formulate a principal-cancelled reciprocal frame on the pair-sum set of the primorial-prefix path. Its harmonic energies admit an exact one-sided decomposition: the lower side of the centred prime-gap residual is automatic, and only an upper estimate is load-bearing. We prove an exact Lebesgue fourth-moment formula for the pair-sum polynomial, a growing-degree Möbius truncation theorem with negligible Frobenius tail, a semiprime resonance obstruction to Hardy--Littlewood density replacement, and exact character-diagonal and character-ratio identities showing that CRT de-tensorisation reconstructs the original additive kernel in the unequal-character sector. For a possible density-one route we prove a cubic failure certificate, but also show that primorial-centre phases are macroscopically coherent at the natural zero-pair scale and that the effective explicit-formula conductor migrates by a factor asymptotic to \(p_{n+1}\) between successive indices. Finally, we give exact harmonic aggregation and Fourier-scale conservation identities and quantify why power-scale large values do not yield the exponentially precise phase alignment needed for divisor pinning. No proof of Fortune's conjecture is claimed. The results isolate a signed reciprocal sampling theorem for the consecutive-prime prefix-product walk as the remaining analytic boundary.

**Keywords:** Fortunate numbers; primorials; primes in short intervals; reciprocal exponential sums; Barban--Davenport--Halberstam variance; multiplicative characters; sieve parity.

**MSC 2020:** 11N05, 11N13, 11N35, 11L07, 11B83.

# Introduction

Let \(p_n\) denote the \(n\)-th prime and

\[
P_n=\prod_{p\le p_n}p.
\]

The \(n\)-th Fortunate number is the least integer \(F_n>1\) for which \(P_n+F_n\) is prime. This classical problem is recorded in the standard problem literature [@guy2004]. The elementary observation underlying the subject is that every prime factor of \(F_n\) exceeds \(p_n\). Consequently,

\[
F_n\text{ composite}\quad\Longrightarrow\quad F_n\ge p_{n+1}^2.
\tag{1.1}
\]

Thus a prime in the interval

\[
(P_n,P_n+p_{n+1}^2)
\tag{1.2}
\]

is sufficient to prove that \(F_n\) is prime. The interval length is

\[
p_{n+1}^2=(1+o(1))(\log P_n)^2,
\]

so the pointwise problem is at the Cramér--Granville scale at a prescribed and extremely sparse family of centres [@granville1995]. Standard theorems on primes in short intervals, including conditional mean-square results related to pair correlation, concern continuous or dense averages in the centre variable and do not automatically control the primorial sequence [@montgomery-soundararajan2004; @chan2003; @harper2025].

Paper I [@bozzard2026paper1] studied the deterministic cumulative-product path formed by consecutive primes in a dyadic block. It proved exact collision identities, low-transport and offset-slice bounds, average almost-injectivity, an interval-graph Smith-form theorem, and a detailed decomposition of the centred two-run energy. It deliberately stopped before claiming a prime-offset theorem. The present paper begins at that interface.

There are two complementary analytic entry points.

First, one may work directly with the complete shifted von Mangoldt detector at the primorial centres. We prove that a random-scale block second moment with loss \(o(\log X)\) implies the existence of a prime in every required interval. This is stronger than an almost-all conclusion: because a single failed centre contributes quadratically, the natural variance scale already excludes every failure.

Second, one may pass through a principal-cancelled reciprocal frame obtained from the low-frequency prime-modulus shell of the shifted detector. Its rows are indexed by primes \(q\asymp X^2\) and small nonzero additive harmonics, while its columns are indexed by pair sums of consecutive-prime prefixes. The exact dual-row kernel is

\[
\left|H_2\!\left(a\left(\frac1q-\frac1r\right)\right)\right|^2-M,
\qquad
H_2(\theta)=\sum_{j\le k}e\bigl(\theta(P_j+P_k)\bigr),
\tag{1.3}
\]

where \(M\) is the number of pair sums and \(e(x)=e^{2\pi i x}\). This formulation makes centring exact and exposes the required arithmetic sampling theorem.

The principal results are as follows.

1. A complete shifted-prime variance bound
   \[
   \sum_j\left|\sum_{2\le m\le H}(\Lambda(P_j+m)-1)\right|^2
   \ll NHX L(X),\qquad L(X)=o(\log X),
   \]
   with \(H\asymp X^2\), forces every centre in the block to contain a prime.
2. The reciprocal-frame harmonic energy satisfies an exact decomposition
   \[
   \mathcal E_a=M(M-1)\kappa_{2,a}+\mathcal R_a.
   \]
   Hence only the upper estimate for \(\mathcal R_a\) is required; the lower side is automatic.
3. The pair-sum polynomial has exact Lebesgue fourth moment
   \[
   \int_0^1|H_2(\theta)|^4\,d\theta
   =\frac{N(3N^3-2N^2+2N-1)}2,
   \]
   and centred \(L^2\)-mass \(5M^2(1+O(N^{-1}))\).
4. The exact prime indicator on the critical shell may be replaced by a cumulative Möbius detector of degree
   \[
   k\sim(1+\eta)\frac{\log X}{\log\log X}
   \]
   with negligible Frobenius error. The retained degrees must, however, remain globally signed and coupled.
5. A Hardy--Littlewood density surrogate is polynomially too large because of semiprimes that divide every primorial centre. Thus a positive density main term plus a small error cannot prove the centred reciprocal estimate.
6. In multiplicative Fourier variables, the equal-character diagonal is explicit, but an exact character-ratio identity reconstructs the original additive kernel in the unequal-character sector. CRT factorisation therefore does not create independent modulus averages.
7. Fortune failure implies a cubic local Selberg-energy lower bound. Nevertheless, averaging over the primorial index is coherent at the natural zero-pair scale, and the dominant explicit-formula conductor changes by an unbounded factor at each step.
8. Harmonic aggregation can be made exact without truncation, but the critical shell has only bounded effective harmonic dimension. Narrowing the physical window and summing translates reconstructs the original Fourier transform exactly. Large-value information at a power scale also does not imply the exponentially precise phase alignment needed for divisor pinning.

These statements are exact theorems or exact algebraic reductions. Finite computations are used only to validate identities and to record non-load-bearing diagnostics. No asymptotic conclusion is inferred from a finite panel.

# Primorial blocks and the direct detector

Fix a large parameter \(X\). Let

\[
A_X=\prod_{p<X}p,
\qquad
X\le \ell_1<\ell_2<\cdots<\ell_N<2X
\]

be the primes in the dyadic block, and define

\[
Q_0=1,
\qquad
Q_j=\prod_{u=1}^j\ell_u,
\qquad
P_j=A_XQ_j.
\tag{2.1}
\]

Thus \(P_j\) runs through a consecutive block of primorial centres, up to the harmless endpoint convention at \(j=0\). By the prime number theorem,

\[
N\asymp\frac{X}{\log X},
\qquad
\log P_j\asymp X
\tag{2.2}
\]

uniformly in the block.

## The elementary offset reduction

**Proposition 2.1 (Fortunate-number lower bound).**  If \(F_n\) is composite, then \(F_n\ge p_{n+1}^2\).

**Proof.** If a prime \(r\le p_n\) divided \(F_n\), then \(r\mid P_n\) and \(r\mid P_n+F_n\), contradicting the primality of \(P_n+F_n\). Every prime factor of \(F_n\) is therefore at least \(p_{n+1}\). A composite \(F_n\) has at least two prime factors, counted with multiplicity. \(\square\)

The primorial centre also rigidifies the admissible offsets.

**Lemma 2.2 (candidate collapse below the square threshold).**  Let \(m\) satisfy

\[
1<m<\ell_{j+1}^2
\qquad\text{and}\qquad
(m,P_j)=1.
\]

Then \(m\) is prime. Consequently, a prime in \((P_j,P_j+\ell_{j+1}^2)\) exists if and only if there is a prime \(r\) with

\[
\ell_j<r<\ell_{j+1}^2
\qquad\text{and}\qquad
P_j+r\text{ prime}.
\tag{2.3}
\]

**Proof.** Every prime factor of \(m\) exceeds \(\ell_j\), hence is at least \(\ell_{j+1}\). If \(m\) were composite, then \(m\ge \ell_{j+1}^2\), contrary to the hypothesis. \(\square\)

This binary-prime reformulation is exact, but it does not remove the parity problem. The direct detector below does not impose primality on the offset; it asks only for a prime value of \(P_j+m\).

## Proper prime powers

Fix \(0<\eta<1\) and put

\[
H=\eta X^2.
\tag{2.4}
\]

For all sufficiently large \(X\), one has \(H<\ell_{j+1}^2\) uniformly in the block. Define

\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m),
\qquad
E_j(H)=\Psi_j(H)-H.
\tag{2.5}
\]

**Lemma 2.3 (prime-power contamination).** Uniformly in \(j\), the contribution to \(\Psi_j(H)\) from proper prime powers is

\[
O(X\log X)=o(H).
\tag{2.6}
\]

**Proof.** Near \(P_j\), consecutive squares are separated by \(\gg P_j^{1/2}\), which is exponentially larger than \(H\). The same is true for every higher power. Thus the interval \([P_j+2,P_j+H]\) contains at most one \(k\)-th power for each \(k\ge2\). If that power is \(r^k\), its von Mangoldt weight is

\[
\log r\le \frac{\log(2P_j)}k\ll\frac Xk.
\]

The possible exponents satisfy \(k\ll X\). Summing \(X/k\) gives \(O(X\log X)\). \(\square\)

## A second moment that forces every centre

**Theorem 2.4 (block-variance criterion).** Suppose that for some function \(L(X)\),

\[
\sum_{j=0}^{N-1}|E_j(H)|^2
\le C NHX L(X),
\tag{2.7}
\]

where \(C\) is fixed and \(L(X)=o(\log X)\). Then, for all sufficiently large \(X\), every centre \(P_j\) in the block has a prime in \([P_j+2,P_j+H]\). Consequently, the corresponding Fortunate numbers are prime.

**Proof.** Let \(B_X\) be the number of centres with no prime in the interval. At such a centre, Lemma 2.3 gives

\[
\Psi_j(H)=o(H),
\]

so \(|E_j(H)|\ge H/2\) for sufficiently large \(X\). Therefore

\[
B_X\frac{H^2}{4}
\le
\sum_j|E_j(H)|^2
\le C NHX L(X).
\]

Using \(N\asymp X/\log X\) and \(H=\eta X^2\),

\[
B_X\ll \frac{L(X)}{\log X}=o(1).
\]

Since \(B_X\) is an integer, it is eventually zero. The interval length is below \(\ell_{j+1}^2\), so Proposition 2.1 completes the implication. \(\square\)

The scale on the right of (2.7) is the natural short-interval variance scale suggested by the Selberg integral and by probabilistic models of \(\psi(x+H)-\psi(x)\) [@goldston-montgomery1987; @montgomery-soundararajan2004]. The novelty of Theorem 2.4 is not the variance heuristic but the quantifier: an \(o(\log X)\) loss is already strong enough to pass from a block mean square to every one of the \(N\asymp X/\log X\) primorial centres.

# The reciprocal pair-sum frame

The direct variance in Theorem 2.4 is the cleanest sufficient condition. A complementary harmonic architecture isolates a smaller reciprocal sampling problem and connects it to the cumulative-product geometry of Paper I.

Let

\[
\mathcal P_2=\{(j,k):0\le j\le k<N\},
\qquad
M=|\mathcal P_2|=\frac{N(N+1)}2,
\]

and put

\[
S_{jk}=P_j+P_k.
\tag{3.1}
\]

Define

\[
F(\theta)=\sum_{j<N}e(\theta P_j),
\qquad
H_2(\theta)=\sum_{j\le k}e(\theta S_{jk})
=\frac{F(\theta)^2+F(2\theta)}2.
\tag{3.2}
\]

Fix a nonnegative even Schwartz function \(\rho\), and let \(\mathcal Q_X\) be the primes in \([H,2H)\), with \(H\asymp X^2\). For \(q\in\mathcal Q_X\) and \(a\in\mathbb Z\setminus\{0\}\), set

\[
w_{q,a}=\rho(Ha/q),
\qquad
D_X=\sum_{q\in\mathcal Q_X}\sum_{a\ne0}w_{q,a},
\qquad
p_{q,a}=\frac{w_{q,a}}{D_X}.
\tag{3.3}
\]

Thus \(p_{q,-a}=p_{q,a}\) and \(\sum_{q,a\ne0}p_{q,a}=1\). Define the principal-cancelled row measure

\[
\Phi_X(L)=\sum_{q\in\mathcal Q_X}\sum_{a\ne0}p_{q,a}e(aL/q).
\tag{3.4}
\]

The associated pair-space Frobenius energy is

\[
\mathfrak F_X=
\sum_{u\ne v}|\Phi_X(S_u-S_v)|^2.
\tag{3.5}
\]

The earlier pair-lift and principal-cancellation reductions identify a bound

\[
\mathfrak F_X\ll MX^{o(1)}
\tag{3.6}
\]

as a sufficient local input for the prime-detection architecture. The present paper analyses the exact content of (3.6). The distinction between this sufficient architecture and Theorem 2.4 should be kept explicit: the direct variance theorem is unconditional as an implication, while (3.6) is a harmonic sufficient target arising from the chosen reciprocal-frame reduction.

## Exact harmonic aggregation

For \(a\ge1\), put

\[
\Psi_a(L)=\sum_{q\in\mathcal Q_X}p_{q,a}e(aL/q),
\qquad
m_a=\sum_{q\in\mathcal Q_X}p_{q,a},
\tag{3.7}
\]

and

\[
\mathcal E_a=\sum_{u\ne v}|\Psi_a(S_u-S_v)|^2.
\tag{3.8}
\]

Because the full row measure is symmetric,

\[
\Phi_X(L)=2\Re\sum_{a\ge1}\Psi_a(L),
\qquad
\sum_{a\ge1}m_a=\frac12.
\tag{3.9}
\]

**Proposition 3.1 (exact weighted harmonic reduction).** One has

\[
\boxed{
\mathfrak F_X
\le
2\sum_{a\ge1}\frac{\mathcal E_a}{m_a}.
}
\tag{3.10}
\]

**Proof.** Weighted Cauchy--Schwarz gives

\[
\left|\sum_{a\ge1}\Psi_a(L)\right|^2
\le
\left(\sum_{a\ge1}m_a\right)
\left(\sum_{a\ge1}\frac{|\Psi_a(L)|^2}{m_a}\right)
=\frac12\sum_{a\ge1}\frac{|\Psi_a(L)|^2}{m_a}.
\]

Since \(|2\Re z|^2\le4|z|^2\), summing over \(u\ne v\) proves (3.10). \(\square\)

This removes the artificial truncation parameter from the harmonic reduction. It does not create cancellation between different harmonics: the right side is a positive sum of energies.

## The exact one-sided residual

Let

\[
\kappa_{2,a}=\sum_{q\in\mathcal Q_X}p_{q,a}^2.
\tag{3.11}
\]

**Proposition 3.2 (dual-row identity and one-sided centring).** For every positive harmonic \(a\),

\[
\mathcal E_a
=
\sum_{q,r\in\mathcal Q_X}p_{q,a}p_{r,a}
\left(
\left|H_2\!\left(a\left(\frac1q-\frac1r\right)\right)\right|^2-M
\right).
\tag{3.12}
\]

Writing the distinct-modulus part as

\[
\mathcal R_a=
\sum_{\substack{q,r\in\mathcal Q_X\\q\ne r}}
p_{q,a}p_{r,a}
\left(
\left|H_2\!\left(a\left(\frac1q-\frac1r\right)\right)\right|^2-M
\right),
\tag{3.13}
\]

one has exactly

\[
\boxed{
\mathcal E_a=M(M-1)\kappa_{2,a}+\mathcal R_a.
}
\tag{3.14}
\]

In particular,

\[
\mathcal R_a\ge -M(M-1)\kappa_{2,a}
\tag{3.15}
\]

is automatic, and only an upper bound for \(\mathcal R_a\) is load-bearing.

**Proof.** Expand the square in (3.8) and use

\[
\sum_{u\ne v}e\bigl(\theta(S_u-S_v)\bigr)
=|H_2(\theta)|^2-M.
\]

When \(q=r\), the argument is zero and the bracket equals \(M^2-M=M(M-1)\). \(\square\)

The customary absolute target \(|\mathcal R_a|\ll MX^{o(1)}\), and the stronger squared-kernel sampling theorem, are therefore unnecessary. The correct fixed-harmonic target is the one-sided estimate

\[
\mathcal R_a\le MX^{o(1)}.
\tag{3.16}
\]

More precisely, Proposition 3.1 shows that the smallest aggregate target in this frame is

\[
\sum_{a\ge1}\frac{\mathcal R_a}{m_a}
\ll MX^{o(1)},
\tag{3.17}
\]

because the corresponding weighted sum of diagonal terms is \(o(M)\) for the critical prime shell. Uniform control of every small \(a\) is a convenient sufficient condition, not a necessary quantifier.
