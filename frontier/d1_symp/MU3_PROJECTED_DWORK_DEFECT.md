# The Airy boundary defect after the `mu_3` projection

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling, `p == 2 mod 3`.  
**Status:** the projected full-rank statement is **PROVED**.

## 1. Input

For `k=p-2`, Haessig's effective Dwork decomposition gives the primitive target basis

\[
PH^1_{p-2}
=
\bigoplus_{j=0}^{(p-3)/2}
\mathbf C_p\,[a v^{p-2-2j}w^{2j}].
\]

The canonical integral lift of the modular Adams quotient has principal connection defect

\[
aJ_p(q_i)=a r_i,
\qquad
q_i=v^{p-i}w^i,
\qquad
r_i=v^{p-2-i}w^i.
\]

The previous cohomology audit proved that the even source monomials map onto the entire unprojected primitive target.

## 2. `mu_3` characters

Use the symmetry preserving `x^3+ax`:

\[
(a,x)\longmapsto(\zeta a,\zeta^{-1}x),
\qquad \zeta^3=1.
\]

In Haessig's frame,

\[
\operatorname{wt}_{\mu_3}(a)=1,
\qquad
\operatorname{wt}_{\mu_3}(v=x)=-1,
\qquad
\operatorname{wt}_{\mu_3}(w=x^2)=1
\]

modulo `3`.

For a target basis class

\[
c_j=a v^{p-2-2j}w^{2j},
\]

its character exponent is

\[
1-(p-2-2j)+2j
=3-p+4j
\equiv 1+j\pmod3,
\]

because `p == 2 mod 3`.

Hence

\[
\boxed{c_j\text{ is }\mu_3\text{-invariant}\iff j\equiv2\pmod3.}
\]

Write `p=6r+5`. Since

\[
0\le j\le\frac{p-3}{2}=3r+1,
\]

the invariant indices are

\[
j=2,5,8,\ldots,3r-1,
\]

exactly `r=(p-5)/6` values. This recovers the rank of Chuang's surviving target space `U_{p-2}` directly on the Dwork basis.

## 3. The source characters match

For the corresponding source monomial

\[
q_{2j}=v^{p-2j}w^{2j},
\]

the character exponent is

\[
-(p-2j)+2j=-p+4j\equiv1+j\pmod3.
\]

Therefore `q_{2j}` is invariant for exactly the same indices `j == 2 mod 3`, and

\[
aJ_p(q_{2j})=c_j.
\]

Consequently,

\[
\boxed{
\operatorname{rank}
\left(
M_p^{\mu_3}
\xrightarrow{\ aJ_p\ }
PH^1_{p-2}{}^{\mu_3}
\right)
=
\frac{p-5}{6}.
}
\]

The endpoint map in the exact connection defect is supported only on the terminal source monomial and cannot remove these independent classes.

## 4. Verdict

### PROVED

The principal lift defect remains full rank after projection to the exact cohomology sector that contributes to the `p == 2 mod 3` trace.

### CLOSED

The hope that Chuang's `mu_3` reduction might make the canonical near-intertwiner a bounded-rank correction is false. It has maximal rank `(p-5)/6` on the surviving target.

### Remaining requirement

A successful Dwork proof must construct a genuinely Frobenius-dependent cancellation among all these invariant defect classes. Such a cancellation is not a consequence of:

- the mod-`p` Adams exact sequence;
- divisibility of the lift defect by `p`;
- the `mu_3` projector;
- or Haessig's ordinary effective decomposition.

Producing it is a new global theorem, not further reduction of the known near-intertwiner.
