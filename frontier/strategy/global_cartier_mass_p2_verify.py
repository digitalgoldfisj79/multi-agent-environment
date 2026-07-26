#!/usr/bin/env python3
"""Exact regressions for the global Cartier mass and its naive mod-p^2 lift.

The proved general Cartier-cofactor theorem gives, for
 F=X^p+aX^3+cX+d (a != 0),
 C_3(F)=3a*1_irreducible in F_p.

This verifier:
  * checks the two surviving a-Fourier modes at p=5,7;
  * enumerates the naive integral cofactor modulo p^2;
  * counts reducible fibres with nonzero naive lift;
  * checks dependence on the integer lift a -> a+p;
  * shows that the complete naive p^2 mass is not the lifted count.

No external packages are required.
"""
from __future__ import annotations

import json


def trim(poly: list[int], modulus: int) -> list[int]:
    poly = [value % modulus for value in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def multiply(left: list[int], right: list[int], modulus: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a == 0:
            continue
        for j, b in enumerate(right):
            if b:
                out[i + j] = (out[i + j] + a * b) % modulus
    return trim(out, modulus)


def power(poly: list[int], exponent: int, modulus: int) -> list[int]:
    out = [1]
    base = trim(poly, modulus)
    while exponent:
        if exponent & 1:
            out = multiply(out, base, modulus)
        exponent >>= 1
        if exponent:
            base = multiply(base, base, modulus)
    return out


def determinant_ring(matrix: list[list[int]], modulus: int) -> int:
    """Subset-DP determinant, valid over the non-field Z/(p^2)."""
    size = len(matrix)
    states: dict[int, int] = {0: 1}
    for row in range(size):
        next_states: dict[int, int] = {}
        for mask, value in states.items():
            for column in range(size):
                if mask & (1 << column):
                    continue
                position = (mask & ((1 << column) - 1)).bit_count()
                sign = -1 if (row + position) & 1 else 1
                new_mask = mask | (1 << column)
                contribution = sign * value * matrix[row][column]
                next_states[new_mask] = (
                    next_states.get(new_mask, 0) + contribution
                ) % modulus
        states = next_states
    return states[(1 << size) - 1] % modulus


def cofactor_c3(p: int, a: int, c: int, d: int, modulus: int) -> int:
    coefficients = [d, c, 0, a] + [0] * (p - 4) + [1]
    expanded = power(coefficients, p - 1, modulus)
    columns = [v for v in range(1, p + 1) if v != 3]
    matrix: list[list[int]] = []
    for u in range(1, p):
        row: list[int] = []
        for v in columns:
            exponent = p * u - v
            h_value = expanded[exponent] if exponent < len(expanded) else 0
            row.append(((1 if u == v else 0) - h_value) % modulus)
        matrix.append(row)
    return determinant_ring(matrix, modulus)


def run_prime(p: int) -> dict[str, object]:
    modulus = p * p
    squares = {value * value % p for value in range(1, p)}
    fixed_class_total = {"square": 0, "nonsquare": 0}
    reducible_nonzero_lift = 0
    changed_by_a_lift = 0
    indicator_total = 0
    mass_trivial = 0
    mass_quadratic = 0
    naive_mass_p2 = 0

    for a in range(1, p):
        is_square = a in squares
        class_name = "square" if is_square else "nonsquare"
        chi = 1 if is_square else -1
        inverse_p = pow(a, -1, p)
        inverse_p2 = pow(a, -1, modulus)
        for c in range(p):
            for d in range(p):
                lifted = cofactor_c3(p, a, c, d, modulus)
                residue = lifted % p
                shifted_lift = cofactor_c3(p, a + p, c, d, modulus)

                if residue:
                    assert residue == (3 * a) % p
                    indicator_total += 1
                    fixed_class_total[class_name] += 1
                elif lifted:
                    # By the proved mod-p cofactor theorem this fibre is reducible.
                    reducible_nonzero_lift += 1

                if shifted_lift != lifted:
                    changed_by_a_lift += 1

                mass_trivial = (mass_trivial + inverse_p * residue) % p
                mass_quadratic = (
                    mass_quadratic + chi * inverse_p * residue
                ) % p
                naive_mass_p2 = (
                    naive_mass_p2 + inverse_p2 * lifted
                ) % modulus

    class_size = (p - 1) // 2
    n_plus = fixed_class_total["square"] // class_size
    n_minus = fixed_class_total["nonsquare"] // class_size
    inverse_two = pow(2, -1, p)
    expected_trivial = (-3 * inverse_two * (n_plus + n_minus)) % p
    expected_quadratic = (-3 * inverse_two * (n_plus - n_minus)) % p
    lifted_indicator_target = (3 * indicator_total) % modulus

    assert mass_trivial == expected_trivial
    assert mass_quadratic == expected_quadratic
    assert reducible_nonzero_lift > 0
    assert changed_by_a_lift > 0
    assert naive_mass_p2 != lifted_indicator_target

    return {
        "p": p,
        "fixed_class_counts": {"N_plus": n_plus, "N_minus": n_minus},
        "global_indicator_total": indicator_total,
        "mod_p_masses": {
            "trivial_mode": mass_trivial,
            "quadratic_mode": mass_quadratic,
        },
        "naive_mod_p2": {
            "reducible_fibres_with_nonzero_lift": reducible_nonzero_lift,
            "fibres_changed_by_a_to_a_plus_p": changed_by_a_lift,
            "weighted_mass": naive_mass_p2,
            "three_times_indicator_count": lifted_indicator_target,
        },
    }


def main() -> None:
    results = {str(p): run_prime(p) for p in (5, 7)}
    print(json.dumps(results, indent=2, sort_keys=True))
    print("ALL GLOBAL CARTIER MASS / P^2 LIFT CHECKS PASSED")


if __name__ == "__main__":
    main()
