# Signed quadratic incidence in the d=1 cubic slice

**Date:** 2026-07-21  
**Status:** exact decomposition and effective `O(p^(3/2))` bound proved.

## 1. Setup

Let `p >= 5` be prime, let `a` be nonzero in `F_p`, and put

`F_(c,d)(X) = X^p + a X^3 + c X + d`.

For a monic irreducible quadratic

`h_(s,n)(X) = X^2 - s X + n`,

Theorem LI.1 gives the unique compatible member

`c = 1 - a(s^2 - n)`,

`d = s(an - 1)`.

Let `H_(s,n)(X) = aX^3 + (c+1)X + d` be the local cubic. Define

`L_(a,2)^chi = sum chi(Disc F_(c,d))`,

where the sum runs over irreducible quadratics `h_(s,n)` for which `H_(s,n)` is rootless.

For each irreducible quadratic write

`r(h) = number of roots of H_(s,n) in F_p`,

and let `delta(h)` be one when the monic local cubic is `X^3`, and zero otherwise. The exact cubic irreducibility indicator gives

`L_(a,2)^chi = (2 T0 + TDelta - R - Ttriple)/3`,

where

`T0 = sum_h chi(Disc F)`,

`TDelta = sum_h chi(Disc F) chi(Disc H)`,

`R = sum_h chi(Disc F) r(h)`,

`Ttriple = sum_h chi(Disc F) delta(h)`.

All sums in this note are over the compatible member attached to `h`.

## 2. Complete two-variable terms

Put

`eps = chi(a)`,

`gamma = chi(3a)`,

`D = a(s^2 - 4n)`,

`S = a s^2`.

Define

`L(D,S) = D + 3S - 4`,

`Uplus(D,S) = D^3 - 18D^2S - 24D^2 + 81DS^2 - 360DS + 180D + 108S - 400`,

`Uminus(D,S) = D^3 - 18D^2S + 81DS^2 - 216DS - 12D + 216S^2 - 468S - 16`,

`Q(D,S) = D^3 - 18D^2S - 24D^2 + 81DS^2 - 360DS + 192D + 144S - 512`.

A direct substitution into the degree-p discriminant formula gives

`chi(Disc F) = A(D,S)/2`,

where

`A(D,S) = chi(Uplus) + chi(Uminus) + gamma chi(L) [chi(Uplus) - chi(Uminus)]`.

The monic local-cubic discriminant satisfies

`chi(Disc H) = eps chi(Q)`.

The irreducibility condition on `h` is `D != 0` and `chi(D) = -eps`. The number of `s` mapping to a fixed `S` is `1 + eps chi(S)`. Consequently

`T0 = (1/4) sum_(D != 0,S) (1 - eps chi(D))(1 + eps chi(S)) A(D,S)`,

`TDelta = (eps/4) sum_(D != 0,S) (1 - eps chi(D))(1 + eps chi(S)) A(D,S) chi(Q(D,S))`.

These identities are exact, including all zero-character fibres.

## 3. The root-incidence term

For a root `x` of `H_(s,n)`, put

`z = s + x`,

`y = s - 2x`.

The identity

`H_(s,n)(X) = a(X+s)h_(s,n)(X) + (2X-s)`

shows that the fibre `z = 0` forces `s = x = 0`. Its contribution is

`R0 = sum_(n: chi(-4n)=-1) chi(Disc F_(1+an,0))`.

On the fibre `z != 0`, put

`t = a z^2`,

`w = a z y`.

Then

`D = w(w-4)/t`,

`S = (w+2t)^2/(9t)`.

Define

`E(w,t) = t^2 + tw - 3t + w^2 - 3w`,

`A1(w,t) = tw - t - w`,

`A2(w,t) = t^3w - 3t^3 + 2t^2w^2 - 15t^2w + 25t^2 + tw^3 - 9tw^2 + 20tw - w^3 + 4w^2`,

`B(w,t) = 8t^5 + 3t^4w^2 + 4t^4w - 39t^4 + 6t^3w^3 - 30t^3w^2 + 33t^3w - 3t^3 + 3t^2w^4 - 20t^2w^3 + 36t^2w^2 + 9t^2w + 2tw^4 - 6tw^3 + 3w^4 - 12w^3`.

On the supported square class `chi(t) = eps`, the degree-p discriminant character becomes

`chi(Disc F) = (eps/2) [(1 + chi(E))chi(A1 A2) + chi(3)(1 - chi(E))chi(B)]`.

The quadratic `h` is irreducible exactly when `w` is not `0` or `4` and

`chi(w(w-4)) = -1`.

Each supported pair `(w,t)` has two preimages in `z`. Therefore the nonzero-z contribution is exactly

