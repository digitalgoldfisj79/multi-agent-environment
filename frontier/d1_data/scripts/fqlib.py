#!/usr/bin/env python3
"""F_Q arithmetic library, Q = p^p, F_Q = F_p[T]/(T^p - T + 1).

Elements are coeff vectors (numpy int64, length p, index = power of T).
Provides: batched multiplication, Frobenius matrix, trace Gram matrix,
element <-> index encoding, batched exponentiation, quadratic character.
"""
import numpy as np
from itertools import product
import math


class FQ:
    def __init__(self, p):
        self.p = p
        self.Q = p ** p
        # T^p = T - 1 mod (T^p - T + 1)
        # Precompute T^k mod m for k = 0..3p (as coeff vectors), for reductions.
        deg_needed = 3 * p
        pows = np.zeros((deg_needed + 1, p), dtype=np.int64)
        cur = np.zeros(p, dtype=np.int64); cur[0] = 1
        for k in range(deg_needed + 1):
            pows[k] = cur
            cur = self._multT_raw(cur)
        self.Tpows = pows  # Tpows[k] = coeffs of T^k reduced
        # Frobenius matrix: column j = (T^j)^p = (T-1)^j mod p
        F = np.zeros((p, p), dtype=np.int64)
        for j in range(p):
            for i in range(j + 1):
                F[i, j] = (math.comb(j, i) * pow(-1, j - i, p)) % p
        self.F = F
        # F^(p-1) = inverse Frobenius (x -> x^{1/p})
        Fi = np.eye(p, dtype=np.int64)
        for _ in range(p - 1):
            Fi = (Fi @ F) % p
        self.Finvfrob = Fi
        # trace: S = sum F^i; Tr(x) = (S @ x)[0], other coords must vanish
        S = np.zeros((p, p), dtype=np.int64)
        M = np.eye(p, dtype=np.int64)
        for _ in range(p):
            S = (S + M) % p
            M = (M @ F) % p
        assert np.all(S[1:, :] == 0), "trace not scalar"
        self.trvec = S[0, :].copy()          # Tr(x) = trvec @ x mod p
        # trace Gram matrix B[i,j] = Tr(T^{i+j})
        B = np.zeros((p, p), dtype=np.int64)
        for i in range(p):
            for j in range(p):
                B[i, j] = int(self.trvec @ self.Tpows[i + j]) % p
        self.B = B

    def _multT_raw(self, vec):
        p = self.p
        v = np.roll(vec, 1).copy()
        hi = vec[p - 1]
        v[0] = (-hi) % p         # T^p = T - 1
        v[1] = (v[1] + hi) % p
        return v % p

    # ---------- element enumeration ----------
    def all_elements(self):
        """(Q, p) array; row index = base-p integer with digit i = coeff of T^i."""
        p, Q = self.p, self.Q
        idx = np.arange(Q, dtype=np.int64)
        out = np.empty((Q, p), dtype=np.int64)
        for i in range(p):
            out[:, i] = (idx // p ** i) % p
        return out

    def encode(self, A):
        """(N,p) coeff array -> (N,) index array."""
        p = self.p
        w = p ** np.arange(p, dtype=np.int64)
        return A @ w

    # ---------- batched arithmetic ----------
    def bmul(self, A, Bv):
        """batched product: A, Bv (N,p) -> (N,p) reduced."""
        p = self.p
        N = A.shape[0]
        conv = np.zeros((N, 2 * p - 1), dtype=np.int64)
        for i in range(p):
            conv[:, i:i + p] = (conv[:, i:i + p] + A[:, i:i + 1] * Bv) % p
        # reduce degrees p..2p-2 using Tpows
        out = conv[:, :p].copy()
        for k in range(p, 2 * p - 1):
            out = (out + conv[:, k:k + 1] * self.Tpows[k]) % p
        return out

    def bpow(self, A, e):
        """batched A^e (e >= 0)."""
        N = A.shape[0]
        res = np.zeros((N, self.p), dtype=np.int64); res[:, 0] = 1
        base = A % self.p
        while e:
            if e & 1:
                res = self.bmul(res, base)
            base = self.bmul(base, base)
            e >>= 1
        return res

    def frob(self, A):
        return (A @ self.F.T) % self.p

    def invfrob(self, A):
        return (A @ self.Finvfrob.T) % self.p

    def tr(self, A):
        """batched trace -> (N,) in F_p."""
        return (A @ self.trvec) % self.p

    def tr_pair(self, t, Th):
        """Tr(t * theta) for one t (p,) and many theta (N,p): via Gram matrix."""
        w = (t @ self.B) % self.p    # linear functional coeffs
        return (Th @ w) % self.p

    def eta_table(self):
        """quadratic character on F_Q by element index: +1 square, -1 nonsq, 0 at 0."""
        Th = self.all_elements()
        sq = self.bmul(Th, Th)
        sqi = self.encode(sq)
        tab = -np.ones(self.Q, dtype=np.int64)
        tab[np.unique(sqi)] = 1
        tab[0] = 0
        return tab


# ---------- batched Rabin irreducibility for the family T^p+aT^3+bT^2+cT+d ----------
def irred_mask_family(p, quads):
    """quads: (N,4) array of (a,b,c,d). p >= 5 prime.
    Returns boolean mask: T^p + aT^3 + bT^2 + cT + d irreducible (degree p).
    Test: no F_p-root AND x^{p^p} == x mod f.
    Uses x^p mod f = -(a x^3 + b x^2 + c x + d)."""
    assert p >= 5
    N = quads.shape[0]
    a, b, c, d = (quads[:, i] for i in range(4))
    # no-root test: f(x) = x^p + a x^3 + b x^2 + c x + d ; x^p = x on F_p
    ok = np.ones(N, dtype=bool)
    for x in range(p):
        v = (x + a * pow(x, 3, p) + b * (x * x % p) + c * x + d) % p
        ok &= (v != 0)
    # h_1 = x^p mod f = -(a x^3 + b x^2 + c x + d): degree < p rep, length p
    h = np.zeros((N, p), dtype=np.int64)
    h[:, 3] = (-a) % p
    h[:, 2] = (-b) % p
    h[:, 1] = (-c) % p
    h[:, 0] = (-d) % p

    def mulmod(u, v):
        # u,v (N,p) polys deg<p; multiply then reduce mod f (monic deg p)
        conv = np.zeros((N, 2 * p - 1), dtype=np.int64)
        for i in range(p):
            conv[:, i:i + p] = (conv[:, i:i + p] + u[:, i:i + 1] * v) % p
        # reduce: x^p = -(a x^3 + b x^2 + c x + d), i.e. x^{p+j} = x^j * h1
        # do it degree by degree from top
        for k in range(2 * p - 2, p - 1, -1):
            coef = conv[:, k].copy()
            conv[:, k] = 0
            j = k - p
            # add coef * x^j * (-(a x^3+b x^2+c x+d))
            conv[:, j + 3] = (conv[:, j + 3] - coef * a) % p
            conv[:, j + 2] = (conv[:, j + 2] - coef * b) % p
            conv[:, j + 1] = (conv[:, j + 1] - coef * c) % p
            conv[:, j] = (conv[:, j] - coef * d) % p
        return conv[:, :p] % p

    def pow_p(u):
        # u^p mod f by square-and-multiply
        res = np.zeros((N, p), dtype=np.int64); res[:, 0] = 1
        base = u
        e = p
        while e:
            if e & 1:
                res = mulmod(res, base)
            base = mulmod(base, base)
            e >>= 1
        return res

    # iterate Frobenius p-1 more times: h_{k+1} = h_k^p mod f; h_p = x^{p^p}
    cur = h
    for _ in range(p - 1):
        cur = pow_p(cur)
    isx = np.zeros((N, p), dtype=np.int64); isx[:, 1] = 1
    ok &= np.all(cur == isx, axis=1)
    return ok


def brute_counts_p3():
    """p=3 special: family (1+a)T^3 + bT^2 + cT + d; count degree-3 irreducibles."""
    import sympy
    T = sympy.symbols('T')
    tot = 0
    slices = {}
    fortune = 0  # (a,b) != (0,0)
    for a in range(3):
        cnt = 0
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    lead = (1 + a) % 3
                    if lead == 0:
                        continue
                    poly = sympy.Poly([lead, b, c, d], T, modulus=3)
                    # monic normalize
                    if lead != 1:
                        poly = poly * sympy.invert(lead, 3)
                    if poly.is_irreducible:
                        cnt += 1
                        tot += 1
                        if (a, b) != (0, 0):
                            fortune += 1
        slices[a] = cnt
    return tot, slices, fortune
