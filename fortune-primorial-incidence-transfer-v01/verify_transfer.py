#!/usr/bin/env python3
"""Exact finite diagnostics for Primorial Incidence Transfer v0.1.

These checks validate algebraic identities and finite combinatorics only; they are not
used as evidence for the asymptotic PNT or Stevens--de Zeeuw incidence theorem.
"""
from collections import Counter
from math import log
import json


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    if n >= 0: sieve[0] = 0
    if n >= 1: sieve[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * (((n - p*p)//p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True


def next_prime(n):
    q = n + 1
    while not is_prime(q):
        q += 1
    return q


def inv(a, p):
    return pow(a, p-2, p)


def panel(X):
    allp = primes_upto(2*X)
    qs = [q for q in allp if X <= q <= 2*X]
    assert len(qs) >= 3
    mod = next_prime(2*X)
    assert mod > 2*X

    B = 1
    for q in allp:
        if q >= X: break
        B = (B*q) % mod
    P = [B]
    for q in qs:
        P.append((P[-1]*q) % mod)
    A = set(P)

    # Exact recurrence for all transitions.
    for j in range(len(qs)-1):
        g = qs[j+1] - qs[j]
        lhs = P[j+2]
        rhs = (g*P[j+1] + P[j+1]*P[j+1]*inv(P[j], mod)) % mod
        assert lhs == rhs, (X,j,lhs,rhs)

    gaps = [qs[j+1]-qs[j] for j in range(len(qs)-1)]
    short = [g for g in gaps if g <= 6*log(X)]
    counts = Counter(short)
    d,T = max(counts.items(), key=lambda kv: kv[1])
    assert d % 2 == 0 and d != 0 and d < mod

    # Every selected gap gives a distinct (x,a) transition inside A.
    seen = set()
    for j,g in enumerate(gaps):
        if g != d: continue
        x,a,z = P[j],P[j+1],P[j+2]
        assert (d*a + a*a*inv(x,mod)) % mod == z
        assert x in A and a in A and z in A
        pair=(x,a)
        assert pair not in seen
        seen.add(pair)
        assert (a*inv(x,mod)) % mod == qs[j] % mod
    assert len(seen) == T

    # Affine composition and multiplicity on A^2.
    line_mult = Counter()
    for a in A:
        assert a != 0
        for b in A:
            r = b*inv(a,mod) % mod
            slope = r*r % mod
            intercept = d*a*r*(1-r) % mod
            line_mult[(slope,intercept)] += 1
            # direct spot check at x=1 (always allowed, output may be any field point)
            x=1
            u=(d*a+a*a*inv(x,mod))%mod
            v=(d*b+b*b*inv(x,mod))%mod
            assert v == (slope*u+intercept)%mod
    identity=(1,0)
    assert line_mult[identity] == len(A)
    max_nonid=max(v for k,v in line_mult.items() if k != identity)
    assert max_nonid <= 2, (X,mod,d,max_nonid)

    ratio = len(A)/(T**(8/15))
    return {
        'X': X,
        'modulus': mod,
        'block_primes': len(qs),
        'value_set_size': len(A),
        'selected_gap': d,
        'selected_gap_count': T,
        'max_nonidentity_line_multiplicity': max_nonid,
        'value_over_T_8_15': ratio,
        'sqrt_modulus': mod**0.5,
        'value_over_sqrt_modulus': len(A)/(mod**0.5),
    }


def main():
    panels=[panel(X) for X in (100,250,500,1000,2500,5000)]
    out={
        'status':'FINITE_ALGEBRA_AND_COMBINATORICS_PASS',
        'panels':panels,
        'note':'Finite panels do not prove the asymptotic repeated-gap count or the incidence theorem.'
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
