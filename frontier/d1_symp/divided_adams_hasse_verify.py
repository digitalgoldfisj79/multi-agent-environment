#!/usr/bin/env python3
"""Deterministic checks for DIVIDED_ADAMS_HASSE_COEFFICIENT_20260725.md.

The proof is symbolic. This script verifies its finite recurrences, the
committed exact calibrations, and a broad nonvanishing range. It does not
replace the uniform proof still required for H_p != 0.
"""

from __future__ import annotations

from math import factorial, isqrt


EXACT_T = {
    5: 0,
    11: 322102,
    17: 11899821517,
    23: -1010446643080743,
    29: -798145148362709627351,
    41: 285608599198466451834837856911313,
    47: -36201375290118292903477796139763762494,
    53: 625211553014678241605175931243651758726469297,
    71: 36727396978062655326395765238086038211050946366161670340353263984,
}


def inv(x: int, p: int) -> int:
    x %= p
    if x == 0:
        raise ZeroDivisionError(f"attempted inversion of zero modulo {p}")
    return pow(x, -1, p)


def vp(n: int, p: int) -> tuple[int, int]:
    if n == 0:
        raise ValueError("v_p(0) is not finite")
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value, n


def edge_polynomial_coefficients(p: int) -> list[int]:
    if p % 6 != 5:
        raise ValueError("this verifier is for p = 5 mod 6")
    h = (p - 2) // 3
    coeffs = [1]
    for n in range(h):
        first = (
            -coeffs[-1] * inv(9 * (n + 1) * (3 * n + 4), p)
        ) % p
        second = (
            coeffs[-1] * inv(27 * (n + 1) * (2 * h - n), p)
        ) % p
        assert first == second
        coeffs.append(first)

    denom_common = factorial(2 * h) % p
    for n, value in enumerate(coeffs):
        closed = factorial(2 * h - n) % p
        closed *= inv(pow(27, n, p) * (factorial(n) % p), p)
        closed *= inv(denom_common, p)
        assert value == closed % p
    return coeffs


def logarithmic_derivative(coeffs: list[int], p: int) -> list[int]:
    h = len(coeffs) - 1
    result: list[int] = []
    for n in range(h):
        value = ((n + 1) * coeffs[n + 1]) % p
        for i in range(1, n + 1):
            value -= coeffs[i] * result[n - i]
        result.append(value % p)

    assert result[0] == (-inv(36, p)) % p
    for n in range(1, h):
        convolution = sum(
            result[i] * result[n - 1 - i] for i in range(n)
        ) % p
        expected = (-3 * convolution * inv(3 * n + 4, p)) % p
        assert result[n] == expected
    return result


def hasse_coefficient(p: int) -> tuple[int, int, int]:
    h = (p - 2) // 3
    coeffs = edge_polynomial_coefficients(p)
    rayleigh = logarithmic_derivative(coeffs, p)

    log_coefficient = rayleigh[h - 1] * inv(h, p) % p
    fact_h = factorial(h) % p
    fact_2h1 = factorial(2 * h + 1) % p

    scalar = (
        fact_h * inv(6 * fact_2h1 * fact_2h1, p)
    ) % p
    endpoint = log_coefficient * inv(fact_h, p) % p

    assert h % 2 == 1
    assert fact_2h1 * fact_h % p == 1
    assert scalar == pow(fact_h, 3, p) * inv(6, p) % p

    return (scalar + endpoint) % p, scalar, endpoint


def primes_below(limit: int) -> list[int]:
    if limit <= 2:
        return []
    sieve = bytearray(b"\x01") * limit
    sieve[0:2] = b"\x00\x00"
    for q in range(2, isqrt(limit - 1) + 1):
        if sieve[q]:
            start = q * q
            count = ((limit - 1 - start) // q) + 1
            sieve[start:limit:q] = b"\x00" * count
    return [q for q in range(limit) if sieve[q]]


def verify_calibrations() -> None:
    assert hasse_coefficient(5)[0] == 0
    assert EXACT_T[5] == 0

    expected_rows = {
        11: (5, 2, 3, 6),
        17: (7, 12, 3, 2),
        23: (9, 14, 16, 16),
        29: (11, 5, 19, 5),
        41: (15, 13, 38, 31),
        47: (17, 4, 15, 28),
        53: (19, 10, 13, 30),
        71: (25, 32, 45, 65),
    }

    for p, (valuation, unit, scalar, endpoint) in expected_rows.items():
        actual_valuation, quotient = vp(EXACT_T[p], p)
        h_value, scalar_value, endpoint_value = hasse_coefficient(p)
        assert actual_valuation == valuation == (p + 4) // 3
        assert quotient % p == unit
        assert scalar_value == scalar
        assert endpoint_value == endpoint
        assert (-h_value) % p == unit
        print(
            f"p={p}: valuation={valuation}, unit={unit}, "
            f"scalar={scalar}, endpoint={endpoint}: OK"
        )


def verify_nonvanishing_scan(limit: int = 1500) -> None:
    zeros: list[int] = []
    checked = 0
    for p in primes_below(limit):
        if p % 6 != 5:
            continue
        checked += 1
        value, _, _ = hasse_coefficient(p)
        if value == 0:
            zeros.append(p)

    assert zeros == [5], zeros
    print(
        f"Hasse scan: {checked} primes p=5 mod 6 below {limit}; "
        "only p=5 vanishes: OK"
    )


def verify_walk_coefficients() -> None:
    for p in (5, 7, 11, 17, 23):
        one_excursion_after_division = p // p
        two_excursions_before_division = p * (p - 3) // 2
        two_excursions_after_division = (
            two_excursions_before_division // p
        )
        assert one_excursion_after_division == 1
        assert two_excursions_after_division == (p - 3) // 2
    print("closed-walk divided coefficients: OK")


if __name__ == "__main__":
    verify_walk_coefficients()
    verify_calibrations()
    verify_nonvanishing_scan()
    print("DIVIDED_ADAMS_HASSE_VERIFY: PASS")
