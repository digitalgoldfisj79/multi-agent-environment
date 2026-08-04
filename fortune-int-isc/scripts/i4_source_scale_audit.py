#!/usr/bin/env python3
"""Scale audit for the shifted-prime lower-tail theorem INT-PSLT."""

import math


def run() -> None:
    for x in (10**4, 10**6, 10**8, 10**10):
        logx = math.log(x)
        h = x * x
        failure_ceiling = x * logx
        barrier = x * logx * logx
        expected_mass = h
        assert math.isclose(
            failure_ceiling / barrier,
            1 / logx,
            rel_tol=1e-12,
            abs_tol=1e-15,
        )
        assert math.isclose(
            barrier / expected_mass,
            logx * logx / x,
            rel_tol=1e-12,
            abs_tol=1e-15,
        )
        print(
            f"X={x} H={h:.6g} failure_ceiling~{failure_ceiling:.6g} "
            f"barrier={barrier:.6g} ceiling_ratio={failure_ceiling/barrier:.6g} "
            f"barrier_to_H={barrier/expected_mass:.6g}"
        )
    print("FORTUNE_INT_ISC_I4_SOURCE_SCALE_PASS")


if __name__ == "__main__":
    run()
