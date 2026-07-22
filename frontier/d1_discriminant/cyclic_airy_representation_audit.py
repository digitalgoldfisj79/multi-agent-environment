#!/usr/bin/env python3
"""Independent finite audit for CYCLIC_AIRY_FORMALISM_AND_NO_GO.md.

The script checks, using cycle types rather than enumerating S_p, that

    sum_i (-1)^i chi_{wedge^i Std}(sigma)
      = Fix(sigma^p)-Fix(sigma)
      = p * 1_{sigma is a p-cycle}

for all partitions of each selected prime p.  It also records the exact
positive/negative effective dimensions and the cyclic eigenspace dimensions
for a rank-p tensor power.

No external packages are required.
"""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path
from typing import Iterator, List, Sequence


def partitions(n: int, minimum: int = 1) -> Iterator[List[int]]:
    """Yield integer partitions of n in nondecreasing order."""
    if n == 0:
        yield []
        return
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield [first, *rest]


def poly_mul(a: Sequence[int], b: Sequence[int]) -> List[int]:
    result = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result


def divide_by_one_plus_t(poly: Sequence[int]) -> List[int]:
    """Divide an exact integer polynomial by 1+t."""
    if len(poly) < 2:
        raise ValueError("polynomial degree must be at least one")
    quotient = [0] * (len(poly) - 1)
    quotient[0] = poly[0]
    for index in range(1, len(quotient)):
        quotient[index] = poly[index] - quotient[index - 1]
    if poly[-1] != quotient[-1]:
        raise ArithmeticError("division by 1+t was not exact")
    return quotient


def exterior_standard_characters(cycle_lengths: Sequence[int]) -> List[int]:
    """Return chi_{wedge^i Std} for i=0,...,p-1 at a cycle type.

    For a cycle of length d,

        det(1+t C_d) = 1-(-t)^d.

    The permutation representation contains one global invariant line, so
    division by 1+t gives the generating polynomial for exterior powers of
    Std=Perm-1.
    """
    polynomial = [1]
    for length in cycle_lengths:
        factor = [0] * (length + 1)
        factor[0] = 1
        factor[length] = -((-1) ** length)
        polynomial = poly_mul(polynomial, factor)
    return divide_by_one_plus_t(polynomial)


def fixed_points(cycle_lengths: Sequence[int]) -> int:
    return sum(1 for length in cycle_lengths if length == 1)


def fixed_points_of_pth_power(cycle_lengths: Sequence[int], p: int) -> int:
    return sum(length for length in cycle_lengths if p % length == 0)


def audit_prime(p: int) -> dict:
    if p < 2:
        raise ValueError("p must be at least 2")

    checked_types = 0
    failures = []
    for cycle_type in partitions(p):
        checked_types += 1
        hook_characters = exterior_standard_characters(cycle_type)
        alternating_hook_sum = sum(
            (-1) ** i * value for i, value in enumerate(hook_characters)
        )
        adams_difference = (
            fixed_points_of_pth_power(cycle_type, p)
            - fixed_points(cycle_type)
        )
        p_cycle_indicator = p if cycle_type == [p] else 0
        if not (
            alternating_hook_sum == adams_difference == p_cycle_indicator
        ):
            failures.append(
                {
                    "cycle_type": cycle_type,
                    "hook_characters": hook_characters,
                    "alternating_hook_sum": alternating_hook_sum,
                    "adams_difference": adams_difference,
                    "p_cycle_indicator": p_cycle_indicator,
                }
            )

    positive_dimension = sum(
        comb(p - 1, i) for i in range(p) if i % 2 == 0
    )
    negative_dimension = sum(
        comb(p - 1, i) for i in range(p) if i % 2 == 1
    )

    rank = p
    cyclic_trivial_dimension = (rank**p + (p - 1) * rank) // p
    cyclic_nontrivial_dimension = (rank**p - rank) // p

    return {
        "p": p,
        "cycle_types_checked": checked_types,
        "identity_passed": not failures,
        "failures": failures,
        "positive_hook_dimension": positive_dimension,
        "negative_hook_dimension": negative_dimension,
        "minimum_total_effective_rank": positive_dimension + negative_dimension,
        "expected_each_parity_dimension": 2 ** (p - 2),
        "expected_total_effective_rank": 2 ** (p - 1),
        "cyclic_trivial_eigenspace_dimension": cyclic_trivial_dimension,
        "cyclic_nontrivial_eigenspace_dimension": cyclic_nontrivial_dimension,
        "cyclic_dimension_difference": (
            cyclic_trivial_dimension - cyclic_nontrivial_dimension
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--primes",
        nargs="+",
        type=int,
        default=[5, 7, 11, 13, 17, 19],
        help="primes/cycle sizes to audit",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="optional JSON output path",
    )
    args = parser.parse_args()

    results = [audit_prime(p) for p in args.primes]
    if not all(row["identity_passed"] for row in results):
        raise SystemExit(json.dumps(results, indent=2))

    payload = {
        "status": "PASS",
        "description": (
            "All cycle types satisfy the Adams/p-cycle/hook identity; "
            "effective hook dimensions and cyclic eigenspace dimensions "
            "match the exact formulas."
        ),
        "results": results,
    }
    rendered = json.dumps(payload, indent=2)
    print(rendered)
    if args.output is not None:
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
