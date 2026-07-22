# Fixed-cutoff dynatomic sieve in every period

**Date:** 2026-07-22  
**Status:** exact asymptotic theorem for every fixed cutoff K; constants are effective but not uniform when K grows with p.

## 1. Statement of the problem

For

`F_(a,c,d)(X)=X^p+aX^3+cX+d`, `a!=0`,

put

`g_(a,c,d)(X)=-aX^3-cX-d`.

If an irreducible factor of F has degree k, then on any one of its roots

`g(alpha)=alpha^p`.

For `k<p`, the Frobenius orbit has length k, so that factor is exactly an
exact period-k cycle of g.

Fix an integer `K>=2`.  We restrict to primes `p>K`; the finitely many
smaller primes are irrelevant to the fixed-K asymptotic and can be checked
separately.

For each k define

`r_k=(1/k) sum_(m|k) mu(k/m) 3^m`.

This is the number of generic exact period-k cycles of a cubic polynomial.
For a family member F, let `nu_k(F)` be the number of its irreducible
factors of degree k.

## 2. Direct-product dynatomic monodromy for an arbitrary finite cutoff

After geometric scaling it is enough to take `a=1`.  The centered cubic
family contains the unicritical line `X^3+t`, up to an affine change of
variables and signs.

Morton's Theorem D for `X^q+t`, together with its published corrigendum,
gives for every k:

`Gal(Phi_k)=C_k wr S_(r_k)`

and gives linear disjointness of the splitting fields belonging to distinct
periods.  This is also stated explicitly in later work on dynamically
distinguishing polynomials.

For a fixed finite set of periods `2,...,K`, the specialized Galois group is
therefore

`product_(k=2)^K (C_k wr S_(r_k)).`

A specialization group embeds into the generic centered-family group, while
the generic group is always a subgroup of this same product.  Hence:

### Theorem FCDS.1

Over characteristic zero, the arithmetic and geometric monodromy of the
combined exact-period covers `2,...,K` for the generic centered cubic family
is the full direct product

`G_[2,K]=product_(k=2)^K (C_k wr S_(r_k)).`

After reduction, the same geometric integrality statements hold outside a
finite set of primes depending on K.

## 3. Local rootlessness is independent of every fixed dynatomic product

The local cubic is

`H_(c,d)(Z)=Z^3+(c+1)Z+d`

with discriminant

`Delta_H=-4(c+1)^3-27d^2`.

Its generic Galois group is `S_3`.  Any nontrivial intersection of its
splitting field with the dynatomic compositum would force its quadratic sign
field into that compositum.  It is therefore enough to show that the generic
local-discriminant divisor is not a branch divisor of any exact-period cover
with period at least two.

Parameterize `Delta_H=0` by

`c=-1-3r^2`, `d=2r^3`.

The associated dynamical map is

`g_r(X)=-X^3+(1+3r^2)X-2r^3`.

The point r is a parabolic fixed point.  Choose `r^2=-1/3`.  After the
scaling `X=rZ`, the map becomes

`f(Z)=(Z^3+2)/3`.

This map has one finite critical point, Z=0, of multiplicity two.  On the
real interval `[0,1)` one has

`f(Z)-Z=(Z-1)^2(Z+2)/3>0`,

and `f(Z)<1`.  Thus the critical orbit increases to the parabolic fixed point
Z=1.

Every finite attracting or parabolic cycle of a polynomial requires a
critical orbit in its basin.  Since the unique finite critical orbit belongs
to the basin of Z=1, this map has no other finite cycle whose multiplier is a
root of unity.  The standard dynatomic multiplicity criterion then implies
that every exact dynatomic polynomial `Phi_k`, `k>=2`, is squarefree at this
parameter.

Consequently `Delta_H=0` is not a branch component of any period-k splitting
field for `k>=2`.  It is therefore unramified in every finite dynatomic
compositum.

### Theorem FCDS.2

For every fixed K, the local `S_3` splitting field is linearly disjoint from
the complete period `2,...,K` dynatomic compositum.

The local rootless condition is the Frobenius 3-cycle class in this
independent `S_3`, and contributes density `1/3` on every mixed marked-cycle
cover.

## 4. Independence of the degree-p discriminant character

The signed sieve uses the already established raw quadratic classes for the
degree-p discriminant.  Every nontrivial class has a finite branch component
among

`c=0`, `Fplus=0`, `Fminus=0`,

where

`Fplus =4c^3+12c^2+9c+27d^2`,

`Fminus=4c^3-12c^2+9c+27d^2`.

At `(c,d)=(0,0)`, the dynamical map is `-X^3`.  Its periodic points are zero
and roots of unity, and every exact dynatomic polynomial is squarefree in
characteristic zero.  The local discriminant is `-4`, so the local cubic is
also unramified there.  The divisors `Fplus=0` and `Fminus=0` are smooth at
the origin because their c-derivative is 9.

