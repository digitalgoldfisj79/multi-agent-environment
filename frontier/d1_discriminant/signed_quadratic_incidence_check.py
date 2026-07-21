#!/usr/bin/env python3
"""Verify the exact signed quadratic-incidence decomposition.

Standard-library only. For each configured prime and both square classes of a:
1. enumerate irreducible quadratics h_(s,n);
2. compute the compatible sparse polynomial and the signed locally admissible
   quadratic incidence directly;
3. recompute T0, TDelta, R, and Ttriple using the transformed formulas from
   SIGNED_QUADRATIC_INCIDENCE.md.
"""

from math import isqrt


def primes_upto(limit):
    out = []
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            out.append(n)
    return out


def chi(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def inv(x, p):
    return pow(x % p, -1, p)


def disc_f_char(p, a, c, d):
    sign = 1 if p % 4 == 1 else -1
    eps_c = chi(-c * inv(3 * a, p), p)
    value = 3 * a * d * d + c * (eps_c + 2 * c * inv(3, p)) ** 2
    return chi(sign * value, p)


def local_roots(p, a, c, d):
    return sum(
        1 for x in range(p)
        if (a * x**3 + (c + 1) * x + d) % p == 0
    )


def local_disc_char(p, a, c, d):
    u = (c + 1) * inv(a, p) % p
    v = d * inv(a, p) % p
    return chi(-4 * u**3 - 27 * v**2, p)


def ds_polynomials(D, S, p):
    up = (
        D**3 - 18 * D**2 * S - 24 * D**2
        + 81 * D * S**2 - 360 * D * S + 180 * D
        + 108 * S - 400
    ) % p
    um = (
        D**3 - 18 * D**2 * S
        + 81 * D * S**2 - 216 * D * S - 12 * D
        + 216 * S**2 - 468 * S - 16
    ) % p
    q = (
        D**3 - 18 * D**2 * S - 24 * D**2
        + 81 * D * S**2 - 360 * D * S + 192 * D
        + 144 * S - 512
    ) % p
    ell = (D + 3 * S - 4) % p
    return up, um, q, ell


def root_polynomials(w, t, p):
    ell = (t**2 + t * w - 3 * t + w**2 - 3 * w) % p
    a1 = (t * w - t - w) % p
    a2 = (
        t**3 * w - 3 * t**3
        + 2 * t**2 * w**2 - 15 * t**2 * w + 25 * t**2
        + t * w**3 - 9 * t * w**2 + 20 * t * w
        - w**3 + 4 * w**2
    ) % p
    b = (
        8 * t**5 + 3 * t**4 * w**2 + 4 * t**4 * w - 39 * t**4
        + 6 * t**3 * w**3 - 30 * t**3 * w**2
        + 33 * t**3 * w - 3 * t**3
        + 3 * t**2 * w**4 - 20 * t**2 * w**3
        + 36 * t**2 * w**2 + 9 * t**2 * w
        + 2 * t * w**4 - 6 * t * w**3
        + 3 * w**4 - 12 * w**3
    ) % p
    return ell, a1, a2, b


def direct_terms(p, a):
    t0 = tdelta = root = triple = signed = 0
    for s in range(p):
        for n in range(p):
            if chi(s * s - 4 * n, p) != -1:
                continue
            c = (1 - a * (s * s - n)) % p
            d = s * (a * n - 1) % p
            df = disc_f_char(p, a, c, d)
            r = local_roots(p, a, c, d)
            dh = local_disc_char(p, a, c, d)
            u = (c + 1) * inv(a, p) % p
            v = d * inv(a, p) % p
            delta = int(u == 0 and v == 0)
            t0 += df
            tdelta += df * dh
            root += df * r
            triple += df * delta
            if r == 0:
                signed += df
    assert 3 * signed == 2 * t0 + tdelta - root - triple
    return t0, tdelta, root, triple, signed


def transformed_terms(p, a):
    eps = chi(a, p)
    gamma = chi(3 * a, p)

    raw0 = raw_delta = 0
    for D in range(1, p):
        for S in range(p):
            weight = (1 - eps * chi(D, p)) * (1 + eps * chi(S, p))
            up, um, q, ell = ds_polynomials(D, S, p)
            amp = (
                chi(up, p) + chi(um, p)
                + gamma * chi(ell, p) * (chi(up, p) - chi(um, p))
            )
            raw0 += weight * amp
            raw_delta += weight * amp * chi(q, p)
    assert raw0 % 4 == 0 and (eps * raw_delta) % 4 == 0
    t0 = raw0 // 4
    tdelta = eps * raw_delta // 4

    raw_root = 0
    chi3 = chi(3, p)
    for w in range(p):
        W = w * (w - 4) % p
        if W == 0:
            continue
        for t in range(1, p):
            weight = (1 + eps * chi(t, p)) * (1 - chi(W, p))
            if weight == 0:
                continue
            ell, a1, a2, b = root_polynomials(w, t, p)
            amp = (
                (1 + chi(ell, p)) * chi(a1 * a2, p)
                + chi3 * (1 - chi(ell, p)) * chi(b, p)
            )
            raw_root += weight * amp
    assert (eps * raw_root) % 4 == 0
    root = eps * raw_root // 4

    for n in range(p):
        if chi(-4 * n, p) == -1:
            root += disc_f_char(p, a, 1 + a * n, 0)

    triple_count = (
        int(chi(2 * a, p) == -1)
        + 2 * int(chi(3 * a, p) == 1 and chi(-a, p) == -1)
    )
    triple = triple_count * disc_f_char(p, a, -1, 0)

    numerator = 2 * t0 + tdelta - root - triple
    assert numerator % 3 == 0
    return t0, tdelta, root, triple, numerator // 3


def main():
    checked = 0
    for p in primes_upto(61):
        if p < 5:
            continue
        nonsquare = next(a for a in range(2, p) if chi(a, p) == -1)
        for a in (1, nonsquare):
            direct = direct_terms(p, a)
            transformed = transformed_terms(p, a)
            assert direct == transformed, (p, a, direct, transformed)
            checked += 1
            print(
                f"p={p:2d} class={chi(a,p):+d} "
                f"T0={direct[0]:4d} Td={direct[1]:4d} "
                f"R={direct[2]:4d} T={direct[3]:2d} "
                f"Lchi={direct[4]:4d}"
            )
    print(f"SIGNED QUADRATIC DECOMPOSITION VERIFIED: {checked} slice classes")


if __name__ == "__main__":
    main()
