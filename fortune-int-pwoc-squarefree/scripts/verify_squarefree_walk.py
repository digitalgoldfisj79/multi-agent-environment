#!/usr/bin/env python3
"""Exact finite regressions for the INT-PWOC-SF build."""
from __future__ import annotations

import cmath
import math
from dataclasses import dataclass


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [i for i, value in enumerate(sieve) if value]


def squarefree_factors(n: int, primes: list[int]) -> tuple[int, ...] | None:
    factors: list[int] = []
    value = n
    for p in primes:
        if p * p > value:
            break
        if value % p == 0:
            exponent = 0
            while value % p == 0:
                exponent += 1
                value //= p
            if exponent > 1:
                return None
            factors.append(p)
    if value > 1:
        factors.append(value)
    return tuple(factors)


@dataclass(frozen=True)
class Panel:
    X: int
    Q: int
    rows: tuple[int, ...]
    centres: tuple[int, ...]
    moduli: tuple[tuple[int, tuple[int, ...]], ...]


def build_panel(X: int, Q: int, max_order: int = 2) -> Panel:
    primes = primes_upto(Q)
    rows = tuple(p for p in primes if X <= p < 2 * X)
    assert len(rows) >= 2
    row_set = set(rows)
    accumulator = 1
    centres: list[int] = []
    for p in primes:
        if p > rows[-1]:
            break
        accumulator *= p
        if p in row_set:
            centres.append(accumulator)
    moduli: list[tuple[int, tuple[int, ...]]] = []
    for q in range(2, Q + 1):
        factors = squarefree_factors(q, primes)
        if factors and len(factors) <= max_order and all(p > 2 * X for p in factors):
            moduli.append((q, factors))
    return Panel(X, Q, rows, tuple(centres), tuple(moduli))


def weight(q: int, profile: str) -> float:
    if profile == "inverse":
        return 1.0 / q
    if profile == "inverse_square":
        return 1.0 / (q * q)
    raise ValueError(profile)


def direct_energy(panel: Panel, coefficients: tuple[complex, ...], profile: str) -> float:
    total = 0.0
    for q, _ in panel.moduli:
        residues = [centre % q for centre in panel.centres]
        modulus_energy = 0.0
        for c in range(q):
            value = sum(
                a * cmath.exp(2j * math.pi * c * residue / q)
                for a, residue in zip(coefficients, residues, strict=True)
            )
            modulus_energy += abs(value) ** 2
        total += weight(q, profile) * modulus_energy
    return total


def kernel_energy(panel: Panel, coefficients: tuple[complex, ...], profile: str) -> float:
    total = 0j
    for q, _ in panel.moduli:
        residues = [centre % q for centre in panel.centres]
        beta_q_q = weight(q, profile) * q
        for j, a_j in enumerate(coefficients):
            for k, a_k in enumerate(coefficients):
                if residues[j] == residues[k]:
                    total += beta_q_q * a_j * a_k.conjugate()
    assert abs(total.imag) <= 1e-8 * max(1.0, abs(total.real))
    return total.real


def schur_bound(
    panel: Panel, coefficients: tuple[complex, ...], profile: str
) -> tuple[float, float, float]:
    diagonal = sum(weight(q, profile) * q for q, _ in panel.moduli)
    row_sums: list[float] = []
    for j, centre_j in enumerate(panel.centres):
        row_total = 0.0
        for k, centre_k in enumerate(panel.centres):
            if j == k:
                continue
            difference = abs(centre_j - centre_k)
            row_total += sum(
                weight(q, profile) * q
                for q, _ in panel.moduli
                if difference % q == 0
            )
        row_sums.append(row_total)
    radius = max(row_sums, default=0.0)
    mass = sum(abs(a) ** 2 for a in coefficients)
    return diagonal, radius, (diagonal + radius) * mass


def verify_subset_count(panel: Panel) -> None:
    primes = primes_upto(panel.Q)
    for j in range(len(panel.rows)):
        for k in range(j + 1, len(panel.rows)):
            distance = k - j
            delta = panel.centres[k] // panel.centres[j] - 1
            large_prime_divisors = [
                p for p in primes if p > 2 * panel.X and delta % p == 0
            ]
            assert len(large_prime_divisors) < distance, (
                panel.X,
                j,
                k,
                distance,
                large_prime_divisors,
            )
            for order in (1, 2):
                supported = sum(
                    1
                    for q, factors in panel.moduli
                    if len(factors) == order and delta % q == 0
                )
                cap = (
                    math.comb(len(large_prime_divisors), order)
                    if len(large_prime_divisors) >= order
                    else 0
                )
                assert supported <= cap, (panel.X, j, k, order, supported, cap)


def run_panel(X: int, Q: int) -> None:
    panel = build_panel(X, Q)
    coefficients = tuple(
        complex((j % 3) - 1, ((2 * j + 1) % 5) - 2)
        for j in range(len(panel.rows))
    )
    verify_subset_count(panel)
    for profile in ("inverse", "inverse_square"):
        direct = direct_energy(panel, coefficients, profile)
        kernel = kernel_energy(panel, coefficients, profile)
        diagonal, radius, upper = schur_bound(panel, coefficients, profile)
        tolerance = 2e-7 * max(1.0, abs(kernel))
        assert abs(direct - kernel) <= tolerance, (
            X,
            Q,
            profile,
            direct,
            kernel,
            tolerance,
        )
        assert kernel <= upper + tolerance, (X, Q, profile, kernel, upper)
        print(
            f"X={X} Q={Q} rows={len(panel.rows)} moduli={len(panel.moduli)} "
            f"profile={profile} diagonal={diagonal:.9g} radius={radius:.9g} "
            f"energy={kernel:.9g} bound={upper:.9g}"
        )


def main() -> None:
    for X, Q in ((8, 500), (10, 1000), (12, 1500)):
        run_panel(X, Q)
    print("FORTUNE_INT_PWOC_SF_EXACT_REGRESSION_PASS")


if __name__ == "__main__":
    main()
