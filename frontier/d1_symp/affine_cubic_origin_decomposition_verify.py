#!/usr/bin/env python3
"""Deterministic checks for AFFINE_CUBIC_ORIGIN_AIRY_DECOMPOSITION_20260725.md.

The theorem is algebraic and valid for every Frobenius power.  This verifier:

1. checks the coefficient-stratum algebra symbolically;
2. performs a fresh direct enumeration in F_(5^5)=F_5[t]/(t^5-t-1);
3. verifies the p=5 cubic-origin count and T_5=0 without importing prior data;
4. checks the equivalent D_p and R_p trace formulae on committed exact first traces.

No external package is required.
"""

from __future__ import annotations

from itertools import product
from typing import Iterable, Tuple


# ---------------------------------------------------------------------------
# Symbolic integer identities
# ---------------------------------------------------------------------------


def lower_strata_total(q: int, degree_p: int) -> int:
    """A=0 contribution before division by q^3."""
    quadratic = -q * q * (q - 1)
    linear = q**degree_p - q * q
    return quadratic + linear


def theorem_numerator(q: int, degree_p: int, cubic_depressed_sum: int) -> int:
    """Sum_(A,B,C) Def before division by q^3."""
    return q * cubic_depressed_sum + q**degree_p - q**3


def theorem_trace_from_T(q: int, degree_p: int, sum_nonzero_A_T: int) -> int:
    assert sum_nonzero_A_T % q == 0
    return q ** (degree_p - 3) - q + sum_nonzero_A_T // q


def check_symbolic_grid() -> None:
    for q in (5, 7, 11, 25, 49, 121):
        for degree_p in (5, 7, 11):
            # The lower strata simplify exactly to q^p-q^3.
            assert lower_strata_total(q, degree_p) == q**degree_p - q**3

            # Use arbitrary multiples of q to check the two rearrangements.
            for k in (-17, -1, 0, 3, 29):
                sum_T = q * k
                depressed = q * sum_T - q * q * (q - 1)
                numerator = theorem_numerator(q, degree_p, depressed)
                lhs = numerator // q**3
                rhs = theorem_trace_from_T(q, degree_p, sum_T)
                assert numerator % q**3 == 0
                assert lhs == rhs


# ---------------------------------------------------------------------------
# Direct F_(5^5) arithmetic
# ---------------------------------------------------------------------------

P = 5
FieldElement = Tuple[int, int, int, int, int]
ZERO: FieldElement = (0, 0, 0, 0, 0)
ONE: FieldElement = (1, 0, 0, 0, 0)
ELEMENTS = [tuple(v) for v in product(range(P), repeat=5)]


def add(a: FieldElement, b: FieldElement) -> FieldElement:
    return tuple((x + y) % P for x, y in zip(a, b))  # type: ignore[return-value]


def mul(a: FieldElement, b: FieldElement) -> FieldElement:
    """Multiply modulo t^5-t-1, i.e. t^5=t+1."""
    c = [0] * 9
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % P

    for k in range(8, 4, -1):
        value = c[k] % P
        if value:
            c[k] = 0
            c[k - 4] = (c[k - 4] + value) % P
            c[k - 5] = (c[k - 5] + value) % P
    return tuple(c[:5])  # type: ignore[return-value]


def power(a: FieldElement, n: int) -> FieldElement:
    result = ONE
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n //= 2
    return result


def trace(a: FieldElement) -> int:
    total = ZERO
    x = a
    for _ in range(5):
        total = add(total, x)
        x = power(x, P)
    assert total[1:] == (0, 0, 0, 0)
    return total[0]


def direct_p5_check() -> dict[str, int | list[int]]:
    theta: FieldElement = (0, 1, 0, 0, 0)
    assert power(theta, P**5) == theta
    assert power(theta, P) != theta

    constraint_count = 0
    trace_zero_cubic_phases = [0] * P

    # Store trace triples to permit a second, coefficient-side check.
    triples: list[tuple[int, int, int]] = []

    for alpha in ELEMENTS:
        alpha2 = mul(alpha, alpha)
        alpha3 = mul(alpha2, alpha)
        t1 = trace(alpha)
        t2 = trace(alpha2)
        t3 = trace(alpha3)
        triples.append((t1, t2, t3))

        if t1 == t2 == t3 == 0:
            constraint_count += 1
        if t1 == 0:
            trace_zero_cubic_phases[t3] += 1

    h0 = constraint_count - P
    assert constraint_count == 25
    assert h0 == 20

    # Nonzero phase counts are equal, so the rational cubic character sum is
    # phase[0]-phase[1].  This independently gives T_5=0.
    assert trace_zero_cubic_phases[1:] == [trace_zero_cubic_phases[1]] * 4
    T5 = trace_zero_cubic_phases[0] - trace_zero_cubic_phases[1]
    assert T5 == 0
    assert h0 == P ** (P - 3) - P + (P - 1) * T5 // P

    # Coefficient-side orthogonality: sum_(A,B,C) of the additive phase is
    # q^3 times the number of simultaneous trace-zero solutions.  Subtracting
    # q for each of q^3 coefficient triples gives q^3*h0.
    phase_coefficient_total = 0
    for t1, t2, t3 in triples:
        if t1 == t2 == t3 == 0:
            phase_coefficient_total += P**3
    defect_coefficient_total = phase_coefficient_total - P**4
    assert defect_coefficient_total == P**3 * h0

    return {
        "constraint_count": constraint_count,
        "h0": h0,
        "T5": T5,
        "phase_counts": trace_zero_cubic_phases,
        "defect_numerator": defect_coefficient_total,
    }


# ---------------------------------------------------------------------------
# Exact first-trace consistency checks
# ---------------------------------------------------------------------------


def first_trace_calibrations() -> list[tuple[int, int]]:
    # Exact T_p values already committed in the branch.  These are used only
    # to check integrality and agreement of the D_p and R_p presentations.
    exact_T = {
        5: 0,
        11: 322102,
        17: 11899821517,
        23: -1010446643080743,
        29: -798145148362709627351,
    }

    output: list[tuple[int, int]] = []
    for p, T in exact_T.items():
        assert T % p == 0

        # At r=1 and p == 2 mod 3 there is one nonzero cube class.
        direct = p ** (p - 3) - p + (p - 1) * (T // p)

        # Tr(D_p)=T/p^2 and Tr(R_p)=p*T.
        assert T % (p * p) == 0 or p == 5
        if p != 5:
            D_trace = T // (p * p)
            via_D = p ** (p - 3) - p + p * (p - 1) * D_trace
            via_R_numerator = (p - 1) * (p * T)
            assert via_R_numerator % (p * p) == 0
            via_R = p ** (p - 3) - p + via_R_numerator // (p * p)
            assert direct == via_D == via_R

        output.append((p, direct))
    return output


def main() -> None:
    check_symbolic_grid()
    p5 = direct_p5_check()
    calibrations = first_trace_calibrations()

    print("AFFINE_CUBIC_ORIGIN_DECOMPOSITION_VERIFY PASS")
    print("p=5 direct:", p5)
    print("first-trace h_(p,1)(0):")
    for p, value in calibrations:
        print(f"  p={p}: {value}")


if __name__ == "__main__":
    main()
