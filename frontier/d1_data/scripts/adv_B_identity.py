#!/usr/bin/env python3
"""ADVERSARY part B: independent verification of the exact incidence identities
at p=5 (full) using field F_Q = F_p[x]/(h), h = T^p - T + 1 (Artin-Schreier, irreducible).

Checks:
 (B1) C_quad := #{(theta,b,c) in F_Q x F_p^2 : theta^p + b theta^2 + c theta in F_p}
      equals p^3 + p * #irred_2.
 (B2) C_cub := #{(theta,a,b,c) : theta^p + a theta^3 + b theta^2 + c theta in F_p}
      equals p^4 + p * #irred_4.
 (B3) NEW theta-reformulation:
      p * #irred_4 == #{theta in F_Q \\ F_p : theta^p in span_Fp(1,theta,theta^2,theta^3)}
      p * #irred_2 == #{theta in F_Q \\ F_p : theta^p in span_Fp(1,theta,theta^2)}
 (B4) linearization Tr(t theta^p) == Tr(t^{1/p} theta) for random t,theta.
"""
import numpy as np
from itertools import product
from flint import nmod_poly

p = 5
Q = p**p

# ---- field setup: h = T^p - T + 1 ----
hco = [1, p-1] + [0]*(p-2) + [1]
assert len(hco) == p+1
h = nmod_poly(hco, p)
fac = h.factor()
assert len(fac[1]) == 1 and fac[1][0][1] == 1, "h not irreducible!"

# reduction table: x^k mod h for k = 0..3p-3  (needed for theta^3)
red = np.zeros((3*p-2, p), dtype=np.int64)
for k in range(3*p-2):
    r = nmod_poly([0]*k + [1], p) % h
    cl = r.coeffs()
    for i, cc in enumerate(cl):
        red[k, i] = int(cc)

def batch_mul(A, B):
    """A, B: (M,p) coeff arrays; return A*B mod (h,p)."""
    M = A.shape[0]
    conv = np.zeros((M, 2*p-1), dtype=np.int64)
    for i in range(p):
        for j in range(p):
            conv[:, i+j] += A[:, i] * B[:, j]
    conv %= p
    return (conv @ red[:2*p-1]) % p

# all field elements
Theta = np.array(list(product(range(p), repeat=p)), dtype=np.int64)[:, ::-1].copy()
# order irrelevant; column i = coeff of x^i
Th2 = batch_mul(Theta, Theta)
Th3 = batch_mul(Th2, Theta)
# Frobenius matrix: x^p = x - 1 mod h -> (x^j)^p = (x-1)^j
import math
F = np.zeros((p, p), dtype=np.int64)
for j in range(p):
    for i in range(j+1):
        F[i, j] = (math.comb(j, i) * pow(-1, j-i, p)) % p
Thp = (Theta @ F.T) % p

# in F_p <=> coords 1..p-1 all zero
def infp(A): return np.all(A[:, 1:] == 0, axis=1)

isfp = infp(Theta)
assert isfp.sum() == p

# ---- B1 ----
C = 0
for b in range(p):
    for c in range(p):
        val = (Thp + b*Th2 + c*Theta) % p
        C += int(infp(val).sum())
# independent irred counts via flint
def irred(p, a, b, c, d):
    coeffs = [0]*(p+1); coeffs[p] = 1
    coeffs[3] = (coeffs[3]+a) % p; coeffs[2] = (coeffs[2]+b) % p
    coeffs[1] = (coeffs[1]+c) % p; coeffs[0] = (coeffs[0]+d) % p
    f = nmod_poly(coeffs, p); fc = f.factor()[1]
    return len(fc) == 1 and fc[0][1] == 1 and fc[0][0].degree() == p
n2 = sum(irred(p,0,b,c,d) for b in range(p) for c in range(p) for d in range(p))
print(f"B1: C_quad = {C}, p^3 + p*#irred_2 = {p**3 + p*n2}, MATCH = {C == p**3 + p*n2}")

# ---- B2 ----
C4 = 0
for a in range(p):
    Ta = (Thp + a*Th3) % p
    for b in range(p):
        Tab = (Ta + b*Th2) % p
        for c in range(p):
            val = (Tab + c*Theta) % p
            C4 += int(infp(val).sum())
n4 = sum(irred(p,a,b,c,d) for a in range(p) for b in range(p) for c in range(p) for d in range(p))
print(f"B2: C_cub = {C4}, p^4 + p*#irred_4 = {p**4 + p*n4}, MATCH = {C4 == p**4 + p*n4}")

# ---- B3: span membership ----
def rank_mod_p(M):
    M = M % p
    M = M.astype(np.int64).copy()
    r = 0
    rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c] % p: piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), p-2, p)
        M[r] = (M[r] * inv) % p
        for i in range(rows):
            if i != r and M[i, c]:
                M[i] = (M[i] - M[i, c]*M[r]) % p
        r += 1
    return r

one = np.zeros(p, dtype=np.int64); one[0] = 1
cnt3 = 0; cnt2 = 0
for idx in range(Q):
    if isfp[idx]: continue
    M4 = np.stack([one, Theta[idx], Th2[idx], Th3[idx]])
    M5 = np.vstack([M4, Thp[idx]])
    if rank_mod_p(M5) == 4: cnt3 += 1     # theta^p in span(1,th,th^2,th^3) (rank M4 = 4 for th notin F_p)
    M3 = np.stack([one, Theta[idx], Th2[idx]])
    M4b = np.vstack([M3, Thp[idx]])
    if rank_mod_p(M4b) == 3: cnt2 += 1
print(f"B3: #(theta^p in span(1..th^3), th notin F_p) = {cnt3}, p*#irred_4 = {p*n4}, MATCH = {cnt3 == p*n4}")
print(f"B3: #(theta^p in span(1..th^2), th notin F_p) = {cnt2}, p*#irred_2 = {p*n2}, MATCH = {cnt2 == p*n2}")

# ---- B4: linearization ----
# trace vector: Tr(x^j)
S = np.zeros((p,p), dtype=np.int64); Fi = np.eye(p, dtype=np.int64)
for i in range(p):
    S = (S + Fi) % p; Fi = (Fi @ F) % p
assert np.all(S[1:, :] == 0)
trv = S[0]
Finv = np.linalg.matrix_power(F, p-1)  # F^{p-1} = Frobenius^{p-1} = inverse Frobenius
Finv = Finv % p
rng = np.random.default_rng(0)
ok = True
for _ in range(200):
    t = rng.integers(0, p, p); th = rng.integers(0, p, p)
    lhs = int(trv @ batch_mul(t[None,:], (th[None,:] @ F.T) % p)[0]) % p
    rhs = int(trv @ batch_mul((t[None,:] @ Finv.T) % p, th[None,:])[0]) % p
    if lhs != rhs: ok = False; break
print(f"B4: Tr(t theta^p) == Tr(t^(1/p) theta) on 200 random samples: {ok}")
