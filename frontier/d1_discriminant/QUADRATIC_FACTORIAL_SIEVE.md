# Exact quadratic-factorial sieve in the d=1 cubic slice

**Date:** 2026-07-21  
**Status:** exact parametrisation and unconditional factorial-moment theorems proved, with fixed-degree Lang-Weil estimates and an explicit characteristic-zero genericity certificate.

## 1. Setup

Let `p >= 5` be prime and let `a` be nonzero in `F_p`. Put

`F_(c,d)(X) = X^p + a X^3 + c X + d`.

For a squarefree member let `nu_2(F)` be its number of monic irreducible quadratic factors. On the locally admissible family define

`Q_(a,j) = sum binom(nu_2(F),j)`

and

`Q_(a,j)^chi = sum chi(Disc F) binom(nu_2(F),j)`.

The sums are over coefficient pairs for which `aX^3+(c+1)X+d` is rootless.

The case `j=1` is the quadratic-incidence theorem already proved in `QUADRATIC_LOCAL_INCIDENCE.md` and `SIGNED_QUADRATIC_INCIDENCE.md`. This note closes `j=2,3` and hence removes quadratic factors by exact inclusion-exclusion.

## 2. The trace cubic and the bound nu_2 <= 3

An irreducible quadratic is written

`h_(s,n)(X) = X^2 - sX + n`.

The unique compatible coefficients satisfy

`c = 1 - a(s^2-n)`

and

`d = s(an-1)`.

Eliminating `n` gives the trace equation

`a s^3 - (2-c)s - d = 0`.

Therefore the traces of all irreducible quadratic factors of a fixed family member are roots of one cubic. Distinct irreducible quadratics have distinct traces, because `n` is determined by `s` and `c`.

### Theorem QFS.1

For every member of the slice,

`nu_2(F) <= 3`.

Consequently

`1_(nu_2(F)=0) = 1 - nu_2(F) + binom(nu_2(F),2) - binom(nu_2(F),3)`.

This turns quadratic sieving into a finite exact problem.

## 3. Pair parametrisation

Suppose two distinct irreducible quadratics have traces `s` and `t`. Equality of their compatible coefficient pairs gives

`a(s^2+st+t^2) = 2-c`.

Put

`u = s+2t`, `v = 2s+t`.

This change is invertible because `p != 3`. The two quadratic discriminants are

`u^2 - 4/a`

and

`v^2 - 4/a`.

The common coefficient pair is

`c(u,v) = 2 - a(u^2-uv+v^2)/3`

and

`d(u,v) = a(u-2v)(u+v)(2u-v)/27`.

Swapping the two factors swaps `u` and `v`, and the factors are distinct exactly when `u != v`.

Let

`E_a = {u in F_p : chi(u^2-4/a) = -1}`.

The standard quadratic-character sum gives

`|E_a| = n_a = (p-chi(a))/2`.

### Theorem QFS.2

The complete-slice second factorial moment is exactly

`sum_(c,d) binom(nu_2(F_(c,d)),2) = n_a(n_a-1)/2`.

## 4. Triple parametrisation

If three distinct quadratic factors occur, their traces are the three roots `s,t,r` of the trace cubic, so

`r = -s-t`.

With the same `u,v` as above, the third quadratic discriminant is

`(u-v)^2 - 4/a`.

The three roots are distinct exactly when

`u v (u-v) != 0`.

Each unordered triple has six ordered choices of `(s,t)`. Hence the complete-slice third factorial moment is exactly

`M_(a,3) = (1/6) # {(u,v):`
`  u v (u-v) != 0,`
`  chi(u^2-4/a) = chi(v^2-4/a) = chi((u-v)^2-4/a) = -1 }`.

Expanding the three exact nonsquare indicators gives fixed-degree two-variable character sums. Therefore

`M_(a,3) = p^2/48 + O(p^(3/2))`

with an absolute effective constant.

## 5. The attached local cubic

For either the pair or triple parametrisation define

`q = u^2-uv+v^2`

and

`r = (u-2v)(u+v)(2u-v)`.

The monic local cubic attached to the common coefficient pair is

`K_(u,v)(Z) = Z^3 + U_(u,v) Z + W_(u,v)`

with

`U_(u,v) = 3/a - q/3`

and

`W_(u,v) = r/27`.

Its discriminant is

