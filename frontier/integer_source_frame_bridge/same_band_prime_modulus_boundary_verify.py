#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def split_panel(primes: list[int]) -> dict:
    rows = []
    splits = (
        (
            "all_weight_on_centre",
            lambda p: Fraction(1, p - 2),
            lambda p: Fraction(1),
        ),
        (
            "all_weight_on_source",
            lambda p: Fraction(1),
            lambda p: Fraction(1, p - 2),
        ),
        (
            "rational_unbalanced",
            lambda p: Fraction(2, p - 2),
            lambda p: Fraction(1, 2),
        ),
    )
    number_of_moduli = len(primes)
    for label, centre_weight, source_weight in splits:
        centre_mass = Fraction(0)
        source_mass = Fraction(0)
        local_products = []
        for p in primes:
            a = centre_weight(p)
            b = source_weight(p)
            assert a * b == Fraction(1, p - 2)
            x = Fraction(p - 2) * a * a
            y = Fraction(p - 2) * b * b
            assert x * y == 1
            centre_mass += x
            source_mass += y
            local_products.append(str(x * y))
        product_mass = centre_mass * source_mass
        assert product_mass >= number_of_moduli**2
        rows.append(
            {
                "split": label,
                "centre_mass": str(centre_mass),
                "source_mass": str(source_mass),
                "product_mass": str(product_mass),
                "sharp_lower_bound": str(number_of_moduli**2),
                "local_products": local_products,
            }
        )

    return {
        "primes": primes,
        "number_of_moduli": number_of_moduli,
        "splits": rows,
        "status": "PASS",
    }


def first_band_geometry_panel() -> dict:
    rows = []
    for x, numerator, denominator in (
        (100, 3, 4),
        (1000, 4, 5),
        (10000, 9, 10),
    ):
        h = Fraction(numerator, denominator) * x * x
        assert x * x > h
        rows.append(
            {
                "X": x,
                "eta": f"{numerator}/{denominator}",
                "H": str(h),
                "sqrt_H_less_than_X": True,
            }
        )
    return {"rows": rows, "status": "PASS"}


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "scalar_source_centre_factorization_no_go": split_panel(
                [13, 17, 19]
            ),
            "physical_band_above_square_root": first_band_geometry_panel(),
        },
        "boundary": (
            "Every scalar split of the first-order coefficient 1/(p-2) has "
            "centre/source diagonal product at least the square of the number "
            "of physical prime moduli. Hence sequential source and centre "
            "Cauchy estimates necessarily reproduce the full modulus-count "
            "loss. The lower physical band also lies strictly above sqrt(H) "
            "because H=eta X^2 with eta<1."
        ),
    }
    output = Path(__file__).with_name(
        "same_band_prime_modulus_boundary_results.json"
    )
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
