#!/usr/bin/env python3
"""Verify the corrected three-block Fourier identity.

Requires the `galois` package.  The script checks the original coefficient
formulas against the Fourier form for random vectors at p=5,7,11,13.
"""
import random
import galois


def direct_forms(a, p):
    n = p - 1
    q = 0
    c = 0
    for i in range(1, n):
        for j in range(1, n):
            if i + j == n:
                q -= a[i] * a[j]
            for k in range(1, n):
                if i + j + k in (n, 2*n, 2*n + 1):
                    c -= a[i] * a[j] * a[k]
    return q, c


def run(p, trials=100):
    n = p - 1
    extension_degree = 1
    while (p**extension_degree - 1) % (3*n):
        extension_degree += 1
    field = galois.GF(p**extension_degree)
    zeta = field.primitive_element ** ((p**extension_degree - 1) // (3*n))
    rho = zeta**n
    roots = [zeta**(3*j) for j in range(n)]
    inv_n = field(pow(n, -1, p))
    inv_3 = field(pow(3, -1, p))

    def evaluate(a, x):
        return sum((a[j] * x**j for j in range(n)), field(0))

    for _ in range(trials):
        a = [field(0)] + [field(random.randrange(p)) for _ in range(n-1)]
        q, c = direct_forms(a, p)

        q_fourier = -inv_n * sum((evaluate(a, s)**2 for s in roots), field(0))
        k0 = inv_n * sum((evaluate(a, s)**3 for s in roots), field(0))
        layer = field(0)
        for r in range(3):
            kr1 = inv_n * sum(
                (evaluate(a, zeta**r * s)**3 * s**-1 for s in roots),
                field(0),
            )
            dr = zeta**(-r) * kr1
            layer += rho**(-2*r) * dr
        layer *= inv_3
        c_fourier = -k0 - layer

        assert q == q_fourier
        assert c == c_fourier
    print(f"p={p}, extension degree={extension_degree}: PASS")


if __name__ == "__main__":
    for prime in (5, 7, 11, 13):
        run(prime)
    print("THREE-BLOCK FOURIER CHECKS PASS")
