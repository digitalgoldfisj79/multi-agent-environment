#!/usr/bin/env python3
"""Checks for CANONICAL_QUADRATIC_OSCILLATOR_ON_SPARSE_FREQUENCIES_20260725.md."""

from __future__ import annotations

from itertools import product


def quadratic_character(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def verify_symbolic_prime(p: int) -> None:
    degrees = list(range(4, p - 3))
    dimension = p - 7
    half = dimension // 2
    assert len(degrees) == dimension == 2 * half

    # Degree reversal and anti-symplectic pairing.
    for a in degrees:
        partner = p - a
        assert partner in degrees
        assert p - partner == a

        original = (a - partner) % p
        reversed_value = (partner - a) % p
        assert reversed_value == (-original) % p

    # Hessian diagonal entries and nondegeneracy.
    hessian = [(2 * a - p) % p for a in degrees]
    assert all(value != 0 for value in hessian)

    # Quadratic coefficients are a modulo p.
    coefficients = [a % p for a in degrees]
    determinant = 1
    for value in coefficients:
        determinant = determinant * value % p

    expected_square_class = -1 if half % 2 else 1
    assert (
        quadratic_character(determinant, p)
        == quadratic_character(expected_square_class, p)
    )

    # chi(det Q) * chi(-1)^m = 1, so the 2m-dimensional Gauss sum
    # has no residual quadratic Kummer sign.
    total_sign = quadratic_character(determinant, p) * (
        quadratic_character(-1, p) ** half
    )
    assert total_sign == 1

    print(
        f"p={p}: dim={dimension}, half={half}, det={determinant}, "
        "Gauss sign=+1: PASS"
    )


def verify_direct_p11() -> None:
    p = 11
    degrees = list(range(4, p - 3))
    half = (p - 7) // 2
    phase_counts = [0] * p

    for coordinates in product(range(p), repeat=len(degrees)):
        phase = sum(
            degree * coordinate * coordinate
            for degree, coordinate in zip(degrees, coordinates)
        ) % p
        phase_counts[phase] += 1

    # Rationality: all nonzero additive phases occur equally often.
    assert phase_counts[1:] == [phase_counts[1]] * (p - 1)
    exact_sum = phase_counts[0] - phase_counts[1]
    assert exact_sum == p**half == 121
    assert exact_sum - 1 == 120

    print(
        "p=11 direct quadratic census:",
        phase_counts,
        "sum=121, punctured sum=120: PASS",
    )


def main() -> None:
    for p in (11, 17, 23, 29, 41, 47, 53):
        verify_symbolic_prime(p)
    verify_direct_p11()
    print("CANONICAL_QUADRATIC_OSCILLATOR_VERIFY: PASS")


if __name__ == "__main__":
    main()
