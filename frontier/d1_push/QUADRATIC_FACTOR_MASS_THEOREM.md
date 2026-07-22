# Exact quadratic-factor mass and first mixed singular-series moment

**Date:** 2026-07-22  
**Status:** exact theorem for every prime `p>=5` and every `a in F_p^*`. This advances Phase Z, Route 4. It does not prove irreducibility or the d=1 crown.

## 1. Setup

Fix a prime `p>=5`, `a!=0`, and write

`F_(c,d)(X)=X^p+aX^3+cX+d`,

with `(c,d) in F_p^2`.

Let

`Q_2(c,d)=#{monic irreducible quadratics h over F_p : h|F_(c,d)}`

and

`L(c,d)=#{x in F_p : F_(c,d)(x)=0}`.

The purpose is to compute the first two factorial moments of `Q_2` and its first mixed moment with `L`.

## 2. Exact parametrisation of quadratic factors

Write a monic quadratic as

`h_(t,n)(X)=X^2-tX+n`.

It is irreducible exactly when

`chi(t^2-4n)=-1`.

In `F_p[X]/(h_(t,n))`, Frobenius exchanges the two roots, hence

`X^p=t-X`.

Also

`X^3=(t^2-n)X-tn`.

Therefore

`F_(c,d) mod h_(t,n)`

`=[-1+a(t^2-n)+c]X+[t-atn+d]`.

Thus:

### Theorem QFM.1 — quadratic-factor parametrisation

For every irreducible `h_(t,n)`, there is exactly one member of the slice divisible by it, namely

`boxed( c=1-a(t^2-n),  d=t(an-1). )`

Consequently

`boxed( sum_(c,d) Q_2(c,d)=p(p-1)/2. )`

This is the exact quadratic-factor incidence mass.

## 3. Dual cubic formula

Solving the first displayed equation for `n` gives

`n=(c-1+at^2)/a`.

Substitution into the second gives

`a t^3+(c-2)t-d=0`.

The quadratic discriminant becomes

`t^2-4n=-3t^2-4(c-1)/a`.

Hence:

### Corollary QFM.2 — dual cubic statistic

`boxed( Q_2(c,d)`

`=#{t in F_p : at^3+(c-2)t-d=0,`

`                 chi(-3t^2-4(c-1)/a)=-1}. )`

In particular `0<=Q_2(c,d)<=3`.

Thus quadratic factors are controlled by a second depressed cubic, shifted from the linear-root cubic

`a x^3+(c+1)x+d=0`.

## 4. Exact second factorial moment

Suppose two distinct irreducible quadratics, with trace-norm pairs `(t,n)` and `(u,m)`, map to the same `(c,d)`. Equality of the two `c` values gives

`n-t^2=m-u^2`.

Using equality of the two `d` values and `t!=u` gives

`n=1/a-tu-u^2,`

`m=1/a-t^2-tu.`

Their discriminants are

`Delta_t=(t+2u)^2-4/a,`

`Delta_u=(u+2t)^2-4/a.`

Put

`r=t+2u,  s=u+2t.`

The linear transformation `(t,u)->(r,s)` has determinant `-3`, so it is a bijection for `p>=5`; moreover `t!=u` if and only if `r!=s`.

Define

`R_a={r in F_p : chi(r^2-4/a)=-1}.`

The standard quadratic character sum

`sum_r chi(r^2-4/a)=-1`

and the `1+chi(a)` zeroes of `r^2-4/a` give

`|R_a|=(p-chi(a))/2.`

Ordered pairs of distinct quadratic factors of one slice member are therefore in bijection with ordered pairs of distinct elements of `R_a`. Hence:

### Theorem QFM.3 — second factorial moment

`boxed( sum_(c,d) binom(Q_2(c,d),2)`

`       =binom((p-chi(a))/2,2). )`

This exact moment depends only on the square class of `a`.

## 5. Exact mixed linear-quadratic moment

For a quadratic `h_(t,n)` mapped to `(c,d)` by QFM.1, an element `x in F_p` is a root of `F_(c,d)` precisely when

`a n(x+t)+a x^3-a t^2x+2x-t=0.`

If `x+t=0`, this reduces to `-3t=0`; hence the only exceptional pair is `x=t=0`. It contributes `(p-1)/2` values of `n`, those for which `chi(-4n)=-1`.

Assume now `x+t!=0`; then `n` is uniquely determined. Put

`u=2x-t,  v=x+t.`

The map `(x,t)->(u,v)` has determinant `3` and is bijective. Direct substitution gives the quadratic discriminant

`Delta=u(auv+4)/(av)=u^2+4u/(av).`

For each fixed `v!=0`, this is a monic quadratic polynomial in `u` with two distinct roots. Therefore

`sum_u chi(Delta)=-1`,

so exactly `(p-1)/2` values of `u` give a nonsquare discriminant. Summing over the `p-1` nonzero values of `v` and adding the exceptional contribution gives

`(p-1)^2/2+(p-1)/2=p(p-1)/2.`

Thus:

### Theorem QFM.4 — first mixed singular-series moment

`boxed( sum_(c,d) L(c,d) Q_2(c,d)=p(p-1)/2. )`

Equivalently,

`boxed( sum_(c,d) (L(c,d)-1)Q_2(c,d)=0. )`

Quadratic-factor incidence is exactly uncorrelated with the centred linear-root count at the first mixed-moment level.

## 6. Multiplicity distribution and the remaining third moment

Put

`T_3(a,p)=sum_(c,d) binom(Q_2(c,d),3).`

Since `Q_2<=3`, the full distribution is determined by QFM.1, QFM.3 and `T_3`:

`#{Q_2=3}=T_3,`

`#{Q_2=2}=binom((p-chi(a))/2,2)-3T_3,`

`#{Q_2=1}=p(p-1)/2-2binom((p-chi(a))/2,2)+3T_3,`

`#{Q_2=0}=p^2-p(p-1)/2+binom((p-chi(a))/2,2)-T_3.`

For three distinct traces `t,u,v`, collision forces `t+u+v=0`; the three irreducibility conditions become

`chi((t-u)^2-4/a)=-1,`

`chi((u-v)^2-4/a)=-1,`

`chi((v-t)^2-4/a)=-1.`

Thus `T_3` is an explicit two-dimensional additive correlation of the set `R_a`. Its uniform evaluation is the next quadratic-factor mass problem.

## 7. Consequence and limit

The first quadratic-factor local mass and its interaction with linear factors are now exact, not heuristic:

- linear-factor incidence: exact from the existing cubic-tail theorem;
- quadratic-factor incidence: `p(p-1)/2`;
- quadratic pair incidence: `binom((p-chi(a))/2,2)`;
- mixed linear-quadratic incidence: `p(p-1)/2`.

This supplies the first two levels of a rigorous factor-degree singular series. It does not control factors of degree `>=3`, and therefore does not yet imply `N_a(p)>0`.

## 8. Audit

`quadratic_factor_mass_audit.py` independently enumerates every irreducible quadratic, maps it to its unique slice member, recomputes all linear roots, verifies the dual cubic formula pointwise, and checks QFM.1, QFM.3 and QFM.4.

The audit passes for both square classes for every prime

`5<=p<=101`.

No floating-point arithmetic or fitting is used.

## 9. Epistemic classification

- QFM.1: exact quotient-ring calculation.
- QFM.2: exact elimination.
- QFM.3: exact collision classification and quadratic-character count.
- QFM.4: exact incidence count and quadratic-character summation.
- Finite audit through `p=101`: exact independent computation.
- Uniform evaluation of `T_3`: open.
- Higher factor-degree singular series: open.
- Function-field d=1 crown: open.
