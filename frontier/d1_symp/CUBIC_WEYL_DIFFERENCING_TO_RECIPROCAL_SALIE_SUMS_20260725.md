# Cubic Weyl differencing reduces the Airy bound to two reciprocal Salié sums

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic `d=1` Airy wall, every odd prime `p`; application sector `p congruent 5 mod 6`.  
**Status:** the exact second-moment identity is **PROVED**. The two resulting square-root estimates are **OPEN**.

## 1. Setup

Let

\[
E=\mathbf F_{p^p},
\qquad
H=\{x\in E:\operatorname{Tr}(x)=0\},
\]

and let

\[
\Psi(z)=\psi(\operatorname{Tr}z).
\]

Put

\[
T_p=\sum_{x\in H}\Psi(x^3).
\]

Let `chi_E` and `chi` denote the quadratic characters of `E^*` and `F_p^*`, extended by zero at the origin. Let

\[
G_p=\sum_{c\in\mathbf F_p}\psi(c^2),
\qquad
G_p^2=\chi(-1)p.
\]

## 2. Exact Weyl-differencing identity

For `h in H`, define the quadratic hyperplane sum

\[
\mathcal G_H(h)
=
\sum_{z\in H}\Psi(3hz^2).
\]

### Theorem 2.1

\[
\boxed{
|T_p|^2
=
\sum_{h\in H}
\Psi\left(\frac{h^3}{4}\right)
\mathcal G_H(h).
}
\]

### Proof

Write `x=y+h`. Then

\[
x^3-y^3
=3hy^2+3h^2y+h^3
=3h\left(y+\frac h2\right)^2+\frac{h^3}{4}.
\]

Since `h in H`, translation by `h/2` preserves `H`. Summing over `(y,h)` gives the identity.

The term `h=0` is

\[
\mathcal G_H(0)=|H|=p^{p-1}.
\]

## 3. Exact quadratic Gauss evaluation

For `h!=0`, put

\[
\delta(h)=\operatorname{Tr}(h^{-1}).
\]

The bilinear form associated with `z -> Tr(3hz^2)` is

\[
B_h(z,w)=6\operatorname{Tr}(hzw).
\]

The orthogonal complement of `H` in `E` is the line

\[
\mathbf F_p h^{-1}.
\]

### Theorem 3.1: regular case

If `delta(h)!=0`, then

\[
\boxed{
\mathcal G_H(h)
=
\chi(-1)p^{(p-1)/2}
\chi_E(h)\chi(\delta(h)).
}
\]

### Proof

The orthogonal decomposition is

\[
E=H\perp\mathbf F_p h^{-1}.
\]

On the second factor the quadratic form is

\[
c\longmapsto3\delta(h)c^2.
\]

Therefore

\[
\sum_{z\in E}\Psi(3hz^2)
=
\mathcal G_H(h)\chi(3\delta(h))G_p.
\]

The full extension-field sum is

\[
\chi_E(3h)G_p^p
\]

by Hasse--Davenport. The factors `chi(3)` cancel, and

\[
G_p^{p-1}
=
\chi(-1)p^{(p-1)/2}.
\]

This proves the formula.

### Theorem 3.2: degenerate case

If `delta(h)=0`, then `F_p h^(-1)` is the radical of the quadratic form on `H`, and

\[
\boxed{
\mathcal G_H(h)
=
\chi_E(3h)G_p^p.
}
\]

### Proof

Choose a complement to the radical in `H` and a vector outside `H` pairing nontrivially with `h^(-1)`. The resulting two-dimensional plane is hyperbolic and has quadratic Gauss sum `p`. Both the full sum over `E` and the degenerate sum over `H` are `p` times the Gauss sum on the same nondegenerate complement. Hence they are equal.

## 4. Reciprocal Salié sums

Define

\[
\boxed{
\mathcal S_{\mathrm{reg}}(p)
=
\sum_{\substack{h\in H^*\\ \delta(h)\ne0}}
\chi_E(h)\chi(\delta(h))
\Psi\left(\frac{h^3}{4}\right)
}
\]

and

\[
\boxed{
\mathcal S_{\mathrm{deg}}(p)
=
\sum_{\substack{h\in H^*\\ \delta(h)=0}}
\chi_E(h)
\Psi\left(\frac{h^3}{4}\right).
}
\]

Substitution gives the exact theorem:

### Theorem 4.1

\[
\boxed{
\begin{aligned}
|T_p|^2
={}&p^{p-1}
+\chi(-1)p^{(p-1)/2}\mathcal S_{\mathrm{reg}}(p)\\
&+\chi(-1)\chi(3)p^{(p-1)/2}G_p
\mathcal S_{\mathrm{deg}}(p).
\end{aligned}
}
\]

The right-hand side is rational, although the two displayed Salié terms may individually lie in the quadratic Gauss field.

## 5. Polynomial form of the regular character

For `h!=0`,

\[
\operatorname{N}_{E/\mathbf F_p}(h)
\operatorname{Tr}(h^{-1})
\]

is the `(p-1)`-st elementary symmetric function of the Frobenius conjugates of `h`. Therefore

\[
\boxed{
\chi_E(h)\chi(\operatorname{Tr}(h^{-1}))
=
\chi\left(e_{p-1}(h,h^p,\ldots,h^{p^{p-1}})\right).
}
\]

Thus the regular sum has no genuine denominator: extending `chi(0)=0`,

\[
\mathcal S_{\mathrm{reg}}(p)
=
\sum_{h\in H}
\chi(e_{p-1}(h))
\Psi(h^3/4).
\]

The degenerate locus is exactly the divisor

\[
e_{p-1}(h)=0
\]

inside the trace-zero hyperplane.

## 6. Sufficient terminal theorem

The natural square-root estimates are

\[
\boxed{
|\mathcal S_{\mathrm{reg}}(p)|
\le C_1p^{(p-1)/2}
}
\]

and

\[
\boxed{
|\mathcal S_{\mathrm{deg}}(p)|
\le C_2p^{(p-2)/2}.
}
\]

If `C_1,C_2` are absolute, Theorem 4.1 gives

\[
|T_p|^2\le Cp^{p-1}
\]

and hence

\[
\boxed{|T_p|\le C' p^{(p-1)/2}.}
\]

This proves the required analytic half-theorem.

## 7. What has changed

The terminal Airy estimate is no longer only a cross-symmetric-power correlation problem. It is also equivalent, up to the exact identity above, to square-root cancellation in two explicit rank-one mixed character sums:

1. a cubic Artin--Schreier phase with quadratic character of the `(p-1)`-st elementary coefficient on `H`;
2. its reciprocal-trace-zero boundary divisor.

This is a potentially more tractable route because the coefficient sheaves are rank one. However, the ambient dimensions and divisor degrees grow with `p`; generic Deligne bounds do not automatically give an absolute constant.

## 8. Exact new wall

> **Uniform reciprocal Salié theorem.** Prove the two displayed square-root estimates with constants independent of `p`, exploiting the Artin--Schreier trace algebra and not merely generic Betti-number bounds.

A proof closes the analytic wall. A theorem that the corresponding primitive Betti or critical-point contribution grows superlinearly without further cancellation would close this route.

## 9. Verification

`cubic_weyl_salie_identity_verify.py` verifies the complete cyclotomic identity by direct enumeration in `F_(5^5)`.
