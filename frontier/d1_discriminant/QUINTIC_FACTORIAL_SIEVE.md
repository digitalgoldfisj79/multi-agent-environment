# Exact quintic-factorial sieve

**Date:** 2026-07-21  
**Status:** all quintic factorial moments are proved, signed and unsigned; quintic factors can be removed by exact inclusion-exclusion.

## 1. Setup

Define

`Q_(a,5,j)=sum_(locally admissible F) binom(nu_5(F),j)`

and its discriminant-weighted analogue `Q_(a,5,j)^chi`.

`QUINTIC_LOCAL_INCIDENCE.md` proves that every quintic factor is a period-five cycle of the cubic map and that

`nu_5(F) <= 48`.

## 2. Marked-cycle covers

Morton's generic periodic-point theorem gives

`G_5=C_5 wr S_48`

for the generic centered cubic family. This group is transitive on every ordered j-tuple of distinct five-cycles with one marked point in each cycle, for `0 <= j <= 48`.

The corresponding finite-field twist selecting actual irreducible quintic factors is geometrically integral. Its marked degree is

`j! 5^j`.

The local cubic field is linearly disjoint from the full period-five field by the ramification calculation in `quintic_local_audit.sage`; local rootlessness contributes density `1/3`.

### Theorem QFS5.1

For every `0 <= j <= 48`, uniformly in p and nonzero a,

`Q_(a,5,j)=p^2/[3 j!5^j]+O(p^(3/2))`.

## 3. Signed moments

The degree-p discriminant Kummer classes have finite branch components among

`c=0`, `Fplus=0`, `Fminus=0`.

At the origin, every dynatomic polynomial of the map `X^3` is separable in characteristic zero, while the local discriminant is nonzero. Hence these Kummer fields are not contained in the period-five/local compositum. Products with the local discriminant retain an extra raw branch component.

On a local-root cover, odd degree preserves nonsquareness.

### Theorem QFS5.2

For every `0 <= j <= 48`, uniformly in p and nonzero a,

`Q_(a,5,j)^chi=O(p^(3/2))`.

## 4. Exact quintic deletion

Put

`E_5=sum_(j=0)^48 (-1/5)^j/j!`.

Exact inclusion-exclusion gives:

### Theorem QFS5.3

`N_(a,no5)=(E_5/3)p^2+O(p^(3/2))`,

`M_(a,no5)=O(p^(3/2))`.

Consequently each parity sector has size

`N_(a,no5,+)=(E_5/6)p^2+O(p^(3/2))`,

`N_(a,no5,-)=(E_5/6)p^2+O(p^(3/2))`.

Numerically,

`E_5=0.8187307530779818...`.

This is the fourth complete single-degree multiplicative deletion.

## 5. Reproducibility

The local-field ramification check is in `quintic_local_audit.sage`. Maximal period-five monodromy is the specialization argument recorded in `QUINTIC_LOCAL_INCIDENCE.md`, using Morton's full wreath-product theorem for `X^3+t`.