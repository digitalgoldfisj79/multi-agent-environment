# Explicit zero-frequency principal term

Date: 28 July 2026  
Status: exact zero-mode formula proved; asymptotic evaluation uses the classical prime number theorem zero-free-region estimates.

## 1. Weighted shifted source

Let `w_m` be deterministic real weights supported on `2<=m<=H`.  Put

\[
W_H=\sum_{m=2}^{H}w_m
\]

and

\[
L_j=\sum_{m=2}^{H}w_m\log(P_j+m).
\tag{1.1}
\]

For the sharp detector, `w_m=1` and `W_H=H-1`.

Use the exact Vaughan cutoff

\[
Y=\lfloor P_0^{1/3}\rfloor>H
\]

and write

\[
S_\mu(T)=\sum_{n\le T}\frac{\mu(n)}n,
\qquad
S_{\mu\log}(T)=\sum_{n\le T}\frac{\mu(n)\log n}{n},
\qquad
S_\Lambda(T)=\sum_{n\le T}\frac{\Lambda(n)}n.
\tag{1.2}
\]

For a divisibility condition `q|P_j+m`, additive orthogonality gives a zero
frequency equal to `W_H/q`.  In the Type I term the logarithmic weight gives the
zero frequency

\[
\frac1d\sum_m w_m\log\frac{P_j+m}{d}
=
\frac{L_j-W_H\log d}{d}.
\tag{1.3}
\]

## 2. Exact Type I zero mode

The Type I source is

\[
\sum_{d\le Y}\mu(d)
\sum_{m}w_m\mathbf1_{d\mid P_j+m}
\log\frac{P_j+m}{d}.
\]

### Proposition 2.1

Its zero-frequency contribution is exactly

\[
\boxed{
M_{I,j}
=
L_jS_\mu(Y)-W_HS_{\mu\log}(Y).
}
\tag{2.1}
\]

This is immediate from (1.3).

## 3. Exact subtraction zero mode

The subtraction term is

\[
-
\sum_{d\le Y}\sum_{c\le Y}
\mu(d)\Lambda(c)
\sum_m w_m\mathbf1_{dc\mid P_j+m}.
\]

### Proposition 3.1

Its zero-frequency contribution is exactly

\[
\boxed{
M_{II}
=-W_HS_\mu(Y)S_\Lambda(Y).
}
\tag{3.1}
\]

The product factorisation is exact because the modulus is `dc` and the zero mode
is `W_H/(dc)`.

## 4. Exact large-large zero mode

Put

\[
Z_j=P_j+H.
\]

The large-large term is

\[
\sum_{a>Y}\sum_{c>Y}
\mu(a)\Lambda(c)
\sum_mw_m\mathbf1_{ac\mid P_j+m}.
\]

Only products `ac<=Z_j` occur in the original finite convolution.

### Proposition 4.1

Its zero-frequency contribution is exactly

\[
\boxed{
M_{III,j}
=
W_H
\sum_{\substack{c>Y\\c\le Z_j/Y}}
\frac{\Lambda(c)}c
\left[
S_\mu(Z_j/c)-S_\mu(Y)
\right].
}
\tag{4.1}
\]

### Proof

The zero mode for fixed `(a,c)` is `W_H/(ac)`.  Sum first over

\[
Y<a\le Z_j/c.
\]

The inner sum is exactly the bracket in (4.1).  \(\square\)

## 5. Complete principal term

### Theorem 5.1 (exact zero-frequency baseline)

The zero-frequency contribution of the full signed Vaughan source is

\[
\boxed{
\mu_j^{(0)}
=
M_{I,j}+M_{II}+M_{III,j}.
}
\tag{5.1}
\]

No Hardy--Littlewood conjecture enters this identity.

## 6. Classical asymptotic evaluation

The classical zero-free region for the Riemann zeta function gives, for some
absolute `c>0`,

\[
S_\mu(T)
\ll
\exp\left(
-c(\log T)^{3/5}(\log\log T)^{-1/5}
\right),
\tag{6.1}
\]

and partial summation gives

\[
S_{\mu\log}(T)
=-1+
O\left(
\exp\left(
-c(\log T)^{3/5}(\log\log T)^{-1/5}
\right)
\right).
\tag{6.2}
\]

Also

\[
S_\Lambda(T)=\log T+O(1).
\tag{6.3}
\]

Since

\[
\log Y=\frac13\log P_0+O(1)\asymp X,
\]

the error in (6.1)--(6.2) is smaller than every negative power of `X`.
Moreover

\[
L_j\ll W_HX
\]

uniformly in the dyadic block.

For (4.1), let

\[
E(Y)=
\sup_{T\ge Y}|S_\mu(T)|.
\]

Then

\[
|S_\mu(Z_j/c)-S_\mu(Y)|\le2E(Y)
\]

and

\[
\sum_{c\le Z_j/Y}\frac{\Lambda(c)}c
\ll\log Z_j\ll X.
\]

Therefore

\[
M_{III,j}\ll W_HX E(Y)=o(W_H).
\tag{6.4}
\]

Combining (2.1), (3.1), and (4.1) gives:

### Corollary 6.1 (uniform positive principal term)

Uniformly for all centres in the dyadic primorial block,

\[
\boxed{
\mu_j^{(0)}
=W_H+o(W_H).
}
\tag{6.5}
\]

In particular, for sufficiently large `X`,

\[
\frac12W_H
\le
\mu_j^{(0)}
\le
\frac32W_H.
\tag{6.6}
\]

For the sharp detector, this is `mu_j^(0)=H+o(H)`.

## 7. Consequence for the Fortune programme

The required positive baseline no longer needs to be inserted heuristically.  It
is the zero-frequency term produced by the exact signed source decomposition.

Define the nonzero-mode residual by

\[
\mathcal E_j
=
\sum_mw_m\Lambda(P_j+m)-\mu_j^{(0)}.
\tag{7.1}
\]

The remaining theorem is purely nonzero-frequency:

\[
\sum_{j<N}|\mathcal E_j|^2
\ll NHX L(X),
\qquad
L(X)=o(\log X).
\tag{7.2}
\]

Together with (6.6), the one-sided shifted-detector criterion excludes every failed
centre.

Thus principal subtraction is now exact and uniform.  The sole remaining analytic
problem is cancellation in the nonzero reciprocal modes of the three orbit-column
source.

## 8. Boundary

Proved internally:

1. exact zero-mode formulas (2.1), (3.1), (4.1), and (5.1);
2. reduction of the principal term to classical summatory functions.

Invoked published input:

1. the classical zeta zero-free-region bounds (6.1)--(6.3).

Open:

1. the nonzero-mode variance estimate (7.2);
2. Fortune's conjecture.
