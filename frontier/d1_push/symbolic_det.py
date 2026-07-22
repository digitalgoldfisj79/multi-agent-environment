#!/usr/bin/env python3
"""Symbolic C_3 determinant polynomial in (c,d) over F_p, for fixed a.

Builds the (p-1)x(p-1) minor of I-H (delete row p, column 3) with entries
as exact bivariate polynomials in (c,d) mod p (via the verified
trinomial-coefficient formula), computes det by subset-DP, then:
  - reports degree structure,
  - lists surviving monomials c^K d^L with K,L>=1 and (p-1)|K,(p-1)|L,
  - checks   sum of surviving coeffs == 3 a N_a(p)  mod p
    against direct flint count.
Polynomials: numpy 2D int64 arrays indexed [deg_c, deg_d], reduced mod p.
"""
import numpy as np
from math import factorial
from itertools import combinations
from flint import nmod_poly
import sys

def entry_poly(p, u, v, a):
    """(c,d)-polynomial for H_{u,v} with numeric a, as dict {(j,k):coef}."""
    out = {}
    for w in range(1, min(4, u) + 1):
        n = p - 1 - u + w
        sgn = (-1) ** n
        target = p * w - v
        for i in range(0, min(n, target // 3) + 1):
            j = target - 3 * i
            if j < 0:
                break
            k = n - i - j
            if k < 0:
                continue
            coef = factorial(n) // (factorial(i) * factorial(j) * factorial(k))
            val = (sgn * coef * pow(a, i, p)) % p
            if val:
                out[(j, k)] = (out.get((j, k), 0) + val) % p
    return out

def dict_to_arr(dd, p):
    if not dd:
        return np.zeros((1, 1), dtype=np.int64)
    mc = max(j for j, k in dd) + 1
    md = max(k for j, k in dd) + 1
    A = np.zeros((mc, md), dtype=np.int64)
    for (j, k), v in dd.items():
        A[j, k] = v % p
    return A

def pmul(A, B, p):
    """2D polynomial multiply mod p; B assumed small."""
    out = np.zeros((A.shape[0] + B.shape[0] - 1, A.shape[1] + B.shape[1] - 1),
                   dtype=np.int64)
    js, ks = np.nonzero(B)
    for j, k in zip(js, ks):
        out[j:j + A.shape[0], k:k + A.shape[1]] += B[j, k] * A
        out %= p
    return out % p

def padd(A, B, p):
    m = max(A.shape[0], B.shape[0]); n = max(A.shape[1], B.shape[1])
    out = np.zeros((m, n), dtype=np.int64)
    out[:A.shape[0], :A.shape[1]] += A
    out[:B.shape[0], :B.shape[1]] += B
    return out % p

def det_poly(M, p):
    """Determinant of matrix of 2D-array polynomials via subset DP.

    D[S] = det of submatrix (rows 0..|S|-1, columns S).  Laplace along the
    last row: sign = (-1)^{r + #{col' in S : col' < col}} with r = |S|.
    """
    n = len(M)
    cols = tuple(range(n))
    D = {(): np.array([[1]], dtype=np.int64)}
    for r in range(n):
        ND = {}
        for S, poly in D.items():
            for col in cols:
                if col in S:
                    continue
                e = M[r][col]
                pos = sum(1 for c in S if c < col)
                sgn = (-1) ** (r + pos)
                term = pmul(poly, e, p)
                if sgn < 0:
                    term = (-term) % p
                NS = tuple(sorted(S + (col,)))
                if NS in ND:
                    ND[NS] = padd(ND[NS], term, p)
                else:
                    ND[NS] = term
        D = ND
    return D[cols]

def irr(f, p):
    lead, facs = f.factor()
    return len(facs) == 1 and facs[0][1] == 1 and facs[0][0].degree() == p

def Na(p, a):
    cnt = 0
    for c in range(p):
        for d in range(p):
            F = nmod_poly([d, c, 0, a] + [0]*(p-4) + [1], p)
            if irr(F, p):
                cnt += 1
    return cnt

def run(p, a):
    colset = [v for v in range(1, p + 1) if v != 3]
    M = []
    for u in range(1, p):
        row = []
        for v in colset:
            dd = entry_poly(p, u, v, a)
            # I - H : subtract from identity
            arr = dict_to_arr(dd, p)
            arr = (-arr) % p
            if u == v:
                arr[0, 0] = (arr[0, 0] + 1) % p
            row.append(arr)
        M.append(row)
    Dp = det_poly(M, p)
    # trim zeros
    nz = np.nonzero(Dp)
    if len(nz[0]) == 0:
        print(f"p={p} a={a}: determinant is ZERO polynomial")
        return
    degc = nz[0].max(); degd = nz[1].max()
    # surviving monomials
    surv = []
    ssum = 0
    for K in range(p - 1, degc + 1, p - 1):
        for L in range(p - 1, degd + 1, p - 1):
            if K < Dp.shape[0] and L < Dp.shape[1] and Dp[K, L]:
                surv.append((K, L, int(Dp[K, L])))
                ssum = (ssum + int(Dp[K, L])) % p
    # d-parity structure: which d-degrees appear
    dpar = sorted(set(int(k) for k in np.nonzero(Dp)[1]))
    na = Na(p, a)
    target = (3 * a * na) % p
    ok = (ssum == target)
    print(f"p={p} a={a}: deg_c={degc} deg_d={degd} nmono={len(nz[0])} "
          f"N_a={na} 3aN_a mod p={target} survivor_sum={ssum} {'OK' if ok else 'MISMATCH'}")
    print(f"   survivors (K,L,coef): {surv}")
    even_d = all(k % 2 == 0 for k in dpar)
    print(f"   d-degrees all even: {even_d}")
    return Dp, surv, ok

def numeric_crosscheck(p, a, Dp, trials=25):
    """Evaluate det polynomial at random (c,d) and compare against
    direct numeric determinant of the I-H minor built from flint coeffs."""
    import random
    from flint import nmod_mat
    rng = random.Random(7)
    bad = 0
    for _ in range(trials):
        c = rng.randrange(p); d = rng.randrange(p)
        # polynomial evaluation
        val = 0
        js, ks = np.nonzero(Dp)
        for j, k in zip(js, ks):
            val = (val + int(Dp[j, k]) * pow(c, int(j), p) * pow(d, int(k), p)) % p
        # numeric determinant
        F = nmod_poly([d, c, 0, a] + [0]*(p-4) + [1], p)
        G = F ** (p - 1)
        deg = G.degree()
        colset = [v for v in range(1, p + 1) if v != 3]
        rows = []
        for u in range(1, p):
            row = []
            for v in colset:
                e = p * u - v
                h = int(G[e]) if 0 <= e <= deg else 0
                row.append(((1 if u == v else 0) - h) % p)
            rows.append(row)
        ref = int(nmod_mat(rows, p).det()) % p
        if val != ref:
            bad += 1
    print(f"   numeric crosscheck p={p} a={a}: bad={bad}/{trials}")
    return bad

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    alist = ([int(sys.argv[2])] if len(sys.argv) > 2 else list(range(1, p)))
    for a in alist:
        out = run(p, a)
        if out:
            numeric_crosscheck(p, a, out[0])
