#!/usr/bin/env python3
"""Exact audit of the observed p-adic valuation signal for committed T_p values.

This script does not compute new exponential sums. It checks the exact values already
committed in COLLAPSE_LEMMA.md and records v_p(T_p), the residual unit U_p, and the
exponent gap to the desired archimedean square-root scale.
"""

EXACT_T = {
    5: 0,
    11: 322102,
    17: 11899821517,
    23: -1010446643080743,
    29: -798145148362709627351,
}


def valuation(n: int, p: int):
    if n == 0:
        return None
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v, n


if __name__ == "__main__":
    for p, T in EXACT_T.items():
        if T == 0:
            print(f"p={p}: T_p=0; valuation infinite")
            continue
        v, unit_abs = valuation(T, p)
        predicted = (p + 4) // 3
        assert 3 * predicted == p + 4
        status = "MATCH" if v == predicted else "MISMATCH"
        signed_unit = T // (p ** v)
        target_exp = (p - 1) / 2
        gap = target_exp - v
        print(
            f"p={p}: v_p(T_p)={v}, predicted=(p+4)/3={predicted}: {status}; "
            f"U_p={signed_unit}; target exponent gap={gap:g}"
        )

    for p in (11, 17, 23, 29):
        assert valuation(EXACT_T[p], p)[0] == (p + 4) // 3

    print("ALL AVAILABLE NONZERO p=2 mod 3 EXACT VALUES MATCH THE SLOPE SIGNAL")
