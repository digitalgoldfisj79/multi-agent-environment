#!/usr/bin/env python3
"""Measure the residual E_A from committed exact data.

The conditional gate is  S_A = eps_A * p rho_p + E_A,  eps_A in {0,+1,-1},
with  p rho_p = T_p / p^((p-3)/2)  and the sufficient condition

    |E_A| < 2 p d_A(p) - 2(p-1) sqrt(p),     d_A = min{C_A, 2p - C_A},
    C_A = p - 2 + B_A.

Every ingredient is exactly committed, so E_A is exactly computable for each
choice of eps_A.  Nobody has evaluated it.
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

# S_0, S_chi from BOUNDARY_DISCRIMINANT_AND_FOURIER_CALIBRATION (p<=29)
# and GENERIC_QLINE_ONLY_CROWN_P53_P71 (p=53,71).  B_+ = 0 proved uniformly.
LEDGER = {
    11: dict(S0=-44, Schi=-66, Bp=0, Bm=6),
    17: dict(S0=34, Schi=-136, Bp=0, Bm=4),
    23: dict(S0=322, Schi=92, Bp=0, Bm=6),
    29: dict(S0=-232, Schi=-290, Bp=0, Bm=2),
    53: dict(S0=424, Schi=-954, Bp=0, Bm=0),
    71: dict(S0=-710, Schi=284, Bp=0, Bm=0),
}


def p_rho(p: int) -> Fraction:
    """p * rho_p = T_p / p^((p-3)/2), exactly."""
    e = (p - 3) // 2
    return Fraction(EXACT_T[p], p**e)


def main() -> None:
    print("=== 1. is the transported Airy contribution even a p-adic integer? ===")
    print(f"{'p':>4} {'v_p(T_p)':>9} {'(p-3)/2':>8} {'v_p(p rho_p)':>13} {'p rho_p':>22}")
    for p in sorted(EXACT_T):
        v = 0
        t = EXACT_T[p]
        while t % p == 0:
            v += 1
            t //= p
        pr = p_rho(p)
        print(f"{p:>4} {v:>9} {(p-3)//2:>8} {v-(p-3)//2:>13} {str(pr):>22}")
    print("  predicted valuation (p-17)/6 below zero:",
          [(p, -(p - 17) // 6) for p in sorted(EXACT_T)])

    print("\n=== 2. E_A = S_A - eps * p rho_p, for each admissible eps ===")
    print(f"{'p':>4} {'A':>3} {'S_A':>7} {'d_A':>5} {'threshold':>11} "
          f"{'eps':>4} {'E_A':>26} {'|E_A|':>10} {'int?':>5} {'pass?':>6}")
    rows = []
    for p in sorted(LEDGER):
        L = LEDGER[p]
        pr = p_rho(p)
        for A, B in ((+1, L["Bp"]), (-1, L["Bm"])):
            S_A = L["S0"] + A * L["Schi"]
            C_A = p - 2 + B
            d_A = min(C_A, 2 * p - C_A)
            thr = 2 * p * d_A - 2 * (p - 1) * math.sqrt(p)
            # sanity: N_A must be a non-negative integer
            N_A = Fraction(C_A) - Fraction(S_A, 2 * p)
            assert N_A.denominator == 1 and N_A >= 0, f"bad ledger at p={p}, A={A}"
            for eps in (0, 1, -1):
                E = Fraction(S_A) - eps * pr
                ok = abs(E) < thr
                rows.append((p, A, eps, E, thr, ok))
                shown = str(E) if len(str(E)) < 26 else f"{float(E):.6e}"
                print(f"{p:>4} {A:>+3} {S_A:>7} {d_A:>5} {thr:>11.1f} "
                      f"{eps:>+4} {shown:>26} {abs(float(E)):>10.2f} "
                      f"{'yes' if E.denominator==1 else 'NO':>5} "
                      f"{'PASS' if ok else 'FAIL':>6}")
        print()

    print("=== 3. integrality verdict ===")
    for eps in (1, -1):
        bad = [(p, A) for (p, A, e, E, _, _) in rows if e == eps and E.denominator != 1]
        print(f"  eps={eps:+d}: E_A non-integral at {bad if bad else 'nowhere'}")
    bad0 = [(p, A) for (p, A, e, E, _, _) in rows if e == 0 and E.denominator != 1]
    print(f"  eps= 0: E_A non-integral at {bad0 if bad0 else 'nowhere'}")

    print("\n=== 4. observed growth of |S_A| against the p^2 gate scale ===")
    print(f"{'p':>4} {'max|S_A|':>10} {'2p*d_A':>10} {'ratio':>8} {'|S_A|/p':>9}")
    for p in sorted(LEDGER):
        L = LEDGER[p]
        vals = [abs(L["S0"] + A * L["Schi"]) for A in (1, -1)]
        m = max(vals)
        d = min(p - 2, p + 2)
        print(f"{p:>4} {m:>10} {2*p*d:>10} {m/(2*p*d):>8.4f} {m/p:>9.2f}")


if __name__ == "__main__":
    main()


def check_valuation_identity() -> None:
    """v_p(p rho_p) = -(p-17)/6, using the proved v_p(T_p) = (p+4)/3."""
    for p in sorted(EXACT_T):
        v, t = 0, EXACT_T[p]
        while t % p == 0:
            v, t = v + 1, t // p
        assert v == (p + 4) // 3, f"v_p(T_p) != (p+4)/3 at p={p}"
        pr = p_rho(p)
        vp = 0
        num, den = pr.numerator, pr.denominator
        while num % p == 0:
            vp, num = vp + 1, num // p
        while den % p == 0:
            vp, den = vp - 1, den // p
        assert vp == -((p - 17) // 6), f"v_p(p rho_p) != -(p-17)/6 at p={p}"
    print("\nVALUATION IDENTITY v_p(p rho_p) = -(p-17)/6: PASS")
    print("  => if eps_A != 0 then E_A is NOT a p-adic integer for p > 17")
    print("RESIDUAL_GATE_MEASUREMENT_VERIFY: PASS")


check_valuation_identity()
