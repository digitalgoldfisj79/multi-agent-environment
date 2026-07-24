---
title: "Prime Detection at Primorial Centres"
subtitle: "Reciprocal frames, exact moments, and structural obstructions"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "24 July 2026"
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

# Exact Lebesgue moments of the pair-sum kernel

The size of the trigonometric kernel itself is not mysterious. Its Lebesgue moments are determined by the superincreasing geometry of the primorial-prefix path.

## Four-copy rigidity

Within the dyadic block, successive prefixes satisfy

\[
P_{j+1}=\ell_{j+1}P_j,
\qquad
\ell_{j+1}\ge X.
\]

For large \(X\),

\[
4\sum_{i<j}P_i<P_j.
\tag{4.1}
\]

**Lemma 4.1 (four-copy rigidity).** For sufficiently large \(X\), an equality

\[
P_i+P_j+P_k+P_\ell
=P_a+P_b+P_c+P_d
\tag{4.2}
\]

holds if and only if the two multisets of endpoint indices are equal.

**Proof.** If the multiplicity vectors differ, let \(t\) be the largest index at which they differ. The coefficient of \(P_t\) in the difference has absolute value at least one and at most four, while the total contribution from smaller indices is less than \(P_t\) by (4.1). Cancellation is impossible. \(\square\)

## Fourth moment

**Theorem 4.2 (exact pair-sum fourth moment).** One has

\[
\boxed{
\int_0^1|H_2(\theta)|^4\,d\theta
=
\frac{N(3N^3-2N^2+2N-1)}2.
}
\tag{4.3}
\]

Consequently,

\[
\boxed{
\int_0^1\bigl(|H_2(\theta)|^2-M\bigr)^2\,d\theta
=
\frac{N(N-1)(5N^2-N+2)}4
=5M^2\bigl(1+O(N^{-1})\bigr).
}
\tag{4.4}
\]

**Proof.** By orthogonality, the fourth moment counts ordered decompositions of an endpoint multiset of size four into two unordered pairs. There are five multiplicity types:

| Endpoint multiplicities | Number of multisets | Ordered decompositions | Contribution |
|---|---:|---:|---:|
| \(1+1+1+1\) | \(\binom N4\) | 6 | \(36\binom N4\) |
| \(2+1+1\) | \(N\binom{N-1}2\) | 4 | \(16N\binom{N-1}2\) |
| \(2+2\) | \(\binom N2\) | 3 | \(9\binom N2\) |
| \(3+1\) | \(N(N-1)\) | 2 | \(4N(N-1)\) |
| \(4\) | \(N\) | 1 | \(N\) |

Summing gives (4.3). Pair-sum injectivity gives \(\int_0^1|H_2|^2=M\), so expanding the centred square gives (4.4). \(\square\)

The theorem solves the kernel-size side of the reciprocal-frame problem. If the arithmetic sampling measure behaved like Lebesgue measure at second moment, the desired scale would follow. The open issue is concentration of the reciprocal prime-pair atoms on the high-value sets of the kernel.

## A strictly weaker level-set target

Let \(\mu_{X,a}\) be the positive measure on \(\mathbb R/\mathbb Z\) assigning mass \(p_{q,a}p_{r,a}\) to

\[
\theta_{q,r}=a\left(\frac1q-\frac1r\right),
\qquad q\ne r,
\]

and put

\[
K_X(\theta)=|H_2(\theta)|^2-M.
\]

The residual is \(\mathcal R_a=\int K_X\,d\mu_{X,a}\). Since only an upper bound is required,

\[
\mathcal R_a\le \int (K_X)_+\,d\mu_{X,a}.
\]

**Proposition 4.3 (one-sided level-set criterion).** Fix \(\varepsilon>0\). It is sufficient to prove, for dyadic

\[
MX^\varepsilon\le \lambda\le M^2,
\]

that

\[
\mu_{X,a}\{K_X\ge\lambda\}
\ll
\frac{MX^{o(1)}}{\lambda}.
\tag{4.5}
\]

