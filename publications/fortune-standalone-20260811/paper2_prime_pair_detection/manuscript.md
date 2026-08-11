---
title: "Prime-Pair Detection at Primorial Centres"
subtitle: "Exact existence criteria, reciprocal frames, and structural obstructions"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "11 August 2026"
bibliography: references.bib
---

**Abstract.** Let \(P_n=\prod_{p\le p_n}p\) and let \(F_n\) be the least integer \(m>1\) for which \(P_n+m\) is prime. We begin with the elementary but decisive observation that, below the square threshold \(p_{n+1}^2\), every offset producing a prime at a primorial centre must itself be prime. Prime detection at that scale is therefore a two-prime problem. We prove an exact prime-pair detector decomposition, three block criteria showing that sufficiently sharp mean-square control excludes every failed primorial centre, and an exact double-von-Mangoldt Fourier representation whose geometric kernel is the single cumulative-product walk. The Hardy--Littlewood singular-series expressions used to calibrate the expected means are stated explicitly as conjectural rather than proved asymptotics.

Independently of that direct detector, we analyse a reciprocal pair-sum model attached to the same cumulative-product path. We prove an exact harmonic-energy decomposition with one-sided centring, an exact fourth moment and centred \(L^2\) law for the pair-sum polynomial, a growing-degree cumulative Möbius truncation, a semiprime-resonance obstruction to positive density surrogates, exact multiplicative-character diagonal and ratio identities, a local failure certificate, critical-scale coherence and conductor-migration results, and a Fourier-scale conservation obstruction. These results explain why several natural large-sieve, density, character-factorisation and large-value mechanisms do not by themselves yield the required prime-pair variance. No source-to-reciprocal transference theorem and no proof of Fortune's conjecture is claimed.

**Keywords:** Fortunate numbers; primorials; prime pairs; primes in short intervals; reciprocal exponential sums; Barban--Davenport--Halberstam variance; multiplicative characters; sieve parity.

**MSC 2020:** 11N05, 11N13, 11N35, 11L07, 11B83.

# Introduction

Let \(p_n\) denote the \(n\)-th prime and define the primorial
\[
P_n=\prod_{p\le p_n}p.
\]
The \(n\)-th Fortunate number is the least integer \(F_n>1\) for which \(P_n+F_n\) is prime [@guy2004]. Every prime divisor of \(F_n\) exceeds \(p_n\); hence
\[
F_n\text{ composite}\quad\Longrightarrow\quad F_n\ge p_{n+1}^2.
\tag{1.1}
\]
Consequently, a prime in
\[
(P_n,P_n+p_{n+1}^2)
\tag{1.2}
\]
forces \(F_n\) to be prime. Since \(p_{n+1}^2=(1+o(1))(\log P_n)^2\), this is a pointwise prime-detection problem at a Cramér--Granville-scale interval around a prescribed and extremely sparse sequence of centres [@granville1995]. Classical and modern results on primes in short intervals or mean-square prime distribution average over substantially denser families of centres and do not directly supply such pointwise information [@goldston-montgomery1987; @chan2003; @montgomery-soundararajan2004; @harper2025].

The first purpose of this paper is to identify the exact arithmetic object that must be controlled at this scale. Fix a dyadic block of consecutive primes \(X\le \ell_1<\cdots<\ell_N<2X\), set
\[
A_X=\prod_{p<X}p,\qquad Q_j=\prod_{u=1}^j\ell_u,\qquad P_j=A_XQ_j,
\]
and take \(H=\eta X^2\) with fixed \(0<\eta<1\). If \(P_j+m\) is prime for \(1<m<H<\ell_{j+1}^2\), then \((m,P_j)=1\), and every prime factor of \(m\) exceeds \(\ell_j\). Thus \(m\) itself is prime. The exact existence variable is therefore
\[
Z_j(H)=\#\{m\le H:m\text{ prime and }P_j+m\text{ prime}\},
\]
not an ordinary shifted-prime count. We also use the weighted variants
\[
Y_j(H)=\sum_{m\le H}\mathbf1_{\mathbb P}(m)\Lambda(P_j+m),
\qquad
T_j(H)=\sum_{m\le H}\Lambda(m)\Lambda(P_j+m).
\]
A single failed centre creates a discrepancy of the same order as the full expected mean. This converts sufficiently sharp block variance bounds into exact no-failure criteria. The proofs of those implications are elementary; the missing mathematics is the variance theorem itself.

