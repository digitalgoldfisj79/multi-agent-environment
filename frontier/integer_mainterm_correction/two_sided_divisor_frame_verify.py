#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import divisors, factorint, mobius, primerange


def von_mangoldt(n: int) -> float:
    fac = factorint(n)
    if len(fac) != 1:
        return 0.0
    p, _ = next(iter(fac.items()))
    return math.log(p)


def direct(P: int, H: int) -> float:
    return sum(von_mangoldt(m) * von_mangoldt(P + m) for m in range(2, H + 1))


def divisor_identity(P: int, H: int) -> float:
    total = 0.0
    for m in range(2, H + 1):
        left = -sum(int(mobius(d)) * math.log(d) for d in divisors(m))
        right = -sum(int(mobius(e)) * math.log(e) for e in divisors(P + m))
        total += left * right
    return total


def crt_frame(P: int, H: int) -> tuple[float, float, float]:
    ds = sorted({d for m in range(2, H + 1) for d in divisors(m) if mobius(d)})
    es = sorted({e for m in range(2, H + 1) for e in divisors(P + m) if mobius(e)})
    exact = 0.0
    principal = 0.0
    discrepancy = 0.0
    for d in ds:
        wd = int(mobius(d)) * math.log(d)
        if wd == 0:
            continue
        for e in es:
            we = int(mobius(e)) * math.log(e)
            if we == 0:
                continue
            g = math.gcd(d, e)
            solvable = (P % g == 0)
            count = sum(1 for m in range(2, H + 1) if m % d == 0 and (P + m) % e == 0)
            exact += wd * we * count
            if solvable:
                lcm = d // g * e
                main_count = (H - 1) / lcm
                principal += wd * we * main_count
                discrepancy += wd * we * (count - main_count)
            elif count:
                raise AssertionError((P, H, d, e, count))
    return exact, principal, discrepancy


def main() -> None:
    rows = []
    P = 1
    targets = {5, 7, 11, 13, 17, 19}
    for p in primerange(2, 20):
        P *= int(p)
        if p not in targets:
            continue
        H = 40
        direct_value = direct(P, H)
        divisor_value = divisor_identity(P, H)
        frame, principal, discrepancy = crt_frame(P, H)
        row = {
            "p": int(p),
            "P": P,
            "H": H,
            "direct": direct_value,
            "divisor_identity": divisor_value,
            "crt_frame": frame,
            "principal": principal,
            "discrepancy": discrepancy,
            "principal_plus_discrepancy": principal + discrepancy,
            "max_abs_error": max(
                abs(direct_value - divisor_value),
                abs(direct_value - frame),
                abs(frame - principal - discrepancy),
            ),
        }
        rows.append(row)
        print(row)
        if row["max_abs_error"] > 1e-9:
            raise SystemExit("verification failed")
    Path("two_sided_divisor_frame_results.json").write_text(json.dumps(rows, indent=2))
    print("ALL TWO-SIDED DIVISOR-FRAME CHECKS PASSED")


if __name__ == "__main__":
    main()
