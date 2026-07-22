# Boundary inertia on the normalized q-line

**Date:** 2026-07-22  
**Status:** exact geometric inertia cycle types at q=0 and q=2, and exact wild inertia group/jump at q=infinity, proved for the generic t-fibre. Direct-image effectivity remains open.

## 1. The two-parameter normal form

Work over an algebraically closed field k of characteristic p>=5 and consider

`P_(q,t)(X)=qX^p+X^3-3X-(q-2)t.`

For q outside `{0,2,infinity}`, this is the critical-value normalized degree-p cover from `CRITICAL_VALUE_NORMAL_FORM.md`. Its finite t-branch values are `+1` and `-1`.

Let `Lambda_p` be the p-cycle virtual character: it has value p on a p-cycle and zero on every other permutation.

## 2. The boundary q=0

Over `k(t)((q))`, reduction at q=0 is the generically separable cubic

`X^3-3X+2t`.

Its three roots lift unramified by Hensel's lemma.

The remaining p-3 roots have negative valuation and are governed to first order by

`qX^p+X^3=0`,

or

`X^(p-3)=-q^(-1)`.

Because p-3 is prime to p, the geometric tame inertia is cyclic and acts transitively on these p-3 roots.

### Theorem QBI.1

The geometric inertia generator at q=0 has cycle type

`boxed((p-3)(1)(1)(1).)`

No element of this inertia group is a p-cycle. Therefore

`boxed(Lambda_p|_(I_0)=0)`

in the rational representation ring.

## 3. The boundary q=2

Put `epsilon=q-2`. At epsilon=0 the polynomial becomes

`G(X)=2X^p+X^3-3X`.

One has

`G'(X)=3(X^2-1)`.

The roots `X=+1` and `X=-1` are double, since `G(+/-1)=0` and the second derivative is nonzero. The remaining p-4 roots are simple.

For generic t, the epsilon-deformation splits each double root quadratically. After passing to geometric inertia, both square roots use the same tame parameter `sqrt(epsilon)`; the residue-field distinction is unramified.

### Theorem QBI.2

The geometric inertia generator at q=2 has cycle type

`boxed((2)(2)(1)^(p-4).)`

Again no inertia element is a p-cycle, so

`boxed(Lambda_p|_(I_2)=0.)`

## 4. The boundary q=infinity

Put `r=q^(-1)` and divide the equation by q:

`X^p-t+r(X^3-3X+2t)=0.`

The residue polynomial `X^p-t` is purely inseparable over `k(t)`. Make the purely inseparable base change

`t=tau^p`.

This does not alter the geometric etale topos. After writing `X=tau+Z`, the local equation is

`Z^p+r[Z^3+3tau Z^2+(3tau^2-3)Z+H(tau)]=0`,

where

`H(tau)=tau^3-3tau+2tau^p`.

For generic tau, both `H(tau)` and `3tau^2-3` are units. The polynomial is Eisenstein in r, so it defines a totally ramified separable extension of degree p. Its derivative at a root is r times a unit. With the extension valuation normalized by `v_L(r)=p`, the different exponent is exactly p.

Let I be the normal-closure inertia group. Since the p-adic valuation of `|S_p|` is one,

`I=C_p semidirect C_m`, `m|(p-1)`,

with a single positive lower jump j. The different formula for the degree-p subextension is

`p=(p-1)+j(p-1)/m`.

Thus `j/m=1/(p-1)`. The tame action on the unique wild ramification quotient is faithful, so `gcd(j,m)=1`. Hence:

### Theorem QBI.3

`boxed(I_infinity=C_p semidirect C_(p-1),)`

`boxed(j=1.)`

This is the full affine linear group on the p roots.

## 5. Virtual conductor at q=infinity

For `I=C_p semidirect C_(p-1)`, the p-cycle character has virtual invariants

`dim Lambda_p^I=1`,

`dim Lambda_p^(C_p)=p-1`,

and virtual rank zero.

The single jump gives

`Swan_infinity(Lambda_p)`
` =(1/(p-1))(0-(p-1))=-1.`

Therefore:

### Theorem QBI.4

`boxed(Swan_infinity(Lambda_p)=-1,)`

`boxed(Artin_infinity(Lambda_p)=-2.)`

The negative values are legitimate for a virtual representation and encode the cancellation between the hook constituents.

## 6. Consequence and limitation

At the root-local-system level, every affine q-boundary is invisible to the p-cycle virtual character, and all nontrivial boundary conductor is concentrated at q=infinity with constant virtual size.

This is substantially stronger than an O(p) conductor statement. It explains why the universal q-sums can plausibly have absolute Hasse-scale errors.

It does not yet prove such a bound. Proper/direct image in the t-direction can create vanishing-cycle cohomology, and a bound on the virtual conductor does not control the numerator-plus-denominator degrees of the resulting virtual L-function. The remaining theorem is an effectivity or cancellation-before-cohomology statement for the two-dimensional direct image.
