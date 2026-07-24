#!/usr/bin/env python3
"""Direct p=5, r=2 check of the three-cube-class bridge over F_25."""

from itertools import product

P = 5
ZERO = (0, 0)
ONE = (1, 0)
ELEMENTS = [(a, b) for a in range(P) for b in range(P)]


def add(x, y):
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def neg(x):
    return ((-x[0]) % P, (-x[1]) % P)


def mul(x, y):
    # F_25 = F_5[t]/(t^2-2)
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % P, (a * d + b * c) % P)


def power(x, exponent):
    result = ONE
    base = x
    while exponent:
        if exponent & 1:
            result = mul(result, base)
        base = mul(base, base)
        exponent >>= 1
    return result


def trace_to_f5(x):
    return add(x, power(x, 5))[0]


def generator():
    for candidate in ELEMENTS[1:]:
        if len({power(candidate, exponent) for exponent in range(24)}) == 24:
            return candidate
    raise AssertionError("no generator found")


def quadratic(coords):
    values = {index + 1: coords[index] for index in range(3)}
    total = ZERO
    for i in range(1, 4):
        for j in range(1, 4):
            if i + j == 4:
                total = add(total, mul(values[i], values[j]))
    return neg(total)


def cubic(coords):
    values = {index + 1: coords[index] for index in range(3)}
    total = ZERO
    targets = {4, 8, 9}
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                if i + j + k in targets:
                    total = add(total, mul(mul(values[i], values[j]), values[k]))
    return neg(total)


def rational_character_value(counts):
    assert counts[1] == counts[2] == counts[3] == counts[4], counts
    return counts[0] - counts[1]


def main():
    null_cone = []
    zero_fibre = 0
    for coords in product(ELEMENTS, repeat=3):
        if quadratic(coords) != ZERO:
            continue
        null_cone.append(coords)
        if cubic(coords) == ZERO:
            zero_fibre += 1

    assert len(null_cone) == 625
    assert zero_fibre == 25
    projective_count = (zero_fibre - 1) // 24
    assert projective_count == 1

    g = generator()
    representatives = [ONE, g, power(g, 2)]
    additive_sums = []
    for coefficient in representatives:
        counts = [0] * 5
        for coords in null_cone:
            phase = trace_to_f5(mul(coefficient, cubic(coords)))
            counts[phase] += 1
        additive_sums.append(rational_character_value(counts))

    assert additive_sums == [-50, 25, 25], additive_sums
    extension_sums = [25 * value for value in additive_sums]
    assert extension_sums == [-1250, 625, 625]
    assert sum(additive_sums) == 0
    assert sum(extension_sums) == 0

    print("PASS: F_25 null cone and cubic zero fibre enumerated exactly.")
    print("PASS: three cube-class sums are -50, 25, 25 with zero average.")
    print("PASS: #X_5(F_25)-#P^0(F_25)=0 matches the three-twist bridge.")


if __name__ == "__main__":
    main()
