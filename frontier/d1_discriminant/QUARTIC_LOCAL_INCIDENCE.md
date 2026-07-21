# Locally admissible quartic-factor incidence

**Date:** 2026-07-21  
**Status:** unsigned and signed `O(p^(3/2))` theorems proved from fixed geometry; the resulting positive-parity sector with no factors of degrees 2, 3, or 4 has positive density.

## 1. Setup

Let p >= 5, let a be nonzero in F_p, and put

`F_(a,c,d)(X) = X^p + aX^3 + cX + d`.

Let `nu_4(F)` be the number of distinct monic irreducible quartic factors. Define

`L_(a,4) = sum_(locally admissible F) nu_4(F)`

and

`L_(a,4)^chi = sum_(locally admissible F) chi(Disc F) nu_4(F)`.

## 2. Universal ordered-cycle model

Let `x_0,x_1,x_2,x_3` be a Frobenius-ordered quartic orbit. The quartic divides a member of the slice exactly when there are c,d such that

`x_(i+1) + a x_i^3 + c x_i + d = 0`

for i modulo four.

Over the algebraic closure choose s with `a s^2=1` and replace every x_i by `s x_i`. This reduces the geometry to a=1, with d rescaled by a nonzero constant. Hence all geometric assertions below are uniform in a.

For a=1 define the affine variety X_4 in variables

`x_0,x_1,x_2,x_3,c,d`

by the four equations

`x_(i+1) + x_i^3 + c x_i + d = 0`.

Remove the repeated-coordinate locus by saturating with the Vandermonde

`Vand = product_(i<j) (x_i-x_j)`.

### Theorem QLI.1

The saturated characteristic-zero ideal is prime of dimension two.

The exact Sage audit gives

`BASE_DIM 2`, `BASE_PRIME True`, `BASE_ASS 1`.

For every p outside a finite set, the Frobenius-4-cycle twist is therefore geometrically integral. Lang-Weil gives

`# X_4(F_p, twisted) = p^2 + O(p^(3/2))`.

Points from proper subfields lie on the removed Vandermonde boundary and contribute only O(p). Every irreducible quartic factor is represented by its four roots, so the complete compatible-quartic incidence is

`M_(a,4) = p^2/4 + O(p^(3/2))`.

The finitely many bad primes are absorbed by enlarging the absolute effective constant.

## 3. The local-root cover

The monic local cubic is

`K_(c,d)(Z) = Z^3 + ((c+1)/a)Z + d/a`.

After the geometric scaling to a=1, add the equation

`z^3 + (c+1)z + d = 0`

to the ordered-cycle model. The saturated characteristic-zero ideal is again prime of dimension two:

`ROOT_DIM 2`, `ROOT_PRIME True`, `ROOT_ASS 1`.

Consequently the ordered quartic-root incidence with a local root has

`p^2 + O(p^(3/2))`

points. Dividing by four gives

`R_(a,4) = p^2/4 + O(p^(3/2))`,

where `R_(a,4)` is the sum, over compatible irreducible quartics, of the number of F_p-roots of the attached local cubic.

The triple-root locus is obtained by adding `c+1=0` and `d=0`. Its saturated ideal has dimension zero, so its total contribution is O(1).

## 4. Kummer weights

For a=1 put

`Delta = -4(c+1)^3 - 27d^2`,

`Fplus  = 4c^3 + 12c^2 + 9c + 27d^2`,

`Fminus = 4c^3 - 12c^2 + 9c + 27d^2`.

The local-cubic discriminant character is `chi(Delta)`.

For c nonzero, the exact degree-p discriminant formula splits into the raw square classes

`Fplus`, `Fminus`, `c Fplus`, `c Fminus`.

Multiplication by the local discriminant adds the four classes

`Delta Fplus`, `Delta Fminus`, `c Delta Fplus`, `c Delta Fminus`.

The locus c=0 is a divisor and costs only O(p).

### Exact nonsquareness certificate

Use the cyclic Fourier coordinates