`Rstar = (eps/4) sum_(w != 0,4; t != 0) (1 + eps chi(t))(1 - chi(w(w-4)))`

`        * [(1 + chi(E))chi(A1 A2) + chi(3)(1 - chi(E))chi(B)]`.

Thus

`R = Rstar + R0`.

## 4. Triple-root correction

All triple-root local cubics have the same compatible coefficients

`c = -1`, `d = 0`.

Let

`Ta = 1_(chi(2a)=-1) + 2 * 1_(chi(3a)=1 and chi(-a)=-1)`.

Then

`Ttriple = Ta * chi(Disc F_(-1,0))`.

In particular, `|Ttriple| <= 3`.

## 5. Nonsquare-fibre audit for the complete sums

Expand the projectors and `A(D,S)`. Every raw complete term is the quadratic character of a product containing exactly one of `Uplus` or `Uminus`, and optionally some of `S`, `L`, and `Q`.

The exceptional polynomial in the slicing variable `D` may be taken as the product of

`D`, `3D+8`, `D-4`, `D-10`, `D+2`, `D-8`, `2D+1`, `4D+9`, `2D+7`, `4D+11`, `D+1`,

`D^3 - 12D - 20`,

`D^3 - 8D^2 - 12D - 4`,

`64D^6 - 48D^5 - 1431D^4 - 424D^3 + 13524D^2 + 32220D + 25216`.

Its degree is 23. The discriminants and pairwise resultants used to form it have integer contents divisible only by 2 and 3. Hence for every `p >= 5`, outside at most 23 values of `D`, the factors `S,L,Uplus,Uminus,Q` are squarefree and pairwise coprime as polynomials in `S`.

Every raw polynomial is therefore nonsquare and has degree at most 6 in `S`. The one-variable Weil bound gives, for each raw complete sum,

`|sum_(D != 0,S) chi(product)| <= 5 p^(3/2) + 23p`.

Put

`Bc = 5 p^(3/2) + 23p`.

There are 16 raw sums in each of `T0` and `TDelta`, with the prefactor `1/4`. Thus

`|T0| <= 4Bc`,

`|TDelta| <= 4Bc`.

## 6. Nonsquare-fibre audit for the root term

For the root sum, slice in `t` with `w` fixed. The factors are

`t`, `A1`, `A2`, `B`, and `E`.

An exceptional polynomial in `w` is the product of

`w`, `w-1`, `w-3`, `w+1`, `w-4`, `2w-7`,

`4w^3 - 37w^2 + 122w - 125`,

`w-5`, `2w-1`, `2w^2 - 22w + 63`,

`288w^10 - 8376w^9 + 105068w^8 - 740793w^7 + 3204594w^6 - 8696455w^5 + 14466060w^4 - 13610007w^3 + 5822658w^2 - 378513w - 3564`,

`2w^2 - 10w + 9`, `w-2`, `w^2 - 8w + 18`.

Its degree is 28. Outside its roots, the five factors are squarefree and pairwise coprime in `F_p[t]`. Every expanded root polynomial contains `A1 A2` or `B` exactly once, optionally multiplied by `t` and `E`, so it is nonsquare and has degree at most 8 in `t`.

The puncture `t != 0` costs at most one per `w`. Hence each raw root sum is bounded by

`Br = 7 p^(3/2) + 29p`.

There are 16 raw sums with prefactor `1/4`, and `|R0| <= p`. Therefore

`|R| <= 4Br + p`.

## 7. The signed-incidence theorem

### Theorem SQI.1

Uniformly for every prime `p >= 5` and every nonzero `a` in `F_p`,

`|L_(a,2)^chi| <= 30 p^(3/2) + 131p + 1`.

In particular,

`L_(a,2)^chi = O(p^(3/2))`

with an absolute effective constant.

### Proof

Use the exact identity

`L_(a,2)^chi = (2T0 + TDelta - R - Ttriple)/3`.

The estimates above give

`|L_(a,2)^chi| <= 4Bc + (4/3)Br + p/3 + 1`,

which is at most the displayed bound.

## 8. Interpretation

Together with

`L_(a,2) = p^2/6 + O(p)`,

the theorem shows that positive- and negative-discriminant locally admissible members carry asymptotically equal quadratic-factor incidence:

`L_(a,2,+) = p^2/12 + O(p^(3/2))`,

`L_(a,2,-) = p^2/12 + O(p^(3/2))`.

This completes the first signed level of the parity-breaking sieve. The observed data are substantially smaller, of order `p`; proving the sharper `O(p)` estimate is now a finite irregularity and singularity audit of the fixed double-cover surfaces occurring in Sections 5 and 6.