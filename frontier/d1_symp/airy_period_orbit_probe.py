#!/usr/bin/env python3
"""
Exact period-orbit probe for the cubic Airy Adams trace.

For p == 2 (mod 3), the nonzero Airy parameters split into two Galois
orbits: squares and nonsquares.  For each orbit this script:

  * constructs the exact orbit polynomial of the Airy trace t_u in
    Z[zeta_p], using only the relation 1+zeta+...+zeta^(p-1)=0;
  * reduces the p-th Dickson polynomial D_p(X,p) modulo that orbit
    polynomial;
  * computes the exact field trace of D_p(t_u,p);
  * verifies that the two traces sum to -p*T_p for committed exact T_p.

A remainder of degree orbit_degree-1 is a focused failure certificate for a
bounded-degree period-polynomial collapse.  It is not a proof that no other
cross-orbit identity can exist.

Dependencies: Python 3 and sympy.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass

import sympy as sp

X = sp.symbols("X")


Vector = tuple[int, ...]


def canonical(v: Vector) -> Vector:
    """Canonical representative in Z[zeta_p], setting coeff(zeta^(p-1))=0."""
    c = v[-1]
    return tuple(x - c for x in v[:-1]) + (0,)


def zero(p: int) -> Vector:
    return (0,) * p


def integer(n: int, p: int) -> Vector:
    return (n,) + (0,) * (p - 1)


def add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))


def negate(a: Vector) -> Vector:
    return tuple(-x for x in a)


def scale(a: Vector, n: int) -> Vector:
    return tuple(n * x for x in a)


def multiply(a: Vector, b: Vector, p: int) -> Vector:
    out = [0] * p
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[(i + j) % p] += ai * bj
    return canonical(tuple(out))


def polynomial_multiply(a: list[Vector], b: list[Vector], p: int) -> list[Vector]:
    out = [zero(p) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = add(out[i + j], multiply(ai, bj, p))
    return [canonical(c) for c in out]


def airy_trace(p: int, u: int) -> Vector:
    """Return t_u = -sum_x zeta_p^(x^3+u*x) in canonical coordinates."""
    out = [0] * p
    for x in range(p):
        out[(x**3 + u * x) % p] -= 1
    return canonical(tuple(out))


def parameter_orbit(p: int, square: bool) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    if square:
        return sorted(squares)
    return sorted(set(range(1, p)) - squares)


def orbit_polynomial(p: int, square: bool) -> sp.Poly:
    coefficients = [integer(1, p)]
    for u in parameter_orbit(p, square):
        coefficients = polynomial_multiply(
            coefficients,
            [negate(airy_trace(p, u)), integer(1, p)],
            p,
        )

    rational_coefficients: list[int] = []
    for coefficient in coefficients:
        c = canonical(coefficient)
        if any(x != 0 for x in c[1:]):
            raise ArithmeticError("orbit polynomial coefficient is not rational")
        rational_coefficients.append(c[0])

    return sp.Poly(
        sum(c * X**i for i, c in enumerate(rational_coefficients)),
        X,
        domain=sp.ZZ,
    )


def dickson_polynomial(n: int, parameter: int) -> sp.Poly:
    """D_n(X,a), characterized by D_n(alpha+beta,alpha*beta)=alpha^n+beta^n."""
    if n == 0:
        return sp.Poly(2, X, domain=sp.ZZ)
    if n == 1:
        return sp.Poly(X, X, domain=sp.ZZ)
    d0 = sp.Integer(2)
    d1 = X
    for _ in range(2, n + 1):
        d0, d1 = d1, sp.expand(X * d1 - parameter * d0)
    return sp.Poly(d1, X, domain=sp.ZZ)


def evaluate_dickson_in_cyclotomic_ring(p: int, t: Vector) -> Vector:
    if p == 1:
        return t
    d0 = integer(2, p)
    d1 = t
    for _ in range(2, p + 1):
        d0, d1 = d1, add(multiply(t, d1, p), negate(scale(d0, p)))
    return canonical(d1)


def orbit_field_trace(p: int, square: bool) -> int:
    total = zero(p)
    for u in parameter_orbit(p, square):
        total = add(total, evaluate_dickson_in_cyclotomic_ring(p, airy_trace(p, u)))
    total = canonical(total)
    if any(x != 0 for x in total[1:]):
        raise ArithmeticError("orbit sum is not rational")
    return total[0]


@dataclass(frozen=True)
class OrbitResult:
    label: str
    orbit_degree: int
    orbit_polynomial: sp.Poly
    remainder: sp.Poly
    field_trace: int


def probe_orbit(p: int, square: bool) -> OrbitResult:
    label = "square" if square else "nonsquare"
    minimal_candidate = orbit_polynomial(p, square)
    expected_degree = (p - 1) // 2
    if minimal_candidate.degree() != expected_degree:
        raise AssertionError((p, label, minimal_candidate.degree(), expected_degree))
    if sp.gcd(minimal_candidate, minimal_candidate.diff()).degree() != 0:
        raise AssertionError("orbit polynomial is not square-free")

    dickson = dickson_polynomial(p, p)
    remainder = dickson.rem(minimal_candidate)
    return OrbitResult(
        label=label,
        orbit_degree=expected_degree,
        orbit_polynomial=minimal_candidate,
        remainder=remainder,
        field_trace=orbit_field_trace(p, square),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", nargs="*", type=int, default=[11, 17, 23, 29])
    args = parser.parse_args()

    committed_t = {
        5: 0,
        11: 322102,
        17: 11899821517,
        23: -1010446643080743,
        29: -798145148362709627351,
    }

    for p in args.primes:
        if not sp.isprime(p) or p % 3 != 2:
            raise ValueError(f"p={p} must be prime and 2 mod 3")
        results = [probe_orbit(p, True), probe_orbit(p, False)]
        print(f"p={p}")
        total = 0
        for result in results:
            total += result.field_trace
            print(
                f"  {result.label}: orbit_degree={result.orbit_degree} "
                f"remainder_degree={result.remainder.degree()} "
                f"field_trace={result.field_trace}"
            )
            print(f"    orbit_polynomial={result.orbit_polynomial.as_expr()}")
            print(f"    dickson_remainder={result.remainder.as_expr()}")
        print(f"  total_virtual_trace={total}")
        if p in committed_t:
            expected = -p * committed_t[p]
            if total != expected:
                raise AssertionError((p, total, expected))
            print(f"  check=-p*T_p={expected}: PASS")


if __name__ == "__main__":
    main()
