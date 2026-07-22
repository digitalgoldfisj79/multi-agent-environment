#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from math import comb
from pathlib import Path


def primes_upto(n: int) -> list[int]:
    out = []
    for x in range(2, n + 1):
        if all(x % d for d in range(2, int(x**0.5) + 1)):
            out.append(x)
    return out


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def audit(p: int, a: int) -> dict:
    q2 = Counter()
    linear = Counter()
    domain = 0

    for t in range(p):
        for n in range(p):
            if chi(t * t - 4 * n, p) != -1:
                continue
            domain += 1
            c = (1 - a * (t * t - n)) % p
            d = (t * (a * n - 1)) % p
            q2[(c, d)] += 1

    inv_a = pow(a, -1, p)
    for c in range(p):
        for d in range(p):
            linear[(c, d)] = sum(
                (x + a * x**3 + c * x + d) % p == 0 for x in range(p)
            )
            dual = sum(
                (a * t**3 + (c - 2) * t - d) % p == 0
                and chi(-3 * t * t - 4 * (c - 1) * inv_a, p) == -1
                for t in range(p)
            )
            assert dual == q2[(c, d)]

    first = sum(q2.values())
    second = sum(comb(v, 2) for v in q2.values())
    third = sum(comb(v, 3) for v in q2.values())
    mixed = sum(linear[key] * q2[key] for key in q2)
    size_r = (p - chi(a, p)) // 2
    distribution = Counter(q2[(c, d)] for c in range(p) for d in range(p))

    predicted = {
        3: third,
        2: second - 3 * third,
        1: first - 2 * second + 3 * third,
        0: p * p - first + second - third,
    }

    assert domain == p * (p - 1) // 2
    assert first == domain
    assert second == comb(size_r, 2)
    assert mixed == domain
    assert dict(distribution) == {
        k: predicted[k] for k in sorted(predicted) if predicted[k]
    }

    return {
        "a": a,
        "square_class": chi(a, p),
        "quadratic_factor_incidence": first,
        "mixed_linear_quadratic_incidence": mixed,
        "second_factorial_moment": second,
        "third_factorial_moment": third,
        "R_size": size_r,
        "multiplicity_distribution": {
            str(k): distribution[k] for k in sorted(distribution)
        },
    }


def main() -> None:
    rows = []
    for p in [x for x in primes_upto(101) if x >= 5]:
        nonsquare = next(a for a in range(2, p) if chi(a, p) == -1)
        rows.append({"prime": p, "classes": [audit(p, 1), audit(p, nonsquare)]})

    result = {
        "status": "PASS",
        "statement": (
            "For every audited prime and both square classes, irreducible "
            "quadratic factors are parametrized by trace and norm; total "
            "incidence is p(p-1)/2, the second factorial moment is "
            "binom((p-chi(a))/2,2), and the mixed linear-quadratic incidence "
            "is again p(p-1)/2."
        ),
        "range": "all primes 5<=p<=101",
        "rows": rows,
    }

    output = Path(__file__).with_name("quadratic_factor_mass_audit_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "prime_count": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