The second purpose is structural. Reciprocal harmonic sampling of the cumulative-product path naturally produces the pair-sum polynomial
\[
H_2(\theta)=\sum_{0\le j\le k<N}e\bigl(\theta(P_j+P_k)\bigr)
\]
and kernels of the form
\[
\left|H_2\!\left(a\left(\frac1q-\frac1r\right)\right)\right|^2-M,
\qquad M=\frac{N(N+1)}2.
\tag{1.3}
\]
We study this reciprocal frame as an independent deterministic model. It has exact collision, moment, Möbius and character structure, but no theorem in this paper transfers the direct two-prime detector to that frame. This separation is deliberate: it prevents a structural identity about the reciprocal model from being mistaken for a prime-detection theorem.

The principal results are grouped as follows.

1. **Exact detector and no-failure criteria.** Proposition 2.3 proves candidate collapse and isolates the proper-prime-power remainder. Theorems 2.4, 2.5 and 2.7 give unweighted, weighted and double-von-Mangoldt block criteria. Theorem 2.8 gives the exact double-von-Mangoldt source-to-walk Fourier identity.
2. **Reciprocal-frame structure.** Propositions 3.1 and 3.2 give exact harmonic aggregation and the one-sided residual decomposition. Theorem 4.2 gives the exact fourth moment of the pair-sum polynomial and its centred \(L^2\) mass.
3. **Signed detector and obstruction results.** Theorem 5.2 gives a growing-degree Möbius truncation with negligible high-degree tail while preserving the need for global signed coupling. Theorem 6.1 shows that a positive Hardy--Littlewood density surrogate is polynomially too large because of resonant semiprimes. Theorems 7.1 and 7.2 and Corollary 7.3 show that multiplicative-character factorisation does not de-tensorise the load-bearing additive kernel.
4. **Sparse-centre and harmonic obstructions.** Theorem 8.1 converts Fortune failure into a cubic local Selberg-energy lower bound. Theorems 8.2 and 8.3 establish critical-scale phase coherence and moving conductors along primorial centres. Proposition 9.1 and Lemma 9.2 show why enlarging the harmonic family or using power-scale large values does not create the required fine arithmetic alignment.

## Status of results

The article uses four distinct epistemic classes.

- Statements labelled theorem, proposition, lemma or corollary are proved in the text.
- Hardy--Littlewood formulae used for \(\lambda_j\), \(\mu_j\) and \(\nu_j\) are conjectural calibrations; the no-failure implications require only baselines of the displayed orders.
- Finite computations in the reproducibility section validate exact identities or illustrate diagnostics and are not used to infer asymptotic theorems.
- The required sparse-centre prime-pair variance estimates and any source-to-reciprocal transference theorem remain open.

The paper is therefore a collection of exact reductions, structural theorems and obstruction results around a sharply stated open analytic boundary. It does not prove Fortune's conjecture.

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

This binary-prime reformulation is exact and exposes the parity problem: below the square threshold, successful outputs and admissible offsets must both be prime.

## Exact collapse of the detector

Fix \(0<\eta<1\) and put
\[
H=\eta X^2.
\tag{2.4}
\]
For all sufficiently large \(X\), \(H<\ell_{j+1}^2\) uniformly in the block.
Define the unweighted prime-pair detector
\[
Z_j(H)=
\sum_{2\le m\le H}
\mathbf 1_{\mathbb P}(m)\mathbf 1_{\mathbb P}(P_j+m),
\tag{2.5}
\]
and the weighted prime-pair detector
\[
Y_j(H)=
\sum_{2\le m\le H}
\mathbf 1_{\mathbb P}(m)\Lambda(P_j+m).
\tag{2.6}
\]
The lower cutoff \(m>\ell_j\) is automatic: if a prime \(m\le\ell_j\), then
\(m\mid P_j\) and \(P_j+m\) is divisible by \(m\).