`x_0=A+B+C`, `x_1=A-B+D`, `x_2=A+B-C`, `x_3=A-B-D`.

On the transverse section D=1, elimination of A gives the irreducible quartic curve

`16B^4C - 8B^2C^3 - 4B^2C^2 + 4B^2 + C^5 + C^4 - 2C^3 + C - 1 = 0`.

Specialising further to C=2 gives the irreducible number-field polynomial

`32B^4 - 76B^2 + 33`.

Inside this quartic number field, Sage verifies that each of the nine weights

`Delta`, `Fplus`, `Fminus`, `cFplus`, `cFminus`,
`DeltaFplus`, `DeltaFminus`, `cDeltaFplus`, `cDeltaFminus`

is a nonsquare.

A square in the generic function field would remain a square under this good specialisation. Hence all nine generic weights are nonsquares.

Therefore the corresponding complete character sums on the ordered-cycle surface are O(p^(3/2)).

The local-root cover has odd generic degree three over the base surface. A nonsquare cannot become a square in an odd-degree field extension. Thus the degree-p discriminant weights remain nontrivial on the root cover, giving the same O(p^(3/2)) bound for signed root incidence.

## 5. Exact incidence decompositions

For every compatible irreducible quartic h, let

- `r(h)` be the number of roots of its attached local cubic;
- `delta(h)` indicate the triple-root local cubic;
- `eta(h)=chi(Disc F)`;
- `Delta(h)` be the local-cubic discriminant.

The exact cubic irreducibility indicator gives

`L_(a,4) = [2M_(a,4) + S_Delta - R_(a,4) - T_(a,4)]/3`,

where

`S_Delta = sum_h chi(Delta(h))`.

The signed form is

`L_(a,4)^chi = [2S_F + S_FDelta - R_F - T_F]/3`.

The Kummer certificates and root-cover theorem give

`S_Delta, S_F, S_FDelta, R_F = O(p^(3/2))`,

and the two triple-root terms are O(1).

## 6. Quartic incidence theorem

### Theorem QLI.2

Uniformly for every p >= 5 and every nonzero a in F_p,

`L_(a,4) = p^2/12 + O(p^(3/2))`.

### Theorem QLI.3

Uniformly for every p >= 5 and every nonzero a in F_p,

`L_(a,4)^chi = O(p^(3/2))`.

The constants are absolute and effective.

Consequently

`L_(a,4,+) = p^2/24 + O(p^(3/2))`,

`L_(a,4,-) = p^2/24 + O(p^(3/2))`.

## 7. Positive-parity sector rough through degree four

Let `N_(a,rough4,+)` count locally admissible positive-discriminant members with no irreducible factor of degree 2, 3, or 4.

The completed quadratic factorial sieve gives

`N_(a,no2,+) = 29p^2/288 + O(p^(3/2))`.

A member with a cubic or quartic factor is counted at least once by the corresponding incidence. Therefore

`N_(a,rough4,+)`
`  >= N_(a,no2,+) - L_(a,3,+) - L_(a,4,+)`
`  = [29/288 - 1/18 - 1/24]p^2 + O(p^(3/2))`
`  = p^2/288 + O(p^(3/2))`.

### Corollary QLI.4

For all sufficiently large p, every nonzero cubic slice contains locally admissible positive-discriminant members with no factors of degrees 2, 3, or 4.

This does not yet prove irreducibility. It is the strongest completed roughness level of the parity sieve: any remaining positive-parity reducible member in this sector has at least three factors and smallest factor degree at least five.

## 8. Reproducibility

The characteristic-zero checks are recorded in

`quartic_cycle_geometry_audit.sage`.

The Sage/Hugging Face verification jobs were:

- base surface: `6a5f932b13e6ef894d549dae`;
- local-root cover: `6a5f933413e6ef894d549db0`;
- triple-root locus: `6a5f9346d09dc1f57c6bf8d3`;
- number-field square-class audit: `6a5f965813e6ef894d549de9`.