**Proof.** Split \((K_X)_+\) at \(MX^\varepsilon\) and apply the dyadic layer-cake inequality. The low part contributes at most \(MX^\varepsilon\), and each dyadic high level contributes \(MX^{o(1)}\). The logarithmic number of levels is absorbed into \(X^{o(1)}\). \(\square\)

This is strictly weaker than the squared-kernel estimate obtained from Chebyshev and Theorem 4.2. It allows an exceptional set of reciprocal pairs of total mass about \(1/M\) to carry the maximal kernel value.

# A globally coupled Möbius detector

A natural attempt to replace the prime-supported shell by a smooth density loses the signed cancellation that distinguishes primes from resonant composites. The exact prime indicator nevertheless admits a useful growing-degree truncation.

Set

\[
H=\frac{X^2}{2},
\qquad
I_X=[H,2H),
\qquad
A_X=\prod_{p<X}p.
\tag{5.1}
\]

For \(n\in I_X\), let

\[
s_X(n)=\omega((n,A_X)).
\]

Since \(n<X^2\), a composite \(n\) coprime to \(A_X\) would have at least two prime factors not smaller than \(X\), which is impossible. Thus

\[
n\text{ prime}\quad\Longleftrightarrow\quad s_X(n)=0.
\tag{5.2}
\]

For an integer \(k\ge0\), define

\[
T_k(n)=
\sum_{\substack{d\mid(n,A_X)\\\omega(d)\le k}}\mu(d).
\tag{5.3}
\]

## Exact degree identity

**Proposition 5.1.** One has

\[
\boxed{
T_k(n)=
\begin{cases}
1,&s_X(n)=0,\\
0,&1\le s_X(n)\le k,\\
(-1)^k\binom{s_X(n)-1}{k},&s_X(n)>k.
\end{cases}}
\tag{5.4}
\]

**Proof.** If \(s=s_X(n)\), then

\[
T_k(n)=\sum_{j=0}^{\min(k,s)}(-1)^j\binom sj.
\]

For \(0<s\le k\) this is \((1-1)^s=0\); for \(s>k\) it is the standard partial alternating-binomial identity. \(\square\)

Write

\[
\mathbf1_{n\text{ prime}}=T_k(n)-R_k(n),
\qquad
R_k(n)=T_k(n)\mathbf1_{s_X(n)>k}.
\tag{5.5}
\]

## Negligible high-degree tail

**Theorem 5.2 (growing-degree truncation).** Let \(\eta>0\) and

\[
k=\left\lceil(1+\eta)\frac{\log X}{\log\log X}\right\rceil.
\tag{5.6}
\]

Then

\[
\sum_{n<2H}|R_k(n)|
\le HX^{-1-\eta+o(1)}.
\tag{5.7}
\]

Moreover, for any matrix-valued shell operator of the form

\[
\mathcal C(c)=
\sum_{n\in I_X}\gamma_n c(n)B_n,
\qquad
|\gamma_n|\ll\frac{\log H}{H},
\qquad
\|B_n\|_F\le M,
\tag{5.8}
\]

one has

\[
\boxed{
\|\mathcal C(R_k)\|_F^2
\le MX^{-2\eta+o(1)}
}
\tag{5.9}
\]

whenever \(M=X^{2+o(1)}\).

**Proof.** For \(s>k\),

\[
|T_k(n)|=\binom{s-1}{k}\le\binom{s}{k+1}.
\]

Hence

\[
\sum_{n<2H}|R_k(n)|
\le
2H\sum_{\substack{d\mid A_X\\\omega(d)=k+1}}\frac1d
\le
\frac{2H}{(k+1)!}
\left(\sum_{p<X}\frac1p\right)^{k+1}.
\]

Mertens' theorem and Stirling's formula give (5.7). The triangle inequality in (5.8) gives

\[
\|\mathcal C(R_k)\|_F
\ll
\frac{M\log H}{H}\sum_{n<2H}|R_k(n)|
\le MX^{-1-\eta+o(1)},
\]

