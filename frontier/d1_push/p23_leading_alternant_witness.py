#!/usr/bin/env python3
"""Reconstruct the p=23 leading filtered-assignment witness.

This audit is narrower than p23_filtered_survivor_audit.cpp.  It exhibits one
explicit w=1 identity-selected assignment above the proposed support boundary,
shows that its individual falling-factorial alternant contribution is nonzero,
and then enumerates the complete leading coefficient for that same identity
minor.  The 332,192 distinct-degree assignments collapse into 18 factorial-
alternant degree sets; every scalar coefficient is 0 modulo 23.

No third-party packages are required.
"""
from __future__ import annotations

import json
from collections import defaultdict
from math import factorial
from pathlib import Path

P = 23
BOUNDARY = (P * P - 1) // 2

# The identity rows are encoded in the n=p-u coordinate by T.
OMITTED_N = (1, 2, 5, 6, 7)
IDENTITY_ROWS = tuple(sorted(P - n for n in OMITTED_N))

# One exact assignment returned by the filtered w=1 optimization.
# map column v -> cubic-factor count i.
I_BY_COLUMN = {
    1: 4,
    2: 3,
    4: 6,
    5: 6,
    6: 0,
    7: 0,
    8: 5,
    9: 2,
    10: 0,
    11: 0,
    12: 0,
    13: 3,
    14: 3,
    15: 0,
    19: 1,
    20: 1,
    23: 0,
}


def inv(x: int) -> int:
    return pow(x % P, P - 2, P)


def falling(n: int, m: int) -> int:
    out = 1
    for r in range(m):
        out = out * (n - r) % P
    return out


def det_mod(matrix: list[list[int]]) -> int:
    a = [[x % P for x in row] for row in matrix]
    n = len(a)
    out = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            out = -out
        pv = a[col][col] % P
        out = out * pv % P
        ipv = inv(pv)
        for row in range(col + 1, n):
            if not a[row][col]:
                continue
            q = a[row][col] * ipv % P
            for j in range(col, n):
                a[row][j] = (a[row][j] - q * a[col][j]) % P
    return out % P


def inversion_parity(values: tuple[int, ...]) -> int:
    return sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    ) & 1


def witness_data() -> dict:
    active_columns = tuple(sorted(I_BY_COLUMN))
    active_rows = tuple(sorted((set(active_columns) - {P}) | {3}))
    row_n = tuple(P - u for u in active_rows)

    i_values = []
    j_values = []
    m_values = []
    for v in active_columns:
        i = I_BY_COLUMN[v]
        target = P - v
        j = target - 3 * i
        m = target - 2 * i
        assert j >= 0 and m >= 0
        i_values.append(i)
        j_values.append(j)
        m_values.append(m)

    total_i = sum(i_values)
    total_j = sum(j_values)
    total_k = P - 3 + 2 * total_i
    weight = total_j + 2 * total_k

    alternant = [
        [falling(n, m) for m in m_values]
        for n in row_n
    ]
    alternant_det = det_mod(alternant)

    scalar = 1
    for i, j in zip(i_values, j_values):
        scalar = scalar * inv(factorial(i)) * inv(factorial(j)) % P

    # Expansion sign from selected identities, -H entries, and row signs.
    def col_position(u: int) -> int:
        return u if u < 3 else u - 1

    identity_sign_parity = sum(
        u + col_position(u) for u in IDENTITY_ROWS
    ) & 1
    minus_h_parity = len(active_rows) & 1
    row_sign_parity = sum(row_n) & 1
    total_sign = -1 if (
        identity_sign_parity ^ minus_h_parity ^ row_sign_parity
    ) else 1
    signed_contribution = total_sign * scalar * alternant_det % P

    return {
        "identity_rows": IDENTITY_ROWS,
        "omitted_n": OMITTED_N,
        "active_rows": active_rows,
        "active_columns": active_columns,
        "row_n": row_n,
        "i_values": tuple(i_values),
        "j_values": tuple(j_values),
        "m_values": tuple(m_values),
        "total_i": total_i,
        "total_j": total_j,
        "total_k": total_k,
        "weight": weight,
        "boundary": BOUNDARY,
        "alternant_det_mod_23": alternant_det,
        "factorial_scalar_mod_23": scalar,
        "signed_single_assignment_contribution_mod_23": signed_contribution,
    }


def enumerate_leading_groups() -> tuple[int, list[dict]]:
    # Natural column order for this identity-selected minor.
    active_columns = tuple(sorted(I_BY_COLUMN))
    column_n = tuple(P - v for v in active_columns)
    row_n = tuple(P - u for u in sorted((set(active_columns) - {P}) | {3}))

    options: list[list[tuple[int, int, int]]] = []
    for n in column_n:
        if n == 0:
            options.append([(0, 0, 1)])
            continue
        current = []
        for i in range(n // 3 + 1):
            j = n - 3 * i
            m = n - 2 * i
            if m == 0:
                continue  # m=0 is already used by the p-column
            scalar = inv(factorial(i)) * inv(factorial(j)) % P
            current.append((i, m, scalar))
        options.append(current)

    grouped_scalar = defaultdict(int)
    grouped_count = defaultdict(int)
    chosen_m = [0] * len(options)
    total_assignments = 0

    def visit(col: int, total_i: int, used_m: int, scalar: int) -> None:
        nonlocal total_assignments
        if total_i > 34:
            return
        if col == len(options):
            if total_i != 34:
                return
            total_assignments += 1
            m_tuple = tuple(chosen_m)
            sign = -1 if inversion_parity(m_tuple) else 1
            key = tuple(sorted(m_tuple))
            grouped_scalar[key] = (
                grouped_scalar[key] + sign * scalar
            ) % P
            grouped_count[key] += 1
            return

        for i, m, factor in options[col]:
            if (used_m >> m) & 1:
                continue
            chosen_m[col] = m
            visit(
                col + 1,
                total_i + i,
                used_m | (1 << m),
                scalar * factor % P,
            )

    visit(0, 0, 0, 1)

    rows = []
    for m_set in sorted(grouped_scalar):
        matrix = [[falling(n, m) for m in m_set] for n in row_n]
        rows.append(
            {
                "m_set": m_set,
                "assignment_count": grouped_count[m_set],
                "scalar_sum_mod_23": grouped_scalar[m_set],
                "alternant_det_mod_23": det_mod(matrix),
            }
        )
    return total_assignments, rows


def main() -> None:
    witness = witness_data()
    total_assignments, groups = enumerate_leading_groups()

    assert witness["total_i"] == 34
    assert witness["total_j"] == 110
    assert witness["total_k"] == 88
    assert witness["weight"] == 286
    assert witness["weight"] > BOUNDARY
    assert witness["alternant_det_mod_23"] != 0
    assert witness["signed_single_assignment_contribution_mod_23"] != 0

    assert total_assignments == 332_192
    assert len(groups) == 18
    assert all(row["scalar_sum_mod_23"] == 0 for row in groups)

    result = {
        "status": "PASS",
        "prime": P,
        "statement": (
            "An explicit weight-286 w=1 assignment contributes nontrivially, "
            "but the complete leading coefficient of its identity-selected "
            "minor vanishes modulo 23."
        ),
        "witness": witness,
        "leading_group_assignment_count": total_assignments,
        "leading_degree_set_count": len(groups),
        "all_group_scalar_sums_zero": True,
        "groups": groups,
    }

    output = Path(__file__).with_name(
        "p23_leading_alternant_witness_results.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