**Proposition 2.3 (exact candidate-collapse detector).** For every \(j\):

1. \(Z_j(H)>0\) if and only if \([P_j+2,P_j+H]\) contains a prime;
2. if
   \[
   \Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m),
   \]
   then
   \[
   \boxed{\Psi_j(H)=Y_j(H)+R_j(H)},
   \tag{2.7}
   \]
   where \(R_j(H)\) is supported on proper prime powers \(P_j+m=r^k\), \(k\ge2\), and
   \[
   R_j(H)=O(X\log X)=o(H)
   \tag{2.8}
   \]
   uniformly in \(j\).

**Proof.** If \(P_j+m\) is prime, then \((m,P_j)=1\); otherwise a common
prime divisor would divide the prime output. Lemma 2.2 therefore forces \(m\)
to be prime. This proves the first assertion and identifies every prime term in
\(\Psi_j\) with a term of \(Y_j\). The remaining von Mangoldt terms are proper
prime powers. Near \(P_j\), consecutive \(k\)-th powers are separated by more
than \(H\); for each \(k\ge2\) there is at most one, with weight
\(O(X/k)\). Summing over \(k\ll X\) gives \(O(X\log X)\). \(\square\)

Thus the complete shifted detector is a weighted prime-pair detector plus a
negligible prime-power remainder. It is not naturally centred at the ordinary
short-interval mean \(H\).

### Expanded coprimality and prime-power details

If \(P_j+m\) is prime and a prime \(q\mid(m,P_j)\), then
\(q\mid P_j+m\). Since \(q\le\ell_j<P_j+m\), this would be a proper
divisor of the output, a contradiction. Thus \((m,P_j)=1\), and Lemma 2.2
applies without an additional assumption.

For the remainder in Proposition 2.3, if \(r^k\asymp P_j\), then
\[
(r+1)^k-r^k\ge k r^{k-1}\gg P_j^{(k-1)/k}.
\]
This spacing is exponential in \(X\), hence larger than \(H\asymp X^2\),
uniformly for \(k\ge2\) once \(X\) is large. There is therefore at most one
\(k\)-th power in the interval for each exponent. Its weight is
\(\log r\le\log(2P_j)/k=O(X/k)\); and \(2^k\le2P_j\) gives \(k=O(X)\).
Summing \(X/k\) proves \(R_j(H)=O(X\log X)\).

## Block-variance implications

The following criteria separate the exact deterministic implication from the conjectural
choice of main term.

**Theorem 2.4 (unweighted prime-pair block criterion).** Let \(\lambda_j>0\)
satisfy
\[
cX\le\lambda_j\le CX
\tag{2.9}
\]
uniformly for fixed constants \(c,C>0\). If
\[
\sum_{j=0}^{N-1}|Z_j(H)-\lambda_j|^2
\ll NX L(X),
\qquad L(X)=o(\log X),
\tag{2.10}
\]
then every centre in the block contains a prime in \([P_j+2,P_j+H]\).

**Proof.** If \(B_X\) centres fail, then \(Z_j=0\) at each of them, so
\[
B_Xc^2X^2\le\sum_j|Z_j-\lambda_j|^2\ll NXL(X).
\]
Since \(N\asymp X/\log X\), \(B_X\ll L(X)/\log X=o(1)\). Integrality gives
\(B_X=0\) for sufficiently large \(X\). \(\square\)

**Theorem 2.5 (weighted prime-pair block criterion).** Let \(\mu_j>0\) satisfy
\[
cH\le\mu_j\le CH.
\tag{2.11}
\]
If
\[
\sum_{j=0}^{N-1}|Y_j(H)-\mu_j|^2
\ll NHX L(X),
\qquad L(X)=o(\log X),
\tag{2.12}
\]
then every centre in the block contains a prime in the required interval.

The proof is identical: at a failed centre \(Y_j=0\), and
\(H\asymp X^2\). Proposition 2.3 allows \(Y_j\) to be replaced by \(\Psi_j\)
only after the prime-power remainder and the corresponding change of centring
are retained explicitly.

