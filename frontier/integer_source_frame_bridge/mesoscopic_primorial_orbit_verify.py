#!/usr/bin/env python3
"""Verify the mesoscopic primorial orbit kernel and collision bounds."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


def prime_sieve(n: int) -> tuple[bytearray, list[int]]:
    flags = bytearray(b"\x01") * (n + 1)
    flags[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            flags[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return flags, [value for value in range(2, n + 1) if flags[value]]


def direct_additive_sum(r: int, difference: int) -> complex:
    residue = difference % r
    return sum(cmath.exp(2j * math.pi * a * residue / r) for a in range(1, r))


def panel(X: int, eta: float = 0.8) -> dict:
    H = int(eta * X * X)
    _, primes = prime_sieve(H)
    block_primes = [p for p in primes if X <= p < 2 * X]
    K = max(1, math.isqrt(X))

    P = 1
    for p in primes:
        if p > block_primes[0]:
            break
        P *= p
    centres: list[int] = []
    current = P
    for index, z in enumerate(block_primes):
        if index == 0:
            centres.append(current)
        else:
            current *= z
            centres.append(current)

    rows = []
    maximum_formula_error = 0.0
    maximum_collision_count_ratio = 0.0
    maximum_schur_ratio = 0.0

    for start in range(0, len(centres), K):
        stop = min(len(centres), start + K)
        local_centres = centres[start:stop]
        local_z = block_primes[start:stop]
        zB = local_z[-1]
        moduli = [r for r in primes if zB < r <= H]
        diagonal = math.fsum((r - 1) / (r * r) for r in moduli)
        square_tail = math.fsum(1 / (r * r) for r in moduli)
        log_ratio = math.log(2 * X) / math.log(X)
        theoretical = diagonal + len(local_centres) * square_tail + (
            log_ratio * len(local_centres) * max(0, len(local_centres) - 1) / X
        )

        kernel = [[0.0] * len(local_centres) for _ in local_centres]
        for a in range(len(local_centres)):
            kernel[a][a] = diagonal
            qproduct = 1
            for b in range(a + 1, len(local_centres)):
                qproduct *= local_z[b]
                collisions = [r for r in moduli if qproduct % r == 1]
                count_bound = math.log(max(2, qproduct - 1)) / math.log(X)
                assert len(collisions) <= count_bound + 1e-12
                if count_bound:
                    maximum_collision_count_ratio = max(
                        maximum_collision_count_ratio, len(collisions) / count_bound
                    )
                value = -square_tail + math.fsum(1 / r for r in collisions)
                kernel[a][b] = value
                kernel[b][a] = value

                difference = local_centres[a] - local_centres[b]
                for r in moduli[: min(3, len(moduli))]:
                    direct = direct_additive_sum(r, difference) / (r * r)
                    formula = (-1 / (r * r)) + (1 / r if difference % r == 0 else 0)
                    maximum_formula_error = max(maximum_formula_error, abs(direct - formula))

        row_sums = [math.fsum(abs(x) for x in row) for row in kernel]
        maximum_row_sum = max(row_sums, default=0.0)
        assert maximum_row_sum <= theoretical + 1e-10
        if theoretical:
            maximum_schur_ratio = max(maximum_schur_ratio, maximum_row_sum / theoretical)

        rows.append(
            {
                "start_index": start,
                "block_size": len(local_centres),
                "z_min": local_z[0],
                "z_max": local_z[-1],
                "modulus_count": len(moduli),
                "diagonal": diagonal,
                "maximum_absolute_row_sum": maximum_row_sum,
                "theoretical_schur_bound": theoretical,
                "row_sum_to_bound_ratio": maximum_row_sum / theoretical if theoretical else 0.0,
            }
        )

    boundary_budget_ratio = K * K * X / (H if H else 1)
    assert boundary_budget_ratio <= 2.0
    assert maximum_formula_error < 2e-10

    return {
        "X": X,
        "H": H,
        "N": len(centres),
        "K": K,
        "boundary_budget_ratio_K2X_over_H": boundary_budget_ratio,
        "maximum_formula_error": maximum_formula_error,
        "maximum_collision_count_ratio": maximum_collision_count_ratio,
        "maximum_schur_ratio": maximum_schur_ratio,
        "blocks": rows,
    }


def main() -> None:
    panels = [panel(X) for X in (101, 211, 503)]
    payload = {
        "status": "PASS",
        "scope": "mesoscopic primorial collision kernel and Schur bound",
        "panels": panels,
        "boundary": (
            "The verifier checks the orbit frame and cutoff budget only; "
            "the joint common-source bilinear estimate remains OPEN."
        ),
    }
    output = Path(__file__).with_name("mesoscopic_primorial_orbit_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
