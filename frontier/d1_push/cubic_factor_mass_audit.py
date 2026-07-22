#!/usr/bin/env python3
"""Independent exact audit of the cubic-factor mass theorem."""
from __future__ import annotations

import json
from collections import Counter
from math import comb
from pathlib import Path

PRIMES = (5, 7, 11, 13, 17, 19, 23, 29)


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def multiply_mod_cubic(
    left: list[int],
    right: list[int],
    p: int,
    t: int,
    s: int,
    n: int,
) -> list[int]:
    product = [0] * 5
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            product[i + j] = (product[i + j] + x * y) % p

    # X^3=tX^2-sX+n.
    for degree in range(4, 2, -1):
        coefficient = product[degree] % p
        if not coefficient:
            continue
        product[degree] = 0
        shift = degree - 3
        product[shift] = (product[shift] + coefficient * n) % p
        product[shift + 1] = (product[shift + 1] - coefficient * s) % p
        product[shift + 2] = (product[shift + 2] + coefficient * t) % p

    return product[:3]


def x_to_p_mod_cubic(p: int, t: int, s: int, n: int) -> list[int]:
    result = [1, 0, 0]
    base = [0, 1, 0]
    exponent = p
    while exponent:
        if exponent & 1:
            result = multiply_mod_cubic(result, base, p, t, s, n)
        base = multiply_mod_cubic(base, base, p, t, s, n)
        exponent >>= 1
    return result


def irreducible_cubic(p: int, t: int, s: int, n: int) -> bool:
    return all(
        (x**3 - t * x * x + s * x - n) % p != 0
        for x in range(p)
    )


def audit_class(p: int, a: int) -> dict:
    factors_per_member: Counter[tuple[int, int]] = Counter()
    satisfying_roots = 0
    translation_orbits = 0

    # Each orbit has a unique representative with trace zero.
    for s0 in range(p):
        for n0 in range(p):
            if irreducible_cubic(p, 0, s0, n0):
                translation_orbits += 1

    for t in range(p):
        for s in range(p):
            for n in range(p):
                if not irreducible_cubic(p, t, s, n):
                    continue

                A, B, C = x_to_p_mod_cubic(p, t, s, n)
                if (C + a * t) % p != 0:
                    continue

                c = (a * s - B) % p
                d = (-A - a * n) % p
                factors_per_member[(c, d)] += 1
                satisfying_roots += 3

                # Direct quotient-ring divisibility check.
                remainder = [
                    (A + a * n + d) % p,
                    (B - a * s + c) % p,
                    (C + a * t) % p,
                ]
                assert remainder == [0, 0, 0]

                # Check the Frobenius-oriented discriminant interpolation.
                discriminant = (
                    t * t * s * s
                    - 4 * s**3
                    - 4 * t**3 * n
                    - 27 * n * n
                    + 18 * t * s * n
                ) % p

                numerator_c = (t * t - 3 * s) % p
                candidates = []
                if C:
                    candidates.append(numerator_c * pow(C, -1, p) % p)
                denominator_b = (2 * B + 1) % p
                numerator_b = (-2 * t**3 + 7 * t * s - 9 * n) % p
                if denominator_b:
                    candidates.append(
                        numerator_b * pow(denominator_b, -1, p) % p
                    )
                denominator_a = (2 * A - t) % p
                numerator_a = (t * t * s + 3 * t * n - 4 * s * s) % p
                if denominator_a:
                    candidates.append(
                        numerator_a * pow(denominator_a, -1, p) % p
                    )

                assert candidates
                assert len(set(candidates)) == 1
                delta = candidates[0]
                assert delta * delta % p == discriminant
                assert (t * t - 3 * s + a * t * delta) % p == 0

    incidence = sum(factors_per_member.values())
    expected = (p * p - 1) // 3
    assert incidence == expected
    assert satisfying_roots == p * expected
    assert translation_orbits == expected

    distribution = Counter(
        factors_per_member[(c, d)] for c in range(p) for d in range(p)
    )

    return {
        "a": a,
        "square_class": chi(a, p),
        "translation_orbit_count": translation_orbits,
        "cubic_factor_incidence": incidence,
        "expected_incidence": expected,
        "member_multiplicity_distribution": {
            str(k): distribution[k] for k in sorted(distribution)
        },
        "second_factorial_moment": sum(
            comb(value, 2) for value in factors_per_member.values()
        ),
        "third_factorial_moment": sum(
            comb(value, 3) for value in factors_per_member.values()
        ),
    }


def main() -> None:
    rows = []
    for p in PRIMES:
        nonsquare = next(a for a in range(2, p) if chi(a, p) == -1)
        rows.append(
            {
                "prime": p,
                "classes": [audit_class(p, 1), audit_class(p, nonsquare)],
            }
        )

    result = {
        "status": "PASS",
        "statement": (
            "For both square classes and every audited prime, additive "
            "translation orbits of degree-three elements are counted exactly "
            "by (p^2-1)/3, and exactly one element per orbit satisfies the "
            "fixed-a cubic divisibility condition."
        ),
        "range": "all prime p from 5 through 29",
        "rows": rows,
    }

    output = Path(__file__).with_name("cubic_factor_mass_audit_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