## A double-von-Mangoldt source

For analytic decomposition it is convenient to retain von Mangoldt weights on
both prime variables:
\[
T_j(H)=\sum_{2\le m\le H}\Lambda(m)\Lambda(P_j+m).
\tag{2.13}
\]

**Lemma 2.6 (failure contamination for the double source).** If the centre
\(P_j\) has no prime in \([P_j+2,P_j+H]\), then
\[
T_j(H)=O(X(\log X)^2).
\tag{2.14}
\]

**Proof.** Every nonzero term must have \(P_j+m=r^k\) with \(k\ge2\).
For each exponent \(k\), the interval contains at most one such power.
Moreover \(\Lambda(P_j+m)\ll X/k\) and \(\Lambda(m)\le\log H\ll\log X\).
Summing over \(k\ll X\) gives the result. \(\square\)

The spacing argument above also makes Lemma 2.6 explicit. At a failed
centre, each nonzero term has \(P_j+m=r^k\), and there is at most one such
power for each \(k\). Its two weights contribute at most
\(O((X/k)\log X)\). Summing over \(k=O(X)\) gives
\(O(X(\log X)^2)\).

The Hardy--Littlewood model predicts the main term
\[
\nu_j(H)=\mathfrak S(P_j)H\asymp H\log X.
\tag{2.15}
\]
Thus a failed centre is separated from the predicted mean by
\(\asymp H\log X\), despite the residual prime-power contamination.

**Theorem 2.7 (double-von-Mangoldt block criterion).** Let deterministic
baselines \(\nu_j\) satisfy
\[
cH\log X\le\nu_j\le CH\log X.
\]
If
\[
\sum_{j<N}|T_j(H)-\nu_j|^2
\ll NHX(\log X)^2L(X),
\qquad L(X)=o(\log X),
\tag{2.16}
\]
then every centre in the block succeeds.

**Proof.** At a failed centre Lemma 2.6 gives
\(|T_j-\nu_j|\gg H\log X\). Hence
\[
B_XH^2(\log X)^2
\ll NHX(\log X)^2L(X),
\]
and \(B_X\ll L(X)/\log X=o(1)\). \(\square\)

This source is particularly useful because it is an exact additive correlation
of two von Mangoldt sequences; no division by \(\log m\) or replacement of a
prime indicator is required.

## Conjectural Hardy--Littlewood calibration

For the even primorial difference \(P_j\), define
\[
\mathfrak S(P_j)
=2C_2\prod_{\substack{p\mid P_j\\p>2}}\frac{p-1}{p-2},
\qquad
C_2=\prod_{p>2}\frac{p(p-2)}{(p-1)^2}.
\tag{2.17}
\]
Mertens' product theorem gives
\[
\mathfrak S(P_j)\sim e^\gamma\log\ell_j.
\tag{2.18}
\]
The standard Hardy--Littlewood prime-pair model predicts
\[
\lambda_j(H)=
\mathfrak S(P_j)
\int_{\ell_j}^{H}
\frac{dt}{\log t\,\log(P_j+t)},
\tag{2.19}
\]
and
\[
\mu_j(H)=
\mathfrak S(P_j)
\int_{\ell_j}^{H}\frac{dt}{\log t}.
\tag{2.20}
\]
Uniformly in a dyadic block, \(\lambda_j(H)\asymp X\) and
\(\mu_j(H)\asymp H\). Moreover
\[
\frac{\mu_j(H)}H\longrightarrow\frac{e^\gamma}{2}
\tag{2.21}
\]
in the idealised square-boundary scaling. The convergence is logarithmically
slow, so finite data at modest primes need not visibly separate \(H\) from
\(\mu_j(H)\).

Equations (2.19)--(2.21) are conjectural calibrations, not proved asymptotics.
Theorems 2.4--2.5 require only baselines of the displayed sizes.

# Exact Fourier source identity