`Delta_(u,v) = -4U_(u,v)^3 - 27W_(u,v)^2`.

Let `rho_(u,v)` be its number of roots in `F_p`, and let `delta_(u,v)` be one when `U=W=0` and zero otherwise. Then

`1_(K_(u,v) irreducible) = [2 + chi(Delta) - rho - delta]/3`.

This gives exact formulas for all four local factorial moments by inserting either the pair projector or the triple projector and dividing by two or six.

## 6. Genericity certificate

After scaling over the algebraic closure, every nonzero `a` is geometrically equivalent to `a=1`. At `a=1` the root-incidence surface is

`G(x,y,z) = 27z^3 + 9(9-x^2+xy-y^2)z`
`           + (x-2y)(x+y)(2x-y) = 0`.

The committed symbolic audit proves that `G` is geometrically irreducible and that `U=0`, `W=0` have no common curve.

For the character weights, restrict to the affine line `y=2x+1`. Up to nonzero constants, the required raw factors become

`A = (x-2)(x+2)`

`B = (2x-1)(2x+3)`

`C = (x-1)(x+3)`

`Delta = 4x^6+12x^5-23x^4-66x^3+49x^2+84x-76`

`Fplus = 4x^6+12x^5-23x^4-66x^3+46x^2+81x-67`

`Fminus = 12x^6+36x^5+3x^4-54x^3-30x^2+3x-1`

`c = 3x^2+3x-5`.

They are squarefree and pairwise coprime over the rationals. Thus every nonempty product needed after expanding the quadratic projectors, local-discriminant weight, and split degree-p discriminant weight is geometrically nonsquare.

The locus `c=0`, the zero loci introduced by the exact projectors, and the finitely many bad reductions contribute only `O(p)` and are absorbed in the final estimates.

## 7. Lang-Weil estimates

A geometrically nonsquare plane weight defines a geometrically irreducible fixed-degree double cover, so its complete character sum is `O(p^(3/2))`.

On the root surface `G=0`, the function-field extension over the parameter plane has odd degree three. A nonsquare plane weight cannot become a square in an odd-degree extension. Hence every nontrivial weighted root-incidence sum is also `O(p^(3/2))`.

The unweighted root surface has

`p^2 + O(p^(3/2))`

points. After applying the pair or triple projector, this gives one root on average, with the same error. The triple-root locus contributes `O(1)`.

All constants are absolute and effective.

## 8. Local factorial-moment theorems

### Theorem QFS.3

Uniformly for all `p >= 5` and `a != 0`,

`Q_(a,2) = n_a(n_a-1)/6 + O(p^(3/2))`

and

`Q_(a,2)^chi = O(p^(3/2))`.

In particular,

`Q_(a,2) = p^2/24 + O(p^(3/2))`.

### Theorem QFS.4

Uniformly for all `p >= 5` and `a != 0`,

`Q_(a,3) = p^2/144 + O(p^(3/2))`

and

`Q_(a,3)^chi = O(p^(3/2))`.

## 9. Exact removal of quadratic factors

Let

`N_(a,no2) = # {locally admissible F : nu_2(F)=0}`

and let

`M_(a,no2) = sum_(same family) chi(Disc F)`.

The exact finite inclusion-exclusion identity from Theorem QFS.1 gives

`N_(a,no2) = (p^2-1)/3 - Q_(a,1) + Q_(a,2) - Q_(a,3)`

and

`M_(a,no2) = M_a^loc - Q_(a,1)^chi + Q_(a,2)^chi - Q_(a,3)^chi`.

Using the completed first, second, and third moment estimates:

### Theorem QFS.5

`N_(a,no2) = 29 p^2/144 + O(p^(3/2))`

and

`M_(a,no2) = O(p^(3/2))`.

Therefore the positive- and negative-discriminant sectors with no quadratic factor satisfy

`N_(a,no2,+) = 29 p^2/288 + O(p^(3/2))`

and

`N_(a,no2,-) = 29 p^2/288 + O(p^(3/2))`.

This is the first complete multiplicative level of the parity-breaking sieve. It removes every possible quadratic factor, including multiple quadratic factors, rather than controlling only the first incidence moment.

## 10. Reproducibility

Run

`python frontier/d1_discriminant/quadratic_factorial_sieve_check.py`

and, with SymPy installed,

`python frontier/d1_discriminant/quadratic_factorial_symbolic_audit.py`.
