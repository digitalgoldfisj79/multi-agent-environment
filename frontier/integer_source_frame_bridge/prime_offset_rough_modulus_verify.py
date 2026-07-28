#!/usr/bin/env python3
"""Verify candidate roughness and the exact prime-modulus/large-divisor split."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import divisors, factorint, isprime, mobius, nextprime, primerange


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def one_case(pj: int, H: int) -> dict:
    P = 1
    for q in primerange(2, pj + 1):
        P *= int(q)
    pnext = int(nextprime(pj))
    assert H < pnext * pnext

    direct = 0.0
    small = 0.0
    large = 0.0
    checked_divisors = 0
    max_error = 0.0
    for p in primerange(pj + 1, H + 1):
        p = int(p)
        n = P + p
        assert math.gcd(n, P) == 1
        direct_term = math.log(p) * von_mangoldt(n)
        small_term = 0.0
        large_term = 0.0
        for d0 in divisors(n):
            d = int(d0)
            if mobius(d) == 0:
                continue
            coeff = -float(mobius(d)) * math.log(d)
            if d <= H:
                if d > 1:
                    assert isprime(d), (pj, H, p, n, d, factorint(d))
                    assert d > pj
                    small_term += math.log(p) * math.log(d)
                checked_divisors += 1
            else:
                large_term += math.log(p) * coeff
        err = abs(direct_term - small_term - large_term)
        max_error = max(max_error, err)
        assert err < 2e-10, (p, n, direct_term, small_term, large_term)
        direct += direct_term
        small += small_term
        large += large_term

    return {
        "p_j": pj,
        "P_j": P,
        "p_next": pnext,
        "H": H,
        "prime_offset_count": len(list(primerange(pj + 1, H + 1))),
        "checked_small_squarefree_divisors": checked_divisors,
        "direct_source": direct,
        "small_prime_modulus_source": small,
        "large_divisor_source": large,
        "split_error": abs(direct - small - large),
        "maximum_per_offset_error": max_error,
    }


def main() -> None:
    rows = [one_case(11, 150), one_case(13, 200), one_case(17, 400)]
    for row in rows:
        assert row["split_error"] < 3e-10
        assert row["maximum_per_offset_error"] < 2e-10
    payload = {
        "status": "PASS",
        "scope": "prime-offset roughness and exact prime-modulus/large-divisor split",
        "rows": rows,
        "boundary": "Finite exact verification only; joint signed covariance remains open.",
    }
    Path(__file__).with_name("prime_offset_rough_modulus_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
