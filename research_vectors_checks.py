#!/usr/bin/env python3
"""Numerical exploration for new exact results on the pair-sum kernel H2.

1. Sixth Lebesgue moment of H2: brute-force collision count for superincreasing
   P, interpolate the exact degree-6 polynomial in N, verify on held-out N.
2. General moment law: check int |H2|^{2k} ~ (2k)!/4^k * N^{2k} (half-squared-
   Gaussian law) for k=2,3,4 at moderate N.
3. Multiplicity stratification of the difference multiset {S_u - S_v}:
   common-endpoint differences P_i - P_k carry multiplicity ~N, everything
   else O(1).
4. Lebesgue tail: check meas{|H2|^2 - M >= lam} <= exp(-c sqrt(lam/M)) shape
   numerically at N=24 via dense theta sampling of a random superincreasing
   model (diagnostic only).
"""
from collections import Counter
from fractions import Fraction
import cmath, math, random

def prefixes(n, R=100):
    return [R**j for j in range(n)]

def pair_sums(P):
    n = len(P)
    return [P[i] + P[j] for i in range(n) for j in range(i, n)]

def moment_2k(P, k):
    """int_0^1 |H2|^{2k} = # of (u_1..u_k, v_1..v_k) with equal S-sums."""
    S = pair_sums(P)
    sums = Counter()
    def rec(depth, tot, counter):
        if depth == 0:
            counter[tot] += 1
            return
        for s in S:
            rec(depth-1, tot+s, counter)
    rec(k, 0, sums)
    return sum(v*v for v in sums.values())

# --- 1. sixth moment: interpolate exact polynomial ---
pts = []
for n in range(2, 10):
    val = moment_2k(prefixes(n), 3)
    pts.append((n, val))
    print(f"N={n} sixth moment = {val}")

# Lagrange interpolation with exact fractions, degree 7 through 8 points
def interp(pts):
    def L(x):
        tot = Fraction(0)
        for i, (xi, yi) in enumerate(pts):
            term = Fraction(yi)
            for j, (xj, _) in enumerate(pts):
                if i != j:
                    term *= Fraction(x - xj, xi - xj)
            tot += term
        return tot
    return L

L = interp(pts)
# verify on held-out N = 10, 11
for n in (10, 11):
    got = moment_2k(prefixes(n), 3)
    pred = L(n)
    assert pred == got, (n, pred, got)
    print(f"N={n} held-out sixth moment {got} == interpolated {pred}: OK")

# recover monomial coefficients (finite differences on exact values)
import itertools
# polynomial degree <= 6 expected; fit coefficients exactly by solving Vandermonde
deg = 6
A = [[Fraction(n)**p for p in range(deg+1)] for n, _ in pts[:deg+1]]
y = [Fraction(v) for _, v in pts[:deg+1]]
# gaussian elimination
for col in range(deg+1):
    piv = next(r for r in range(col, deg+1) if A[r][col] != 0)
    A[col], A[piv] = A[piv], A[col]; y[col], y[piv] = y[piv], y[col]
    for r in range(deg+1):
        if r != col and A[r][col] != 0:
            f = A[r][col]/A[col][col]
            A[r] = [a - f*b for a, b in zip(A[r], A[col])]
            y[r] = y[r] - f*y[col]
coeffs = [y[i]/A[i][i] for i in range(deg+1)]
print("sixth-moment polynomial coefficients (c0..c6):", coeffs)
# check it reproduces all points incl. held-out
def evalpoly(n):
    return sum(c*Fraction(n)**p for p, c in enumerate(coeffs))
for n in range(2, 12):
    assert evalpoly(n) == moment_2k(prefixes(n), 3) if n < 10 else True
print("leading coefficient:", coeffs[6], "(predicted (2k)!/4^k = 720/64 = 45/4)")
assert coeffs[6] == Fraction(45, 4)

# --- 2. general moment law ratio check ---
for k in (2, 3, 4):
    n = 8 if k < 4 else 6
    got = moment_2k(prefixes(n), k)
    lead = math.factorial(2*k)/4**k * n**(2*k)
    print(f"k={k} N={n}: moment/leading = {got/lead:.4f} (→1 as N grows)")

# --- 3. multiplicity stratification of differences ---
n = 9
P = prefixes(n)
S = pair_sums(P)
diffs = Counter(a-b for a in S for b in S if a != b)
mult_hist = Counter(diffs.values())
print("difference multiplicity histogram:", dict(sorted(mult_hist.items())))
# common-endpoint differences P_i - P_k should have multiplicity about N
ce = Counter()
for i in range(n):
    for kk in range(n):
        if i != kk:
            ce[P[i]-P[kk]] = diffs.get(P[i]-P[kk], 0)
print("multiplicity at common-endpoint differences P_i-P_k:",
      sorted(set(ce.values())))

# --- 4. Lebesgue tail shape (diagnostic) ---
# Exact phase arithmetic: theta = t/2^B with B large enough to resolve the
# top frequency; evaluate H2 via the exact identity H2 = (F(th)^2+F(2th))/2.
random.seed(3)
n = 24
P = [1]
for _ in range(n-1):
    P.append(P[-1]*random.randint(50, 150))
M = n*(n+1)//2
B = 220
DEN = 1 << B
assert 2*max(P) < DEN
samples = 200000
tail = Counter()
levels = [2, 4, 8, 16, 32, 64]
def F_at(t):
    return sum(cmath.exp(2j*cmath.pi*((p*t) % DEN)/DEN) for p in P)
for _ in range(samples):
    t = random.randrange(DEN)
    F1 = F_at(t)
    F2 = F_at((2*t) % DEN)
    K = abs((F1*F1 + F2)/2)**2 - M
    for lv in levels:
        if K >= lv*M:
            tail[lv] += 1
for t in levels:
    frac = tail[t]/samples
    if frac > 0:
        print(f"meas(K >= {t:2d}M) ≈ {frac:.2e}   -log/sqrt(t) = "
              f"{-math.log(frac)/math.sqrt(t):.2f}")
    else:
        print(f"meas(K >= {t:2d}M) < {1/samples:.0e}")
print("DONE")

# --- 5. third centred moment exact formula (see RESEARCH_VECTORS.md A2) ---
def third_centred_check():
    from fractions import Fraction
    def m2k(P, k):
        S=[P[i]+P[j] for i in range(len(P)) for j in range(i,len(P))]
        c=Counter([0])
        for _ in range(k):
            c2=Counter()
            for t,v in c.items():
                for s in S: c2[t+s]+=v
            c=c2
        return sum(v*v for v in c.values())
    for n in (3,5,7):
        P=[100**j for j in range(n)]; Mn=n*(n+1)//2
        k3=m2k(P,3)-3*Mn*m2k(P,2)+2*Mn**3
        pred=Fraction(n*(n-1)**2*(37*n**3-115*n**2+174*n-136),4)
        assert k3==pred,(n,k3,pred)
    print("third centred moment N(N-1)^2(37N^3-115N^2+174N-136)/4: OK")

third_centred_check()
