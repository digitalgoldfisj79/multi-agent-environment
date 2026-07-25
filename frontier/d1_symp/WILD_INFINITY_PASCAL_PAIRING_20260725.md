# Wild-infinity Pascal pairing and the three-level residual tail

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** formal filtered model of the Smith defect at the cyclic diagonal at infinity.  
**Status:** the expansion, determinant and associated-graded tail statements are **PROVED**. Clean integral Fourier elimination through the nonsplit Jordan extensions is **OPEN**.

## 1. Coefficient variables

Write

\[
f_a(T)=\sum_{m=1}^{p-4}a_mT^m,
\]

with

\[
(a_1,a_2,a_3)=(u_1,u_2,u_3),
\qquad
a_m=\lambda_m\quad(4\le m\le p-4).
\]

The multiplier and sparse-frequency variables therefore form one vector of dimension `p-4`.

## 2. Formal expansion at infinity

Choose a formal diagonal parameter `z` and write

\[
z_i=z(1+w_i),
\qquad
x_i=z_i^{-1}=z^{-1}(1+w_i)^{-1}.
\]

For `m<p`,

\[
x_i^m=z^{-m}\sum_{j\ge0}(-1)^j
\binom{m+j-1}{j}w_i^j.
\]

Put `s_j(w)=sum_i w_i^j`. The constant term vanishes after summing over the `p` factors, so

\[
\boxed{
\sum_{i=1}^pf_a(x_i)
=
\sum_{m=1}^{p-4}a_mz^{-m}
\sum_{j\ge1}(-1)^j
\binom{m+j-1}{j}s_j(w).
}
\]

The choice of `z` is not a `C_p`-equivariant splitting of the diagonal normal sequence; no such splitting exists. Changing the choice acts triangularly on the power sums. Consequently the statements below are canonical on the associated graded of the Jordan/divided-power filtration, while the extension data between levels remain part of the open integral problem.

## 3. Unimodular Pascal determinant

For `n>=1`, let

\[
B_n=\left(\binom{m+j-1}{j}\right)_{1\le j,m\le n}.
\]

### Lemma 3.1

\[
\boxed{\det B_n=1.}
\]

For fixed `j`, `P_j(x)=binom(x+j-1,j)` is a degree-`j` polynomial with zero constant term and leading coefficient `1/j!`. The evaluation matrix of `x,x^2,...,x^n` at `1,...,n` has determinant

\[
\left(\prod_{m=1}^nm\right)
\prod_{1\le a<b\le n}(b-a)
=
\prod_{j=1}^nj!.
\]

The triangular change from the monomials to the `P_j` multiplies this by `prod_j(1/j!)`, giving one.

For `n=p-4`, the signed Laurent coefficient matrix

\[
M_{j,m}=(-1)^j\binom{m+j-1}{j}z^{-m}
\]

has

\[
\boxed{
\det M=\pm z^{-\sum_{m=1}^{p-4}m}.
}
\]

Its numerical determinant is `+-1`; no factor of `p` or any denominator occurs.

## 4. Unimodular filtered coefficient--normal pairing

Let `c_j(a,z)` be the coefficient of `s_j(w)`. For `1<=j<=p-4`,

\[
(c_1,\ldots,c_{p-4})^t
=M(a_1,\ldots,a_{p-4})^t.
\]

Thus, in any chosen formal splitting, the coefficient variables and the first `p-4` power-sum levels are related by an invertible integral linear transformation. Because changes of splitting are triangular, this gives a canonical perfect pairing on the associated graded of the Jordan filtration.

This is the local algebraic reason that the number of multiplier plus sparse-frequency variables is exactly `p-4`.

## 5. Lucas support and the residual three levels

For `1<=m,j<p`, Lucas' theorem gives

\[
\binom{m+j-1}{j}\equiv0\pmod p
\quad\Longleftrightarrow\quad
m+j>p.
\]

A monomial of degree `m` therefore contributes only to levels `j<=p-m`.

For the sparse coefficients `m>=4`, no term occurs beyond `j=p-4`. The final levels

\[
s_{p-3},\qquad s_{p-2},\qquad s_{p-1}
\]

are fed only by `a_1,a_2,a_3`.

Hence, on the associated graded, the first `p-4` normal levels pair unimodularly with all coefficient variables and only a three-level tail remains. This matches the three nonconstant tail coefficients in

\[
T^p+AT^3+BT^2+CT+D
\]

after the sparse power-sum equations and before the final affine/projective quotient.

## 6. Consequence and limitation

There is no `p`-adic resonance in the associated-graded coefficient-to-normal matrix. An unexplained constituent cannot be blamed on a singular middle-level Jacobian.

A clean integral Fourier theorem should eliminate the paired associated-graded levels and leave:

1. the three deepest Jordan levels;
2. the fixed-diagonal Tate line;
3. the explicit discriminant and quotient boundaries.

However, unimodularity does **not** prove that Fourier transform commutes with the nonsplit Jordan filtration. The missing calculation must control the extension data, pole-order filtration in `z`, Frobenius, and the cyclic trivial-minus-nontrivial character difference. The earlier full-rank global Dwork defect is not contradicted.

## 7. Exact next theorem

Prove clean integral Fourier elimination for this unimodular filtered pairing. It must show that the middle associated-graded pairs contribute only the forced Tate shift, control the extensions between them, and reduce the Smith-defect complex to the three residual tail levels. Then compute that residual complex and compare its cubic specialization with `R_p((p-1)/2)` and the q-line ledger.

## 8. Ruling

### PROVED

- the exact formal Laurent expansion;
- `det B_n=1`;
- a perfect integral pairing on the associated graded of the first `p-4` Jordan levels;
- only three deepest levels remain on that associated graded.

### OPEN

- clean integral elimination through the nonsplit extensions;
- the residual three-level vanishing-cycle complex;
- the crown.

The wild-infinity wall is a three-level integral extension problem after a unimodular associated-graded reduction, not an uncontrolled `p`-dimensional stationary-phase problem.
