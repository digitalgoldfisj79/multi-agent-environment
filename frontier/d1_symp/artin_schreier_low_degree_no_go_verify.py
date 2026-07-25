#!/usr/bin/env python3
"""Checks for ARTIN_SCHREIER_LOW_DEGREE_TSCHIRNHAUS_NO_GO_20260725.md."""

from __future__ import annotations

from math import comb, isqrt


def primes_below(limit: int):
    for p in range(5, limit):
        if p % 6 != 5:
            continue
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def trace_power_of_alpha(p: int, exponent: int) -> list[int]:
    """Return Tr(alpha^exponent) in basis 1,alpha,...,alpha^(p-1).

    Uses alpha^p=alpha+1 after the conjugate-sum formula.
    All exponents used here are at most 2p-1.
    """
    result = [0] * p
    for j in range(p - 1, exponent + 1, p - 1):
        coefficient = (-comb(exponent, j)) % p
        remaining = exponent - j
        if remaining == p:
            result[1] = (result[1] + coefficient) % p
            result[0] = (result[0] + coefficient) % p
        else:
            result[remaining] = (result[remaining] + coefficient) % p
    return result


def assert_minus_one_trace(p: int, exponent: int) -> None:
    value = trace_power_of_alpha(p, exponent)
    assert value[0] == p - 1
    assert all(x == 0 for x in value[1:])


def verify_prime(p: int) -> None:
    # Universal trace identities.
    assert_minus_one_trace(p, p - 1)
    assert_minus_one_trace(p, 2 * p - 2)
    assert_minus_one_trace(p, 2 * p - 1)

    # Quadratic critical moment.
    quadratic_moment = (p - 1) // 2
    assert quadratic_moment <= p - 4
    assert 2 * quadratic_moment == p - 1

    # Cubic first gate and final contradiction.
    h = (p - 2) // 3
    cubic_first = h + 1
    cubic_final = 2 * h + 1
    assert 3 * cubic_first == p + 1
    assert 3 * cubic_final == 2 * p - 1
    assert cubic_first <= p - 4
    assert cubic_final <= p - 4

    for r in range(p):
        trace_first = (-cubic_first * r) % p
        if trace_first == 0:
            assert r == 0

    assert_minus_one_trace(p, 3 * cubic_final)

    # Quartic gates.
    if p % 4 == 1:
        quartic_direct = (p - 1) // 4
        assert quartic_direct <= p - 4
        assert 4 * quartic_direct == p - 1
    else:
        quartic_first = (p + 1) // 4
        quartic_second = quartic_first + 1
        quartic_final = (p - 1) // 2
        assert quartic_first <= p - 4
        assert quartic_second <= p - 4
        assert quartic_final <= p - 4

        for r in range(p):
            if (-quartic_first * r) % p == 0:
                assert r == 0

        coefficient = comb(quartic_second, 2) % p
        assert coefficient != 0
        for s in range(p):
            if (-coefficient * s * s) % p == 0:
                assert s == 0

        assert 4 * quartic_final == 2 * p - 2
        assert_minus_one_trace(p, 4 * quartic_final)

    # Möbius logarithmic-derivative identity at every base-field r.
    for r in range(p):
        f_r = (pow(r, p, p) - r - 1) % p
        fprime_r = (-1) % p
        assert f_r == p - 1
        assert fprime_r * pow(f_r, -1, p) % p == 1

    print(
        f"p={p}: quadratic, cubic and quartic gates PASS"
    )


def main() -> None:
    checked = 0
    for p in primes_below(200):
        if p < 11:
            continue
        verify_prime(p)
        checked += 1
    print(f"ARTIN_SCHREIER_LOW_DEGREE_NO_GO_VERIFY: PASS ({checked} primes)")


if __name__ == "__main__":
    main()
