#!/usr/bin/env python3
"""Exact finite verification of selected primorial residue multiplicities."""
from __future__ import annotations

from collections import Counter


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def main() -> None:
    for x in (20, 30, 50, 80):
        primes = primes_upto(20 * x)
        rows = [p for p in primes if x <= p < 2 * x]
        moduli = [q for q in primes if 2 * x < q <= 20 * x]

        residues: dict[int, list[int]] = {q: [] for q in moduli}
        running = {q: 1 for q in moduli}
        row_set = set(rows)
        for p in primes:
            if p > rows[-1]:
                break
            for q in moduli:
                running[q] = (running[q] * p) % q
            if p in row_set:
                for q in moduli:
                    residues[q].append(running[q])

        total_collisions = 0
        multiplicity_energy = 0
        for q in moduli:
            counts = Counter(residues[q])
            multiplicity_energy += sum(v * v for v in counts.values())
            total_collisions += sum(v * (v - 1) // 2 for v in counts.values())

        pair_distance_budget = 0
        for j in range(len(rows)):
            pair_collision_count = 0
            for k in range(j + 1, len(rows)):
                distance = k - j
                collisions = sum(
                    residues[q][j] == residues[q][k] for q in moduli
                )
                assert collisions < distance
                pair_collision_count += collisions
                pair_distance_budget += distance
            assert pair_collision_count <= sum(range(1, len(rows) - j))

        exact_energy = len(rows) * len(moduli) + 2 * total_collisions
        assert multiplicity_energy == exact_energy
        assert total_collisions <= pair_distance_budget
        print(
            f"X={x} rows={len(rows)} moduli={len(moduli)} "
            f"collisions={total_collisions} distance_budget={pair_distance_budget} "
            f"energy={multiplicity_energy}"
        )

    print("FORTUNE_INT_SCME_M4_COLLISION_MULTIPLICITY_PASS")


if __name__ == "__main__":
    main()
