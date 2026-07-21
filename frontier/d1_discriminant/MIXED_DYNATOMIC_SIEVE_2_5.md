# Exact mixed dynatomic sieve through degree five

**Date:** 2026-07-21  
**Status:** all mixed factorial moments for factor degrees 2, 3, 4, and 5 are proved, signed and unsigned; these four degrees are removed simultaneously.

## 1. Dynatomic periods and factor degrees

For

`g_(a,c,d)(X)=-aX^3-cX-d`,

a degree-k irreducible factor of

`F_(a,c,d)(X)=X^p+aX^3+cX+d`

is a Frobenius k-cycle and hence an exact period-k cycle of g.

For `k=2,3,4,5`, let

`r_k=(1/k)sum_(m|k) 3^m mu(k/m)`.

Then

`r_2=3`, `r_3=8`, `r_4=18`, `r_5=48`.

The generic marked period-k Galois group is

`G_k=C_k wr S_(r_k)`.

## 2. Direct product monodromy

On the unicritical specialization `X^3+t`, Morton's Theorem D proves that dynatomic splitting fields belonging to distinct periods are linearly disjoint. It also proves the full wreath-product group for each period.

The specialized compositum for periods 2,3,4,5 therefore has group

`G_2 x G_3 x G_4 x G_5`.

A specialized separable Galois group embeds into the generic group, while the generic compositum is always a subgroup of this same product. Hence the generic centered two-parameter family also has full direct-product arithmetic and geometric monodromy:

### Theorem MDS.1

`G_(2,3,4,5)=product_(k=2)^5 (C_k wr S_(r_k))`.

## 3. Independence of local admissibility

The local cubic has generic Galois group `S_3` and discriminant

`Delta_H=-4(c+1)^3-27d^2`.

Any nontrivial intersection with the dynatomic product would contain its quadratic sign field: no factor `G_k` has an `S_3` quotient except the period-two factor, and equality with that `S_3` field would still force equality of quadratic sign fields.

On the unicritical line c=0, set

`d=2 sqrt(-3)/9`,

so `4+27d^2=0`.

The exact dynatomic polynomials of periods 2,3,4,5 have degrees

`6,24,72,240`

and are all squarefree at this value. The period-two and period-three checks are in `mixed_dynatomic_local_audit.sage`; the period-four and period-five checks are in the existing quartic and quintic audit files.

Thus the full dynatomic product is unramified at the generic local-discriminant divisor. The local quadratic field is not contained in it, and the local `S_3` field is linearly disjoint from the complete dynatomic product.

Local rootlessness contributes density `1/3` independently of every mixed factor configuration.

## 4. Mixed factorial moments

For a tuple

`j=(j_2,j_3,j_4,j_5)`

with

`0 <= j_k <= r_k`,

define

`Q_(a;j)=sum_(locally admissible F) product_(k=2)^5 binom(nu_k(F),j_k)`.

The full direct-product marked monodromy is transitive on an ordered selection of `j_k` distinct k-cycles with one marked root in each selected cycle. The marked degree is

`product_(k=2)^5 j_k! k^(j_k)`.

Fixed-degree Lang--Weil estimates give:

### Theorem MDS.2

Uniformly in p and nonzero a,

`Q_(a;j)`
` = p^2/[3 product_(k=2)^5 j_k! k^(j_k)] + O(p^(3/2))`.

## 5. Signed mixed moments

The raw degree-p discriminant Kummer fields have finite branch components among

`c=0`, `Fplus=0`, `Fminus=0`.

At the origin, all dynatomic polynomials of `X^3` are separable and the local discriminant is nonzero. Therefore these Kummer fields are not contained in the dynatomic/local compositum. Products with the local discriminant retain an extra raw branch component.

On local-root covers, odd degree preserves nonsquareness.

### Theorem MDS.3

For every allowed tuple j,

`Q_(a;j)^chi=O(p^(3/2))`.

## 6. Exact simultaneous deletion

For k=2,3,4,5 put

`E_k=sum_(j=0)^(r_k) (-1/k)^j/j!`.

Exact finite inclusion-exclusion gives

`N_(a,no2to5)`
` = (1/3) product_(k=2)^5 E_k * p^2 + O(p^(3/2))`,

and the discriminant-character mass of this family is `O(p^(3/2))`.

### Theorem MDS.4

Each parity sector with no factors of degrees 2,3,4,5 has size

`N_(a,no2to5,+)`
` = (1/6) product_(k=2)^5 E_k * p^2 + O(p^(3/2))`,

with the same formula for negative discriminant.

Numerically,

`(1/6) product_(k=2)^5 E_k`
` = 0.04600533167213053...`.

This replaces all previous rough-through-five lower bounds by an exact asymptotic.

## 7. Consequence for degree six

The expected positive degree-six first-incidence density is `1/36`.

Since

`0.04600533167213053 - 1/36`
` = 0.01822755389435275... > 0`,

a signed degree-six single-factor theorem with the standard main term will produce a positive-discriminant sector rough through degree six.

The method has now reached the point where every further fixed period can in principle be added by the same wreath-product and ramification procedure. The remaining crown obstruction is uniformity when the cutoff grows with p, not any fixed factor degree.