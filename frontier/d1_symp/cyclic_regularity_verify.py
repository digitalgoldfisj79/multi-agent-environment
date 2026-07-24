#!/usr/bin/env python3
from itertools import product


def primes(limit):
    for n in range(5, limit + 1, 2):
        if all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            yield n


def canonical_class(vector, p):
    candidates = []
    for constant in range(p):
        translated = [(x + constant) % p for x in vector]
        for scalar in range(1, p):
            candidates.append(tuple((scalar * x) % p for x in translated))
    return min(candidates)


def x5_points():
    p = 5
    points = set()
    for vector in product(range(p), repeat=p):
        if sum(vector) % p != 0:
            continue
        if len(set(vector)) == 1:
            continue
        if sum(x * x for x in vector) % p != 0:
            continue
        if sum(x * x * x for x in vector) % p != 0:
            continue
        points.add(canonical_class(vector, p))
    return points


def shift(vector, power):
    n = len(vector)
    power %= n
    return vector[-power:] + vector[:-power] if power else vector


def verify_p5():
    points = x5_points()
    assert len(points) == 6, points
    for power in range(1, 5):
        fixed = {
            point for point in points
            if canonical_class(shift(point, power), 5) == point
        }
        assert len(fixed) == 1, (power, fixed)
        assert len(fixed) - 1 == 0


def verify_regular_characters():
    checked = []
    for p in primes(199):
        if p % 3 != 2:
            continue
        numerator = 2 ** (p - 1) - 1
        assert numerator % (3 * p) == 0, p
        multiplicity = numerator // (3 * p)
        rank = numerator // 3
        assert p * multiplicity == rank
        character = [p * multiplicity] + [0] * (p - 1)
        assert character[0] == rank
        assert all(value == 0 for value in character[1:])
        checked.append(p)
    print(f"PASS: regular-character arithmetic through p={checked[-1]}.")


def main():
    verify_p5()
    print("PASS: direct p=5 projective fixed-point check.")
    verify_regular_characters()


if __name__ == "__main__":
    main()
