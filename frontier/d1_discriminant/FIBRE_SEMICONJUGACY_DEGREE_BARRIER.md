# Linear degree barrier for fibre-specific Artin--Schreier semiconjugacy

**Date:** 2026-07-21  
**Status:** exact obstruction theorem proved.

## 1. Setup

Let

`M_p(Z)=Z^p-Z-1`

and let

`g(Y)=-aY^3-cY-d`, with `a!=0`.

A fibre-specific constructive witness is a rational function

`R(Z)=A(Z)/B(Z) in F_p(Z)`

such that B is invertible modulo `M_p` and

`R(Z+1)=g(R(Z)) mod M_p(Z)`.

This is exactly the Artin--Schreier semiconjugacy programme: if z is a root of `M_p`, then `alpha=R(z)` satisfies `alpha^p=g(alpha)`. If R(z) has degree p, the corresponding polynomial `X^p-g(X)` is irreducible.

## 2. Cleared numerator

Choose coprime A,B with

`max(deg A,deg B)=m`.

Clearing denominators gives the polynomial

`N(Z)=A(Z+1)B(Z)^3`
`     +a B(Z+1)A(Z)^3`
`     +c B(Z+1)A(Z)B(Z)^2`
`     +d B(Z+1)B(Z)^3`.

The fibre congruence is equivalent to

`M_p divides N`.

Every term in N has degree at most `4m`. Therefore

`deg N<=4m`.

## 3. Barrier theorem

### Theorem FSD.1

If a fibre-specific rational semiconjugacy exists for a cubic g with `a!=0`, then

`boxed(m>=p/4.)`

More precisely, if `4m<p`, then no such semiconjugacy exists.

### Proof

If `4m<p`, divisibility of N by the degree-p polynomial `M_p` forces `N=0` identically. Thus

`R(Z+1)=g(R(Z))`

as an identity in the rational function field `F_p(Z)`.

But translation `Z->Z+1` has finite order p. The subfield `F_p(R)` is then stable under translation, and the induced self-map is an automorphism of the rational function field `F_p(R)`. Every such automorphism is Möbius. Hence g must have rational degree one.

This contradicts `deg g=3`, since `a!=0`. QED.

## 4. Consequences

The obstruction applies to every rational ansatz, not merely:

- monomials;
- sparse polynomials;
- two-term binomial-basis expressions;
- cubic polynomial images.

Any successful Artin--Schreier construction must have complexity growing linearly with p. In particular, no fixed-degree rational template can prove the d=1 crown for infinitely many primes.

The computational failures are consistent with the sharp mechanism:

- monomial images produced only an accidental p=5 case and none through p=101;
- two-term translation-binomial images produced only p=5 cases and none through p=43;
- every normalized cubic image `Z^3+qZ+r` failed for p>=7 through p=101.

These experiments are no longer the basis for rejecting the route; Theorem FSD.1 supplies the rigorous reason.

## 5. Strategic conclusion

The constructive semiconjugacy programme remains logically possible, but it is not a bounded-template route. It requires at least `ceil(p/4)` rational degree, comparable to the dense interpolants already observed. The ordinary Cartier cofactor and translation-weight architectures are therefore the more compressed crown fronts.
