#!/usr/bin/env python3
"""Exact small-prime checks for the direct von Mangoldt formulation.

Requires python-flint.  It verifies
    A_p = sum_{f in I_p} Lambda(f) = p * I_4 + p
and the local-unit character average for p=5,7.
"""
from collections import Counter
from itertools import product
import cmath
from flint import nmod_poly


def reverse_coeffs(f, degree, p):
    return [int(f[degree-k]) % p for k in range(1, degree+1)]


def log_vector(coeffs, N, p):
    u = [0] * (N + 1)
    for i, value in enumerate(coeffs, 1):
        if i <= N:
            u[i] = value % p
    out = [0] * (N + 1)
    power = [0] * (N + 1)
    power[0] = 1
    for j in range(1, N + 1):
        nxt = [0] * (N + 1)
        for a in range(N + 1):
            if power[a]:
                for b in range(1, N + 1 - a):
                    nxt[a+b] = (nxt[a+b] + power[a] * u[b]) % p
        power = nxt
        coefficient = (1 if j % 2 else -1) * pow(j, -1, p)
        for k in range(1, N + 1):
            out[k] = (out[k] + coefficient * power[k]) % p
    return tuple(out[1:])


def von_mangoldt(f):
    factors = f.factor()[1]
    if len(factors) == 1:
        prime, exponent = factors[0]
        return prime.degree()
    return 0


def run(p):
    N = p - 4
    histogram = Counter()
    A = 0
    irreducibles = 0
    for coefficients in product(range(p), repeat=p):
        f = nmod_poly(list(coefficients) + [1], p)
        value = von_mangoldt(f)
        vector = log_vector(reverse_coeffs(f, p, p), N, p)
        histogram[vector] += value
        if all(v == 0 for v in vector):
            A += value
            factors = f.factor()[1]
            irreducibles += int(len(factors) == 1 and factors[0][1] == 1)

    assert A == p * irreducibles + p

    total = 0j
    for lam in product(range(p), repeat=N):
        twisted = 0j
        for vector, weight in histogram.items():
            dot = sum(a*b for a, b in zip(lam, vector)) % p
            twisted += weight * cmath.exp(2j * cmath.pi * dot / p)
        total += twisted
    recovered = total / (p**N)
    assert abs(recovered - A) < 1e-7
    print(f"p={p}: A={A}, irreducibles={irreducibles}, character average PASS")


if __name__ == "__main__":
    for prime in (5, 7):
        run(prime)
    print("DIRECT LAMBDA CHECKS PASS")
