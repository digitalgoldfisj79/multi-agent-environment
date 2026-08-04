#!/usr/bin/env python3
"""Scale audit for the direct four-prime covariance lane."""

import math


def run() -> None:
    for x in (10**4, 10**6, 10**8, 10**10):
        logx = math.log(x)
        n = x / logx
        h = x * x
        loss = math.sqrt(logx)  # representative admissible o(log X) loss
        main = n * x * x
        target = n * x * loss
        pairs = n * h
        per_pair = target / pairs
        raw_loss = main / target
        print(
            f"X={x} N~{n:.6g} main~{main:.6g} target~{target:.6g} "
            f"raw_to_target={raw_loss:.6g} required_avg_error={per_pair:.6g}"
        )
        assert math.isclose(raw_loss, x / loss, rel_tol=1e-12)
        assert math.isclose(per_pair, loss / x, rel_tol=1e-12)
    print("FORTUNE_INT_ISC_I3_SCALE_OBSTRUCTION_PASS")


if __name__ == "__main__":
    run()
