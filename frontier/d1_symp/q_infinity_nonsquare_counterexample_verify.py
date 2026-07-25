#!/usr/bin/env python3
"""Exact complete finite-boundary census at p=53 and p=71.

For prime degree p, a monic polynomial f over F_p is irreducible iff

    gcd(f, X^p-X)=1
    and
    X^(p^p)=X mod f.

The script checks every constant in all four q-line boundary readings:

    I_+(infinity), I_-(infinity), I_+(2), I_-(2).
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


def sparse_polynomial(p, cubic, linear, constant):
    return [constant % p, linear % p, 0, cubic % p] + [0] * (p - 4) + [1]


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


def census(p, cubic, linear):
    counts = {"linear": 0, "other": 0, "irreducible": 0}
    constants = []
    for constant in range(p):
        result = classify(sparse_polynomial(p, cubic, linear, constant), p)
        counts[result] += 1
        if result == "irreducible":
            constants.append(constant)
    return counts, constants


def verify(p, nonsquare):
    # q=infinity, square and nonsquare readings.
    infinity_square, square_constants = census(p, 1, 0)
    infinity_nonsquare, nonsquare_constants = census(p, nonsquare, 0)

    inverse_two = pow(2, -1, p)
    q2_linear = -3 * inverse_two % p
    q2_square_cubic = inverse_two
    q2_nonsquare_cubic = pow(2 * nonsquare % p, -1, p)
    q2_square, q2_square_constants = census(p, q2_square_cubic, q2_linear)
    q2_nonsquare, q2_nonsquare_constants = census(
        p, q2_nonsquare_cubic, q2_linear
    )

    assert not square_constants
    assert not nonsquare_constants
    assert not q2_square_constants
    assert not q2_nonsquare_constants

    expected_nonsquare_infinity = {
        53: {"linear": 35, "other": 18, "irreducible": 0},
        71: {"linear": 47, "other": 24, "irreducible": 0},
    }[p]
    assert infinity_nonsquare == expected_nonsquare_infinity

    print(f"p={p}: I_+(infinity)=I_-(infinity)=I_+(2)=I_-(2)=0")
    print(f"  infinity square:    {infinity_square}")
    print(f"  infinity nonsquare: {infinity_nonsquare}")
    print(f"  q=2 square:         {q2_square}")
    print(f"  q=2 nonsquare:      {q2_nonsquare}")


def main():
    verify(53, 2)
    verify(71, 7)
    print("COMPLETE_BOUNDARY_COUNTEREXAMPLE_VERIFY: PASS")


if __name__ == "__main__":
    main()
