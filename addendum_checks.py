#!/usr/bin/env python3
"""Validation suite for PAPER2_ADDENDUM.md.

Checks (numbering follows Section A.5 of the addendum):
1. Theorem A.3  — difference-multiplicity dichotomy and the exact sliding
                  family (A.3), at N = 8, 9.
2. Lemma A.6    — moment bound (A.8) against exact collision counts.
3. Remark A.9   — exact sixth moment (A.11) and third centred moment (A.12).
4. Theorem A.7  — tail bounds (A.9)/(A.10): empirical tail at N = 24 with
                  exact modular phase arithmetic, plus the calculus fact
                  f(t) <= 0 for t >= 121 used in the proof of (A.10).

Pure standard library; no external dependencies.
"""
from collections import Counter
from fractions import Fraction
import cmath, math, random

R = 100  # superincreasing ratio for finite models (plays the role of X > 5)


def prefixes(n):
    return [R**j for j in range(n)]


def index_pairs(n):
    return [(i, j) for i in range(n) for j in range(i, n)]


# ---------------------------------------------------------------- check 1
def check_dichotomy():
    for n in (8, 9):
        P = prefixes(n)
        pairs = index_pairs(n)
        M = len(pairs)
        S = {u: P[u[0]] + P[u[1]] for u in pairs}
        reps = {}
        for u in pairs:
            for v in pairs:
                if u != v:
                    reps.setdefault(S[u] - S[v], []).append((u, v))
        hist = Counter(len(r) for r in reps.values())
        walk_count = n * (n - 1)
        sidon_count = M * (M - 1) - n * n * (n - 1)
        assert hist == Counter({1: sidon_count, n: walk_count}), (n, hist)
        # multiplicity-N differences are exactly P_i - P_k with the exact
        # sliding family (A.3)
        for i in range(n):
            for k in range(n):
                if i == k:
                    continue
                D = P[i] - P[k]
                got = sorted(reps[D])
                want = sorted(
                    ((min(i, t), max(i, t)), (min(k, t), max(k, t)))
                    for t in range(n))
                assert got == want, (n, i, k)
        print(f"check 1 (Theorem A.3) N={n}: histogram "
              f"{{1: {sidon_count}, {n}: {walk_count}}} and sliding family exact: OK")


# ---------------------------------------------------------------- check 2
def moment_count(P, k):
    """Exact integer value of int_0^1 |H2|^{2k} by collision counting."""
    S = [P[i] + P[j] for i in range(len(P)) for j in range(i, len(P))]
    c = Counter([0])
    for _ in range(k):
        c2 = Counter()
        for tot, v in c.items():
            for s in S:
                c2[tot + s] += v
        c = c2
    return sum(v * v for v in c.values())


def check_moment_bound():
    for k in (2, 3, 4):
        for n in ((5, 7, 9) if k < 4 else (5, 6)):
            got = moment_count(prefixes(n), k)
            M = n * (n + 1) // 2
            bound = math.factorial(2 * k) * M**k // 2**k
            assert got <= bound, (k, n, got, bound)
        print(f"check 2 (Lemma A.6) k={k}: exact count <= (2k)!/2^k M^k: OK")


# ---------------------------------------------------------------- check 3
def check_exact_moments():
    for n in range(2, 12):
        got = moment_count(prefixes(n), 3)
        want = Fraction(45*n**6 - 189*n**5 + 438*n**4 - 597*n**3
                        + 443*n**2 - 136*n, 4)
        assert got == want, (n, got, want)
    print("check 3 (A.11) sixth moment exact for N=2..11: OK")
    for n in (3, 5, 7):
        M = n * (n + 1) // 2
        k3 = moment_count(prefixes(n), 3) \
            - 3 * M * moment_count(prefixes(n), 2) + 2 * M**3
        want = Fraction(n*(n-1)**2*(37*n**3 - 115*n**2 + 174*n - 136), 4)
        assert k3 == want, (n, k3, want)
    print("check 3 (A.12) third centred moment exact for N=3,5,7: OK")


# ---------------------------------------------------------------- check 4
def check_tail():
    # calculus fact used in the proof of (A.10)
    def f(t):
        return 3 + 0.25*math.log(2*(t+1)) - math.sqrt(2*(t+1)) + math.sqrt(t)
    assert f(121) < -0.2, f(121)
    ts = [121 * (1.1**j) for j in range(150)]
    assert all(f(b) < f(a) + 1e-12 for a, b in zip(ts, ts[1:]))
    print("check 4 f(121) < 0 and f decreasing on [121, 1e8]: OK")

    # empirical tail at N=24, exact modular phase arithmetic
    random.seed(3)
    n = 24
    P = [1]
    for _ in range(n - 1):
        P.append(P[-1] * random.randint(50, 150))
    M = n * (n + 1) // 2
    B = 220
    DEN = 1 << B
    assert 2 * max(P) < DEN
    samples = 200000
    levels = [2, 4, 8, 16, 32, 64]
    tail = Counter()

    def F_at(t):
        return sum(cmath.exp(2j * cmath.pi * ((p * t) % DEN) / DEN) for p in P)

    for _ in range(samples):
        t = random.randrange(DEN)
        F1 = F_at(t)
        F2 = F_at((2 * t) % DEN)
        K = abs((F1 * F1 + F2) / 2)**2 - M
        for lv in levels:
            if K >= lv * M:
                tail[lv] += 1
    for lv in levels:
        emp = tail[lv] / samples
        s_over_M = lv + 1  # s = M + lambda, lambda = lv*M
        bound = math.e**3 * (2 * s_over_M)**0.25 \
            * math.exp(-math.sqrt(2 * s_over_M))
        assert emp <= bound, (lv, emp, bound)
        c_emp = -math.log(emp) / math.sqrt(lv) if emp > 0 else float('inf')
        print(f"check 4 (A.9) lambda={lv:2d}M: empirical {emp:.2e} <= "
              f"bound {bound:.2e}; exponent constant {c_emp:.2f}")


if __name__ == "__main__":
    check_dichotomy()
    check_moment_bound()
    check_exact_moments()
    check_tail()
    print("ADDENDUM_CHECKS_PASS")
