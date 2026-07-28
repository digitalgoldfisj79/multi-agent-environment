#!/usr/bin/env python3
"""Verify the h-shift variance expansion and scale arithmetic."""
from __future__ import annotations

import json
import math
from pathlib import Path


def exact_case(values: list[int], baseline: int) -> dict:
    total = sum(values)
    direct = (total - baseline) ** 2
    diagonal = sum(x * x for x in values)
    off_diagonal = 0
    H = len(values)
    by_shift = {}
    for h in range(-(H - 1), H):
        if h == 0:
            continue
        subtotal = 0
        for m in range(H):
            n = m + h
            if 0 <= n < H:
                subtotal += values[m] * values[n]
        by_shift[str(h)] = subtotal
        off_diagonal += subtotal
    expanded = diagonal + off_diagonal - 2 * baseline * total + baseline**2
    assert direct == expanded
    assert total * total == diagonal + off_diagonal
    return {
        "values": values,
        "baseline": baseline,
        "direct_variance": direct,
        "diagonal": diagonal,
        "off_diagonal": off_diagonal,
        "expanded_variance": expanded,
        "by_shift": by_shift,
    }


def scale_case(X: int, eta: float = 0.8) -> dict:
    H = eta * X * X
    logx = math.log(X)
    expected_pair_count = H / X
    sieve_pair_count = H / logx
    squared_weight = X * X * logx * logx
    desired_diagonal = expected_pair_count * squared_weight
    sieve_diagonal = sieve_pair_count * squared_weight
    loss = sieve_diagonal / desired_diagonal
    assert abs(loss - X / logx) < 1e-9
    return {
        "X": X,
        "H": H,
        "expected_pair_count_scale": expected_pair_count,
        "positive_sieve_pair_count_scale": sieve_pair_count,
        "squared_prime_weight_scale": squared_weight,
        "desired_diagonal_scale": desired_diagonal,
        "positive_sieve_diagonal_scale": sieve_diagonal,
        "loss_factor": loss,
        "X_over_logX": X / logx,
    }


def main() -> None:
    exact = [
        exact_case([2, 3, 5, 7], 11),
        exact_case([0, 4, 0, 9, 1], 8),
        exact_case([6, 1, 8, 2, 3, 5], 17),
    ]
    scales = [scale_case(X) for X in (101, 503, 1009, 10007)]
    payload = {
        "status": "PASS",
        "scope": "exact h-shift second-moment identity and positive-sieve scale arithmetic",
        "exact_cases": exact,
        "scale_cases": scales,
        "boundary": (
            "The scale calculation is a method obstruction for positive sieve majorants, "
            "not a lower bound for the true diagonal or a proof of the correlation theorem."
        ),
    }
    path = Path(__file__).with_name("four_prime_variance_results.json")
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
