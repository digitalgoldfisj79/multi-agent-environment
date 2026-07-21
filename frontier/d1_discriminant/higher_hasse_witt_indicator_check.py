#!/usr/bin/env python3
"""Exhaustive checks for the higher Hasse--Witt indicator.

Standard library only. By default checks every a != 0, c, d at p=5,7.
The proved assertion is enforced on squarefree members with d != 0.
The same identity on singular members is reported as a diagnostic.
"""

from __future__ import annotations

from itertools import permutations


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add_poly(f: list[int], g: list[int], mod: int) -> list[int]:
    out = [0] * max(len(f), len(g))
    for i in range(len(out)):
        out[i] = ((f[i] if i < len(f) else 0)
                  + (g[i] if i < len(g) else 0)) % mod
    return trim(out)


def mul_poly(f: list[int], g: list[int], mod: int) -> list[int]:
    out = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        if x:
            for j, y in enumerate(g):
                if y:
                    out[i + j] = (out[i + j] + x * y) % mod
    return trim(out)


def pow_poly(base: list[int], exponent: int, mod: int) -> list[int]:
    out = [1]
    while exponent:
        if exponent & 1:
            out = mul_poly(out, base, mod)
        exponent >>= 1
        if exponent:
            base = mul_poly(base, base, mod)
    return out


def divmod_poly(
    dividend: list[int], divisor: list[int], p: int
) -> tuple[list[int], list[int]]:
    dividend = trim([x % p for x in dividend])
    divisor = trim([x % p for x in divisor])
    if divisor == [0]:
        raise ZeroDivisionError
    if len(dividend) < len(divisor):
        return [0], dividend

    quotient = [0] * (len(dividend) - len(divisor) + 1)
    inv = pow(divisor[-1], -1, p)
    while dividend != [0] and len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        coeff = dividend[-1] * inv % p
        quotient[shift] = coeff
        for j, value in enumerate(divisor):
            dividend[shift + j] = (
                dividend[shift + j] - coeff * value
            ) % p
        trim(dividend)
    return trim(quotient), trim(dividend)


def gcd_poly(f: list[int], g: list[int], p: int) -> list[int]:
    f = trim(f[:])
    g = trim(g[:])
    while g != [0]:
        _, r = divmod_poly(f, g, p)
        f, g = g, r
    inv = pow(f[-1], -1, p)
    return [(x * inv) % p for x in f]


def mul_mod_f(
    f: list[int], g: list[int], modulus: list[int], p: int
) -> list[int]:
    out = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i + j] = (out[i + j] + x * y) % p

    degree = len(modulus) - 1
    for k in range(len(out) - 1, degree - 1, -1):
        coeff = out[k] % p
        if coeff:
            for j in range(degree):
                out[k - degree + j] = (
                    out[k - degree + j] - coeff * modulus[j]
                ) % p
    out = out[:degree]
    out += [0] * (degree - len(out))
    return trim(out)


def pow_mod_f(
    base: list[int], exponent: int, modulus: list[int], p: int
) -> list[int]:
    out = [1]
    while exponent:
        if exponent & 1:
            out = mul_mod_f(out, base, modulus, p)
        exponent >>= 1
        if exponent:
            base = mul_mod_f(base, base, modulus, p)
    return trim(out)


def polynomial(p: int, a: int, c: int, d: int) -> list[int]:
    return [d % p, c % p, 0, a % p] + [0] * (p - 4) + [1]


def derivative(f: list[int], p: int) -> list[int]:
    return trim([(i * f[i]) % p for i in range(1, len(f))] or [0])


def squarefree(p: int, a: int, c: int, d: int) -> bool:
    f = polynomial(p, a, c, d)
    return len(gcd_poly(f, derivative(f, p), p)) == 1


def irreducible(p: int, a: int, c: int, d: int) -> bool:
    f = polynomial(p, a, c, d)
    x = [0, 1]

    # Prime degree p: Rabin criterion.
    xp = pow_mod_f(x, p, f, p)
    if len(gcd_poly(f, add_poly(xp, [0, -1], p), p)) != 1:
        return False

    xpp = pow_mod_f(x, p**p, f, p)
    return add_poly(xpp, [0, -1], p) == [0]


def beta_matrix(
    p: int, a: int, c: int, d: int, m: int
) -> list[list[int]]:
    mod = p * p
    f = polynomial(p, a, c, d)
    f = [x % mod for x in f]
    power = pow_poly(f, m - 1, mod)

    return [
        [
            power[m * u - v] if m * u - v < len(power) else 0
            for v in range(1, p)
        ]
        for u in range(1, p)
    ]


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions & 1 else 1


def determinant_mod(matrix: list[list[int]], mod: int) -> int:
    n = len(matrix)
    total = 0
    for perm in permutations(range(n)):
        term = permutation_sign(perm)
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total = (total + term) % mod
    return total


def indicator(p: int, a: int, c: int, d: int) -> tuple[int, int]:
    mod = p * p
    b1 = beta_matrix(p, a, c, d, p)
    b2 = beta_matrix(p, a, c, d, p * p)
    diff = [
        [(b1[i][j] - b2[i][j]) % mod for j in range(p - 1)]
        for i in range(p - 1)
    ]
    det = determinant_mod(diff, mod)
    assert det % p == 0, (p, a, c, d, det)
    return det, (det // p) % p


def verify() -> None:
    expected_irreducibles = {5: 20, 7: 54}

    for p in (5, 7):
        ordinary_checked = 0
        singular_checked = 0
        irreducible_count = 0

        for a in range(1, p):
            for c in range(p):
                for d in range(p):
                    det, value = indicator(p, a, c, d)
                    truth = int(irreducible(p, a, c, d))
                    is_squarefree = squarefree(p, a, c, d)

                    if is_squarefree and d != 0:
                        ordinary_checked += 1
                        assert value == truth, (
                            "ordinary mismatch", p, a, c, d,
                            det, value, truth,
                        )
                        assert det == p * truth, (
                            "mod-p^2 mismatch", p, a, c, d,
                            det, truth,
                        )
                    elif not is_squarefree:
                        singular_checked += 1
                        # Diagnostic strengthening, not used in HHW.1.
                        assert value == 0, (
                            "singular diagnostic mismatch",
                            p, a, c, d, det, value,
                        )

                    irreducible_count += truth

        assert irreducible_count == expected_irreducibles[p]
        print(
            f"PASS p={p}: ordinary={ordinary_checked}, "
            f"singular={singular_checked}, "
            f"irreducibles={irreducible_count}"
        )

    print("ALL HIGHER HASSE-WITT INDICATOR CHECKS PASSED")


if __name__ == "__main__":
    verify()