and squaring yields (5.9). \(\square\)

The theorem removes the high-Möbius-degree tail. It does not justify estimating the retained degrees separately. In exact finite panels, splitting the retained detector by degree or divisor size produces norms tens to thousands of times larger than the recombined prime operator. The theorem boundary is therefore a *globally coupled* detector of growing degree.

# A density main-term obstruction

The previous section shows that high degree is not the obstacle. The obstacle is the cancellation among the retained signed terms. A positive Hardy--Littlewood density model fails dramatically because it assigns large mass to composite moduli that are perfectly resonant with every primorial centre.

For \(n\in I_X\), let \(w_a(n)\) be a fixed positive smooth harmonic weight and define

\[
D_\rho=
\sum_{n\in I_X}\frac1{\log n}\sum_{b\ne0}w_b(n),
\qquad
\widetilde p_{n,a}=
\frac{w_a(n)}{D_\rho\log n}.
\tag{6.1}
\]

Consider the Hardy--Littlewood density surrogate

\[
\mathcal R_a^{\mathrm{HL}}
=
\sum_{\substack{n,m\in I_X\\n\ne m}}
\widetilde p_{n,a}\widetilde p_{m,a}
\mathfrak S(m-n)
\left(
\left|H_2\!\left(a\left(\frac1n-\frac1m\right)\right)\right|^2-M
\right),
\tag{6.2}
\]

where \(\mathfrak S\) is the binary singular series.

Define

\[
\mathcal A_X=
\{pr:X/\sqrt2\le p<r<X,\ p,r\text{ prime}\}.
\tag{6.3}
\]

**Theorem 6.1 (semiprime resonance obstruction).** One has

\[
\boxed{
\mathcal R_a^{\mathrm{HL}}
\gg
\frac{M^2}{\log^4X}-MX^{o(1)}.
}
\tag{6.4}
\]

In particular, the density surrogate is polynomially larger than the required \(MX^{o(1)}\) scale.

**Proof.** Every \(n=pr\in\mathcal A_X\) lies in \([X^2/2,X^2)\) and divides \(A_X\), hence divides every centre \(P_j\). Therefore, for distinct \(n,m\in\mathcal A_X\),

\[
e(P_j/n)=e(P_j/m)=1
\]

for every \(j\), and

\[
H_2\!\left(a\left(\frac1n-\frac1m\right)\right)=M.
\]

The kernel equals \(M^2-M\). Moreover, \(m-n\) is even, so its singular series is bounded below by a positive absolute constant. The prime number theorem gives

\[
|\mathcal A_X|\asymp\frac{X^2}{\log^2X}\asymp M,
\qquad
\widetilde p_{n,a}\asymp H^{-1}
\]

on this family. Its positive contribution is therefore

\[
\gg(M^2-M)\frac{|\mathcal A_X|^2}{H^2}
\asymp\frac{M^2}{\log^4X}.
\]

The kernel is bounded below by \(-M\), and the maximum singular series is subpolynomial, so all negative terms together are \(\gg-MX^{o(1)}\). \(\square\)

Thus a decomposition

\[
\text{prime-pair measure}
=
\text{positive density main term}
+
\text{small error}
\]

cannot prove the centred reciprocal estimate. The error would need to cancel a polynomially large resonant-composite contribution. The prime detector must remain signed until after the reciprocal kernel is formed.

# Multiplicative Fourier anatomy

A squarefree additive modulus can be factorised by the Chinese remainder theorem, and additive phases can be expanded in multiplicative characters. This suggests a possible route to independent local averages. The exact character algebra shows why that route fails in the load-bearing sector.

Let

\[
m=\prod_{s=1}^tq_s
\]

be squarefree, and assume every \(P_j\) is a unit modulo \(m\). For a unit \(A\pmod m\), define

\[
F_m(A)=\sum_{j<N}e_m(AP_j),
\qquad
S_m(\chi)=\sum_{j<N}\chi(P_j),
\tag{7.1}
\]

