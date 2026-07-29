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


def coefficient(P: int, d: int) -> Fraction:
    return Fraction(int(totient(P)), P) * Fraction(int(mobius(d)), int(totient(d)))


def interval_bounds(P: int, Z: int, H: int, q: int) -> tuple[int, int]:
    return (P + Z) // q + 1, (P + H) // q


def rough_count(P: int, base: int, Z: int, H: int, q: int) -> int:
    lo, hi = interval_bounds(P, Z, H, q)
    return sum(1 for k in range(lo, hi + 1) if math.gcd(k, base) == 1)


def projector_count(P: int, base: int, Z: int, H: int, q: int) -> Fraction:
    lo, hi = interval_bounds(P, Z, H, q)
    total = Fraction(0)
    for d0 in divisors(base):
        d = int(d0)
        total += coefficient(base, d) * sum(ramanujan_sum(d, k) for k in range(lo, hi + 1))
    return total


def qd_fourier_count(P: int, base: int, Z: int, H: int, q: int) -> complex:
    delta = Fraction(int(totient(base)), base)
    total = 0j
    for d0 in divisors(base):
        d = int(d0)
        scalar = float(delta * Fraction(int(mobius(d)), int(totient(d)))) / q
        for h in range(q * d):
            if math.gcd(h, d) != 1:
                continue
            source = sum(cmath.exp(2j * math.pi * h * m / (q * d)) for m in range(Z + 1, H + 1))
            total += scalar * cmath.exp(2j * math.pi * h * P / (q * d)) * source
    return total


def conductor_panel(z: int) -> dict:
    P = primorial(z)
    delta = Fraction(int(totient(P)), P)
    coeffs = [(int(d), coefficient(P, int(d))) for d in divisors(P)]
    assert sum(abs(lam) for _, lam in coeffs) == 1
    assert sum(lam * lam * int(totient(d)) for d, lam in coeffs) == delta
    assert all(lam * lam * int(totient(d)) == delta * abs(lam) for d, lam in coeffs)

    tails = []
    for A in (1, 2, 3, 4):
        cutoff = z**A
        l1_tail = sum(abs(lam) for d, lam in coeffs if d > cutoff)
        energy_tail = sum(lam * lam * int(totient(d)) for d, lam in coeffs if d > cutoff)
        assert energy_tail == delta * l1_tail
        tails.append({
            "A": A,
            "cutoff": cutoff,
            "l1_tail": str(l1_tail),
            "normalized_energy_tail": str(energy_tail / delta),
        })

    pointwise = None
    if P <= 30030:
        A = 2
        cutoff = z**A
        values = []
        for k in range(P):
            tail = sum(lam * ramanujan_sum(d, k) for d, lam in coeffs if d > cutoff)
            values.append(tail)
        mean_square = sum(v * v for v in values) / P
        predicted = sum(lam * lam * int(totient(d)) for d, lam in coeffs if d > cutoff)
        assert mean_square == predicted
        pointwise = {
            "A": A,
            "maximum_absolute_tail": float(max(abs(v) for v in values)),
            "complete_period_mean_square": float(mean_square),
        }

    return {
        "z": z,
        "P": P,
        "rough_density": str(delta),
        "coefficient_l1": "1",
        "weighted_quadratic_mass": str(delta),
        "tails": tails,
        "pointwise_tail_diagnostic": pointwise,
    }


def block_panel(X: int) -> dict:
    H = 4 * X * X // 5
    zs = [int(p) for p in primerange(X, 2 * X)]
    K = max(1, math.isqrt(X))
    blocks = []
    max_fourier_error = 0.0
    for start in range(0, len(zs), K):
        local = zs[start : start + K]
        base_z = local[0]
        base = primorial(base_z)
        Z = local[-1]
        checks = 0
        for z in local:
            P = primorial(z)
            for q0 in primerange(Z + 1, H + 1):
                q = int(q0)
                moving = rough_count(P, P, Z, H, q)
                frozen = rough_count(P, base, Z, H, q)
                projected = projector_count(P, base, Z, H, q)
                assert moving == frozen == projected
                checks += 1
                if X == 7 and q < 20:
                    max_fourier_error = max(max_fourier_error, abs(qd_fourier_count(P, base, Z, H, q) - moving))
        blocks.append({
            "start_index": start,
            "block_size": len(local),
            "base_z": base_z,
            "Z": Z,
            "checked_modulus_centre_pairs": checks,
            "common_base_projector_exact": True,
        })
    return {
        "X": X,
        "H": H,
        "K": K,
        "blocks": blocks,
        "maximum_joint_qd_fourier_error": max_fourier_error,
    }


def truncation_energy_panel(X: int) -> dict:
    H = 4 * X * X // 5
    zs = [int(p) for p in primerange(X, 2 * X)]
    K = max(1, math.isqrt(X))
    records = []
    for start in range(0, len(zs), K):
        local = zs[start : start + K]
        base = primorial(local[0])
        Z = local[-1]
        moduli = [int(q) for q in primerange(Z + 1, H + 1)]
        M = len(moduli)
        coeffs = [(int(d), coefficient(base, int(d))) for d in divisors(base)]
        for A in (1, 2, 3):
            D = X**A
            full_energy = Fraction(0)
            low_energy = Fraction(0)
            tail_energy = Fraction(0)
            twice_cross = Fraction(0)
            for z in local:
                P = primorial(z)
                low_sum = Fraction(0)
                tail_sum = Fraction(0)
                for q in moduli:
                    lo, hi = interval_bounds(P, Z, H, q)
                    low = Fraction(0)
                    tail = Fraction(0)
                    for d, lam in coeffs:
                        value = lam * sum(ramanujan_sum(d, k) for k in range(lo, hi + 1))
                        if d <= D:
                            low += value
                        else:
                            tail += value
                    weight = Fraction(q - 1, q - 2)
                    low_sum += weight * (low - Fraction(M - 1, q - 1))
                    tail_sum += weight * tail
                full = low_sum + tail_sum
                full_energy += full * full
                low_energy += low_sum * low_sum
                tail_energy += tail_sum * tail_sum
                twice_cross += 2 * low_sum * tail_sum
            assert full_energy == low_energy + tail_energy + twice_cross
            records.append({
                "start_index": start,
                "block_size": len(local),
                "A": A,
                "cutoff": D,
                "full_energy": float(full_energy),
                "low_energy": float(low_energy),
                "tail_energy": float(tail_energy),
                "twice_cross": float(twice_cross),
                "tail_to_full_ratio": float(tail_energy / full_energy) if full_energy else 0.0,
            })
    return {"X": X, "records": records}


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "conductor_panels": [conductor_panel(z) for z in (5, 7, 11, 13, 17, 19)],
            "common_base_panels": [block_panel(X) for X in (7, 11, 13, 17)],
        },
        "empirical": {
            "truncation_energy_panels": [truncation_energy_panel(X) for X in (7, 11, 13, 17)],
            "qualification": "Low/high conductor block energies are diagnostics only; truncation is not a monotone contraction.",
        },
        "boundary": (
            "The common-base projector and conductor probability law are exact. "
            "Conductor concentration is a complete-period/model-energy statement; it does not by itself "
            "bound the deterministic moving intervals. The joint sampling-transfer theorem remains open."
        ),
    }
    output = Path(__file__).with_name("common_base_conductor_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
