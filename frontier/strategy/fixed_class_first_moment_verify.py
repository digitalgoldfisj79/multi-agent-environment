#!/usr/bin/env python3
"""Exact regressions for the fixed-class first Cartier moment.

Requires python-flint.  The script verifies:
  * C1-weighted moment data for the depressed cubic family;
  * the full-family translation identity
        sum b^(p-1)c 1_irred = -M_a;
  * the reciprocal q-line assembly
        M_A = -3 sum_q q^(-1) I_(A chi(q))(q);
  * non-p-divisibility of the c-weighted odd reducible strata.

The finite checks are structural regressions and counterexamples, not a proof of
uniform moment nonvanishing or of function-field d=1.
"""
from __future__ import annotations

import json
from pathlib import Path
from flint import nmod_poly


def chi(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(a for a in range(2, p) if chi(a, p) == -1)


def is_irreducible(coefficients: list[int], p: int) -> bool:
    polynomial = nmod_poly(coefficients, p)
    _, factors = polynomial.factor()
    return (
        len(factors) == 1
        and factors[0][1] == 1
        and factors[0][0].degree() == p
    )


def depressed_stats(p: int, a: int) -> tuple[int, int, list[int]]:
    count = 0
    moment = 0
    cells = []
    for c in range(p):
        cell = 0
        for d in range(p):
            coefficients = [d, c, 0, a] + [0] * (p - 4) + [1]
            if is_irreducible(coefficients, p):
                count += 1
                cell += 1
                moment = (moment + c) % p
        cells.append(cell)
    return count, moment, cells


def full_translation_weight(p: int, a: int) -> int:
    total = 0
    for b in range(p):
        bweight = pow(b, p - 1, p)
        if bweight == 0:
            continue
        for c in range(p):
            for d in range(p):
                coefficients = [d, c, b, a] + [0] * (p - 4) + [1]
                if is_irreducible(coefficients, p):
                    total = (total + bweight * c) % p
    return total


def qline_moment(p: int, a: int) -> int:
    eta = least_nonsquare(p)
    arithmetic_class = chi(a, p)
    total = 0
    for q in range(1, p):
        epsilon = arithmetic_class * chi(q, p)
        cubic = pow(q, -1, p) if epsilon == 1 else pow(eta * q % p, -1, p)
        linear = -3 * pow(q, -1, p) % p
        cell = 0
        for delta in range(p):
            coefficients = [delta, linear, 0, cubic] + [0] * (p - 4) + [1]
            cell += int(is_irreducible(coefficients, p))
        total = (total - 3 * pow(q, -1, p) * cell) % p
    return total


def local_factor_parity(p: int, a: int) -> dict[str, int]:
    irreducible_count = irreducible_moment = 0
    odd_reducible_count = odd_reducible_moment = 0
    even_count = even_moment = 0
    for c in range(p):
        for d in range(p):
            if any((a * x**3 + (c + 1) * x + d) % p == 0 for x in range(p)):
                continue
            polynomial = nmod_poly([d, c, 0, a] + [0] * (p - 4) + [1], p)
            _, factors = polynomial.factor()
            number_of_factors = sum(exponent for _, exponent in factors)
            if number_of_factors == 1:
                irreducible_count += 1
                irreducible_moment = (irreducible_moment + c) % p
            elif number_of_factors % 2:
                odd_reducible_count += 1
                odd_reducible_moment = (odd_reducible_moment + c) % p
            else:
                even_count += 1
                even_moment = (even_moment + c) % p
    return {
        "irreducible_count": irreducible_count,
        "irreducible_c_moment": irreducible_moment,
        "odd_reducible_count": odd_reducible_count,
        "odd_reducible_c_moment": odd_reducible_moment,
        "even_factor_count": even_count,
        "even_factor_c_moment": even_moment,
    }


def main() -> None:
    expected = {
        5: {"+": (4, 0), "-": (6, 1)},
        7: {"+": (10, 1), "-": (8, 4)},
        11: {"+": (14, 1), "-": (14, 1)},
    }
    identity_rows = {}
    for p in (5, 7, 11):
        identity_rows[str(p)] = {}
        for label, a in (("+", 1), ("-", least_nonsquare(p))):
            count, moment, cells = depressed_stats(p, a)
            assert (count, moment) == expected[p][label]
            qmoment = qline_moment(p, a)
            assert qmoment == moment
            row = {
                "a": a,
                "count": count,
                "c_moment": moment,
                "qline_c_moment": qmoment,
                "cell_counts": cells,
            }
            if p in (5, 7):
                translation = full_translation_weight(p, a)
                assert translation == (-moment) % p
                row["full_translation_weight"] = translation
            identity_rows[str(p)][label] = row

    parity_expected = {
        11: {"+": (8, 2), "-": (14, 2)},
        17: {"+": (26, 16), "-": (42, 14)},
        23: {"+": (70, 19), "-": (70, 14)},
        29: {"+": (106, 14), "-": (130, 28)},
        41: {"+": (216, 20), "-": (270, 24)},
        47: {"+": (298, 21), "-": (314, 42)},
        53: {"+": (366, 32), "-": (408, 50)},
    }
    parity_rows = {}
    for p, classes in parity_expected.items():
        parity_rows[str(p)] = {}
        for label, a in (("+", 1), ("-", least_nonsquare(p))):
            row = local_factor_parity(p, a)
            expected_count, expected_moment = classes[label]
            assert row["odd_reducible_count"] == expected_count
            assert row["odd_reducible_c_moment"] == expected_moment
            assert expected_moment % p != 0
            parity_rows[str(p)][label] = row

    output = {
        "classification": "exact finite regressions and counterexamples; no uniform nonvanishing theorem",
        "identity_rows": identity_rows,
        "odd_reducible_parity_rows": parity_rows,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "fixed_class_first_moment_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print("FIXED_CLASS_FIRST_MOMENT_VERIFY: PASS")


if __name__ == "__main__":
    main()
