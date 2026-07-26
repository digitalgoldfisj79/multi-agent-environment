#!/usr/bin/env python3
"""Regression for the generic Cartier/Krylov transfer-minimality theorem.

The theorem itself is algebraic over K=F_p(a,c,d).  This script checks its
two concrete signatures at irreducible square- and nonsquare-class
specializations for p=5,7,11:

  * h=aX^3+cX+d satisfies h^p+a h^3+c h-d=0 in F_p[X]/(F);
  * 1,h,...,h^(p-1) have full rank p.

Only a single witness per class is located; this is not a prime census.
"""
from __future__ import annotations

import json
from pathlib import Path


def trim(f: list[int], p: int) -> list[int]:
    f = [x % p for x in f]
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def add(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    return trim([
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(n)
    ], p)


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    return trim([
        (a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
        for i in range(n)
    ], p)


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out, p)


def divmod_poly(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    a = trim(a, p)
    b = trim(b, p)
    if b == [0]:
        raise ZeroDivisionError
    q = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], -1, p)
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        coeff = a[-1] * inv % p
        q[shift] = coeff
        for j, value in enumerate(b):
            a[shift + j] = (a[shift + j] - coeff * value) % p
        a = trim(a, p)
    return trim(q, p), a


def mod_poly(a: list[int], modulus: list[int], p: int) -> list[int]:
    return divmod_poly(a, modulus, p)[1]


def powmod_poly(a: list[int], exponent: int, modulus: list[int], p: int) -> list[int]:
    out = [1]
    a = mod_poly(a, modulus, p)
    while exponent:
        if exponent & 1:
            out = mod_poly(mul(out, a, p), modulus, p)
        a = mod_poly(mul(a, a, p), modulus, p)
        exponent //= 2
    return out


def gcd_poly(a: list[int], b: list[int], p: int) -> list[int]:
    while trim(b, p) != [0]:
        _, remainder = divmod_poly(a, b, p)
        a, b = b, remainder
    a = trim(a, p)
    inv = pow(a[-1], -1, p)
    return trim([inv * x for x in a], p)


def irreducible_prime_degree(f: list[int], p: int) -> bool:
    """Rabin criterion for degree p (p itself prime)."""
    x = [0, 1]
    xp = powmod_poly(x, p, f, p)
    if len(gcd_poly(sub(xp, x, p), f, p)) > 1:
        return False
    value = x
    for _ in range(p):
        value = powmod_poly(value, p, f, p)
    return sub(value, x, p) == [0]


def rank_mod(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(inv * x) % p for x in a[rank]]
        for row in range(rows):
            if row != rank and a[row][col]:
                factor = a[row][col]
                a[row] = [
                    (a[row][j] - factor * a[rank][j]) % p
                    for j in range(cols)
                ]
        rank += 1
    return rank


def smallest_nonsquare(p: int) -> int:
    squares = {x * x % p for x in range(1, p)}
    return next(x for x in range(2, p) if x not in squares)


def find_witness(p: int, a: int) -> tuple[int, int, list[int]]:
    for c in range(p):
        for d in range(p):
            f = [d, c, 0, a] + [0] * (p - 4) + [1]
            if irreducible_prime_degree(f, p):
                return c, d, f
    raise AssertionError((p, a, "no witness"))


def check(p: int, a: int) -> dict[str, int | bool]:
    c, d, f = find_witness(p, a)
    h = [d, c, 0, a]
    powers: list[list[int]] = []
    current = [1]
    for _ in range(p):
        powers.append(current + [0] * (p - len(current)))
        current = mod_poly(mul(current, h, p), f, p)

    hp = current
    h3 = powmod_poly(h, 3, f, p)
    relation = add(hp, [(a * x) % p for x in h3], p)
    relation = add(relation, [(c * x) % p for x in h], p)
    relation = add(relation, [(-d) % p], p)
    relation = mod_poly(relation, f, p)

    result = {
        "p": p,
        "a": a,
        "c": c,
        "d": d,
        "krylov_rank": rank_mod(powers, p),
        "relation_zero": relation == [0],
    }
    assert result["krylov_rank"] == p
    assert result["relation_zero"]
    return result


def main() -> None:
    results = []
    for p in (5, 7, 11):
        for a in (1, smallest_nonsquare(p)):
            results.append(check(p, a))
    output = {
        "classification": "structural regression; not a prime census",
        "cases": results,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "generic_cartier_transfer_minimality_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    for row in results:
        print(
            f"p={row['p']} a={row['a']} witness=(c={row['c']},d={row['d']}) "
            f"rank={row['krylov_rank']} relation={'PASS' if row['relation_zero'] else 'FAIL'}"
        )
    print("GENERIC_CARTIER_TRANSFER_MINIMALITY_VERIFY: PASS")


if __name__ == "__main__":
    main()
