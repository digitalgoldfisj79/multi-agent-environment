# Exact quartic-factorial sieve

**Date:** 2026-07-21  
**Status:** all quartic factorial moments are proved, signed and unsigned; quartic factors can be removed by exact finite inclusion-exclusion.

## 1. Setup

Let

`F_(a,c,d)(X)=X^p+aX^3+cX+d`, `a != 0`,

and let `nu_4(F)` be the number of distinct monic irreducible quartic factors. On the locally admissible family define

`Q_(a,4,j)=sum_F binom(nu_4(F),j)`

and

`Q_(a,4,j)^chi=sum_F chi(Disc F) binom(nu_4(F),j)`.

`QUARTIC_FACTORIAL_STATUS.md` proves

`nu_4(F) <= 18`.

Thus orders `0 <= j <= 18` suffice for exact quartic deletion.

## 2. Maximal marked-cycle monodromy

`QUARTIC_MONODROMY.md` proves that the fourth dynatomic polynomial of the generic centered cubic map has arithmetic and geometric Galois group

`G_4=C_4 wr S_18=C_4^18 semidirect S_18`.

This is the full group permitted by the 18 dynamical four-cycles. It acts transitively on an ordered j-tuple of distinct cycles together with one marked point in each cycle, for every `0 <= j <= 18`.

Consequently the corresponding ordered marked fibre power is geometrically integral and has generic degree

`j! 4^j`

over the coefficient plane.

For the complete coefficient slice, fixed-degree Lang--Weil estimates give

`M_(a,4,j)=p^2/(j!4^j)+O(p^(3/2))`.

## 3. Independence of the local cubic

After geometric scaling take a=1. The local cubic is

`K_(c,d)(Z)=Z^3+(c+1)Z+d`

with discriminant

`Delta_H=-4(c+1)^3-27d^2`.

Its generic Galois group is `S_3`.

Any nontrivial common quotient of `S_3` and `G_4` must be `C_2`:

- the base group `C_4^18` is a 2-group;
- every homomorphism `S_18 -> S_3` has image at most `C_2`.

Thus a nontrivial intersection would force the local discriminant field into the quartic dynatomic splitting field.

This is excluded by exact ramification on the unicritical line c=0. For

`g(X)=X^3+d`,

the discriminant of the degree-72 fourth dynatomic polynomial factors as

`Disc_X Phi_4 =`
` (729d^4+1620d^2+1000)^2`
` (729d^4-324d^2+100)^3`
` P_16(d)^4 P_24(d)^4`,

where `P_16` and `P_24` are the explicit degree-16 and degree-24 factors recorded in `quartic_factorial_audit.sage`.

The local branch polynomial on this line is

`4+27d^2`.

It is coprime to every displayed dynatomic factor. Hence the local quadratic field ramifies at a divisor where the dynatomic field is unramified and cannot be contained in it.

Therefore the local `S_3` field and the full marked quartic field are linearly disjoint.

The local rootless condition is the Frobenius 3-cycle class in `S_3`, of density `1/3`.

### Theorem QFS4.1

For every `0 <= j <= 18`, uniformly in p and nonzero a,

`Q_(a,4,j)=p^2/[3 j!4^j]+O(p^(3/2))`.

All constants are absolute and effective.

## 4. Signed moments

For a=1, the exact degree-p discriminant character is split into the raw quadratic classes

`Fplus  = 4c^3+12c^2+9c+27d^2`,

`Fminus = 4c^3-12c^2+9c+27d^2`,

and their products with c. Multiplication by the local discriminant gives the additional classes used in the local irreducibility projector.

Each nontrivial raw class has a finite branch component among

`c=0`, `Fplus=0`, `Fminus=0`.

These components are not components of either the quartic dynatomic branch divisor or the local discriminant divisor:

- the c=0 dynatomic specialization is separable and has maximal monodromy;
- at `(c,d)=(0,0)`, the fourth dynatomic polynomial is separable and `Delta_H=-4`;
- `Fplus` and `Fminus` are smooth at the origin because their c-derivative is 9.

Therefore none of the raw Kummer fields is contained in the compositum of the marked quartic field and the local cubic field. Products with `Delta_H` retain the extra branch component and are also independent.

On the local-root cover, the extension in the root variable has odd degree three, so a remaining nonsquare cannot become a square.

Fixed-degree Kummer Lang--Weil estimates therefore give:

### Theorem QFS4.2

For every `0 <= j <= 18`, uniformly in p and nonzero a,

`Q_(a,4,j)^chi=O(p^(3/2))`.

## 5. Exact quartic deletion

Let

`N_(a,no4)=# {locally admissible F : nu_4(F)=0}`

and let `M_(a,no4)` be its discriminant-character mass.

Exact inclusion-exclusion gives

`N_(a,no4)=sum_(j=0)^18 (-1)^j Q_(a,4,j)`,

`M_(a,no4)=sum_(j=0)^18 (-1)^j Q_(a,4,j)^chi`.

Put

`C_4=(1/3)sum_(j=0)^18 (-1/4)^j/j!`

`   =342647244523312988285643481/1319903312777860217831424000`.

### Theorem QFS4.3

Uniformly for every p >= 5 and nonzero a,

`N_(a,no4)=C_4 p^2+O(p^(3/2))`,

`M_(a,no4)=O(p^(3/2))`.

Consequently

`N_(a,no4,+)=(C_4/2)p^2+O(p^(3/2))`,

`N_(a,no4,-)=(C_4/2)p^2+O(p^(3/2))`.

Numerically,

`C_4=0.2596002610238016...`.

This is the third complete single-degree multiplicative deletion.

## 6. Intersection with the completed no-2/no-3 sector

Let U be the positive-discriminant locally admissible sector. Its density is `1/6`.

Let A be the positive sector with no quadratic or cubic factor, and B the positive sector with no quartic factor. Then

`#(A intersect B) >= #A + #B - #U`.

Using `MIXED_QUADRATIC_CUBIC_SIEVE.md` and Theorem QFS4.3 gives

`N_(a,no234,+)`
` >= D_4 p^2+O(p^(3/2))`,

where

`D_4 = 5496974621/76187381760 + C_4/2 - 1/6`

`    = 2514872562887291005263119587/71274778890004451762896896000`

`    = 0.03528418610415326...`.

This lower bound does not require mixed quartic moments.

It exceeds the expected positive degree-five first-incidence density `1/30`. Thus a signed degree-five single-factor theorem with the standard main term will already produce a positive sector rough through degree five.

## 7. Reproducibility

`quartic_factorial_audit.sage` reconstructs the fourth dynatomic polynomial on the unicritical line, factors its discriminant, and checks the coprimality with the local branch polynomial.