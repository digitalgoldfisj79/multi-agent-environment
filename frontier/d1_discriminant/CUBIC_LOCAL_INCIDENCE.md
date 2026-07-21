# Locally admissible cubic-factor incidence

**Date:** 2026-07-21  
**Status:** exact decomposition and uniform `O(p^(3/2))` theorems proved, using standard fixed-degree Weil and Lang-Weil estimates plus the exact genericity certificate in `oriented_cubic_symbolic_audit.py`.

## 1. Setup

Let `p >= 5` be prime and `a != 0` in `F_p`. Put

`F_(c,d)(X) = X^p + aX^3 + cX + d`.

Let `L_(a,3)` be the total incidence of monic irreducible cubic factors among locally admissible members of this slice. Thus a family member with two distinct irreducible cubic factors contributes two.

Let

`L_(a,3)^chi`

be the same incidence weighted by `chi(Disc F_(c,d))`.

Use the oriented trace-zero plane of `ORIENTED_CUBIC_PARAMETERIZATION.md`. For every nonzero plane point `xi=(x,y)`, let

`u(xi), v(xi), V(xi)`

be the oriented depressed-cubic invariants and let

`c(xi), d(xi)`

be the unique compatible coefficients. Every oriented irreducible cubic is represented by exactly three plane points.

## 2. Local cubic data

Define the monic local cubic

`K_xi(X) = X^3 + U_xi X + W_xi`,

where

`U_xi = (c(xi)+1)/a`,

`W_xi = d(xi)/a`.

Put

`Delta_xi = -4 U_xi^3 - 27 W_xi^2`,

`r_xi = number of roots of K_xi in F_p`,

`delta_xi = 1_((U_xi,W_xi)=(0,0))`,

`eta_xi = chi(Disc F_(c(xi),d(xi)))`.

The exact cubic irreducibility indicator is

`1_(K_xi irreducible) = (2 + chi(Delta_xi) - r_xi - delta_xi)/3`.

Since every cubic factor is represented three times, define

`S_H = sum_(xi != 0) chi(Delta_xi)`,

`R_H = sum_(xi != 0) r_xi`,

`T_H = sum_(xi != 0) delta_xi`,

and

`S_F = sum_(xi != 0) eta_xi`,

`S_FH = sum_(xi != 0) eta_xi chi(Delta_xi)`,

`R_F = sum_(xi != 0) eta_xi r_xi`,

`T_F = sum_(xi != 0) eta_xi delta_xi`.

Then the exact decompositions are

`L_(a,3) = [2(p^2-1) + S_H - R_H - T_H]/9`,

`L_(a,3)^chi = [2S_F + S_FH - R_F - T_F]/9`.

## 3. The root-incidence surface

After shifting the local root by the compatible translation, the root equation is

`G_a(u,v,V,z) = 0`,

where

`G_a = 2aV(z^3+uz+v) - 6uz^2 + (3V+9v)z - 4u^2`.

After substituting the plane forms, this is a fixed degree-six surface in `(x,y,z)`.

For a projective direction `(r:1)`, write `(x,y)=lambda(r,1)`. Then the fibre equation is

`2a lambda W z^3 + 2a lambda^3 WU z + 2a lambda^4 WN - 6Uz^2 + 3lambda(W+3N)z - 4lambda^2 U^2 = 0`,

of bounded bidegree `(4,3)` in `(lambda,z)`.

## 4. Genericity and the choice of base cubic

The base cubic is

`X^3 + X + b`,

with canonical orientation `W0`, where

`W0^2 + 27b^2 + 4 = 0`.

The exact symbolic audit uses the characteristic-zero point

`a=1`, `b=0`, `W0=2i`.

At this point it verifies:

1. the degree-six root surface is geometrically irreducible;
2. the local-discriminant weight is geometrically nonsquare;
3. every raw degree-p discriminant weight appearing after the standard nested-character split is geometrically nonsquare;
4. multiplying those weights by the local discriminant preserves nonsquareness;
5. the equations `U_xi=W_xi=0` have no common curve.

