#!/usr/bin/env python3
"""Exact arithmetic checks for the Sawin packaging audit.

For n=q=p and interval dimension h, Proposition 4.2 has exponent

    (h + floor(p/p) - floor((p-h)/p) + 1) / 2 = (h+2)/2

for 1 <= h < p.

For h=4 and centre T^p-T, the von Mangoldt sum is exactly

    sum Lambda = p * I_4 + p,

because the only degree-p prime powers other than irreducibles are
(T-a)^p = T^p-a, one for each a in F_p, each of weight 1.

Consequently B_Lambda <= p-1 in

    |sum Lambda - p^4| <= B_Lambda p^3

forces I_4 > p-1.
"""

from __future__ import annotations

from fractions import Fraction


def exponent_twice(p: int, h: int) -> int:
    """Twice Sawin's Frobenius exponent for n=q=p, m=p-h."""
    assert 1 <= h < p
    n = p
    m = p - h
    return n - m + n // p - m // p + 1


def required_b_scale_exponent(h: int) -> Fraction:
    """Power beta such that B < p^beta makes error smaller than main."""
    # main p^h; error B*p^((h+2)/2)
    return Fraction(h, 1) - Fraction(h + 2, 2)


def h4_lower_sum(p: int, b: int) -> int:
    """Sawin lower bound for sum Lambda in the h=4 package."""
    return p**4 - b * p**3


def crown_from_weighted_sum(p: int, weighted_sum: int) -> bool:
    """Recover I_4 using sum Lambda = p I_4 + p and test I_4>p-1."""
    assert (weighted_sum - p) % p == 0
    i4 = (weighted_sum - p) // p
    return i4 > p - 1


def main() -> None:
    for p in (5, 7, 11, 17, 23, 29, 53, 71, 101):
        for h in (2, 3, 4):
            assert h < p
            assert exponent_twice(p, h) == h + 2

        assert required_b_scale_exponent(2) == 0
        assert required_b_scale_exponent(3) == Fraction(1, 2)
        assert required_b_scale_exponent(4) == 1

        # The exact real-valued condition is B < p - 1/p.
        exact_cutoff = Fraction(p**2 - 1, p)
        assert p - 1 < exact_cutoff < p

        # Since B is integral, B <= p-1 suffices.
        lower = h4_lower_sum(p, p - 1)
        assert lower == p**3
        assert lower > p**2
        assert crown_from_weighted_sum(p, lower)

        # B=p is not certified by this triangle bound.
        assert h4_lower_sum(p, p) == 0

    print("PASS: Sawin exponent is (h+2)/2 for h=2,3,4.")
    print("PASS: required B scales are 1, sqrt(p), p respectively.")
    print("PASS: aggregate h=4 bound B_Lambda <= p-1 certifies I_4 > p-1.")
    print("SAWIN_PACKAGING_THRESHOLD_VERIFY: PASS")


if __name__ == "__main__":
    main()