where \(e_m(x)=e(x/m)\). With

\[
\tau_m(\overline\chi)
=
\sum_{u\in(\mathbb Z/m\mathbb Z)^\times}
\overline\chi(u)e_m(u),
\]

multiplicative Fourier inversion gives

\[
F_m(A)=
\frac1{\varphi(m)}
\sum_{\chi\bmod m}
\tau_m(\overline\chi)\chi(A)S_m(\chi).
\tag{7.2}
\]

## The character diagonal

Write

\[
|F_m(A)|^2=\mathfrak D_m+\mathfrak O_m(A),
\]

where \(\mathfrak D_m\) is the equal-character part.

For a unit \(z\pmod m\), define

\[
K_m(z)=
\prod_{q\mid m}
\frac{q\mathbf1_{z\equiv1\, (q)}-1}{q-1}.
\tag{7.3}
\]

**Theorem 7.1 (exact character diagonal).** One has

\[
\boxed{
\mathfrak D_m
=
\sum_{i,j<N}K_m(P_iP_j^{-1}).
}
\tag{7.4}
\]

In particular, \(\mathfrak D_m\) is independent of \(A\). If no off-diagonal pair \(P_i,P_j\) collides modulo any prime factor of \(m\), then for even \(t\),

\[
\mathfrak D_m
=
N+\frac{N(N-1)}{\varphi(m)}.
\tag{7.5}
\]

**Proof.** For one prime \(q\), the principal Gauss sum has squared magnitude one and every nonprincipal Gauss sum has squared magnitude \(q\). Hence

\[
\frac1{(q-1)^2}
\sum_{\chi\bmod q}
|\tau_q(\overline\chi)|^2\chi(z)
=
\frac{q\mathbf1_{z=1}-1}{q-1}.
\]

The character group and the squared Gauss weights factor over the CRT. Summing over \(i,j\) proves (7.4). \(\square\)

The diagonal is close to \(N\) for a product of four large shell primes. It is not the source of the large fluctuations.

## Character-ratio collapse

**Theorem 7.2 (local ratio identity).** Let \(q\) be prime, let \(a,x,y\) be nonzero modulo \(q\), and let \(\rho\) be a multiplicative character. For each character \(\chi\), put \(\psi=\chi\overline\rho\). Then

\[
\boxed{
\frac1{(q-1)^2}
\sum_{\chi\bmod q}
\tau_q(\overline\chi)
\overline{\tau_q(\overline\psi)}
\chi(ax)\overline{\psi(ay)}
=
\begin{cases}
\mathbf1_{\rho=1},&x=y,\\[4pt]
\dfrac{\tau_q(\overline\rho)}{q-1}\rho(a(x-y)),&x\ne y.
\end{cases}}
\tag{7.6}
\]

Summing (7.6) over \(\rho\) reconstructs exactly

\[
e_q(a(x-y)).
\tag{7.7}
\]

**Proof.** Expand the two Gauss sums and sum first over \(\chi\). Character orthogonality forces \(xv\equiv yu\pmod q\). If \(x\ne y\), substitute \(v=yu/x\); the remaining sum is the Gauss sum of \(\rho\) evaluated at \(a(x-y)\). If \(x=y\), only the principal ratio character survives. The final sum over \(\rho\) is multiplicative Fourier inversion. \(\square\)

**Corollary 7.3 (CRT de-tensorisation no-go).** Let \(m=q_1q_2q_3q_4\) and choose two positive and two negative CRT signs. Applying Theorem 7.2 at the four prime factors to the unequal-character sector of \(|F_m(A)|^2\) reconstructs

\[
e_m(A(P_i-P_j))
\]

exactly. It does not produce four independent modulus averages.

The divisor conditions

\[
q_s\mid P_i-P_j
\quad\Longleftrightarrow\quad
q_s\mid P_j/P_i-1
\]

