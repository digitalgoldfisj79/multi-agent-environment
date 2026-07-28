#!/usr/bin/env python3
"""Verify the squarefree small-modulus one-new-prime decomposition."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import factorint, isprime, mobius, nextprime, primerange


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def one_case(pj: int, H: int) -> dict:
    P = 1
    for p in primerange(2, pj + 1):
        P *= int(p)
    pnext = int(nextprime(pj))
    assert H < pnext * pnext
    weights = {m: 1.0 + 0.1 * math.cos(m) for m in range(2, H + 1)}

    direct = 0.0
    smooth = 0.0
    new_prime = 0.0
    classified = 0
    for d in range(1, H + 1):
        mud = int(mobius(d))
        if mud == 0:
            continue
        incidence = sum(w for m, w in weights.items() if (P + m) % d == 0)
        direct += -mud * math.log(d) * incidence
        factors = [int(p) for p in factorint(d)]
        large = [p for p in factors if p > pj]
        assert len(large) <= 1, (pj, H, d, factors)
        if not large:
            assert P % d == 0
            expected = sum(w for m, w in weights.items() if m % d == 0)
            assert abs(incidence - expected) < 2e-12
            smooth += -mud * math.log(d) * expected
        else:
            q = large[0]
            assert isprime(q)
            s = d // q
            assert P % s == 0 and s <= H // q
            expected = sum(
                w
                for m, w in weights.items()
                if m % s == 0 and ((P // s) + (m // s)) % q == 0
            )
            assert abs(incidence - expected) < 2e-12
            new_prime += int(mobius(s)) * (math.log(q) + math.log(s)) * expected
        classified += 1

    smooth_sharp = 0.0
    gcd_form = 0.0
    for d in range(1, H + 1):
        if P % d == 0 and mobius(d) != 0:
            smooth_sharp += -int(mobius(d)) * math.log(d) * sum(
                1 for m in range(2, H + 1) if m % d == 0
            )
    for m in range(2, H + 1):
        gcd_form += von_mangoldt(math.gcd(m, P))

    return {
        "p_j": pj,
        "P_j": P,
        "p_next": pnext,
        "H": H,
        "classified_squarefree_moduli": classified,
        "direct_weighted_small_source": direct,
        "smooth_weighted_source": smooth,
        "one_new_prime_weighted_source": new_prime,
        "weighted_decomposition_error": abs(direct - smooth - new_prime),
        "smooth_sharp_source": smooth_sharp,
        "gcd_form": gcd_form,
        "smooth_gcd_error": abs(smooth_sharp - gcd_form),
    }


def main() -> None:
    rows = [one_case(11, 150), one_case(13, 200), one_case(17, 350)]
    for row in rows:
        assert row["weighted_decomposition_error"] < 3e-10
        assert row["smooth_gcd_error"] < 3e-10
    payload = {
        "status": "PASS",
        "scope": "small squarefree moduli: smooth or one new prime",
        "rows": rows,
        "boundary": "Exact finite identities only; signed dispersion remains open.",
    }
    Path(__file__).with_name("small_modulus_one_new_prime_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
