# Frobenius convention and primitive Betti audit for the twisted `(2,3)` model

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** the convention statement and primitive Betti formula below are **PROVED**. They sharpen the main analytic target and prevent a false bounded-rank interpretation.

## 0. Result

Let

\[
X_p=X_p^{\mathrm{AS}}
\subset\mathbf P^{p-3}
\]

be the smooth complete intersection of type `(2,3)` from
`TWISTED_DESCENT_AND_PRIMITIVE_TRACE_IDENTITY_20260724.md`. Its dimension is

\[
m=p-5.
\]

Then

\[
\boxed{
\dim H^{p-5}_{\mathrm{prim}}
(X_{p,\overline{\mathbf F}_p},\mathbf Q_\ell)
=
\frac{2^{p-1}-1}{3}.
}
\]

Consequently, the exact identity

\[
T_p=p^2\operatorname{Tr}
\left(F_p\mid H^{p-5}_{\mathrm{prim}}(X_p)\right)
\]

is a trace on an exponentially growing space. The desired estimate

\[
|T_p|\le C p^{(p-1)/2}
\]

cannot follow from a bounded-rank interpretation of the primitive motive. It requires cancellation among

\[
\frac{2^{p-1}-1}{3}
\]

weight-`p-5` Frobenius eigenvalues, or an independent virtual/correspondence mechanism cancelling them before the trace is taken.

This is directly on the main analytic branch: it identifies the exact size of the sole remaining cohomology group in the smooth linear-section formulation.

## 1. Frobenius convention

There are two related actions.

1. On geometric points, **arithmetic Frobenius** is the `p`-power map.
2. In the standard Grothendieck--Lefschetz point-count formula, the cohomological operator is **geometric Frobenius**, the inverse of arithmetic Frobenius.

Under the splitting

\[
K\otimes_{\mathbf F_p}\overline{\mathbf F}_p
\cong
\overline{\mathbf F}_p^p,
\]

the arithmetic descent action is a cyclic shift composed with coordinatewise `p`-power Frobenius. Therefore the geometric Frobenius acting in the trace formula becomes the corresponding inverse cyclic shift composed with geometric coordinate Frobenius.

Reversing the order of the `p` embeddings conjugates `sigma` to `sigma^{-1}` and preserves

\[
\sum x_i,
\qquad
\sum x_i^2,
\qquad
\sum x_i^3.
\]

Hence the two cyclic orientations are conjugate on the complete intersection and have the same cohomological trace. The exact safe formulation is:

\[
\boxed{
T_p=p^2\operatorname{Tr}
\left(
F_{p,\mathrm{geom}}
\mid H^{p-5}_{\mathrm{prim}}(X_p^{\mathrm{AS}})
\right)
}
\]

or, on the split model,

\[
\boxed{
T_p=p^2\operatorname{Tr}
\left(
\sigma^{\pm1}F_{p,\mathrm{geom}}
\mid H^{p-5}_{\mathrm{prim}}(X_p^{\mathrm{perm}})
\right).
}
\]

No inversion of Frobenius eigenvalues is being declared harmless; only the cyclic orientation `sigma` versus `sigma^{-1}` is harmless by conjugacy.

## 2. Euler characteristic of a `(2,3)` complete intersection

Put

\[
N=p-3,
\qquad
m=N-2=p-5.
\]

For a smooth complete intersection of degrees `2` and `3` in `P^N`, the total Chern class is

\[
c(TX_p)
=
\frac{(1+H)^{N+1}}{(1+2H)(1+3H)}.
\]

Since the degree of `X_p` is `6`, Gauss--Bonnet gives

\[
\chi(X_p)
=
6[H^m]
\frac{(1+H)^{m+3}}{(1+2H)(1+3H)}.
\]

Use

\[
\frac1{(1+2H)(1+3H)}
=-\frac2{1+2H}+\frac3{1+3H}.
\]

Write

\[
S_c=[H^m]\frac{(1+H)^{m+3}}{1+cH}.
\]

Because `m` is even and `n=m+3=p-2` is odd, completing the truncated binomial sum gives

\[
S_2=\frac{(n-1)^2}{4}
\]

and

\[
S_3=\frac{2^n+1}{27}+\frac{n(3n-5)}{18}.
\]

Therefore

\[
[H^m]
\frac{(1+H)^{m+3}}{(1+2H)(1+3H)}
=-2S_2+3S_3
=
\frac{m}{6}+\frac{2^{p-1}+2}{18}.
\]

Multiplying by `6` yields

\[
\boxed{
\chi(X_p)
=
m+\frac{2^{p-1}+2}{3}.
}
\]

Equivalently,

\[
\chi(X_p)
=
p-4+\frac{2^{p-1}-1}{3}.
\]

## 3. Primitive middle Betti number

Weak Lefschetz and Poincare duality show that all cohomology outside degree `m` agrees with projective space. Since `m` is even, the total contribution of the ambient projective cohomology to the Euler characteristic is

\[
m+1=p-4.
\]

Thus

\[
\dim H^m_{\mathrm{prim}}(X_p)
=
\chi(X_p)-(m+1)
=
\frac{2^{p-1}-1}{3}.
\]

This proves the displayed rank formula.

Exact values begin

| `p` | `dim X_p` | primitive rank |
|---:|---:|---:|
| 5 | 0 | 5 |
| 7 | 2 | 21 |
| 11 | 6 | 341 |
| 13 | 8 | 1365 |
| 17 | 12 | 21845 |

## 4. Consequence for the two main branches

### Analytic branch

The smooth complete-intersection formulation has removed singularities, main terms and Tate factors, but it has not reduced rank. The remaining theorem is an exponentially large twisted trace cancellation:

\[
\left|
\operatorname{Tr}
\left(
\sigma^{\pm1}F_{p,\mathrm{geom}}
\mid H^{p-5}_{\mathrm{prim}}(X_p^{\mathrm{perm}})
\right)
\right|
\le C p^{(p-5)/2}.
\]

A successful proof must exploit the cyclic descent operator or exhibit a virtual cancellation. Generic Weil bounds lose the factor

\[
\frac{2^{p-1}-1}{3}.
\]

### Application branch

The primitive rank formula also prevents identifying this entire primitive motive with the empirically `O(p)` post-pushforward hook survivor. Any valid hook comparison must be virtual, filtered, or trace-level: it must cancel almost all of the primitive cohomology rather than carry it injectively into an `O(p)` object.

Thus the next admissible application step is specific:

> construct a correspondence or spectral-sequence map whose cone accounts for the exponential primitive part and whose surviving trace is the zero-frequency hook constituent, with the `q=2`, `q=infinity`, twist and Artin--Schreier cells explicit.

Merely matching dimensions or first traces cannot do this.

## 5. Verification

`twisted_descent_betti_verify.py` computes the Chern-class coefficient exactly and verifies

\[
b^{\mathrm{prim}}_{p-5}=\frac{2^{p-1}-1}{3}
\]

for odd primes through `p=199`. This is a regression check of the closed coefficient calculation above.
