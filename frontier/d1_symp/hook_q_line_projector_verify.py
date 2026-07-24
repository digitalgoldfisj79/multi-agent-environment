#!/usr/bin/env python3
"""Check the exact q-line class-projector ledger at p=5,7,11."""

from normal_form_cell_verify import (
    chi,
    least_nonsquare,
    normalized_count,
    original_counts,
)


def class_representative(arithmetic_class, p):
    return 1 if arithmetic_class == 1 else least_nonsquare(p)


def cell_count(p, q, epsilon):
    arithmetic_class = epsilon * chi(q, p)
    a = class_representative(arithmetic_class, p)
    c = -3 * pow(q, -1, p) % p
    q_check, epsilon_check, count = normalized_count(p, a, c)
    assert q_check == q and epsilon_check == epsilon
    return count


def main():
    committed = {5: (4, 6), 7: (10, 8), 11: (14, 14)}

    for p in (5, 7, 11):
        eta = least_nonsquare(p)
        generic_q = [q for q in range(1, p) if q != 2]

        e_plus = {q: p * (1 - cell_count(p, q, 1)) for q in generic_q}
        e_minus = {q: p * (1 - cell_count(p, q, -1)) for q in generic_q}

        s0 = sum(e_plus[q] + e_minus[q] for q in generic_q)
        schi = sum(
            chi(q, p) * (e_plus[q] - e_minus[q]) for q in generic_q
        )

        recovered = []
        for a in (1, eta):
            arithmetic_class = chi(a, p)
            counts = original_counts(p, a)
            c_q2 = -3 * pow(2, -1, p) % p
            boundary = counts[0] + counts[c_q2]
            numerator = s0 + arithmetic_class * schi
            assert numerator % (2 * p) == 0
            value = (p - 2) + boundary - numerator // (2 * p)
            assert value == sum(counts.values())
            recovered.append(value)

        assert tuple(recovered) == committed[p]
        print(
            f"PASS p={p}: S0={s0}, Schi={schi}, "
            f"recovered N={tuple(recovered)}."
        )


if __name__ == "__main__":
    main()
