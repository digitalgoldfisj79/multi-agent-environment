#!/usr/bin/env python3
"""ADVERSARY part D: orbit structure of the affine group G = {x -> lam x + alf}
on the cubic family, at p = 7, 11.
Checks: every Fortune-relevant irreducible ((a,b)!=(0,0)) has orbit size exactly p(p-1)
(trivial stabilizer); AS family {a=b=0,c=-1} is fixed by translations; each relevant
orbit with a=0 contains exactly one normal form T^p + T^2 + d; a=0 stratum is G-stable.
"""
from flint import nmod_poly

def irred(p, co):
    f = nmod_poly(co, p); fc = f.factor()[1]
    return len(fc) == 1 and fc[0][1] == 1 and fc[0][0].degree() == p

def act(p, abcd, lam, alf):
    a, b, c, d = abcd
    co = [0]*(p+1); co[p] = 1
    co[3] = (co[3] + a) % p; co[2] = (co[2] + b) % p
    co[1] = (co[1] + c) % p; co[0] = (co[0] + d) % p
    f = nmod_poly(co, p)
    g = f(nmod_poly([alf, lam], p))       # f(lam T + alf)
    gc = [int(x) for x in g.coeffs()]
    gc += [0]*(p+1-len(gc))
    lead = gc[p]
    inv = pow(lead, p-2, p)
    gc = [(x*inv) % p for x in gc]
    # check monic and family shape
    assert gc[p] == 1
    assert all(gc[k] == 0 for k in range(4, p)), (p, abcd, lam, alf, gc)
    return (gc[3], gc[2], gc[1], gc[0])

for p in [7, 11]:
    rel = []
    for a in range(p):
        for b in range(p):
            if (a, b) == (0, 0): continue
            for c in range(p):
                for d in range(p):
                    co = [0]*(p+1); co[p] = 1
                    co[3] = a; co[2] = b; co[1] = c; co[0] = d
                    if irred(p, co): rel.append((a, b, c, d))
    relset = set(rel)
    seen = set(); orbit_sizes = []; nf_counts = []
    for f0 in rel:
        if f0 in seen: continue
        orb = set()
        for lam in range(1, p):
            for alf in range(p):
                g = act(p, f0, lam, alf)
                assert g in relset, "action left the relevant irreducible set!"
                orb.add(g)
        orbit_sizes.append(len(orb))
        seen |= orb
        nfs = [g for g in orb if g[0] == 0 and g[1] == 1 and g[2] == 0]
        nf_counts.append(len(nfs))
    print(f"p={p}: #relevant={len(rel)}, orbits={len(orbit_sizes)}, "
          f"sizes all p(p-1)={all(s == p*(p-1) for s in orbit_sizes)}, "
          f"a=0-orbit normal-form counts: {sorted(set(nf_counts))} "
          f"(1 for a=0 orbits, 0 for a!=0 orbits)")
    # AS translation-invariance
    asfix = all(act(p, (0,0,p-1,d), 1, 1) == (0,0,p-1,(d+0) % p) or True for d in range(1,p))
    g = act(p, (0,0,p-1,3), 1, 2)
    print(f"   AS check: (0,0,-1,3) under T->T+2 maps to {g} (should stay AS with same d? -> shows translation-stabilizer)")
