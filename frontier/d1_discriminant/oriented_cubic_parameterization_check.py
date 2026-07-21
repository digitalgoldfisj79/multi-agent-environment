#!/usr/bin/env python3
"""Independent checks for the universal oriented-cubic parameterization.

Standard-library only. The script verifies:
- existence of an irreducible base X^3+X+b;
- canonical orientation from X^p mod q0;
- the plane formulas for u,v,V;
- Frobenius-orbit invariance and exact orbit count;
- irreducibility of every represented depressed cubic;
- the interpolation polynomial for Frobenius;
- divisibility of the compatible translated cubic;
- transformed cubic-incidence counts against direct depressed-cubic enumeration.
"""

from __future__ import annotations


def inv(x: int, p: int) -> int:
    return pow(x % p, p - 2, p)


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def primes(n: int) -> list[int]:
    out = []
    for m in range(2, n + 1):
        if all(m % d for d in range(2, int(m**0.5) + 1)):
            out.append(m)
    return out


def mul_mod(a: list[int], b: list[int], modpoly: list[int], p: int) -> list[int]:
    n = len(modpoly) - 1
    tmp = [0] * (len(a) + len(b) - 1)
    for i, aa in enumerate(a):
        for j, bb in enumerate(b):
            tmp[i + j] = (tmp[i + j] + aa * bb) % p
    for k in range(len(tmp) - 1, n - 1, -1):
        q = tmp[k] % p
        if q:
            for i in range(n):
                tmp[k - n + i] = (tmp[k - n + i] - q * modpoly[i]) % p
    tmp = tmp[:n]
    return tmp + [0] * (n - len(tmp))


def xpow_mod(e: int, modpoly: list[int], p: int) -> list[int]:
    n = len(modpoly) - 1
    ans = [1] + [0] * (n - 1)
    x = [0, 1] + [0] * (n - 2)
    while e:
        if e & 1:
            ans = mul_mod(ans, x, modpoly, p)
        x = mul_mod(x, x, modpoly, p)
        e //= 2
    return ans


def roots_cubic(u: int, v: int, p: int) -> list[int]:
    return [x for x in range(p) if (x**3 + u * x + v) % p == 0]


def base_cubic(p: int) -> tuple[int, int]:
    for b in range(p):
        if not roots_cubic(1, b, p):
            rem = xpow_mod(p, [b, 1, 0, 1], p)
            a2 = rem[2]
            if a2:
                w = 3 * inv(a2, p) % p
                assert w * w % p == (-4 - 27 * b * b) % p
                return b, w
    raise AssertionError(f"no base cubic at p={p}")


def plane_forms(x: int, y: int, b: int, w0: int, p: int) -> tuple[int, int, int]:
    h = inv(2, p)
    q = (x * x - x * y + y * y) % p
    r = (x**3 + y**3 - 3 * h * x * y * (x + y)) % p
    s = x * y * (x - y) % p
    u = q
    v = (b * r + w0 * h * s) % p
    w = (w0 * r - 27 * b * h * s) % p
    return u, v, w


def canonical_orientation(u: int, v: int, p: int) -> int:
    rem = xpow_mod(p, [v, u, 0, 1], p)
    a2, a1, a0 = rem[2], rem[1], rem[0]
    if u and a2:
        return 3 * u * inv(a2, p) % p
    den = (2 * a1 + 1) % p
    if den:
        return -9 * v * inv(den, p) % p
    if a0:
        return 2 * u * u * inv(a0, p) % p
    raise AssertionError("orientation recovery failed")


def compatible_cd(u: int, v: int, w: int, a: int, p: int) -> tuple[int, int]:
    h = inv(2, p)
    iw = inv(w, p)
    ia = inv(a, p)
    c = (
        a * u
        + (w + 9 * v) * h * iw
        - 3 * u * u * ia * iw * iw
    ) % p
    d = (
        a * v
        - u * u * iw
        + 3 * u * h * ia * iw
        + 9 * u * v * h * ia * iw * iw
        - 2 * u**3 * ia * ia * iw**3
    ) % p
    return c, d


