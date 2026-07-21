# Mixed quadratic-cubic factorial sieve

**Date:** 2026-07-21  
**Status:** the full finite mixed factorial-moment table is proved; quadratic and cubic factors can be removed simultaneously, signed and unsigned.

## 1. Setup

For the locally admissible family

`F_(a,c,d)(X)=X^p+aX^3+cX+d`,

define

`Q_(a;i,j) = sum_F binom(nu_2(F),i) binom(nu_3(F),j)`

and

`Q_(a;i,j)^chi = sum_F chi(Disc F) binom(nu_2(F),i) binom(nu_3(F),j)`.

The relevant orders are

`0 <= i <= 3`, `0 <= j <= 24`.

The quadratic multiplicity is at most three. The cubic generic degree is eight and the uniform multiplicity is at most 24, with orders above eight confined to a fixed divisor.

## 2. Full quadratic marked monodromy

After geometric scaling take a=1. The trace s of a compatible quadratic factor satisfies

`T_(c,d)(s)=s^3+(c-2)s-d=0`.

The generic trace cover has Galois group `S_3`. For a trace root s, the associated quadratic discriminant is

`delta(s)=-3s^2-4(c-1)`.

Marking one root of each of the three possible quadratic factors gives a Kummer kernel in `F_2^3` stable under `S_3`.

The pair and triple nonsquareness audit in `QUADRATIC_FACTORIAL_SIEVE.md` proves that every nonempty product of the three generic delta classes is nonsquare. Hence the kernel is full:

`G_2 = C_2^3 semidirect S_3`.

This group is transitive on an ordered i-tuple of distinct quadratic blocks together with one marked root in each block, for every `0 <= i <= 3`.

## 3. Full cubic marked monodromy

By `CUBIC_MONODROMY.md` and `CUBIC_ROOT_MONODROMY.md`, the corresponding cubic group is

`G_3 = C_3^8 semidirect S_8`.

It is transitive on ordered marked j-tuples of distinct cubic blocks for every `0 <= j <= 8`.

## 4. Linear disjointness of the two factor covers

Any intersection of the quadratic and cubic marked splitting fields is Galois over the coefficient field and yields a common quotient of `G_2` and `G_3`.

The only possible nontrivial common quotient is `C_2`:

- `G_2` has no quotient of order divisible by an isolated C_3 without a C_2 contribution;
- the only relevant common quotient of `G_3` with a quotient of `G_2` is the sign quotient of its `S_8` factor.

The quadratic marked field has three nontrivial quadratic classes. At d=0 they are:

1. the trace-cubic sign class
   `c-2`;
2. the product of the three quadratic-root Kummer classes
   `c-1`;
3. their product
   `(c-2)(c-1)`.

The second assertion follows from the exact norm

`Res_s(s^3+(c-2)s-d, -3s^2-4(c-1))`
` = -4c^3-12c^2-27d^2+16`,

which at d=0 is `-4(c-1)(c+2)^2`.

The unique quadratic sign class of the cubic `S_8` orientation cover is, at d=0,

`c^2-c+1`.

These four square classes are distinct over the algebraic closure. Therefore the quadratic and cubic marked splitting fields are linearly disjoint.

Thus the combined geometric monodromy is

`G_2 x G_3`.

## 5. Independence of local admissibility

The local cubic has generic Galois group `S_3` and discriminant square class, at d=0,

`c+1`.

The four classes

`c-2`, `c-1`, `c^2-c+1`, `c+1`

are independent in `Qbar(c)^*/Qbar(c)^{*2}`: each introduces a distinct simple zero. Hence the local `S_3` splitting field has trivial intersection with the combined marked-factor field.

It retains full `S_3` monodromy on every mixed marked fibre power. Local rootlessness therefore contributes the Frobenius 3-cycle density

`1/3`.

## 6. Mixed unsigned moments

For `0 <= i <= 3` and `0 <= j <= 8`, take the canonical finite-field twists selecting actual irreducible quadratic and cubic factors. The combined marked cover is geometrically integral.