occur in the zero branches and in the character diagonal. They control a sparse correction sector. The unit branches retain the Gauss-weighted character sums and return the original additive reciprocal phase. This is an exact algebraic closure, not a limitation of a particular inequality.

# A density-one certificate and its spectral obstruction

The direct block criterion of Theorem 2.4 aims at every centre. One may ask whether averaging over the primorial index could first yield a density-one theorem. There is a clean positive certificate, but the expected new zero average is absent.

## Failure forces cubic local energy

Let

\[
y_n=p_{n+1}^2-2,
\qquad
h_n=y_n/2,
\]

and define

\[
J_n=
\int_{P_n+1}^{P_n+1+y_n/4}
\left|
\psi(x+h_n)-\psi(x)-h_n
\right|^2\,dx.
\tag{8.1}
\]

**Theorem 8.1 (Fortune-failure certificate).** For all sufficiently large \(n\),

\[
\boxed{
F_n\text{ composite}
\quad\Longrightarrow\quad
J_n\ge\frac{y_n^3}{64}.
}
\tag{8.2}
\]

Consequently,

\[
\boxed{
\left|\{n\le N:F_n\text{ composite}\}\right|
\le
64\sum_{n\le N}\frac{J_n}{y_n^3}+O(1).
}
\tag{8.3}
\]

**Proof.** If \(F_n\) is composite, then there is no prime at any offset \(2\le m<p_{n+1}^2\). For every \(x\) in the integration range, \((x,x+h_n]\) lies inside that failed interval. Its von Mangoldt mass comes only from proper prime powers. As in Lemma 2.3, their total weight is \(O(\log P_n\log\log P_n)=o(h_n)\), uniformly in \(x\). Thus the absolute error is at least \(h_n/2\) throughout an interval of length \(y_n/4\), giving (8.2). Summing the resulting indicator inequality gives (8.3). \(\square\)

A bound

\[
\sum_{n\le N}\frac{J_n}{y_n^3}=o(N)
\tag{8.4}
\]

would prove Fortune for a density-one set of indices.

## Critical-scale coherence

Let

\[
L_n=\log P_n=\vartheta(p_n),
\qquad
\mathcal Z_N(t)=\sum_{n\le N}e^{itL_n}.
\tag{8.5}
\]

**Theorem 8.2 (primorial-centre coherence).** For every fixed real \(c\),

\[
\boxed{
\frac1N\sum_{n\le N}
\exp\left(ic\frac{L_n}{L_N}\right)
\longrightarrow
\int_0^1e^{icu}\,du
=
\begin{cases}
1,&c=0,\\[3pt]
\dfrac{e^{ic}-1}{ic},&c\ne0.
\end{cases}}
\tag{8.6}
\]

**Proof.** The prime number theorem and the asymptotic for the \(n\)-th prime imply

\[
\frac{L_{\lfloor uN\rfloor}}{L_N}\longrightarrow u
\]

for fixed \(0<u\le1\). The sum is a Riemann sum; the first \(o(N)\) indices are negligible. \(\square\)

At frequency \(t=c/L_N\), the sum is generically of order \(N\), not \(N^{1/2}\). Normalised differences of zeta-zero ordinates have precisely this scale in explicit-formula variance calculations [@goldston-montgomery1987; @chan2003]. The primorial-index average is therefore coherent at the point where pair-correlation cancellation would be needed.

## Conductor migration

For the interval in Theorem 8.1, the natural explicit-formula cutoff is

\[
T_n=\frac{P_n}{p_{n+1}^2-2}.
\tag{8.7}
\]

**Theorem 8.3 (conductor migration).** One has

\[
\boxed{
\frac{T_{n+1}}{T_n}
=
\frac{p_{n+1}(p_{n+1}^2-2)}{p_{n+2}^2-2}
\sim p_{n+1}
\longrightarrow\infty.
}
\tag{8.8}
\]

Consequently, for every fixed \(A>1\), the bands \([T_n/A,AT_n]\) are pairwise disjoint for all sufficiently large \(n\).

