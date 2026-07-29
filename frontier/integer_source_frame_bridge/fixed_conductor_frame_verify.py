#!/usr/bin/env python3
from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import divisors, mobius, primerange, totient


def primorial(z: int) -> int:
    value = 1
    for p in primerange(2, z + 1):
        value *= int(p)
    return value


def ramanujan_sum(d: int, k: int) -> int:
    g = math.gcd(d, k)
    return int(mobius(d // g)) * int(totient(d)) // int(totient(d // g))


def direct_gram(Pj: int, Pk: int, d: int, moduli: list[int]) -> complex:
    total = 0j
    phi = int(totient(d))
    for q in moduli:
        for h in range(q * d):
            if math.gcd(h, d) != 1:
                continue
            total += cmath.exp(2j * math.pi * h * (Pj - Pk) / (q * d)) / (q * q * phi)
    return total


def expected_gram(Pj: int, Pk: int, moduli: list[int]) -> Fraction:
    delta = Pj - Pk
    if delta == 0:
        return sum((Fraction(1, q) for q in moduli), Fraction(0))
    return sum((Fraction(1, q) for q in moduli if delta % q == 0), Fraction(0))


def source_energy_direct(Z: int, H: int, q: int, d: int) -> float:
    total = 0.0
    for h in range(q * d):
        if math.gcd(h, d) != 1:
            continue
        W = sum(cmath.exp(2j * math.pi * h * m / (q * d)) for m in range(Z + 1, H + 1))
        total += abs(W) ** 2
    return total


def source_energy_expected(Z: int, H: int, q: int, d: int) -> int:
    L = H - Z
    total = 0
    bound = (L - 1) // q
    for t in range(-bound, bound + 1):
        if abs(q * t) < L:
            total += q * (L - abs(q * t)) * ramanujan_sum(d, t)
    return total


def panel(X: int) -> dict:
    H = 4 * X * X // 5
    zs = [int(p) for p in primerange(X, 2 * X)]
    K = max(1, math.isqrt(X))
    records = []
    max_gram_error = 0.0
    max_source_error = 0.0
    for start in range(0, len(zs), K):
        local = zs[start : start + K]
        base = primorial(local[0])
        Z = local[-1]
        moduli = [int(q) for q in primerange(Z + 1, min(H, 2 * Z) + 1)]
        conductors = [int(d) for d in divisors(base) if int(d) <= max(30, X * X)][:12]
        for d in conductors:
            for zj in local:
                for zk in local:
                    Pj = primorial(zj)
                    Pk = primorial(zk)
                    direct = direct_gram(Pj, Pk, d, moduli)
                    expected = float(expected_gram(Pj, Pk, moduli))
                    max_gram_error = max(max_gram_error, abs(direct - expected))
            for q in moduli[:3]:
                direct_e = source_energy_direct(Z, H, q, d)
                expected_e = source_energy_expected(Z, H, q, d)
                max_source_error = max(max_source_error, abs(direct_e - expected_e))
        records.append({
            "start_index": start,
            "block_size": len(local),
            "base_z": local[0],
            "Z": Z,
            "modulus_count": len(moduli),
            "conductor_count": len(conductors),
        })
    assert max_gram_error < 1e-8
    assert max_source_error < 1e-7
    return {
        "X": X,
        "H": H,
        "records": records,
        "maximum_gram_error": max_gram_error,
        "maximum_source_energy_error": max_source_error,
    }


def interval_fourier_panel() -> dict:
    rows = []
    for M, L in ((30, 7), (30, 44), (77, 123)):
        values = []
        for h in range(1, M):
            W = sum(cmath.exp(2j * math.pi * h * m / M) for m in range(1, L + 1))
            values.append(abs(W) ** 2)
        direct = sum(values)
        r = L % M
        expected = r * (M - r)
        assert abs(direct - expected) < 1e-8
        rows.append({"M": M, "L": L, "remainder": r, "nonzero_energy": expected})
    return {"rows": rows}


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "hybrid_frame_panels": [panel(X) for X in (7, 11, 13)],
            "interval_fourier_energy": interval_fourier_panel(),
        },
        "boundary": (
            "The fixed-conductor centre Gram and Fejer-Ramanujan source-energy identities are exact. "
            "The joint cross-conductor sampling theorem remains open."
        ),
    }
    output = Path(__file__).with_name("fixed_conductor_frame_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
