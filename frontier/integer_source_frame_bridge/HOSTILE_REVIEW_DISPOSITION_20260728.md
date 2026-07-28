# Hostile review disposition: centred source-to-frame identity

Date: 28 July 2026  
Reviewer job: `6a6850076026358f6401918c`  
Model: `Qwen/Qwen3-14B-AWQ`

## Disposition

The review returned `REQUIRES AMENDMENT`.  It found no failed algebraic identity.
Its five adverse findings are either contradicted by hypotheses printed in the
reviewed note or are requests to display one-line inequalities already implicit
in the definitions.  The exact theorem package is retained.  The omitted
one-line verifications are recorded below for auditability.

## Finding 1: `L(X)=o(log X)`

The reviewer wrote that

> the deduction that `L(X)/log X=o(1)` is not universally valid unless `L(X)`
> is strictly sublogarithmic.

The theorem states, in the hypothesis itself,

\[
L(X)=o(\log X).
\]

By the definition of little-o, this is exactly

\[
L(X)/\log X\longrightarrow0.
\]

The review's counterexample `L(X)=log X` violates the printed hypothesis.

**Disposition:** false adverse finding; no amendment required.

## Finding 2: baseline lower bound

The reviewer claimed that the distribution of \(\mu_j\) was not bounded in the
required way.  Immediately before Theorem 2.1 the note assumes uniformly

\[
cH\le\mu_j\le CH.
\]

Only the lower bound is used in the failure argument.  No regularity or
Hardy--Littlewood asymptotic is assumed.

**Disposition:** false adverse finding; the required hypothesis is explicit.

## Finding 3: positive-harmonic mass

Paper II defines

\[
p_{q,a}=w_{q,a}/D_X,
\qquad
D_X=\sum_q\sum_{a\ne0}w_{q,a},
\]

with \(w_{q,-a}=w_{q,a}\).  Hence

\[
\sum_{q,a\ne0}p_{q,a}=1,
\qquad
\sum_{a\ge1}m_a
 =\sum_{a\ge1}\sum_qp_{q,a}=\frac12.
\]

No extra hypothesis is needed beyond the symmetric row definition explicitly
invoked in the note.

**Disposition:** proved.

## Finding 4: kernel range

For every positive harmonic,

\[
|\Theta_{a,X}(L)|
 \le\sum_qp_{q,a}=m_a
\]

by the triangle inequality.  Therefore

\[
0\le\mathcal K_X(L)
 =2\sum_a\frac{|\Theta_{a,X}(L)|^2}{m_a}
 \le2\sum_am_a=1.
\]

At \(L=0\), equality holds termwise:
\(\Theta_{a,X}(0)=m_a\), so \(\mathcal K_X(0)=1\).

**Disposition:** proved; the review requested an expanded one-line proof, not a
mathematical correction.

## Finding 5: pair lift and diagonal masses

From

\[
C_X(\theta)=\sum_jc_je(P_j\theta)
\]

one obtains exactly

\[
C_X(\theta)^2
 =\sum_jc_j^2e(2P_j\theta)
  +2\sum_{j<k}c_jc_ke((P_j+P_k)\theta).
\]

This is equation (6.1).  For

\[
d_{jk}=\sqrt{2-\delta_{jk}}c_jc_k,
\]

\[
\begin{aligned}
\sum_{j\le k}|d_{jk}|^2
 &=\sum_j|c_j|^4+2\sum_{j<k}|c_j|^2|c_k|^2\\
 &=\left(\sum_j|c_j|^2\right)^2.
\end{aligned}
\]

For the literal square coefficients
\(w_{jk}=(2-\delta_{jk})c_jc_k\),

\[
\begin{aligned}
\sum_{j\le k}|w_{jk}|^2
 &=\sum_j|c_j|^4+4\sum_{j<k}|c_j|^2|c_k|^2\\
 &=2\left(\sum_j|c_j|^2\right)^2-\sum_j|c_j|^4.
\end{aligned}
\]

Expanding the reciprocal-row square then gives Theorem 6.1 exactly, with the
same kernel as Theorem 4.1.

**Disposition:** proved.

## Review value

The review correctly confirmed as proved:

- the centred source projection and Parseval identity;
- the centred dual-row identity;
- Hermitian positive semidefiniteness;
- the coefficient-erasure no-go;
- the source-weighted pair-sum identity.

Its useful contribution was to identify normalisation steps that should remain
visible in the audit record.  It did not identify a theorem-level error.

## Final classification

**INTERNAL EXACT-IDENTITY PASS.**

The open statements remain analytic estimates, not hidden assumptions:

1. lower-frame stability, now reduced to the distinct-modulus single-walk mass;
2. the centred source-frame upper bound at the all-centres variance scale.

No proof of Fortune's conjecture is claimed.