**Proof.** Substitute \(P_{n+1}=p_{n+1}P_n\) and use \(p_{n+2}/p_{n+1}\to1\). \(\square\)

Thus the dominant high-zero range is not sampled repeatedly across a long block of primorial indices. A density-one proof through the explicit formula would require a bespoke sparse-centre, moving-conductor theorem, not a direct transfer of continuous Selberg-integral or pair-correlation results.

# Harmonic scale conservation

The exact aggregate reduction in Proposition 3.1 raises the possibility of manufacturing a long average over the numerator harmonic \(a\). At the critical shell this possibility is illusory for structural reasons.

## Shortening and translation

For an interval of length \(h\), its additive transform modulo \(q\) occupies approximately \(q/h\) frequencies. To obtain \(A\) effective harmonics while keeping \(q\asymp H\), one might shorten the physical window to \(h=H/A\) and cover the original interval by \(A\) translates.

**Proposition 9.1 (Fourier-scale conservation).** Assume \(H=Ah\) with integers \(A,h\). For every \(q\) and \(a\),

\[
\boxed{
\sum_{b=0}^{A-1}
\sum_{m=bh}^{(b+1)h-1}e(am/q)
=
\sum_{m=0}^{H-1}e(am/q).
}
\tag{9.1}
\]

Thus the broad transform of one short window, multiplied by the translation sum, reconstructs the original length-\(H\) transform exactly.

The identity is tautological, but its consequence is important. Summing the translates with their phases returns the original bounded-harmonic kernel. Bounding the translates separately pays an \(A\)-fold Cauchy or triangle loss and cancels the apparent frequency gain.

One may instead move to a larger modulus shell \(Q=BH\), which gives \(B\) effective harmonics. The natural low-frequency shell scale is then \(Q/\log Q\), not \(H/\log H\); polynomially growing \(B\) introduces a polynomial loss and squares the pair conductor. Moreover, the exact prime-detection decomposition still contains the mandatory shell \(Q\asymp H\). A larger shell is additional, not a replacement.

## Large values do not force narrow alignment

The level-set criterion in Proposition 4.3 suggests attacking only very large values. Put

\[
K_X(\theta)=|H_2(\theta)|^2-M.
\]

If

\[
K_X(\theta)\ge M^{2-\delta},
\]

then, using \(2|H_2|\le |F|^2+N\) and \(M\asymp N^2\),

\[
|F(\theta)|\gg N^{1-\delta/2}.
\tag{9.2}
\]

This is large relative to \(\sqrt N\), but the normalised resultant tends to zero.

**Lemma 9.2 (projection bound).** Let \(z_1,\ldots,z_N\) be unit complex numbers and suppose

\[
\left|\sum_{j=1}^Nz_j\right|=\mu N.
\]

For every \(0<\tau<\mu\), at least

\[
\frac{(\mu-\tau)N}{1-\tau}
\tag{9.3}
\]

of the phases have projection at least \(\tau\) in the direction of the resultant.

**Proof.** Rotate so that the resultant is positive real. If \(K\) phases have real part at least \(\tau\), then the total real part is at most \(K+(N-K)\tau\). Comparing with \(\mu N\) proves the claim. \(\square\)

Taking \(\tau=\mu/2\) in the regime (9.2) guarantees only \(\asymp N^{1-\delta/2}\) phases in an arc of half-width \(\arccos(\mu/2)=\pi/2-o(1)\). This is a diffuse bias, not a narrow modular-arc certificate.

Even if two narrow constraints

\[
\|\theta L_i\|\le\varepsilon,
\qquad
\theta=\frac{a(r-q)}{qr}
\]

were available, eliminating \(a(r-q)\) yields integers \(n_i\) satisfying

\[
|n_1L_2-n_2L_1|
\le
\varepsilon(|L_1|+|L_2|).
\tag{9.4}
\]

The \(L_i\) are primorial-sized. For (9.4) to force an exact integer relation, \(\varepsilon\) must be exponentially small in \(X\). A power-scale large-value estimate gives no such precision. Consequently, large amplitude alone cannot produce the divisor pinning required by a finite determinant argument.

