# Cartier complementary torus grading and the one-level tail

**Date:** 2026-07-22  
**Status:** exact arithmetic theorem for every dominant `w=1` Cauchy-Binet term. It explains why the first possible support beyond the old boundary is exactly the single level observed in the complete ledgers. It reduces `CT1-w1` to the integer inequality `beta<=gamma+2`.

## 1. Complementary notation

Use the notation of `CARTIER_COMPLEMENTARY_MINOR_REDUCTION.md`.

Let

`E subset {1,...,p-1}`, `p-3 notin E`,

`N={1,...,p-1}\E`,

`Q=(N\{p-3}) union {0}`.

For a Cauchy-Binet degree set `M subset {0,...,p-1}`, put

`R={0,...,p-1}\M`.

The two complements have equal size:

`C_0=E union {0}`, `C_1=E union {p-3}`.

Write the monomial attached to the term as

`a^I c^J d^K`.

## 2. Exact complementary degrees

The total cubic-factor count is

`I=(sum R-sum E-(p-3))/2.`

Since

`sum N=p(p-1)/2-sum E`,

`sum Q=p(p-1)/2-sum E-(p-3)`,

the linear and constant degrees are

`J=sum Q-3I`

and

`K=sum N-sum Q+2I`.

Substitution gives:

### Theorem CCG.1 — complementary degree formulas

`boxed( K=sum R-sum E, )`

`boxed( J=(p^2-3+sum E-3sum R)/2. )`

These identities are independent of whether the two complementary minors vanish.

## 3. Torus survivor equation

For a torus survivor, write

`J=alpha(p-1)`,

`K=beta(p-1)`,

with integers `alpha,beta>=0` in the positive-exponent projection.

The formula for `K` gives

`sum R=sum E+beta(p-1).`

Insert this into the formula for `J`:

`2alpha(p-1)`

` =p^2-3-2sum E-3beta(p-1).`

Reducing modulo `p-1` gives

`2(sum E+1)=0 mod (p-1).`

Therefore define the integer

`boxed( gamma=2(sum E+1)/(p-1). )`

The full equality then becomes:

### Theorem CCG.2 — torus grading simplex

Every dominant torus-surviving term satisfies

`boxed( 2alpha+3beta+gamma=p+1. )`

Thus the identity subset contributes a third nonnegative grading coordinate. The possible survivor triples lie on one finite integral simplex.

## 4. Filtration weight

The `(1,2)`-filtration weight is

`W=(alpha+2beta)(p-1).`

Using CCG.2,

`2(alpha+2beta)=p+1+beta-gamma.`

Hence:

### Corollary CCG.3 — excess formula

`boxed( W=(p^2-1)/2 + ((beta-gamma)/2)(p-1). )`

In particular `beta-gamma` is even. Therefore there is no survivor level halfway between consecutive multiples of `p-1`.

The old boundary corresponds to

`beta<=gamma`.

The first possible excess has

`beta=gamma+2`

and weight

`boxed( W=(p-1)(p+3)/2. )`

This is exactly the single extra level found at every audited prime `29<=p<=47`.

## 5. Corrected support lemma

The complementary inequality from `CT1-w1` is

`sum R<=3sum E+2p.`

Using

`sum R=sum E+beta(p-1)`

and

`2sum E=gamma(p-1)-2`,

one obtains

`beta(p-1)<=gamma(p-1)+2(p-1)`.

Thus:

### Corollary CCG.4 — integer form of CT1-w1

`boxed( CT1-w1 is equivalent to beta<=gamma+2. )`

Equivalently, the dominant corrected support theorem says that the nonzero product of the two complementary minors excludes all torus triples with

`beta>=gamma+4.`

The `p=29` counterexample has `beta=gamma+2` and is therefore extremal.

## 6. Structural consequence

The one-level tail pattern is not merely a numerical spacing artefact.

- Torus grading forces support levels to differ from the old boundary by integral multiples of `p-1`.
- The parity equation forces the excess coordinate `beta-gamma` to be even.
- Therefore the corrected bound `B_1` permits exactly one new level and no intermediate level.

What remains open is not the spacing but the exclusion of `beta-gamma>=4` by the product

`det(P^(-1))_(R,E union {0}) det(U)_(R,E union {p-3}).`

## 7. New proof target

The dominant Route-1 gate can now be stated without degree sums:

> If the two explicit complementary minors are nonzero modulo `p` and the torus grading holds, prove `beta-gamma<=2`.

The inverse-substitution entries are signed Raney numbers:

`|U_(s+2h,s)|=s/(s+3h) binom(s+3h,h),`

counting forests of `s` full ternary trees with `h` internal vertices and `s+2h` leaves. This suggests a nonintersecting-forest interpretation of the remaining minor inequality.

## 8. Epistemic classification

- Complementary degree formulas: exact.
- Integrality of `gamma`: exact consequence of torus orthogonality.
- Grading simplex and excess formula: exact.
- Explanation of the single allowed extra level under CT1: exact.
- Equivalence of CT1-w1 and `beta<=gamma+2`: exact.
- Nonintersecting-forest proof of the minor bound: proposed next mechanism, not yet proved.
- Full CT1 and d=1 crown: open.
