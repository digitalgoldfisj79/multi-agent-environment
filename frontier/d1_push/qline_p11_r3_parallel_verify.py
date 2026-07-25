#!/usr/bin/env python3
"""Independent parallel verification of the p=11, r=3 generic q-line trace.

Requires python-flint.  The calculation enumerates all

    (q,t) in (F_(11^3) minus {0,2}) x F_(11^3)

and factors

    q z^11 + z^3 - 3z - (q-2)t.

Expected exact output:

    irreducible_total = 161446
    qline_trace       = -7007
"""

from __future__ import annotations

import argparse
import os
from multiprocessing import Pool

import flint


def enumerate_field(context, p: int, degree: int):
    generator = context.gen()
    elements = [context(value) for value in range(p)]
    power = context(1)
    for _ in range(1, degree):
        power *= generator
        block = [context(value) * power for value in range(p)]
        elements = [left + right for left in elements for right in block]
    return elements


def is_irreducible(polynomial, p: int) -> bool:
    _, factors = polynomial.factor()
    return (
        len(factors) == 1
        and factors[0][1] == 1
        and factors[0][0].degree() == p
    )


def worker(arguments: tuple[int, int, int, int]) -> int:
    p, degree, start, end = arguments
    context = flint.fq_default_ctx(p, degree)
    polynomial_context = flint.fq_default_poly_ctx(context)
    elements = enumerate_field(context, p, degree)
    zero = context(0)
    two = context(2)
    three = context(3)

    subtotal = 0
    for index in range(start, end):
        q = elements[index]
        if q == zero or q == two:
            continue
        for t in elements:
            # Do not use [context(0)]*(p+1): some finite-field scalar
            # implementations are mutable and would alias every coefficient.
            coefficients = [context(0) for _ in range(p + 1)]
            coefficients[0] = -(q - two) * t
            coefficients[1] = -three
            coefficients[3] = context(1)
            coefficients[p] = q
            if is_irreducible(polynomial_context(coefficients), p):
                subtotal += 1
    return subtotal


def trace_sum(p: int = 11, degree: int = 3, workers: int | None = None):
    cardinality = p**degree
    worker_count = workers or min(os.cpu_count() or 1, 32)
    chunk = (cardinality + worker_count - 1) // worker_count
    tasks = [
        (p, degree, start, min(start + chunk, cardinality))
        for start in range(0, cardinality, chunk)
    ]

    print(
        f"START p={p} r={degree} Q={cardinality} "
        f"workers={worker_count} tasks={len(tasks)}",
        flush=True,
    )

    parts: list[int] = []
    with Pool(worker_count) as pool:
        for completed, value in enumerate(
            pool.imap_unordered(worker, tasks), start=1
        ):
            parts.append(value)
            print(
                f"PART {completed}/{len(tasks)} subtotal={value} "
                f"cumulative={sum(parts)}",
                flush=True,
            )

    irreducible_total = sum(parts)
    trace = (cardinality - 2) * cardinality - p * irreducible_total
    return cardinality, irreducible_total, trace


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=None)
    args = parser.parse_args()

    cardinality, count, trace = trace_sum(workers=args.workers)
    print(
        f"RESULT Q={cardinality} irreducible_total={count} "
        f"qline_trace={trace}",
        flush=True,
    )
    assert count == 161446
    assert trace == -7007
    print("P11_R3_QLINE_INDEPENDENT_VERIFY: PASS", flush=True)


if __name__ == "__main__":
    main()
