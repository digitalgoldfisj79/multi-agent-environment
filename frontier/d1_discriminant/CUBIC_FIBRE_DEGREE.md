# Uniform degree bound for the cubic-factor map

**Date:** 2026-07-21  
**Status:** exact elimination theorem proved.

## 1. Setup

Let p >= 5, let a be nonzero in F_p, and put

`F_(a,c,d)(X) = X^p + aX^3 + cX + d`.

For an oriented irreducible depressed cubic

`h(X) = X^3 + uX + v`

write

`V^2 = -4u^3 - 27v^2`,

where V is the canonical Frobenius orientation. The unique compatible translate and coefficient pair are given in `ORIENTED_CUBIC_PARAMETERIZATION.md`.

Over the algebraic closure, scale X so that a=1. This does not change the fibre cardinality of the compatible-cubic map.

The coefficient formulas are

`c = u + (V+9v)/(2V) - 3u^2/V^2`,

`d = v - u^2/V + 3u/(2V) + 9uv/(2V^2) - 2u^3/V^3`.

Every compatible irreducible cubic has V nonzero.

## 2. Eliminate v

Clearing the c equation gives

`v = [2V^2 c - 2V^2 u - V^2 + 6u^2]/(9V)`.

Substitution into the orientation relation and the d equation gives two polynomial equations in u and V:

`A_(c)(u,V) = 0`,

`B_(c,d)(u,V) = 0`,

where

`A = V^4 c^2 - 2V^4cu - V^4c + V^4u^2 + V^4u + V^4`
`    + 6V^2cu^2 - 3V^2u^3 - 3V^2u^2 + 9u^4`,

and

`B = 2V^4c - 2V^4u - V^4 - 9V^3d + 9V^2cu`
`    - 12V^2u^2 + 9V^2u + 9u^3`.

The polynomial B has degree exactly three in u in every characteristic p >= 5.

## 3. Degree-eight orientation eliminant

A direct resultant calculation gives

`Res_u(A,B) = 3^8 V^12 E_(c,d)(V)`,

where E is monic of degree eight:

`E = V^8`
`  + V^6(4c^3 - 6c^2 + 18c + 27d^2 - 26)`
`  + V^5(-81cd - 27d)`
`  + V^4(69c^4 - 210c^3 + 279c^2 - 81cd^2 - 219c - 81d^2 + 195)`
`  + V^3(-729c^3d + 1458c^2d - 486cd + 351d)`
`  + V^2(81c^5 + 72c^4 - 248c^3 + 2187c^2d^2 - 24c^2`
`         - 1701cd^2 + 39c + 513d^2 - 338)`
`  + V(-324c^4d - 864c^3d - 405c^2d - 2187cd^3 - 162cd`
`       + 729d^3 - 351d)`
`  + 16c^6 + 96c^5 + 204c^4 + 216c^3d^2 + 176c^3`
`    + 648c^2d^2 + 105c^2 + 405cd^2 + 195c + 729d^4 - 27d^2 + 169`.

The leading coefficient is one, so this eliminant never vanishes identically for a specialised coefficient pair.

## 4. Uniform multiplicity bound

Fix c,d. Every compatible oriented cubic gives a nonzero root V of E. There are at most eight possible values of V. For each such V, the equation B=0 has at most three values of u, and v is then uniquely determined by the displayed formula.

Therefore the compatible-cubic fibre has cardinality at most 24 over the algebraic closure.

### Theorem CFD.1

For every prime p >= 5, every nonzero a in F_p, and every c,d in F_p,

`nu_3(F_(a,c,d)) <= 24`.

Here nu_3 denotes the number of distinct monic irreducible cubic factors.

Consequently

`1_(nu_3=0) = sum_(j=0)^24 (-1)^j binom(nu_3,j)`

exactly. Cubic-factor deletion is therefore a finite factorial-moment problem; no tail through order p/3 occurs at degree three.

## 5. Generic degree

For generic c,d the first subresultant is linear in u and E is squarefree, so the rational map has generic degree eight. The theorem above deliberately uses the uniform bound 24, which remains valid on every exceptional fibre without a separate case ledger.

## 6. Verification

The companion script `cubic_fibre_degree_audit.py` reconstructs A and B, verifies the displayed resultant exactly over the integers, checks that E is monic of degree eight, and tests the fibre bound over a range of finite fields.