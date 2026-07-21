# Exact quadratic local incidence in the d=1 cubic slice

**Date:** 2026-07-21  
**Status:** proved, using the Weil conjectures for the fixed K3 surface described below.

## 1. Setup

Let p >= 5 be prime, let a be nonzero in F_p, and write

`F_(c,d)(X) = X^p + a X^3 + c X + d`.

For a monic irreducible quadratic

`h_(s,n)(X) = X^2 - s X + n`,

Theorem LI.1 gives the unique compatible member of the slice:

`c = 1 - a(s^2 - n)`,

`d = s(an - 1)`.

On F_p the local cubic is

`H_(s,n)(X) = a X^3 + (c + 1)X + d`.

Let `L_(a,2)` denote the number of irreducible quadratics h_(s,n) for which H_(s,n) is rootless. Equivalently, this is the total degree-2 factor incidence over locally admissible members.

## 2. A useful polynomial identity

In F_p[X],

`H_(s,n)(X) = a(X + s)h_(s,n)(X) + (2X - s)`.

This identity controls the root-incidence term exactly.

Let

`N_2 = p(p - 1)/2`,

the number of monic irreducible quadratics over F_p.

For a fixed irreducible h, let r(h) be the number of roots of H_(s,n) in F_p.

### Theorem QL.1

`sum_(h irreducible quadratic) r(h) = N_2`.

### Proof

Count triples `(s,n,x)` for which `h_(s,n)` is irreducible and `H_(s,n)(x) = 0`.

Put

`y = s - 2x`,

`z = s + x`.

The change `(s,x) <-> (y,z)` is invertible because p != 3.

If z != 0, the root equation determines n uniquely. Substitution gives

`s^2 - 4n = y(y - 4/(az))`.

After scaling by the square `(az)^2`, the quadratic discriminant has character

`chi(w(w - 4))`,

where `w = azy` runs through F_p as y runs through F_p. Since

`sum_w chi(w(w - 4)) = -1`

and the polynomial has two zeros, exactly `(p - 1)/2` values give character -1. Hence every nonzero z contributes `(p - 1)/2` triples.

When z = 0, the root equation forces s = x = 0. Then n is free subject to `-4n` being nonsquare, giving another `(p - 1)/2` triples.

The total is

`(p - 1)^2/2 + (p - 1)/2 = p(p - 1)/2 = N_2`.

## 3. Triple-root correction

Write the monic local cubic as

`a^(-1) H_(s,n)(X) = X^3 + uX + v`,

where

`u = n - s^2 + 2/a`,

`v = s(n - 1/a)`.

Let `T_a` be the number of irreducible quadratics for which `u = v = 0`.

### Theorem QL.2

`T_a = 1_(chi(2a) = -1) + 2 * 1_(chi(3a) = 1 and chi(-a) = -1)`.

### Proof

The equations u = v = 0 give either

1. `s = 0`, `n = -2/a`; this quadratic is irreducible exactly when `chi(8/a) = -1`, equivalently `chi(2a) = -1`;

or

2. `s^2 = 3/a`, `n = 1/a`; there are two such s exactly when `chi(3a) = 1`, and the quadratic discriminant is `-1/a`, which is nonsquare exactly when `chi(-a) = -1`.

## 4. The cubic-discriminant fluctuation

Let

`C_a = sum_(h irreducible quadratic) chi(Disc(H_(s,n)))`,

where the discriminant is that of the monic cubic `X^3 + uX + v`.

Put

`eps = chi(a)`,

`iota = chi(-1)`.

Define

`P(D,S) = D^3 - 18 D^2 S - 24 D^2 + 81 D S^2 - 360 D S + 192 D + 144 S - 512`

and

`K_p = sum_(D,S in F_p) chi(D S P(D,S))`.

Terms with D = 0 or S = 0 contribute zero, so this agrees with the corresponding punctured sum.

### Theorem QL.3

`C_a = (1 + eps * (p iota - K_p))/2`.

### Proof

Set

`A = s^2 - 4n`,

`D = aA`,

`S = a s^2`.

A direct substitution gives

`16 a^3 Disc(H_(s,n)) = P(D,S)`.

The irreducibility condition on h is `chi(D) = -eps`. The number of s giving a prescribed S is