Every ordered factor tuple is represented by

- `2^i` choices of roots in its quadratic factors;
- `3^j` choices of roots in its cubic factors;
- `i!j!` orderings.

Lang-Weil and the independent local `S_3` condition give:

### Theorem MQC.1

Uniformly for every p >= 5 and nonzero a,

`Q_(a;i,j) = p^2/[3 i! 2^i j! 3^j] + O(p^(3/2))`

for all `0 <= i <= 3`, `0 <= j <= 8`.

This contains the previously proved pure quadratic and pure cubic factorial moments as boundary cases.

## 7. Mixed signed moments

The raw degree-p discriminant Kummer classes are generically nonsquare by the existing symbolic audits.

They remain independent after adjoining all factor and local splitting fields. At d=0, the raw classes specialize to c or 1, whereas every nontrivial quadratic class in the combined marked/local field is a nonempty product of

`c-2`, `c-1`, `c^2-c+1`, `c+1`.

No such product has square class c or 1. The generic classes that specialize to 1 are known independently to be nonsquare, so they are not the trivial class either.

Hence every signed Kummer cover remains geometrically nontrivial on every mixed fibre power.

### Theorem MQC.2

Uniformly for `0 <= i <= 3`, `0 <= j <= 8`,

`Q_(a;i,j)^chi = O(p^(3/2))`.

## 8. Exceptional cubic orders

For `9 <= j <= 24`, all coefficient pairs contributing to `Q_(a;i,j)` lie on the fixed exceptional divisor of the cubic compatible map. Since `nu_2 <= 3` and `nu_3 <= 24`,

`Q_(a;i,j)=O(p)`,

`Q_(a;i,j)^chi=O(p)`

uniformly for every `0 <= i <= 3`.

## 9. Simultaneous deletion of quadratic and cubic factors

Let

`N_(a,no23) = # {locally admissible F : nu_2(F)=nu_3(F)=0}`

and let `M_(a,no23)` be its discriminant-character mass.

Exact finite inclusion-exclusion gives

`N_(a,no23)=sum_(i=0)^3 sum_(j=0)^24 (-1)^(i+j) Q_(a;i,j)`,

with the analogous signed identity.

Put

`C_2 = sum_(i=0)^3 (-1/2)^i/i! = 29/48`,

`C_3 = (1/3)sum_(j=0)^8 (-1/3)^j/j!`
`    = 189550849/793618560`.

### Theorem MQC.3

`N_(a,no23) = C_2 C_3 p^2 + O(p^(3/2))`

`             = (5496974621/38093690880)p^2 + O(p^(3/2))`,

and

`M_(a,no23)=O(p^(3/2))`.

Consequently

`N_(a,no23,+)`
` = (5496974621/76187381760)p^2 + O(p^(3/2))`,

`N_(a,no23,-)`
` = (5496974621/76187381760)p^2 + O(p^(3/2))`.

The common parity-sector density is

`0.07215072225891911...`.

This is the first simultaneous multiplicative deletion across two distinct factor degrees.

## 10. Improved roughness through degree four

Subtract the positive quartic incidence from `QUARTIC_LOCAL_INCIDENCE.md`:

`N_(a,rough4,+)`
` >= N_(a,no23,+)-L_(a,4,+)`
` = [5496974621/76187381760 - 1/24]p^2 + O(p^(3/2))`
` = (2322500381/76187381760)p^2 + O(p^(3/2))`.

### Corollary MQC.4

For all sufficiently large p, every nonzero cubic slice contains locally admissible positive-discriminant members with no factors of degrees 2, 3, or 4, with density at least

`2322500381/76187381760`

`=0.03048405559225244...`.

This is almost nine times the earlier first-moment margin `1/288`.

The expected positive degree-five incidence density is `1/30`, still slightly larger than this margin. Passing degree five therefore requires either exact quartic deletion, mixed quartic moments, or the determinant route; another first-moment subtraction is not enough.