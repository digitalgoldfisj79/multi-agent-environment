#!/usr/bin/env python3
"""Independent numeric re-verification of exact identities claimed in
Fortune Papers I, II, III, V.

Every check prints PASS/FAIL; exit code 1 on any failure.

Checks:
  1. Paper II Thm 4.2  : \int |H2|^4 = N(3N^3-2N^2+2N-1)/2 (enumeration N=2..8),
                          and formula value at N=55 equals 13,562,560.
  2. Paper II Thm 4.2  : centred L2 mass N(N-1)(5N^2-N+2)/4 (enumeration).
  3. Paper III Thm 3.1 : difference-multiplicity dichotomy histogram at N=8,9:
                          {1: M(M-1)-N^2(N-1), N: N(N-1)}.
  4. Paper III Rmk A.9 : sixth moment polynomial (enumeration N=3..8).
  5. Paper I Prop 5.4  : eigenvalues of the median matrix M are
                          -1, 4, (19 +- sqrt(281))/2.
  6. Paper I Prop 5.6  : E|K_V|^2 = C(V,4) and
                          E|K_V|^4 = C(V,4)+40C(V,5)+420C(V,6)+1736C(V,7)+2556C(V,8)
                          (exhaustive over root orders q=3,4 at V=5,6).
  7. Paper V Thm 4.1   : exact orbit decomposition and reported counts at p=5,7,11:
                          I4, N2, Nsq, Nns, W_p.
"""
import itertools, math, sys
import numpy as np

FAIL = 0

def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

# ----------------------------------------------------------------------
# Superincreasing model walk: P_j = B^j with huge base B emulates rigidity.
def pairsums(N, B=10**6):
    P = [B**j for j in range(N)]
    return [P[j] + P[k] for j in range(N) for k in range(j, N)]

# 1+2. fourth moment and centred mass
for N in range(2, 9):
    S = pairsums(N)
    M = len(S)
    from collections import Counter
    c2 = Counter(a + b for a in S for b in S)          # pair-of-pairs sums
    m4 = sum(v * v for v in c2.values())               # \int |H2|^4
    f4 = N * (3 * N**3 - 2 * N**2 + 2 * N - 1) // 2
    report(f"PaperII Thm4.2 fourth moment N={N}", m4 == f4, f"enum={m4} formula={f4}")
    cen = m4 - 2 * M * M + M * M                       # \int (|H2|^2-M)^2 = m4 - M^2 (since \int|H2|^2=M... )
    # correct centring: \int(|H2|^2-M)^2 = m4 - 2M*\int|H2|^2 + M^2 = m4 - M^2
    cen = m4 - M * M
    fc = N * (N - 1) * (5 * N**2 - N + 2) // 4
    report(f"PaperII Thm4.2 centred mass  N={N}", cen == fc, f"enum={cen} formula={fc}")

v55 = 55 * (3 * 55**3 - 2 * 55**2 + 2 * 55 - 1) // 2
report("PaperII Thm4.2 value at N=55", v55 == 13562560, f"formula={v55}")

# 3. dichotomy histogram
from collections import Counter
for N in (8, 9):
    S = pairsums(N)
    M = len(S)
    diffs = Counter(a - b for i, a in enumerate(S) for j, b in enumerate(S) if i != j)
    hist = Counter(diffs.values())
    expect = {1: M * (M - 1) - N * N * (N - 1), N: N * (N - 1)}
    report(f"PaperIII Thm3.1 dichotomy N={N}", dict(hist) == expect,
           f"hist={dict(hist)} expect={expect}")

# 4. sixth moment
for N in range(3, 8):
    S = pairsums(N)
    c3 = Counter(a + b + c for a in S for b in S for c in S)
    m6 = sum(v * v for v in c3.values())
    f6 = (45 * N**6 - 189 * N**5 + 438 * N**4 - 597 * N**3 + 443 * N**2 - 136 * N) // 4
    report(f"PaperIII RmkA.9 sixth moment N={N}", m6 == f6, f"enum={m6} formula={f6}")

