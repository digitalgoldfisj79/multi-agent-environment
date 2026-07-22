#!/usr/bin/env python3
"""Exact audit of the Kummer trace formula for the quadratic third moment.

For each prime 5<=p<=101 and both square classes, the script independently:
  * counts zero-sum triples in the quadratic-factor trace set;
  * evaluates the six-line double-plane character sum directly;
  * computes the genus-two Frobenius traces over F_p and F_(p^2);
  * computes the elliptic root-correction trace; and
  * verifies the exact formulas in QUADRATIC_THIRD_MOMENT_KUMMER_THEOREM.md.

Only the Python standard library is used.
"""
from __future__ import annotations

import csv
from pathlib import Path


def primes_to(limit: int) -> list[int]:
    out = []
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            out.append(n)
    return out


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def first_nonsquare(p: int) -> int:
    return next(x for x in range(2, p) if chi(x, p) == -1)


def mul2(x: tuple[int, int], y: tuple[int, int], p: int, nr: int) -> tuple[int, int]:
    a, b = x
    c, d = y
    return ((a * c + nr * b * d) % p, (a * d + b * c) % p)


def add2(x: tuple[int, int], y: tuple[int, int], p: int) -> tuple[int, int]:
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def sub2(x: tuple[int, int], y: tuple[int, int], p: int) -> tuple[int, int]:
    return ((x[0] - y[0]) % p, (x[1] - y[1]) % p)


def scalar2(k: int, x: tuple[int, int], p: int) -> tuple[int, int]:
    return (k * x[0] % p, k * x[1] % p)


def norm2(x: tuple[int, int], p: int, nr: int) -> int:
    return (x[0] * x[0] - nr * x[1] * x[1]) % p


def genus_two_traces(p: int) -> tuple[int, int, int, int, int]:
    """For C: y^2=t(t-1)(t+1)(t+2)(2t+1).

    Returns S1, S2, Tr(F|H1), Tr(F^2|H1), Tr(F|wedge^2 H1).
    """
    nr = first_nonsquare(p)
    s1 = sum(
        chi(t * (t - 1) * (t + 1) * (t + 2) * (2 * t + 1), p)
        for t in range(p)
    )

    one = (1, 0)
    two = (2, 0)
    s2 = 0
    for a in range(p):
        for b in range(p):
            t = (a, b)
            factors = (
                t,
                sub2(t, one, p),
                add2(t, one, p),
                add2(t, two, p),
                add2(scalar2(2, t, p), one, p),
            )
            value = one
            for factor in factors:
                value = mul2(value, factor, p, nr)
            # In a quadratic extension, z is a square iff Norm(z) is a
            # square in the base field.
            s2 += chi(norm2(value, p, nr), p)

    tr1 = -s1
    tr2 = -s2
    wedge_trace = (tr1 * tr1 - tr2) // 2
    return s1, s2, tr1, tr2, wedge_trace


def elliptic_trace(p: int) -> int:
    """Trace for E: z^2=(u^2-1)((u+1)^2-1)."""
    affine_character_sum = sum(
        chi((u * u - 1) * (((u + 1) % p) ** 2 - 1), p)
        for u in range(p)
    )
    # The monic quartic model has two points at infinity.
    return -1 - affine_character_sum


def raw_six_line_sum(p: int, delta: int) -> int:
    return sum(
        chi(
            (x * x - delta)
            * (y * y - delta)
            * (((x + y) % p) ** 2 - delta),
            p,
        )
        for x in range(p)
        for y in range(p)
    )


def direct_third_moment(p: int, delta: int) -> int:
    trace_set = {
        r for r in range(1, p) if chi(r * r - delta, p) == -1
    }
    ordered = sum(
        1
        for x in trace_set
        for y in trace_set
        if (-x - y) % p in trace_set
    )
    assert ordered % 6 == 0
    return ordered // 6


def predicted_row(p: int, square_class: int) -> dict[str, int]:
    s1, s2, tr1, tr2, wedge_trace = genus_two_traces(p)
    e_trace = elliptic_trace(p)
    eta = chi(-1, p)
    nu = chi(3, p)
    kappa = chi(-3, p)

    if square_class == 1:
        raw = 2 - p + kappa * wedge_trace
        corrected_binary_sum = (
            raw - 6 * (1 + e_trace) + 6 * (nu + eta)
        )
        zero_in_trace_set = (1 - eta) // 2
        numerator = p * p - 3 * p + 3 - corrected_binary_sum
        assert numerator % 8 == 0
        ordered = (
            numerator // 8
            - zero_in_trace_set * (3 * (p - 1) // 2 - 2)
        )
    else:
        twisted_wedge = (
            4 * p - wedge_trace if kappa == 1 else -wedge_trace
        )
        raw = 2 - p + kappa * twisted_wedge
        # Equivalent closed form:
        assert raw == 2 + p + 2 * p * kappa - kappa * wedge_trace
        corrected_binary_sum = raw
        zero_in_trace_set = (1 + eta) // 2
        numerator = p * p + 3 * p + 3 - corrected_binary_sum
        assert numerator % 8 == 0
        ordered = (
            numerator // 8
            - zero_in_trace_set * (3 * (p + 1) // 2 - 2)
        )

    assert ordered % 6 == 0
    return {
        "prime": p,
        "square_class": square_class,
        "chi_minus_one": eta,
        "chi_three": nu,
        "chi_minus_three": kappa,
        "genus2_S1": s1,
        "genus2_S2": s2,
        "genus2_H1_trace": tr1,
        "genus2_H1_square_trace": tr2,
        "genus2_wedge2_trace": wedge_trace,
        "elliptic_trace": e_trace,
        "predicted_raw_six_line_sum": raw,
        "predicted_third_factorial_moment": ordered // 6,
    }


def main() -> None:
    rows: list[dict[str, int]] = []
    for p in primes_to(101):
        if p < 5:
            continue
        for square_class in (1, -1):
            row = predicted_row(p, square_class)
            delta = 1 if square_class == 1 else first_nonsquare(p)
            row["direct_raw_six_line_sum"] = raw_six_line_sum(p, delta)
            row["direct_third_factorial_moment"] = direct_third_moment(
                p, delta
            )
            assert (
                row["predicted_raw_six_line_sum"]
                == row["direct_raw_six_line_sum"]
            )
            assert (
                row["predicted_third_factorial_moment"]
                == row["direct_third_factorial_moment"]
            )
            rows.append(row)

    output = Path(__file__).with_name(
        "quadratic_third_moment_kummer_audit_results.csv"
    )
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(
        "PASS:",
        len(rows),
        "prime/square-class cases through p=101;",
        "all direct character sums and third moments match the Kummer formulas.",
    )


if __name__ == "__main__":
    main()
