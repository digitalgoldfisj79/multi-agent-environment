# Wild-infinity Pascal pairing and the three-level residual tail

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** formal local model of the Smith defect at the cyclic diagonal at infinity.  
**Status:** the expansion, determinant and tail-support statements are **PROVED**. Clean integral Fourier elimination and the residual vanishing cycles remain **OPEN**.

## 1. Coefficient variables

Write the complete polynomial phase as

\[
f_a(T)=\sum_{m=1}^{p-4}a_mT^m,
\]

where

\[
(a_1,a_2,a_3)=(u_1,u_2,u_3),
\qquad
a_m=\lambda_m\quad(4\le m\le p-4).
\]

Thus the multiplier and sparse-frequency variables form one vector

\[
a=(a_1,\ldots,a_{p-4})
\]

of dimension `p-4`.

## 2. Formal expansion at the diagonal at infinity

Use the coordinate `z=1/t` at infinity and write a point near the cyclic diagonal as

\[
z_i=z(1+w_i),
\qquad
x_i=z_i^{-1}=z^{-1}(1+w_i)^{-1}.
\]

For every `m<p`,

\[
x_i^m
=z^{-m}\sum_{j\ge0}(-1)^j
\binom{m+j-1}{j}w_i^j.
\]

Put

\[
s_j(w)=\sum_{i=1}^p w_i^j.
\]

The constant term vanishes after summing over `i` because `p=0`. Hence the cyclic phase has the exact formal expansion

\[
\boxed{
\sum_{i=1}^pf_a(x_i)
=
\sum_{m=1}^{p-4}a_mz^{-m}
\sum_{j\ge1}(-1)^j
\binom{m+j-1}{j}s_j(w).
}
\]

## 3. The Pascal matrix is unimodular

For `n>=1`, define

\[
B_n=(b_{j,m})_{1\le j,m\le n},
\qquad
b_{j,m}=\binom{m+j-1}{j}.
\]

### Lemma 3.1

\[
\boxed{\det B_n=1.}
\]

### Proof

For fixed `j`, the function

\[
P_j(x)=\binom{x+j-1}{j}
\]

is a polynomial of degree `j`, has zero constant term, and has leading coefficient `1/j!`. The matrix `B_n` evaluates the basis `P_1,...,P_n` at `x=1,...,n`.

Replacing `P_j` by its leading monomial changes the determinant by the product of the leading coefficients. The evaluation matrix of `x,x^2,...,x^n` at `1,...,n` has determinant

\[
\left(\prod_{m=1}^n m\right)
\prod_{1\le a<b\le n}(b-a)
=
\prod_{j=1}^n j!.
\]

Multiplying by `prod_j(1/j!)` gives one. \(\square\)

The row signs `(-1)^j` change only the determinant sign. Therefore, for

\[
n=p-4,
\]

the coefficient matrix

\[
M_{j,m}=(-1)^j\binom{m+j-1}{j}z^{-m},
\qquad
1\le j,m\le p-4,
\]

has determinant

\[
\boxed{
\det M=\pm z^{-\sum_{m=1}^{p-4}m}.
}
\]

It is a unit over the Laurent field `k((z))`. More importantly, its numerical determinant is `+-1`, so no factor of `p` or any other denominator occurs.

## 4. Perfect coefficient--normal pairing

Let `c_j(a,z)` be the coefficient of `s_j(w)` in the phase. For `1<=j<=p-4`,

\[
(c_1,\ldots,c_{p-4})^t=M(a_1,\ldots,a_{p-4})^t.
\]

Hence

\[
\boxed{
(a_1,\ldots,a_{p-4})
\longleftrightarrow
(c_1,\ldots,c_{p-4})
}
\]

is an invertible integral linear change of frequency coordinates after the natural Laurent weighting at infinity.

Thus the multiplier plus sparse-frequency space pairs perfectly with the first `p-4` power-sum levels of the modular Jordan normal representation.

This is the local algebraic reason the number of coefficient variables is exactly `p-4`.

## 5. Only three normal levels remain

For `1<=m<p` and `1<=j<p`, Lucas' theorem gives

\[
\binom{m+j-1}{j}\equiv0\pmod p
\quad\Longleftrightarrow\quad
m+j>p.
\]

Therefore a monomial of degree `m` contributes only to levels

\[
1\le j\le p-m.
\]

Since `m<=p-4`, the sparse coefficients contribute no terms beyond `j=p-4`. The final three levels

\[
s_{p-3},\qquad s_{p-2},\qquad s_{p-1}
\]

are fed only by the cubic multiplier variables `a_1,a_2,a_3`.

After the perfect pairing with levels `1,...,p-4`, the formal normal problem has a residual tail of dimension three. This matches the three nonconstant tail coefficients remaining in

\[
T^p+AT^3+BT^2+CT+D
\]

after the sparse power-sum equations and before the final affine/projective quotient.

## 6. Consequence for Fourier elimination

At the level of the formal phase, there is no `p`-adic resonance in the middle normal directions. The pairing matrix is unimodular. Therefore any unexplained constituent cannot be attributed to a singular coefficient-to-normal Jacobian in those `p-4` directions.

A clean integral Fourier--Deligne or Dwork elimination theorem should remove these paired directions and leave only:

1. the three deepest Jordan levels;
2. the fixed diagonal Tate line;
3. the explicit discriminant and quotient boundaries.

This is a strict reduction of the wild-infinity theorem from a `p-1` dimensional indecomposable normal block to a three-level residual tail, provided clean integral elimination is established.

## 7. What is not yet proved

Unimodularity of the formal coefficient matrix does not by itself prove that integral compactly supported Fourier transform commutes with the Jordan filtration. The missing step must control:

- extension data between the one-dimensional associated-graded levels;
- the pole-order filtration in `z`;
- Frobenius on the resulting Dwork/nearby-cycle complex;
- the cyclic trivial-minus-nontrivial character difference.

The full-rank Dwork defect found earlier is global and is not contradicted by the local unimodular pairing.

## 8. Exact next theorem

Prove a clean integral Fourier-elimination theorem for the unimodular Pascal pairing. It should identify the Fourier transform along the first `p-4` Jordan levels with a Tate shift and reduce the Smith-defect complex to the three residual tail levels. Then compute that residual complex and compare its cubic specialization with `R_p((p-1)/2)` and the q-line ledger.

## 9. Ruling

### PROVED

- the exact Laurent/Hasse expansion at infinity;
- `det B_n=1`;
- perfect integral pairing of all `p-4` coefficient variables with the first `p-4` Jordan levels;
- only three deepest normal levels remain unpaired.

### OPEN

- clean integral Fourier elimination through the nonsemisimple Jordan extensions;
- the residual three-level vanishing-cycle complex;
- the crown.

The wild-infinity wall is now a three-level integral extension problem, not an uncontrolled `p`-dimensional stationary-phase problem.
