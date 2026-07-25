#!/usr/bin/env python3
"""Exact verification that I_-(infinity)=0 at p=53 and p=71.

For prime degree p, a monic polynomial f over F_p is irreducible iff

    gcd(f, X^p-X)=1
    and
    X^(p^p)=X mod f.

The script checks every constant d in the boundary family

    X^p + a X^3 + d

for the stated nonsquare a.
"""

from __future__ import annotations


def add(a, b, p):
    length = max(len(a), len(b))
    output = [0] * length
    for index in range(length):
        output[index] = (
            (a[index] if index < len(a) else 0)
            + (b[index] if index < len(b) else 0)
        ) % p
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def subtract(a, b, p):
    return add(a, [(-value) % p for value in b], p)


def multiply_mod(a, b, modulus, p):
    output = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            output[i + j] = (output[i + j] + left * right) % p

    degree = len(modulus) - 1
    for index in range(len(output) - 1, degree - 1, -1):
        coefficient = output[index] % p
        if coefficient:
            for j in range(degree):
                output[index - degree + j] = (
                    output[index - degree + j] - coefficient * modulus[j]
                ) % p
    output = output[:degree]
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def power_mod(base, exponent, modulus, p):
    result = [1]
    while exponent:
        if exponent & 1:
            result = multiply_mod(result, base, modulus, p)
        base = multiply_mod(base, base, modulus, p)
        exponent >>= 1
    return result


def divide_with_remainder(a, b, p):
    a = a[:]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    inverse = pow(b[-1], -1, p)
    quotient = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and not (len(a) == 1 and a[0] == 0):
        degree = len(a) - len(b)
        coefficient = a[-1] * inverse % p
        quotient[degree] = coefficient
        for j in range(len(b)):
            a[degree + j] = (a[degree + j] - coefficient * b[j]) % p
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return quotient, a


def gcd_polynomial(a, b, p):
    while not (len(b) == 1 and b[0] == 0):
        _, remainder = divide_with_remainder(a, b, p)
        a, b = b, remainder
    inverse = pow(a[-1], -1, p)
    return [(value * inverse) % p for value in a]


def boundary_polynomial(p, cubic, constant):
    return [constant, 0, 0, cubic] + [0] * (p - 4) + [1]


def classify(polynomial, p):
    x = [0, 1]
    x_to_p = power_mod(x, p, polynomial, p)
    linear_gcd = gcd_polynomial(subtract(x_to_p, x, p), polynomial, p)
    if len(linear_gcd) > 1:
        return "linear"

    current = x
    for _ in range(p):
        current = power_mod(current, p, polynomial, p)
    if subtract(current, x, p) == [0]:
        return "irreducible"
    return "other"


def verify(p, nonsquare):
    counts = {"linear": 0, "other": 0, "irreducible": 0}
    irreducible_constants = []
    for constant in range(p):
        result = classify(boundary_polynomial(p, nonsquare, constant), p)
        counts[result] += 1
        if result == "irreducible":
            irreducible_constants.append(constant)

    assert not irreducible_constants
    expected = {
        53: {"linear": 35, "other": 18, "irreducible": 0},
        71: {"linear": 47, "other": 24, "irreducible": 0},
    }[p]
    assert counts == expected
    print(f"p={p}, a={nonsquare}: {counts}, I_-(infinity)=0: PASS")


def main():
    verify(53, 2)
    verify(71, 7)
    print("Q_INFINITY_NONSQUARE_COUNTEREXAMPLE_VERIFY: PASS")


if __name__ == "__main__":
    main()
