# Hayes orientation cover and telescoping correlation

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-boulders-hayes-first-20260725`  
**Scope:** exact geometry of the combined Hayes correlation.  
**Status:** **PROVED**.

## 1. Essential self-duality and orientation character

On

\[
S=\{wv\ne0\}\subset\mathbf A^3_{u,w,v},
\]
put

\[
\mathcal M
=
\mathbf Q_\ell(-1)
\otimes
\mathcal L_\chi\!\left(\frac{v}{3w}\right).
\]

For a closed point with residue field `F_q`, Theorem 2.1 of

`HAYES_QUARTIC_FUNCTIONAL_EQUATION_AND_SQUARE_CLASS_DICHOTOMY_20260725.md`

gives

\[
C_3=q\chi_q(v/(3w))C_1.
\]

Thus the Frobenius eigenvalue multiset is invariant under

\[
\alpha\longmapsto
\frac{q\chi_q(v/(3w))}{\alpha}.
\]

By Chebotarev, on semisimplifications,

\[
\boxed{
\mathscr H^{ss}
\cong
(\mathscr H^\vee\otimes\mathcal M)^{ss}.
}
\]

The determinant identity is

\[
\boxed{
\det\mathscr H
=
\mathbf Q_\ell(-2)
\otimes
\mathcal L_\chi\!\left(-\frac{v}{3w}\right).
}
\]

Since

\[
\mathcal M^2=\mathbf Q_\ell(-2),
\]

the orientation character is

\[
\boxed{
\mathcal O
=
\det\mathscr H\otimes\mathcal M^{-2}
=
\mathcal L_\chi\!\left(-\frac{v}{3w}\right).
}
\]

Equivalently, because the ratio is a square,

\[
\mathcal O
=
\mathcal L_\chi(-3wv).
\]

The generic system is therefore an orthogonal-similitude rank-four system with multiplier `M` and orientation character `O`. The orientation double cover is

\[
\boxed{
y^2=-\frac{v}{3w}.}
\]

A lift from the resulting `GSO_4` system to `GSpin_4` is a separate obstruction problem and is not asserted here.

## 2. The selected arithmetic sector is the split orientation cover

Restrict to `w=1`. For `p congruent 5 mod 6`,

\[
\chi(-3)=\chi(-1)\chi(3)=-1.
\]

Hence

\[
v=-3y^2,
\qquad y\in\mathbf F_p^*,
\]

runs exactly over the nonsquare values of `v`, with multiplicity two. Indeed:

- every `-3y^2` is a nonsquare;
- every nonsquare `v` has exactly two solutions of `y^2=-v/3`.

Therefore

\[
\boxed{
\sum_{y\in\mathbf F_p^*}
I_p(u,1,-3y^2)
=
2
\sum_{\substack{v\in\mathbf F_p^*\\\chi(v)=-1}}
I_p(u,1,v).
}
\]

This is an exact parametrisation of the arithmetic projector by the orientation cover.

## 3. Telescoping of the degree-drop correction

Recall

\[
\mathcal A_p=\sum_{u,w}I_p(u,w,1),
\qquad
\mathcal B_p=\sum_{u,v}I_p(u,1,v).
\]

Put

\[
\varepsilon_p=\chi(-1),
\qquad
\chi(3)=-\varepsilon_p.
\]

The one-family reduction gives

\[
\mathcal A_p-\mathcal B_p
=
\sum_uI_p(u,0,1)
-
\sum_uI_p(u,1,0)
-
2\sum_{u,\chi(v)=-1}I_p(u,1,v).
\]

Use the orientation parametrisation. Since the `y=0` fibre is exactly `v=0`,

\[
\sum_{u,y\in\mathbf F_p}
I_p(u,1,-3y^2)
=
\sum_uI_p(u,1,0)
+
2\sum_{u,\chi(v)=-1}I_p(u,1,v).
\]

The `v=0` term cancels. Therefore

\[
\boxed{
\chi(-1)\mathcal A_p+\chi(3)\mathcal B_p
=
\varepsilon_p
\left(
\sum_{u\in\mathbf F_p}I_p(u,0,1)
-
\sum_{u,y\in\mathbf F_p}I_p(u,1,-3y^2)
\right).
}
\]

This is the exact telescoping correlation identity.

## 4. Cohomological form

Define

\[
\mathscr K_1
=
\mathscr H|_{(u,w,v)=(u,0,1)}
\]

on `A^1_u`, and

\[
\mathscr K_2
=
(-3y^2)^*\mathscr H_B
\]

on `A^2_(u,y)`, i.e. the family

\[
R^1\pi_!
\left(
\mathcal L_\chi(x)
\otimes
\mathcal L_\psi(x^3+ux-3y^2/x)
\right).
\]

Then the analytic wall is the `p`-th Adams trace of the explicit relative pair

\[
\boxed{
(\mathbf A^2_{u,y},\mathscr K_2)
\quad\text{minus}\quad
(\mathbf A^1_u,\mathscr K_1).
}
\]

The generic orientation character of `K_2` is trivial, and its reciprocal multiplier is the constant

\[
\boxed{p\chi(-1)}
\]

on every `F_p`-rational fibre.

## 5. Trace-function check

Using

\[
pI_p(u,w,v)
=-\sum_j\alpha_j(u,w,v)^p,
\]

the displayed identity is equivalent to the original combined Hayes correlation theorem, with no loss or unproved comparison.

It is also the low-dimensional sheaf-theoretic form of the already proved projective Salie collapse: summing over `u` imposes `Tr(x)=0`, and summing over `y` is a quadratic Gauss transform in `Tr(x^{-1})`.

## 6. New first boulder

The correct analytic kill gate is now:

> **Orientation-cover Adams cancellation theorem.** Prove
> \[
> \left|
> \sum_{u,y}I_p(u,1,-3y^2)
> -
> \sum_uI_p(u,0,1)
> \right|
> \ll p^{p/2}
> \]
> with an absolute constant, by constructing a bounded-complexity realization of the relative `p`-th Adams trace or proving an equivalent all-power cancellation theorem.

This replaces the less structured two-plane conductor problem.

## 7. Remaining geometric gates

1. determine the generic geometric monodromy of `K_2`;
2. compute the `GSpin_4` lifting obstruction on the orientation cover;
3. if it lifts, construct the two half-spin rank-two systems;
4. determine whether their Adams correlation has bounded cohomological complexity;
5. otherwise prove a theorem-level obstruction and return to the projective reciprocal-trace formulation.
