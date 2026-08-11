#!/usr/bin/env python3
"""Exact finite audit of the two-level Heath--Brown identity and punctured-centre collapse."""
from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def divisors(n: int) -> list[int]:
    values = [1]
    for p, exponent in factor(n).items():
        values = [d * p**a for d in values for a in range(exponent + 1)]
    return sorted(values)


def mobius(n: int) -> int:
    f = factor(n)
    if any(exponent > 1 for exponent in f.values()):
        return 0
    return -1 if len(f) % 2 else 1


def log_signature(n: int) -> Counter[int]:
    return Counter(factor(n))


def add_signature(target: Counter[int], source: Counter[int], coefficient: int) -> None:
    for p, exponent in source.items():
        target[p] += coefficient * exponent
        if target[p] == 0:
            del target[p]


def lambda_signature(n: int) -> Counter[int]:
    f = factor(n)
    if len(f) == 1:
        p = next(iter(f))
        return Counter({p: 1})
    return Counter()


def hb_two_level_signature(n: int, Y: int) -> Counter[int]:
    """2 mu_<=Y * log - mu_<=Y * mu_<=Y * 1 * log."""
    out: Counter[int] = Counter()
    for d in divisors(n):
        if d <= Y:
            mu_d = mobius(d)
            if mu_d:
                add_signature(out, log_signature(n // d), 2 * mu_d)

    for d1 in divisors(n):
        if d1 > Y or not mobius(d1):
            continue
        rem1 = n // d1
        for d2 in divisors(rem1):
            if d2 > Y or not mobius(d2):
                continue
            rem2 = rem1 // d2
            for e in divisors(rem2):
                ell = rem2 // e
                add_signature(out, log_signature(ell), -mobius(d1) * mobius(d2))
    return out


def hb_reduced_signature(n: int, Y: int) -> Counter[int]:
    """mu_<=Y * log + mu_<=Y * mu_>Y * 1 * log."""
    out: Counter[int] = Counter()
    for d in divisors(n):
        if d <= Y and mobius(d):
            add_signature(out, log_signature(n // d), mobius(d))

    for d in divisors(n):
        if d > Y or not mobius(d):
            continue
        rem = n // d
        for a in divisors(rem):
            if a <= Y or not mobius(a):
                continue
            rem2 = rem // a
            for e in divisors(rem2):
                ell = rem2 // e
                add_signature(out, log_signature(ell), mobius(d) * mobius(a))
    return out


def primorial_below(X: int, primes: list[int]) -> int:
    value = 1
    for p in primes:
        if p >= X:
            break
        value *= p
    return value


def panel(X: int, eta_num: int = 4, eta_den: int = 5) -> dict:
    H = eta_num * X * X // eta_den
    Y = math.isqrt(H)
    if Y * Y < H:
        Y += 1
    assert H <= Y * Y
    assert Y < X

    primes = primes_upto(max(H, 2 * X))
    P = primorial_below(X, primes)
    band = [p for p in primes if X < p <= min(2 * X, H)]

    identity_checks = 0
    two_level_tuples = 0
    reduced_tuples = 0
    overlap_tuples = 0
    punctured_checks = 0

    for n in range(1, H + 1):
        expected = lambda_signature(n)
        assert hb_two_level_signature(n, Y) == expected
        assert hb_reduced_signature(n, Y) == expected
        identity_checks += 1

        for d1 in divisors(n):
            if d1 > Y or not mobius(d1):
                continue
            rem1 = n // d1
            for d2 in divisors(rem1):
                if d2 > Y or not mobius(d2):
                    continue
                rem2 = rem1 // d2
                for _ in divisors(rem2):
                    two_level_tuples += 1
                    if math.gcd(d1, d2) > 1:
                        overlap_tuples += 1

        for d in divisors(n):
            if d > Y or not mobius(d):
                continue
            reduced_tuples += 1
            rem = n // d
            for a in divisors(rem):
                if a <= Y or not mobius(a):
                    continue
                reduced_tuples += len(divisors(rem // a))

    nonzero_small = [d for d in range(1, Y + 1) if mobius(d)]
    for d in nonzero_small:
        assert P % d == 0
        for p in band:
            assert (d * pow(P, -1, p) - pow(P // d, -1, p)) % p == 0
            punctured_checks += 1

    prime_power_correction = 0
    for n in range(2, H + 1):
        f = factor(n)
        if len(f) == 1 and next(iter(f.values())) >= 2:
            prime_power_correction += 1

    return {
        "X": X,
        "H": H,
        "Y": Y,
        "Y_below_X": True,
        "identity_values_checked": identity_checks,
        "two_level_factor_tuples": two_level_tuples,
        "two_level_overlap_tuples": overlap_tuples,
        "reduced_identity_terms": reduced_tuples,
        "punctured_centre_checks": punctured_checks,
        "prime_power_correction_count": prime_power_correction,
        "band_moduli": band,
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact_identities": [
            "Lambda = 2 mu_<=Y * log - mu_<=Y * mu_<=Y * 1 * log for n <= H <= Y^2",
            "Lambda = mu_<=Y * log + mu_<=Y * mu_>Y * 1 * log for n <= H",
            "d P_j^{-1} = (P_j/d)^{-1} mod p for squarefree d <= Y < X < p",
        ],
        "panels": [panel(X) for X in (11, 17, 23, 29, 37)],
        "boundary": (
            "The provisional three-small-variable source identity is unnecessary.  The exact "
            "two-level identity resums to a source with one small Mobius variable, which divides "
            "every primorial centre.  Prime powers remain an explicit sparse correction."
        ),
    }
    output = Path(__file__).with_name("prime_source_heath_brown_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