Let
\[
a_H(m)=\Lambda(m)\mathbf1_{[2,H]}(m),
\]
and let \(b_X(n)=\Lambda(n)\) on the finite interval
\([P_0+2,P_{N-1}+H]\), zero elsewhere. Put
\[
A_H(\theta)=\sum_m a_H(m)e(-m\theta),
\qquad
B_X(\theta)=\sum_n b_X(n)e(n\theta),
\qquad
G_X(\theta)=A_H(\theta)B_X(\theta).
\tag{2.22}
\]

**Theorem 2.8 (corrected source-to-walk identity).** One has exactly
\[
\boxed{
T_j(H)=\int_0^1G_X(\theta)e(-P_j\theta)\,d\theta.
}
\tag{2.23}
\]
If
\[
F_X(\theta)=\sum_{j<N}e(P_j\theta),
\qquad
V_X(\theta)=\sum_{j<N}\nu_j e(P_j\theta),
\]
then
\[
\boxed{
\begin{aligned}
\sum_{j<N}|T_j-\nu_j|^2
={}&\int_0^1\!\int_0^1
G_X(\alpha)\overline{G_X(\beta)}
F_X(\beta-\alpha)\,d\alpha\,d\beta\\
&-2\Re\int_0^1G_X(\alpha)V_X(-\alpha)\,d\alpha
+\sum_{j<N}\nu_j^2.
\end{aligned}}
\tag{2.24}
\]

**Proof.** Expanding (2.23), orthogonality forces
\(n-m-P_j=0\), leaving the defining correlation \(T_j\). Squaring, summing
over \(j\), and interchanging the finite sums and integrals gives the first
term in (2.24); the cross term and baseline square are immediate. \(\square\)

### Expanded Fourier-sign verification

Expanding the integrand in Theorem 2.8 gives
\[
G_X(\theta)e(-P_j\theta)
=\sum_{m,n}a_H(m)b_X(n)e((n-m-P_j)\theta).
\]
Orthogonality forces \(n=P_j+m\), leaving exactly \(T_j(H)\). In the
squared block sum, the conjugate contributes \(e(P_j\beta)\), so
\[
\sum_{j<N}e(-P_j\alpha)e(P_j\beta)=F_X(\beta-\alpha).
\]
This derives both Fourier signs and the single-walk kernel directly; all sums
are finite.

For the double-von-Mangoldt representation, the first exact harmonic object is
the single-walk polynomial \(F_X\), and the source
\(G_X=A_HB_X\) retains both von Mangoldt factors and their common offset.
There is also a distinct one-sided representation: Proposition 2.3 shows that the
shifted detector \(\Psi_j\), after recentering at \(\mu_j\) and controlling
\(R_j\), is already a weighted prime-pair detector. A reciprocal
transference from that source need not introduce an explicit factor \(A_H\),
but it must compute the principal term at the square-root sieve boundary.
The pair-sum frame below is therefore analysed as a model whose connection to
either prime-pair source is proved; none of the structural results below is used
as a substitute for that missing transference theorem.

# The reciprocal pair-sum frame

Theorems 2.4--2.7 give the direct Fortune implications. We now introduce an independent reciprocal pair-sum model on the same cumulative-product path. It is motivated by harmonic sampling of pair differences; no transference from the two-prime source to this model is proved.

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

Fix a nonnegative even Schwartz function \(\rho\) such that
\[
\inf_{1/2\le |t|\le1}\rho(t)>0,
\]
and let \(\mathcal Q_X\) be the primes in \([H,2H)\), with \(H\asymp X^2\). This admissibility condition guarantees \(D_X>0\) and the comparison \(D_X\asymp_\rho|\mathcal Q_X|\) used below. For \(q\in\mathcal Q_X\) and \(a\in\mathbb Z\) with \(a\ne0\), set

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

A natural local target for this reciprocal model is:

\[
\mathfrak F_X\ll MX^{o(1)}.
\tag{3.6}
\]

Equation (3.6) is not derived from Theorems 2.4--2.7. For the
double-von-Mangoldt source, (2.24) contains the additional factor \(A_H\).
For the recentered one-sided source \(\Psi_j-\mu_j\), that factor is implicit
rather than explicit, and no principal-cancellation theorem at the prime-pair
mean \(\mu_j\) is proved. Consequently (3.6) is treated as a deterministic
model estimate whose internal structure is analysed below. Proving it for the
increasing order could contribute to Fortune only together with a new
source-to-frame theorem; the present manuscript neither proves nor rules out
such a theorem.

