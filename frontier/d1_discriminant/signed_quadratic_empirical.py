#!/usr/bin/env python3
"""Transformed-only sweep for the signed quadratic incidence.

Uses the exact O(p^2) formulas, not polynomial factorization or Monte Carlo.
The output is diagnostic and is not used in the proof.
"""

from signed_quadratic_incidence_check import chi, primes_upto, transformed_terms


def main(limit=293):
    records = []
    for p in primes_upto(limit):
        if p < 5:
            continue
        nonsquare = next(a for a in range(2, p) if chi(a, p) == -1)
        for a in (1, nonsquare):
            value = transformed_terms(p, a)[4]
            records.append((abs(value) / p, p, chi(a, p), value))
    ratio, p, square_class, value = max(records)
    print(f"classes checked: {len(records)}")
    print(
        "max |Lchi|/p: "
        f"{ratio:.12f} at p={p}, class={square_class:+d}, Lchi={value}"
    )


if __name__ == "__main__":
    main()
