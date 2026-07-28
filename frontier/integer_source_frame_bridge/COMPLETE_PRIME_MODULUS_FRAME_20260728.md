# Complete prime-modulus frame for the centred Fortune source

Date: 28 July 2026  
Status: exact finite identity and unconditional uniform frame stability proved.

## 1. Purpose

The reciprocal frame from `CENTRED_SOURCE_TO_FRAME_IDENTITY_20260728.md`
preserves the detector residuals, but its lower-frame estimate was reduced to a
new reciprocal-fraction dispersion theorem.  That theorem is not necessary.

A complete additive-character frame at prime moduli on the critical shell has
an exact arithmetic Gram kernel whose off-diagonal entries can be bounded by
factor counting.  This closes the lower-frame side unconditionally.

Let

\[
c_j=\Psi_j(H)-\mu_j,
\qquad
C_X(\theta)=\sum_{j<N}c_j e(P_j\theta),
\]

where `cH <= mu_j <= CH`, `H=eta X^2`, and

\[
P_j=A_X\prod_{u=1}^j\ell_u
\]

is the primorial-prefix block.  Let

\[
\mathcal Q_X=\{q\text{ prime}:H\le q<2H\},
\qquad Q_X=|\mathcal Q_X|.
\]

## 2. Exact complete-modulus frame

Define

\[
\boxed{
\mathfrak D_X(c)
 =\frac1{Q_X}\sum_{q\in\mathcal Q_X}\frac1q
  \sum_{a\bmod q}\left|C_X\!\left(\frac aq\right)\right|^2.
}
\tag{2.1}
\]

For an integer `L`, put

\[
\Delta_X(L)=\frac1{Q_X}\#\{q\in\mathcal Q_X:q\mid L\}.
\tag{2.2}
\]

Thus `Delta_X(0)=1`.

### Theorem 2.1 (complete prime-modulus dual-row identity)

One has exactly

\[
\boxed{
\mathfrak D_X(c)
 =\sum_{j,k<N}c_j\overline{c_k}\,\Delta_X(P_j-P_k).
}
\tag{2.3}
\]

In particular, if

\[
\mathbf D_X=(\Delta_X(P_j-P_k))_{j,k<N},
\]

then

\[
\mathfrak D_X(c)=c^*\mathbf D_Xc,
\qquad
(\mathbf D_X)_{jj}=1.
\tag{2.4}
\]

### Proof

Expand the square in (2.1) and use complete additive orthogonality:

\[
\frac1q\sum_{a\bmod q}e\!\left(\frac{a(P_j-P_k)}q\right)
 =\mathbf 1_{q\mid P_j-P_k}.
\]

Average over `q`.  All sums are finite.  \(\square\)

The identity is also an exact source frame, because

\[
C_X(\theta)
 =\int_0^1\mathscr R_X(\alpha)F_X(\theta-\alpha)\,d\alpha
\]

with the baseline already subtracted in `mathscr R_X`.

## 3. Off-diagonal divisor reduction

For `j<k`, write

\[
U_{j,k}=\prod_{j<u\le k}\ell_u,
\qquad P_k=P_jU_{j,k}.
\tag{3.1}
\]

Every prime factor of `P_j` is below `2X`, whereas every
`q in mathcal Q_X` satisfies `q >= H >> 2X`.  Hence `(q,P_j)=1` and

\[
\boxed{
q\mid P_k-P_j
\quad\Longleftrightarrow\quad
q\mid U_{j,k}-1.
}
\tag{3.2}
\]

This removes the enormous primorial factor completely.

### Lemma 3.1 (shell-divisor count)

For `j<k`,

\[
\#\{q\in\mathcal Q_X:q\mid P_k-P_j\}
 \le
 \frac{(k-j)\log(2X)}{\log H}.
\tag{3.3}
\]

### Proof

The relevant shell primes are distinct divisors of the positive integer
`U_{j,k}-1`.  Their product is at least `H^r` if there are `r` of them.  Since