## Exact harmonic aggregation

For \(a\ge1\), put

\[
\Psi_a(L)=\sum_{q\in\mathcal Q_X}p_{q,a}e(aL/q),
\qquad
m_a=\sum_{q\in\mathcal Q_X}p_{q,a},
\tag{3.7}
\]

If \(m_a=0\), then every \(p_{q,a}=0\) and hence \(\Psi_a\equiv0\). Such harmonics are omitted from every quotient by \(m_a\); all quotient sums below are therefore over \(a\ge1\) with \(m_a>0\).

Define

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
2\sum_{\substack{a\ge1\\m_a>0}}\frac{\mathcal E_a}{m_a}.
}
\tag{3.10}
\]

**Proof.** Weighted Cauchy--Schwarz gives

\[
\left|\sum_{a\ge1}\Psi_a(L)\right|^2
\le
\left(\sum_{a\ge1}m_a\right)
\left(\sum_{\substack{a\ge1\\m_a>0}}\frac{|\Psi_a(L)|^2}{m_a}\right)
=\frac12\sum_{\substack{a\ge1\\m_a>0}}\frac{|\Psi_a(L)|^2}{m_a}.
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
\sum_{\substack{a\ge1\\m_a>0}}\frac{\mathcal R_a}{m_a}
\ll MX^{o(1)},
\tag{3.17}
\]

because the corresponding weighted sum of diagonal terms is \(o(M)\) for the critical prime shell. Indeed,
\[
\frac{\kappa_{2,a}}{m_a}
=\frac{\sum_q w_{q,a}^2}{D_X\sum_q w_{q,a}}
\le \frac{\max_q w_{q,a}}{D_X},
\]
and Schwartz decay gives \(\sum_{a\ge1}\max_q w_{q,a}=O_\rho(1)\), whereas the prime number theorem gives \(D_X\asymp_\rho |\mathcal Q_X|\asymp H/\log H\). Thus
\[
M(M-1)\sum_{\substack{a\ge1\\m_a>0}}\frac{\kappa_{2,a}}{m_a}
\ll_\rho \frac{M^2\log H}{H}=o(M),
\]
since \(M\asymp X^2/\log^2X\) and \(H\asymp X^2\). Uniform control of every small \(a\) is a convenient sufficient condition, not a necessary quantifier.

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

**Proposition 4.3 (one-sided level-set criterion).** Let \(L(X)\ge1\) satisfy \(L(X)=X^{o(1)}\). It is sufficient to prove, for dyadic

\[
ML(X)\le \lambda\le M^2,
\]

that

\[
\mu_{X,a}\{K_X\ge\lambda\}
\ll
\frac{MX^{o(1)}}{\lambda}.
\tag{4.5}
\]

**Proof.** Split \((K_X)_+\) at \(ML(X)\) and apply the dyadic layer-cake inequality. The low part contributes at most \(ML(X)=MX^{o(1)}\), and each dyadic high level contributes \(MX^{o(1)}\). The logarithmic number of levels is absorbed into \(X^{o(1)}\). \(\square\)

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

The kernel equals \(M^2-M\). Moreover, \(m-n\) is even. For the binary singular series,
\[
\mathfrak S(d)=2C_2\prod_{\substack{p\mid d\\p>2}}\frac{p-1}{p-2}
\qquad(d\ \text{even}),
\]
so \(\mathfrak S(m-n)\ge2C_2>0\) uniformly. The prime number theorem gives

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

**Proof.** If \(F_n\) is composite, then there is no prime at any offset \(2\le m<p_{n+1}^2\). For every \(x\) in the integration range, \((x,x+h_n]\) lies inside that failed interval. Its von Mangoldt mass comes only from proper prime powers. The proof of Lemma 2.3 is translation-uniform throughout this range: each exponent \(k\ge2\) contributes at most one \(k\)-th power because consecutive \(k\)-th powers near \(P_n\) are separated by more than \(h_n\), and its weight is \(O(\log P_n/k)\). Summing over \(k\ll\log P_n\) gives \(O(\log P_n\log\log P_n)=o(h_n)\), uniformly in \(x\). Thus the absolute error is at least \(h_n/2\) throughout an interval of length \(y_n/4\), giving (8.2). Summing the resulting indicator inequality gives (8.3). \(\square\)

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

