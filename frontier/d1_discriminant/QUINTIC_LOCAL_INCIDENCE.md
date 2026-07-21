# Locally admissible quintic-factor incidence

**Date:** 2026-07-21  
**Status:** unsigned and signed degree-five incidence theorems proved; a positive-discriminant sector rough through degree five follows.

## 1. Period-five model

Let

`g_(a,c,d)(X)=-aX^3-cX-d`.

Every root of an irreducible quintic factor of

`F_(a,c,d)(X)=X^p+aX^3+cX+d`

is an exact composition-period-five point of g.

Since five is prime, the fifth dynatomic polynomial is

`Phi_(g,5)(X)=[g^5(X)-X]/[g(X)-X]`.

Its degree is

`3^5-3=240=5*48`.

Consequently every member has at most 48 irreducible quintic factors.

## 2. Maximal dynatomic monodromy

As in `QUARTIC_MONODROMY.md`, specialize the generic centered cubic family to the unicritical line and apply Morton's generic periodic-point theorem.

The arithmetic and geometric Galois groups of the fifth dynatomic polynomial are

`G_5=C_5 wr S_48=C_5^48 semidirect S_48`.

The group is transitive on the 240 marked period-five points and on the 48 cycles.

The canonical finite-field twist selecting Frobenius five-cycles is geometrically integral. Lang--Weil therefore gives the complete compatible-quintic incidence

`M_(a,5)=p^2/5+O(p^(3/2))`.

## 3. Independence of the local cubic

The local cubic has generic Galois group `S_3` and discriminant

`Delta_H=-4(c+1)^3-27d^2`.

Any common quotient of `S_3` and `G_5` is at most `C_2`: the base group is a 5-group and every homomorphism `S_48 -> S_3` has image at most `C_2`.

It is therefore enough to show that the local discriminant field is not contained in the period-five splitting field.

On the unicritical line c=0, take

`d=2 sqrt(-3)/9`,

so that `4+27d^2=0`. Over `Q(sqrt(-3))`, the exact degree-240 polynomial

`Phi_5(X)=[(X^3+d)^5-X]/[(X^3+d)-X]`

has gcd one with its derivative. Thus the period-five field is unramified at the generic local-discriminant divisor.

This exact calculation is reproduced in `quintic_local_audit.sage`.

Hence the local `S_3` field and the period-five field are linearly disjoint. Local rootlessness contributes the 3-cycle density `1/3`.

### Theorem QLI5.1

Uniformly for every p >= 5 and nonzero a,

`L_(a,5)=p^2/15+O(p^(3/2))`.

## 4. Signed incidence

The raw degree-p discriminant Kummer classes have branch components among

`c=0`, `Fplus=0`, `Fminus=0`,

with

`Fplus=4c^3+12c^2+9c+27d^2`,

`Fminus=4c^3-12c^2+9c+27d^2`.

At the origin, the map is `X^3`; every exact period-five point is a simple root because

`(X^(3^5)-X)' = 3^5 X^(3^5-1)-1`

equals `3^5-1` on a nonzero periodic root. The local discriminant is also nonzero at the origin.

Thus the finite branch components of every raw Kummer class are absent from the period-five and local branch divisors. None of these quadratic fields is contained in their compositum. Products with the local discriminant retain an extra raw branch component.

On the local-root cover, odd extension degree preserves nonsquareness.

### Theorem QLI5.2

Uniformly for every p >= 5 and nonzero a,

`L_(a,5)^chi=O(p^(3/2))`.

Consequently

`L_(a,5,+)=p^2/30+O(p^(3/2))`,

`L_(a,5,-)=p^2/30+O(p^(3/2))`.

## 5. Roughness through degree five

`QUARTIC_FACTORIAL_SIEVE.md` gives the lower bound

`N_(a,no234,+) >= D_4 p^2+O(p^(3/2))`,

where

`D_4=2514872562887291005263119587/71274778890004451762896896000`

`   =0.03528418610415326...`.

Subtracting the positive quintic incidence gives

`N_(a,rough5,+)`
` >= [D_4-1/30]p^2+O(p^(3/2))`
` = D_5 p^2+O(p^(3/2))`,

where

`D_5=139046599887142613166556387/71274778890004451762896896000`

`   =0.001950852770819924...`.

### Corollary QLI5.3

For all sufficiently large p, every nonzero cubic slice contains locally admissible positive-discriminant members with no irreducible factors of degrees 2, 3, 4, or 5.

The remaining margin is smaller than the expected positive degree-six incidence `1/36`. Further progress requires exact quintic deletion, mixed moments, or a growing-degree compression.