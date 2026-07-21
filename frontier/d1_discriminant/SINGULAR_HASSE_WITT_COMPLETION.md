# Singular completion of the higher Hasse--Witt indicator

**Date:** 2026-07-21  
**Status:** exact theorem for every member with nonzero constant term, conditional only on the standard Beukers--Vlasenko unit-root comparison on the squarefree locus.

## 1. Setup

Let

`F(X)=X^p+aX^3+cX+d`,

where `p>=5`, `a!=0`, and `d!=0`. For `m>=1` let

`Beta_m(F)_(u,v)=[X^(mu-v)]F(X)^(m-1)`, `1<=u,v<=p-1`.

Put `B=Beta_p(F)` and `B2=Beta_(p^2)(F)`, using canonical integer lifts modulo `p^2`.

The higher Hasse--Witt congruence is unchanged if the published index convention `mv-u` is transposed to `mu-v`. In particular,

`B2 = B^2 mod p`.

## 2. Characteristic polynomial on the singular locus

Let

`A=F_p[X]/(F)`

and let `Fr:A->A` be p-power Frobenius. Because `d!=0`, the zero scheme lies in the one-dimensional torus. On the squarefree locus, the ordinary Hasse--Witt matrix `B mod p` represents Cartier/Frobenius on the reduced zero-dimensional torus crystal. Consequently its characteristic polynomial is that of Frobenius on `A/F_p` (up to transpose or inverse convention, which does not change the roots 0 and 1).

Both characteristic polynomials are polynomial functions of the coefficients of the universal monic degree-p polynomial with invertible constant term:

- the entries of `B` are explicit coefficients of `F^(p-1)`;
- the entries of Frobenius in the monomial quotient basis are obtained by monic polynomial reduction and are polynomial in the coefficients.

The squarefree locus is Zariski dense. Hence the characteristic-polynomial identity extends to every polynomial with nonzero constant term, including singular members.

## 3. The simultaneous zero and one eigenvalues

Write

`F=product_i h_i^(e_i)`

with distinct monic irreducibles `h_i`, and let `r` be the number of distinct factors.

If F is singular, its nilradical is nonzero. Frobenius kills a nonzero nilpotent direction after iteration, so zero is an eigenvalue of Frobenius on A, and hence of `B mod p`.

On the reduced quotient

`A_red = product_i F_(p^(deg h_i))`,

Frobenius has one fixed copy of `F_p` for each distinct factor. After quotienting the global constants, the 1-eigenspace has dimension `r-1`.

A singular degree-p polynomial with only one distinct factor would have to be `(X-r)^p`, because p is prime. That is impossible in the present slice since `a!=0`. Therefore `r>=2`, and 1 is also an eigenvalue of `B mod p`.

The 0- and 1-eigenspaces are independent. Thus

`B(I-B) mod p`

has kernel dimension at least two.

## 4. Divisibility by p squared

The universal first congruence gives

`B-B2 = B(I-B) mod p`.

Therefore the reduction of the `(p-1)x(p-1)` matrix `B-B2` has corank at least two on every singular member with `d!=0`. Any lift of a matrix of corank at least two has determinant divisible by `p^2` (equivalently, at least two Smith invariant factors are divisible by p). Hence

`det(B-B2)=0 mod p^2`

for every singular member with nonzero d.

## 5. Completed indicator

For squarefree members with `d!=0`, the Beukers--Vlasenko unit-root comparison gives

`det(B-B2)/p = 1_(F irreducible) mod p`.

For singular members, the preceding theorem gives zero. Therefore:

### Theorem SHW.1

For every prime `p>=5`, every `a!=0`, every `c in F_p`, and every `d in F_p^*`,

`det(Beta_p(F)-Beta_(p^2)(F))/p = 1_(F irreducible) mod p`.

No squarefreeness or local-admissibility hypothesis remains.

Since an irreducible member necessarily has `d!=0`, define

`K_a(c,d)=det(Beta_p-Beta_(p^2))/p mod p`.

Then exactly

`N_a(p)=sum_(c in F_p, d in F_p^*) K_a(c,d) mod p`.

This is the useful singular completion: the cubic rootlessness projector is removed, while the omitted `d=0` line contains no irreducible members.

## 6. References and convention audit

The matrix congruence and unit-root approximation are the standard results in:

- M. Vlasenko, *Higher Hasse--Witt matrices*, Indagationes Mathematicae 29 (2018), 1411--1424;
- F. Beukers and M. Vlasenko, *Dwork Crystals I*, IMRN 2021;
- F. Beukers and M. Vlasenko, *Dwork Crystals II*, IMRN 2021.

Those papers define entries using the transposed indexing `mv-u`. The present convention `mu-v` transposes every matrix and leaves determinants, characteristic polynomials, coranks, and the indicator unchanged.
