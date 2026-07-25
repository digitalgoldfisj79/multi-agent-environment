#!/usr/bin/env python3
"""Exact checks for SPARSE_FREQUENCY_SYMPLECTIC_POLARIZATION_20260725.md.

The script verifies, over F_p for the calibrated primes:

- the monomial Wronskian matrix;
- nondegeneracy and the complementary-degree pairing;
- isotropy and half dimension of the canonical lower Lagrangian;
- translation invariance for all basis pairs and selected translations;
- the radical of the cubic multiplier subspace;
- conformal scaling with multiplier a^p.

Only Python integer arithmetic is used.
"""

from __future__ import annotations

from math import comb


def polynomial_basis(degree: int, max_degree: int) -> list[int]:
    result = [0] * (max_degree + 1)
    result[degree] = 1
    return result


def derivative(poly: list[int], p: int) -> list[int]:
    return [(i * poly[i]) % p for i in range(1, len(poly))]


def multiply(a: list[int], b: list[int], p: int) -> list[int]:
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] = (result[i + j] + x * y) % p
    return result


def translate(poly: list[int], value: int, p: int) -> list[int]:
    max_degree = len(poly) - 1
    result = [0] * (max_degree + 1)
    for degree, coefficient in enumerate(poly):
        for new_degree in range(degree + 1):
            result[new_degree] += (
                coefficient
                * comb(degree, new_degree)
                * pow(value, degree - new_degree, p)
            )
            result[new_degree] %= p
    return result


def scale(poly: list[int], value: int, p: int) -> list[int]:
    return [
        coefficient * pow(value, degree, p) % p
        for degree, coefficient in enumerate(poly)
    ]


def omega(f: list[int], g: list[int], p: int) -> int:
    left = multiply(derivative(f, p), g, p)
    right = multiply(f, derivative(g, p), p)
    length = max(len(left), len(right))
    left += [0] * (length - len(left))
    right += [0] * (length - len(right))
    coefficient = p - 1
    return (
        (left[coefficient] if coefficient < len(left) else 0)
        - (right[coefficient] if coefficient < len(right) else 0)
    ) % p


def verify_prime(p: int) -> None:
    if p < 11 or p % 2 == 0:
        raise ValueError("expected an odd prime p>=11")

    max_degree = p - 4
    frequency_degrees = list(range(4, p - 3))
    dimension = len(frequency_degrees)
    half = (p - 7) // 2
    assert dimension == p - 7 == 2 * half

    basis = {
        degree: polynomial_basis(degree, max_degree)
        for degree in range(max_degree + 1)
    }

    # Exact monomial matrix.
    for a in frequency_degrees:
        for b in frequency_degrees:
            expected = (a - b) % p if a + b == p else 0
            assert omega(basis[a], basis[b], p) == expected

    # The cubic multiplier subspace is in the radical before quotienting.
    for a in range(4):
        for b in range(max_degree + 1):
            assert omega(basis[a], basis[b], p) == 0
            assert omega(basis[b], basis[a], p) == 0

    # Every frequency degree has one complementary partner and a unit entry.
    for a in frequency_degrees:
        partner = p - a
        assert partner in frequency_degrees
        assert (2 * a - p) % p != 0

    lower = list(range(4, (p - 1) // 2 + 1))
    upper = list(range((p + 1) // 2, p - 3))
    assert len(lower) == len(upper) == half

    # Both halves are Lagrangian, and the cross-pairing is perfect.
    for a in lower:
        for b in lower:
            assert omega(basis[a], basis[b], p) == 0
    for a in upper:
        for b in upper:
            assert omega(basis[a], basis[b], p) == 0
    for a in lower:
        assert omega(basis[a], basis[p - a], p) != 0

    # Translation invariance.  This exhausts basis pairs for four translations.
    for value in (0, 1, 2, p - 1):
        for a in frequency_degrees:
            translated_a = translate(basis[a], value, p)
            for b in frequency_degrees:
                translated_b = translate(basis[b], value, p)
                assert omega(translated_a, translated_b, p) == omega(
                    basis[a], basis[b], p
                )

    # The lower Lagrangian is degree-filtered and therefore translation stable
    # modulo the cubic multiplier subspace.
    lower_bound = (p - 1) // 2
    for value in (0, 1, 2, p - 1):
        for a in lower:
            translated = translate(basis[a], value, p)
            assert all(
                coefficient == 0
                for degree, coefficient in enumerate(translated)
                if degree > lower_bound
            )

    # Conformal scaling: omega(f(aT),g(aT))=a^p omega(f,g).
    for value in (1, 2, p - 1):
        for a in frequency_degrees:
            scaled_a = scale(basis[a], value, p)
            for b in frequency_degrees:
                scaled_b = scale(basis[b], value, p)
                assert omega(scaled_a, scaled_b, p) == (
                    pow(value, p, p) * omega(basis[a], basis[b], p)
                ) % p

    print(
        f"p={p}: dim={dimension}, lagrangian_dim={half}, "
        "symplectic/affine checks PASS"
    )


def main() -> None:
    for p in (11, 17, 23, 29, 41, 47, 53):
        verify_prime(p)
    print("SPARSE_FREQUENCY_SYMPLECTIC_VERIFY: PASS")


if __name__ == "__main__":
    main()
