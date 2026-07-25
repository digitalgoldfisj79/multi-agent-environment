# Canonical quadratic oscillator on the sparse frequency space

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** one exactly evaluable quadratic model compatible with the wild-infinity residue polarization.  
**Status:** the algebraic and Gauss-sum statements are **PROVED**. This model is **NOT** identified with the actual Pascal wild-infinity nearby-cycle phase.

## 0. Scope warning

The actual high coefficient--normal map in the Laurent expansion is the Pascal matrix `D` proved anti-symplectic in

`PASCAL_SPARSE_BLOCK_ANTI_SYMPLECTIC_THEOREM_20260725.md`.

The degree-reversal involution used below is a simpler anti-symplectic polarization on the same residue symplectic space. The resulting quadratic form demonstrates that the required half-twist has an exact oscillator model with trivial arithmetic sign. It does not prove that the wild Smith-defect phase has this Hessian or is right-equivalent to this quadratic form.

## 1. Degree reversal

Let

\[
\mathcal V_p
=
\operatorname{span}
\{e_a=T^a:4\le a\le p-4\}
\]

be the canonical high-degree representative of the sparse frequency quotient. Define

\[
\boxed{
\mathcal R(e_a)=e_{p-a}.
}
\]

It exchanges the lower and upper Lagrangians and satisfies `R^2=1`. For

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

## 2. Symmetric model form

Define

\[
B_p(v,w)=\omega_p(v,\mathcal Rw).
\]

Because `R` is an anti-symplectic involution, `B_p` is symmetric. On the monomial basis,

\[
\boxed{
B_p(e_a,e_b)
=(2a-p)\mathbf1_{a=b}.
}
\]

Every diagonal entry is nonzero modulo `p`. The associated quadratic form is

\[
Q_p(v)=\frac12B_p(v,v).
\]

Writing

\[
v=\sum_{a=4}^{p-4}x_ae_a,
\]

one obtains

\[
\boxed{
Q_p(v)=\sum_{a=4}^{p-4}a x_a^2.
}
\]

Its dimension is

\[
2m=p-7,
\qquad m=\frac{p-7}{2}.
\]

## 3. Determinant square class

Pair `a` with `p-a`. Their product is `-a^2`; hence

\[
\boxed{
\det Q_p\equiv(-1)^m
\quad\text{modulo squares.}
}
\]

## 4. Exact quadratic exponential sum

Let `q=p^r`, and let `psi_q` be the standard nontrivial additive character. With

\[
G_q=\sum_x\psi_q(x^2),
\qquad G_q^2=\chi_q(-1)q,
\]

one has

\[
\sum_{v\in\mathcal V_p(\mathbf F_q)}\psi_q(Q_p(v))
=
\chi_q(\det Q_p)G_q^{2m}
=q^m.
\]

Therefore

\[
\boxed{
\sum_v\psi_q(Q_p(v))
=q^{(p-7)/2},
}
\]

with no quadratic Kummer sign. Removing the origin gives

\[
\boxed{
\sum_{v\ne0}\psi_q(Q_p(v))
=q^{(p-7)/2}-1.
}
\]

The virtual Weil class of this model is

\[
\boxed{
\mathbf Q_\ell(-(p-7)/2)-\mathbf Q_\ell.
}
\]

Tensoring with the Airy block gives the formally required class

\[
\boxed{
\mathcal D_p(-(p-7)/2)-\mathcal D_p.
}
\]

## 5. Scientific use and limitation

### Proved

1. Degree reversal is an explicit anti-symplectic involution of the residue-paired sparse frequency space.
2. It produces a nondegenerate symmetric model form.
3. The model has exact all-power sum `q^((p-7)/2)` and trivial arithmetic sign.
4. The punctured model has precisely the virtual Tate class required for Airy transport.

### Not proved

The actual Pascal anti-symplectic correspondence need not equal or be integrally conjugate to degree reversal. The actual wild-infinity Smith-defect phase has not been shown to have Hessian `B_p`.

The load-bearing theorem is the Pascal oscillator nearby-cycle realization stated in

`MAIN_BRANCH_STATUS_AFTER_PASCAL_OSCILLATOR_REDUCTION_20260725.md`.

## 6. Verification

The determinant and Gauss-sign cancellation are checked by

`frontier/d1_symp/canonical_quadratic_oscillator_verify.py`.
