# Hayes two-plane target collapses to one quadratic Kummer projector

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** terminal analytic `d=1` correlation.  
**Status:** **PROVED**.

## 1. Notation

Write

\[
I_A(u,t)=I_p(u,t,1),
\qquad
I_B(u,t)=I_p(u,1,t).
\]

Thus

\[
\mathcal A_p=\sum_{u,t\in\mathbf F_p}I_A(u,t),
\qquad
\mathcal B_p=\sum_{u,t\in\mathbf F_p}I_B(u,t).
\]

For `p congruent 5 mod 6`, cubing is a bijection of `F_p^*`.

## 2. Exact scaling relation on the nonzero torus

Let `t=s^3`, with the unique `s in F_p^*`. The proved scaling law

\[
I_p(u,w,v)
=
\chi(\lambda)
I_p(u\lambda,w\lambda^3,v\lambda^{-1})
\]

with `lambda=s^{-1}` gives

\[
I_A(u,s^3)
=
\chi(s)
I_B(u/s,s).
\]

Since `chi(s^3)=chi(s)`, this is

\[
\boxed{
I_A(u,t)=\chi(t)I_B(u/t^{1/3},t^{1/3})
\qquad(t\ne0).
}
\]

Summing over `u` and reindexing `u/s` yields

\[
\boxed{
\sum_{u,t\ne0}I_A(u,t)
=
\sum_{u,s\ne0}\chi(s)I_B(u,s).
}
\]

## 3. The two-plane combination

For primes `p congruent 5 mod 6`, quadratic reciprocity gives

\[
\boxed{\chi(3)=-\chi(-1).}
\]

Therefore

\[
\chi(-1)\mathcal A_p+\chi(3)\mathcal B_p
=
\chi(-1)(\mathcal A_p-\mathcal B_p).
\]

Separate the zero-parameter fibres:

\[
\mathcal A_{0,p}=\sum_u I_A(u,0),
\qquad
\mathcal B_{0,p}=\sum_u I_B(u,0).
\]

Using the nonzero-torus relation gives the exact identity

\[
\boxed{
\mathcal A_p-\mathcal B_p
=
\mathcal A_{0,p}-\mathcal B_{0,p}
+
\sum_{u\in\mathbf F_p}
\sum_{s\in\mathbf F_p^*}
(\chi(s)-1)I_B(u,s).
}
\]

Equivalently,

\[
\boxed{
\mathcal A_p-\mathcal B_p
=
\mathcal A_{0,p}-\mathcal B_{0,p}
-2
\sum_{u\in\mathbf F_p}
\sum_{s\text{ nonsquare}}
I_B(u,s).
}
\]

Thus the terminal correlation is not a correlation between two unrelated parameter-plane families. It is one rank-four Hayes family on `(u,s)`, projected to the difference between its quadratic Kummer twist and its untwisted part, plus two explicit one-dimensional boundary sums.

## 4. Sheaf form

On

\[
\mathbf A^1_u\times\mathbf G_m{}_s,
\]

let `H_B` be the rank-four sheaf with fibre

\[
H_c^1\left(
\mathbf G_m{}_x,
\mathcal L_\chi(x)
\otimes
\mathcal L_\psi(x^3+ux+s/x)
\right).
\]

The generic contribution to the target is the rational-point trace of

\[
\boxed{
\Psi^p(\mathscr H_B)
\otimes
(\mathcal L_\chi(s)-\mathbf 1).
}
\]

The Adams operation commutes with the quadratic twist because

\[
\mathcal L_\chi^{\otimes p}=\mathcal L_\chi
\]

for odd `p`.

This has virtual generic rank zero. The unequal affine rank drops identified in `UNIVERSAL_HAYES_LAURENT_SHEAF_20260725.md` are exactly the separate boundary term `A_(0,p)-B_(0,p)`.

## 5. Boundary size is already on the permitted scale

The fibre ranks on the zero lines are at most three. The pointwise Hayes Riemann-hypothesis estimate therefore gives

\[
|\mathcal A_{0,p}|+|\mathcal B_{0,p}|
\ll p\,p^{(p-2)/2}
=
 p^{p/2},
\]

with an absolute constant.

Hence the boundary contribution already satisfies the required terminal scale. The only remaining analytic theorem is the generic Kummer-projector estimate

\[
\boxed{
\left|
\sum_{u\in\mathbf F_p}
\sum_{s\in\mathbf F_p^*}
(\chi(s)-1)I_B(u,s)
\right|
\ll p^{p/2}.
}
\]

## 6. Revised first boulder

The exact next theorem is:

> **Kummer-projected Adams theorem.** For the rank-four Laurent family
> \[
> \mathscr H_B(u,s)=
> H_c^1(\mathbf G_m,
> \mathcal L_\chi(x)\mathcal L_\psi(x^3+ux+s/x)),
> \]
> prove an absolute `p^(p/2)` bound for the compactly supported first-trace of
> \[
> \Psi^p(\mathscr H_B)\otimes(\mathcal L_\chi(s)-1)
> \]
> over `A^1 x G_m`.

This is strictly smaller than the original two-plane correlation theorem.

## 7. Ruling

### Proved

- exact cubic-cover equivalence of the two nonzero parameter planes;
- reduction of the signed target to one quadratic Kummer projector;
- separation of the two harmless one-dimensional boundary sums;
- virtual generic-rank cancellation.

### Open

- bounded compactly supported complexity of the Kummer-projected `p`-th Adams class;
- the terminal estimate and the `d=1` crown.