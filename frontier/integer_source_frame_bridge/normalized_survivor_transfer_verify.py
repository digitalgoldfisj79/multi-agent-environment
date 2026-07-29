#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import primerange


def primorial(z: int) -> int:
    value = 1
    for p in primerange(2, z + 1):
        value *= int(p)
    return value


def inv_v(primes: list[int]) -> Fraction:
    value = Fraction(1)
    for r in primes:
        value *= Fraction(r - 1, r - 2)
    return value


def normalized_survivor(n: int, primes: list[int]) -> Fraction:
    if any(n % r == 0 for r in primes):
        return Fraction(0)
    return inv_v(primes)


def exact_local_panel() -> dict:
    bands = [[7, 11], [13]]
    all_primes = [r for band in bands for r in band]
    modulus = math.prod(all_primes)
    residues = [a for a in range(modulus) if all(a % r != 1 for r in all_primes)]
    increments: list[list[Fraction]] = []
    previous: list[int] = []
    for band in bands:
        before = [normalized_survivor(a, previous) for a in residues]
        previous = previous + band
        after = [normalized_survivor(a, previous) for a in residues]
        increments.append([y - x for x, y in zip(before, after)])
    means = [sum(row, Fraction(0)) / len(residues) for row in increments]
    cross = sum(x * y for x, y in zip(increments[0], increments[1])) / len(residues)
    final = [normalized_survivor(a, all_primes) - 1 for a in residues]
    qv = sum(sum(x * x for x in row) / len(residues) for row in increments)
    energy = sum(x * x for x in final) / len(residues)
    assert means == [0, 0]
    assert cross == 0
    assert qv == energy
    return {
        "bands": bands,
        "sample_size": len(residues),
        "increment_means": [str(x) for x in means],
        "cross_covariance": str(cross),
        "quadratic_variation": str(qv),
        "final_energy": str(energy),
    }


def top_tail_panel(X: int) -> dict:
    H = 4 * X * X // 5
    zs = [int(p) for p in primerange(X, 2 * X)]
    rows = []
    for z in zs:
        P = primorial(z)
        Y = math.isqrt(P + H)
        candidates = [int(m) for m in primerange(z + 1, H + 1)]
        physical = [int(r) for r in primerange(z + 1, min(H, Y) + 1)]
        tail = [int(r) for r in primerange(H + 1, Y + 1)] if Y > H else []
        A = inv_v(tail)
        total = Fraction(0)
        drift = Fraction(0)
        hit = Fraction(0)
        hit_offsets = 0
        for m in candidates:
            n = P + m
            M_H = normalized_survivor(n, physical)
            has_tail_hit = any(n % r == 0 for r in tail)
            if has_tail_hit:
                hit_offsets += 1
            d = M_H * (A - 1)
            h = -M_H * A if has_tail_hit else Fraction(0)
            b = normalized_survivor(n, physical + tail) - M_H
            assert b == d + h
            total += b
            drift += d
            hit += h
        assert total == drift + hit
        rows.append({
            "z": z,
            "P": P,
            "Y": Y,
            "candidate_count": len(candidates),
            "tail_prime_count": len(tail),
            "tail_hit_offsets": hit_offsets,
            "total_increment": float(total),
            "drift_component": float(drift),
            "hit_component": float(hit),
            "twice_drift_hit": float(2 * drift * hit),
        })
    total_energy = sum(row["total_increment"] ** 2 for row in rows)
    drift_energy = sum(row["drift_component"] ** 2 for row in rows)
    hit_energy = sum(row["hit_component"] ** 2 for row in rows)
    cross = sum(row["twice_drift_hit"] for row in rows)
    return {
        "X": X,
        "H": H,
        "rows": rows,
        "block_total_energy": total_energy,
        "block_drift_energy": drift_energy,
        "block_hit_energy": hit_energy,
        "block_twice_cross": cross,
        "drift_plus_hit_identity": abs(total_energy - drift_energy - hit_energy - cross) < 1e-8,
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {"complete_crt_survivor_martingale": exact_local_panel()},
        "empirical": {
            "top_tail_drift_hit_panels": [top_tail_panel(X) for X in (7, 11, 13)],
            "qualification": (
                "The top-tail drift/hit split is exact on each finite row; block energies are empirical. "
                "They test whether sparse hit support can be bounded independently of normalization drift."
            ),
        },
        "boundary": (
            "Normalized survivor increments are exact martingale differences under complete CRT sampling. "
            "On the deterministic Fortune source the sparse hit term must remain coupled to its dense normalization drift."
        ),
    }
    output = Path(__file__).with_name("normalized_survivor_transfer_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