These are Zariski-open conditions on the base conic. Their complement is therefore a finite set of geometric base points, of an absolute effectively bounded size `B`.

For every fixed `u=1`, the number of `b` for which `X^3+X+b` is irreducible is

`(p-chi(-3))/3`.

Thus, for all sufficiently large `p`, one may choose an irreducible base cubic outside the finite bad set. The incidence sums do not depend on the chosen base, so this choice is legitimate. The finitely many remaining primes are absorbed by enlarging the absolute constants.

### Independence of `a`

Over the algebraic closure choose `s` with `a s^2=1` and scale

`u -> s^2u`, `v -> s^3v`, `V -> s^3V`.

Then

`c_a -> c_1`, `d_a -> s d_1`.

The local cubic is carried to the `a=1` local cubic by `X=sZ`; its discriminant changes by the square factor `s^6`. The two split degree-p discriminant functions `P+Q` and `P-Q` are unchanged, while `-c/(3a)` changes by a square. Hence all geometric nonsquareness and irreducibility assertions are uniform in every `a != 0`.

## 5. Fixed-degree estimates

For a good base, slice the nonzero plane by its `p+1` projective directions.

### Plane character sums

Every raw term in `S_H`, `S_F`, and `S_FH` is a quadratic-character sum of a fixed-degree rational function in the scale variable `lambda`. For all but an absolute number of directions, the function is nonsquare. The one-variable Weil bound gives `O(sqrt(p))` per good direction; exceptional directions contribute `O(p)` in total. Therefore

`S_H = O(p^(3/2))`,

`S_F = O(p^(3/2))`,

`S_FH = O(p^(3/2))`.

### Unsigned root incidence

For all but an absolute number of projective directions, the curve `G_a=0` is geometrically irreducible of bounded genus. The Weil bound gives

`p + O(sqrt(p))`

points on each good fibre. Summing over directions and accounting for `lambda=0`, infinity, and exceptional fibres gives

`R_H = p^2 + O(p^(3/2))`.

### Signed root incidence

The degree-p discriminant weights are nonsquares in the plane function field. The root equation is irreducible of degree three in `z`, so its function field is an odd-degree extension of the plane function field. A nonsquare cannot become a square in an odd-degree extension. Therefore the pulled-back Kummer sheaves remain nontrivial on the root curves. The curve Weil bound gives

`R_F = O(p^(3/2))`.

### Triple-root terms

For a good base, the two triple-root equations have no common component, so Bezout gives

`T_H = O(1)`, `T_F = O(1)`.

All implied constants are absolute and effective.

## 6. Cubic-incidence theorem

### Theorem CLI.1

Uniformly for every prime `p >= 5` and every nonzero `a in F_p`,

`L_(a,3) = p^2/9 + O(p^(3/2))`.

### Theorem CLI.2

Uniformly for every prime `p >= 5` and every nonzero `a in F_p`,

`L_(a,3)^chi = O(p^(3/2))`.

Both constants are absolute and effective.

### Proof

Insert the estimates of Section 5 into the exact decompositions of Section 2. QED.

## 7. Parity sectors

Define

`L_(a,3,+) = (L_(a,3)+L_(a,3)^chi)/2`,

`L_(a,3,-) = (L_(a,3)-L_(a,3)^chi)/2`.

Then

`L_(a,3,+) = p^2/18 + O(p^(3/2))`,

`L_(a,3,-) = p^2/18 + O(p^(3/2))`.

Thus the first two signed single-factor levels of the parity-breaking sieve, degrees two and three, are now both complete.

## 8. Evidence for the sharper bound

A vectorised exact sweep over every prime below `1200`, for both square classes of `a`, found

`max |L_(a,3)-p^2/9|/p < 1.05`,

`max |L_(a,3)^chi|/p < 1.66`.

The data strongly support

`L_(a,3) = p^2/9 + O(p)`,

`L_(a,3)^chi = O(p)`.

The sharpening requires a global irregularity audit of the fixed root surface and its finite Kummer covers. Fibrewise Weil estimates alone necessarily lose `sqrt(p)`.