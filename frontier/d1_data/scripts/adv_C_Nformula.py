#!/usr/bin/env python3
"""ADVERSARY part C: verify the closed N(p) Gauss-sum formula for p=3,5,7:
   N(p) = p^{-p} G_Q * S(p),  S(p) = sum_{tau in kerTr\\0} eta(tau) e_p(-(1/4) Tr(tau^{2-p}))
plus Hasse-Davenport sign G_Q = -(-G_p)^p, and the intermediate identity
   N(p) + 1 = p^{-p} sum_{t in kerTr} sum_theta e_p(Tr(t theta^2 + t^{1/p} theta)).
"""
import numpy as np, math, cmath
from itertools import product
from flint import nmod_poly

def run(p, check_intermediate):
    Q = p**p
    hco = [1, p-1] + [0]*(p-2) + [1]
    h = nmod_poly(hco, p)
    assert h.factor()[1][0][0].degree() == p
    red = np.zeros((2*p-1, p), dtype=np.int64)
    for k in range(2*p-1):
        r = nmod_poly([0]*k + [1], p) % h
        for i, cc in enumerate(r.coeffs()): red[k, i] = int(cc)

    def bmul(A, B):
        conv = np.zeros((A.shape[0], 2*p-1), dtype=np.int64)
        for i in range(p):
            Ai = A[:, i]
            for j in range(p):
                conv[:, i+j] += Ai * B[:, j]
        conv %= p
        return (conv @ red) % p

    # Frobenius matrix and trace vector
    F = np.zeros((p, p), dtype=np.int64)
    for j in range(p):
        for i in range(j+1):
            F[i, j] = (math.comb(j, i) * pow(-1, j-i, p)) % p
    S = np.zeros((p, p), dtype=np.int64); Fi = np.eye(p, dtype=np.int64)
    for i in range(p):
        S = (S + Fi) % p; Fi = (Fi @ F) % p
    assert np.all(S[1:] == 0)
    trv = S[0]
    # kernel basis of trv
    piv = next(i for i in range(p) if trv[i] % p)
    basis = []
    for i in range(p):
        if i == piv: continue
        v = np.zeros(p, dtype=np.int64); v[i] = 1
        v[piv] = (-trv[i] * pow(int(trv[piv]), p-2, p)) % p
        basis.append(v)
    basis = np.array(basis)          # (p-1, p)
    coefs = np.array(list(product(range(p), repeat=p-1)), dtype=np.int64)
    Tau = (coefs @ basis) % p        # all kerTr elements
    nz = np.any(Tau != 0, axis=1)
    Tau = Tau[nz]                    # kerTr \ 0
    M = Tau.shape[0]
    assert M == p**(p-1) - 1
    # sanity: traces zero
    assert np.all((Tau @ trv) % p == 0)

    def bpow(A, e):
        R = np.zeros_like(A); R[:, 0] = 1
        B = A.copy()
        while e:
            if e & 1: R = bmul(R, B)
            B = bmul(B, B)
            e >>= 1
        return R

    # eta(tau) = tau^{(Q-1)/2}: constant +-1
    eta_el = bpow(Tau, (Q-1)//2)
    assert np.all(eta_el[:, 1:] == 0)
    eta = np.where(eta_el[:, 0] == 1, 1, -1)
    assert np.all((eta_el[:, 0] == 1) | (eta_el[:, 0] == p-1))
    # tau^{2-p} = tau^{Q-1-(p-2)}
    T2p = bpow(Tau, Q - 1 - (p - 2))
    tr_t2p = (T2p @ trv) % p
    inv4 = pow(4, p-2, p)
    w = np.exp(2j*np.pi/p)
    Sp = np.sum(eta * w**((-inv4 * tr_t2p) % p))
    # G_Q directly
    All = np.array(list(product(range(p), repeat=p)), dtype=np.int64)
    Sq = bmul(All, All)
    trsq = (Sq @ trv) % p
    G_Q = np.sum(w**trsq)
    G_p = sum(cmath.exp(2j*np.pi*(x*x % p)/p) for x in range(p))
    HD = -(-G_p)**p
    print(f"p={p}: S(p) = {Sp:.6f}")
    print(f"   G_Q direct = {G_Q:.6f},  -(-G_p)^p = {HD:.6f},  HD-match: {abs(G_Q-HD)<1e-6*abs(G_Q)}")
    Nf = G_Q * Sp / p**p
    print(f"   N via formula = {Nf:.8f}  (should be integer; N(3)=N(5)=N(7)=1)")
    if check_intermediate:
        # N+1 = p^-p sum_{t in kerTr} sum_theta e_p(Tr(t th^2 + t^{1/p} th))
        Finv = np.linalg.matrix_power(F, p-1) % p
        tot = 0j
        # t = 0 term: Q
        tot += Q
        Th2 = Sq
        for k in range(M):
            t = Tau[k]
            s = (Finv @ t) % p
            # Tr(t th^2): linear in Th2 coords: weight vector w2[j] = Tr(t x^j ... ) need Tr(t * u) for u=Th2 rows
            # Tr(t*u) = trv @ bmul(t,u); vectorize: precompute matrix Mt: (Mt @ u) = coeffs of t*u
            # build mult-by-t matrix
            Mt = np.zeros((p, p), dtype=np.int64)
            for j in range(p):
                ej = np.zeros((1, p), dtype=np.int64); ej[0, j] = 1
                Mt[:, j] = bmul(t[None, :], ej)[0]
            wt = (trv @ Mt) % p     # functional u -> Tr(t u)
            Ms = np.zeros((p, p), dtype=np.int64)
            for j in range(p):
                ej = np.zeros((1, p), dtype=np.int64); ej[0, j] = 1
                Ms[:, j] = bmul(s[None, :], ej)[0]
            ws = (trv @ Ms) % p
            ph = ((Th2 @ wt) + (All @ ws)) % p
            tot += np.sum(w**ph)
        lhs = tot / p**p
        print(f"   intermediate: p^-p * full double sum = {lhs:.8f} (should equal N+1 = 2)")

for p in [3, 5]:
    run(p, True)
run(7, False)
