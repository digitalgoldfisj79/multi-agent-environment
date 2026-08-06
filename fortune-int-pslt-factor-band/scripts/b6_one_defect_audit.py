#!/usr/bin/env python3
"""Verify the exact one-defect scale for the factor-coverage formulation."""

from __future__ import annotations

import math


def positive_part(x: float) -> float:
    return max(0.0, x)


def main() -> None:
    for x in (10**2, 10**3, 10**4, 10**5):
        rows = max(3, int(x / math.log(x)))
        candidate = int(x * x / math.log(x))
        margin = max(1, int(math.log(x)))

        covered = [candidate - margin - 1] * rows
        defect = rows // 2
        covered[defect] = candidate

        terms = [
            positive_part(c - candidate + margin) ** 2
            for c in covered
        ]
        assert terms[defect] == margin * margin
        assert sum(t > 0 for t in terms) == 1
        assert sum(terms) >= margin * margin

        print(
            f"X={x} rows={rows} candidates_per_row={candidate} "
            f"margin={margin} defect_energy={sum(terms):.8g}"
        )

    print("FORTUNE_INT_PSLT_B6_ONE_DEFECT_PASS")


if __name__ == "__main__":
    main()
