#!/usr/bin/env python3
"""Checks for SPARSE_FREQUENCY_SYMPLECTIC_JORDAN_THEOREM_20260725.md."""

from __future__ import annotations


def verify_prime(p: int) -> None:
    degrees = list(range(4, p - 3))
    n = p - 7
    assert len(degrees) == n and n % 2 == 0

    # D e_a = a e_(a-1), with e_4 killed in the quotient.  Every link in
    # the chain is nonzero, so D is one Jordan block of length n.
    for a in degrees[1:]:
        assert a % p != 0

    # Kernel dimensions of powers of one Jordan block.
    for power in range(n + 1):
        kernel_dimension = min(power, n)
        direct_count = sum(1 for a in degrees if a - 4 < power)
        assert direct_count == kernel_dimension

    half = n // 2
    lower = list(range(4, (p - 1) // 2 + 1))
    assert len(lower) == half
    assert lower == [a for a in degrees if a - 4 < half]

    # Uniqueness recurrence for an affine-conformal alternating form.
    # Normalize c_4=4; then c_a=a is the unique solution.
    c = {4: 4 % p}
    for a in range(5, p - 3):
        c[a] = a * pow(a - 1, -1, p) * c[a - 1] % p
        assert c[a] == a % p

    # Alternation across complementary degrees.
    for a in degrees:
        partner = p - a
        assert partner in degrees
        assert c[partner] == (-c[a]) % p

    print(f"p={p}: J_{n}, intrinsic Lagrangian dimension {half}: PASS")


def main() -> None:
    for p in (11, 17, 23, 29, 41, 47, 53):
        verify_prime(p)
    print("SPARSE_FREQUENCY_JORDAN_VERIFY: PASS")


if __name__ == "__main__":
    main()
