# Two-variable alternating correspondence: exact failure certificate

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling, `p == 2 mod 3`.  
**Status:** the naive add-two-variables correspondence is **CLOSED**.

## 1. Context

After the Chuang specialization, the surviving trace spaces are

\[
U_k=H_c^1(\mathbb A^1_{\overline{\mathbb F}_p},\operatorname{Sym}^k\mathcal A)^{\mu_3},
\]

and for `p=6r+5`,

\[
\dim U_p=\dim U_{p-2}=r=\frac{p-5}{6}.
\]

The most direct geometric proposal was to relate the sign-isotypic motives for

\[
A'_p:\ \sum_{i=1}^{p}f(y_i)=0,
\qquad
A'_{p-2}:\ \sum_{i=1}^{p-2}f(y_i)=0,
\qquad
f(y)=\frac{y^3}{3}-y,
\]

by adding the final two variables and taking the alternating projector in them.

## 2. The super-sign correction

The one-variable Airy object is carried by odd compactly supported cohomological degree. Therefore the geometric transposition of two one-variable factors already contributes the Koszul sign `-1`.

Consequently, imposing the ordinary sign representation of the final `S_2` does **not** produce the ordinary exterior square of the rank-two Airy object. It produces its ordinary symmetric square:

\[
(\mathcal A[1]^{\otimes2})^{\operatorname{sgn}_{S_2}}
\cong
\operatorname{Sym}^2(\mathcal A)[2].
\]

This is the same super-linear-algebra mechanism by which the sign-isotypic `k`-variable construction realizes `Sym^k(A)` rather than `\wedge^k(A)`.

## 3. Clebsch--Gordan decomposition

For any rank-two characteristic-zero object `V` and `m>=2`,

\[
\operatorname{Sym}^{m}V\otimes\operatorname{Sym}^{2}V
\cong
\operatorname{Sym}^{m+2}V
\oplus
\det(V)\otimes\operatorname{Sym}^{m}V
\oplus
\det(V)^2\otimes\operatorname{Sym}^{m-2}V.
\]

Taking `m=p-2` gives

\[
\operatorname{Sym}^{p-2}\mathcal A\otimes\operatorname{Sym}^{2}\mathcal A
\cong
\operatorname{Sym}^{p}\mathcal A
\oplus
\det(\mathcal A)\otimes\operatorname{Sym}^{p-2}\mathcal A
\oplus
\det(\mathcal A)^2\otimes\operatorname{Sym}^{p-4}\mathcal A.
\]

Thus the two desired adjacent terms occur, but they are accompanied by a third growing symmetric-power summand. The construction is not a two-term correspondence with bounded cone.

## 4. The residual survives the `mu_3` projection

Write `p=6r+5`. Then `p-4=6r+1<p`, so no `k=p` boundary correction occurs. Chuang's dimension formulas give

\[
\dim M'_{p-4}=\frac{p-3}{2}=3r+1,
\]

and

\[
\dim B_{p-4}
=\left\lfloor\frac{p-4}{3}\right\rfloor+1
-\mathbf 1_{p-4\equiv1\ (3)}
=2r.
\]

Therefore

\[
\boxed{
\dim H_c^1(\operatorname{Sym}^{p-4}\mathcal A)^{\mu_3}
=r+1=\frac{p+1}{6}.
}
\]

The determinant has trivial `mu_3` character, so the third Clebsch--Gordan summand contributes this entire linearly growing invariant sector.

## 5. Verdict

### PROVED

The natural add-two-variables/sign-projector construction has a residual `mu_3`-invariant cohomology space of rank `(p+1)/6`.

### CLOSED

It cannot yield

\[
\operatorname{Tr}(F_p|U_p)
-p\operatorname{Tr}(F_p|U_{p-2})
\]

as a bounded-rank local kernel or bounded cone.

### Boundary

This does not exclude every conceivable cross-`k` correspondence. It proves that any successful one must use an additional Frobenius-dependent cancellation among the three Clebsch--Gordan summands. That additional cancellation is not supplied by variable addition, the sign projector, or rank-two representation theory alone.