`1 + eps chi(S)`.

Therefore

`C_a = eps/2 * sum_(D != 0, S) (1 - eps chi(D))(1 + eps chi(S)) chi(P(D,S))`.

Introduce

`A_0 = sum_(D != 0,S) chi(P)`,

`A_S = sum_(D != 0,S) chi(SP)`,

`A_D = sum_(D != 0,S) chi(DP)`,

`A_DS = sum_(D != 0,S) chi(DSP) = K_p`.

Then

`C_a = eps/2 * (A_0 + eps A_S - eps A_D - A_DS)`.

As a quadratic polynomial in S, P has discriminant

`20736 (D + 1)^3`.

The standard complete quadratic-character sum therefore gives

`A_0 = p iota`,

`A_D = 1`.

It remains to evaluate A_S. Put

`d = D + 1`,

`v = 9(S - 3)`.

Then the exact identity

`P(D,S) = d(d - v)^2 - (9d - v)^2`

holds. For d != 0, use the Mobius variable

`r = (9d - v)/(d - v)`.

For finite r != 1 the transformed summand is the character of

`Q_r(d) = (r - 1)[(r - 9)d + 27(r - 1)](d - r^2)`.

The two linear roots coincide only at r = 3; r = 9 is the linear exceptional fibre. The complete d-sums are therefore elementary quadratic-character sums. After subtracting d = 0 and d = 1, and adding the r = infinity and d = 0 fibres, the ledger is

`A_S = -chi(-3) + [1 + p chi(-3)] - (p - 2)chi(-3) -[-chi(-7) - 1] - chi(-1)[chi(3) + chi(28)]`.

Since `chi(28) = chi(7)`, the final three character terms cancel, leaving

`A_S = 2`.

Substitution gives the displayed formula for C_a.

## 5. K3 interpretation and O(p) bound

Homogenise the affine equation

`Z^2 = D S P(D,S)`

on `P^1_D x P^1_S`. The branch divisor is the reduced divisor of class `(4,4)` consisting of

- `D = 0`,
- `S = 0`,
- `S = infinity`,
- the irreducible bidegree-(3,2) curve `P = 0`.

The curve P = 0 has exactly two cusps, at `(-1,3)` and `(infinity,infinity)`. Its intersections with the three branch lines give only the following rational double points on the double cover:

- A1 at `(0,0)`;
- A1 at `(0,32/9)`;
- D4 at `(0,infinity)`;
- A5 at `(8,0)`;
- A2 over the cusp `(-1,3)`;
- D5 over `(infinity,infinity)`.

These assertions follow from the identities

`Disc_S(P) = 20736(D + 1)^3`,

`P(D,0) = (D - 8)^3`,

and the local cusp expansions at the two singular points.

Thus the minimal resolution is a K3 surface. In particular, its first and third l-adic cohomology vanish and its second Betti number is 22. The Weil conjectures give

`K_p = O(p)`

with an absolute effective constant; passing between the affine character sum and the smooth projective model changes the count by only O(p), because the boundary and exceptional locus have fixed complexity.

Consequently

`C_a = O(p)`

uniformly in nonzero a.

## 6. Exact formula for the locally admissible quadratic incidence

For a cubic `X^3 + uX + v`, the exact irreducibility indicator is

`1_irred = [2 + chi(Disc) - number_of_roots - 1_((u,v)=(0,0))]/3`.

Summing over irreducible quadratics and applying Theorems QL.1-QL.3 gives

`L_(a,2) = [N_2 + C_a - T_a]/3`.

Equivalently,

`L_(a,2) = p(p - 1)/6 + [1 + eps(p iota - K_p) - 2T_a]/6`.

Therefore

`L_(a,2) = p^2/6 + O(p)`

uniformly in a.

This is stronger than the previously targeted `O(p^(3/2))` error.

## 7. What remains

The unsigned quadratic incidence layer is now complete. The next quantity is the discriminant-weighted local incidence

`L_(a,2)^chi = sum_((c,d) locally admissible) chi(Disc(F_(c,d))) nu_2(F_(c,d))`.

Substituting the unique compatible coefficients reduces this to a finite linear combination of fixed-degree Kummer sums on surfaces. The expected bound is O(p), but the branch-divisor audit for those additional covers remains to be completed.