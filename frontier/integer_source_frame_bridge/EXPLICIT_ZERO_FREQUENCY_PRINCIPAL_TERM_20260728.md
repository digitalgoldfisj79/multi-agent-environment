# Explicit zero-frequency principal term

Date: 28 July 2026  
Status: exact zero-mode formula proved; uniform positivity uses classical zeta zero-free-region estimates.

## 1. Weighted source and hypotheses

Let `w_m` be deterministic **nonnegative** real weights supported on
`2<=m<=H`, and assume

\[
W_H=\sum_{m=2}^{H}w_m>0.
\]

Put

\[
L_j=\sum_{m=2}^{H}w_m\log(P_j+m).
\]

The exact formulas below remain valid for arbitrary real weights.  Nonnegativity is
used only for the uniform estimate `L_j<<W_H X` and the positive lower bound on the
principal term.

For the sharp detector `w_m=1`, so `W_H=H-1`.  For the symmetric source one may
take `w_m=Lambda(m)`, for which the prime number theorem gives `W_H~H`.

Use

\[
Y=\lfloor P_0^{1/3}\rfloor>H
\]

and define

\[
S_\mu(T)=\sum_{n\le T}\frac{\mu(n)}n,
\quad
S_{\mu\log}(T)=\sum_{n\le T}\frac{\mu(n)\log n}{n},
\quad
S_\Lambda(T)=\sum_{n\le T}\frac{\Lambda(n)}n.
\]

## 2. Exact zero modes

The Type I part has exact zero-frequency contribution

\[
\boxed{
M_{I,j}=L_jS_\mu(Y)-W_HS_{\mu\log}(Y).
}
\tag{2.1}
\]

Indeed the zero additive character for a fixed `d<=Y` is

\[
\frac1d\sum_m w_m\log\frac{P_j+m}{d}
=
\frac{L_j-W_H\log d}{d}.
\]

The Vaughan subtraction term has exact zero mode

\[
\boxed{
M_{II}=-W_HS_\mu(Y)S_\Lambda(Y).
}
\tag{2.2}
\]

For the large-large term put `Z_j=P_j+H`.  Its finite product condition is
`ac<=Z_j`, and its exact zero mode is

\[
\boxed{
M_{III,j}
=
W_H\sum_{Y<c\le Z_j/Y}
\frac{\Lambda(c)}c
\left[S_\mu(Z_j/c)-S_\mu(Y)\right].
}
\tag{2.3}
\]

Thus the exact principal term produced by the signed Vaughan source is

\[
\boxed{
\mu_j^{(0)}=M_{I,j}+M_{II}+M_{III,j}.
}
\tag{2.4}
\]

No Hardy--Littlewood conjecture enters (2.1)--(2.4).

## 3. Uniform asymptotic evaluation

The classical zero-free region for `zeta(s)` gives, for some absolute `c>0`,

\[
S_\mu(T)
\ll
\exp\!\left[-c(\log T)^{3/5}(\log\log T)^{-1/5}\right],
\tag{3.1}
\]

\[
S_{\mu\log}(T)
=-1+O\!\left(
\exp\!\left[-c(\log T)^{3/5}(\log\log T)^{-1/5}\right]
\right),
\tag{3.2}
\]

and

\[
S_\Lambda(T)=\log T+O(1).
\tag{3.3}
\]

Since `log Y asymp X`, these errors are smaller than every negative power of `X`.
For nonnegative weights,

\[
L_j\ll W_HX
\]

uniformly in the dyadic primorial block.  Hence (2.1) gives

\[
M_{I,j}=W_H+o(W_H),
\]

and (2.2) gives `M_II=o(W_H)`.

For (2.3), let

\[
E(Y)=\sup_{T\ge Y}|S_\mu(T)|.
\]

Then

\[
|M_{III,j}|
\ll
W_HE(Y)\sum_{c\le Z_j/Y}\frac{\Lambda(c)}c
\ll W_HX E(Y)
=o(W_H).
\]

Therefore:

### Theorem 3.1 (uniform positive baseline)

For nonnegative weights with `W_H>0`, uniformly over the dyadic block,

\[
\boxed{
\mu_j^{(0)}=W_H+o(W_H).
}
\tag{3.4}
\]

In particular, for sufficiently large `X`,

\[
\boxed{
\frac12W_H\le\mu_j^{(0)}\le\frac32W_H.
}
\tag{3.5}
\]

For the sharp detector this is `mu_j^(0)=H+o(H)`.

## 4. Exact remaining target

Define

\[
\mathcal E_j
=
\sum_{m=2}^{H}w_m\Lambda(P_j+m)-\mu_j^{(0)}.
\]

All zero-frequency terms have now been removed exactly.  The remaining theorem is
purely nonzero-frequency:

\[
\boxed{
\sum_{j<N}|\mathcal E_j|^2
\ll NHX L(X),
\qquad L(X)=o(\log X).
}
\tag{4.1}
\]

For the sharp detector, (3.5) and (4.1) imply the corrected all-centres criterion
and therefore Fortune for all sufficiently large centres.

## 5. Boundary

Proved internally:

1. exact formulas (2.1)--(2.4);
2. reduction of the baseline to classical summatory functions.

Published input invoked:

1. the classical prime-number-theorem zero-free-region estimates (3.1)--(3.3).

Open:

1. the nonzero-mode variance estimate (4.1);
2. Fortune's conjecture.
