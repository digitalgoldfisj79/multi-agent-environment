#!/usr/bin/env python3
"""Checks of exact small-p closed forms and the grading constraint.

(1) p=5: S_a(5) = 2 a^3 for all a != 0   (equivalently 3aN_a = 2a^3).
(2) p=7: S_a(7) = 6a + 3a^4 for all a != 0.
(3) p=11, p=13: fit S_a(p) as the unique polynomial a*(A + B*chi(a));
    verify A = 3(N_+ + N_-)/2, B = 3(N_+ - N_-)/2 mod p against counts.
(4) Grading sanity: entry monomials a^i c^j d^k of H_{u,v} satisfy
    (p-3)i + (p-1)j + pk = p(p-1) - pu + v  (checked numerically p=5..13).
"""
from math import factorial
from flint import nmod_poly

def irr(f, p):
    lead, facs = f.factor()
    return len(facs) == 1 and facs[0][1] == 1 and facs[0][0].degree() == p

def Na(p, a):
    n = 0
    for c in range(p):
        for d in range(1, (p + 1) // 2):
            if irr(nmod_poly([d, c, 0, a] + [0]*(p-4) + [1], p), p):
                n += 2
    return n

def chi(a, p):
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

# (1),(2)
ok = True
for a in range(1, 5):
    lhs = (3 * a * Na(5, a)) % 5
    rhs = (2 * a**3) % 5
    if lhs != rhs:
        ok = False; print("p=5 FAIL", a, lhs, rhs)
print("p=5: S_a = 2a^3 for all a:", ok)
ok = True
for a in range(1, 7):
    lhs = (3 * a * Na(7, a)) % 7
    rhs = (6 * a + 3 * a**4) % 7
    if lhs != rhs:
        ok = False; print("p=7 FAIL", a, lhs, rhs)
print("p=7: S_a = 6a + 3a^4 for all a:", ok)

# (3)
for p in (11, 13):
    Nplus = Na(p, 1)
    nr = 2
    while chi(nr, p) == 1:
        nr += 1
    Nminus = Na(p, nr)
    inv2 = pow(2, p - 2, p)
    A = 3 * (Nplus + Nminus) * inv2 % p
    B = 3 * (Nplus - Nminus) * inv2 % p
    allok = True
    for a in range(1, p):
        lhs = (3 * a * Na(p, a)) % p
        rhs = a * (A + B * chi(a, p)) % p
        if lhs != rhs:
            allok = False; print(p, a, lhs, rhs)
    print(f"p={p}: S_a = a(A + B chi(a)) with A={A}, B={B}: {allok}")

# (4) grading on entry formula
def entry_terms(p, u, v):
    out = []
    for w in range(1, min(4, u) + 1):
        n = p - 1 - u + w
        target = p * w - v
        for i in range(0, min(n, target // 3) + 1):
            j = target - 3 * i
            if j < 0:
                break
            k = n - i - j
            if k < 0:
                continue
            coef = factorial(n) // (factorial(i) * factorial(j) * factorial(k))
            if coef % p:
                out.append((i, j, k))
    return out

gradeok = True
for p in (5, 7, 11, 13):
    for u in range(1, p + 1):
        for v in range(1, p + 1):
            want = p * (p - 1) - p * u + v
            for (i, j, k) in entry_terms(p, u, v):
                if (p - 3) * i + (p - 1) * j + p * k != want:
                    gradeok = False
                    print("GRADE FAIL", p, u, v, i, j, k)
print("grading (p-3)i+(p-1)j+pk = p(p-1)-pu+v on all entry monomials:", gradeok)
