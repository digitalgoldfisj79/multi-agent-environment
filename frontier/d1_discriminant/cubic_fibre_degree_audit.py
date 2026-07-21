#!/usr/bin/env python3
"""Exact symbolic audit for the cubic-factor fibre-degree theorem.

Requires SymPy. It verifies the v elimination, the two reduced equations,
the degree-eight orientation resultant, and finite-field fibre bounds.
"""

from __future__ import annotations

import sympy as sp

u, v, V, c, d = sp.symbols("u v V c d")

orientation = V**2 + 4*u**3 + 27*v**2
ceq = 2*V**2*c - (2*u*V**2 + V*(V + 9*v) - 6*u**2)
deq = 2*V**3*d - (
    2*v*V**3 - 2*u**2*V**2 + 3*u*V**2 + 9*u*v*V - 4*u**3
)

v_formula = sp.factor(sp.solve(ceq, v)[0])
assert v_formula == (2*V**2*c - 2*V**2*u - V**2 + 6*u**2)/(9*V)

A = sp.factor(sp.together(orientation.subs(v, v_formula)) * 3*V**2 / 4)
B = sp.factor(-9*sp.together(deq.subs(v, v_formula)) / 2)

A_expected = (
    V**4*c**2 - 2*V**4*c*u - V**4*c + V**4*u**2 + V**4*u + V**4
    + 6*V**2*c*u**2 - 3*V**2*u**3 - 3*V**2*u**2 + 9*u**4
)
B_expected = (
    2*V**4*c - 2*V**4*u - V**4 - 9*V**3*d + 9*V**2*c*u
    - 12*V**2*u**2 + 9*V**2*u + 9*u**3
)
assert sp.expand(A - A_expected) == 0
assert sp.expand(B - B_expected) == 0

resultant = sp.factor(sp.resultant(A, B, u))
quotient = sp.cancel(resultant / (6561*V**12))
num, den = sp.fraction(quotient)
assert den == 1
E = sp.factor(num)
assert sp.Poly(E, V).degree() == 8
assert sp.Poly(E, V).LC() == 1

# Generic specialisation has eight nonzero orientation roots over C,
# counted with multiplicity, and a linear first subresultant in u.
E23 = sp.Poly(E.subs({c: 2, d: 3}), V)
assert E23.degree() == 8
assert sp.gcd(E23, E23.diff()).degree() == 0
subres = sp.subresultants(A.subs({c: 2}), B.subs({c: 2, d: 3}), u)
assert any(sp.Poly(s, u).degree() == 1 for s in subres)


def inv(x: int, p: int) -> int:
    return pow(x % p, p - 2, p)


def eval_a(uu: int, vv: int, cv: int, p: int) -> int:
    return (
        vv**4*cv**2 - 2*vv**4*cv*uu - vv**4*cv + vv**4*uu**2
        + vv**4*uu + vv**4 + 6*vv**2*cv*uu**2 - 3*vv**2*uu**3
        - 3*vv**2*uu**2 + 9*uu**4
    ) % p


def eval_b(uu: int, vv: int, cv: int, dv: int, p: int) -> int:
    return (
        2*vv**4*cv - 2*vv**4*uu - vv**4 - 9*vv**3*dv
        + 9*vv**2*cv*uu - 12*vv**2*uu**2 + 9*vv**2*uu + 9*uu**3
    ) % p


def count_solutions(p: int, cv: int, dv: int) -> int:
    count = 0
    for vv in range(1, p):
        for uu in range(p):
            if eval_a(uu, vv, cv, p) == 0 and eval_b(uu, vv, cv, dv, p) == 0:
                # v is uniquely recovered because 9V is invertible.
                _ = (
                    (2*vv*vv*cv - 2*vv*vv*uu - vv*vv + 6*uu*uu)
                    * inv(9*vv, p)
                ) % p
                count += 1
    return count


for p in (5, 7, 11, 13, 17, 19):
    maximum = 0
    argmax = None
    for cv in range(p):
        for dv in range(p):
            value = count_solutions(p, cv, dv)
            if value > maximum:
                maximum = value
                argmax = (cv, dv)
    assert maximum <= 24
    print(f"p={p}: max algebraic compatible triples={maximum} at {argmax}")

print("PASS: cubic fibre degree audit")
print("orientation eliminant degree:", sp.Poly(E, V).degree())
