# Quadratic third factorial moment as an explicit Kummer trace

**Date:** 2026-07-22  
**Status:** exact general-prime theorem for the remaining third factorial moment of the irreducible-quadratic factor count. It completes the multiplicity distribution of `Q_2(c,d)` in terms of one fixed genus-two Frobenius trace and one fixed elliptic trace. It does not prove the `d=1` crown.

## 1. Setup

Fix a prime `p>=5`, `a in F_p^*`, and

`F_(c,d)(X)=X^p+aX^3+cX+d`.

Let

`Q_2(c,d)=#{monic irreducible quadratic factors of F_(c,d)}`

and

`T_3(a,p)=sum_(c,d) binom(Q_2(c,d),3).`

Write

`epsilon=chi(a)`, `eta=chi(-1)`, `nu=chi(3)`, `kappa=chi(-3)=eta nu`.

Put

`delta=4/a`.

The square class of `delta` is `epsilon`.

## 2. Collision triples are zero-sum triples

The quadratic pair calculation in `QUADRATIC_FACTOR_MASS_THEOREM.md` shows that three distinct quadratic factors with traces `t,u,v` divide one slice member only if

`t+u+v=0`,

and their three discriminants are nonsquare exactly when

`chi((t-u)^2-delta)=-1`,

`chi((u-v)^2-delta)=-1`,

`chi((v-t)^2-delta)=-1`.

Put

`x=t-u`, `y=u-v`, `z=v-t`.

Then `x+y+z=0`, and because `3` is invertible the map from ordered trace triples to ordered difference triples is bijective. Therefore, with

`A_delta={r in F_p^* : chi(r^2-delta)=-1}`,

one has the exact additive formula

`boxed( 6 T_3(a,p)=#{(x,y,z) in A_delta^3:x+y+z=0}. )`

Thus the open quadratic third moment is an additive triple correlation.

## 3. Binary correlation formula

Define

`g_delta(r)=chi(r^2-delta)+1_(r^2=delta).`

Then `g_delta(r)` is always `+1` or `-1`, and

`B_delta={r:chi(r^2-delta)=-1}`

has indicator `(1-g_delta)/2` and size `(p-epsilon)/2`.

The point `0` belongs to `B_delta` exactly when

`lambda_epsilon=(1-eta epsilon)/2`

equals `1`. Removing that point from all three coordinates gives

`boxed( 6T_3`

` = [p^2-3p epsilon+3-G_epsilon]/8`

`   -lambda_epsilon(3(p-epsilon)/2-2), )`

where

`G_epsilon=sum_(x,y)g_delta(x)g_delta(y)g_delta(x+y)`.

The formula follows by expanding the three binary indicators. The three one-variable sums are `epsilon`, the three pair sums are `1`, and inclusion-exclusion removes the triples containing zero.

## 4. The six-line double plane

First remove the zero-discriminant correction and put

`K_epsilon(p)=sum_(x,y)`

` chi((x^2-delta)(y^2-delta)((x+y)^2-delta)).`

This is the affine character sum of the double plane

`W^2=(X^2-delta Z^2)(Y^2-delta Z^2)((X+Y)^2-delta Z^2).`

Over the algebraic closure its branch lines have dual points

`[1,0,+sqrt(delta)]`, `[1,0,-sqrt(delta)]`,

`[0,1,+sqrt(delta)]`, `[0,1,-sqrt(delta)]`,

`[1,1,+sqrt(delta)]`, `[1,1,-sqrt(delta)]`.

They lie on the smooth dual conic

`n^2=delta(l^2+m^2-lm).`

Consequently the resolved double plane is a Kummer surface.

For the square model `delta=1`, parameterise the dual conic by

`[l:m:n]=[t^2-1:t(t+2):t^2+t+1].`

The six tangent parameters are

`{-2,0,-1,1,infinity,-1/2}`.

The associated genus-two curve is

`boxed( C: y^2=t(t-1)(t+1)(t+2)(2t+1). )`

This is the Shioda-sextic/Kummer construction for `Kum(Jac(C))`.

The standard tangent coefficient vector is `[t^2,-t,1]`. The matrix

`[[1,0,-1],[1,-2,0],[1,-1,1]]`

maps it to the displayed dual-conic parametrisation and has determinant `-3`. Tracking the six individual line normalisations gives product scalar `-4/27=(-3)(2/9)^2`. Therefore the actual square-class double plane is the `-3` quadratic twist of the standard Shioda sextic.

This is the origin of `kappa=chi(-3)` in the trace formulas below.

## 5. Genus-two trace

Let

`V=H^1(C_bar,Q_l)`

and define

`A_p=Tr(Frob_p | wedge^2 V).`

Equivalently, if

`S_1=sum_(t in F_p)chi(t(t-1)(t+1)(t+2)(2t+1))`

and

`S_2=sum_(t in F_(p^2))chi_(p^2)(t(t-1)(t+1)(t+2)(2t+1)),`

then

`boxed( A_p=(S_1^2+S_2)/2. )`

Indeed `Tr(Frob|V)=-S_1` and `Tr(Frob^2|V)=-S_2`.

### Theorem QTK.1 — raw six-line sums

For the square class,

`boxed( K_+(p)=2-p+kappa A_p. )`

For the nonsquare class,

`boxed( K_-(p)=2+p+2p kappa-kappa A_p. )`

### Proof

