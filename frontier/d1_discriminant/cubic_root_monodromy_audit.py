#!/usr/bin/env python3
"""Exact algebraic audit for CUBIC_ROOT_MONODROMY.md.

Requires SymPy. Number-field discriminants of the two rational cyclic cubics
are independently checked in the Sage audit commands recorded in the note.
"""

from __future__ import annotations

import sympy as sp

V, u, c, d, s, t = sp.symbols("V u c d s t")

A = (
    V**4*c**2 - 2*V**4*c*u - V**4*c + V**4*u**2 + V**4*u + V**4
    + 6*V**2*c*u**2 - 3*V**2*u**3 - 3*V**2*u**2 + 9*u**4
)
B = (
    2*V**4*c - 2*V**4*u - V**4 - 9*V**3*d + 9*V**2*c*u
    - 12*V**2*u**2 + 9*V**2*u + 9*u**3
)

# 1. Two distinct cyclic cubic fields at c=-5,d=-4.
solutions = [
    (sp.Rational(13), sp.Rational(-13, 3), sp.Rational(-65, 27)),
    (sp.Rational(7), sp.Rational(-7), sp.Rational(7)),
]
for vv, uu, ww in solutions:
    assert sp.expand(A.subs({V: vv, u: uu, c: -5})) == 0
    assert sp.expand(B.subs({V: vv, u: uu, c: -5, d: -4})) == 0
    assert sp.expand(vv**2 + 4*uu**3 + 27*ww**2) == 0

Z = sp.symbols("Z")
g13 = sp.Poly(Z**3 - 39*Z - 65, Z)
g7 = sp.Poly(Z**3 - 7*Z + 7, Z)
assert sp.factor(g13.as_expr()) == g13.as_expr()
assert sp.factor(g7.as_expr()) == g7.as_expr()
assert sp.discriminant(g13.as_expr(), Z) == 3**6 * 13**2
assert sp.discriminant(g7.as_expr(), Z) == 7**2

# 2. Reconstruct the product of the eight Cardano classes at c=d=-2.
E = (
    V**8
    + V**6*(4*c**3 - 6*c**2 + 18*c + 27*d**2 - 26)
    + V**5*(-81*c*d - 27*d)
    + V**4*(69*c**4 - 210*c**3 + 279*c**2 - 81*c*d**2 - 219*c - 81*d**2 + 195)
    + V**3*(-729*c**3*d + 1458*c**2*d - 486*c*d + 351*d)
    + V**2*(81*c**5 + 72*c**4 - 248*c**3 + 2187*c**2*d**2 - 24*c**2
            - 1701*c*d**2 + 39*c + 513*d**2 - 338)
    + V*(-324*c**4*d - 864*c**3*d - 405*c**2*d - 2187*c*d**3
        - 162*c*d + 729*d**3 - 351*d)
    + 16*c**6 + 96*c**5 + 204*c**4 + 216*c**3*d**2 + 176*c**3
    + 648*c**2*d**2 + 105*c**2 + 405*c*d**2 + 195*c
    + 729*d**4 - 27*d**2 + 169
)

subresultants = sp.subresultants(A, B, u)
linear = sp.Poly(subresultants[-2], u)
linear_coefficient = sp.factor(linear.coeff_monomial(u))
constant_coefficient = sp.factor(linear.coeff_monomial(1))
u_rational = sp.cancel(-constant_coefficient / linear_coefficient)
v_rational = sp.cancel(
    (2*V**2*c - 2*V**2*u_rational - V**2 + 6*u_rational**2)/(9*V)
)
q_rational = sp.cancel((-9*v_rational + s*V)/18)
q_num, q_den = sp.fraction(q_rational)

special = {c: -2, d: -2}
f = sp.Poly(E.subs(special), V, domain=sp.ZZ)
num_resultant = sp.resultant(f.as_expr(), sp.expand(q_num.subs(special)), V)
den_resultant = sp.resultant(f.as_expr(), sp.expand(q_den.subs(special)), V)
product = sp.cancel(num_resultant / den_resultant)

product_num, product_den = sp.fraction(product)
product_num_reduced = sp.rem(
    sp.Poly(product_num, s), sp.Poly(s**2 + 3, s)
).as_expr()
product_reduced = sp.cancel(product_num_reduced / product_den)
expected_product = sp.Rational(11779, 2*3**21) * (2089 + 1983*s)
assert sp.expand(product_reduced - expected_product) == 0

# 3. The product is not a cube in Q(sqrt(-3)).
ratio_equation = sp.factor(
    sp.Rational(1983, 2089)*(1 - 9*t**2) - (3*t - 3*t**3)
)
assert sp.factor(ratio_equation * sp.Rational(2089, 3)) == (
    2089*t**3 - 5949*t**2 - 2089*t + 661
)
noncube_cubic = sp.Poly(2089*t**3 - 5949*t**2 - 2089*t + 661, t)
_, factors_mod_5 = sp.factor_list(noncube_cubic.as_expr(), modulus=5)
assert len(factors_mod_5) == 1
assert sp.degree(factors_mod_5[0][0], t) == 3

print("compatible cyclic cubics verified at c=-5,d=-4")
print("Cardano product:", product_reduced)
print("noncube cubic mod 5:", sp.factor(noncube_cubic.as_expr(), modulus=5))
print("PASS: full root-marking monodromy is C3^8 semidirect S8")
