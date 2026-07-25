#!/usr/bin/env python3
"""Exact regression for the Fourier/q-line boundary calibration.

Uses the existing pure-Python irreducibility implementation in
normal_form_cell_verify.py. This is a structural check at the already
calibrated primes p=11,17,23,29, not a new prime sweep.
"""

from fractions import Fraction

from normal_form_cell_verify import (
    chi,
    irreducible_prime_degree,
    least_nonsquare,
    polynomial,
)


DATA = {
    11: {"N": (14, 14), "T": 322102, "expected": (0, 6, -44, -66, Fraction(22))},
    17: {"N": (18, 14), "T": 11899821517, "expected": (0, 4, 34, -136, Fraction(29))},
    23: {"N": (12, 22), "T": -1010446643080743, "expected": (0, 6, 322, 92, Fraction(-561, 23))},
    29: {"N": (36, 28), "T": -798145148362709627351, "expected": (0, 2, -232, -290, Fraction(-65419, 841))},
}


def count_constant_slice(p: int, cubic: int, linear: int) -> int:
    return sum(
        irreducible_prime_degree(polynomial(p, cubic % p, linear % p, d), p)
        for d in range(p)
    )


def boundaries(p: int, arithmetic_class: int) -> tuple[int, int]:
    a = 1 if arithmetic_class == 1 else least_nonsquare(p)
    infinity_count = count_constant_slice(p, a, 0)
    c_q2 = -3 * pow(2, -1, p) % p
    q2_count = count_constant_slice(p, a, c_q2)
    return infinity_count, q2_count


def main() -> None:
    for p, data in DATA.items():
        plus_inf, plus_q2 = boundaries(p, 1)
        minus_inf, minus_q2 = boundaries(p, -1)

        b_plus = plus_inf + plus_q2
        b_minus = minus_inf + minus_q2
        n_plus, n_minus = data["N"]

        # S0 + Schi and S0 - Schi from the exact class ledger.
        plus_projector = 2 * p * ((p - 2) + b_plus - n_plus)
        minus_projector = 2 * p * ((p - 2) + b_minus - n_minus)
        assert (plus_projector + minus_projector) % 2 == 0
        assert (plus_projector - minus_projector) % 2 == 0
        s0 = (plus_projector + minus_projector) // 2
        schi = (plus_projector - minus_projector) // 2

        normalized_airy = Fraction(data["T"], p ** ((p - 3) // 2))
        actual = (b_plus, b_minus, s0, schi, normalized_airy)
        assert actual == data["expected"], (p, actual, data["expected"])

        # Uniform discriminant theorem on the square-class infinity boundary.
        assert plus_inf == 0
        if chi(2, p) == 1:
            assert plus_q2 == 0

        print(
            f"PASS p={p}: boundaries (+)=({plus_inf},{plus_q2}), "
            f"(-)=({minus_inf},{minus_q2}); S0={s0}, Schi={schi}, "
            f"normalized Airy={normalized_airy}."
        )


if __name__ == "__main__":
    main()
