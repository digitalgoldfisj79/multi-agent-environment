#!/usr/bin/env python3
"""Closed-form hunt for r_+/-(p) = N_+/-(p) mod p (centered).

Battery:
 (1) elliptic curves y^2 = x^3 + Ax + B, A,B in [-8,8]: a_p mod p vs
     targets across all 30 primes (skip p | disc).
 (2) truncated hypergeometric sums sum_{k<=(p-1)/2} binom(2k,k)^m t^k
     and full-range versions, m=1,2,3, fixed rational t.
 (3) sum_{c,d} chi(Disc) via DM.1 formula (direct), correlate.
Targets: r_+, r_-, -r_+, -r_-, 1-r_+, 1-r_-, r_+ + r_-, r_- - r_+,
         A_p mod p, B_p mod p (A_p=p+1-(N_++N_-)/2, B_p=(N_--N_+)/2).
A candidate "hit" = matches one target for ALL primes tested.
"""
import json
from math import comb

data = json.load(open("scan_results.json"))
primes = sorted(int(p) for p in data)

Np = {p: data[str(p)]["+"]["N"] for p in primes}
Nm = {p: data[str(p)]["-"]["N"] for p in primes}

def targets(p):
    rp = Np[p] % p; rm = Nm[p] % p
    A = (p + 1 - (Np[p] + Nm[p]) // 2) % p
    B = ((Nm[p] - Np[p]) // 2) % p
    return {
        "r+": rp, "r-": rm, "-r+": (-rp) % p, "-r-": (-rm) % p,
        "1-r+": (1 - rp) % p, "1-r-": (1 - rm) % p,
        "r++r-": (rp + rm) % p, "r--r+": (rm - rp) % p,
        "A_p": A, "-A_p": (-A) % p, "B_p": B, "-B_p": (-B) % p,
    }

T = {p: targets(p) for p in primes}
tkeys = list(T[primes[0]].keys())

def test_candidate(name, valfun, min_ok=None):
    """valfun(p) -> value mod p or None (skip prime). Hit = all non-skipped match."""
    best = []
    for tk in tkeys:
        ok = 0; tot = 0
        for p in primes:
            v = valfun(p)
            if v is None:
                continue
            tot += 1
            if v % p == T[p][tk]:
                ok += 1
        if tot >= 25 and ok == tot:
            best.append((tk, ok, tot))
        elif tot >= 25 and ok >= tot - 1:
            best.append((tk + " (all-but-one)", ok, tot))
    if best:
        print(f"HIT {name}: {best}")
    return best

# ---------- (1) elliptic curves ----------
def ap_curve(A, B, p):
    disc = -16 * (4 * A**3 + 27 * B**2)
    if disc % p == 0:
        return None
    # a_p = p + 1 - #E(F_p);  #E = p + 1 + sum_x chi(x^3+Ax+B)
    s = 0
    for x in range(p):
        v = (x * x * x + A * x + B) % p
        if v == 0:
            continue
        s += 1 if pow(v, (p - 1) // 2, p) == 1 else -1
    return (-s) % p   # a_p = -sum chi

hits = 0
for A in range(-8, 9):
    for B in range(-8, 9):
        if (4 * A**3 + 27 * B**2) == 0:
            continue
        h = test_candidate(f"E: y^2=x^3+{A}x+{B}", lambda p, A=A, B=B: ap_curve(A, B, p))
        hits += len(h)
print(f"elliptic battery done, hits={hits}")

# ---------- (2) truncated hypergeometric ----------
def trunc_sum(p, m, tnum, tden, full=False):
    if tden % p == 0:
        return None
    t = tnum * pow(tden, p - 2, p) % p
    lim = p - 1 if full else (p - 1) // 2
    s = 0
    tk = 1
    b = 1  # binom(2k,k) mod p incrementally
    for k in range(lim + 1):
        s = (s + pow(b, m, p) * tk) % p
        tk = tk * t % p
        # binom(2k+2,k+1) = binom(2k,k) * 2(2k+1)/(k+1)
        b = b * 2 * (2 * k + 1) % p * pow(k + 1, p - 2, p) % p
    return s

ts = [(1,1),(-1,1),(2,1),(-2,1),(3,1),(-3,1),(1,2),(-1,2),(1,4),(-1,4),
      (1,8),(-1,8),(1,16),(-1,16),(1,64),(-1,64),(1,256),(-1,256),
      (1,3),(-1,3),(1,9),(-1,9),(1,27),(-1,27),(2,27),(-2,27),(4,27),(-4,27),(1,12),(-1,12)]
hh = 0
for m in (1, 2, 3):
    for (tn, td) in ts:
        for full in (False, True):
            h = test_candidate(f"hyp m={m} t={tn}/{td} full={full}",
                               lambda p, m=m, tn=tn, td=td, full=full: trunc_sum(p, m, tn, td, full))
            hh += len(h)
print(f"hypergeometric battery done, hits={hh}")

# ---------- (3) chi(Disc) double sum ----------
def chi_disc_sum(p, a):
    # DM.1: Disc = s_p (3 a d^2 + c (eps_c + 2c/3)^2) for c!=0; s_p*3ad^2 for c=0
    def chi(x):
        x %= p
        if x == 0:
            return 0
        return 1 if pow(x, (p - 1) // 2, p) == 1 else -1
    sp = (-1) ** ((p - 1) // 2)
    inv3 = pow(3, p - 2, p)
    tot = 0
    for c in range(p):
        if c == 0:
            base = 0
            for d in range(p):
                tot += chi(sp * 3 * a * d * d)
            continue
        eps = chi(-c * pow(3 * a, p - 2, p) % p)
        u = (eps + 2 * c * inv3) % p
        for d in range(p):
            tot += chi(sp * (3 * a * d * d + c * u * u))
    return tot

print("chi(Disc) sums (exact integers), a=1 then least NR:")
def least_nr(p):
    n = 2
    while pow(n, (p - 1) // 2, p) != p - 1:
        n += 1
    return n
rows = []
for p in primes[:16]:
    s1 = chi_disc_sum(p, 1)
    s2 = chi_disc_sum(p, least_nr(p))
    rows.append((p, s1, s2))
    print(p, s1, s2)
h = test_candidate("chiDisc a=1", lambda p, R={r[0]: r[1] for r in rows}: R.get(p))
h2 = test_candidate("chiDisc a=nr", lambda p, R={r[0]: r[2] for r in rows}: R.get(p))
print("done")
