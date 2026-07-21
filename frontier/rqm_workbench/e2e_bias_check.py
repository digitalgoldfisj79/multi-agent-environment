import itertools, math, cmath
# End-to-end: E_sigma[e_{qr}(b D_uv)] computed (A) directly over all K! perms,
# (B) via the slot character expansion: sum over chi-tuples prod_s c_{chi_s}(b c_s A) Phi(psi;n).
q, r = 3, 5
MOD = q*r
units = [u for u in range(MOD) if math.gcd(u, MOD) == 1]
phi = len(units)
def dl(p, g):
    d = {}; x = 1
    for k in range(p-1): d[x] = k; x = (x*g) % p
    return d
d3, d5 = dl(3, 2), dl(5, 2)
CH = []
for j3 in range(2):
    for j5 in range(4):
        CH.append({u: cmath.exp(2j*math.pi*(j3*d3[u % 3]/2 + j5*d5[u % 5]/4)) for u in units})
def em(x): return cmath.exp(2j*math.pi*(x % MOD)/MOD)
def cc(chi, m): return sum(em(m*w)*chi[w].conjugate() for w in units)/phi

Lp = [2, 7, 11, 13, 4, 8]   # 6 "block primes": units mod 15
K = 6
A = 2   # plays A_X (unit mod 15)
b = 4   # plays a(r-q) (unit mod 15)

def direct(tr, cf):
    tot = 0
    for perm in itertools.permutations(Lp):
        pref = [1]*(K+1)
        for i in range(K): pref[i+1] = pref[i]*perm[i]
        D = A*sum(cf[s]*pref[tr[s]] for s in range(len(tr)))
        tot += em(b*D)
    return tot/math.factorial(K)

def multinom(K, ns):
    v = math.factorial(K)
    for n in ns: v //= math.factorial(n)
    return v

def Phi(psivals, ns):
    # psivals: list per cell of dict ell->value; ns same length; coefficient extraction
    mm = len(ns)
    poly = {tuple([0]*mm): 1.0+0j}
    for ell in Lp:
        new = {}
        for exps, cval in poly.items():
            for s in range(mm):
                if exps[s] >= ns[s]: continue
                e2 = list(exps); e2[s] += 1; e2 = tuple(e2)
                new[e2] = new.get(e2, 0) + cval*psivals[s][ell]
        poly = new
    return poly.get(tuple(ns), 0)/multinom(K, ns)

def viachars(tr, cf):
    m = len(tr)
    ns = [tr[0]] + [tr[s+1]-tr[s] for s in range(m-1)] + [K - tr[-1]]
    slots = list(range(1, m+1))
    const = 1.0+0j
    if ns[0] == 0:
        const = em(b*A*cf[0])   # slot 1: e_{qr}(m_1 * 1), V_1 = empty product
        slots = slots[1:]
    tot = 0
    for tup in itertools.product(range(phi), repeat=len(slots)):
        cp = 1.0+0j
        for idx, s in enumerate(slots):
            cp *= cc(CH[tup[idx]], b*cf[s-1]*A)
        if abs(cp) < 1e-15: continue
        # cell characters psi_i = prod_{slots s>i} chi^{(s)}; cells 0..m; drop empty cells
        keep = [i for i in range(m+1) if ns[i] > 0]
        psiv, nsk = [], []
        for i in keep:
            dct = {}
            for ell in Lp:
                v = 1.0+0j
                for idx, s in enumerate(slots):
                    if s > i: v *= CH[tup[idx]][ell % MOD]
                dct[ell] = v
            psiv.append(dct); nsk.append(ns[i])
        tot += cp*Phi(psiv, nsk)
    return const*tot

tests = [
    ([1, 4], [1, -1]),               # m=2 sliding
    ([2, 5], [2, -2]),               # m=2 doubled
    ([0, 3], [1, -1]),               # empty W_0 (slot-1 constant)
    ([1, 3, 5], [1, 1, -2]),         # m=3
    ([2, 4, 5], [-1, 2, -1]),        # m=3 other pattern
    ([1, 2, 4, 6], [1, -1, -1, 1]),  # m=4, tail empty (t_m = K)
    ([0, 2, 4, 5], [1, 1, -1, -1]),  # m=4, empty W_0
    ([1, 2, 3, 5], [-1, 1, 1, -1]),  # m=4 generic with micro gaps
]
print("End-to-end bias check (K=6, qr=15, A=2, b=4): direct vs character expansion")
for tr, cf in tests:
    dv, cv = direct(tr, cf), viachars(tr, cf)
    print(f"  ranks={tr} c={cf}: err={abs(dv-cv):.2e}  |bias|={abs(dv):.5f}")
