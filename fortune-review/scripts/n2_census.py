#!/usr/bin/env python3
"""Census for the function-field d=1 crown (Papers V-VI) and for the
dynamical mechanisms M1/M2 of the review.

Computes, for primes p in a range:
  * N2(p)  = #{d in F_p : x^p + x^2 + d irreducible}  and the witness set;
  * quick diagnostics of the witness law (is d(p) a power of 2? quadratic
    character data of the witness);
  * for small p also Nsq, Nns and W_p = N2 + (Nsq+Nns)/2;
  * integrable-map checks (M1): factor-degree profile of the Chebyshev cubic
    graph polynomial x^p - (x^3 - 3x) and of special quadratic parameters
    d = 0, +-2 (conjugates of the power map / Chebyshev T2), verifying that
    "integrable" maps yield reducible polynomials with only small factors.

Irreducibility test used (dynamical form): a root of the monic degree-p
f = x^p - phi(x) (deg phi <= 3) satisfies alpha^{p^l} = phi^l(alpha).  Hence
f has an irreducible factor of degree dividing l iff gcd(phi^l(x) - x, f) != 1,
and f (of prime degree p) is irreducible iff gcd(phi^l(x)-x, f) = 1 for all
l <= p//2.  Each step costs one composition h -> phi(h) mod f (deg phi <= 3),
i.e. O(1) polynomial multiplications, not a full Frobenius power.
"""
import sys, math, time
import numpy as np

