# Hayes orientation tensor factorisation and exact circularity

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-boulders-hayes-first-20260725`  
**Scope:** terminal analytic `d=1` wall.  
**Status:** **PROVED**. This closes the two-parameter Hayes correlation as an independent route.

## 1. The rank-two cubic Airy system

Let

\[
\varpi:\mathbf A^1_r\times\mathbf A^1_t
\longrightarrow\mathbf A^1_t
\]

and define

\[
\boxed{
\mathscr E
=R^1\varpi_!
\mathcal L_\psi(4r^3+tr).
}
\]

For a finite extension `k/F_p`, put

\[
J_k(t)
=
\operatorname{Tr}(F_t\mid\mathscr E_t)
=-\sum_{r\in k}\psi_k(4r^3+tr).
\]

The sheaf `E` has rank two and determinant `Q_l(-1)`. Thus its Frobenius polynomial is

\[
1-J_k(t)z+|k|z^2.
\]

## 2. The rank-three Kummer cubic system is its symmetric square

Put

\[
K_k(t)
=
\sum_{x\in k^*}
\chi_k(x)\psi_k(-x^3-tx).
\]

Let

\[
\mathscr A
=R^1\rho_!
\left(
\mathcal L_\chi(x)
\otimes
\mathcal L_\psi(-x^3-tx)
\right),
\]

so

\[
\operatorname{Tr}(F_t\mid\mathscr A_t)=-K_k(t).
\]

A direct square calculation gives

\[
\begin{aligned}
J_k(t)^2
&=
\sum_{r,s\in k}
\psi_k\bigl(4r^3+tr+4s^3+ts\bigr)\\
&=
|k|+
G_k\chi_k(3)
\sum_{x\ne0}\chi_k(x)\psi_k(x^3+tx).
\end{aligned}
\]

After `x -> -x`,

\[
\boxed{
J_k(t)^2-|k|
=-G_p^{[k:F_p]}K_k(t).
}
\]

Here Hasse--Davenport is used in the form

\[
G_p^{[k:F_p]}
=(-1)^{[k:F_p]-1}G_k
\]

and `chi_p(-3)=-1`.

Let `G` be the constant Weil line on `Spec(F_p)` with Frobenius eigenvalue `G_p`. Since

\[
\operatorname{Tr}(F_t\mid\operatorname{Sym}^2\mathscr E_t)
=J_k(t)^2-|k|,
\]

Chebotarev gives

\[
\boxed{
(\operatorname{Sym}^2\mathscr E)^{ss}
\cong
(\mathcal G\otimes\mathscr A)^{ss}.
}
\]

Thus the rank-three orthogonal factor has an explicit rank-two Spin lift: it is the Gauss twist of the symmetric square of `E`.

## 3. Tensor factorisation of the orientation family

Let

\[
\mathscr K_2
=R^1\pi_!
\left(
\mathcal L_\chi(x)
\otimes
\mathcal L_\psi(x^3+ux-3y^2/x)
\right)
\]

on `A^2_(u,y)`. On `y ne 0`, define

\[
t_+=u+6y,
\qquad
t_-=u-6y.
\]

For `k/F_p`, set

\[
S_k(u,y)
=
\sum_{x\ne0}
\chi_k(x)
\psi_k(x^3+ux-3y^2/x).
\]

Then

\[
\operatorname{Tr}(F_{u,y}\mid\mathscr K_2)=-S_k(u,y).
\]

Expand the product of the two rank-two Airy traces:

\[
\begin{aligned}
J_k(t_+)J_k(t_-)
&=
\sum_{r,s\in k}
\psi_k\bigl(
4r^3+t_+r+4s^3+t_-s
\bigr).
\end{aligned}
\]

Use

\[
x=r+s,
\qquad z=r-s.
\]

Since

\[
4(r^3+s^3)=x^3+3xz^2
\]

and

\[
t_+r+t_-s=ux+6yz,
\]

one obtains

\[
J_k(t_+)J_k(t_-)
=
G_k\chi_k(3)S_k(u,y)
\]

for `y ne 0`; the `x=0` term vanishes because the `z`-sum is nontrivial.

Let `C` be the constant Weil line with Frobenius eigenvalue

\[
\boxed{
\frac{\chi_p(-1)}{G_p}.
}
\]

For every extension degree its eigenvalue equals

\[
-\frac1{G_k\chi_k(3)}.
\]

Therefore, on `y ne 0`,

\[
\boxed{
\mathscr K_2^{ss}
\cong
\left(
\mathcal C
\otimes
t_+^*\mathscr E
\otimes
t_-^*\mathscr E
\right)^{ss}.
}
\]

This is the explicit `GSpin_4` factorisation anticipated by the orientation calculation.

## 4. The diagonal fibre

At `y=0`, the `x=0` contribution in the preceding square calculation is `|k|`. Hence

\[
J_k(u)^2
=
|k|+G_k\chi_k(3)S_k(u,0).
\]

Thus

\[
\boxed{
\operatorname{Tr}(F_{u,0}\mid\mathscr K_2)
=
\frac{|k|-J_k(u)^2}{G_k\chi_k(3)}.
}
\]

This is the symmetric-square degree-drop fibre.

## 5. Summing the orientation plane at the p-th Frobenius

Now take

\[
k=\mathbf F_{p^p},
\qquad q=p^p.
\]

For `t in F_p`, write

\[
J_p(t)=\operatorname{Tr}(F_t^p\mid\mathscr E_t).
\]

Since `p` is odd,

\[
G_k=G_p^p.
\]

The linear map

\[
(u,y)\longmapsto(t_+,t_-)
=(u+6y,u-6y)
\]

is a bijection of `F_p^2`; `y ne0` corresponds to `t_+ ne t_-`.

The off-diagonal tensor factorisation and diagonal formula give

\[
\boxed{
\sum_{u,y\in\mathbf F_p}
\operatorname{Tr}(F_{u,y}^p\mid\mathscr K_2)
=
\frac{\chi(-1)}{G_p^p}
\left[
\left(\sum_{t\in\mathbf F_p}J_p(t)\right)^2
-p^{p+1}
\right].
}
\]

The `sum J_p(t)^2` terms cancel exactly between the off-diagonal and diagonal sectors.

## 6. The one-dimensional boundary

Let

\[
\mathscr K_1
=R^1\pi_!
\left(
\mathcal L_\chi(x)
\otimes
\mathcal L_\psi(ux+1/x)
\right).
\]

The exact Salie main-term evaluation already proved in the branch gives

\[
\boxed{
\sum_{u\in\mathbf F_p}
\operatorname{Tr}(F_u^p\mid\mathscr K_1)
=-pG_p^p.
}
\]

Since

\[
G_p^{2p}=\chi(-1)p^p,
\]

this is exactly the scalar term needed to cancel `-p^(p+1)` in the orientation-plane formula.

## 7. Recovery of the original Airy trace

Additive orthogonality gives

\[
\begin{aligned}
\sum_{t\in\mathbf F_p}J_p(t)
&=-p
\sum_{\substack{x\in\mathbf F_{p^p}\\\operatorname{Tr}(x)=0}}
\psi_p\!\left(\operatorname{Tr}(4x^3)\right).
\end{aligned}
\]

Cubing is a bijection on `F_p^*`, so scaling by the unique cube root of `4` preserves the trace-zero hyperplane and yields

\[
\boxed{
\sum_{t\in\mathbf F_p}J_p(t)=-pT_p.
}
\]

Substitution into the preceding formulas gives exactly

\[
T_p^2
=
\frac{p^{(p-1)/2}}{G_p}
\left(
\chi(-1)\mathcal A_p+\chi(3)\mathcal B_p
\right).
\]

## 8. Ruling on the Hayes correlation route

The two-parameter Hayes correlation is not an independent averaging mechanism. After the orientation cover and Spin factorisation, it is exactly

\[
\boxed{
\text{an explicit scalar multiple of }
\left(\sum_tJ_p(t)\right)^2
=p^2T_p^2.
}
\]

Therefore any proof of the two-parameter correlation bound necessarily proves the original one-parameter Airy bound inside the argument. The hoped-for factor-`p` cancellation across the parameter plane is the square of the missing square-root cancellation across the `p` Airy parameters.

This closes the proposed bounded-complexity two-plane Hayes route as circular.

## 9. Correct analytic boulder

The irreducible analytic target is now

\[
\boxed{
\left|
\sum_{t\in\mathbf F_p}
J_p(t)
\right|
\ll p^{(p+1)/2},
}
\]

or equivalently

\[
\boxed{|T_p|\ll p^{(p-1)/2}.}
\]

Since

\[
J_p(t)
=
D_p(j_1(t),p)
\]

for the rank-two cubic Airy Frobenius trace `j_1(t)`, this is a one-parameter `p`-th Adams/Dickson correlation theorem. The next viable route must act directly on this rank-two family; the two-parameter Hayes lift does not lower its difficulty.
