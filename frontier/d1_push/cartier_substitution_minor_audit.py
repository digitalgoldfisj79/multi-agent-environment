#!/usr/bin/env python3
"""Exact audit of dominant-w=1 grouped Cartier coefficients.

The grouped scalar attached to column-deficit set Q and falling-factorial
degree set M is the minor of the substitution matrix

    B[q,m] = 1/m! * [x^q](x+x^3)^m.

This replaces assignment enumeration by Cauchy--Binet.  The script audits the
committed p=17,19,23 examples and the first counterexample at p=29.
Only the Python standard library is used.
"""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from math import factorial
from pathlib import Path

CASES = (
    (17, (1, 2, 4), 17),
    (19, (1, 2, 5), 19),
    (23, (1, 2, 5, 6, 7), 34),
    (29, (1, 2, 4, 5, 7, 8), 43),
)


def inv(x: int, p: int) -> int:
    return pow(x % p, p - 2, p)


def falling(n: int, m: int, p: int) -> int:
    out = 1
    for r in range(m):
        out = out * (n - r) % p
    return out


def det_mod(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    n = len(a)
    out = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            out = -out
        pv = a[col][col] % p
        out = out * pv % p
        ipv = inv(pv, p)
        for row in range(col + 1, n):
            if not a[row][col]:
                continue
            q = a[row][col] * ipv % p
            for j in range(col, n):
                a[row][j] = (a[row][j] - q * a[col][j]) % p
    return out % p


def substitution_entry(q: int, m: int, p: int) -> int:
    """Return 1/m! [x^q](x+x^3)^m modulo p."""
    if q < m or (q - m) & 1:
        return 0
    i = (q - m) // 2
    j = m - i
    if i < 0 or j < 0:
        return 0
    return inv(factorial(i), p) * inv(factorial(j), p) % p


def compatible_degree_sets(
    p: int, omitted_n: tuple[int, ...], target_i: int
) -> dict[int, int]:
    """DP over assignments; return degree-set bitmask -> assignment count."""
    active_n = [n for n in range(1, p) if n not in omitted_n]
    assert p - 3 in active_n
    q_values = [0] + [n for n in active_n if n != p - 3]

    columns: list[tuple[int, list[tuple[int, int]]]] = []
    for q in q_values:
        choices = [(i, q - 2 * i) for i in range(q // 3 + 1)]
        columns.append((q, choices))
    columns.sort(key=lambda item: (len(item[1]), item[0]))

    suffix_min = [0] * (len(columns) + 1)
    suffix_max = [0] * (len(columns) + 1)
    for idx in range(len(columns) - 1, -1, -1):
        i_values = [i for i, _ in columns[idx][1]]
        suffix_min[idx] = suffix_min[idx + 1] + min(i_values)
        suffix_max[idx] = suffix_max[idx + 1] + max(i_values)

    states: dict[tuple[int, int], int] = {(0, 0): 1}
    for idx, (_, choices) in enumerate(columns):
        next_states: defaultdict[tuple[int, int], int] = defaultdict(int)
        for (mask, total_i), count in states.items():
            for i, m in choices:
                new_i = total_i + i
                if new_i + suffix_min[idx + 1] > target_i:
                    continue
                if new_i + suffix_max[idx + 1] < target_i:
                    continue
                if (mask >> m) & 1:
                    continue
                next_states[(mask | (1 << m), new_i)] += count
        states = dict(next_states)

    return {
        mask: count
        for (mask, total_i), count in states.items()
        if total_i == target_i
    }


def identity_expansion_sign(p: int, omitted_n: tuple[int, ...]) -> int:
    identity_rows = tuple(sorted(p - n for n in omitted_n))

    def column_position(row: int) -> int:
        return row if row < 3 else row - 1

    identity_parity = sum(
        row + column_position(row) for row in identity_rows
    ) & 1
    active_count = (p - 1) - len(omitted_n)
    minus_h_parity = active_count & 1
    row_sign_parity = sum(
        n for n in range(1, p) if n not in omitted_n
    ) & 1
    return -1 if (
        identity_parity ^ minus_h_parity ^ row_sign_parity
    ) else 1


def audit_case(p: int, omitted_n: tuple[int, ...], target_i: int) -> dict:
    active_n_desc = tuple(
        n for n in range(p - 1, 0, -1) if n not in omitted_n
    )
    q_desc = tuple(n for n in active_n_desc if n != p - 3) + (0,)
    groups = compatible_degree_sets(p, omitted_n, target_i)

    grouped_rows = []
    coefficient = 0
    for mask, assignment_count in sorted(groups.items()):
        m_set = tuple(m for m in range(p) if (mask >> m) & 1)
        scalar_minor = det_mod(
            [[substitution_entry(q, m, p) for m in m_set] for q in q_desc],
            p,
        )
        alternant = det_mod(
            [[falling(n, m, p) for m in m_set] for n in active_n_desc],
            p,
        )
        contribution = scalar_minor * alternant % p
        coefficient = (coefficient + contribution) % p
        grouped_rows.append(
            {
                "m_set": m_set,
                "assignment_count": assignment_count,
                "substitution_minor_mod_p": scalar_minor,
                "alternant_mod_p": alternant,
                "contribution_mod_p": contribution,
            }
        )

    sum_n = sum(active_n_desc)
    sum_q = sum(q_desc)
    c_degree = sum_q - 3 * target_i
    d_degree = sum_n - sum_q + 2 * target_i
    weight = c_degree + 2 * d_degree
    sign = identity_expansion_sign(p, omitted_n)

    return {
        "prime": p,
        "omitted_n": omitted_n,
        "identity_rows": tuple(sorted(p - n for n in omitted_n)),
        "target_a_degree": target_i,
        "c_degree": c_degree,
        "d_degree": d_degree,
        "weight": weight,
        "support_boundary": (p * p - 1) // 2,
        "assignment_count": sum(groups.values()),
        "degree_set_count": len(groups),
        "nonzero_substitution_minor_count": sum(
            row["substitution_minor_mod_p"] != 0 for row in grouped_rows
        ),
        "nonzero_alternant_count": sum(
            row["alternant_mod_p"] != 0 for row in grouped_rows
        ),
        "identity_minor_coefficient_mod_p": coefficient,
        "identity_expansion_sign": sign,
        "signed_cartier_contribution_mod_p": sign * coefficient % p,
        "zero_substitution_minor_count": sum(
            row["substitution_minor_mod_p"] == 0 for row in grouped_rows
        ),
        "nonzero_substitution_groups": [
            row for row in grouped_rows
            if row["substitution_minor_mod_p"] != 0
        ],
        "sample_zero_scalar_nonzero_alternant": next(
            (row for row in grouped_rows
             if row["substitution_minor_mod_p"] == 0
             and row["alternant_mod_p"] != 0),
            None,
        ),
        "all_group_records_sha256": hashlib.sha256(
            json.dumps(grouped_rows, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def main() -> None:
    results = [audit_case(*case) for case in CASES]

    expected = {
        17: (476, 2, 0, 0),
        19: (7054, 5, 0, 0),
        23: (332_192, 18, 0, 0),
        29: (2_166_022_375, 2177, 7, 22),
    }
    for row in results:
        assignment_count, group_count, raw, signed = expected[row["prime"]]
        assert row["assignment_count"] == assignment_count
        assert row["degree_set_count"] == group_count
        assert row["identity_minor_coefficient_mod_p"] == raw
        assert row["signed_cartier_contribution_mod_p"] == signed
        assert row["weight"] > row["support_boundary"]

    p29 = results[-1]
    assert p29["nonzero_substitution_minor_count"] == 15
    assert len(p29["nonzero_substitution_groups"]) == 15
    assert p29["nonzero_substitution_groups"][0]["substitution_minor_mod_p"] != 0

    output = {
        "status": "PASS",
        "statement": (
            "The substitution-minor cancellation holds in the selected "
            "p=17,19,23 witnesses but fails at p=29.  The p=29 identity "
            "minor has coefficient 7 mod 29 and signed Cartier contribution "
            "22 mod 29 at c^224 d^112."
        ),
        "cases": results,
    }
    path = Path(__file__).with_name(
        "cartier_substitution_minor_audit_results.json"
    )
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
