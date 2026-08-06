#!/usr/bin/env python3
"""Exact adversarial count models for one-defect resolution."""

from fractions import Fraction


def run() -> None:
    for n, k in ((10, 100), (100, 1000), (1000, 10000)):
        balanced = [k] * n
        defect = [0, 2 * k] + [k] * (n - 2)
        assert sum(defect) == sum(balanced)
        balanced_second = sum(z * z for z in balanced)
        defect_second = sum(z * z for z in defect)
        second_excess = defect_second - balanced_second
        relative_excess = Fraction(second_excess, balanced_second)
        lower_tail = sum(max(0, k - z) ** 2 for z in defect)
        assert second_excess == 2 * k * k
        assert relative_excess == Fraction(2, n)
        assert lower_tail == k * k
        print(
            f"N={n} K={k} first_moment_equal=1 "
            f"relative_second_excess={relative_excess} lower_tail={lower_tail}"
        )
    print("FORTUNE_INT_ISC_I6_ADVERSARIAL_PASS")


if __name__ == "__main__":
    run()
