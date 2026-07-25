#!/usr/bin/env python3
"""Exact regression checks for the wild-infinity filtered reduction.

Checks:
- det[binom(m+j-1,j)] = 1;
- Lucas support binom(m+j-1,j)=0 mod p iff m+j>p for 1<=m,j<p;
- the residual Newton identities have signs s_(p-3)=3A,
  s_(p-2)=2B, s_(p-1)=C.

No third-party packages are required.
"""

from fractions import Fraction
from math import comb


def bareiss_det(matrix: list[list[int]]) -> int:
    """Fraction-free determinant for a square integer matrix."""
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if a[r][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                if numerator % previous:
                    raise AssertionError("Bareiss division was not exact")
                a[i][j] = numerator // previous
        previous = pivot_value
    return sign * a[-1][-1]


def primes(limit: int):
    for n in range(5, limit + 1, 2):
        if all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            yield n


def verify_pascal_determinants(limit: int = 30) -> None:
    for n in range(1, limit + 1):
        matrix = [
            [comb(m + j - 1, j) for m in range(1, n + 1)]
            for j in range(1, n + 1)
        ]
        actual = bareiss_det(matrix)
        assert actual == 1, (n, actual)
    print(f"PASS: Pascal determinants equal 1 through n={limit}.")


def verify_lucas_support(limit: int = 199) -> None:
    checked = []
    for p in primes(limit):
        for m in range(1, p):
            for j in range(1, p):
                vanishes = comb(m + j - 1, j) % p == 0
                assert vanishes == (m + j > p), (p, m, j)
        checked.append(p)
    print(f"PASS: Lucas support through p={checked[-1]}.")


def verify_tail_signs(limit: int = 199) -> None:
    checked = []
    for p in primes(limit):
        if p % 6 != 5:
            continue
        # In T^p + A T^3 + B T^2 + C T + D,
        # coefficient of T^(p-k) is (-1)^k e_k.
        assert (-1) ** (p - 3) == 1   # A=e_(p-3)
        assert (-1) ** (p - 2) == -1  # B=-e_(p-2)
        assert (-1) ** (p - 1) == 1   # C=e_(p-1)

        # Newton: s_k=(-1)^(k+1) k e_k when all lower terms vanish.
        coefficient_a = ((-1) ** (p - 2) * (p - 3)) % p
        coefficient_b = ((-1) ** (p - 1) * (p - 2) * -1) % p
        coefficient_c = ((-1) ** p * (p - 1)) % p
        assert coefficient_a == 3 % p
        assert coefficient_b == 2 % p
        assert coefficient_c == 1
        checked.append(p)
    print(f"PASS: residual Newton tail signs through p={checked[-1]}.")


def main() -> None:
    verify_pascal_determinants()
    verify_lucas_support()
    verify_tail_signs()


if __name__ == "__main__":
    main()
