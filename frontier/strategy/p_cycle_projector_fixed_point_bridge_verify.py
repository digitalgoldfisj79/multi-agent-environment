#!/usr/bin/env python3
"""Exact checks for the p-cycle projector, fixed-point circularity, and q-line bridge.

This verifier checks only finite character/algebra identities and committed exact
census data. It does not claim a uniform positivity theorem.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from fractions import Fraction
from math import factorial
from pathlib import Path
from typing import Iterable

OUT = Path(__file__).with_name("p_cycle_projector_fixed_point_bridge_results_20260726.json")


@dataclass(frozen=True)
class Row:
    p: int
    I4: int
    s: int
    N2: int
    Nplus: int
    Nminus: int
    S0: int | None = None
    Bplus: int | None = None
    Bminus: int | None = None
    T_air_raw: int | None = None


ROWS = [
    Row(5, 124, 0, 1, 4, 6, T_air_raw=0),
    Row(7, 426, 1, 1, 10, 8),
    Row(11, 1660, 1, 1, 14, 14, S0=-44, Bplus=0, Bminus=6, T_air_raw=322102),
    Row(13, 1572, 0, 2, 10, 6),
    Row(17, 4640, 0, 1, 18, 14, S0=34, Bplus=0, Bminus=4, T_air_raw=11899821517),
    Row(23, 9636, -1, 2, 12, 22, S0=322, Bplus=0, Bminus=6, T_air_raw=-1010446643080743),
]


def partitions(n: int, max_part: int | None = None) -> Iterable[tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def z_lambda(part: tuple[int, ...]) -> int:
    counts: dict[int, int] = {}
    for x in part:
        counts[x] = counts.get(x, 0) + 1
    z = 1
    for length, multiplicity in counts.items():
        z *= (length ** multiplicity) * factorial(multiplicity)
    return z


def det_one_minus_standard(part: tuple[int, ...]) -> int:
    # det(1-g | Std) is the t->1 limit of prod(1-t^ell)/(1-t).
    # It vanishes unless there is one cycle, and equals its length then.
    return part[0] if len(part) == 1 else 0


def check_projector(primes: Iterable[int]) -> dict[int, dict[str, int]]:
    results: dict[int, dict[str, int]] = {}
    for p in primes:
        weighted = 0
        nonzero_classes = 0
        for part in partitions(p):
            class_size = factorial(p) // z_lambda(part)
            det = det_one_minus_standard(part)
            weighted += class_size * det
            if det:
                nonzero_classes += 1
                assert part == (p,) and det == p
        assert weighted == factorial(p)
        assert nonzero_classes == 1
        results[p] = {
            "weighted_character_sum": weighted,
            "group_order": factorial(p),
            "nonzero_conjugacy_classes": nonzero_classes,
        }
    return results


def sign_coefficient(p: int) -> int:
    def legendre(a: int) -> int:
        a %= p
        if a == 0:
            return 0
        return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

    return ((1 - legendre(-1)) // 2) * legendre(-6)


def exact_tmid_from_I4(row: Row) -> int:
    numerator = row.I4 + 1 - row.p**3
    assert numerator % (row.p - 1) == 0
    return numerator // (row.p - 1) - row.s * row.p


def exact_I4_from_orbits(row: Row) -> int:
    p = row.p
    return (
        (p - 1)
        + p * (p - 1) * row.N2
        + p * (p - 1) * (row.Nplus + row.Nminus) // 2
    )


def exact_tmid_from_counts(row: Row) -> int:
    p = row.p
    W = row.N2 + (row.Nplus + row.Nminus) // 2
    assert (row.Nplus + row.Nminus) % 2 == 0
    return p * (W - (p + 1 + row.s))


def exact_tmid_from_qline(row: Row) -> int | None:
    if row.S0 is None:
        return None
    assert row.Bplus is not None and row.Bminus is not None
    numerator = row.p * (2 * row.N2 - 6 - 2 * row.s + row.Bplus + row.Bminus) - row.S0
    assert numerator % 2 == 0
    return numerator // 2


def normalized_airy(row: Row) -> Fraction | None:
    if row.T_air_raw is None:
        return None
    return Fraction(row.T_air_raw, row.p ** ((row.p - 3) // 2))


def check_rows() -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for row in ROWS:
        assert row.s == sign_coefficient(row.p)
        assert row.I4 == exact_I4_from_orbits(row)

        t1 = exact_tmid_from_I4(row)
        t2 = exact_tmid_from_counts(row)
        assert t1 == t2

        W = row.N2 + (row.Nplus + row.Nminus) // 2
        assert Fraction(t1, row.p) + row.p + 1 + row.s == W
        assert (t1 > -row.p * (row.p + 1 + row.s)) == (row.I4 > row.p - 1) == (W > 0)

        tq = exact_tmid_from_qline(row)
        if tq is not None:
            assert tq == t1
            assert row.Bplus is not None and row.Bminus is not None
            s0_recovered = row.p * (
                2 * (row.p - 2) + row.Bplus + row.Bminus - row.Nplus - row.Nminus
            )
            assert s0_recovered == row.S0

        air = normalized_airy(row)
        out.append(
            {
                **asdict(row),
                "Tmid": t1,
                "W": W,
                "threshold": -row.p * (row.p + 1 + row.s),
                "qline_bridge_Tmid": tq,
                "normalized_airy": None if air is None else str(air),
                "airy_equals_Tmid": None if air is None else air == t1,
            }
        )

    # The p=11 equality is a genuine exact coincidence, not a uniform identity.
    assert normalized_airy(ROWS[2]) == exact_tmid_from_I4(ROWS[2]) == 22
    assert normalized_airy(ROWS[4]) == 29 != exact_tmid_from_I4(ROWS[4]) == -17
    assert normalized_airy(ROWS[5]) == Fraction(-561, 23) != exact_tmid_from_I4(ROWS[5]) == -92
    return out


def main() -> None:
    projector = check_projector([5, 7, 11, 13, 17, 23])
    rows = check_rows()
    result = {
        "status": "PASS",
        "projector": projector,
        "rows": rows,
        "identities": {
            "fixed_point_count": "#Fix(F sigma | X_p) = p I4 + p",
            "projector": "sum_i (-1)^i Tr(F|M_i) = Tr(F sigma|H^2_prim(Y_p))",
            "circularity": "Tmid = (I4+1-p^3)/(p-1) - s p",
            "orbit_quantization": "Tmid = p(N2+(Nplus+Nminus)/2-(p+1+s))",
            "qline_bridge": "Tmid = p(N2-3-s+(Bplus+Bminus)/2)-S0/2",
            "crown_equivalence": "Tmid > -p(p+1+s) iff I4>p-1 iff W>0",
        },
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("P_CYCLE_PROJECTOR_FIXED_POINT_BRIDGE_VERIFY: PASS")
    for row in rows:
        print(
            f"p={row['p']:>2} I4={row['I4']:>5} Tmid={row['Tmid']:>4} "
            f"W={row['W']:>2} threshold={row['threshold']:>5} "
            f"Airy={row['normalized_airy']}"
        )
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
