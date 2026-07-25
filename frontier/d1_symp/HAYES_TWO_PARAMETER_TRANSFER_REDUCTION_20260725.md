# Hayes two-parameter transfer reduction of the combined projective sum

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic `d=1` Airy wall, primes `p congruent 5 mod 6`, `p>=11`.  
**Status:** the exact reduction is **PROVED**, using the published Hayes/Hsu Riemann hypothesis for prescribed-coefficient character `L`-functions. The final two-parameter correlation bound is **OPEN**.

## 1. Hayes characters

Let `P` be a monic polynomial over `F_p` with nonzero constant term, and let its roots, with multiplicity, be `alpha`. Define

\[
s_1(P)=\sum_\alpha\alpha,
\qquad
s_3(P)=\sum_\alpha\alpha^3,
\qquad
r_1(P)=\sum_\alpha\alpha^{-1},
\]

and let

\[
n(P)=\prod_\alpha\alpha.
\]

For `u,w,v in F_p`, put

\[
\boxed{
\Theta_{u,w,v}(P)
=
\chi(n(P))
\psi\left(us_1(P)+ws_3(P)+vr_1(P)\right).
}
\]

The four root statistics are additive or multiplicative under polynomial multiplication, so `Theta_(u,w,v)` is a character of the Hayes equivalence group with three leading and two trailing coefficients.

The norm character is quadratic and nontrivial, so every `Theta_(u,w,v)` is nontrivial.

## 2. Published bounded-degree L-functions

The Hayes/Hsu theory of irreducible polynomials with prescribed leading and trailing coefficients attaches

\[
L(z,\Theta_{u,w,v})
=
\prod_P
\left(1-\Theta_{u,w,v}(P)z^{\deg P}\right)^{-1}.
\]

For a nontrivial character with `ell=3` and `t=2`, this is a polynomial of degree at most

\[
\ell+t-1=4.
\]

Write

\[
L(z,\Theta_{u,w,v})
=
\prod_{j=1}^{d(u,w,v)}(1-\alpha_j(u,w,v)z).
\]

The prescribed-coefficient Riemann hypothesis gives

\[
|\alpha_j(u,w,v)|=\sqrt p.
\]

References:

- D. Hayes, *The distribution of irreducibles in GF[q,x]*, 1965.
- Zhicheng Gao, *Improved error bounds for the number of irreducible polynomials and self-reciprocal irreducible monic polynomials with prescribed coefficients over a finite field*, 2021, arXiv:2109.14154.

## 3. Prime-degree Fourier coefficient

Let

\[
I_p(u,w,v)
=
\sum_{\substack{P\text{ monic irreducible}\\ \deg P=p}}
\Theta_{u,w,v}(P).
\]

The logarithmic derivative of the Euler product gives

\[
pI_p(u,w,v)
+
\sum_{\deg L=1}\Theta_{u,w,v}(L^p)
=
-
\sum_{j=1}^{d(u,w,v)}\alpha_j(u,w,v)^p.
\]

For a linear polynomial with nonzero constant term, the `p`-th power has zero first, third and reciprocal power sums in characteristic `p`, while its norm remains the base-field root. Hence

\[
\sum_{\deg L=1}\Theta_{u,w,v}(L^p)
=
\sum_{a\in\mathbf F_p^*}\chi(a)=0.
\]

Therefore

\[
\boxed{
I_p(u,w,v)
=-\frac1p
\sum_{j=1}^{d(u,w,v)}
\alpha_j(u,w,v)^p.
}
\]

In particular,

\[
|I_p(u,w,v)|\le4p^{(p-2)/2}.
\]

This is the exact bounded-state local transfer representation.

## 4. Scaling law

Scaling every root by `lambda in F_p^*` permutes the degree-`p` irreducible polynomials and gives

\[
\boxed{
I_p(u,w,v)
=
\chi(\lambda)
I_p(u\lambda,w\lambda^3,v\lambda^{-1}).
}
\]

