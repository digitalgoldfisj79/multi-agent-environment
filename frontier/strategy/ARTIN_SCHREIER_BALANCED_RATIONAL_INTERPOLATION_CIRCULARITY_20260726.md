# Balanced rational interpolation and the constructive circularity threshold

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** rational Artin--Schreier semiconjugacy route for function-field Fortune `d=1`.  
**Status:** the interpolation and determinantal statements below are **PROVED**. The crown remains **OPEN**.

## 1. Universal balanced representation

Let

\[
E=\mathbf F_p[Z]/(Z^p-Z-1)
\]

and put

\[
m=\frac{p-1}{2}.
\]

Fix any element `beta in E`. Seek polynomials

\[
A(Z),B(Z)\in\mathbf F_p[Z],
\qquad
\deg A,\deg B\le m,
\]

such that

\[
\beta B=A
\quad\text{in }E.
\]

Write

\[
B=b_0+b_1Z+\cdots+b_mZ^m.
\]

The requirement that `beta B` have no coefficients in degrees `m+1,...,p-1` gives exactly

\[
p-1-m=m
\]

homogeneous linear equations in the `m+1` unknowns `b_0,...,b_m`. Hence there is a nonzero solution `B`.

The Artin--Schreier polynomial is irreducible, so `E` is a field. Every nonzero polynomial `B` of degree below `p` represents a nonzero, hence invertible, element of `E`. Setting

\[
A=\beta B
\]

gives the desired representation.

### Theorem 1.1 — universal balanced rational interpolation

Every element of `F_(p^p)` has an Artin--Schreier rational representation

\[
\boxed{
\beta=\frac{A(\alpha)}{B(\alpha)},
\qquad
\deg A,\deg B\le\frac{p-1}{2}.
}
\]

No arithmetic property of `beta` is used.

## 2. The sub-half determinantal varieties

For an integer `r<(p-1)/2`, define the high-coefficient matrix

\[
\mathcal P_r(\beta)
=
\left(
[Z^i](\beta Z^j\bmod (Z^p-Z-1))
\right)_{
 r+1\le i\le p-1,
 0\le j\le r
}.
\]

It has `p-1-r` rows and `r+1` columns.

A rational representation with

\[
\deg A,\deg B\le r
\]

exists exactly when a nonzero coefficient vector for `B` lies in the kernel. Therefore:

### Theorem 2.1 — exact rational-compression criterion

\[
\boxed{
\beta=A/B,\quad \deg A,\deg B\le r
\iff
\operatorname{rank}\mathcal P_r(\beta)<r+1.
}
\]

For `r<(p-1)/2`, this is a genuine determinantal rank-drop condition. At `r=(p-1)/2`, rank drop is automatic by matrix dimensions.

## 3. Consequence for the constructive programme

The earlier fibre-semiconjugacy theorem proves that any rational construction to a genuine cubic map has degree at least

\[
\left\lceil\frac p4\right\rceil.
\]

The present theorem shows that degree

\[
\frac{p-1}{2}
\]

is not a special constructive regime: every field element has such a representation. Searching the full balanced rational class is therefore exactly universal interpolation followed by the original sparse-minimal-polynomial condition.

The only potentially compressive rational corridor is

\[
\boxed{
\left\lceil\frac p4\right\rceil
\le r<
\frac{p-1}{2}.
}
\]

A proof in this corridor must establish a structured rank drop for `mathcal P_r(beta)` together with the cubic Frobenius relation. Once `r=(p-1)/2` is reached, the rank drop is automatic and supplies no information toward the crown.

### Corollary 3.1 — rational circularity threshold

A dense rational-semiconjugacy search at degree at least `(p-1)/2` is not an independent route to `d=1`. It parametrizes arbitrary elements of the degree-`p` field and leaves the entire sparse irreducibility condition unresolved.

This does not rule out a sub-half rational construction. It identifies its exact new theorem:

> exhibit, uniformly in `p`, a solution of the cubic semiconjugacy equations lying on one of the nonautomatic determinantal rank-drop loci `rank P_r<r+1` with `r<(p-1)/2`.

No such structured rank-drop theorem is currently available.

## 4. Verification

`artin_schreier_balanced_rational_interpolation_verify.py` constructs balanced numerator/denominator pairs for deterministic elements at `p=5,7,11,13,17,19,23,29` and checks the quotient identity exactly.

This is a regression of the linear-algebra theorem, not a finite-prime proof of Fortune.

Frozen output:

`artin_schreier_balanced_rational_interpolation_results_20260726.json`.
