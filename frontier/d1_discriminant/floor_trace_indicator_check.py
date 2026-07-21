#!/usr/bin/env python3
"""Exhaustive verification of the single-trace irreducibility indicator."""

from __future__ import annotations


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add_poly(f: list[int], g: list[int], p: int) -> list[int]:
    out = [0] * max(len(f), len(g))
    for i in range(len(out)):
        out[i] = (
            (f[i] if i < len(f) else 0)
            + (g[i] if i < len(g) else 0)
        ) % p
    return trim(out)


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


def mul_mod(
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


def pow_mod(
    base: list[int], exponent: int, modulus: list[int], p: int
) -> list[int]:
    out = [1]
    while exponent:
        if exponent & 1:
            out = mul_mod(out, base, modulus, p)
        exponent >>= 1
        if exponent:
            base = mul_mod(base, base, modulus, p)
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

    xp = pow_mod(x, p, f, p)
    if len(gcd_poly(f, add_poly(xp, [0, -1], p), p)) != 1:
        return False

    xpp = pow_mod(x, p**p, f, p)
    return add_poly(xpp, [0, -1], p) == [0]


def frobenius_matrix(
    p: int, a: int, c: int, d: int
) -> list[list[int]]:
    modulus = polynomial(p, a, c, d)
    g = [(-d) % p, (-c) % p, 0, (-a) % p]

    columns: list[list[int]] = []
    current = [1]
    for power in range(p):
        if power == 0:
            current = [1]
        elif power == 1:
            current = g[:]
        else:
            current = mul_mod(current, g, modulus, p)
        columns.append(current + [0] * (p - len(current)))

    return [
        [columns[column][row] % p for column in range(p)]
        for row in range(p)
    ]


def matmul(
    left: list[list[int]], right: list[list[int]], p: int
) -> list[list[int]]:
    rows = len(left)
    cols = len(right[0])
    inner = len(right)
    out = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for k in range(inner):
            value = left[i][k]
            if value:
                for j in range(cols):
                    out[i][j] = (
                        out[i][j] + value * right[k][j]
                    ) % p
    return out


def matrix_power(
    matrix: list[list[int]], exponent: int, p: int
) -> list[list[int]]:
    n = len(matrix)
    out = [[int(i == j) for j in range(n)] for i in range(n)]
    base = matrix
    while exponent:
        if exponent & 1:
            out = matmul(out, base, p)
        exponent >>= 1
        if exponent:
            base = matmul(base, base, p)
    return out


def floor_trace(p: int, a: int, c: int, d: int) -> int:
    phi = frobenius_matrix(p, a, c, d)
    n = len(phi)
    shifted = [
        [
            (phi[i][j] - int(i == j)) % p
            for j in range(n)
        ]
        for i in range(n)
    ]
    power = matrix_power(shifted, p - 1, p)
    return sum(power[i][i] for i in range(n)) % p


def verify() -> None:
    expected_counts = {5: 20, 7: 54}

    for p in (5, 7):
        count = 0
        zero_trace_squarefree = 0

        for a in range(1, p):
            for c in range(p):
                for d in range(p):
                    tau = floor_trace(p, a, c, d)
                    sq = int(squarefree(p, a, c, d))
                    indicator = sq * (1 - pow(tau, p - 1, p)) % p
                    truth = int(irreducible(p, a, c, d))

                    assert indicator == truth, (
                        p, a, c, d, tau, sq, indicator, truth
                    )

                    if sq and tau == 0:
                        zero_trace_squarefree += 1
                    count += truth

        assert count == expected_counts[p]
        assert zero_trace_squarefree == count
        print(
            f"PASS p={p}: irreducibles={count}, "
            f"squarefree_zero_trace={zero_trace_squarefree}"
        )

    print("ALL FLOOR-TRACE INDICATOR CHECKS PASSED")


if __name__ == "__main__":
    verify()