## 5. Two parameter sums

Define

\[
\mathcal A_p
=
\sum_{u,w\in\mathbf F_p}I_p(u,w,1),
\]

\[
\mathcal B_p
=
\sum_{u,v\in\mathbf F_p}I_p(u,1,v).
\]

### Theorem 5.1

\[
\boxed{
\mathcal R_0(p)=\frac{\mathcal A_p}{pG_p},
\qquad
\mathcal D(p)=\frac{\mathcal B_p}{pG_p}.
}
\]

### Proof

Let `Sigma_0` be the signed sum over degree-`p` irreducible polynomials with

\[
s_1(P)=s_3(P)=0
\]

and weight

\[
\chi(n(P))\chi(r_1(P)).
\]

Additive orthogonality and the quadratic Gauss expansion give

\[
\Sigma_0
=
\frac1{p^2G_p}
\sum_{u,w}
\sum_{v\ne0}
\chi(v)I_p(u,w,v).
\]

Use the scaling law with `lambda=v`. The two quadratic characters cancel, and reindexing `(u,w)` gives

\[
\Sigma_0
=
\frac{p-1}{p^2G_p}\mathcal A_p.
\]

Each scaling class of irreducible polynomials contributes `p-1` polynomials and corresponds to `p` Frobenius-conjugate projective root lines. Therefore

\[
(p-1)\mathcal R_0(p)=p\Sigma_0,
\]

which proves the first identity.

For `D`, use the constraints

\[
s_1(P)=r_1(P)=0
\]

and weight

\[
\chi(n(P))\chi(s_3(P)).
\]

Expanding the quadratic character of `s_3`, then scaling by the unique `lambda` satisfying `w lambda^3=1`, gives

\[
\Sigma_D
=
\frac{p-1}{p^2G_p}\mathcal B_p.
\]

The same polynomial/projective-line incidence gives the second identity.

## 6. Exact low-dimensional terminal identity

The exact Salié cancellation theorem gives

\[
T_p^2
=
p^{(p+1)/2}
\left(
\chi(-1)\mathcal R_0(p)
+
\chi(3)\mathcal D(p)
\right).
\]

Substituting Theorem 5.1 yields

\[
\boxed{
T_p^2
=
\frac{p^{(p-1)/2}}{G_p}
\left(
\chi(-1)\mathcal A_p
+
\chi(3)\mathcal B_p
\right).
}
\]

Equivalently, the desired Airy estimate follows from

\[
\boxed{
\left|
\chi(-1)\mathcal A_p
+
\chi(3)\mathcal B_p
\right|
\le C p^{p/2}.
}
\]

## 7. What generic prescribed-coefficient bounds provide

The pointwise estimate for `I_p` and the triangle inequality give only

\[
|\mathcal A_p|+|\mathcal B_p|
\le8p^{(p+2)/2},
\]

which loses a factor `p` relative to the required combined bound.

Thus the published prescribed-coefficient theorem proves bounded local state complexity but not the needed global parameter correlation.

## 8. Exact fixed-state wall

The analytic wall is now equivalently:

> **Two-parameter Hayes correlation theorem.** For the degree-at-most-four Hayes `L`-polynomial family above, prove
> \[
> \chi(-1)\sum_{u,w}I_p(u,w,1)
> +
> \chi(3)\sum_{u,v}I_p(u,1,v)
> \ll p^{p/2}
> \]
> with an absolute implied constant.

This is the precise fixed-state transfer version of the combined projective character theorem. The two formulations are exactly equivalent.

## 9. Scientific position

### Proved

- every local transfer polynomial has degree at most four;
- its inverse roots have absolute value `sqrt(p)`;
- the degree-`p` irreducible Fourier coefficient is the divided `p`-th power sum of those roots;
- the high-dimensional projective sum equals the displayed two-parameter correlation.

### Open

The factor-`p` cancellation across the parameter planes. This is a Frobenius-power correlation theorem, not a local conductor or state-dimension problem.
