# Three-block Fourier normal form for the null-quadric cubic

**Date:** 24 July 2026  
**Status:** exact identities proved and independently verified; bounded linear-mode compression ruled out.  
**Scope:** the trace-zero cubic model in the function-field `d=1` programme.

## 1. Coefficient model

Put `n=p-1` and write

\[
A(X)=\sum_{j=1}^{n-1}a_jX^j.
\]

The exact Artin--Schreier coefficient formulas are

\[
Q(a)=-\sum_{i+j=n}a_ia_j
\]

and

\[
C(a)=
-\sum_{i+j+k=n}a_ia_ja_k
-\sum_{i+j+k=2n}a_ia_ja_k
-\sum_{i+j+k=2n+1}a_ia_ja_k.
\]

All indices lie in `{1,...,n-1}`.

A first proposed diagonal formula for `C` using only the `n`-th roots of unity is false: ordinary cyclic Fourier projection cannot distinguish total degree `n+1` from `2n+1`. The corrected formula requires three blocks.

## 2. Quadratic Fourier identity

Let `E` be any extension of `F_p` containing the group `mu_n` of `n`-th roots of unity. Since `n=-1` in `F_p`, it remains invertible. Orthogonality gives

\[
\frac1n\sum_{s\in\mu_n}A(s)^2
=\sum_{i+j\equiv0\;(n)}a_ia_j.
\]

Here `2\le i+j\le2n-2`, so the only multiple of `n` is `n`. Therefore

\[
\boxed{
Q(a)=-\frac1n\sum_{s\in\mu_n}A(s)^2.
}
\]

## 3. Corrected three-block cubic identity

Choose `zeta` of order `3n` and put `rho=zeta^n`, a primitive cube root of unity. Define

\[
K_0=\frac1n\sum_{s\in\mu_n}A(s)^3.
\]

This selects precisely the total-index layers `n` and `2n`.

For `r=0,1,2`, define

\[
K_{r,1}=\frac1n\sum_{s\in\mu_n}A(\zeta^rs)^3s^{-1},
\qquad
D_r=\zeta^{-r}K_{r,1}.
\]

The `s`-sum selects total index congruent to one modulo `n`. Since the possible layers are `n+1` and `2n+1`, their coefficients in `D_r` are respectively `rho^r` and `rho^{2r}`. Cubic Fourier projection therefore gives

\[
K_{2n+1}=\frac13\sum_{r=0}^{2}\rho^{-2r}D_r
=\sum_{i+j+k=2n+1}a_ia_ja_k.
\]

Consequently

\[
\boxed{
C(a)=
-K_0-rac13\sum_{r=0}^{2}\rho^{-2r}\zeta^{-r}
\left(\frac1n\sum_{s\in\mu_n}A(\zeta^rs)^3s^{-1}\right).
}
\]

This is a simultaneous Fourier normal form for the null-quadric pair `(Q,C)`. It uses one quadratic block and three cubic blocks, but still has `n` modes per block; it is not a bounded-dimensional compression.

The identities were verified for 100 random vectors at each of `p=5,7,11,13` in Hugging Face job `6a63a727db23d7a7ec1cae00`.

## 4. Essential linear dimension of the cubic on the quadric tangent

Let `e_1` be the point with `a_1=1` and all other coordinates zero. Then `Q(e_1)=C(e_1)=0`.

The gradient of `Q` at `e_1` is supported on `a_{n-1}`, so the tangent space to `Q=0` at `e_1` is obtained by deleting that coordinate. On the remaining coordinates

\[
a_1,\ldots,a_{n-2},
\]

the Hessian of `C` at `e_1` is

\[
\frac{\partial^2C}{\partial a_u\partial a_v}(e_1)
=
\begin{cases}
-6,&u+v=n-1,\\
0,&\text{otherwise}.
\end{cases}
\]

For `p\ge5`, `6` is nonzero and this is an invertible anti-diagonal matrix of size `n-2=p-3`. Hence

\[
\boxed{
\operatorname{rank}\operatorname{Hess}(C|_{T_{e_1}Q})=p-3.
}
\]

This was checked exactly at `p=5,7,11,13,17` in job `6a63a7f97ef3c08464967af8`.

### Consequence

If the restricted cubic were a polynomial in `d` linear forms after any linear change of coordinates, every Hessian would have rank at most `d`. Therefore

\[
\boxed{d\ge p-3.}
\]

Thus the null-quadric cubic does not factor through a bounded number of linear Fourier modes or a bounded-dimensional linear quotient. This statement does **not** by itself exclude an exotic nonlinear quotient; it closes only the linear-mode compression proposed in this programme.

## 5. Ruling

- **PROVED:** corrected three-block Fourier identity; full tangent Hessian rank.
- **FALSIFIED:** the earlier one-block diagonal-cubic formula.
- **CLOSED:** bounded-dimensional linear/Fourier-mode compression.
- **OPEN:** cancellation exploiting the structured four-block Fourier expression, or a genuinely nonlinear invariant-theoretic quotient.
