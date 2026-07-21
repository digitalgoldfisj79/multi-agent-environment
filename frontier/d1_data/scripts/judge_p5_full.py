"""JUDGE: independent p=5 (and p=7 brute force) verification of the cubic ledger.

Written from scratch (not reusing prior session code) to independently check:
  (1) brute-force counts #irred_2, #irred_4, slices #irred_a, N(p)
  (2) b=0 translation reduction: #irred_a = p * #irred_{a,b=0} for a != 0
  (3) exact slice decomposition #irred_a = p^2 - p^{3-p} + p^{2-p} R_a with
      R_a = sum_{t in kerTr\0} sum_{theta in V_t \ F_p} e_p(Tr(a t theta^3 + t^{1/p} theta))
  (4) |V_t| = p^{p-2} for all t in kerTr\0
  (5) u=0,v!=0 stratum closed form: A' = sum eta(t) chi(Tr(t^{2-p})), contribution
      chi(-1)^{(p+3)/2} p^{(3-p)/2} A'  =?=  #irred_2 - (p-1)
  (6) t in F_p^* strata of quadratic formula contribute exactly p-1 (adversary Defect 5)
  (7) second moment: sum_{t in kerTr} |W(ut,vt,wt+t^{1/p})|^2 for (u,v,w)=(2,4,1)
      =?= 11434375, and N_corr = #{(th1,th2): g(th1)-g(th2) in F_p} =?= 18295
      i.e. N_corr - p^{p+1} = 2670 (adversary) and (p+1)Q - p + E with E=-450 (writeup)
  (8) second moment of E_a(t) over t: is typical |E_a(t)| ~ sqrt(|V_t|) = p^{(p-2)/2}
      or ~ p^{(p+1)/2}?  (decides between writeup sec.6 claim and random model)
"""
import numpy as np
from itertools import product

p = 5
Q = p**p

