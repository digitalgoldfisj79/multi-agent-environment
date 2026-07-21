#!/usr/bin/env python3
"""Exact audit for the generic S8 monodromy theorem.

Requires SymPy. It verifies:
- the degree-eight specialization at c=d=-2;
- good-prime factorisations with cycle types 8, 7+1, and 2+1^6;
- the non-square generic discriminant via the d=0 specialization.
"""

from __future__ import annotations

import sympy as sp

V, c, d = sp.symbols("V c d")

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

f = sp.Poly(E.subs({c: -2, d: -2}), V, domain=sp.ZZ)
expected = sp.Poly(
    V**8 - 10*V**6 - 270*V**5 + 4857*V**4 - 25974*V**3
    + 50684*V**2 - 40986*V + 11779,
    V,
    domain=sp.ZZ,
)
assert f == expected

disc = sp.discriminant(f.as_expr(), V)

expected_types = {
    5: (8,),
    13: (7, 1),
    293: (2, 1, 1, 1, 1, 1, 1),
}

for prime, expected_type in expected_types.items():
    assert disc % prime != 0
    _, factors = sp.factor_list(f.as_expr(), modulus=prime)
    cycle_type = tuple(sorted(
        [sp.degree(g, V) for g, exponent in factors for _ in range(exponent)],
        reverse=True,
    ))
    assert cycle_type == expected_type, (prime, cycle_type)
    print(f"p={prime}: discriminant residue={disc % prime}, cycle type={cycle_type}")
    print(sp.factor(f.as_expr(), modulus=prime))

# A nonsquare d=0 discriminant proves that the geometric group is not A8.
disc0 = sp.factor(sp.discriminant(E.subs(d, 0), V))
_, factor_meta = sp.factor_list(disc0)
assert any(sp.expand(g) == c**2 - c + 1 and exponent == 1 for g, exponent in factor_meta)

print("d=0 discriminant factors:")
for factor, exponent in factor_meta:
    print(" degree", sp.degree(factor, c), "exponent", exponent, ":", factor)

print("PASS: generic cubic orientation monodromy is S8")
