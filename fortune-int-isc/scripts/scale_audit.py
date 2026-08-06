#!/usr/bin/env python3
"""Executable asymptotic sanity checks for the INT-ISC loss ledger."""

from __future__ import annotations

import math


def main() -> int:
    rows = []
    for X in (10**4, 10**6, 10**8, 10**10):
        logx = math.log(X)
        # Representative admissible loss: grows, but is o(log X).
        loss = math.sqrt(logx)
        N = X / logx
        H = X * X
        baseline_sum = N * X
        variance_target = N * X * loss
        failure_cost = X * X
        max_failures = variance_target / failure_cost
        necessary_fm_error = N * math.sqrt(X * loss)
        relative_fm_error = necessary_fm_error / baseline_sum
        rows.append(
            {
                "X": X,
                "N_proxy": N,
                "H_proxy": H,
                "L_proxy": loss,
                "failure_bound_proxy": max_failures,
                "L_over_logX": loss / logx,
                "relative_first_moment_error": relative_fm_error,
            }
        )

    # Registered implications must improve along the asymptotic sequence.
    if not all(rows[i + 1]["L_over_logX"] < rows[i]["L_over_logX"] for i in range(len(rows) - 1)):
        raise SystemExit("FAIL: representative loss is not o(log X)")
    if not all(rows[i + 1]["failure_bound_proxy"] < rows[i]["failure_bound_proxy"] for i in range(len(rows) - 1)):
        raise SystemExit("FAIL: one-failure bound does not tend to zero")
    if not all(rows[i + 1]["relative_first_moment_error"] < rows[i]["relative_first_moment_error"] for i in range(len(rows) - 1)):
        raise SystemExit("FAIL: necessary first-moment error is not relatively small")

    print("FORTUNE_INT_ISC_SCALE_AUDIT_PASS")
    print("registered_N=X/logX")
    print("registered_H=X^2")
    print("registered_failure_bound=L/logX")
    print("registered_relative_FM_error=sqrt(L/X)")
    for row in rows:
        print(
            "X={X} L/logX={L_over_logX:.6g} "
            "failure_bound={failure_bound_proxy:.6g} "
            "relative_FM_error={relative_first_moment_error:.6g}".format(**row)
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
