# Frobenius-aligned dynamical zeta target

**Date:** 2026-07-21  
**Status:** exact compression identity; family-average theorem open.

## 1. Why the ordinary Artin--Mazur zeta is not enough

Let

`F(X)=X^p+aX^3+cX+d`

and

`g(X)=-aX^3-cX-d`.

On every root alpha of F,

`alpha^p=g(alpha)`.

An irreducible factor of degree k corresponds to a k-cycle on which arithmetic Frobenius acts as the one-step dynamical map g.

The ordinary Artin--Mazur zeta function of g counts every dynamical cycle of g. It does not impose the Frobenius-alignment condition and therefore contains cycles that do not arise as factors of F.

The crown requires a twisted, Frobenius-aligned object.

## 2. Exact cycle polynomial

Let

`A=F_p[X]/(F)`

and let `Phi(z)=z^p`. On A, the relation `X^p=g(X)` identifies Phi with the substitution operator induced by g.

Assume F is squarefree. If

`F=product_k product_(i=1)^(nu_k) h_(k,i)`

is its irreducible factorisation, then on the geometric roots Phi is a permutation with `nu_k` cycles of length k.

Define

`Z_F(T)=det(1-T Phi | A)`.

### Theorem TZ.1

`Z_F(T)=product_(k>=1) (1-T^k)^(nu_k(F))`.

This identity is exact and packages the complete factor-degree partition of F.

In particular:

- linear admissibility is the absence of a `(1-T)` factor;
- excluding factors through K removes all factors `(1-T^k)` for `k<=K`;
- F is irreducible of degree p exactly when
  `Z_F(T)=1-T^p`.

## 3. Trace expansion

The logarithmic derivative gives

`-T Z_F'(T)/Z_F(T)=sum_(m>=1) Tr(Phi^m | A) T^m`.

For squarefree F,

`Tr(Phi^m | A)=# {geometric roots alpha of F : alpha^(p^m)=alpha}`

and hence

`Tr(Phi^m | A)=sum_(k|m) k nu_k(F)`.

Equivalently,

`Tr(Phi^m | A)=deg gcd(F,X^(p^m)-X)`.

Using `Phi=g` on the root algebra, the same trace counts roots satisfying the aligned relation

`g^m(alpha)=alpha`

inside the root set of F.

## 4. Relation to the existing two architectures

### Dynatomic sieve

The dynatomic programme studies the individual cycle factors `(1-T^k)` and their mixed factorial moments. It expands the product representation of `Z_F` degree by degree.

### Frobenius determinant

The Berlekamp matrix is `Phi-I`. Its selected cofactor

`J_a(c,d)=3a 1_irreducible`

is a connectedness/full-cycle functional extracted from the same operator at `T=1`.

Thus the two programmes are not merely analogous. They are two expansions of the same exact cycle polynomial.

## 5. The genuine compression problem

For each coefficient pair, the full partition is compressed by one degree-p polynomial `Z_F(T)`. The crown problem is to average or extract the full-cycle part across the two-dimensional coefficient family without expanding all mixed factorial moments.

Acceptable crown-level targets include:

1. a family trace formula for `Z_F(T)` or its exterior-power coefficients;
2. a transfer operator whose determinant is `Z_F(T)` and whose family average has bounded complexity;
3. a Dwork or p-adic cohomological formula for the selected cofactor at `T=1`;
4. a recurrence for the two square-class modes of the determinant top coefficient;
5. a uniform estimate for the truncated Euler product through `K=floor(p/3)` derived directly from `Z_F`, not from a factorial table.

## 6. Warning on uniformity

For every fixed finite set of periods, Morton-type monodromy and Lang--Weil control the corresponding finite collection of factors of `Z_F`.

Nothing currently controls the full initial segment through `p/3`. The obstruction is not merely accumulation of numerical errors; it is the absence of a bounded-complexity description of the growing collection of Frobenius-aligned cycle conditions.

The ordinary Artin--Mazur zeta of g does not remove this obstruction. The required object is the Frobenius-aligned cycle polynomial above, or an equivalent trace/determinant representation of the correspondence `Frobenius = g`.