\[
U_{j,k}-1<U_{j,k}\le(2X)^{k-j},
\]

we have `r log H < (k-j) log(2X)`.  \(\square\)

Consequently,

\[
0\le\Delta_X(P_j-P_k)
 \le
 \frac{|j-k|\log(2X)}{Q_X\log H}.
\tag{3.4}
\]

## 4. Unconditional uniform frame stability

Let

\[
R_j=\sum_{k\ne j}\Delta_X(P_j-P_k).
\]

By (3.4),

\[
R_j
 \le
 \frac{\log(2X)}{Q_X\log H}
 \left(\sum_{h=1}^{j}h+\sum_{h=1}^{N-1-j}h\right)
 \le
 \frac{N(N-1)\log(2X)}{2Q_X\log H}.
\tag{4.1}
\]

The prime number theorem and `H asymp X^2`, `N asymp X/log X` give

\[
Q_X\asymp\frac{H}{\log H}
\]

and therefore

\[
\boxed{
\max_j R_j\ll\frac1{\log X}.
}
\tag{4.2}
\]

### Theorem 4.1 (near-Parseval complete-modulus frame)

Uniformly for every complex vector `c`,

\[
\boxed{
\left(1-O\!\left(\frac1{\log X}\right)\right)\|c\|_2^2
 \le \mathfrak D_X(c)
 \le
\left(1+O\!\left(\frac1{\log X}\right)\right)\|c\|_2^2.
}
\tag{4.3}
\]

In particular, for all sufficiently large `X`,

\[
\mathfrak D_X(c)\ge\frac12\|c\|_2^2.
\tag{4.4}
\]

### Proof

The matrix `D_X-I` is real symmetric, has zero diagonal and nonnegative
off-diagonal entries.  Hence

\[
\|\mathbf D_X-I\|_{\mathrm{op}}
 \le\max_j R_j
 \ll1/\log X
\]

by the maximum-row-sum bound.  Apply the spectral theorem.  \(\square\)

This theorem is unconditional apart from standard prime-number-theorem input
for the shell cardinality.

## 5. Direct consequence for the Fortune route

The lower-frame boulder is closed.  It is sufficient to prove the complete-grid
source-energy estimate

\[
\boxed{
\mathfrak D_X(c)
 \ll NHX L(X),
\qquad L(X)=o(\log X).
}
\tag{5.1}
\]

Indeed, Theorem 4.1 gives

\[
\sum_{j<N}|\Psi_j(H)-\mu_j|^2
 =\|c\|_2^2
 \ll\mathfrak D_X(c)
 \ll NHX L(X),
\]

and the one-sided shifted-detector criterion then excludes every failed centre.

At row level, (5.1) is

\[
\frac1{Q_X}\sum_{q\in\mathcal Q_X}\frac1q
\sum_{a\bmod q}
\left|
\int_0^1\mathscr R_X(\alpha)
F_X\!\left(\frac aq-\alpha\right)d\alpha
\right|^2
\ll NHX L(X).
\tag{5.2}
\]

This is a complete additive-modulus sampling theorem for the centred prime
source.  It is the sole remaining integer-side analytic estimate in this frame.

## 6. Relation to the reciprocal frame

The reciprocal frame and its exact identities remain valid, but its separate
single-walk dispersion theorem is no longer required for Fortune.  Complete
additive orthogonality gives a stronger and unconditional lower frame.

The old coefficient-free pair frame and Paper IV derandomisation remain
secondary.  Weighted pair geometry should be used only if it contributes to the
source-energy estimate (5.1).

## 7. Boundary

Proved:

1. exact centred complete-modulus source-to-frame identity;
2. exact reduction of off-diagonal collisions to shell divisors of
   `U_{j,k}-1`;
3. unconditional `1-O(1/log X)` uniform frame bounds.

Open:

1. the centred source-energy estimate (5.1);
2. the construction and cancellation of its explicit prime-pair principal term.

No proof of Fortune's conjecture is claimed.