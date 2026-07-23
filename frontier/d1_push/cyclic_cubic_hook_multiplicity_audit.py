#!/usr/bin/env python3
"""Exact audit for CYCLIC_CUBIC_HOOK_MULTIPLICITY_THEOREM.md."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from math import factorial
from pathlib import Path


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    maximum = n if maximum is None else min(maximum, n)
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def z_partition(partition: tuple[int, ...]) -> int:
    counts = Counter(partition)
    result = 1
    for length, multiplicity in counts.items():
        result *= length**multiplicity * factorial(multiplicity)
    return result


def polynomial_mul(a: list[int], b: list[int]) -> list[int]:
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def polynomial_div_exact(a: list[int], b: list[int]) -> list[int]:
    remainder = a[:]
    quotient = [0] * max(1, len(a) - len(b) + 1)
    while True:
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
        if len(remainder) < len(b):
            break
        degree = len(remainder) - len(b)
        if remainder[-1] % b[-1]:
            raise ValueError("nonexact division")
        coefficient = remainder[-1] // b[-1]
        quotient[degree] = coefficient
        for j, value in enumerate(b):
            remainder[degree + j] -= coefficient * value
    if any(remainder):
        raise ValueError(f"nonzero remainder: {remainder}")
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return quotient


def standard_determinant(partition: tuple[int, ...], power: int, plus: bool) -> list[int]:
    polynomial = [1]
    for length in partition:
        degree = power * length
        factor = [0] * (degree + 1)
        factor[0] = 1
        factor[degree] = -((-1) ** length) if plus else -1
        polynomial = polynomial_mul(polynomial, factor)
    denominator = [1, 1] if plus else [1] + [0] * (power - 1) + [-1]
    return polynomial_div_exact(polynomial, denominator)


def milnor_character(partition: tuple[int, ...]) -> list[int]:
    numerator = standard_determinant(partition, 2, False)
    denominator = standard_determinant(partition, 1, False)
    return polynomial_div_exact(numerator, denominator)


def hook_character_generating(partition: tuple[int, ...]) -> list[int]:
    return standard_determinant(partition, 1, True)


def audit_prime(p: int) -> dict:
    maximum_degree = p - 1
    multiplicities = [
        [Fraction(0) for _ in range(p)] for _ in range(maximum_degree + 1)
    ]

    for partition in partitions(p):
        z_value = z_partition(partition)
        milnor = milnor_character(partition)
        hooks = hook_character_generating(partition)
        milnor += [0] * (maximum_degree + 1 - len(milnor))
        hooks += [0] * (p - len(hooks))
        for degree in range(maximum_degree + 1):
            for hook in range(p):
                multiplicities[degree][hook] += Fraction(
                    milnor[degree] * hooks[hook], z_value
                )

    rows = []
    passed = True
    for degree, row in enumerate(multiplicities):
        expected_hook = 0 if degree % 2 == 0 else 1
        expected = [0] * p
        expected[expected_hook] = 1
        integral = all(value.denominator == 1 for value in row)
        actual = [int(value) if value.denominator == 1 else str(value) for value in row]
        check = integral and actual == expected
        passed = passed and check
        rows.append(
            {
                "degree": degree,
                "expected_hook": expected_hook,
                "actual": actual,
                "pass": check,
            }
        )

    return {"p": p, "pass": passed, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", nargs="*", type=int, default=[5, 7, 11, 13, 17])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    results = [audit_prime(p) for p in args.primes]
    output = {
        "status": "PASS" if all(row["pass"] for row in results) else "FAIL",
        "method": "Exact conjugacy-class character inner products over Q.",
        "primes": args.primes,
        "results": results,
    }
    text = json.dumps(output, indent=2)
    print(text)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
