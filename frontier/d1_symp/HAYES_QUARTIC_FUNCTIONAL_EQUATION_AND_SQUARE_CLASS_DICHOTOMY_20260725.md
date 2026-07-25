# Hayes quartic functional equation and square-class dichotomy

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-boulders-hayes-first-20260725`  
**Scope:** the universal rank-four Hayes sheaf for `p congruent 5 mod 6`.  
**Status:** **PROVED**.

## 1. Coefficient notation

For `wv ne 0`, write

\[
L(z,\Theta_{u,w,v})
=
1+C_1z+C_2z^2+C_3z^3+C_4z^4.
\]

Put

\[
a=\chi\!\left(\frac{v}{3w}\right),
\qquad
b=\chi(-1).
\]

## 2. Exact top coefficients

### Theorem 2.1

\[
\boxed{C_3=paC_1}
\]

and

\[
\boxed{C_4=p^2ab.}
\]

### Proof

For a monic degree-four polynomial

\[
P=T^4+c_1T^3+c_2T^2+c_3T+c_4,
\qquad c_4\ne0,
\]

the coefficient sum is

\[
C_4
=
\sum
\chi(c_4)
\psi\!\left(
-uc_1-wc_1^3+3wc_1c_2-3wc_3-vc_3/c_4
\right).
\]

The `c_2`-sum forces `c_1=0`. The `c_3`-sum then forces

\[
c_4=-\frac{v}{3w}.
\]

Each forced sum contributes `p`, giving

\[
C_4=p^2\chi\!\left(-\frac{v}{3w}\right)=p^2ab.
\]

For degree three, summing over `c_2` forces

\[
c_1=\frac{v}{3wc_3}.
\]

Put

\[
x=\frac{v}{3wc_3}.
\]

The remaining phase becomes

\[
-wx^3-ux-v/x,
\]

and the multiplicative character becomes

\[
\chi(-c_3)
=
\chi\!\left(-\frac{v}{3w}\right)\chi(x).
\]

Thus

\[
C_3
=p\chi\!\left(-\frac{v}{3w}\right)
\sum_{x\ne0}\chi(x)\psi(-wx^3-ux-v/x).
\]

But

\[
C_1
=
\chi(-1)
\sum_{x\ne0}\chi(x)\psi(-wx^3-ux-v/x).
\]

Division by `chi(-1)` gives `C_3=paC_1`.

## 3. Exact middle-coefficient vanishing in the opposite-sign sector

### Theorem 3.1

If

\[
a=-b,
\]

then

\[
\boxed{C_2=0.}
\]

### Proof

For a monic quadratic polynomial,

\[
C_2
=
\sum_{x\in\mathbf F_p}
\psi(-wx^3-ux)
\sum_{c\ne0}
\chi(c)
\psi(3wxc-vx/c).
\]

The `x=0` term vanishes because `sum chi(c)=0`. For `x ne 0`, the inner sum is the classical Salie sum

\[
S(A,B)=\sum_{c\ne0}\chi(c)\psi(Ac+B/c)
\]

with

\[
A=3wx,
\qquad
B=-vx.
\]

Its exact evaluation is

\[
S(A,B)
=G_p\chi(B)
\sum_{y^2=4AB}\psi(y).
\]

Hence it vanishes whenever `AB` is a nonsquare. Here

\[
\chi(AB)
=
\chi(-3wv)
=ab.
\]

If `a=-b`, then `ab=-1`, so every inner Salie sum vanishes and `C_2=0`.

## 4. The two exact quartic shapes

### Same-sign sector: `a=b`

Put

\[
\mu=pb=pa.
\]

Then

\[
\boxed{
L(z)
=
1+C_1z+C_2z^2+\mu C_1z^3+\mu^2z^4.
}
\]

This is a reciprocal quartic with constant multiplier `mu`. Its four reciprocal roots can be grouped into two `mu`-reciprocal pairs. If the pair traces are `r` and `s`, then

\[
r+s=-C_1,
\qquad
rs=C_2-2\mu,
\]

and

\[
L(z)
=(1-rz+\mu z^2)(1-sz+\mu z^2).
\]

Consequently the `p`-th reciprocal-root power sum is

\[
\boxed{
\sum_{j=1}^4\alpha_j^p
=D_p(r,\mu)+D_p(s,\mu),
}
\]

where `D_p` is the Dickson polynomial.

### Opposite-sign sector: `a=-b`

The exact identities give

\[
\boxed{
L(z)
=(1+pa z^2)(1+C_1z-pa z^2).
}
\]

Thus one quadratic factor is fixed and the other is determined only by `C_1`.

## 5. Which sector survives the d=1 correlation

The exact one-family reduction selects

\[
\chi(v)=-1
\]

on the plane `w=1`. For `p congruent 5 mod 6`,

\[
\chi(3)=-\chi(-1)=-b.
\]

Therefore, on the selected nonsquare sector,

\[
a
=
\chi(v/3)
=
\chi(v)\chi(3)
=(-1)(-b)
=b.
\]

Hence:

\[
\boxed{
\text{Every fibre surviving the combined d=1 correlation lies in the same-sign reciprocal sector.}
}
\]

The sector annihilated by the quadratic projector is precisely the opposite-sign sector in which the fixed quadratic factor splits off.

## 6. Refined analytic wall

The selected family has a constant reciprocal multiplier

\[
\boxed{\mu=p\chi(-1).}
\]

The local degree-`p` coefficient is therefore

\[
I_p(u,1,v)
=-\frac1p
\left(
D_p(r_{u,v},\mu)+D_p(s_{u,v},\mu)
\right)
\]

for nonsquare `v`, where `r_(u,v)` and `s_(u,v)` are the roots of

\[
X^2+C_1(u,v)X+C_2(u,v)-2\mu=0.
\]

The factor-`p` correlation theorem is consequently a correlation of two rank-two Dickson traces on a canonical double cover of the nonsquare parameter surface, rather than an unrestricted rank-four Adams problem.

## 7. Next gate

The next theorem is:

> **Spin/Dickson cover theorem.** Construct the canonical double cover on which the two reciprocal pair traces `r,s` are defined as rank-two Weil local systems, determine its branch and boundary divisors, and decide whether the combined sum of their `p`-th Dickson traces has bounded conductor after the nonsquare projector.

This is strictly sharper than the generic rank-four Adams conductor gate.
