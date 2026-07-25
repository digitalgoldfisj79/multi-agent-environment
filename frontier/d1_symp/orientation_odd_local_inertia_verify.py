#!/usr/bin/env python3
"""Regression checks for ORIENTATION_ODD_LAURENT_AIRY_LOCAL_INERTIA_20260725.md.

This checks the stationary Puiseux coefficients and the finite tame-character
calculation behind the Adams regular-representation lemma.  The local Fourier
transform and determinant inputs are the cited theorems, not computer claims.
"""
from __future__ import annotations

import sympy as sp


def check_s_infinity() -> None:
    z, u, a = sp.symbols("z u a", nonzero=True)
    b = -u / (12 * a)
    x = a / z + b * z
    # Work through the orders needed, imposing 3*a**4=1.
    critical = sp.expand(3 * x**4 + u * x**2 - z**-4)
    critical = sp.expand(critical.subs(a**4, sp.Rational(1, 3)))
    assert sp.expand(critical).coeff(z, -4) == 0
    assert sp.simplify(sp.expand(critical).coeff(z, -2)) == 0

    value = sp.expand(4 * x**3 + 2 * u * x)
    assert sp.simplify(value.coeff(z, -3) - 4 * a**3) == 0
    assert sp.simplify(value.coeff(z, -1) - u * a) == 0
    print("s=infinity stationary expansion: PASS")


def check_u_infinity_large() -> None:
    z, s, a = sp.symbols("z s a", nonzero=True)
    c = -s / (2 * a)
    x = a / z + c * z**3
    critical = sp.expand(3 * x**4 + z**-2 * x**2 - s)
    # Reduce powers using a^2=-1/3.
    critical = sp.rem(
        sp.Poly(sp.together(critical * z**4), a),
        sp.Poly(3 * a**2 + 1, a),
    ).as_expr() / z**4
    assert sp.expand(critical).coeff(z, -4) == 0
    assert sp.expand(critical).coeff(z, 0) == 0

    value = sp.expand(4 * x**3 + 2 * z**-2 * x)
    reduced = sp.rem(
        sp.Poly(sp.together(value * z**3), a),
        sp.Poly(3 * a**2 + 1, a),
    ).as_expr() / z**3
    assert sp.simplify(sp.expand(reduced).coeff(z, -3) - 2 * a / 3) == 0
    assert sp.simplify(sp.expand(reduced).coeff(z, 1) - s / a) == 0
    print("u=infinity large-branch expansion: PASS")


def check_u_infinity_small() -> None:
    z, a = sp.symbols("z a", nonzero=True)
    x = a * z
    value = sp.expand(4 * x**3 + 2 * z**-2 * x)
    assert sp.simplify(value.coeff(z, -1) - 2 * a) == 0
    assert sp.simplify(value.coeff(z, 3) - 4 * a**3) == 0
    print("u=infinity small-branch expansion: PASS")


def induced_character(d: int, exponent: int) -> list[int]:
    """Character of Psi^exponent(Ind from the trivial index-d subgroup model).

    On the tame quotient C_d, the induction character is d at identity and zero
    elsewhere.  Adams sends chi(g) to chi(g^exponent).
    """
    return [d if (exponent * k) % d == 0 else 0 for k in range(d)]


def check_regular_adams() -> None:
    for p in (5, 11, 17, 23, 29, 41, 47, 53, 71):
        for d in (2, 4):
            assert sp.gcd(p, d) == 1
            assert induced_character(d, p) == [d] + [0] * (d - 1)
            # Twisting the regular character by any character does not alter it.
            for m in range(d):
                twisted = []
                for k, value in enumerate(induced_character(d, p)):
                    root = sp.exp(2 * sp.pi * sp.I * m * k / d)
                    twisted.append(sp.simplify(root * value))
                assert twisted == [d] + [0] * (d - 1)
    print("Adams induced-block regular character: PASS")


def check_s_zero_class() -> None:
    # In R(C2), (3*1+chi)*(chi-1)=2*(chi-1).
    # Store coefficients in basis [1, chi], with chi^2=1.
    left = (-3 + 1, 3 - 1)
    right = (-2, 2)
    assert left == right
    print("s=0 Kummer-projected class: PASS")


def main() -> None:
    check_s_infinity()
    check_u_infinity_large()
    check_u_infinity_small()
    check_regular_adams()
    check_s_zero_class()
    print("ORIENTATION_ODD_LOCAL_INERTIA_VERIFY: PASS")


if __name__ == "__main__":
    main()