def primes_upto(n):
    sieve = np.ones(n + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return np.nonzero(sieve)[0].tolist()

def make_reducer(f, p):
    n = len(f) - 1
    xp = (-f[:n]) % p
    top = np.zeros((n - 1, n), dtype=np.int64)
    cur = xp.copy()
    for i in range(n - 1):
        top[i] = cur
        nxt = np.zeros(n + 1, dtype=np.int64)
        nxt[1:] = cur
        cur = (nxt[:n] + nxt[n] * xp) % p
    def reduce(r):
        r = r % p
        if len(r) <= n:
            out = np.zeros(n, dtype=np.int64); out[:len(r)] = r
            return out
        return (r[:n] + r[n:] @ top[:len(r) - n]) % p
    return reduce

def polygcd(a, b, p):
    a = np.trim_zeros(a % p, 'b'); b = np.trim_zeros(b % p, 'b')
    while len(b):
        while len(a) >= len(b):
            c = (int(a[-1]) * pow(int(b[-1]), p - 2, p)) % p
            a[len(a) - len(b):] = (a[len(a) - len(b):] - c * b) % p
            a = np.trim_zeros(a, 'b')
            if not len(a):
                break
        a, b = b, a
    return a

def factor_profile(f, p, phi_step, lmax=None):
    """Distinct-degree style profile via the dynamical iteration.
    Returns list of (l, degree_of_gcd) for l where gcd is nontrivial,
    plus 'rest' degree.  Not a full DDF (repeated factors lumped), but enough
    to certify (ir)reducibility and small-factor structure."""
    n = p
    red = make_reducer(f, p)
    x = np.zeros(n, dtype=np.int64); x[1] = 1
    h = phi_step(x, red)
    g = f.copy()
    found = []
    l = 1
    lim = lmax if lmax else p
    while l <= lim and len(np.trim_zeros(g, 'b')) - 1 > 0:
        d = polygcd(g.copy(), (h - x) % p, p)
        if len(d) > 1:
            found.append((l, len(d) - 1))
            # divide g by d (exact division)
            g = polydiv(g, d, p)
        h = phi_step(h, red)
        l += 1
    rest = len(np.trim_zeros(g, 'b')) - 1
    return found, rest

def polydiv(a, b, p):
    a = np.trim_zeros(a % p, 'b').astype(np.int64)
    b = np.trim_zeros(b % p, 'b').astype(np.int64)
    q = np.zeros(max(len(a) - len(b) + 1, 1), dtype=np.int64)
    binv = pow(int(b[-1]), p - 2, p)
    while len(a) >= len(b):
        c = (int(a[-1]) * binv) % p
        q[len(a) - len(b)] = c
        a[len(a) - len(b):] = (a[len(a) - len(b):] - c * b) % p
        a = np.trim_zeros(a, 'b')
        if not len(a):
            break
    return q

def is_irreducible(f, p, phi_step, chunk=16):
    n = p
    red = make_reducer(f, p)
    x = np.zeros(n, dtype=np.int64); x[1] = 1
    h = phi_step(x, red)
    acc = np.zeros(n, dtype=np.int64); acc[0] = 1
    pend = 0
    for l in range(1, p // 2 + 1):
        acc = red(np.convolve(acc, (h - x) % p))
        pend += 1
        if pend == chunk or l == p // 2:
            g = polygcd(f.copy(), acc.copy(), p)
            if len(g) != 1:
                return False
            acc = np.zeros(n, dtype=np.int64); acc[0] = 1
            pend = 0
        if l < p // 2:
            h = phi_step(h, red)
    return True

def quad_phi(d, p):
    """phi(x) = -x^2 - d  (for f = x^p + x^2 + d)."""
    def step(h, red):
        out = (p - red(np.convolve(h, h))) % p
        out[0] = (out[0] - d) % p
        return out
    return step

def cubic_phi(a, c, d, p):
    """phi(x) = -(a x^3 + c x + d) for f = x^p + a x^3 + c x + d."""
    def step(h, red):
        h2 = red(np.convolve(h, h))
        h3 = red(np.convolve(h2, h))
        out = (-(a * h3 + c * h) ) % p
        out[0] = (out[0] - d) % p
        return out
    return step

def N2_of(p, with_witness=True):
    wit = []
    for d in range(p):
        # cheap pre-filter: linear factor iff x^2 + x + d has a root in F_p,
        # i.e. 1 - 4d is a square (or 0) mod p
        disc = (1 - 4 * d) % p
        if disc == 0 or pow(disc, (p - 1) // 2, p) == 1:
            continue
        f = np.zeros(p + 1, dtype=np.int64); f[p] = 1; f[2] = 1; f[0] = d
        if is_irreducible(f, p, quad_phi(d, p)):
            wit.append(d)
    return len(wit), wit

def cubic_counts(p):
    def is_sq(a): return pow(a, (p - 1) // 2, p) == 1
    nsq = next(a for a in range(2, p) if not is_sq(a))
    out = {}
    for a in (1, nsq):
        cnt = 0
        for c in range(p):
            for d in range(p):
                f = np.zeros(p + 1, dtype=np.int64); f[p] = 1
                f[3] = a; f[1] = c; f[0] = d
                if is_irreducible(f, p, cubic_phi(a, c, d, p)):
                    cnt += 1
        out[a] = cnt
    return out[1], out[nsq]

def main():
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    cubic_pmax = int(sys.argv[2]) if len(sys.argv) > 2 else 31
    ps = [p for p in primes_upto(pmax) if p > 3]

    print("== N2 census: f = x^p + x^2 + d ==")
    print("p, N2, witnesses d, [d==2^k mod p?], chi_p(1-4d) (must be -1)")
    t0 = time.time()
    for p in ps:
        n2, wit = N2_of(p)
        pow2 = []
        for d in wit:
            k = None
            v = 1
            for e in range(1, p):
                v = (v * 2) % p
                if v == d:
                    k = e; break
            pow2.append(k)
        print(f"p={p:4d}  N2={n2}  wit={wit}  log2(wit)={pow2}", flush=True)
    print(f"[N2 census time {time.time()-t0:.1f}s]")

    print("\n== cubic sector counts and W_p (small p) ==")
    for p in [q for q in ps if q <= cubic_pmax]:
        n2, wit = N2_of(p)
        nsq, nns = cubic_counts(p)
        wp = n2 + (nsq + nns) // 2
        print(f"p={p:3d}  N2={n2} Nsq={nsq} Nns={nns}  W_p={wp}  W_p/p={wp/p:.3f}", flush=True)

    print("\n== M1 integrable-map diagnostics ==")
    print("Chebyshev cubic graph poly x^p - (x^3 - 3x): factor profile (l, deg) + rest")
    for p in [q for q in ps if 7 <= q <= 61]:
        f = np.zeros(p + 1, dtype=np.int64); f[p] = 1
        f[3] = (-1) % p; f[1] = 3 % p   # x^p - x^3 + 3x
        prof, rest = factor_profile(f, p, cubic_phi((-1) % p, 3 % p, 0, p), lmax=p // 2)
        print(f"p={p:3d}: factors found at l<=p/2: {prof}, undetected-degree rest={rest}")
    print("Special quadratic parameters d in {0, 2, p-2} (power map / Chebyshev conjugates):")
    for p in [q for q in ps if q <= 61]:
        row = []
        for d in (0, 2, (p - 2) % p):
            f = np.zeros(p + 1, dtype=np.int64); f[p] = 1; f[2] = 1; f[0] = d
            row.append((d, is_irreducible(f, p, quad_phi(d, p))))
        print(f"p={p:3d}: {row}")

if __name__ == "__main__":
    main()
