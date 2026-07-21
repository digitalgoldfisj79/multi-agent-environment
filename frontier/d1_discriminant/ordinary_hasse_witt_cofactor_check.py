#!/usr/bin/env python3
"""Exhaustive verifier for the ordinary Hasse--Witt cofactor indicator.

Requires python-flint. By default checks every a != 0, c, d for
p = 5, 7, 11, 13.
"""

from __future__ import annotations

from flint import nmod_mat, nmod_poly


def polynomial(p: int, a: int, c: int, d: int) -> nmod_poly:
    return nmod_poly([d, c, 0, a] + [0] * (p - 4) + [1], p)


def irreducible(f: nmod_poly, p: int) -> bool:
    factors = f.factor()[1]
    return (
        len(factors) == 1
        and factors[0][0].degree() == p
        and factors[0][1] == 1
    )


def selected_cofactor(p: int, a: int, c: int, d: int) -> int:
    f = polynomial(p, a, c, d)
    power = f ** (p - 1)

    # Delete row p and column 3 from I-H. The remaining rows are
    # u=1,...,p-1 and columns are 1,2,4,...,p.
    columns = [1, 2] + list(range(4, p + 1))
    rows: list[list[int]] = []
    for u in range(1, p):
        row: list[int] = []
        for v in columns:
            exponent = p * u - v
            h = (
                int(power[exponent])
                if 0 <= exponent <= power.degree()
                else 0
            )
            row.append((int(u == v) - h) % p)
        rows.append(row)

    return int(nmod_mat(rows, p).det()) % p


def verify(primes: tuple[int, ...] = (5, 7, 11, 13)) -> None:
    for p in primes:
        total = 0
        irreducible_total = 0
        for a in range(1, p):
            slice_count = 0
            for c in range(p):
                for d in range(p):
                    f = polynomial(p, a, c, d)
                    truth = int(irreducible(f, p))
                    value = selected_cofactor(p, a, c, d)
                    expected = 3 * a * truth % p
                    assert value == expected, (
                        p,
                        a,
                        c,
                        d,
                        value,
                        expected,
                        f.factor(),
                    )
                    slice_count += truth
                    total += 1
                    irreducible_total += truth
            print(f"PASS p={p}, a={a}: irreducibles={slice_count}")

        print(
            f"PASS p={p}: members={total}, "
            f"irreducibles={irreducible_total}"
        )

    print("ALL ORDINARY HASSE-WITT COFACTOR CHECKS PASSED")


if __name__ == "__main__":
    verify()
