#!/usr/bin/env python3
"""Independent reviewer checks for Paper II, written from the theorem statements."""
import cmath, math, random
from itertools import product
from sympy import symbols, binomial, simplify, expand, isprime, primitive_root

N = symbols('N', positive=True, integer=True)

# --- Theorem 4.2: combinatorial sum equals closed form ---
lhs = 36*binomial(N,4) + 16*N*binomial(N-1,2) + 9*binomial(N,2) + 4*N*(N-1) + N
rhs = N*(3*N**3 - 2*N**2 + 2*N - 1)/2
assert simplify(expand(lhs - rhs)) == 0
print("T4.2 multiset-sum == closed form: OK")

# --- Theorem 4.4: centred second moment identity ---
M = N*(N+1)/2
centred = rhs - M**2          # int |H2|^4 - M^2  (since int|H2|^2 = M)
claimed = N*(N-1)*(5*N**2 - N + 2)/4
assert simplify(expand(centred - claimed)) == 0
print("T4.2 centred formula == closed form: OK")
# leading constant: centred / M^2 -> 5
from sympy import limit, oo
assert limit(claimed/M**2, N, oo) == 5
print("centred mass ~ 5 M^2: OK")

# --- Proposition 5.1: partial alternating binomial ---
for s in range(1, 40):
    for k in range(0, 40):
        t = sum((-1)**j * math.comb(s, j) for j in range(0, min(k, s)+1))
        if s == 0: want = 1
        elif s <= k: want = 0
        else: want = (-1)**k * math.comb(s-1, k)
        assert t == want, (s, k, t, want)
print("P5.1 partial alternating binomial: OK")

# --- Theorem 7.2: local character-ratio identity, brute force over characters ---
def characters(q):
    g = primitive_root(q)
    # index table
    idx = {}
    x = 1
    for e in range(q-1):
        idx[x] = e
        x = x*g % q
    chars = []
    for a in range(q-1):
        w = cmath.exp(2j*cmath.pi*a/(q-1))
        chars.append({u: w**idx[u] for u in range(1, q)})
    return chars

def gauss(q, chibar):
    return sum(chibar[u]*cmath.exp(2j*cmath.pi*u/q) for u in range(1, q))

random.seed(7)
for q in (7, 11, 13):
    chars = characters(q)
    gsums = [gauss(q, {u: c[u].conjugate() for u in c}) for c in chars]
    for trial in range(30):
        a = random.randrange(1, q); x = random.randrange(1, q); y = random.randrange(1, q)
        for rho_i, rho in enumerate(chars):
            s = 0
            for chi_i, chi in enumerate(chars):
                # psi = chi * conj(rho): index arithmetic on exponents
                psi_i = (chi_i - rho_i) % (q-1)
                psi = chars[psi_i]
                s += gsums[chi_i] * gsums[psi_i].conjugate() * chi[a*x % q] * psi[a*y % q].conjugate()
            s /= (q-1)**2
            if x == y:
                want = 1.0 if rho_i == 0 else 0.0
            else:
                want = gsums[rho_i]/(q-1) * rho[(a*(x-y)) % q]
            assert abs(s - want) < 1e-8, (q, a, x, y, rho_i, s, want)
        # sum over rho reconstructs e_q(a(x-y))
        tot = 0
        for rho_i, rho in enumerate(chars):
            if x == y:
                pass
            s2 = gsums[rho_i]/(q-1) * rho[(a*(x-y)) % q] if x != y else (1.0 if rho_i == 0 else 0.0)
            tot += s2
        want2 = cmath.exp(2j*cmath.pi*(a*(x-y) % q)/q)
        if x != y:
            assert abs(tot - want2) < 1e-8, (q, a, x, y, tot, want2)
print("T7.2 character-ratio collapse + reconstruction: OK (q=7,11,13)")

# --- Theorem 7.1: character diagonal K_m for prime m, numeric ---
for q in (7, 11, 13):
    chars = characters(q)
    gsums = [gauss(q, {u: c[u].conjugate() for u in c}) for c in chars]
    # pick a set of "P_j" units mod q
    P = [1, 2, 3, 5, 6][:4]
    Pq = [p % q for p in P]
    for A in range(1, q):
        # full |F_q(A)|^2
        F = sum(cmath.exp(2j*cmath.pi*(A*p % q)/q) for p in Pq)
        # equal-character part
        D = 0
        for chi_i, chi in enumerate(chars):
            S = sum(chi[p] for p in Pq)
            D += abs(gsums[chi_i])**2 * abs(S)**2
        D /= (q-1)**2
        # K_q formula: sum_{i,j} (q*1[Pi=Pj mod q]-1)/(q-1)
        K = sum((q*(1 if (pi-pj) % q == 0 else 0)-1)/(q-1) for pi in Pq for pj in Pq)
        assert abs(D - K) < 1e-8, (q, A, D, K)
print("T7.1 character diagonal (prime modulus): OK")

# --- Prop 3.2 / dual-row identity: random-vector check (rewritten) ---
random.seed(11)
Nn = 7
P = []
x = 1
primes = [2,3,5,7,11,13,17]
for p in primes[:Nn]:
    x *= p
    P.append(x)
S = [P[i]+P[j] for i in range(Nn) for j in range(i, Nn)]
Mm = len(S)
Q = [q for q in range(97, 160) if isprime(q)][:5]
for a in (1, 2, 3):
    w = [random.random() for _ in Q]
    tot = sum(w); pw = [t/tot for t in w]
    # E_a directly
    def Psi(L):
        return sum(pw[i]*cmath.exp(2j*cmath.pi*a*L/Q[i]) for i in range(len(Q)))
    Ea = sum(abs(Psi(S[u]-S[v]))**2 for u in range(Mm) for v in range(Mm) if u != v)
    # via identity
    def H2(theta):
        return sum(cmath.exp(2j*cmath.pi*theta*s) for s in S)
    rhsv = 0
    for i in range(len(Q)):
        for j in range(len(Q)):
            th = a*(1.0/Q[i]-1.0/Q[j])
            rhsv += pw[i]*pw[j]*(abs(H2(th))**2 - Mm)
    kappa = sum(t*t for t in pw)
    diag = Mm*(Mm-1)*kappa
    Ra = rhsv - diag
    assert abs(Ea - rhsv) < 1e-6*abs(Ea), (a, Ea, rhsv)
    assert Ra >= -diag - 1e-6
print("P3.2 dual-row identity E_a = M(M-1)k2 + R_a: OK")

print("ALL INDEPENDENT CHECKS PASS")