For the square model, the singular projective double plane has affine count `p^2+K_+`, has `2p-1` points on the line at infinity, and has fifteen rational `A_1` nodes. Resolution therefore gives

`#X_+(F_p)=p^2+K_++17p-1.`

On the Kummer side, the sixteen exceptional classes are rational, while the six-dimensional `wedge^2 V` part is multiplied by the `-3` twisting character. Thus

`#X_+(F_p)=1+p^2+16p+kappa A_p.`

Equating the counts gives the first formula.

For nonsquare `delta`, scaling by `sqrt(delta)` over `F_(p^2)` gives descent by the involution which swaps all three pairs of branch lines. On the genus-two parameter it is

`j(t)=-(t+2)/(2t+1)`

and

`f(j(t))=-27 f(t)/(2t+1)^6`

for `f(t)=t(t-1)(t+1)(t+2)(2t+1)`.

The lift is defined over `F_p` when `kappa=1`; its two elliptic eigenspaces then give twisted wedge trace `4p-A_p`. When `kappa=-1`, Frobenius exchanges the two eigenspaces and the twisted wedge trace is `-A_p`. The branch-point permutation is three transpositions, fixing four two-torsion classes. Hence the resolved nonsquare Kummer form has four fixed exceptional classes.

The singular double plane now has only the three rational nodes at infinity, so

`#X_-(F_p)=p^2+K_-+5p-1.`

Equating this with the descended Kummer count gives

`K_-=2-p+kappa(4p-A_p)` when `kappa=1`,

and

`K_-=2-p+kappa(-A_p)` when `kappa=-1`.

These two cases combine to the displayed formula.

## 6. Root correction in the square class

When `epsilon=-1`, the polynomial `r^2-delta` has no zero, so

`G_-=K_-`.

When `epsilon=1`, scale to `delta=1` and define the elliptic curve

`boxed( E: z^2=(u^2-1)((u+1)^2-1). )`

Let

`e_p=Tr(Frob_p|H^1(E_bar,Q_l)).`

The shifted autocorrelation is

`sum_u chi((u^2-1)((u+1)^2-1))=-1-e_p.`

Expanding the three root indicators gives

`boxed( G_+=K_+-6(1+e_p)+6(nu+eta). )`

The final finite correction comes from the ordered pairs of roots `+/-1`: their third coordinate contributes `2chi(3)+2chi(-1)`.

## 7. Closed third-moment formulas

Combining the binary correlation, Kummer trace and elliptic correction gives:

### Theorem QTK.2 — exact quadratic third factorial moment

For square `a`,

`boxed( T_3(a,p)`

` =[p^2-2p+7-kappa A_p+6e_p-6nu-6eta]/48`

`  -(1-eta)(3p-7)/24. )`

For nonsquare `a`,

`boxed( T_3(a,p)`

` =[(p+1)^2-2p kappa+kappa A_p]/48`

`  -(1+eta)(3p-1)/24. )`

Every quantity on the right is attached to one fixed genus-two curve, one fixed elliptic curve, and elementary quadratic characters. The formulas are integer-valued.

## 8. Complete quadratic-factor multiplicity distribution

Put

`m=(p-chi(a))/2`

and let `T_3` be given by QTK.2. Then the distribution from QFM.3 becomes exact:

`#{Q_2=3}=T_3,`

`#{Q_2=2}=binom(m,2)-3T_3,`

`#{Q_2=1}=p(p-1)/2-2binom(m,2)+3T_3,`

`#{Q_2=0}=p^2-p(p-1)/2+binom(m,2)-T_3.`

Thus the quadratic factor locus is now completely determined by fixed-rank Frobenius data.

## 9. Uniform estimate

Weil gives

`|A_p|<=6p`, `|e_p|<=2sqrt(p)`.

Consequently

`T_3(a,p)=p^2/48+O(p)`

uniformly in both square classes, with an absolute effective constant. For example the displayed formulas imply the crude bounds

`|T_3(+)-p^2/48|<=5p/12+sqrt(p)/4+19/48,`

`|T_3(-)-p^2/48|<=11p/24+1/48.`

The third factorial moment is therefore a fixed-dimensional Kummer error term, not a growing-dimensional character-sum wall.

## 10. Audit

`quadratic_third_moment_kummer_audit.py` independently computes:

1. the direct zero-sum triple count;
2. the raw two-dimensional six-line character sum;
3. `S_1` and `S_2` for the genus-two curve;
4. `A_p` and the elliptic trace `e_p`;
5. both formulas in QTK.1 and QTK.2.

All 48 prime/square-class cases for `5<=p<=101` pass exactly. The resulting third moments agree with the independent irreducible-quadratic enumeration already committed in `quadratic_factor_mass_audit_results.csv`.

No floating-point arithmetic or fitting is used.

## 11. Consequence for Route 4

The quadratic third moment is no longer open. The next singular-series gates are now:

1. `sum binom(Q_3,2)`;
2. `sum LQ_3`;
3. `sum Q_2Q_3`;
4. an all-degree cycle-index or sieve assembly with controlled remainder.

## 12. Epistemic classification

- Additive zero-sum reduction: exact elementary bijection.
- Six-line tangency and Kummer identification: exact Shioda-sextic construction.
- Square/nonsquare descent and trace formulas: exact.
- QTK.2 and complete `Q_2` distribution: exact general-prime theorem.
- Audit through `p=101`: exact finite arithmetic.
- Cubic higher and mixed moments: open.
- Singular-series positivity and the general `d=1` crown: open.
