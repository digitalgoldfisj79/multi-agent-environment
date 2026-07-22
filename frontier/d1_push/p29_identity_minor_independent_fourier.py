#!/usr/bin/env python3
"""Independent p=29 identity-minor Fourier verification.

This audit does not enumerate assignments or degree sets. It evaluates the
selected dominant-w=1 identity minor directly at every nonzero element of two
independent models of F_(29^2), and uses multiplicative Fourier inversion to
extract its a^43 coefficient after setting c=d=1.

For a fixed identity minor the c- and d-degrees are determined by the a-degree,
so [a^43] at c=d=1 is exactly [a^43 c^224 d^112].
Only Python's standard library is used.
"""
from __future__ import annotations

import json
from math import factorial
from pathlib import Path

P = 29
FIELD_ORDER = P * P
GROUP_ORDER = FIELD_ORDER - 1
OMITTED_N = (1, 2, 4, 5, 7, 8)
TARGET_A_DEGREE = 43
TARGET_C_DEGREE = 224
TARGET_D_DEGREE = 112
TARGET_WEIGHT = TARGET_C_DEGREE + 2 * TARGET_D_DEGREE


def build_field(nonsquare: int):
    mul = [[0] * FIELD_ORDER for _ in range(FIELD_ORDER)]
    for x in range(FIELD_ORDER):
        a, b = x % P, x // P
        for y in range(FIELD_ORDER):
            c, d = y % P, y // P
            mul[x][y] = (
                (a * c + nonsquare * b * d) % P
                + P * ((a * d + b * c) % P)
            )

    def powf(x: int, exponent: int) -> int:
        out = 1
        while exponent:
            if exponent & 1:
                out = mul[out][x]
            x = mul[x][x]
            exponent >>= 1
        return out

    inverses = [0] * FIELD_ORDER
    for x in range(1, FIELD_ORDER):
        inverses[x] = powf(x, FIELD_ORDER - 2)
    return mul, inverses, powf


def addf(x: int, y: int) -> int:
    return ((x % P + y % P) % P) + P * ((x // P + y // P) % P)


def subf(x: int, y: int) -> int:
    return ((x % P - y % P) % P) + P * ((x // P - y // P) % P)


def determinant(matrix, mul, inverses):
    a = [row[:] for row in matrix]
    n = len(a)
    out = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            out = subf(0, out)
        pv = a[col][col]
        out = mul[out][pv]
        ipv = inverses[pv]
        for row in range(col + 1, n):
            if not a[row][col]:
                continue
            factor = mul[a[row][col]][ipv]
            for j in range(col, n):
                a[row][j] = subf(a[row][j], mul[factor][a[col][j]])
    return out


def identity_expansion_sign() -> int:
    identity_rows = tuple(sorted(P - n for n in OMITTED_N))

    def column_position(row: int) -> int:
        return row if row < 3 else row - 1

    identity_parity = sum(
        row + column_position(row) for row in identity_rows
    ) & 1
    active_count = (P - 1) - len(OMITTED_N)
    minus_h_parity = active_count & 1
    row_sign_parity = sum(
        n for n in range(1, P) if n not in OMITTED_N
    ) & 1
    return -1 if (
        identity_parity ^ minus_h_parity ^ row_sign_parity
    ) else 1


def extract_in_model(nonsquare: int) -> dict:
    assert pow(nonsquare, (P - 1) // 2, P) == P - 1
    mul, inverses, powf = build_field(nonsquare)

    active_n_desc = tuple(
        n for n in range(P - 1, 0, -1) if n not in OMITTED_N
    )
    q_desc = tuple(n for n in active_n_desc if n != P - 3) + (0,)

    fac = [factorial(k) % P for k in range(P)]
    ifac = [pow(fac[k], P - 2, P) for k in range(P)]

    terms = {}
    for n in active_n_desc:
        for q in q_desc:
            current = []
            for i in range(q // 3 + 1):
                j = q - 3 * i
                k = n - i - j
                if k < 0:
                    continue
                coeff = fac[n]
                coeff = coeff * ifac[i] % P
                coeff = coeff * ifac[j] % P
                coeff = coeff * ifac[k] % P
                current.append((i, coeff))
            terms[(n, q)] = current

    degree_bound = sum(active_n_desc)
    assert degree_bound < GROUP_ORDER

    fourier_sum = 0
    for aval in range(1, FIELD_ORDER):
        powers = [1] * P
        for exponent in range(1, P):
            powers[exponent] = mul[powers[exponent - 1]][aval]

        matrix = []
        for n in active_n_desc:
            row = []
            for q in q_desc:
                value = 0
                for i, coeff in terms[(n, q)]:
                    value = addf(value, mul[coeff][powers[i]])
                row.append(value)
            matrix.append(row)

        det_value = determinant(matrix, mul, inverses)
        weight = powf(inverses[aval], TARGET_A_DEGREE)
        fourier_sum = addf(fourier_sum, mul[det_value][weight])

    coefficient = subf(0, fourier_sum)
    return {
        "field": f"F_29[s]/(s^2-{nonsquare})",
        "nonsquare": nonsquare,
        "multiplicative_order": GROUP_ORDER,
        "a_degree_bound": degree_bound,
        "coefficient_encoded": coefficient,
        "coefficient_real": coefficient % P,
        "coefficient_imag": coefficient // P,
    }


def main() -> None:
    models = [extract_in_model(2), extract_in_model(3)]
    assert all(row["coefficient_real"] == 7 for row in models)
    assert all(row["coefficient_imag"] == 0 for row in models)

    sign = identity_expansion_sign()
    assert sign == -1
    signed = sign * 7 % P
    assert signed == 22
    nonsquare_a_check = signed * pow(2, TARGET_A_DEGREE, P) % P
    assert nonsquare_a_check == 14

    active_n = tuple(n for n in range(1, P) if n not in OMITTED_N)
    q_values = tuple(n for n in active_n if n != P - 3) + (0,)
    assert sum(q_values) - 3 * TARGET_A_DEGREE == TARGET_C_DEGREE
    assert sum(active_n) - sum(q_values) + 2 * TARGET_A_DEGREE == TARGET_D_DEGREE
    assert TARGET_WEIGHT > (P * P - 1) // 2

    result = {
        "status": "PASS",
        "method": (
            "Direct evaluation of the selected 22x22 dominant-w=1 identity "
            "minor at all 840 nonzero elements of two independent F_(29^2) "
            "models, followed by exact multiplicative Fourier extraction of "
            "the a^43 coefficient. No assignment or degree-set enumeration."
        ),
        "prime": P,
        "omitted_n": list(OMITTED_N),
        "identity_rows": sorted(P - n for n in OMITTED_N),
        "target": {
            "a_degree": TARGET_A_DEGREE,
            "c_degree": TARGET_C_DEGREE,
            "d_degree": TARGET_D_DEGREE,
            "weight": TARGET_WEIGHT,
            "support_boundary": (P * P - 1) // 2,
        },
        "field_models": models,
        "identity_minor_coefficient_mod_29": 7,
        "identity_expansion_sign": sign,
        "signed_cartier_contribution_mod_29": signed,
        "a_2_signed_check_mod_29": nonsquare_a_check,
    }

    output = Path(__file__).with_name(
        "p29_identity_minor_independent_fourier_results.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
