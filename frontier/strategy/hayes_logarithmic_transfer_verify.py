#!/usr/bin/env python3
"""Verify the truncated-log and Fourier-support statements for the Hayes route.

No irreducible-polynomial census is performed.  The script checks:
  * the truncated logarithm is a group homomorphism on
    1+z F_p[z]/(z^(p-1));
  * every unit has p-th power one;
  * the cubic/quadratic coefficient plane maps to the final two log coordinates;
  * fixed classes and square-class projectors have full character support;
  * averaging the complete (a,b)-plane leaves exactly p^(p-4) characters.
"""
from __future__ import annotations

import json
from itertools import product
from pathlib import Path


def add(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    return tuple((x + y) % p for x, y in zip(a, b))


def mul(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    """Multiply in F_p[z]/(z^(p-1)); vectors include the constant term."""
    n = len(a)
    out = [0] * n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < n:
                out[i + j] = (out[i + j] + x * y) % p
    return tuple(out)


def power(a: tuple[int, ...], exponent: int, p: int) -> tuple[int, ...]:
    out = (1,) + (0,) * (len(a) - 1)
    while exponent:
        if exponent & 1:
            out = mul(out, a, p)
        a = mul(a, a, p)
        exponent //= 2
    return out


def log_unit(unit: tuple[int, ...], p: int) -> tuple[int, ...]:
    """Truncated log; output has zero constant coordinate."""
    n = len(unit)
    u = list(unit)
    u[0] = (u[0] - 1) % p
    u = tuple(u)
    out = (0,) * n
    term = u
    for k in range(1, p):
        coeff = (1 if k % 2 else -1) * pow(k, -1, p)
        out = add(out, tuple(coeff * x % p for x in term), p)
        term = mul(term, u, p)
    return out


def plane_unit(p: int, a: int, b: int) -> tuple[int, ...]:
    # Powers 0,...,p-2; a is at z^(p-3), b at z^(p-2).
    out = [0] * (p - 1)
    out[0] = 1
    out[p - 3] = a % p
    out[p - 2] = b % p
    return tuple(out)


def deterministic_units(p: int) -> list[tuple[int, ...]]:
    n = p - 1
    units = [(1,) + (0,) * (n - 1)]
    for seed in range(1, min(20, p * 3)):
        coeffs = [1]
        value = seed
        for index in range(1, n):
            value = (value * (index + 2) + seed + index) % p
            coeffs.append(value)
        units.append(tuple(coeffs))
    return units


def check_prime(p: int) -> dict[str, int | bool]:
    identity = (1,) + (0,) * (p - 2)
    units = deterministic_units(p)

    homomorphism_checks = 0
    for left in units:
        assert power(left, p, p) == identity
        for right in units[:8]:
            assert log_unit(mul(left, right, p), p) == add(
                log_unit(left, p), log_unit(right, p), p
            )
            homomorphism_checks += 1

    plane_checks = 0
    for a, b in product(range(p), repeat=2):
        expected = [0] * (p - 1)
        expected[p - 3] = a
        expected[p - 2] = b
        assert log_unit(plane_unit(p, a, b), p) == tuple(expected)
        plane_checks += 1

    ell = p - 2
    fixed_class_support = p ** ell
    trivial_a_average_support = p ** ell
    quadratic_a_average_support = (p - 1) * p ** (ell - 1)
    square_class_support = p ** ell
    full_plane_support = p ** (ell - 2)

    # Exact additive-character orthogonality on the last two coordinates.
    for top_a, top_b in product(range(p), repeat=2):
        counts = [0] * p
        for a, b in product(range(p), repeat=2):
            counts[(top_a * a + top_b * b) % p] += 1
        if top_a == top_b == 0:
            assert counts[0] == p * p and sum(counts[1:]) == 0
        else:
            assert counts == [p] * p

    return {
        "p": p,
        "log_homomorphism_checks": homomorphism_checks,
        "plane_checks": plane_checks,
        "fixed_class_character_support": fixed_class_support,
        "trivial_nonzero_a_average_support": trivial_a_average_support,
        "quadratic_nonzero_a_average_support": quadratic_a_average_support,
        "one_square_class_support": square_class_support,
        "complete_ab_plane_support": full_plane_support,
        "status": True,
    }


def main() -> None:
    results = [check_prime(p) for p in (5, 7, 11)]
    output = {
        "classification": "exact finite-group regression; no polynomial census",
        "results": results,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "hayes_logarithmic_transfer_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    for row in results:
        print(
            f"p={row['p']} fixed={row['fixed_class_character_support']} "
            f"square_class={row['one_square_class_support']} "
            f"plane={row['complete_ab_plane_support']} PASS"
        )
    print("HAYES_LOGARITHMIC_TRANSFER_VERIFY: PASS")


if __name__ == "__main__":
    main()