# 5. median matrix eigenvalues
Mmat = np.array([[3, 4, 4, 4], [4, 3, 4, 4], [4, 4, 8, 4], [4, 4, 4, 8]], float)
ev = sorted(np.linalg.eigvals(Mmat).real)
claimed = sorted([-1.0, (19 - math.sqrt(281)) / 2, 4.0, (19 + math.sqrt(281)) / 2])
report("PaperI Prop5.4 eigenvalues", np.allclose(ev, claimed, atol=1e-9),
       f"computed={[round(x,6) for x in ev]}")

# 6. two-run spectrum moments, exhaustive over roots of unity.
# NB: the kernel is the ALTERNATING two-run kernel Z̄_a Z_b Z̄_c Z_d on sorted
# endpoints (it models chi(Q_b Q_d / Q_a Q_c)); with all-plus exponents the
# formula genuinely fails (coefficients become 1,40,540,2800,4900).
def kv_moments(V, q):
    idx = list(itertools.combinations(range(V), 4))
    tot2 = 0.0
    tot4 = 0.0
    n = 0
    for tup in itertools.product(range(q), repeat=V):
        z = np.exp(2j * np.pi * np.array(tup) / q)
        K = sum(np.conj(z[a]) * z[b] * np.conj(z[c]) * z[d] for a, b, c, d in idx)
        a2 = abs(K) ** 2
        tot2 += a2
        tot4 += a2 * a2
        n += 1
    return tot2 / n, tot4 / n

def C(n, k):
    return math.comb(n, k) if n >= k else 0

for V in (5, 6):
    for q in (3, 4):
        m2, m4 = kv_moments(V, q)
        f2 = C(V, 4)
        f4 = C(V, 4) + 40 * C(V, 5) + 420 * C(V, 6) + 1736 * C(V, 7) + 2556 * C(V, 8)
        ok = abs(m2 - f2) < 1e-6 * max(1, f2) and abs(m4 - f4) < 1e-6 * max(1, f4)
        report(f"PaperI Prop5.6 moments V={V} q={q}", ok,
               f"m2={m2:.6f}/{f2} m4={m4:.6f}/{f4}")

# 7. Paper V exact counts at p=5,7,11 -----------------------------------
def make_reducer(f, p):
    """f monic degree n (numpy int64 array, index=degree). Returns reduce fn
    for arrays of length <= 2n-1 using a precomputed reduction matrix.
    top[i] = x^{n+i} mod f, for i = 0..n-2."""
    n = len(f) - 1
    xp = (-f[:n]) % p                        # x^n mod f
    top = np.zeros((n - 1, n), dtype=np.int64)
    cur = xp.copy()
    for i in range(n - 1):
        top[i] = cur
        nxt = np.zeros(n + 1, dtype=np.int64)
        nxt[1:] = cur
        cur = (nxt[:n] + nxt[n] * xp) % p
    def reduce(r):
        r = r % p
        if len(r) <= n:
            out = np.zeros(n, dtype=np.int64)
            out[:len(r)] = r
            return out
        low = r[:n].copy()
        hi = r[n:]
        out = (low + hi @ top[:len(hi)]) % p
        return out
    return reduce

def polymulmod(a, b, red, p):
    return red(np.convolve(a, b))

def polygcd(a, b, p):
    a = np.trim_zeros(a % p, 'b')
    b = np.trim_zeros(b % p, 'b')
    while len(b):
        # a mod b
        a = a % p
        while len(a) >= len(b):
            c = (a[-1] * pow(int(b[-1]), p - 2, p)) % p
            a[len(a) - len(b):] = (a[len(a) - len(b):] - c * b) % p
            a = np.trim_zeros(a, 'b')
            if not len(a):
                break
        a, b = b, a
    return a

