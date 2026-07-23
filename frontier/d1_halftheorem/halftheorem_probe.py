#!/usr/bin/env python3
"""Half-theorem probe (p = 2 mod 3) for the wild-trace cubic reduction.

Independent implementation of WTCK section 5: compute
  N_b - p^{p-2} = p^{-2} sum_{v!=0,u} psi(-vb) S_p(u,v)
via the degree-two L-function recurrence, in EXACT Z[zeta_p] arithmetic
(integer vectors modulo Phi_p). Reproduces the committed p=5,7,11 examples,
then computes deviations for p = 13,17,19,23 to (a) verify cube-class
support (WTCK.4), (b) extract the p = 2 mod 3 nonzero-fibre CONSTANT and
hunt a closed form, (c) track the b=0 punctual term.
"""
import sys

def cyc_reduce(vec, p):
    """Reduce a length-p integer vector (coeffs of 1..zeta^{p-1}) to length p-1
    basis 1,zeta,...,zeta^{p-2} using zeta^{p-1} = -(1+...+zeta^{p-2})."""
    out = list(vec[:p-1])
    hi = vec[p-1] if len(vec) == p else 0
    if hi:
        out = [x - hi for x in out]
    return out

def cyc_mul(a, b, p):
    """Multiply two elements of Z[zeta_p] in basis 1..zeta^{p-2}."""
    n = p - 1
    full = [0]*(2*n - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    full[i+j] += ai*bj
    # fold exponents >= p via zeta^p = 1, then reduce zeta^{p-1}
    folded = [0]*p
    for e, cf in enumerate(full):
        folded[e % p] += cf
    return cyc_reduce(folded, p)

def cyc_addmul_shift(acc, vec, shift, p, sign=1):
    """acc += sign * zeta^shift * vec (vec in basis 1..zeta^{p-2})."""
    folded = [0]*p
    for e, cf in enumerate(vec):
        folded[(e + shift) % p] += sign*cf
    red = cyc_reduce(folded, p)
    for i in range(p-1):
        acc[i] += red[i]

def S1_vec(u, v, p):
    """S_1(u,v) = sum_x zeta^{ux+vx^3} as counts vector."""
    cnt = [0]*p
    for x in range(p):
        cnt[(u*x + v*x*x*x) % p] += 1
    return cyc_reduce(cnt, p)

def build_fp2(p):
    """F_{p^2} = F_p(w), w^2 = n (n a nonresidue). Return n and cube table."""
    n = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
    elems = [(A, B) for A in range(p) for B in range(p)]
    def mul(x, y):
        return ((x[0]*y[0] + n*x[1]*y[1]) % p, (x[0]*y[1] + x[1]*y[0]) % p)
    cubes = {}
    for e in elems:
        e2 = mul(e, e)
        cubes[e] = mul(e2, e)
    return n, elems, cubes

def S2_vec(u, v, p, elems, cubes):
    """S_2(u,v) = sum_{x in F_{p^2}} zeta^{Tr(ux+vx^3)}, Tr(A+Bw) = 2A."""
    cnt = [0]*p
    for x in elems:
        c = cubes[x]
        A = (u*x[0] + v*c[0]) % p
        cnt[(2*A) % p] += 1
    return cyc_reduce(cnt, p)

def halve(vec):
    assert all(c % 2 == 0 for c in vec), "E2 not divisible by 2"
    return [c//2 for c in vec]

def deviations(p):
    """Return list D_b (b = 0..p-1) of exact integers N_b - p^{p-2}."""
    n_, elems, cubes = build_fp2(p)
    one = [1] + [0]*(p-2)
    acc = {b: [0]*(p-1) for b in range(p)}
    for v in range(1, p):
        for u in range(0, p):
            P1 = [-c for c in S1_vec(u, v, p)]
            P2 = [-c for c in S2_vec(u, v, p, elems, cubes)]
            E2 = halve([a - b for a, b in zip(cyc_mul(P1, P1, p), P2)])
            # P_r = P1*P_{r-1} - E2*P_{r-2}
            Pm2, Pm1 = P1, P2
            for _ in range(3, p+1):
                Pr = [a - b for a, b in zip(cyc_mul(P1, Pm1, p),
                                            cyc_mul(E2, Pm2, p))]
                Pm2, Pm1 = Pm1, Pr
            Sp = [-c for c in Pm1]  # S_p(u,v) = -(alpha^p+beta^p)
            for b in range(p):
                cyc_addmul_shift(acc[b], Sp, (-v*b) % p, p)
    out = []
    for b in range(p):
        vec = acc[b]
        assert all(c % (p*p) == 0 for c in vec), f"not divisible by p^2 at b={b}"
        vec = [c//(p*p) for c in vec]
        assert all(c == 0 for c in vec[1:]), f"non-rational deviation at b={b}: {vec}"
        out.append(vec[0])
    return out

if __name__ == "__main__":
    maxp = int(sys.argv[1]) if len(sys.argv) > 1 else 23
    from sympy import primerange
    for p in primerange(5, maxp+1):
        D = deviations(p)
        norm = p**((p-3)//2)
        Dn = [d/norm for d in D]
        cls = "p=1 mod 3" if p % 3 == 1 else "p=2 mod 3"
        nz = sorted(set(D[1:]))
        print(f"p={p} ({cls}): D_0={D[0]} (D_0/norm={Dn[0]:+.3f}); "
              f"nonzero-b deviations/norm: {sorted(set(round(x,6) for x in Dn[1:]))}; "
              f"raw distinct nonzero-b: {nz}", flush=True)
        # verify cube-class constancy
        cubes_mod = {pow(x, 3, p) for x in range(1, p)}
        classes = {}
        for b in range(1, p):
            key = next(i for i, s in enumerate(sorted({frozenset((b*c) % p for c in cubes_mod)})) ) if False else None
        # direct check: D_b depends only on cube class of b
        for b in range(1, p):
            for s in range(2, p):
                if D[(pow(s,3,p)*b) % p] != D[b]:
                    print(f"  CUBE-CLASS VIOLATION at p={p}, b={b}"); break
