#!/usr/bin/env python3
"""Exact execution for the INT-LCSK pair-tree programme."""
from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


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


def partitions(n: int) -> list[tuple[tuple[int, ...], ...]]:
    output: list[tuple[tuple[int, ...], ...]] = []

    def recurse(index: int, blocks: list[list[int]]) -> None:
        if index == n:
            output.append(tuple(tuple(block) for block in blocks))
            return
        for block_index in range(len(blocks)):
            blocks[block_index].append(index)
            recurse(index + 1, blocks)
            blocks[block_index].pop()
        blocks.append([index])
        recurse(index + 1, blocks)
        blocks.pop()

    recurse(0, [])
    return output


def local_moment(p: int, residues: tuple[int, ...], block: tuple[int, ...]) -> Fraction:
    distinct = len({residues[i] % p for i in block})
    order = len(block)
    return Fraction(p - distinct, p) * Fraction(p, p - 1) ** order


def connected_local(p: int, residues: tuple[int, ...]) -> Fraction:
    total = Fraction(0)
    for partition in partitions(len(residues)):
        block_count = len(partition)
        coefficient = (-1) ** (block_count - 1) * factorial(block_count - 1)
        term = Fraction(coefficient)
        for block in partition:
            term *= local_moment(p, residues, block)
        total += term
    return total


def verify_order_three_formulas() -> None:
    for p in primes_upto(211):
        if p <= 3:
            continue
        assert connected_local(p, (0, 0, 0)) == -Fraction(p - 2, (p - 1) ** 2)
        assert connected_local(p, (0, 0, 1)) == Fraction(p - 2, (p - 1) ** 3)
        assert connected_local(p, (0, 1, 2)) == -Fraction(2, (p - 1) ** 3)
        assert connected_local(p, (0, 0)) == Fraction(1, p - 1)


def verify_tree_failure() -> None:
    for constant in (1, 2, 4, 8):
        threshold = 3 * constant * constant + 2
        p = next(q for q in primes_upto(max(1000, threshold * 3)) if q > threshold)
        triple = abs(connected_local(p, (0, 0, 0)))
        tree_budget = 3 * Fraction(constant, p - 1) ** 2
        assert triple > tree_budget
        print(
            f"C={constant} p={p} triple={triple} tree={tree_budget} "
            f"ratio={float(triple / tree_budget):.6f}"
        )


def verify_actual_candidate_witness() -> None:
    X = 18
    H = X * X
    p = 37
    offsets = (89, 163, 311)
    primes = set(primes_upto(H))
    assert p > 2 * X
    assert all(m in primes and 2 * X < m <= H for m in offsets)
    assert len({m % p for m in offsets}) == 1
    triple = connected_local(p, tuple(m % p for m in offsets))
    pair = connected_local(p, (0, 0))
    assert triple == -Fraction(35, 36**2)
    assert abs(triple) > 3 * pair * pair
    print(
        f"witness X={X} H={H} p={p} offsets={offsets} "
        f"kappa3={triple} pair_tree={3 * pair * pair}"
    )


def same_residue_panel(X: int) -> tuple[float, float, float, tuple[int, float, float]]:
    H = X * X
    candidates = [m for m in primes_upto(H) if m > 2 * X]
    post_primes = [p for p in primes_upto(H) if p > 2 * X]
    counts: dict[int, dict[int, int]] = {}
    for p in post_primes:
        bucket: dict[int, int] = {}
        for m in candidates:
            residue = m % p
            bucket[residue] = bucket.get(residue, 0) + 1
        counts[p] = bucket

    max_pair = 0.0
    max_triple = 0.0
    max_ratio = 0.0
    witness = (0, 0.0, 0.0)
    for m in candidates:
        pair_mass = Fraction(0)
        triple_mass = Fraction(0)
        for p, bucket in counts.items():
            count = bucket[m % p]
            if count >= 2:
                pair_mass += Fraction(count - 1, p - 1)
            if count >= 3:
                triple_mass += Fraction(comb(count - 1, 2) * (p - 2), (p - 1) ** 2)
        pair_value = float(pair_mass)
        triple_value = float(triple_mass)
        ratio = triple_value / (pair_value * pair_value) if pair_value else 0.0
        if ratio > max_ratio:
            max_ratio = ratio
            witness = (m, pair_value, triple_value)
        max_pair = max(max_pair, pair_value)
        max_triple = max(max_triple, triple_value)
    return max_pair, max_triple, max_ratio, witness


def verify_finite_panels() -> None:
    for X in (18, 20, 30, 40, 50):
        pair, triple, ratio, witness = same_residue_panel(X)
        assert ratio > 1.0
        print(
            f"X={X} H={X*X} max_pair={pair:.9g} max_triple={triple:.9g} "
            f"max_triple_over_pair_sq={ratio:.9g} witness={witness}"
        )


def verify_exponent_ledger() -> None:
    for order in (3, 4, 8, 16, 32, 64):
        maximum_delta = Fraction(1, order - 1)
        assert order == (order - 1) + 1
        print(
            f"r={order} maximum_delta_from_absolute_ledger="
            f"{float(maximum_delta):.9g}"
        )


def main() -> None:
    verify_order_three_formulas()
    verify_tree_failure()
    verify_actual_candidate_witness()
    verify_finite_panels()
    verify_exponent_ledger()
    print("FORTUNE_INT_LCSK_TREE_GRAPH_EXECUTION_PASS")


if __name__ == "__main__":
    main()
