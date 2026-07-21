# Universal oriented-cubic parameterization

**Date:** 2026-07-21  
**Status:** exact algebraic parameterization proved.

## 1. Setup

Let `p >= 5` be prime and let `a` be nonzero in `F_p`.

Choose `b in F_p` such that

`q0(X) = X^3 + X + b`

is irreducible. Such a `b` always exists: the fixed-linear-coefficient count in `DISCRIMINANT_MASS.md` gives `(p - chi(-3))/3 > 0` choices.

Let `theta` be a root of `q0` in `F_(p^3)`, and put

`theta_0 = theta`, `theta_1 = theta^p`, `theta_2 = theta^(p^2)`.

Define the canonical Frobenius orientation

`W0 = (theta_1-theta_0)(theta_2-theta_0)(theta_2-theta_1)`.

Then

`W0^2 = -4 - 27 b^2`.

Because the coefficient of `X` in `q0` is nonzero, `theta` and `theta^p` are linearly independent over `F_p`. They form a basis of the trace-zero plane.

## 2. The universal plane and Frobenius action

For `(x,y) in F_p^2`, define

`alpha_(x,y) = x theta + y theta^p`.

Every trace-zero element occurs uniquely in this form. Since the only element of `F_p` with trace zero is zero, every nonzero `alpha_(x,y)` has degree three.

Using `theta + theta^p + theta^(p^2) = 0`, Frobenius acts on the coordinates by

`tau(x,y) = (-y, x-y)`.

The map `tau` has order three and has no nonzero fixed point. Thus the nonzero plane splits into `(p^2-1)/3` Frobenius orbits.

## 3. Explicit invariant forms

Put

`Q = x^2 - xy + y^2`,

`R = x^3 + y^3 - (3/2)xy(x+y)`,

`S = xy(x-y)`.

Let the minimal polynomial of `alpha_(x,y)` be

`X^3 + uX + v`,

and let

`V = (alpha^p-alpha)(alpha^(p^2)-alpha)(alpha^(p^2)-alpha^p)`.

Then

`u = Q`,

`v = bR + (W0/2)S`,

`V = W0 R - (27b/2)S`.

In particular,

`V^2 = -4u^3 - 27v^2`.

The three forms `u,v,V` are invariant under `tau`. The induced map from nonzero `tau`-orbits to oriented irreducible depressed cubics is a bijection.

### Proof

The conjugates of `alpha` are

`x theta_0 + y theta_1`,

`x theta_1 + y theta_2`,

`x theta_2 + y theta_0`.

Taking their second elementary symmetric function, negative product, and oriented Vandermonde gives the displayed formulas by direct expansion. Every irreducible depressed cubic has three trace-zero roots, forming one Frobenius orbit, so the orbit map is bijective. QED.

## 4. Frobenius interpolation on an oriented cubic

Let `X^3+uX+v` be an oriented irreducible depressed cubic with orientation `V`. On its roots, Frobenius is represented by

`P_(u,v,V)(X) = (3u/V)X^2 - ((V+9v)/(2V))X + 2u^2/V`.

That is, if `alpha` is a root with the chosen Frobenius orientation, then

`alpha^p = P_(u,v,V)(alpha)`.

This follows from quadratic interpolation on the three ordered roots. The coefficients are obtained by reducing the Vandermonde formulas with

`sum alpha_i = 0`, `sum_(i<j) alpha_i alpha_j = u`, `alpha_0 alpha_1 alpha_2 = -v`.

## 5. The unique compatible translate and coefficients

Translate the roots by `t in F_p`. The coefficient of `X^2` in

`(alpha+t)^p + a(alpha+t)^3`

vanishes exactly when

`t = -u/(aV)`.

For this translate, the unique member

`F_(a,c,d)(X) = X^p + aX^3 + cX + d`

divisible by the translated cubic has

`c = au + (V+9v)/(2V) - 3u^2/(aV^2)`,

`d = av - u^2/V + 3u/(2aV) + 9uv/(2aV^2) - 2u^3/(a^2 V^3)`.

Every denominator is nonzero because an irreducible cubic is separable and hence `V != 0`.

### Proof

Write the Frobenius interpolation polynomial after the shift by `t`. Its quadratic coefficient is

`3u/V + 3at`,

so the displayed `t` is forced. The remaining linear and constant coefficients are cancelled by `c` and `d`, giving the formulas above. QED.

## 6. Exact cubic-incidence formulas

Let `Phi_a(x,y)` be any property of the compatible member defined above that depends only on `(c,d)`, for example:

- local admissibility;
- the degree-p discriminant character;
- their product.

Then the corresponding cubic-factor incidence is exactly

`(1/3) sum_((x,y) != (0,0)) Phi_a(x,y)`.

The factor `1/3` is exact because each oriented irreducible depressed cubic is represented by its three Frobenius-conjugate roots.

This gives a fixed two-dimensional parameter space for both the unsigned and signed cubic sieve levels. No choice of square root of the cubic discriminant remains: the Frobenius orientation is built into the plane coordinates.

## 7. Shifted local-root equation

Let `z` be the local root variable after translating by `t`, so the original root is `t+z`. The local cubic vanishes exactly when

`G_a(u,v,V,z) = 0`,

where

`G_a = 2aV(z^3+uz+v) - 6uz^2 + (3V+9v)z - 4u^2`.

This polynomial is linear in the orientation `V` and has fixed degree after substituting the plane forms. It is the basic root-incidence surface for the cubic sieve level.

## 8. Scaling form

For a projective direction `(r:1)`, write `(x,y) = lambda(r,1)`. Then

`u = lambda^2 U`, `v = lambda^3 N`, `V = lambda^3 W`,

where `U,N,W` depend only on the direction. After dividing the shifted root equation by `lambda^2`, one obtains

`2a lambda W z^3 + 2a lambda^3 WUz + 2a lambda^4 WN - 6Uz^2 + 3lambda(W+3N)z - 4lambda^2 U^2 = 0`.

Thus every projective-direction fibre is a curve of bounded bidegree `(4,3)` in `(lambda,z)`. This is the direct route to a uniform `O(p^(3/2))` cubic-incidence theorem by a finite exceptional-fibre audit; a global surface audit may sharpen the error to `O(p)`.