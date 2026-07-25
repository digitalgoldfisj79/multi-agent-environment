#!/usr/bin/env python3
"""Exact base-field checks for the Hayes orientation tensor factorisation.

Cyclotomic integers are represented in Z[zeta_p] by coefficient vectors of
length p.  Equality is tested modulo 1+zeta+...+zeta^(p-1)=0.
"""

from __future__ import annotations


def chi(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def zero(p: int) -> list[int]:
    return [0] * p


def integer(value: int, p: int) -> list[int]:
    result = zero(p)
    result[0] = value
    return result


def canonical(vector: list[int]) -> tuple[int, ...]:
    tail = vector[-1]
    return tuple(value - tail for value in vector[:-1])


def add(left: list[int], right: list[int]) -> list[int]:
    return [a + b for a, b in zip(left, right)]


def subtract(left: list[int], right: list[int]) -> list[int]:
    return [a - b for a, b in zip(left, right)]


def scale(value: int, vector: list[int]) -> list[int]:
    return [value * x for x in vector]


def multiply(left: list[int], right: list[int]) -> list[int]:
    p = len(left)
    result = zero(p)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[(i + j) % p] += a * b
    return result


def equal(left: list[int], right: list[int]) -> bool:
    return canonical(subtract(left, right)) == (0,) * (len(left) - 1)


def exponential_sum(p: int, terms) -> list[int]:
    result = zero(p)
    for phase, weight in terms:
        result[phase % p] += weight
    return result


def J(p: int, t: int) -> list[int]:
    return scale(
        -1,
        exponential_sum(
            p,
            (((4 * r**3 + t * r) % p, 1) for r in range(p)),
        ),
    )


def K(p: int, t: int) -> list[int]:
    return exponential_sum(
        p,
        (
            ((-x**3 - t * x) % p, chi(x, p))
            for x in range(1, p)
        ),
    )


def S(p: int, u: int, y: int) -> list[int]:
    return exponential_sum(
        p,
        (
            (
                (x**3 + u * x - 3 * y * y * pow(x, -1, p)) % p,
                chi(x, p),
            )
            for x in range(1, p)
        ),
    )


def gauss(p: int) -> list[int]:
    return exponential_sum(p, (((x * x) % p, 1) for x in range(p)))


def verify_prime(p: int) -> None:
    G = gauss(p)
    chi3 = chi(3, p)

    # Symmetric-square / Kummer identity.
    for t in range(p):
        lhs = subtract(multiply(J(p, t), J(p, t)), integer(p, p))
        rhs = scale(-1, multiply(G, K(p, t)))
        assert equal(lhs, rhs), (p, "symmetric square", t)

    # Orientation tensor factorisation and diagonal correction.
    for u in range(p):
        for y in range(p):
            t_plus = (u + 6 * y) % p
            t_minus = (u - 6 * y) % p
            product_trace = multiply(J(p, t_plus), J(p, t_minus))
            salie_trace = scale(chi3, multiply(G, S(p, u, y)))
            if y:
                assert equal(product_trace, salie_trace), (
                    p,
                    "off diagonal",
                    u,
                    y,
                )
            else:
                assert equal(
                    product_trace,
                    add(integer(p, p), salie_trace),
                ), (p, "diagonal", u)

    print(f"p={p}: symmetric-square and orientation identities PASS")


def main() -> None:
    for p in (5, 11, 17):
        verify_prime(p)
    print("HAYES_ORIENTATION_FACTORIZATION_VERIFY: PASS")


if __name__ == "__main__":
    main()
