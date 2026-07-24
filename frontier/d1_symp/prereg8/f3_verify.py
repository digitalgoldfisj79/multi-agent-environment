"""
f3_verify.py — PREREG-8: independent re-derivation of Tr(F^3|U_k) at p = 17, 23, 29.
Own implementation: scalar arithmetic mod ell (ell ≡ 1 mod p), 3D p-ary DFT over F_{p^3},
h-recurrence with alpha*beta = p^3, signed CRT over 9 primes + 10th as overdetermination.
Compares against locked predictions in checkpoints/f3_predictions.pkl.
"""
import pickle, sympy

def find_irred_cubic(p):
    for m0 in range(1, p):
        for m1 in range(p):
            for m2 in range(p):
                if all((x**3 + m2*x*x + m1*x + m0) % p for x in range(p)):
                    return [m0, m1, m2, 1]
    raise RuntimeError

def polmulmod(a, b, mp, p):
    r = [0]*5
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                r[i+j] = (r[i+j] + ai*bj) % p
    for d in (4, 3):
        c = r[d]
        if c:
            r[d] = 0
            for k in range(3):
                r[d-3+k] = (r[d-3+k] - c*mp[k]) % p
    return r[:3]

def trace_table(mp, p):
    n = 3
    s = [n % p]
    for k in range(1, n):
        acc = 0
        for i in range(1, k):
            acc = (acc + mp[n-i]*s[k-i]) % p
        acc = (acc + k*mp[n-k]) % p
        s.append((-acc) % p)
    return s

def crt_signed(residues, mods):
    M = 1
    for m in mods: M *= m
    x = 0
    for r, m in zip(residues, mods):
        Mi = M // m
        x = (x + r * Mi * pow(Mi, -1, m)) % M
    if x > M // 2: x -= M
    return x, M

results = {}
pred = pickle.load(open('checkpoints/f3_predictions.pkl', 'rb'))['pred']
targets = {17: ('U17', 'U15'), 23: ('U23', 'U21'), 29: ('U29', 'U27')}

for p in (17, 23, 29):
    mp_ = find_irred_cubic(p)
    tt = trace_table(mp_, p)
    # TR3[c0][c1][c2] = Tr(x^3) for element c0 + c1*t + c2*t^2
    TR3 = [[[0]*p for _ in range(p)] for _ in range(p)]
    for c0 in range(p):
        for c1 in range(p):
            for c2 in range(p):
                a = [c0, c1, c2]
                a2 = polmulmod(a, a, mp_, p)
                a3 = polmulmod(a2, a, mp_, p)
                TR3[c0][c1][c2] = (a3[0]*tt[0] + a3[1]*tt[1] + a3[2]*tt[2]) % p
    # find 10 primes ell ≡ 1 mod p near 1e9
    ells = []
    n0 = 10**9 // p
    n = n0
    while len(ells) < 10:
        n += 1
        L = n*p + 1
        if sympy.isprime(L): ells.append(L)
    res_p = {targets[p][0]: [], targets[p][1]: []}
    anchors_ok = True
    for L in ells:
        g = sympy.primitive_root(L)
        z = pow(g, (L-1)//p, L)
        zp = [pow(z, k, L) for k in range(p)]
        W = [[zp[(a*b) % p] for b in range(p)] for a in range(p)]
        # F array
        F = [[[zp[TR3[c0][c1][c2]] for c2 in range(p)] for c1 in range(p)] for c0 in range(p)]
        # DFT axis 0
        G1 = [[[0]*p for _ in range(p)] for _ in range(p)]
        for a in range(p):
            Wa = W[a]
            for y in range(p):
                for zc in range(p):
                    s = 0
                    for x in range(p):
                        s += Wa[x]*F[x][y][zc]
                    G1[a][y][zc] = s % L
        # axis 1
        G2 = [[[0]*p for _ in range(p)] for _ in range(p)]
        for x in range(p):
            for a in range(p):
                Wa = W[a]
                for zc in range(p):
                    s = 0
                    for y in range(p):
                        s += Wa[y]*G1[x][y][zc]
                    G2[x][a][zc] = s % L
        # axis 2
        vals = []
        for x in range(p):
            for y in range(p):
                row = G2[x][y]
                for a in range(p):
                    Wa = W[a]
                    s = 0
                    for zc in range(p):
                        s += Wa[zc]*row[zc]
                    vals.append(s % L)
        # anchors
        d000 = vals[0]
        s1 = sum(vals) % L
        s2 = sum(v*v for v in vals) % L
        if not (d000 == 0 and s1 == pow(p, 3, L) and s2 == pow(p, 6, L)):
            anchors_ok = False
            print(f"ANCHOR FAIL p={p} ell={L}: D0={d000} s1={s1} s2={s2}")
        # h-recurrence
        P3 = pow(p, 3, L)
        Sp = 0; Spm2 = 0
        for t in vals:
            h0, h1 = 1, (-t) % L
            for k in range(2, p+1):
                h0, h1 = h1, ((-t)*h1 - P3*h0) % L
                if k == p-2: hp2 = h1
            Sp = (Sp + h1) % L
            Spm2 = (Spm2 + hp2) % L
        res_p[targets[p][0]].append((-Sp) % L)
        res_p[targets[p][1]].append((-Spm2) % L)
    # CRT on first 9, check 10th, compare prediction
    for name in targets[p]:
        rec, M = crt_signed(res_p[name][:9], ells[:9])
        tenth_ok = (rec % ells[9]) == res_p[name][9]
        match = (rec == pred[name])
        results[name] = dict(value=rec, tenth_prime_ok=tenth_ok, matches_prediction=match)
        print(f"{name}: measured={rec}")
        print(f"      10th-prime check={tenth_ok}  matches Sol Pro prediction={match}")
    results[f'anchors_p{p}'] = anchors_ok
pickle.dump(results, open('checkpoints/f3_verify.pkl', 'wb'))
print("DONE f3_verify")
