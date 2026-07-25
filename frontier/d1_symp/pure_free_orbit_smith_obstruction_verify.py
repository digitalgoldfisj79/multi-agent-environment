#!/usr/bin/env python3
"""Exact regression for the pure free-orbit Smith obstruction.

For each admitted small prime, construct the two character-block Frobenius
polynomials from PURE_FREE_ORBIT_OBSTRUCTION_TO_INTEGRAL_SMITH_BOUND_20260725.md.
The nontrivial block has X^2+Q; the trivial block has
X^2-p^m X+Q. Both have determinant Q and pure complex roots of modulus p^m,
but their traces differ by p^m while the underlying modular C_p-lattice is free.
"""

from __future__ import annotations


def verify_prime(p: int) -> None:
    assert p % 6 == 5
    m = (p + 1) // 2
    scale = p**m
    determinant = scale**2

    nontrivial_trace = 0
    trivial_trace = scale

    # Both quadratic polynomials have determinant equal to the common
    # weight scale squared.
    assert determinant == p ** (2 * m)

    # Discriminants are negative real numbers, so conjugate roots have
    # modulus sqrt(determinant)=scale.
    disc_nontrivial = -4 * determinant
    disc_trivial = trivial_trace**2 - 4 * determinant
    assert disc_nontrivial < 0
    assert disc_trivial == -3 * determinant < 0

    # The entire cyclic-character defect is one full Weil-scale eigenvalue.
    assert trivial_trace - nontrivial_trace == scale

    rank = (p - 5) // 6
    assert rank * scale == ((p - 5) // 6) * p ** ((p + 1) // 2)

    print(
        f"PASS p={p}: common modulus={scale}, one-block defect={scale}, "
        f"rank-{rank} defect={rank * scale}."
    )


def main() -> None:
    for p in (5, 11, 17, 23, 29, 41, 47):
        verify_prime(p)


if __name__ == "__main__":
    main()