# Relation to existing analytic methods

The remaining theorem is adjacent to several mature bodies of analytic number theory, but does not fit any of them directly.

The direct criterion in Theorem 2.4 resembles a Selberg-integral or Barban--Davenport--Halberstam statement. Classical BDH theory averages residue classes and moduli [@davenport-halberstam1966], while recent general-sequence versions require regularity or non-concentration hypotheses that are themselves unproved for the modulus-dependent primorial detector [@harper2025]. Pair-correlation methods relate continuous mean squares of primes in short intervals to zero statistics [@goldston-montgomery1987; @chan2003], but Theorems 8.2 and 8.3 show that the primorial centres neither provide a common critical-scale phase average nor a stable conductor ensemble.

Asymptotic-sieve methods can break parity when an additional bilinear axiom is available [@friedlander-iwaniec1998]. In the present problem, exact finite decompositions show strong cancellation between Type-I and Type-II pieces of the complete von Mangoldt detector. Bounding those pieces separately removes the stabilising covariance. Modern multiplicatively structured prime-detecting sieves reach short intervals of polynomial length in the ambient prime size, whereas the present interval has length only \((\log P_j)^2\) [@matomaki-merikoski-teravainen2024].

Sparse large-sieve inequalities, additive-energy refinements, and results for freely selected products of primes control substantially different sampling geometries [@chang-kerr-shparlinski2018; @baker-munsch-shparlinski2022; @matomaki-teravainen2024]. Their generic dependence on frequency diameter or conductor does not exploit the signed cumulative Möbius detector. Kloosterman-fraction and dispersion estimates likewise require explicit independent coefficient variables after a usable reciprocity transform [@bettin-chandee2018; @drappeau2017]. The exact ratio-collapse theorem shows that complete character separation of the present kernel does not create those variables.

Factorial exponential-sum methods are a natural neighbouring subject because factorials and primorial prefixes are both cumulative multiplicative walks. Their principal shift identity,

\[
\frac{(n+k)!}{n!}=\prod_{i=1}^k(n+i),
\]

creates a bounded-degree polynomial in the index and enables Weil-type arguments [@garaev-luca-shparlinski2004; @garaev-luca-shparlinski2005]. The corresponding quotient of primorial prefixes is a product of future primes and has no bounded-degree algebraic dependence on the index. The available factorial technology exploits that bounded-degree shift structure, which is absent for primorial prefixes. This analogy therefore identifies the missing structure rather than supplying a theorem.

# Computational verification and reproducibility

All asymptotic statements in this paper are proved symbolically. Computation was used for independent validation of exact identities and for diagnostics that are explicitly excluded from the proofs.

The validation suite includes:

- exhaustive checks of the partial alternating-binomial identity for the Möbius detector;
- direct enumeration of the endpoint-multiset count in Theorem 4.2;
- random complex-vector checks of the one-sided residual identity;
- prime, semiprime, three-prime and four-prime checks of the CRT character diagonal;
- independent verification of the local character-ratio collapse;
- finite Fourier reconstruction tests for Proposition 9.1;
- numerical audits of the critical-scale coherence limit;
- weighted reciprocal-pair samples used only to illustrate the diffuse nature of accessible high values.

Selected checks are shown below.

| Identity or diagnostic | Validation result |
|---|---:|
| Theorem 4.2 at \(N=55\) | exact value \(13{,}562{,}560\) |
| CRT diagonal/full reconstruction | maximum residual below \(2\times10^{-12}\) |
| Character-ratio collapse | maximum residual below \(2.3\times10^{-14}\) |
| One-sided energy identity | maximum residual \(1.30\times10^{-9}\) |
| Fourier-scale reconstruction | maximum residual \(1.31\times10^{-13}\) |
| Coherence diagnostic at \(N=10{,}000\) | correlation \(0.99612\) with limiting sinc profile |