# ---- F_Q = F_p[x]/(x^p - x + 1) via generator log tables ----
# poly mult mod f, elements as tuples of length p (coeff of x^0..x^{p-1})
MOD = [0]*(2*p)  # x^p = x - 1  -> reduction
def polymulmod(a, b):
    c = [0]*(2*p-1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                c[i+j] = (c[i+j] + ai*bj) % p
    # reduce: x^k for k>=p: x^p = x - 1
    for k in range(2*p-2, p-1, -1):
        ck = c[k]
        if ck:
            c[k] = 0
            c[k-p+1] = (c[k-p+1] + ck) % p     # +x^{k-p+1}
            c[k-p]   = (c[k-p] - ck) % p       # -x^{k-p}
    return tuple(c[:p])

def idx(tup):  # element -> integer id, base p
    s = 0
    for i in range(p-1, -1, -1):
        s = s*p + tup[i]
    return s
def tup_of(i):
    t = []
    for _ in range(p):
        t.append(i % p); i //= p
    return tuple(t)

# find generator
one = tuple([1]+[0]*(p-1))
xgen_candidates = []
def order_of(g):
    e = g; n = 1
    while e != one:
        e = polymulmod(e, g); n += 1
        if n > Q: return -1
    return n
import random
random.seed(1)
gen = None
while gen is None:
    cand = tuple(random.randrange(p) for _ in range(p))
    if all(c == 0 for c in cand): continue
    if order_of(cand) == Q-1:
        gen = cand
print("generator found")

# log/exp tables
explog = np.zeros(Q-1, dtype=np.int64)   # exp table: id of gen^k
logtab = -np.ones(Q, dtype=np.int64)     # log of element id
e = one
for k in range(Q-1):
    explog[k] = idx(e)
    logtab[idx(e)] = k
    e = polymulmod(e, gen)
assert e == one

# trace: Tr(x^j) precompute -> linear functional
# Tr(theta) = sum_{i=0}^{p-1} theta^{p^i}. Compute via Frobenius matrix on basis.
def frob(t):  # t^p
    l = logtab[idx(t)]
    if l < 0: return tuple([0]*p)
    return tup_of(explog[(l*p) % (Q-1)])
trvec = []
for j in range(p):
    bj = tuple(1 if i == j else 0 for i in range(p))
    s = [0]*p
    e2 = bj
    for i in range(p):
        for k in range(p): s[k] = (s[k] + e2[k]) % p
        e2 = frob(e2)
    # trace must be in F_p: check
    assert all(s[k] == 0 for k in range(1, p)), s
    trvec.append(s[0])
trvec = np.array(trvec, dtype=np.int64)
print("trace functional on basis:", trvec)

# vectorized tables over all element ids
digits = np.zeros((Q, p), dtype=np.int64)
tmp = np.arange(Q)
for i in range(p):
    digits[:, i] = tmp % p; tmp = tmp // p
TR = (digits @ trvec) % p                      # Tr(element)
LOG = logtab.copy()

def mul_ids(a_ids, b_ids):
    """elementwise product of element-id arrays (0 maps to 0)."""
    a_ids = np.asarray(a_ids); b_ids = np.asarray(b_ids)
    out = np.zeros(np.broadcast(a_ids, b_ids).shape, dtype=np.int64)
    nz = (a_ids != 0) & (b_ids != 0)
    la = LOG[a_ids][..., ] if a_ids.shape else LOG[a_ids]
    out[nz] = explog[(LOG[a_ids][nz] + LOG[b_ids][nz]) % (Q-1)]
    return out

def pow_id(a_id, k):
    if a_id == 0: return 0
    return explog[(LOG[a_id]*k) % (Q-1)]

ALL = np.arange(Q)
SQ  = np.array([pow_id(i, 2) for i in range(Q)])
CU  = np.array([pow_id(i, 3) for i in range(Q)])
FP_ids = np.array([idx(tuple([a]+[0]*(p-1))) for a in range(p)])  # F_p elements
isFp = np.zeros(Q, dtype=bool); isFp[FP_ids] = True

kerTr = ALL[(TR == 0)]
kerTr_nz = kerTr[kerTr != 0]
print("|kerTr| =", len(kerTr), "expected", p**(p-1))

# t^{1/p} = t^{p^{p-1}}
inv_frob_exp = pow(p, p-1, Q-1)
def invfrob_id(t):
    return explog[(LOG[t]*inv_frob_exp) % (Q-1)] if t != 0 else 0

w1 = np.exp(2j*np.pi/p)

# ---------- (1) brute force counts via flint ----------
from flint import nmod_poly
def is_irred_degp(coeffs, pp):
    """coeffs low->high of monic degree-pp poly over F_pp; prime degree test."""
    f = nmod_poly(coeffs, pp)
    x = nmod_poly([0, 1], pp)
    h = pow(x, pp, f)          # x^p mod f  (python-flint supports pow with mod)
    if f.gcd(h - x).degree() > 0:
        return False
    g = h
    for _ in range(pp - 1):
        g = pow(g, pp, f)
    return g == x

# validate against factor() on some random cases
def is_irred_factor(coeffs, pp):
    f = nmod_poly(coeffs, pp)
    fac = f.factor()
    return len(fac[1]) == 1 and fac[1][0][1] == 1 and fac[1][0][0].degree() == pp
for _ in range(200):
    co = [random.randrange(p) for _ in range(4)] + [0]*(p-4) + [1]
    assert is_irred_degp(co, p) == is_irred_factor(co, p)
print("irreducibility test validated against factor()")

def count_all(pp):
    ir2 = 0; ir4 = 0; slices = {}
    Npp = 0
    for a in range(pp):
        cnt = 0
        for b in range(pp):
            for c in range(pp):
                for d in range(pp):
                    co = [d, c, b, a] + [0]*(pp-4) + [1]
                    if is_irred_degp(co, pp):
                        cnt += 1
                        if a == 0: ir2 += 1
        slices[a] = cnt; ir4 += cnt
    for d in range(pp):
        co = [d, 0, 1] + [0]*(pp-3) + [1]
        if is_irred_degp(co, pp): Npp += 1
    return ir2, ir4, slices, Npp

ir2, ir4, slices, N5 = count_all(5)
print("p=5 brute force: #irred_2 =", ir2, " #irred_4 =", ir4, " N(5) =", N5)
print("  slices:", slices)

# (2) b=0 reduction
for a in range(1, p):
    cnt0 = 0
    for c in range(p):
        for d in range(p):
            co = [d, c, 0, a] + [0]*(p-4) + [1]
            if is_irred_degp(co, p): cnt0 += 1
    assert slices[a] == p*cnt0, (a, slices[a], cnt0)
print("b=0 reduction verified at p=5: #irred_a = p * #irred_{a,b=0} for all a!=0")

# ---------- (3),(4) slice decomposition R_a ----------
Rs = {}
Vt_sizes = []
sumE2 = 0.0   # for (8): second moment of E_a(t) for a=1
E1_vals = []
for t in kerTr_nz:
    t_th  = mul_ids(np.full(Q, t), ALL)
    t_th2 = mul_ids(np.full(Q, t), SQ)
    mask = (TR[t_th] == 0) & (TR[t_th2] == 0)
    Vt = ALL[mask]
    Vt_sizes.append(len(Vt))
    tinv = invfrob_id(t)
    phase_lin = TR[mul_ids(np.full(len(Vt), tinv), Vt)]            # Tr(t^{1/p} theta)
    t_th3 = TR[mul_ids(np.full(len(Vt), t), CU[Vt])]               # Tr(t theta^3)
    notFp = ~isFp[Vt]
    for a in range(1, p):
        ph = (a*t_th3 + phase_lin) % p
        Rs[a] = Rs.get(a, 0) + np.sum(np.exp(2j*np.pi*ph[notFp]/p))
    # E_a(t) for a=1 including... (defined over V_t \ F_p in writeup; also full V_t version)
    ph1 = (1*t_th3 + phase_lin) % p
    E1 = np.sum(np.exp(2j*np.pi*ph1[notFp]/p))
    E1_vals.append(E1)

Vt_sizes = np.array(Vt_sizes)
print("(4) |V_t| all equal p^{p-2}?", np.all(Vt_sizes == p**(p-2)), " value:", Vt_sizes[0])
for a in range(1, p):
    Ra = Rs[a]
    assert abs(Ra.imag) < 1e-6
    pred = p**2 - p**(3-p) + p**(2-p)*Ra.real
    print(f"(3) a={a}: R_a = {Ra.real:+.4f}   predicted #irred_a = {pred:.6f}  brute = {slices[a]}")

E1_vals = np.array(E1_vals)
m2 = np.mean(np.abs(E1_vals)**2)
print(f"(8) second moment of E_1(t) over t!=0 in kerTr: mean|E|^2 = {m2:.1f}")
print(f"    compare |V_t| = p^(p-2) = {p**(p-2)} (random/sqrt model) vs p^(p+1) = {p**(p+1)} (critical model)")
print(f"    rms|E_1| = {np.sqrt(m2):.2f};  sqrt(p^(p-2)) = {p**((p-2)/2):.2f};  p^((p+1)/2) = {p**((p+1)/2):.2f}")

# ---------- (5) u=0,v!=0 closed form ----------
# eta = quadratic character of F_Q: eta(t) = (-1)^(log t) ... t is square iff log even
def eta_id(t):
    return 1 if LOG[t] % 2 == 0 else -1
def chi_fp(a):  # Legendre symbol on F_p, a in 0..p-1
    if a % p == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1
Aprime = 0
for t in kerTr_nz:
    t2mp = pow_id(t, (2-p) % (Q-1))
    Aprime += eta_id(t) * chi_fp(int(TR[t2mp]))
contrib = (chi_fp(-1)**((p+3)//2)) * p**((3-p)/2) * Aprime
print(f"(5) A' = {Aprime}, closed-form contribution = {contrib:.6f}, expected #irred_2-(p-1) = {ir2-(p-1)}")

# ---------- (6) t in F_p^* strata of the QUADRATIC formula ----------
contribFp = 0.0
for a in range(1, p):
    t = int(FP_ids[a])
    t_th  = mul_ids(np.full(Q, t), ALL)
    t_th2 = mul_ids(np.full(Q, t), SQ)
    mask = (TR[t_th] == 0) & (TR[t_th2] == 0)
    Vt = ALL[mask]
    tinv = invfrob_id(t)
    ph = TR[mul_ids(np.full(len(Vt), tinv), Vt)]
    contribFp += np.sum(np.exp(2j*np.pi*ph/p)).real
contribFp *= p**(2-p)
print(f"(6) t in F_p^* strata contribution to #irred_2 = {contribFp:.6f}, expected p-1 = {p-1}")

# ---------- (7) second moment for (u,v,w)=(2,4,1) ----------
u, v, w = 2, 4, 1
# g(theta) = theta^p + u theta^3 + v theta^2 + w theta ; theta^p via frobenius on ids
FR = np.array([explog[(LOG[i]*p) % (Q-1)] if i != 0 else 0 for i in range(Q)])
def add_ids(a_ids, b_ids):
    return np.array([idx(tuple((x+y) % p for x, y in zip(tup_of(int(i)), tup_of(int(j)))))
                     for i, j in zip(np.ravel(a_ids), np.ravel(b_ids))]).reshape(np.broadcast(a_ids,b_ids).shape)
# vectorized add via digit arrays
def add_ids_fast(a_ids, b_ids):
    da = digits[a_ids]; db = digits[b_ids]
    dc = (da + db) % p
    return dc @ (p ** np.arange(p))
uFp = int(FP_ids[u]); vFp = int(FP_ids[v]); wFp = int(FP_ids[w])
g1 = FR[ALL]
g2 = mul_ids(np.full(Q, uFp), CU)
g3 = mul_ids(np.full(Q, vFp), SQ)
g4 = mul_ids(np.full(Q, wFp), ALL)
gv = add_ids_fast(add_ids_fast(g1, g2), add_ids_fast(g3, g4))
# W(t) = sum_theta e_p(Tr(t * g(theta)))
S2 = 0.0
for t in kerTr:
    tt = int(t)
    ph = TR[mul_ids(np.full(Q, tt), gv)]
    W = np.sum(np.exp(2j*np.pi*ph/p))
    S2 += abs(W)**2
print(f"(7) sum_(t in kerTr) |W|^2 for (u,v,w)=(2,4,1): {S2:.1f}  expected 11434375")
# N_corr directly: coset histogram of g values (coset = drop constant digit)
coset = gv // p  # careful: constant coeff is digit 0 -> id % p is the F_p part
coset = np.array([int(i) // p for i in gv])   # id = c0 + p*(rest); coset id = rest
counts = np.bincount(coset, minlength=Q//p)
Ncorr = int(np.sum(counts.astype(np.int64)**2)) * 1
# wait: pairs with g(th1)-g(th2) in F_p <=> same coset of F_p. Each coset with n elements
# contributes n^2 ordered pairs... but difference in F_p means same coset: yes n_c^2, times p? no.
# g(th1)-g(th2) in F_p iff cosets equal; number of ordered pairs = sum n_c^2.
print(f"    N_corr = {np.sum(counts.astype(np.int64)**2)}  expected 18295;  p^(p-1)*N_corr = {625*np.sum(counts.astype(np.int64)**2)}")
print(f"    N_corr - p^(p+1) = {np.sum(counts.astype(np.int64)**2) - p**(p+1)}  (adversary reported 2670 for this triple)")
