# Universal Hayes sheaf and exact one-family reduction

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-boulders-hayes-first-20260725`  
**Scope:** analytic `d=1` wall, primes `p congruent 5 mod 6`, `p>=11`.  
**Status:** **PROVED**, using Grothendieck--Ogg--Shafarevich and the already proved Hayes coefficient identity.

## 1. The universal exponential-sum sheaf

Let

\[
\pi:\mathbf G_{m,x}\times\mathbf A^3_{u,w,v}
\longrightarrow\mathbf A^3_{u,w,v}
\]

be projection and put

\[
\mathcal F
=
\mathcal L_\chi(x)
\otimes
\mathcal L_\psi(wx^3+ux+v/x).
\]

Define

\[
\boxed{
\mathscr H=R^1\pi_!\mathcal F.
}
\]

For a closed point represented by a monic irreducible polynomial `P`, the local Euler factor of `F_(u,w,v)` is

\[
1-\Theta_{u,w,v}(P)z^{\deg P},
\]

where

\[
\Theta_{u,w,v}(P)
=
\chi(n(P))
\psi\bigl(us_1(P)+ws_3(P)+vr_1(P)\bigr).
\]

Thus the Hayes polynomial is the cohomological `L`-polynomial

\[
\boxed{
L(z,\Theta_{u,w,v})
=
\det\bigl(1-zF\mid H_c^1(\mathbf G_m,\mathcal F_{u,w,v})\bigr).
}
\]

Its reciprocal roots are exactly the Frobenius eigenvalues on the fibre of `H`.

## 2. Generic rank four

On the open set

\[
U=\{wv\ne0\},
\]

the rank-one sheaf `F_(u,w,v)` has

\[
\operatorname{Swan}_0=1,
\qquad
\operatorname{Swan}_\infty=3.
\]

It is geometrically nonconstant, so

\[
H_c^0=H_c^2=0.
\]

Grothendieck--Ogg--Shafarevich gives

\[
\chi_c(\mathbf G_m,\mathcal F_{u,w,v})=-1-3=-4,
\]

and hence

\[
\boxed{
\dim H_c^1(\mathbf G_m,\mathcal F_{u,w,v})=4.
}
\]

Therefore `H` has generic rank four. The degree-at-most-four Hayes theorem is the same rank statement in Euler-product language.

The stationary equation is

\[
3wx^4+ux^2-v=0.
\]

Thus a safe lisse locus is

\[
\boxed{
U^{\mathrm{sm}}
=
\{wv(u^2+12wv)\ne0\}.
}
\]

The parabola `u^2+12wv=0` is the critical-collision divisor. The coordinate planes `w=0` and `v=0` are the degree-drop divisors.

## 3. Exact degree drops

For the two application planes:

### `v=1`

Put

\[
\mathscr H_A=\mathscr H|_{v=1}.
\]

Its ranks are

\[
\operatorname{rank}\mathscr H_A=
\begin{cases}
4,&w\ne0,\\
2,&w=0,\ u\ne0,\\
1,&w=u=0.
\end{cases}
\]

### `w=1`

Put

\[
\mathscr H_B=\mathscr H|_{w=1}.
\]

Its ranks are

\[
\operatorname{rank}\mathscr H_B=
\begin{cases}
4,&v\ne0,\\
3,&v=0.
\end{cases}
\]

These follow directly from the remaining Swan conductors at zero and infinity.

## 4. Scaling equivariance

For `lambda in F_p^*`, substitute `x=lambda y`. Then

\[
wx^3+ux+v/x
=
(w\lambda^3)y^3+(u\lambda)y+(v\lambda^{-1})/y
\]

and

\[
\mathcal L_\chi(\lambda y)
=
\chi(\lambda)\mathcal L_\chi(y).
\]

Therefore

\[
\boxed{
\mathscr H_{u,w,v}
\cong
\mathcal L_{\chi(\lambda)}
\otimes
\mathscr H_{u\lambda,w\lambda^3,v\lambda^{-1}}.
}
\]

At the level of degree-`p` Hayes coefficients this is

\[
I_p(u,w,v)
=
\chi(\lambda)
I_p(u\lambda,w\lambda^3,v\lambda^{-1}).
\]

## 5. Reduction of the two planes to one family

Because `p congruent 2 mod 3`, cubing is an automorphism of `F_p^*`. For `w ne 0`, write

\[
v=w^{1/3},
\qquad
\lambda=v^{-1}.
\]

Then

\[
w\lambda^3=1,
\qquad
\lambda^{-1}=v.
\]

The scaling identity gives

\[
\boxed{
I_p(u,w,1)
=
\chi(v)
I_p(u/v,1,v).
}
\]

Summing over `u` and nonzero `w`, and reindexing `u/v`, yields

\[
\boxed{
\sum_{u,w\ne0}I_p(u,w,1)
=
\sum_{u,v\ne0}\chi(v)I_p(u,1,v).
}
\]

## 6. Exact signed one-family identity

Put

\[
\varepsilon_p=\chi(-1).
\]

For every prime `p congruent 5 mod 6`, quadratic reciprocity gives

\[
\boxed{
\chi(3)=-\chi(-1)=-\varepsilon_p.
}
\]

Hence the combined Hayes correlation is

\[
\begin{aligned}
\chi(-1)\mathcal A_p+\chi(3)\mathcal B_p
&=
\varepsilon_p(\mathcal A_p-\mathcal B_p)\\
&=
\varepsilon_p
\sum_{u,v\ne0}
(\chi(v)-1)I_p(u,1,v)\\
&\quad+
\varepsilon_p
\left(
\sum_u I_p(u,0,1)
-
\sum_u I_p(u,1,0)
\right).
\end{aligned}
\]

Thus

\[
\boxed{
\chi(-1)\mathcal A_p+\chi(3)\mathcal B_p
=
-2\varepsilon_p
\sum_{\substack{u\in\mathbf F_p\\v\in\mathbf F_p^*\\\chi(v)=-1}}
I_p(u,1,v)
+
\varepsilon_p\mathcal E_p,
}
\]

where

\[
\boxed{
\mathcal E_p
=
\sum_u I_p(u,0,1)
-
\sum_u I_p(u,1,0)
}
\]

is an explicit one-dimensional degree-drop correction.

The two-plane problem is therefore exactly one rank-four family on the `w=1` plane, projected to the nonsquare `v`-class, plus a one-dimensional boundary difference.

## 7. Virtual generic-rank cancellation

Let `Psi^p` denote the `p`-th Adams operation in the Grothendieck group. Adams operations preserve virtual rank. Therefore

\[
\operatorname{rank}\Psi^p(\mathscr H_A)
=
\operatorname{rank}\Psi^p(\mathscr H_B)=4
\]

generically.

Since

\[
\chi(-1)+\chi(3)=0,
\]

the original signed two-plane Adams object has

\[
\boxed{
\operatorname{rank}_{\mathrm{virt}}
\left(
\chi(-1)\Psi^p(\mathscr H_A)
+
\chi(3)\Psi^p(\mathscr H_B)
\right)=0.
}
\]

Equivalently, after the one-family reduction, the generic projector is

\[
(\mathcal L_\chi(v)-\mathbf1)
\otimes
\Psi^p(\mathscr H_B),
\]

which also has virtual rank zero.

This proves the first part of the conductor gate: there is no uncancelled generic-rank contribution of order `p^2`.

## 8. Exact next gate

The analytic boulder is reduced to the following ramification theorem:

> **Combined Hayes--Adams conductor theorem.** Prove that the virtual sheaf
> \[
> (\mathcal L_\chi(v)-\mathbf1)
> \otimes\Psi^p(\mathscr H_B)
> \]
> on the complement of `v(u^2+12v)=0`, together with the explicit degree-drop correction `E_p`, has compactly supported Betti sum bounded by an absolute constant.

The generic rank cancellation is proved. The remaining issue is local monodromy of `Psi^p(H_B)` at:

1. the collision parabola `u^2+12v=0`;
2. the degree-drop line `v=0`;
3. the line at infinity in a compactification of the parameter plane;
4. their intersection points.

## 9. Scientific position

### Proved

- the universal cohomological realization of the Hayes `L`-polynomials;
- generic rank four and exact degree drops;
- the critical-collision divisor;
- scaling equivariance;
- reduction from two parameter planes to one nonsquare-projected family;
- virtual generic-rank zero of the signed Adams object.

### Open

- the complete local inertia and Swan ledger of the `p`-th Adams object;
- an absolute bound for its compactly supported Betti sum;
- the resulting factor-`p` correlation theorem.
