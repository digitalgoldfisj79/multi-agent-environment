# Smith-defect master formula for the hook Fourier transform

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** both admitted function-field `d=1` branches.  
**Status:** the twisted fixed-point and diagonal formulas below are **PROVED**. They identify one master obstruction common to the Fourier application and Airy correlation.

## 1. Cyclic tensor geometry

Let `q=p^r`, let `f in F_q[T]`, and let

\[
\mathcal L_f=\mathcal L_{\psi_q(f)}
\]

be the rank-one Artin--Schreier sheaf on `A^1`. On

\[
X=(\mathbf A^1)^p
\]

put

\[
\mathcal F_f=\mathcal L_f\boxtimes\cdots\boxtimes\mathcal L_f.
\]

Let `C_p=<sigma>` act by cyclic permutation of the factors. The action commutes with Frobenius.

## 2. Twisted fixed points give the extension-field sum

### Theorem 2.1

The alternating cohomological trace of `sigma F_q` is

\[
\boxed{
\operatorname{Tr}_{alt}
\left(\sigma F_q\mid R\Gamma_c(X_{\bar F_q},\mathcal F_f)\right)
=
\sum_{\alpha\in F_{q^p}}
\psi_q\left(Tr_{F_{q^p}/F_q}(f(\alpha))\right).
}
\]

### Proof

A fixed point of `sigma F_q` is a tuple of the form

\[
(\alpha,\alpha^q,\ldots,\alpha^{q^{p-1}})
\]

with `alpha in F_(q^p)`, and every such `alpha` gives one fixed point. The local trace of the external tensor product is

\[
\prod_{j=0}^{p-1}\psi_q(f(\alpha^{q^j}))
=
\psi_q\left(Tr(f(\alpha))\right).
\]

The Grothendieck--Lefschetz formula gives the result. \(\square\)

By Kunneth and the cyclic tensor identity, this is equivalently the cyclic Adams trace

\[
\operatorname{Tr}_{alt}
\left(\sigma F_q\mid
R\Gamma_c(\mathbf A^1,\mathcal L_f)^{\otimes p}
\right).
\]

## 3. The Smith fixed locus is the trivial diagonal

The fixed locus of `sigma` is the diagonal

\[
\Delta\cong\mathbf A^1.
\]

The restriction of the external tensor sheaf is

\[
\Delta^*\mathcal F_f
=
\mathcal L_f^{\otimes p}
=
\mathcal L_{\psi_q(pf)}
\cong\mathbf Q_\ell,
\]

because the base characteristic is `p`. Therefore

\[
\boxed{
\operatorname{Tr}_{alt}
\left(F_q\mid R\Gamma_c(\Delta,\Delta^*\mathcal F_f)\right)
=q.
}
\]

This is independent of `f`.

## 4. Exact Smith-defect trace

Define

\[
\operatorname{Def}_q(f)
=
\sum_{\alpha\in F_{q^p}}
\psi_q(Tr(f(\alpha)))-q.
\]

Then

\[
\boxed{
\operatorname{Def}_q(f)
=
\operatorname{Tr}_{alt}(\sigma F_q|R\Gamma_c(X,\mathcal F_f))
-
\operatorname{Tr}_{alt}(F_q|R\Gamma_c(\Delta,\mathbf Q_\ell)).
}
\]

Thus `Def_q(f)` is exactly the characteristic-zero trace left after subtracting the cyclic Smith fixed-locus contribution.

Modulo `p`, the Tate/Smith localization theorem kills the free cyclic orbits and retains the Frobenius-twisted diagonal. The displayed number is therefore precisely the **integral lift defect** invisible to the modular Smith category.

## 5. The hook Fourier trace is an averaged Smith defect

For

\[
f_{\lambda,u}(T)
=P_\lambda(T)+u_1T+u_2T^2+u_3T^3,
\]

the exact affine Fourier formula from `CYCLIC_INDUCTION_AND_NONZERO_FOURIER_TRACE_20260725.md` becomes

\[
\boxed{
h_q(\lambda)
=q^{-3}\sum_{u_1,u_2,u_3\in F_q}
\operatorname{Def}_q(f_{\lambda,u}).
}
\]

The subtraction `-q` in that formula is therefore not an ad hoc exclusion. It is exactly the Smith diagonal trace.

Consequently:

1. the complete alternating-hook Fourier transform is an average of cyclic Smith defects;
2. the degree-three fibre at `lambda=0` is the Airy boundary of the same defect family;
3. the nonzero-frequency application problem and the characteristic-boundary Airy correlation are two specializations of one integral cyclic-localization problem.

## 6. Interaction with the finite-critical-locus theorem

For nonzero `(lambda,u)`, the phase derivative has no root of degree `p`. Hence the Smith defect on the irreducible root sector has no finite degree-`p` stationary contribution.

The generic defect must be carried by the compactification at infinity and by explicit discriminant or quotient boundaries. At `lambda=0`, the degree drops to three and the corresponding wild-infinity specialization is the cubic Airy object.

Thus the wild-infinity nearby-cycle theorem and the integral Tate-diagonal lift theorem are not separate speculative routes. They are the geometric and integral formulations of the same defect.

## 7. Master theorem sufficient for both branches

A single theorem would advance both branches:

> **Uniform integral Smith-defect theorem.** Construct a Frobenius-compatible integral compactification of the family `(X,F_f)` over the sparse frequency and multiplier space. Identify its Smith fixed-locus object with the trivial diagonal, and prove that the characteristic-zero defect complex is supported at the wild-infinity degree-drop strata with an explicit filtration whose cubic graded piece is `R_p((p-1)/2)` and whose remaining graded pieces are exactly the q-line and finite boundary ledger. Bound the trace of every residual graded piece on the common weight scale by an absolute constant.

The theorem has two outputs:

1. at the cubic origin it gives the absolute Airy correlation;
2. after Fourier integration it transports that trace into the sparse irreducibility certificate.

## 8. What existing theory supplies and what it does not

### Supplied

- ordinary twisted Lefschetz gives the extension-field trace;
- modular Tate diagonal identifies the fixed-locus Frobenius contraction;
- arithmetic Picard--Lefschetz gives the single cubic Tate correction;
- the q-line ledger gives every finite arithmetic boundary;
- zero-frequency localization and the finite-critical theorem exclude the two simpler sources.

### Missing

No existing Smith/Tate theorem controls the characteristic-zero trace of the defect killed by modular localization. No existing tame Fourier-secant theorem computes the wild degree-drop nearby cycles when the degree equals the characteristic.

The natural Dwork lift leaves a linearly growing defect, so the required result must either construct a different integral filtration or prove cancellation within that defect.

## 9. Ruling

### PROVED

- the extension-field generalized Airy sum is a cyclic twisted fixed-point trace;
- the constant `q` is exactly the trivial Smith diagonal trace;
- the hook Fourier trace is an average of integral Smith defects;
- the application and analytic fronts are specializations of the same defect complex.

### OPEN

- the uniform integral Smith-defect theorem;
- its wild-infinity filtration;
- the absolute trace estimate and final crown.

This is now the unique main-branch object. Work that does not alter or control this defect is a diversion.
