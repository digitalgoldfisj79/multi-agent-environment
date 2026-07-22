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
    satisfying_root_count = 0
    translation_orbit_frobenius_classes = 0

    # Each additive translation orbit has one trace-zero element. Frobenius
    # permutes those trace-zero elements in triples, so trace-zero irreducible
    # cubics count Frobenius classes of translation orbits.
    for s0 in range(p):
        for n0 in range(p):
            if irreducible_cubic(p, 0, s0, n0):
                translation_orbit_frobenius_classes += 1

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
                satisfying_root_count += 3

                remainder = [
                    (A + a * n + d) % p,
                    (B - a * s + c) % p,
                    (C + a * t) % p,
                ]
                assert remainder == [0, 0, 0]

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
    expected_factor_incidence = (p * p - 1) // 3
    expected_additive_orbits = p * p - 1
    assert incidence == expected_factor_incidence
    assert satisfying_root_count == expected_additive_orbits
    assert translation_orbit_frobenius_classes == expected_factor_incidence

    distribution = Counter(
        factors_per_member[(c, d)] for c in range(p) for d in range(p)
    )

    return {
        "a": a,
        "square_class": chi(a, p),
        "additive_translation_orbit_count": expected_additive_orbits,
        "translation_orbit_frobenius_class_count": (
            translation_orbit_frobenius_classes
        ),
        "satisfying_degree_three_root_count": satisfying_root_count,
        "cubic_factor_incidence": incidence,
        "expected_incidence": expected_factor_incidence,
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
            "For both square classes and every audited prime, there are "
            "p^2-1 additive translation orbits of degree-three elements, "
            "exactly one satisfying root per orbit, and (p^2-1)/3 "
            "Frobenius classes/irreducible-cubic factor incidences."
        ),
        "range": "all prime p from 5 through 29",
        "rows": rows,
    }

    output = Path(__file__).with_name("cubic_factor_mass_audit_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
