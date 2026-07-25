#!/usr/bin/env python3
"""Exact residual-gate and p-adic transport checks.

The conditional decomposition is

    S_A = eps_A * p_rho_p + E_A,       eps_A in {0,+1,-1},
    p_rho_p = T_p / p^((p-3)/2).

This script:
- reconstructs every committed N_A from the q-line ledger;
- evaluates E_A exactly for every eps_A;
- checks the strict Airy-subtracted gate;
- checks the raw tolerance ratios with the class-specific d_A;
- verifies v_p(p_rho_p)=-(p-17)/6, including v_11(p_rho_11)=1.
"""

from __future__ import annotations

import math
from fractions import Fraction

EXACT_T = {
    11: 322102,
    17: 11899821517,
    23: -1010446643080743,
    29: -798145148362709627351,
    53: 625211553014678241605175931243651758726469297,
    71: 36727396978062655326395765238086038211050946366161670340353263984,
}

# S_0, S_chi and finite boundary counts from the committed exact ledgers.
LEDGER = {
    11: dict(S0=-44, Schi=-66, Bp=0, Bm=6),
    17: dict(S0=34, Schi=-136, Bp=0, Bm=4),
    23: dict(S0=322, Schi=92, Bp=0, Bm=6),
    29: dict(S0=-232, Schi=-290, Bp=0, Bm=2),
    53: dict(S0=424, Schi=-954, Bp=0, Bm=0),
    71: dict(S0=-710, Schi=284, Bp=0, Bm=0),
}

EXPECTED_VALUATIONS = {
    11: 1,
    17: 0,
    23: -1,
    29: -2,
    53: -6,
    71: -9,
}

EXPECTED_RAW_USAGE = {
    11: 0.56,
    17: 0.33,
    23: 0.43,
    29: 0.33,
    53: 0.25,
    71: 0.10,
}


def p_rho(p: int) -> Fraction:
    return Fraction(EXACT_T[p], p ** ((p - 3) // 2))


def valuation_integer(n: int, p: int) -> int:
    n = abs(n)
    value = 0
    while n and n % p == 0:
        value += 1
        n //= p
    return value


def valuation_fraction(x: Fraction, p: int) -> int:
    return valuation_integer(x.numerator, p) - valuation_integer(x.denominator, p)


def class_row(p: int, A: int) -> tuple[int, int, int, int]:
    ledger = LEDGER[p]
    boundary = ledger["Bp"] if A == 1 else ledger["Bm"]
    S_A = ledger["S0"] + A * ledger["Schi"]
    C_A = p - 2 + boundary
    d_A = min(C_A, 2 * p - C_A)
    N_A = Fraction(C_A) - Fraction(S_A, 2 * p)
    assert N_A.denominator == 1 and N_A >= 0
    return S_A, C_A, d_A, int(N_A)


def check_valuations() -> None:
    print("=== p-adic valuation of the normalized Airy term ===")
    print(f"{'p':>4} {'v_p(T_p)':>9} {'(p-3)/2':>9} {'v_p(p rho_p)':>13} {'p rho_p':>24}")
    for p in sorted(EXACT_T):
        v_t = valuation_integer(EXACT_T[p], p)
        assert v_t == (p + 4) // 3
        actual = valuation_fraction(p_rho(p), p)
        predicted = -((p - 17) // 6)
        assert actual == predicted == EXPECTED_VALUATIONS[p]
        print(f"{p:>4} {v_t:>9} {(p-3)//2:>9} {actual:>13} {str(p_rho(p)):>24}")
    print("VALUATION IDENTITY: PASS\n")


def check_gate() -> None:
    print("=== exact residual gate ===")
    print(
        f"{'p':>4} {'A':>3} {'N_A':>5} {'S_A':>7} {'d_A':>5} "
        f"{'eps':>4} {'E_A':>26} {'threshold':>11} {'pass?':>6}"
    )

    failures: list[tuple[int, int, int]] = []
    for p in sorted(LEDGER):
        pr = p_rho(p)
        for A in (1, -1):
            S_A, _, d_A, N_A = class_row(p, A)
            threshold = 2 * p * d_A - 2 * (p - 1) * math.sqrt(p)
            for eps in (0, 1, -1):
                E_A = Fraction(S_A) - eps * pr
                passed = abs(float(E_A)) < threshold
                if not passed:
                    failures.append((p, A, eps))
                shown = str(E_A) if len(str(E_A)) <= 26 else f"{float(E_A):.6e}"
                print(
                    f"{p:>4} {A:>+3} {N_A:>5} {S_A:>7} {d_A:>5} "
                    f"{eps:>+4} {shown:>26} {threshold:>11.1f} "
                    f"{'PASS' if passed else 'FAIL':>6}"
                )
        print()

    assert failures == [(11, 1, 1)], failures
    print("EXPECTED UNIQUE STRICT-GATE FAILURE (11,+1,+1): PASS\n")


def check_raw_usage() -> None:
    print("=== raw tolerance usage ===")
    print(f"{'p':>4} {'max class ratio':>16} {'rounded':>9}")
    for p in sorted(LEDGER):
        ratios = []
        for A in (1, -1):
            S_A, _, d_A, _ = class_row(p, A)
            ratios.append(abs(S_A) / (2 * p * d_A))
        ratio = max(ratios)
        rounded = round(ratio, 2)
        assert rounded == EXPECTED_RAW_USAGE[p], (p, ratio, rounded)
        print(f"{p:>4} {ratio:>16.6f} {rounded:>9.2f}")
    print("RAW USAGE TABLE: PASS\n")


def check_integrality_dichotomy() -> None:
    print("=== integrality dichotomy ===")
    for p in sorted(LEDGER):
        for A in (1, -1):
            S_A, _, _, _ = class_row(p, A)
            for eps in (1, -1):
                E_A = Fraction(S_A) - eps * p_rho(p)
                if p > 17:
                    assert E_A.denominator > 1
                    assert valuation_fraction(E_A, p) == EXPECTED_VALUATIONS[p]
            assert Fraction(S_A).denominator == 1
    print("NONZERO EPS REQUIRES A TWISTED RESIDUAL FOR p>17: PASS")


def main() -> None:
    check_valuations()
    check_gate()
    check_raw_usage()
    check_integrality_dichotomy()
    print("RESIDUAL_GATE_MEASUREMENT_VERIFY: PASS")


if __name__ == "__main__":
    main()
