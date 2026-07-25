# Exact affine cubic-origin decomposition into Tate and Airy terms

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1`, primes `p congruent 5 mod 6`; all Frobenius powers.  
**Status:** **PROVED**, conditional only on the already proved Smith-defect master formula and the all-power Kummer-averaging Airy bridge.

## 1. Smith defect and the cubic-origin fibre

Fix `r>=1`, put

\[
q=p^r,
\qquad
L=\mathbf F_{q^p},
\]

and use the standard additive character `psi_q` of `F_q`. For a polynomial `f` over `F_q`, define the Smith defect

\[
\operatorname{Def}_q(f)
=
\sum_{\alpha\in L}
\psi_q\!\left(\operatorname{Tr}_{L/\mathbf F_q}f(\alpha)\right)-q.
\]

The Smith-defect master formula identifies the affine zero-frequency or cubic-origin hook trace as

\[
h_{p,r}(0)
=
q^{-3}
\sum_{A,B,C\in\mathbf F_q}
\operatorname{Def}_q(AT^3+BT^2+CT).
\]

The subtraction by `q` is exactly the cyclic diagonal contribution.

## 2. Exact elimination of the quadratic coefficient

For `A!=0`, translation in `L` gives

\[
AT^3+BT^2+CT
\sim
AT^3+\left(C-\frac{B^2}{3A}\right)T,
\]

because the omitted constant has extension trace

\[
\operatorname{Tr}_{L/\mathbf F_q}(c)=pc=0.
\]

For fixed `A` and `B`, the map

\[
C\mapsto C-\frac{B^2}{3A}
\]

is a bijection. Hence

\[
\sum_{A\ne0,B,C}\operatorname{Def}_q(AT^3+BT^2+CT)
=
q\sum_{A\ne0,C}\operatorname{Def}_q(AT^3+CT).
\]

## 3. Exact lower-degree strata

If `A=0` and `B!=0`, translation eliminates the linear term:

\[
BT^2+CT\sim BT^2.
\]

The quadratic Gauss sum over `L` is

\[
\sum_{\alpha\in L}
\psi_q\!\left(\operatorname{Tr}(B\alpha^2)\right)
=
\chi_q(B)^pG_L.
\]

Since `p` is odd, `chi_q(B)^p=chi_q(B)`, and therefore

\[
\sum_{B\ne0}
\sum_{\alpha\in L}
\psi_q\!\left(\operatorname{Tr}(B\alpha^2)\right)=0.
\]

Consequently

\[
\sum_{B\ne0}\operatorname{Def}_q(BT^2)
=-q(q-1).
\]

After the free `C`-sum, the complete quadratic stratum contributes

\[
-q^2(q-1).
\]

For the linear stratum,

\[
\operatorname{Def}_q(CT)
=
\begin{cases}
q^p-q,&C=0,\\
-q,&C\ne0.
\end{cases}
\]

Thus

\[
\sum_C\operatorname{Def}_q(CT)=q^p-q^2.
\]

Combining the lower-degree strata gives the exact identity

\[
\boxed{
\sum_{A,B,C}\operatorname{Def}_q(AT^3+BT^2+CT)
=
q\sum_{A\ne0,C}\operatorname{Def}_q(AT^3+CT)
+q^p-q^3.
}
\]

## 4. Reduction to trace-zero cubic sums

For `A!=0`, additive orthogonality in `C` gives

\[
\sum_C\operatorname{Def}_q(AT^3+CT)
=qT_{p,r}^{(A)}-q^2,
\]

where

\[
T_{p,r}^{(A)}
=
\sum_{\substack{\alpha\in L\\
\operatorname{Tr}_{L/\mathbf F_q}(\alpha)=0}}
\psi_q\!\left(
\operatorname{Tr}_{L/\mathbf F_q}(A\alpha^3)
\right).
\]

Therefore

\[
\boxed{
h_{p,r}(0)
=
q^{p-3}-q
+q^{-1}\sum_{A\ne0}T_{p,r}^{(A)}.
}
\]

Let

\[
d_r=\gcd(3,q-1)
\]

and choose representatives `c` of the nonzero cube classes. Each class has `(q-1)/d_r` elements, so

\[
\sum_{A\ne0}T_{p,r}^{(A)}
=
\frac{q-1}{d_r}\sum_cT_{p,r}^{(c)}.
\]

The proved Kummer-averaging bridge states

\[
\operatorname{Tr}(F^r\mid\mathcal D_p)
=
\frac1{d_rq^2}\sum_cT_{p,r}^{(c)},
\]

and

\[
\mathcal R_p^{ss}=\mathcal D_p(-3)^{ss}.
\]

Substitution yields the all-power trace theorem

\[
\boxed{
h_{p,r}(0)
=
q^{p-3}-q
+q(q-1)\operatorname{Tr}(F^r\mid\mathcal D_p).
}
\]

Equivalently,

\[
\boxed{
h_{p,r}(0)
=
q^{p-3}-q
+\frac{q-1}{q^2}
\operatorname{Tr}(F^r\mid\mathcal R_p).
}
\]

## 5. Semisimplified virtual Weil identity

Because the formula holds for every Frobenius power,

\[
\boxed{
\mathcal H_{p,0}^{ss}
=
\mathbf Q_\ell(-(p-3))
-
\mathbf Q_\ell(-1)
+
\mathcal D_p(-2)
-
\mathcal D_p(-1).
}
\]

Using `R_p=D_p(-3)`, this is

\[
\boxed{
\mathcal H_{p,0}^{ss}
=
\mathbf Q_\ell(-(p-3))
-
\mathbf Q_\ell(-1)
+
\mathcal R_p(1)
-
\mathcal R_p(2).
}
\]

Here `H_(p,0)` denotes the virtual affine cubic-origin Smith-defect object whose `r`-th trace is `h_(p,r)(0)`.

## 6. Interpretation

### Proved

1. The entire affine cubic-origin fibre has an exact algebraic/transcendental decomposition.
2. Its algebraic part consists of precisely two Tate terms.
3. Its transcendental part is not an unknown new family: it is the Airy virtual module in two adjacent Tate twists.
4. The quadratic phase stratum cancels exactly after summing over the nonzero quadratic coefficient.
5. The linear and zero phases account exactly for the remaining Tate correction.

### Not proved

This does not yet identify which Airy twist survives the projective sparse-section quotient, the `(q,t)`-surface assembly, or the invariant/quadratic arithmetic projectors. It therefore does not prove the crown or the terminal Airy estimate.

The existing theorem that the canonical projective zero-frequency term has only the full codimension twist is not contradicted. The present object is the affine Smith-defect origin before projectivisation and boundary subtraction.

## 7. New sharply stated continuation lemma

The global Fourier--Cayley programme is reduced to the following exact comparison problem:

> **Projective Airy extraction lemma.** Track the two affine constituents `R_p(1)` and `-R_p(2)`, together with the two Tate terms, through root scaling, projectivisation, boundary subtraction and the invariant/quadratic q-line projectors. Prove that the non-load-bearing Airy twist and Tate terms are absorbed by explicit boundary or collision complexes, leaving the required normalized Airy constituent in the q-line transcendental summand.

This is strictly narrower than constructing an unspecified parity-reversing configuration complex: the only transcendental constituents at the cubic origin are now known exactly.
