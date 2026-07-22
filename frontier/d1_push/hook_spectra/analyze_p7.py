#!/usr/bin/env python3
"""
p=7 hypothesis tests from the cycle-type census (j <= jmax, default 7):

  h_i = [2, 10, 23, 32, 23, 10, 1]  (ledger)

  T1. L_0 = (1-T)^2, L_6 = 1 - chi(u_q) T           (exact, validated all j)
  T2. L_1 = puncture prediction                      (validated all j)
  T3. L_5 = W0(T) * L(D_q):  W0 quadratic solved from j=1,2, validated j>=3
  T4. E_j table; R_j := E_j - chi(u_q)^j + TrD_j  -> the residual surviving
      even-side object (V_2 + V_4 - V_3 weight-1 + residual weight-0)
  T5. configuration counts N2_j = sum n(n-1), N3_j = sum n(n-1)(n-2)
"""
import json, os, sys
from fractions import Fraction
import sympy as sp

P = 7
JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7
T = sp.symbols('T')

H = [2, 10, 23, 32, 23, 10, 1]
CHI_U = {1: 1, 3: -1, 4: 1, 5: -1, 6: -1}

# L(D_q) computed independently (genus4_p7.py, j=5-validated)
LD = {
 1: (49*T**4 - 7*T**3 - 7*T**2 - T + 1)*(49*T**4 + 21*T**3 + 13*T**2 + 3*T + 1),
 3: (49*T**4 - 7*T**3 - 2*T**2 - T + 1)*(49*T**4 + 21*T**3 + 6*T**2 + 3*T + 1),
 4: (49*T**4 + 6*T**2 + 1)*(49*T**4 - 28*T**3 + 10*T**2 - 4*T + 1),
 5: (7*T**2 - 4*T + 1)*(7*T**2 + T + 1)*(49*T**4 - 21*T**3 + 6*T**2 - 3*T + 1),
 6: (49*T**4 + 21*T**3 + 9*T**2 + 3*T + 1)*(49*T**4 + 21*T**3 + 13*T**2 + 3*T + 1),
}
# L_1 predictions from critical-fiber factorizations over F_7
L1PRED = {
 1: (1-T)**2 * (1+T+T**2+T**3+T**4)**2,
 3: (1-T)**6 * (1+T+T**2)**2,
 4: (1-T)**4 * (1+T)**2 * (1+T**2)**2,
 5: (1-T)**4 * (1+T)**2 * (1+T+T**2)**2,
 6: (1-T)**2 * (1+T+T**2+T**3+T**4)**2,
}

def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield (); return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

def build_etab(p):
    t = sp.symbols('t')
    tab = {}
    for typ in partitions(p):
        prod = 1
        for d in typ:
            prod *= (1 - (-t)**d)
        qq, r = sp.div(sp.Poly(sp.expand(prod), t), sp.Poly(1 + t, t))
        assert r.is_zero
        tab[typ] = tuple(int(qq.coeff_monomial(t**i)) for i in range(p))
    return tab

ETAB = build_etab(P)

def powersums_of(Lpoly, jmax):
    """Power sums of reciprocal roots of polynomial L(T) (constant term 1)."""
    c = sp.Poly(sp.expand(Lpoly), T).all_coeffs()[::-1]
    h = len(c) - 1
    s = {}
    for j in range(1, jmax + 1):
        acc = Fraction(int(c[j])) * j if j <= h else Fraction(0)
        for m in range(1, min(j, h) + 1):
            if j - m >= 1:
                acc += Fraction(int(c[m])) * s[j - m]
        s[j] = -acc
    return s

def main():
    for q in [1, 3, 4, 5, 6]:
        data = {}
        for j in range(1, JMAX + 1):
            fn = f"cycle_counts_p7_j{j}_q{q}.json"
            if not os.path.exists(fn): break
            data[j] = {tuple(map(int, k.split(","))): v
                       for k, v in json.load(open(fn)).items()}
        if not data:
            print(f"q={q}: no data"); continue
        jmax = max(data)
        Pj = {i: {} for i in range(P)}
        Ej, N2, N3 = {}, {}, {}
        for j in sorted(data):
            Tv = [0] * P
            n2 = n3 = 0
            for typ, n in data[j].items():
                e = ETAB[typ]
                for i in range(P):
                    Tv[i] += n * e[i]
                n1 = sum(1 for d in typ if d == 1)
                n2 += n * n1 * (n1 - 1)
                n3 += n * n1 * (n1 - 1) * (n1 - 2)
            for i in range(P):
                Pj[i][j] = (P**j if i == 0 else 0) - Tv[i]
            Ej[j] = P**j - P * data[j].get((P,), 0)
            N2[j], N3[j] = n2, n3
            assert sum((-1)**i * Pj[i][j] for i in range(P)) == Ej[j]
        print(f"\n================ p=7 q={q} (jmax={jmax}) ================")
        for i in range(P):
            print(f"  P_j(V_{i}) h={H[i]}: {[Pj[i][j] for j in sorted(Pj[i])]}")
        # T1
        ok0 = all(Pj[0][j] == 2 for j in Pj[0])
        ok6 = all(Pj[6][j] == CHI_U[q]**j for j in Pj[6])
        print(f"  T1: L_0=(1-T)^2: {ok0};  L_6=1-({CHI_U[q]})T: {ok6}")
        # T2
        s1 = powersums_of(L1PRED[q], jmax)
        ok1 = all(s1[j] == Pj[1][j] for j in range(1, jmax + 1))
        print(f"  T2: L_1 puncture prediction: {ok1}")
        # T3: L_5 = W0 * L(D_q)
        sD = powersums_of(LD[q], jmax)
        a = Fraction(Pj[5][1]) - sD[1]          # alpha+beta
        b = Fraction(Pj[5][2]) - sD[2]          # alpha^2+beta^2
        ab = (a * a - b) / 2
        ok5 = all(Pj[5][j] - sD[j] == power_sum_pair(a, ab, j) for j in range(1, jmax + 1))
        print(f"  T3: L_5 = W0 * L(D_q), W0 = 1 - ({a})T + ({ab})T^2 : {ok5}")
        # T4
        Rj = {j: Ej[j] - CHI_U[q]**j + sD[j] for j in sorted(Ej)}
        print(f"  E_j: {[Ej[j] for j in sorted(Ej)]}")
        print(f"  T4 R_j = E_j - chi(u)^j + TrD_j: {[sp.nsimplify(Rj[j]) for j in sorted(Rj)]}")
        print(f"  T5 N2_j: {[N2[j] for j in sorted(N2)]}")
        print(f"     N3_j: {[N3[j] for j in sorted(N3)]}")

def power_sum_pair(s1, e2, j):
    """Power sums of the two roots of x^2 - s1 x + e2."""
    p_prev, p_cur = Fraction(2), s1
    if j == 0: return p_prev
    for _ in range(j - 1):
        p_prev, p_cur = p_cur, s1 * p_cur - e2 * p_prev
    return p_cur

if __name__ == "__main__":
    main()
