"""Diagnostic: Fortunate elements of P_d = prod of monic irreducibles of degree <= d in F_p[T].

Finds the least nonconstant m (ordered by degree, then lex on coefficient tuples
(a_e,...,a_0), a_e != 0) with P_d + m irreducible; checks deg m <= 2d+1 and m irreducible.
Pure numpy, prime fields only. Polys = numpy int64 arrays, lowest degree first.
"""
import numpy as np
import sys
from itertools import product

def trim(a):
    a = np.trim_zeros(np.asarray(a, dtype=np.int64), 'b')
    return a if a.size else np.zeros(1, dtype=np.int64)

def polmod(a, f, p):
    a = trim(a % p); f = trim(f % p)
    df = f.size - 1
    finv = pow(int(f[-1]), p - 2, p) if f[-1] != 1 else 1
    a = a.copy()
    while a.size - 1 >= df and a.any():
        da = a.size - 1
        c = (int(a[-1]) * finv) % p
        a[da - df: da + 1] = (a[da - df: da + 1] - c * f) % p
        a = trim(a)
    return a

def polmulmod(a, b, f, p):
    c = np.convolve(a, b) % p
    return polmod(c, f, p)

def polpowmod(a, e, f, p):
    r = np.array([1], dtype=np.int64)
    a = polmod(a, f, p)
    while e:
        if e & 1:
            r = polmulmod(r, a, f, p)
        a = polmulmod(a, a, f, p)
        e >>= 1
    return r

def polgcd(a, b, p):
    a, b = trim(a), trim(b)
    while b.any():
        a, b = b, polmod(a, b, p)
    return a

def is_irreducible(f, p):
    """Early-abort DDF: f monic degree n irreducible iff no factor of degree <= n/2."""
    f = trim(f)
    n = f.size - 1
    if n <= 0:
        return False
    if n == 1:
        return True
    x = np.array([0, 1], dtype=np.int64)
    t = x.copy()
    for k in range(1, n // 2 + 1):
        t = polpowmod(t, p, f, p)          # t = x^(p^k) mod f
        d = (t - np.pad(x, (0, max(0, t.size - 2)))[:t.size]) % p if t.size >= 2 \
            else (np.pad(t, (0, 2 - t.size)) - x) % p
        g = polgcd(d, f, p)
        if g.size - 1 > 0:
            return False
    return True

def sub(a, b, p):
    n = max(a.size, b.size)
    return (np.pad(a, (0, n - a.size)) - np.pad(b, (0, n - b.size))) % p

def poldivexact(a, b, p):
    a = trim(a.copy()); b = trim(b)
    db = b.size - 1
    binv = pow(int(b[-1]), p - 2, p)
    q = np.zeros(a.size - db, dtype=np.int64)
    while a.size - 1 >= db and a.any():
        da = a.size - 1
        c = (int(a[-1]) * binv) % p
        q[da - db] = c
        a[da - db: da + 1] = (a[da - db: da + 1] - c * b) % p
        a = trim(a)
    assert not a.any(), "division not exact"
    return trim(q)

def primorial(p, d):
    """P_d over F_p via  T^{p^e} - T = prod_{c|e} R_c,  R_e = prod_{deg pi = e} pi."""
    R = {}
    for e in range(1, d + 1):
        a = np.zeros(p ** e + 1, dtype=np.int64)
        a[p ** e] = 1
        a[1] = (a[1] - 1) % p
        for c in range(1, e):
            if e % c == 0:
                a = poldivexact(a, R[c], p)
        R[e] = a
    P = np.array([1], dtype=np.int64)
    for e in range(1, d + 1):
        P = trim(np.convolve(P, R[e]) % p)
    return P

def find_fortunate(p, d, maxdeg=None, verbose=True):
    P = primorial(p, d)
    n = P.size - 1
    nd_formula = sum(len([1]) * 0 for _ in [0])  # placeholder
    bound = min(2 * d + 1, n - 1)
    if maxdeg is None:
        maxdeg = bound + 2   # scan a bit past the conjectured bound
    tried = 0
    for e in range(1, maxdeg + 1):
        # lex order on (a_e, a_{e-1}, ..., a_0), a_e in 1..p-1
        for coeffs in product(range(1, p), *([range(p)] * e)):
            m = np.array(list(coeffs[::-1]), dtype=np.int64)  # lowest-first
            tried += 1
            fm = sub(P, (-m) % p, p)  # P + m
            if is_irreducible(fm, p):
                mi = is_irreducible(m, p) if e >= 1 else False
                return dict(p=p, d=d, n=n, deg_m=e, m=list(map(int, coeffs)),
                            m_irred=bool(mi), within_bound=(e <= bound),
                            bound=bound, tried=tried)
    return dict(p=p, d=d, n=n, deg_m=None, tried=tried, bound=bound)

if __name__ == "__main__":
    cases = eval(sys.argv[1])
    for (p, d) in cases:
        r = find_fortunate(p, d)
        print(r, flush=True)
