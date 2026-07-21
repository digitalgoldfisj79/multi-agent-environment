#!/usr/bin/env python3
"""Validate the FF-Fortune d=1 reduction.

1. Brute-force #irreducible in the quadratic family T^p + b T^2 + c T + d
   over F_p, for p = 3..23; count Fortune-relevant ones (b != 0).
2. For p = 3, 5: verify the EXACT identity
      #irred = p^{2-p} * sum_{t in ker Tr, t != 0} E(t),
   E(t) = sum_{theta in F_Q: Tr(t theta) = Tr(t theta^2) = 0}
              e_p( Tr(t^{1/p} theta) ),
   with Q = p^p, F_Q = F_p[T]/(T^p - T + 1)  (Artin-Schreier, irreducible).
"""
import numpy as np
from itertools import product
import cmath, math

# ---------- polynomial arithmetic mod p ----------
def polymulmod(f, g, p, m):
    """f, g, m lists of coeffs (low->high), m monic; return f*g mod (m, p)."""
    r = [0]*(len(f)+len(g)-1)
    for i, a in enumerate(f):
        if a:
            for j, b in enumerate(g):
                r[i+j] = (r[i+j] + a*b) % p
    # reduce by m (monic, degree D)
    D = len(m)-1
    for k in range(len(r)-1, D-1, -1):
        c = r[k]
        if c:
            r[k] = 0
            for j in range(D):
                r[k-D+j] = (r[k-D+j] - c*m[j]) % p
    r = r[:D]
    return [x % p for x in r] + [0]*(D-len(r))

def polypow_xq(p, m, e):
    """T^(p^e) mod (m, p) via repeated Frobenius using square-and-multiply."""
    D = len(m)-1
    x = [0,1] + [0]*(D-2)   # T
    cur = x[:]
    for _ in range(e):
        # cur -> cur^p by exponentiation
        res = [1] + [0]*(D-1)
        base = cur[:]
        k = p
        while k:
            if k & 1:
                res = polymulmod(res, base, p, m)
            base = polymulmod(base, base, p, m)
            k >>= 1
        cur = res
    return cur

def is_irreducible_deg_p(coeffs, p):
    """coeffs: full coeff list (low->high) of a monic poly of prime degree p.
    Irreducible iff no root in F_p and T^(p^p) == T mod f."""
    # root check
    for x in range(p):
        v = 0
        for a in reversed(coeffs):
            v = (v*x + a) % p
        if v == 0:
            return False
    m = coeffs
    xq = polypow_xq(p, m, p)   # T^(p^p) mod f
    want = [0,1] + [0]*(p-2)
    return xq == want

# ---------- part 1: brute-force counts ----------
print("p  #irred(quad fam)  #b!=0  p^2  ratio")
for p in [3,5,7,11,13]:
    tot = 0; fortune = 0
    for b in range(p):
        for c in range(p):
            for d in range(p):
                f = [d,c,b] + [0]*(p-3) + [1]
                if is_irreducible_deg_p(f, p):
                    tot += 1
                    if b != 0:
                        fortune += 1
    print(f"{p:2d} {tot:8d} {fortune:8d} {p*p:6d}  {tot/(p*p):.3f}")

