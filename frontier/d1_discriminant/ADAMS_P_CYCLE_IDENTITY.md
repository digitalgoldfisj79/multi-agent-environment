# The p-cycle indicator as a two-term Adams trace

**Date:** 2026-07-22  
**Status:** exact class-function and fibrewise trace identities proved; geometric exploitation of the characteristic-p Adams operation remains open.

## 1. Permutation identity

Let sigma be a permutation of p letters, with p prime. Let

`Fix(sigma^n)`

be the number of fixed letters of its n-th power.

A letter is fixed by `sigma^p` exactly when its cycle length divides p. Since p is prime, these cycle lengths are 1 and p. Therefore

`Fix(sigma^p)-Fix(sigma)`

is p times the number of p-cycles in sigma.

A permutation of p letters contains at most one p-cycle, and contains one exactly when it is itself a p-cycle. Hence:

### Theorem API.1

`boxed(Fix(sigma^p)-Fix(sigma)`
`      =p*1_(sigma is a p-cycle).)`

## 2. Adams-operation form

Let `Perm_p` be the p-dimensional permutation representation. The p-th Adams operation has character

`Tr(sigma|psi^p(Perm_p))=Tr(sigma^p|Perm_p)=Fix(sigma^p)`.

The p-cycle virtual character

`Lambda_p=sum_(i=0)^(p-1)(-1)^i exterior^i(Perm_p-1)`

has character p on p-cycles and zero elsewhere. Therefore:

### Theorem API.2

`boxed(Lambda_p=psi^p(Perm_p)-Perm_p)`

as a class function, equivalently in the rational lambda-ring of `S_p` representations.

This agrees with the cyclic-induction identity

`Lambda_p=Ind_(C_p)^(S_p)(1-psi)`.

## 3. Polynomial-fibre identity

Let F be a degree-p polynomial over `F_p`, excluding the pure inseparable one-factor case. Let `V_F` be the permutation representation on its distinct geometric roots and let Frobenius be sigma.

Then

`Tr(sigma^p|V_F)=# roots of F in F_(p^p)`,

`Tr(sigma|V_F)=# roots of F in F_p`.

Theorem API.1 gives

`boxed(p*1_(F irreducible)`
` =#Z(F)(F_(p^p)) - #Z(F)(F_p).)`

This is the master root-incidence formula in its shortest pointwise form.

## 4. Family trace on the normalized root surface

For the split universal family

`qX^p+X^3-3X+v`, `q!=0`,

summing Theorem API.1 over `(q,v) in F_p^* x F_p` gives

`p S_+^0`
` =# {(x,q,v): x in F_(p^p), q,v in F_p,`
`      qx^p+x^3-3x+v=0}`
`  -p(p-1).`

The second term is the contribution of `x in F_p`.

The total root space itself is rational: after solving for v it is the `(x,q)` plane. The difficulty is the mixed fixed-locus condition `x in F_(p^p)` while `(q,v)` remain in F_p`.

## 5. Strategic consequence

The full-cycle indicator now has three equivalent exact compressions:

1. Cartier/Frobenius cofactor;
2. cyclic induction from the rank-one Artin--Schreier character;
3. the two-term Adams trace `psi^p(Perm)-Perm`.

The Adams form is the only one involving the rational root surface directly. A successful characteristic-p Adams--Riemann--Roch or Frobenius-correspondence calculation could bound the universal q-sums without constructing the factorial-degree cyclic quotient.

The current obstacle is that the p-th Adams operation coincides with the characteristic and is not represented by an ordinary fixed-rank l-adic sheaf. It must be handled as a Frobenius correspondence or via cyclic power operations.
