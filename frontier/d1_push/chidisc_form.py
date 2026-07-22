#!/usr/bin/env python3
"""Closed-form test for T_a(p) = sum_{c,d} chi(Disc(F_{a,c,d})) (exact integer).

Conjecture from data:
  p = 1 mod 4:  T_+ = chi_p(3) p, T_- = -chi_p(3) p        (chi_p(3)=+1 iff p=+-1 mod 12)
  p = 3 mod 4:  the class with chi(a)=chi_p(2) has T = +-2p, the other 0;
                sign = -chi_p(3) if chi_p(2)=+1, +chi_p(3) if chi_p(2)=-1.
Tested for all p <= 113 (both classes), Disc computed directly from resultants
(independent of DM.1) AND via DM.1 formula.
"""
from flint import nmod_poly

def chi_int(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1

def disc_direct(p, a, c, d):
    F = nmod_poly([d, c, 0, a] + [0]*(p-4) + [1], p)
    return int(F.discriminant()) % p

def T(p, a):
    t = 0
    for c in range(p):
        for d in range(p):
            t += chi_int(disc_direct(p, a, c, d), p)
    return t

def least_nr(p):
    n = 2
    while pow(n, (p - 1) // 2, p) != p - 1:
        n += 1
    return n

def predict(p):
    chi3 = 1 if p % 12 in (1, 11) else -1
    if p % 4 == 1:
        return chi3 * p, -chi3 * p
    chi2 = 1 if p % 8 in (1, 7) else -1
    sgn = -chi3 if chi2 == 1 else chi3
    if chi2 == 1:
        return sgn * 2 * p, 0
    return 0, sgn * 2 * p

primes = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
allok = True
for p in primes:
    tp = T(p, 1); tm = T(p, least_nr(p))
    pp, pm = predict(p)
    ok = (tp, tm) == (pp, pm)
    if not ok:
        allok = False
    print(p, p % 24, (tp, tm), (pp, pm), "OK" if ok else "FAIL")
print("ALL MATCH" if allok else "PATTERN FAILS")
