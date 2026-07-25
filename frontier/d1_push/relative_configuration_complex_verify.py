#!/usr/bin/env python3
"""
Independent verifier for the relative configuration-space obstruction.

Checks:
1. Hook characters V_i = wedge^i Std are irreducible and pairwise orthogonal.
2. sum_i (-1)^i V_i is the p-cycle detector.
3. The canonical oriented-subset face complex is the exact Koszul complex
   wedge^p Perm -> ... -> wedge^0 Perm.
4. The parabolic hook-rank ledger implied by the proved local monodromy has
   total virtual rank -(p-3), and middle virtual rank
   p-3-2*floor((p-1)/4).
No external dependencies.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def perm_wedge_character_polynomial(cycle_type):
    # det(1+t g | Perm) = product_{cycles c}(1-(-t)^len(c)).
    out = [1]
    for length in cycle_type:
        factor = [0] * (length + 1)
        factor[0] = 1
        factor[length] = -((-1) ** length)
        out = poly_mul(out, factor)
    return out


def divide_by_one_plus_t(poly):
    # Perm = 1 + Std, so lambda_t(Std)=lambda_t(Perm)/(1+t).
    q = [0] * (len(poly) - 1)
    q[0] = poly[0]
    for k in range(1, len(q)):
        q[k] = poly[k] - q[k - 1]
    reconstructed = [0] * len(poly)
    for k, value in enumerate(q):
        reconstructed[k] += value
        reconstructed[k + 1] += value
    assert reconstructed == poly
    return q


def hook_characters(cycle_type):
    return divide_by_one_plus_t(
        perm_wedge_character_polynomial(cycle_type)
    )


def z_lambda(cycle_type):
    counts = Counter(cycle_type)
    z = 1
    for length, multiplicity in counts.items():
        z *= (length ** multiplicity) * factorial(multiplicity)
    return z


def cycle_type_of_permutation(perm):
    seen = [False] * len(perm)
    lengths = []
    for start in range(len(perm)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = perm[current]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def square_multipliers(p):
    return sorted({(x * x) % p for x in range(1, p)})


def affine_inertia_cycle_types(p):
    # I_infty = {x -> ax+b : a square, b arbitrary}.
    types = Counter()
    for a in square_multipliers(p):
        for b in range(p):
            perm = [(a * x + b) % p for x in range(p)]
            types[cycle_type_of_permutation(perm)] += 1
    return types


def average_characters(character_table, group_cycle_types):
    order = sum(group_cycle_types.values())
    p = len(next(iter(character_table.values())))
    out = []
    for i in range(p):
        numerator = sum(
            multiplicity * character_table[cycle_type][i]
            for cycle_type, multiplicity in group_cycle_types.items()
        )
        out.append(Fraction(numerator, order))
    return out


def parabolic_hook_ranks(p):
    character_table = {
        cycle_type: hook_characters(cycle_type)
        for cycle_type in partitions(p)
    }
    identity = tuple([1] * p)
    dimensions = character_table[identity]

    transposition_group = {
        identity: 1,
        tuple([2] + [1] * (p - 2)): 1,
    }
    wild_group = {
        identity: 1,
        (p,): p - 1,
    }
    full_inertia = affine_inertia_cycle_types(p)

    inv_transposition = average_characters(
        character_table, transposition_group
    )
    inv_wild = average_characters(character_table, wild_group)
    inv_infinity = average_characters(character_table, full_inertia)

    # The proved end-piece theorem gives Sw(Std)=p-3.
    # Since Std has wild codimension p-1 and there is one wild break,
    # beta=(p-3)/(p-1).
    beta = Fraction(p - 3, p - 1)
    swan = [
        beta * (dimensions[i] - inv_wild[i])
        for i in range(p)
    ]

    ranks = []
    for i in range(p):
        global_invariants = 1 if i == 0 else 0
        rank = (
            2 * global_invariants
            + dimensions[i]
            + swan[i]
            - 2 * inv_transposition[i]
            - inv_infinity[i]
        )
        assert rank.denominator == 1
        assert rank >= 0
        ranks.append(int(rank))

    return ranks


def boundary_matrix(p, r):
    # d_r: wedge^r Perm -> wedge^(r-1) Perm, contraction by augmentation.
    source = list(combinations(range(p), r))
    target = list(combinations(range(p), r - 1))
    target_index = {basis: i for i, basis in enumerate(target)}
    matrix = [[Fraction(0) for _ in source] for _ in target]
    for j, subset in enumerate(source):
        for position, removed in enumerate(subset):
            face = subset[:position] + subset[position + 1 :]
            matrix[target_index[face]][j] += Fraction((-1) ** position)
    return matrix


def matrix_rank(matrix):
    if not matrix:
        return 0
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_value = a[rank][col]
        a[rank] = [x / pivot_value for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                factor = a[r][col]
                a[r] = [
                    a[r][c] - factor * a[rank][c]
                    for c in range(cols)
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def verify_koszul_exactness(p):
    # Include d_1: wedge^1 -> wedge^0 and d_p.
    ranks = {r: matrix_rank(boundary_matrix(p, r)) for r in range(1, p + 1)}
    homology = []
    for r in range(0, p + 1):
        dim = comb(p, r)
        outgoing_rank = ranks.get(r, 0)
        incoming_rank = ranks.get(r + 1, 0)
        h = dim - outgoing_rank - incoming_rank
        homology.append(h)
    assert homology == [0] * (p + 1)
    return ranks


def verify_prime(p):
    character_table = {
        cycle_type: hook_characters(cycle_type)
        for cycle_type in partitions(p)
    }

    # Detector.
    for cycle_type, chars in character_table.items():
        detector = sum(((-1) ** i) * chars[i] for i in range(p))
        expected = p if cycle_type == (p,) else 0
        assert detector == expected

    # Irreducibility and pairwise non-isomorphism of the hooks.
    for i in range(p):
        for j in range(p):
            inner = sum(
                Fraction(
                    character_table[cycle_type][i]
                    * character_table[cycle_type][j],
                    z_lambda(cycle_type),
                )
                for cycle_type in character_table
            )
            assert inner == (1 if i == j else 0)

    # wedge^r Perm = V_r + V_(r-1).
    for cycle_type, chars in character_table.items():
        perm_chars = perm_wedge_character_polynomial(cycle_type)
        for r in range(p + 1):
            rhs = (chars[r] if r < p else 0) + (
                chars[r - 1] if r > 0 else 0
            )
            assert perm_chars[r] == rhs

    ranks = parabolic_hook_ranks(p)
    total_virtual = sum(((-1) ** i) * ranks[i] for i in range(p))
    middle_virtual = sum(
        ((-1) ** i) * ranks[i] for i in range(3, p - 2)
    )
    expected_middle = p - 3 - 2 * ((p - 1) // 4)

    assert total_virtual == -(p - 3)
    assert middle_virtual == expected_middle
    assert ranks[1] == 0
    assert ranks[p - 1] == 0
    assert ranks[2] == 2 * ((p - 1) // 4)
    assert ranks[p - 2] == 2 * p - 6

    return ranks, total_virtual, middle_virtual


def main():
    for p in (5, 7):
        koszul_ranks = verify_koszul_exactness(p)
        print(f"p={p}: canonical face complex exact; differential ranks={koszul_ranks}")

    for p in (5, 7, 11, 13, 17):
        ranks, total_virtual, middle_virtual = verify_prime(p)
        minimum_generic_hook_homology = 2 ** (p - 1)
        print(
            f"p={p}: hook H1 ranks={ranks}; "
            f"total virtual={total_virtual}; "
            f"middle virtual={middle_virtual}; "
            f"generic hook-complex lower bound={minimum_generic_hook_homology}"
        )

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
