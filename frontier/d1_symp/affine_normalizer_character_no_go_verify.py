#!/usr/bin/env python3
"""Checks for AFFINE_NORMALIZER_SECOND_COLLAPSE_NO_GO_20260725.md.

The irreducible (p-1)-dimensional affine representation is realized on the
nontrivial additive characters of F_p.  An affine element x -> a*x+b acts by

    e_c -> psi(c*b) e_(a^(-1)c).

Its trace is computed exactly as a sum of cyclotomic basis vectors.
"""

from __future__ import annotations


def canonical(vector):
    final = vector[-1]
    return tuple(value - final for value in vector[:-1]) + (0,)


def character_vector(p: int, multiplier: int, translation: int):
    output = [0] * p
    inverse = pow(multiplier, -1, p)
    for character in range(1, p):
        image = inverse * character % p
        if image == character:
            output[character * translation % p] += 1
    return canonical(tuple(output))


def integer_vector(value: int, p: int):
    return (value,) + (0,) * (p - 1)


def verify_prime(p: int):
    for multiplier in range(1, p):
        for translation in range(p):
            value = character_vector(p, multiplier, translation)
            if multiplier == 1 and translation == 0:
                expected = p - 1
            elif multiplier == 1:
                expected = -1
            else:
                expected = 0
            assert value == integer_vector(expected, p), (
                p, multiplier, translation, value, expected
            )
    print(f"p={p}: complete AGL_1 character table PASS")


def main():
    for p in (5, 11, 17, 23, 29, 41, 47, 53):
        verify_prime(p)
    print("AFFINE_NORMALIZER_CHARACTER_NO_GO_VERIFY: PASS")


if __name__ == "__main__":
    main()
