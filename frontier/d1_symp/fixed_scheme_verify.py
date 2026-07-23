#!/usr/bin/env python3
"""Exact checks for the cyclic fixed-scheme calculation.

For W=H/F_p with the cyclic shift acting as one Jordan block of length
n=p-2, the projective fixed scheme is k[t]/(t^n).  In the canonical
formal eigenvector

    x_i(t) = ((1+t)^i-1)/t = sum_{r>=0} binom(i,r+1)t^r,

the descended forms satisfy modulo t^(p-2):

    Q(t) = -t^(p-3),
    C(t) = t^(p-4)*(1+t/2).

Hence Fix(sigma,X_p) has completed local ring k[t]/(t^(p-4)).
This script checks the identities in exact F_p arithmetic for selected
primes.  It is evidence for the displayed algebraic proof, not a proof
by prime sweep.
"""
from math import comb


def add(a, b, p, n):
    return [((a[i] if i < len(a) else 0) +
             (b[i] if i < len(b) else 0)) % p for i in range(n)]


def mul(a, b, p, n):
    out = [0] * n
    for i, ai in enumerate(a[:n]):
        if ai:
            for j, bj in enumerate(b[:n-i]):
                if bj:
                    out[i+j] = (out[i+j] + ai * bj) % p
    return out


def fixed_forms(p):
    n = p - 2
    xs = []
    for i in range(p):
        x = [0] * n
        for r in range(min(i, n)):
            x[r] = comb(i, r + 1) % p
        xs.append(x)

    trace = [0] * n
    Q = [0] * n
    C = [0] * n
    for x in xs:
        trace = add(trace, x, p, n)
        x2 = mul(x, x, p, n)
        Q = add(Q, x2, p, n)
        C = add(C, mul(x2, x, p, n), p, n)
    return trace, Q, C


def expected(p):
    n = p - 2
    q = [0] * n
    c = [0] * n
    q[p - 3] = -1 % p
    c[p - 4] = 1
    c[p - 3] = pow(2, -1, p)
    return [0] * n, q, c


if __name__ == "__main__":
    for p in (5, 7, 11, 13, 17, 19, 23):
        got = fixed_forms(p)
        want = expected(p)
        assert got == want, (p, got, want)
        print(f"p={p}: trace=0, Q=-t^{p-3}, "
              f"C=t^{p-4}(1+t/2) mod t^{p-2}; fixed length={p-4}: OK")
    print("ALL FIXED-SCHEME IDENTITIES VERIFIED EXACTLY")
