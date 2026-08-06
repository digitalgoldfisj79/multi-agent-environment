#!/usr/bin/env python3
"""Exact rational regression for deterministic microblock aggregation."""
from __future__ import annotations

from fractions import Fraction


def partition(size: int, block: int) -> list[tuple[int, int]]:
    pieces = [(start, min(size, start + block)) for start in range(0, size, block)]
    if len(pieces) >= 2 and pieces[-1][1] - pieces[-1][0] < block // 2:
        previous = pieces[-2]
        pieces[-2:] = [(previous[0], pieces[-1][1])]
    return pieces


def main() -> None:
    for size in (17, 31, 64, 101, 257):
        block = max(2, int(round(size ** Fraction(2, 3))))
        pieces = partition(size, block)
        assert pieces[0][0] == 0 and pieces[-1][1] == size
        assert all(pieces[i][1] == pieces[i + 1][0] for i in range(len(pieces) - 1))

        # Give every microblock a mean at least kappa and verify the parent mean.
        kappa = Fraction(7, 5)
        block_means = [kappa + Fraction(i, 17) for i in range(len(pieces))]
        weighted = sum(
            Fraction(end - start) * mean
            for (start, end), mean in zip(pieces, block_means)
        ) / size
        assert weighted >= kappa
        print(f"rows={size} block={block} pieces={pieces} parent_mean={weighted}")

    print("FORTUNE_INT_SCME_M3_MICROBLOCK_PASS")


if __name__ == "__main__":
    main()