# ---------- part 2: exact identity check ----------
def identity_check(p):
    D = p
    m = [1, p-1] + [0]*(p-2) + [1]   # T^p - T + 1: coeffs [1,-1,0,...,0,1]
    # Frobenius on basis: (T^j)^p = (T-1)^j mod m  (since T^p = T-1 mod m)
    # build F matrix: column j = coeffs of (T-1)^j
    F = np.zeros((p,p), dtype=np.int64)
    for j in range(p):
        # (T-1)^j coefficients
        col = [0]*p
        for i in range(j+1):
            col[i] = (math.comb(j,i) * pow(-1, j-i, p)) % p
        F[:, j] = col
    # trace on basis: tr[j] = Tr(T^j) = sum_i (F^i)[.,j] evaluated...
    # Tr(x) = sum_{i=0}^{p-1} Frob^i(x); as functional: trvec = sum_i row-sums?
    # Frob^i as matrix Fi; Tr(T^j) = sum_i (Fi @ e_j) -> element; but trace is
    # an element of F_p (it lies in F_p): its coeff vector should be
    # (Tr(T^j), 0, ..., 0). Compute S = sum_i F^i; then Tr(T^j) = S[0,j]
    # (constant coefficient; verify other coords are 0).
    S = np.zeros((p,p), dtype=np.int64)
    Fi = np.eye(p, dtype=np.int64)
    for i in range(p):
        S = (S + Fi) % p
        Fi = (Fi @ F) % p
    assert np.all(S[1:,:] % p == 0), "trace not scalar!"
    trvec = S[0,:] % p     # Tr(T^j)
    # multiplication by T (shift) with reduction T^p = T - 1
    def multT(vec):
        v = np.roll(vec, 1)
        hi = vec[p-1]
        v[0] = 0
        v[0] = (v[0] + hi*(-1)) % p   # T^p -> -1 ... T^p = T - 1: contributes
        v[1] = (v[1] + hi*1) % p      # to constant -1*hi and T-coeff +hi
        return v % p
    # enumerate all field elements as vectors
    Nfield = p**p
    # all theta as array
    Theta = np.array(list(product(range(p), repeat=p)), dtype=np.int64)  # low->high? use index=power
    # For theta with coeff vector th (th[i] coeff of T^i):
    # need w_k(t) = Tr(t * T^k) for k = 0..2p-2, and s = t^{1/p} = F^{p-1} t
    Fp1 = np.eye(p, dtype=np.int64)
    for _ in range(p-1):
        Fp1 = (Fp1 @ F) % p
    total = 0.0+0.0j
    count_t = 0
    for tt in product(range(p), repeat=p):
        t = np.array(tt, dtype=np.int64)
        if not t.any():
            continue
        if int(trvec @ t) % p != 0:
            continue
        count_t += 1
        # w_k = Tr(t*T^k), k=0..2p-2
        w = np.zeros(2*p-1, dtype=np.int64)
        cur = t.copy()
        for k in range(2*p-1):
            w[k] = int(trvec @ cur) % p
            cur = multT(cur)
        s = (Fp1 @ t) % p
        ws = np.zeros(p, dtype=np.int64)
        cur = s.copy()
        for k in range(p):
            ws[k] = int(trvec @ cur) % p
            cur = multT(cur)
        # linear form L(theta) = sum th_i w_i ; quad form Q = sum th_i th_j w_{i+j}
        Lv = (Theta @ w[:p]) % p
        A = np.zeros((p,p), dtype=np.int64)
        for i in range(p):
            for j in range(p):
                A[i,j] = w[i+j]
        Qv = np.einsum('ni,ij,nj->n', Theta, A, Theta) % p
        lv = (Theta @ ws) % p
        mask = (Lv == 0) & (Qv == 0)
        phases = np.exp(2j*np.pi*lv[mask]/p)
        total += phases.sum()
    pred = (p**(2-p)) * total
    return pred, count_t

for p in [3, 5]:
    pred, nt = identity_check(p)
    # brute-force count again for reference
    tot = 0
    for b in range(p):
        for c in range(p):
            for d in range(p):
                f = [d,c,b] + [0]*(p-3) + [1]
                if is_irreducible_deg_p(f, p):
                    tot += 1
    print(f"p={p}: brute #irred = {tot}; identity RHS = {pred.real:.6f} "
          f"(imag {pred.imag:.2e}); #t in kerTr\\0 = {nt}")
    assert abs(pred.real - tot) < 1e-6 and abs(pred.imag) < 1e-6
print("IDENTITY VERIFIED")