The supplementary archive contains the source manuscript, validators, phase reports, data summaries, a manifest, and checksums. The numerical panels are descriptive and are not used to establish any theorem.

# The remaining theorem boundary

The results above progressively remove non-load-bearing formulations.

- The direct problem does not require a prime offset; any shifted prime below the square threshold suffices.
- A natural block second moment already proves every centre, provided its loss is \(o(\log X)\).
- In the reciprocal frame, the lower side of the centred residual is automatic.
- A weighted aggregate over harmonics is sufficient; uniformity in every harmonic is stronger than necessary.
- The pair-sum kernel has exactly the expected Lebesgue \(L^2\)-mass.
- High Möbius degree is negligible.
- Positive density replacement is invalid because of resonant composites.
- The CRT character diagonal is not load-bearing, and the unequal-character sector reconstructs the original phase.
- Primorial-index averaging is coherent at the critical zero scale and unstable in conductor.
- Long harmonic averaging and finite divisor certificates do not survive exact Fourier accounting.

For the reciprocal architecture, the clean open target is the weighted one-sided estimate

\[
\boxed{
\sum_{a\ge1}\frac1{m_a}
\sum_{\substack{q,r\in\mathcal Q_X\\q\ne r}}
 p_{q,a}p_{r,a}
\left(
\left|H_2\!\left(a\left(\frac1q-\frac1r\right)\right)\right|^2-M
\right)
\ll MX^{o(1)}.
}
\tag{12.1}
\]

The prime support in (12.1) may be replaced by the growing-degree cumulative Möbius detector of Theorem 5.2, but the retained degrees must remain signed and coupled. The theorem is a deterministic transference statement: the reciprocal prime-pair sampling measure must not place excessive mass on the high-value sets of a lacunary pair-sum polynomial generated by one consecutive-prime prefix-product walk.

For the direct architecture, the open target is

\[
\boxed{
\sum_{j<N}
\left|
\sum_{2\le m\le\eta X^2}
(\Lambda(P_j+m)-1)
\right|^2
\ll NHX L(X),
\qquad L(X)=o(\log X).
}
\tag{12.2}
\]

A proof of (12.2) would establish Fortune's conjecture for all sufficiently large indices. A proof of (12.1) would close the reciprocal-frame route to the corresponding principal-cancelled Frobenius estimate. The exact equivalence of these two open targets is not asserted; they are complementary boundaries reached from the same primorial geometry.

# Conclusion

Consecutive-prime partial products carry enough exact structure to support a detailed analytic reduction, but not enough currently known cancellation to prove Fortune's conjecture. The present sequel supplies three kinds of result.

First, it gives positive reductions: a block second moment that forces every centre; an exact harmonic aggregate; an exact one-sided residual; an exact pair-sum fourth moment; and a growing-degree Möbius truncation.

Second, it gives exact obstruction theorems: semiprime resonance defeats positive density replacement; the unequal-character CRT sector reconstructs the additive kernel; the primorial-index average is coherent at critical zero spacing and migrates in conductor; Fourier-scale conservation defeats an artificial long harmonic average; and power-scale large values do not imply divisor-level phase precision.

Third, it identifies the remaining mathematics. The obstacle is not a missing algebraic reformulation. It is a signed arithmetic transference theorem for the consecutive-prime prefix-product walk, or a direct sparse-centre Selberg-integral theorem at interval length \((\log P)^2\). Neither is supplied by current generic sieve, large-sieve, Kloosterman, factorial-sum, or pair-correlation machinery.

No implication beyond the stated conditional criteria is claimed. The value of the analysis is the exact boundary: future progress must create genuinely new cancellation rather than another equivalent decomposition of the same reciprocal kernel.

# AI-assistance disclosure

The research programme used large language models for structured literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. Every mathematical claim presented as a theorem is tied to an explicit proof or an independently reproducible exact computation. Conjectural, conditional, computational, diagnostic, and negative results are labelled separately. The named author takes responsibility for the content, citations, code, and final presentation.

# References

::: {#refs}
:::
