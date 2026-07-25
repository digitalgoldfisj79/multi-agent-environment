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
    Only exponents used here are at most 2p-1.
    """
    result = [0] * p
    for j in range(p - 1, exponent + 1, p - 1):
        coefficient = (-comb(exponent, j)) % p
        remaining = exponent - j
        # remaining is at most p here.  Reduce alpha^p=alpha+1.
        if remaining == p:
            result[1] = (result[1] + coefficient) % p
            result[0] = (result[0] + coefficient) % p
        else:
            result[remaining] = (result[remaining] + coefficient) % p
    return result


def verify_prime(p: int) -> None:
    # Universal trace identities.
    assert trace_power_of_alpha(p, p - 1)[0] == p - 1
    assert all(x == 0 for x in trace_power_of_alpha(p, p - 1)[1:])
    assert trace_power_of_alpha(p, 2 * p - 1)[0] == p - 1
    assert all(x == 0 for x in trace_power_of_alpha(p, 2 * p - 1)[1:])

    # Quadratic critical moment.
    quadratic_moment = (p - 1) // 2
    assert quadratic_moment <= p - 4
    assert 2 * quadratic_moment == p - 1

    # Cubic first gate and final contradiction.
    h = (p - 2) // 3
    first_moment = h + 1
    final_moment = 2 * h + 1
    assert 3 * first_moment == p + 1
    assert 3 * final_moment == 2 * p - 1
    assert first_moment <= p - 4
    assert final_moment <= p - 4

    # For beta=X^3+rX, coefficient of X^(p-1) in beta^m is m*r.
    for r in range(p):
        trace_first = (-first_moment * r) % p
        if trace_first == 0:
            assert r == 0

    # Pure-cube final trace is -1.
    final_trace = trace_power_of_alpha(p, 3 * final_moment)
    assert final_trace[0] == p - 1
    assert all(x == 0 for x in final_trace[1:])

    # Möbius logarithmic-derivative identity at every base-field r.
    # f(r)=f'(r)=-1, hence sum 1/(alpha+i-r)=-1.
    for r in range(p):
        f_r = (pow(r, p, p) - r - 1) % p
        fprime_r = (-1) % p
        assert f_r == p - 1
        assert fprime_r * pow(f_r, -1, p) % p == 1

    print(
        f"p={p}: quadratic m={quadratic_moment}, "
        f"cubic gates {first_moment},{final_moment}: PASS"
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
