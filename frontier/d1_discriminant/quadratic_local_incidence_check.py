#!/usr/bin/env python3
"""Independent checks for QUADRATIC_LOCAL_INCIDENCE.md.

Standard library only.

Checks for both square classes of a:
1. the compatible-coefficient formula;
2. the exact root-incidence identity;
3. the triple-root correction;
4. the polynomial P(D,S) substitution;
5. A_0 = p chi(-1), A_D = 1, A_S = 2;
6. C_a = (1 + chi(a)(p chi(-1) - K_p))/2;
7. L_(a,2) = (N_2 + C_a - T_a)/3.
"""

from __future__ import annotations

from math import isqrt


def primes_upto(limit: int) -> list[int]:
    return [
        p
        for p in range(2, limit + 1)
        if all(p % q for q in range(2, isqrt(p) + 1))
    ]


def chi(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(a for a in range(2, p) if chi(a, p) == -1)


def poly_p(d: int, s: int, p: int) -> int:
    return (
        d**3
        - 18 * d * d * s
        - 24 * d * d
        + 81 * d * s * s
        - 360 * d * s
        + 192 * d
        + 144 * s
        - 512
    ) % p


def cubic_disc(u: int, v: int, p: int) -> int:
    return (-4 * u**3 - 27 * v * v) % p


def compatible_coefficients(p: int, a: int, s: int, n: int) -> tuple[int, int]:
    c = (1 - a * (s * s - n)) % p
    d = (s * (a * n - 1)) % p
    return c, d


def local_cubic_uv(p: int, a: int, s: int, n: int) -> tuple[int, int]:
    inv_a = pow(a, -1, p)
    u = (n - s * s + 2 * inv_a) % p
    v = (s * (n - inv_a)) % p
    return u, v


def is_irreducible_quadratic(p: int, s: int, n: int) -> bool:
    return chi(s * s - 4 * n, p) == -1


def local_root_count(p: int, a: int, s: int, n: int) -> int:
    u, v = local_cubic_uv(p, a, s, n)
    return sum((x**3 + u * x + v) % p == 0 for x in range(p))


def local_irreducible(p: int, a: int, s: int, n: int) -> bool:
    return local_root_count(p, a, s, n) == 0


def triple_formula(p: int, a: int) -> int:
    return int(chi(2 * a, p) == -1) + 2 * int(
        chi(3 * a, p) == 1 and chi(-a, p) == -1
    )


def k_sum(p: int) -> int:
    return sum(
        chi(d * s * poly_p(d, s, p), p)
        for d in range(p)
        for s in range(p)
    )


def complete_auxiliary_sums(p: int) -> tuple[int, int, int, int]:
    a0 = a_s = a_d = a_ds = 0
    for d in range(1, p):
        for s in range(p):
            cp = chi(poly_p(d, s, p), p)
            a0 += cp
            a_s += chi(s, p) * cp
            a_d += chi(d, p) * cp
            a_ds += chi(d * s, p) * cp
    return a0, a_s, a_d, a_ds


def brute_components(p: int, a: int) -> tuple[int, int, int, int, int]:
    n2 = c_sum = root_sum = triple = local_count = 0
    for s in range(p):
        for n in range(p):
            if not is_irreducible_quadratic(p, s, n):
                continue
            n2 += 1
            c, d = compatible_coefficients(p, a, s, n)
            u, v = local_cubic_uv(p, a, s, n)

            # Verify the local polynomial identity at every field element.
            for x in range(p):
                h = (x * x - s * x + n) % p
                lhs = (a * x**3 + (c + 1) * x + d) % p
                rhs = (a * (x + s) * h + 2 * x - s) % p
                assert lhs == rhs

            disc_h = cubic_disc(u, v, p)
            c_sum += chi(disc_h, p)
            roots = local_root_count(p, a, s, n)
            root_sum += roots
            triple += int(u == 0 and v == 0)
            local_count += int(roots == 0)

            big_d = a * (s * s - 4 * n) % p
            big_s = a * s * s % p
            assert (16 * pow(a, 3, p) * disc_h - poly_p(big_d, big_s, p)) % p == 0

    return n2, c_sum, root_sum, triple, local_count


def verify(limit: int = 101) -> None:
    for p in primes_upto(limit):
        if p < 5:
            continue

        a0, a_s, a_d, a_ds = complete_auxiliary_sums(p)
        assert a0 == p * chi(-1, p), (p, "A0", a0)
        assert a_s == 2, (p, "AS", a_s)
        assert a_d == 1, (p, "AD", a_d)
        assert a_ds == k_sum(p), (p, "ADS", a_ds)

        for a in (1, least_nonsquare(p)):
            n2, c_sum, root_sum, triple, local_count = brute_components(p, a)
            assert n2 == p * (p - 1) // 2
            assert root_sum == n2
            assert triple == triple_formula(p, a)

            predicted_c = (
                1 + chi(a, p) * (p * chi(-1, p) - k_sum(p))
            ) // 2
            assert c_sum == predicted_c, (p, a, c_sum, predicted_c)

            predicted_local = (n2 + c_sum - triple) // 3
            assert local_count == predicted_local, (
                p,
                a,
                local_count,
                predicted_local,
            )

        print(f"PASS p={p}")

    print("ALL QUADRATIC LOCAL INCIDENCE CHECKS PASSED")


if __name__ == "__main__":
    verify()
