#!/usr/bin/env python3
"""ADVERSARY part A: independent brute-force counts.

For p in {3,5,7,11,13,17,19}:
  - #irred_2 over (b,c,d)   [quadratic family T^p + bT^2 + cT + d]
  - #irred_2 with b != 0
  - N(p) = #{d : T^p + T^2 + d irreducible}
  - check #irred_2 == p(p-1)N + (p-1) and b!=0 count == p(p-1)N
  - #irred_4 over (a,b,c,d) [cubic family T^p + aT^3 + bT^2 + cT + d],
    #relevant = (a,b) != (0,0); check relevant % (p(p-1)) == 0,
    check #irred_4 - relevant == p-1 (Artin-Schreier), and a=0 slice == #irred_2.
Independent method: flint factor with F_p-root prescreen (f(x) = ax^3+bx^2+(c+1)x+d... careful:
f(x)=x^p+ax^3+bx^2+cx+d, x in F_p => x^p=x => value = ax^3+bx^2+(c+1)x+d).
"""
import sys, time
from flint import nmod_poly

def irred(p, a, b, c, d):
    coeffs = [0]*(p+1)
    coeffs[p] = 1; coeffs[3] = (coeffs[3]+a) % p; coeffs[2] = (coeffs[2]+b) % p
    coeffs[1] = (coeffs[1]+c) % p; coeffs[0] = (coeffs[0]+d) % p
    f = nmod_poly(coeffs, p)
    fac = f.factor()
    facs = fac[1]
    return len(facs) == 1 and facs[0][1] == 1 and facs[0][0].degree() == p

expected_2 = {3:8, 5:24, 7:48, 11:120, 13:324, 17:288, 19:702}
expected_b = {3:6, 5:20, 7:42, 11:110, 13:312, 17:272, 19:684}

for p in [3,5,7,11,13,17,19]:
    t0 = time.time()
    # quadratic family
    n2 = 0; nb = 0
    for b in range(p):
        for c in range(p):
            # prescreen roots: value(x) = b x^2 + (c+1)x + d
            rootd = set((-(b*x*x + (c+1)*x)) % p for x in range(p))
            for d in range(p):
                if d in rootd: continue
                if irred(p, 0, b, c, d):
                    n2 += 1
                    if b: nb += 1
    N = sum(1 for d in range(p) if irred(p, 0, 1, 0, d))
    ok2 = (n2 == p*(p-1)*N + (p-1)) and (nb == p*(p-1)*N)
    okE = (n2 == expected_2[p]) and (nb == expected_b[p])
    # cubic family (only p>=5 is non-degenerate; do p=3 anyway and report raw)
    n4 = 0; rel = 0; a0 = 0
    for a in range(p):
        for b in range(p):
            for c in range(p):
                rootd = set((-(a*x**3 + b*x*x + (c+1)*x)) % p for x in range(p))
                for d in range(p):
                    if d in rootd: continue
                    if p == 3:
                        # build actual polynomial: T^3+aT^3 collides
                        continue
                    if irred(p, a, b, c, d):
                        n4 += 1
                        if (a, b) != (0, 0): rel += 1
                        if a == 0: a0 += 1
    if p > 3:
        okmod = (rel % (p*(p-1)) == 0)
        okAS = (n4 - rel == p-1)
        oka0 = (a0 == n2)
        print(f"p={p}: irred2={n2} (exp ok {okE}) b!=0={nb} N={N} pattern ok {ok2} | "
              f"irred4={n4} relevant={rel} rel/p(p-1)={rel/(p*(p-1)):.3f} mod-ok {okmod} "
              f"AS-ok {okAS} a0slice-ok {oka0} | irred4/p^3={n4/p**3:.4f} | {time.time()-t0:.1f}s",
              flush=True)
    else:
        print(f"p=3: irred2={n2} (exp ok {okE}) b!=0={nb} N={N} pattern ok {ok2} "
              f"[cubic family degenerate at p=3, skipped] | {time.time()-t0:.1f}s", flush=True)
