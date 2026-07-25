# Canonical quadratic oscillator on the sparse frequency space

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** quadratic local model suggested by the wild-infinity residue pairing.  
**Status:** the algebraic and Gauss-sum statements are **PROVED**. Identification with the actual wild-infinity Hessian is **OPEN**.

## 1. Degree reversal

Let

\[
\mathcal V_p
=
\operatorname{span}
\{e_a=T^a:4\le a\le p-4\}
\]

be the canonical high-degree representative of the sparse frequency quotient. Define the degree-reversal involution

\[
\boxed{
\mathcal R(e_a)=e_{p-a}.
}
\]

It exchanges the lower and upper Lagrangians and satisfies

\[
\mathcal R^2=1.
\]

For the residue symplectic form

\[
\omega_p(e_a,e_b)
=(a-b)\mathbf1_{a+b=p},
\]

one has

\[
\boxed{
\omega_p(\mathcal Rv,\mathcal Rw)
=-\omega_p(v,w).
}
\]

Thus degree reversal is anti-symplectic.

## 2. Symmetric Hessian form

Define

\[
B_p(v,w)
=
\omega_p(v,\mathcal Rw).
\]

Because `R` is an anti-symplectic involution, `B_p` is symmetric. On the monomial basis,

\[
\boxed{
B_p(e_a,e_b)
=(2a-p)\mathbf1_{a=b}.
}
\]

Every diagonal entry is nonzero modulo `p`, so `B_p` is nondegenerate. Over a `p`-adic integral lift, every entry is a unit.

The associated quadratic form is

\[
Q_p(v)=\frac12B_p(v,v).
\]

Writing

\[
v=\sum_{a=4}^{p-4}x_ae_a,
\]

one obtains in characteristic `p`

\[
\boxed{
Q_p(v)
=
\sum_{a=4}^{p-4}a x_a^2.
}
\]

Its dimension is

\[
2m=p-7,
\qquad m=\frac{p-7}{2}.
\]

## 3. Determinant square class

Pair the coefficient `a` with `p-a`. Their product is

\[
a(p-a)=-a^2.
\]

There are `m` such pairs. Therefore

\[
\boxed{
\det Q_p
\equiv(-1)^m
\quad\text{modulo squares.}
}
\]

The factors of `2` relating the quadratic coefficient matrix and the Hessian occur to the even power `2m` and do not alter the square class.

## 4. Exact quadratic exponential sum

Let `q=p^r` and let `psi_q` be the standard nontrivial additive character of `F_q`. Put

\[
G_q=\sum_{x\in\mathbf F_q}\psi_q(x^2).
\]

For `a!=0`,

\[
\sum_x\psi_q(ax^2)=\chi_q(a)G_q.
\]

Hence

\[
\sum_{v\in\mathcal V_p(\mathbf F_q)}
\psi_q(Q_p(v))
=
\chi_q(\det Q_p)G_q^{2m}.
\]

The one-dimensional quadratic Gauss identity is

\[
G_q^2=\chi_q(-1)q.
\]

Using the determinant square class,

\[
\chi_q(\det Q_p)G_q^{2m}
=
\chi_q((-1)^m)\chi_q(-1)^m q^m
=q^m.
\]

Thus, for every Frobenius degree,

\[
\boxed{
\sum_{v\in\mathcal V_p(\mathbf F_q)}
\psi_q(Q_p(v))
=q^{(p-7)/2}.
}
\]

There is no quadratic Kummer sign.

Removing the origin gives

\[
\boxed{
\sum_{v\ne0}\psi_q(Q_p(v))
=q^{(p-7)/2}-1.
}
\]

In virtual Weil notation, the quadratic oscillator contributes exactly

\[
\boxed{
\mathbf Q_\ell(-(p-7)/2)-\mathbf Q_\ell.
}
\]

Tensoring with the Airy block gives

\[
\boxed{
\mathcal D_p(-(p-7)/2)-\mathcal D_p,
}
\]

which is exactly the open-sector Airy class required by the Fourier localization triangle.

## 5. What has and has not been achieved

### Proved

1. Degree reversal is the anti-symplectic involution complementary to the intrinsic pole-order Lagrangian.
2. It produces a canonical nondegenerate symmetric form on the sparse frequency quotient.
3. The resulting quadratic phase has exact all-power sum `q^((p-7)/2)`.
4. Its arithmetic sign is identically trivial.
5. The punctured quadratic oscillator has precisely the virtual Tate class required for Airy transport.

### Open

It has not been proved that the actual integral wild-infinity Smith-defect phase is formally equivalent to `Q_p`. The residue symplectic form determines the candidate Hessian, but the nonlinear extension terms in the divided-power/Jordan filtration still have to be removed or controlled.

## 6. Final local lemma

The Airy transport is reduced to the following sharply stated formal theorem:

> **Wild-infinity quadratic normal-form lemma.** In the Airy-isotypic cyclic trivial-minus-nontrivial Smith-defect complex, after the proved elimination of the cubic multiplier, Tate, discriminant and affine-quotient terms, the formal phase on the sparse frequency normal space has Hessian `B_p` and is integrally right-equivalent to
> \[
> Q_p=\sum_{a=4}^{p-4}a x_a^2.
> \]
> The equivalence must commute with Frobenius and the cyclic projector.

Because `p` is odd and `B_p` is integrally nondegenerate, once the Hessian identification is proved, the ordinary formal Morse elimination of higher terms gives the oscillator class above. The remaining load-bearing issue is therefore the Hessian identification, not the evaluation of the resulting quadratic complex.

## 7. Verification

The determinant, complementary-degree pairing and Gauss-sign cancellation are checked by

`frontier/d1_symp/canonical_quadratic_oscillator_verify.py`.
