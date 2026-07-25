#!/usr/bin/env python3
"""Exact square/nonsquare q-line census at p=53 and p=71.

Requires python-flint.  For each prime and cubic square class, every

    X^p + a X^3 + c X + d,  (c,d) in F_p^2

is factored exactly.
"""

from __future__ import annotations

import argparse
import os
from multiprocessing import Pool

import flint


def least_nonsquare(p: int) -> int:
    for value in range(2, p):
        if pow(value, (p - 1) // 2, p) == p - 1:
            return value
    raise AssertionError(p)


def worker(arguments):
    p, cubic, start, end = arguments
    context = flint.fmpz_mod_poly_ctx(p)
    variable = context.gen()
    subtotal = 0
    cell_counts = []
    for linear in range(start, end):
        count = 0
        for constant in range(p):
            polynomial = (
                variable**p
                + cubic * variable**3
                + linear * variable
                + constant
            )
            _, factors = polynomial.factor()
            if (
                len(factors) == 1
                and factors[0][1] == 1
                and factors[0][0].degree() == p
            ):
                count += 1
        assert count % 2 == 0
        subtotal += count
        cell_counts.append((linear, count))
    return subtotal, cell_counts


def census(p: int, cubic: int, workers: int):
    chunk = (p + workers - 1) // workers
    tasks = [
        (p, cubic, start, min(start + chunk, p))
        for start in range(0, p, chunk)
    ]
    totals = []
    cells = []
    with Pool(workers) as pool:
        for subtotal, cell_counts in pool.imap_unordered(worker, tasks):
            totals.append(subtotal)
            cells.extend(cell_counts)
    return sum(totals), sorted(cells)


def verify_prime(p: int, expected_plus: int, expected_minus: int, workers: int):
    eta = least_nonsquare(p)
    plus, plus_cells = census(p, 1, workers)
    minus, minus_cells = census(p, eta, workers)

    assert plus == expected_plus
    assert minus == expected_minus

    # c=0 is q=infinity and must be zero in both readings.
    assert plus_cells[0] == (0, 0)
    assert minus_cells[0] == (0, 0)

    # q=2 corresponds to c=-3/2 in the original depressed family.
    q2_linear = -3 * pow(2, -1, p) % p
    assert dict(plus_cells)[q2_linear] == 0
    assert dict(minus_cells)[q2_linear] == 0

    s0 = p * (2 * (p - 2) - plus - minus)
    schi = p * (minus - plus)
    expected_projectors = {
        53: (424, -954),
        71: (-710, 284),
    }[p]
    assert (s0, schi) == expected_projectors

    assert plus % (2 * p) != 0
    assert minus % (2 * p) != 0

    print(
        f"p={p}, eta={eta}: N_plus={plus}, N_minus={minus}, "
        f"S0={s0}, S_chi={schi}: PASS"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 1, 32))
    arguments = parser.parse_args()

    verify_prime(53, 56, 38, arguments.workers)
    verify_prime(71, 72, 76, arguments.workers)
    print("GENERIC_QLINE_P53_P71_VERIFY: PASS")


if __name__ == "__main__":
    main()