Thus none of the displayed raw branch components is a component of the
branch divisor of the full dynatomic/local compositum, for any finite K.
The existing characteristic-zero nonsquareness audits exclude the remaining
trivial square class.  Passing to a local-root cover has odd degree three and
cannot turn a nonsquare into a square.

### Theorem FCDS.3

Every nontrivial degree-p discriminant Kummer sheaf remains geometrically
nontrivial on every mixed marked-cycle/local cover involving periods
`2,...,K`.

## 5. All mixed factorial moments through K

For a tuple

`j=(j_2,...,j_K)`, `0<=j_k<=r_k`,

define on the locally admissible family

`Q_(a;j)=sum_F product_(k=2)^K binom(nu_k(F),j_k)`

and define `Q_(a;j)^chi` by inserting `chi(Disc F)`.

The full direct-product wreath group is transitive on an ordered selection
of `j_k` distinct k-cycles with one marked point on every selected cycle.
The marked degree is

`product_(k=2)^K j_k! k^(j_k)`.

The local cubic is independent and contributes density `1/3`.  Lang--Weil
on the resulting fixed-dimensional covers gives, for K fixed and outside a
finite set of primes depending on K:

### Theorem FCDS.4

`Q_(a;j)`

` = p^2/[3 product_(k=2)^K j_k! k^(j_k)] + O_K(p^(3/2))`,

uniformly in nonzero a and in the finitely many allowed tuples j.

The signed moments satisfy

`Q_(a;j)^chi=O_K(p^(3/2)).`

All constants are effective once K is fixed.

## 6. Exact simultaneous deletion through K

Put

`E_k=sum_(j=0)^(r_k) (-1/k)^j/j!`.

Because `0<1/k<1`, every alternating partial sum E_k is positive.  Exact
finite inclusion--exclusion over all cycle counts gives:

### Theorem FCDS.5

For every fixed `K>=2`, uniformly in nonzero a,

`N_(a,no[2,K])`

` = (1/3) product_(k=2)^K E_k * p^2 + O_K(p^(3/2))`,

where `N_(a,no[2,K])` counts locally admissible members with no irreducible
factor of any degree `2<=k<=K`.

The discriminant-character mass of this family is `O_K(p^(3/2))`.
Consequently each parity sector has the exact fixed-cutoff asymptotic

`boxed(N_(a,no[2,K],+))`

` = (1/6) product_(k=2)^K E_k * p^2 + O_K(p^(3/2))`,

with the same formula for the negative sector.

In particular, for every fixed K and all sufficiently large p, every
nonzero cubic slice contains positive-discriminant locally admissible members
with no factor degree at most K.

For `K=5` this recovers the previously proved density

`0.04600533167213053...`.

Further values of the positive-sector density are

- `K=6`: `0.03894267250798985...`;
- `K=7`: `0.03375854215438538...`;
- `K=8`: `0.02979180888701659...`;
- `K=10`: `0.02412195387618535...`.

## 7. Sieve dimension and the remaining uniformity wall

The truncation in E_k is extraordinarily deep because `r_k` grows like
`3^k/k`.  Hence

`E_k=e^(-1/k)+O(1/[k^(r_k+1)(r_k+1)!]).`

The correction product

`C_*=product_(k=2)^infinity E_k e^(1/k)`

converges absolutely.  Therefore

`product_(k=2)^K E_k ~ C_0/K`,

where

`C_0=e^(1-gamma) C_*`

and numerically

`C_0=1.5202566273133043...`.

Thus the positive rough-sector density is asymptotic to

`0.2533761045522174.../K`.

This identifies the multiplicative sieve as a genuine dimension-one sieve.
It also states the remaining obstruction precisely:

- every fixed cutoff is now closed;
- the main term remains positive and has the expected `1/K` decay;
- the Lang--Weil constants depend on the full product of dynatomic covers;
- no estimate uniform for `K` comparable with p is obtained.

The function-field crown requires exclusion of factors through
`floor(p/3)`.  Theorem FCDS.5 therefore advances the complete fixed-level
sieve but does not prove the crown.  The unsolved issue is uniformity in a
cutoff growing linearly with p, not any individual period or finite set of
periods.

## 8. Reproducibility and sources

`fixed_cutoff_dynatomic_constants.py` computes `r_k`, the exact small-period
E_k, the fixed-cutoff densities, and the limiting constant.

Primary monodromy sources:

- P. Morton, *On certain algebraic curves related to polynomial maps*,
  Compositio Math. 103 (1996), 319--350, Theorem D;
- P. Morton, corrigendum, Compositio Math. 147 (2011), 332--334;
- later explicit restatement in Bridy--Garton, *Dynamically distinguishing
  polynomials* (2017).

The dynatomic multiplicity and parabolic-cycle facts used in Section 3 are
standard consequences of the Morton--Silverman periodic-point multiplicity
theory and Fatou's critical-orbit theorem for polynomial basins.