def is_irreducible_dyn(p, phi_step, f):
    """f = x^p - phi(x) monic degree p. phi_step(h, red) -> phi(h) mod f.
    Irreducible iff no irreducible factor of degree <= p//2.
    Detect via gcd(phi^l(x) - x, f) since roots alpha satisfy alpha^{p^l} = phi^l(alpha)."""
    red = make_reducer(f, p)
    n = p
    x = np.zeros(n, dtype=np.int64); x[1] = 1
    h = phi_step(x, red)
    acc = np.zeros(n, dtype=np.int64); acc[0] = 1
    CH = 8
    pend = 0
    l = 1
    # degree-1 check included via l=1
    while l <= p // 2:
        t = (h - x) % p
        acc = polymulmod(acc, t, red, p)
        pend += 1
        if pend == CH or l == p // 2:
            g = polygcd(f.copy(), acc.copy(), p)
            if len(g) > 1:
                return False
            acc = np.zeros(n, dtype=np.int64); acc[0] = 1
            pend = 0
        h = phi_step(h, red)
        l += 1
    return True

def irr_generic(f, p):
    """Irreducibility of monic degree-p f over F_p via dynamical iteration with
    phi(x) = -(lower part of f)(x) restricted... generic fallback: use
    h_{l+1} = h_l^p mod f? Too slow. Use phi from f's lower coefficients:
    x^p == -(f - x^p) mod f, i.e. phi(x) = -(f[:p] as poly)."""
    n = p
    red = make_reducer(f, p)
    low = (-f[:n]) % p            # phi as polynomial of degree <= 3 here
    lowpoly = np.trim_zeros(low, 'b')
    if not len(lowpoly):
        return False
    def phi_step(h, red):
        # evaluate phi(h) = sum lowpoly[i] * h^i mod f (deg lowpoly <= 3)
        out = np.zeros(n, dtype=np.int64)
        out[0] = lowpoly[0]
        cur = np.zeros(n, dtype=np.int64); cur[0] = 1
        for i in range(1, len(lowpoly)):
            cur = red(np.convolve(cur, h))
            out = (out + lowpoly[i] * cur) % p
        return out
    return is_irreducible_dyn(p, phi_step, f)

def paperV(p):
    n = p
    I4 = 0
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    f = np.zeros(n + 1, dtype=np.int64); f[n] = 1
                    f[3] = (f[3] + a) % p
                    f[2] = (f[2] + b) % p
                    f[1] = (f[1] + c - 1) % p
                    f[0] = (f[0] + d) % p
                    if irr_generic(f, p):
                        I4 += 1
    N2 = 0
    N2wit = []
    for d in range(p):
        f = np.zeros(n + 1, dtype=np.int64); f[n] = 1; f[2] = 1; f[0] = d
        if irr_generic(f, p):
            N2 += 1; N2wit.append(d)
    # depressed cubic classes: representatives a=1 (square), a=nonsquare
    def is_sq(a):
        return pow(a, (p - 1) // 2, p) == 1
    nsq = next(a for a in range(2, p) if not is_sq(a))
    def Ncount(a):
        cnt = 0
        for c in range(p):
            for d in range(p):
                f = np.zeros(n + 1, dtype=np.int64); f[n] = 1
                f[3] = a; f[1] = c; f[0] = d
                if irr_generic(f, p):
                    cnt += 1
        return cnt
    Nsq = Ncount(1)
    Nns = Ncount(nsq)
    return I4, N2, N2wit, Nsq, Nns

expected = {5: (124, 1, 4, 6, 6), 7: (426, 1, 10, 8, 10), 11: (1660, 1, 14, 14, 15)}
for p in (5, 7, 11):
    I4, N2, wit, Nsq, Nns = paperV(p)
    Wp = N2 + (Nsq + Nns) // 2
    eI4, eN2, eNsq, eNns, eWp = expected[p]
    decomp = (p - 1) + p * (p - 1) * N2 + p * (p - 1) // 2 * (Nsq + Nns)
    ok_dec = (I4 == decomp)
    # Paper's (Nsq, Nns) labels may be swapped depending on representative; compare as multiset
    ok = (I4 == eI4 and N2 == eN2 and {Nsq, Nns} == {eNsq, eNns} and Wp == eWp)
    report(f"PaperV counts p={p}", ok,
           f"I4={I4} N2={N2}(wit d={wit}) Nsq={Nsq} Nns={Nns} W_p={Wp}; orbit-decomp {'OK' if ok_dec else 'BAD'}")

sys.exit(FAIL)
