# Explicit Moore ratio for the cubic coefficient

**Date:** 2026-07-21  
**Status:** exact algebraic reduction proved.

## 1. Root-incidence formulation

Let `K=F_(p^p)` and let `x in K minus F_p`. Put

`delta=x^p-x`.

A cubic-slice relation is equivalent to

`delta=A+C x+lambda x^3`,

with `A,C,lambda in F_p` and `lambda!=0`. The corresponding polynomial coefficients are

`a=-lambda`, `c=-C-1`, `d=-A`.

Because x has degree p, the elements `1,x,x^3` are linearly independent over `F_p`.

## 2. Two three-by-three Moore determinants

Use the first three Frobenius rows. Define

`D0=det [[1,x,x^3],`
`        [1,x^p,x^(3p)],`
`        [1,x^(p^2),x^(3p^2)]]`,

and let `Dlambda` be the determinant obtained by replacing the third column by

`delta,delta^p,delta^(p^2)`.

Cramer's rule gives

`lambda=Dlambda/D0`.

Write

`delta0=delta`, `delta1=delta^p`, `delta2=delta^(p^2)`.

Subtracting the first row from the next two gives the exact factorizations

`boxed(D0=delta0 delta1 (delta0+delta1)`
`             (3x+2delta0+delta1)),`

`boxed(Dlambda=delta0 delta2-delta1^2.)`

The factors in D0 are nonzero because `1,x,x^3` are F_p-linearly independent.

## 3. Hilbert-90 coordinates

Put

`t=delta^(p-1)=delta^p/delta`,

`y=x/delta`.

Then

`y^p=(y+1)/t`.

Also

`delta^(p^2)=t^p delta^p=t^p t delta`.

Substitution in the determinant ratio yields

### Theorem MCC.1

`boxed(lambda(x)=delta^(-2)`
`       (t^p-t)/((1+t)(3y+2+t)).)`

This is the coefficient of `x^3` in the unique relation determined by the first three Frobenius conjugates.

## 4. One scalar Frobenius criterion

Let `(A,C,lambda)` be the coefficient triple obtained from the first three Frobenius equations. Its Frobenius transform solves the shifted equations with rows 1,2,3.

The original triple and its Frobenius transform already agree on rows 1 and 2. If `lambda^p=lambda`, their difference has third coordinate zero and satisfies

`Delta A+Delta C x^p=0`,

`Delta A+Delta C x^(p^2)=0`.

Since `x^p!=x^(p^2)`, this forces `Delta A=Delta C=0`. Thus all three coefficients lie in F_p and the fourth Moore row holds.

Conversely, an F_p-linear relation clearly has `lambda^p=lambda`.

Therefore:

### Theorem MCC.2

For `x notin F_p`,

`boxed(x^p in span_(F_p){1,x,x^3}`
`       iff lambda(x)^p=lambda(x).)`

The cubic Fortune slice corresponds to the additional condition `lambda(x)!=0`.

## 5. Square-class character

Let `n=(p-1)/2` and put

`R(t,y)=(t^p-t)/((1+t)(3y+2+t)).`

On the incidence locus, `lambda=delta^(-2)R` lies in F_p. Hence

`lambda^n=delta^(-(p-1))R^n=t^(-1)R^n`.

Thus

`boxed(chi(a)=chi(-1)t^(-1)`
`       ((t^p-t)/((1+t)(3y+2+t)))^n.)`

This supplies an explicit rational character for the two square-class modes.

## 6. Strategic consequence

The four-column Moore determinant and the simultaneous recovery of a,c,d reduce to one scalar Frobenius equation for lambda. This does not yet count its solutions, but it gives a substantially smaller target for:

1. a Hilbert-90 parameterization of the incidence surface;
2. character-sum analysis of the square-class difference;
3. a rational correspondence or transfer map in the variables `(t,y)`;
4. direct comparison with the two Cartier-cofactor modes.
