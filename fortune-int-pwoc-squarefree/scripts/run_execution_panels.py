#!/usr/bin/env python3
"""Exact P3/P5/P7 panels for the executed INT-PWOC-SF programme."""
from __future__ import annotations

import math


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


def centres_and_rows(X: int, Q: int) -> tuple[list[int], list[int]]:
    primes = primes_upto(max(Q, 2 * X + 10))
    rows = [p for p in primes if X <= p < 2 * X]
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
    return rows, centres


def order_moduli(X: int, Q: int, order: int) -> list[int]:
    primes = [p for p in primes_upto(Q) if p > 2 * X]
    moduli: list[int] = []

    def visit(start: int, need: int, product: int) -> None:
        if need == 0:
            moduli.append(product)
            return
        for index in range(start, len(primes)):
            p = primes[index]
            if product * p > Q:
                break
            visit(index + 1, need - 1, product * p)

    visit(0, order, 1)
    return moduli


def row_norm(centres: list[int], moduli: list[int], value) -> float:
    result = 0.0
    for j, centre_j in enumerate(centres):
        row = 0.0
        for k, centre_k in enumerate(centres):
            if j == k:
                continue
            difference = abs(centre_j - centre_k)
            row += sum(value(q) for q in moduli if difference % q == 0)
        result = max(result, row)
    return result


def first_collision(centres: list[int], moduli: list[int]):
    for j in range(len(centres)):
        for k in range(j + 1, len(centres)):
            difference = centres[k] - centres[j]
            for q in moduli:
                if difference % q == 0:
                    return j, k, q
    return None


def verify_panel(X: int, Q: int) -> None:
    rows, centres = centres_and_rows(X, Q)
    n = len(rows)
    for order in (1, 2):
        moduli = order_moduli(X, Q, order)
        pair_fraction = 0.0
        for j in range(n):
            for k in range(j + 1, n):
                distance = k - j
                count = sum(1 for q in moduli if (centres[k] - centres[j]) % q == 0)
                cap = math.comb(distance - 1, order) if distance - 1 >= order else 0
                assert count <= cap, (X, Q, order, j, k, count, cap)
                if cap:
                    pair_fraction = max(pair_fraction, count / cap)

        universal_cap = math.comb(n - 1, order + 1) if n - 1 >= order + 1 else 0
        diagonal_inverse = float(len(moduli))
        radius_inverse = row_norm(centres, moduli, lambda q: 1.0)
        diagonal_inverse_square = sum(1.0 / q for q in moduli)
        radius_inverse_square = row_norm(centres, moduli, lambda q: 1.0 / q)
        assert radius_inverse <= universal_cap + 1e-12

        collision = first_collision(centres, moduli)
        adversarial = "none"
        if collision is not None:
            j, k, q = collision
            # beta(q) q = 1 on one colliding modulus: D=1 and R>=1.
            adversarial = f"j={j},k={k},q={q},ratio>=1"

        inverse_ratio = radius_inverse / diagonal_inverse if diagonal_inverse else 0.0
        inverse_square_ratio = (
            radius_inverse_square / diagonal_inverse_square
            if diagonal_inverse_square
            else 0.0
        )
        print(
            f"X={X} Q={Q} n={n} r={order} moduli={len(moduli)} "
            f"cap={universal_cap} pair_fraction={pair_fraction:.6g} "
            f"inverse_D={diagonal_inverse:.9g} inverse_R={radius_inverse:.9g} "
            f"inverse_ratio={inverse_ratio:.9g} "
            f"inverse_square_D={diagonal_inverse_square:.9g} "
            f"inverse_square_R={radius_inverse_square:.9g} "
            f"inverse_square_ratio={inverse_square_ratio:.9g} "
            f"adversarial={adversarial}"
        )


def main() -> None:
    for panel in ((10, 400), (10, 1000), (20, 4000), (30, 12000), (50, 50000)):
        verify_panel(*panel)
    print("FORTUNE_INT_PWOC_SF_EXECUTION_PANELS_PASS")


if __name__ == "__main__":
    main()