# Open analytic boundary

The direct arithmetic results isolate three sufficient variance estimates. None is proved in this paper.

For the unweighted prime-pair detector, the target is
\[
\boxed{
\sum_{j<N}|Z_j(H)-\lambda_j(H)|^2
\ll NX L(X),
\qquad L(X)=o(\log X),
}
\tag{12.1}
\]
where the Hardy--Littlewood expression (2.19) supplies the conjectural calibration \(\lambda_j(H)\asymp X\). Theorem 2.4 shows that (12.1) would exclude every failed centre in a sufficiently large dyadic block.

For the singly weighted detector, the corresponding target is
\[
\boxed{
\sum_{j<N}|Y_j(H)-\mu_j(H)|^2
\ll NHX L(X),
\qquad L(X)=o(\log X),
}
\tag{12.2}
\]
with conjectural calibration \(\mu_j(H)\asymp H\); Theorem 2.5 gives the deterministic implication.

For the double-von-Mangoldt source, an analytically natural sufficient target is
\[
\boxed{
\sum_{j<N}|T_j(H)-\nu_j(H)|^2
\ll NHX(\log X)^2L(X),
\qquad L(X)=o(\log X),
}
\tag{12.3}
\]
where \(\nu_j(H)=\mathfrak S(P_j)H\) is the conjectural Hardy--Littlewood calibration. Theorem 2.7 again turns this variance estimate into a no-failure statement.

Theorem 2.8 rewrites the double-von-Mangoldt variance exactly in Fourier variables. This does not solve (12.3): its source \(G_X=A_HB_X\) retains both prime weights and their common offset. A second possible representation starts from the shifted detector \(\Psi_j\), uses Proposition 2.3 to recenter it at the prime-pair scale \(\mu_j\), and keeps the prime-power remainder explicit. Either representation would require a new transference theorem before the reciprocal pair-sum frame of Sections 3--9 could become load-bearing for Fortune.

Thus the reciprocal residual bound analysed in this paper remains a well-defined deterministic model problem, not a proved equivalent of (12.1)--(12.3). The obstruction theorems explain why several natural attempts to build such a bridge fail, but they do not rule out every possible signed transference mechanism.

# Conclusion

At the square threshold relevant to Fortunate numbers, primorial-centre prime detection collapses to a prime-pair problem: a successful offset must itself be prime. This observation fixes the correct arithmetic source before any harmonic or sieve decomposition is attempted. The paper proves exact no-failure criteria for three versions of that source and an exact Fourier representation for the double-von-Mangoldt correlation. What remains open is the sparse-centre variance estimate at the required scale.

The reciprocal pair-sum analysis supplies a separate body of exact mathematics. Its one-sided harmonic decomposition, exact fourth moment, globally coupled Möbius truncation, semiprime resonance theorem, character-ratio collapse, sparse-centre coherence results and harmonic-scale conservation law sharply constrain possible transference arguments. In particular, positive density replacement, naive CRT de-tensorisation, ordinary large-value information and artificial enlargement of the harmonic family do not supply the missing prime-pair variance theorem.

The logical boundary is therefore explicit. Theorems 2.4, 2.5 and 2.7 are exact implications; the Hardy--Littlewood baselines are conjectural calibrations; the reciprocal-frame results are unconditional statements about that model; and no source-to-reciprocal transference theorem is known. No prime-pair asymptotic and no proof of Fortune's conjecture is claimed.

# AI-assistance disclosure

Large language models were used for literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. Every mathematical statement presented as a theorem is accompanied by a proof in the manuscript. Conjectural, conditional, computational, diagnostic and negative results are distinguished explicitly. The named author takes responsibility for the mathematical content, citations, code and final presentation.

# References

::: {#refs}
:::