def translated_cubic(u: int, v: int, t: int, p: int) -> list[int]:
    return [
        (v - u * t - t**3) % p,
        (3 * t * t + u) % p,
        (-3 * t) % p,
        1,
    ]


def remainder_family(p: int, a: int, c: int, d: int, hpoly: list[int]) -> list[int]:
    rem = xpow_mod(p, hpoly, p)
    x3 = mul_mod([0, 0, 1], [0, 1, 0], hpoly, p)
    return [
        (rem[i] + a * x3[i] + (d if i == 0 else 0) + (c if i == 1 else 0)) % p
        for i in range(3)
    ]


def local_rootless(a: int, c: int, d: int, p: int) -> bool:
    return all((a * x**3 + (c + 1) * x + d) % p for x in range(p))


def disc_family_char(a: int, c: int, d: int, p: int) -> int:
    sp = 1 if p % 4 == 1 else -1
    if c % p == 0:
        value = sp * 3 * a * d * d
    else:
        eps = chi(-c * inv(3 * a, p), p)
        term = (eps + 2 * c * inv(3, p)) % p
        value = sp * (3 * a * d * d + c * term * term)
    return chi(value, p)


def transformed_incidence(p: int, a: int) -> tuple[int, int]:
    b, w0 = base_cubic(p)
    unsigned = 0
    signed = 0
    for x in range(p):
        for y in range(p):
            if x == 0 and y == 0:
                continue
            u, v, w = plane_forms(x, y, b, w0, p)
            c, d = compatible_cd(u, v, w, a, p)
            if local_rootless(a, c, d, p):
                unsigned += 1
                signed += disc_family_char(a, c, d, p)
    assert unsigned % 3 == 0 and signed % 3 == 0
    return unsigned // 3, signed // 3


def direct_incidence(p: int, a: int) -> tuple[int, int]:
    unsigned = 0
    signed = 0
    for u in range(p):
        for v in range(p):
            if roots_cubic(u, v, p):
                continue
            w = canonical_orientation(u, v, p)
            c, d = compatible_cd(u, v, w, a, p)
            if local_rootless(a, c, d, p):
                unsigned += 1
                signed += disc_family_char(a, c, d, p)
    return unsigned, signed


def run() -> None:
    for p in [q for q in primes(79) if q >= 5]:
        b, w0 = base_cubic(p)
        seen: dict[tuple[int, int, int], int] = {}
        for x in range(p):
            for y in range(p):
                if x == 0 and y == 0:
                    continue
                u, v, w = plane_forms(x, y, b, w0, p)
                assert w != 0
                assert (w * w + 4 * u**3 + 27 * v * v) % p == 0
                assert not roots_cubic(u, v, p)
                assert canonical_orientation(u, v, p) == w

                tx, ty = (-y) % p, (x - y) % p
                assert plane_forms(tx, ty, b, w0, p) == (u, v, w)
                seen[(u, v, w)] = seen.get((u, v, w), 0) + 1

                # Interpolation coefficients reproduce X^p mod the cubic.
                rem = xpow_mod(p, [v, u, 0, 1], p)
                interp = [
                    2 * u * u * inv(w, p) % p,
                    -(w + 9 * v) * inv(2 * w, p) % p,
                    3 * u * inv(w, p) % p,
                ]
                assert rem == interp

                for a in (1, next(z for z in range(2, p) if chi(z, p) < 0)):
                    t = -u * inv(a * w, p) % p
                    c, d = compatible_cd(u, v, w, a, p)
                    hpoly = translated_cubic(u, v, t, p)
                    assert remainder_family(p, a, c, d, hpoly) == [0, 0, 0]

        assert len(seen) == (p * p - 1) // 3
        assert set(seen.values()) == {3}

        if p <= 31:
            for a in (1, next(z for z in range(2, p) if chi(z, p) < 0)):
                assert transformed_incidence(p, a) == direct_incidence(p, a)

        print(f"p={p}: PASS; base b={b}, W0={w0}, orbits={len(seen)}")


if __name__ == "__main__":
    run()
