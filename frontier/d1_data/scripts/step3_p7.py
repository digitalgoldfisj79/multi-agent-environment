#!/usr/bin/env python3
"""Step 3: p=7 verification of the cheap pieces of the ledger.
(A) master identity p*#irred_4 = C - p^4 (direct C count over F_Q x F_p^3)
(E1) u=v=0 stratum: #(t,w): wt + t^{1/p} = 0 equals p-1
(E3) closed Gauss form: chi(-1)^((p+3)/2) p^((3-p)/2) A' = #irred_2 - (p-1),
     A' = sum_{t in kerTr\0} eta(t) chi(Tr(t^{2-p}))
(V) |V_t| = p^{p-2} exactly for sampled t (also full check at p=5)
(R) inferred R_a = p^{p-2}(#irred_a - p^2) + p from verified slice formula
"""
import numpy as np, sys, time
from itertools import product
sys.path.insert(0, '/tmp/claude-0/-home-user-multi-agent-environment/53da20a7-5af0-58c9-b6a4-3bdefd3e2c90/scratchpad')
from fqlib import FQ, irred_mask_family

def legendre(x, p):
    x %= p
    if x == 0: return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1

p = 7
t0 = time.time()
K = FQ(p); Q = K.Q
Th = K.all_elements()
Th2 = K.bmul(Th, Th)
Th3 = K.bmul(Th2, Th)
Thp = K.frob(Th)
print(f"setup {time.time()-t0:.1f}s")

# brute force counts (again, for slices)
quads = np.array(list(product(range(p), repeat=4)), dtype=np.int64)
mask = irred_mask_family(p, quads)
tot4 = int(mask.sum())
slices = {a: int(mask[quads[:, 0] == a].sum()) for a in range(p)}
irred2 = slices[0]
print(f"#irred_4 = {tot4}, slices = {slices}")

# (A) master identity
t0 = time.time()
C = 0
for a in range(p):
    ga = (Thp + a * Th3) % p
    for b in range(p):
        gb = (ga + b * Th2) % p
        for c in range(p):
            g = (gb + c * Th) % p
            C += int(np.all(g[:, 1:] == 0, axis=1).sum())
print(f"(A) C = {C}; C - p^4 = {C - p**4}; p*#irred_4 = {p*tot4}; "
      f"match = {C - p**4 == p*tot4}  ({time.time()-t0:.1f}s)")

# kernel of trace
tr_all = K.tr(Th)
idx = np.arange(Q)
ker_mask = (tr_all == 0) & (idx != 0)
Tker = Th[ker_mask]
nker = Tker.shape[0]
assert nker == p**(p-1) - 1
T1p_all = K.invfrob(Tker)

# (E1)
cnt = 0
for w in range(p):
    z = (w * Tker + T1p_all) % p
    cnt += int(np.all(z == 0, axis=1).sum())
print(f"(E1) u=v=0 stratum count = {cnt} (pred {p-1})")

# (E3) closed Gauss form
t0 = time.time()
eta = K.eta_table()
e_exp = Q - 1 - (p - 2)
Tpow = K.bpow(Tker, e_exp)
kappa = K.tr(Tpow)
eta_t = eta[K.encode(Tker)]
leg = np.array([legendre(x, p) for x in range(p)])
chi_kappa = leg[kappa]
Aprime = int((eta_t * chi_kappa).sum())
sgn = legendre(-1, p) ** ((p + 3) // 2)
closed = sgn * p ** ((3 - p) / 2) * Aprime
print(f"(E3) A' = {Aprime}; closed = {closed:.6f}; #irred_2-(p-1) = {irred2-(p-1)}; "
      f"match = {abs(closed - (irred2-(p-1))) < 1e-9}  ({time.time()-t0:.1f}s)")

# (V) |V_t| checks: sample 50 t at p=7
rng = np.random.default_rng(2)
Bmat = K.B
ok = True
for i in rng.integers(0, nker, 50):
    t = Tker[i]
    w1 = (t @ Bmat) % p
    q1 = (Th @ w1) % p
    q2 = (Th2 @ w1) % p
    ok &= int(((q1 == 0) & (q2 == 0)).sum()) == p ** (p - 2)
print(f"(V) |V_t| = p^(p-2) for 50 random t at p=7: {ok}")

# (R) inferred R_a
print("(R) inferred R_a = p^(p-2)(#irred_a - p^2) + p  [from slice formula, proved for p>=5]:")
for a in range(1, p):
    Ra = p ** (p - 2) * (slices[a] - p * p) + p
    print(f"   a={a} (chi={legendre(a,p):+d}): #irred_a = {slices[a]}, "
          f"R_a = {Ra}, R_a/p^p = {Ra/p**p:+.4f}")

# also p=5 full |V_t| check
p5 = 5
K5 = FQ(p5)
Th5 = K5.all_elements()
Th52 = K5.bmul(Th5, Th5)
tr5 = K5.tr(Th5)
ker5 = Th5[(tr5 == 0) & (np.arange(K5.Q) != 0)]
ok5 = True
for t in ker5:
    w1 = (t @ K5.B) % p5
    q1 = (Th5 @ w1) % p5
    q2 = (Th52 @ w1) % p5
    ok5 &= int(((q1 == 0) & (q2 == 0)).sum()) == p5 ** (p5 - 2)
print(f"(V5) |V_t| = p^(p-2) for ALL t in kerTr\\0 at p=5: {ok5}")
