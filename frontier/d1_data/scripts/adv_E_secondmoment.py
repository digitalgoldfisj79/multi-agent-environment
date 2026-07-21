#!/usr/bin/env python3
"""ADVERSARY part E: second-moment structure of the coupled cubic Weil sums, p=5.
Verify:  sum_{t in kerTr} |W(ut,vt,wt+t^{1/p})|^2  =  p^{p-1} * N_{u,v,w},
   N_{u,v,w} = #{(th1,th2): u(th1^3-th2^3)+v(th1^2-th2^2)+w(th1-th2)+(th1-th2)^p in F_p}.
Also report: max_t |W|, RMS over t != 0, Weil bound 2 sqrt(Q), and N - p^{p+1}.
And: sum_{t in kerTr} W = p^{p-1} * r(u,v,w) (first moment = Plancherel circularity).
"""
import numpy as np, math
from itertools import product
from flint import nmod_poly

p = 5; Q = p**p
hco = [1, p-1] + [0]*(p-2) + [1]
h = nmod_poly(hco, p)
red = np.zeros((2*p-1, p), dtype=np.int64)
for k in range(2*p-1):
    r = nmod_poly([0]*k + [1], p) % h
    for i, cc in enumerate(r.coeffs()): red[k, i] = int(cc)
def bmul(A, B):
    conv = np.zeros((A.shape[0], 2*p-1), dtype=np.int64)
    for i in range(p):
        for j in range(p):
            conv[:, i+j] += A[:, i]*B[:, j]
    conv %= p
    return (conv @ red) % p
F = np.zeros((p, p), dtype=np.int64)
for j in range(p):
    for i in range(j+1):
        F[i, j] = (math.comb(j, i)*pow(-1, j-i, p)) % p
S = np.zeros((p, p), dtype=np.int64); Fi = np.eye(p, dtype=np.int64)
for i in range(p):
    S = (S+Fi) % p; Fi = (Fi @ F) % p
trv = S[0]
Finv = np.linalg.matrix_power(F, p-1) % p

All = np.array(list(product(range(p), repeat=p)), dtype=np.int64)   # (Q,p)
Th2 = bmul(All, All); Th3 = bmul(Th2, All); Thp = (All @ F.T) % p
w = np.exp(2j*np.pi/p)

def trfunc(t):
    Mt = np.zeros((p, p), dtype=np.int64)
    for j in range(p):
        ej = np.zeros((1, p), dtype=np.int64); ej[0, j] = 1
        Mt[:, j] = bmul(t[None, :], ej)[0]
    return (trv @ Mt) % p

# kerTr elements
piv = next(i for i in range(p) if trv[i])
basis = []
for i in range(p):
    if i == piv: continue
    v = np.zeros(p, dtype=np.int64); v[i] = 1
    v[piv] = (-trv[i]*pow(int(trv[piv]), p-2, p)) % p
    basis.append(v)
basis = np.array(basis)
coefs = np.array(list(product(range(p), repeat=p-1)), dtype=np.int64)
Tau = (coefs @ basis) % p
nzmask = np.any(Tau != 0, axis=1)

rng = np.random.default_rng(1)
for (u, v, wc) in [(1, 0, 0), (1, 2, 3), (2, 4, 1)]:
    Ws = []
    Wsum = 0j; W2sum = 0.0
    for t in Tau:
        s = (Finv @ t) % p
        ft3 = trfunc((u*t) % p); ft2 = trfunc((v*t) % p)
        ft1 = trfunc((wc*t) % p); fs = trfunc(s)
        ph = ((Th3 @ ft3) + (Th2 @ ft2) + (All @ ft1) + (All @ fs)) % p
        W = np.sum(w**ph)
        Ws.append(W)
    Ws = np.array(Ws)
    lhs2 = np.sum(np.abs(Ws)**2)
    lhs1 = np.sum(Ws)
    # correlation count N_{u,v,w} over all pairs: vectorize over th2 for each th1? Q^2 = 9.7M pairs
    # Psi = u(th1^3-th2^3)+v(th1^2-th2^2)+w(th1-th2)+(th1-th2)^p
    # compute via broadcasting in chunks
    Ncorr = 0
    for i0 in range(0, Q, 250):
        A1 = All[i0:i0+250]
        T31 = Th3[i0:i0+250]; T21 = Th2[i0:i0+250]; Tp1 = Thp[i0:i0+250]
        # Psi coeff vectors: (chunk, Q, p)
        Psi = (u*(T31[:, None, :] - Th3[None, :, :])
               + v*(T21[:, None, :] - Th2[None, :, :])
               + wc*(A1[:, None, :] - All[None, :, :])
               + (Tp1[:, None, :] - Thp[None, :, :])) % p
        Ncorr += int(np.sum(np.all(Psi[:, :, 1:] == 0, axis=2)))
    # r(u,v,w) direct
    val = (Thp + u*Th3 + v*Th2 + wc*All) % p
    rdir = int(np.sum(np.all(val[:, 1:] == 0, axis=1)))
    print(f"(u,v,w)=({u},{v},{wc}):")
    print(f"  2nd moment sum_t|W|^2 = {lhs2:.3f} vs p^(p-1)*Ncorr = {p**(p-1)*Ncorr}  match={abs(lhs2 - p**(p-1)*Ncorr) < 1e-4}")
    print(f"  Ncorr = {Ncorr}, p^(p+1) = {p**(p+1)}, Ncorr - p^(p+1) = {Ncorr - p**(p+1)}, p^2 sqrt(Q) = {p*p*math.sqrt(Q):.0f}")
    print(f"  1st moment sum_t W = {lhs1:.3f} vs p^(p-1)*r - Q = {p**(p-1)*rdir - Q}  (r={rdir}, r-p = {rdir-p}, => #irred in (u,v,w)-pencil = {(rdir-p)//p})")
    Wnz = Ws[nzmask]
    print(f"  max|W| over t!=0 = {np.max(np.abs(Wnz)):.2f}, RMS = {np.sqrt(np.mean(np.abs(Wnz)**2)):.2f}, Weil 2sqrt(Q) = {2*math.sqrt(Q):.2f}, p^(1+p/4) = {p**(1+p/4):.2f}")
