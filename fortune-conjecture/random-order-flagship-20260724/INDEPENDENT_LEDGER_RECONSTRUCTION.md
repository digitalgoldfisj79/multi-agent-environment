# Independent ledger reconstruction

## Purpose

This check was written after the rebuilt manuscript and does not call the committed audit code. It independently tests the two finite structural claims on which the no-cushion ledger depends:

1. the multiplicity of each rank/coefficient configuration is exactly `N` for the sliding type-S family and `1` otherwise; and
2. the disjoint `T1–T3`, `C1`, `C2a–C2d`, `C3`, `C4` assignment in the rebuilt manuscript has no holes or double assignments.

It is a finite structural reconstruction, not a proof of the asymptotic contour or character estimates.

## Enumeration method

For each `N=3,...,10`:

1. form all two-element multisets `u={i,j}` with `0<=i<=j<N`;
2. enumerate every ordered pair `(u,v)` with `u!=v`;
3. compute the net coefficient function `c(t)=mult_u(t)-mult_v(t)`;
4. reduce to the ordered nonzero ranks and coefficient vector;
5. group ordered pairs by that exact configuration;
6. verify multiplicity `N` precisely for vectors `(1,-1)` and `(-1,1)`, and multiplicity `1` for every other allowed vector;
7. compute the cell sizes from the ranks; and
8. classify the configuration by the rebuilt manuscript's disjoint rule, for micro thresholds `w0=1,2,3`.

## Results

All `24` panels (`N=3,...,10` and three thresholds each) passed:

- exact ordered-pair total `M(M-1)`;
- exact type-S/other multiplicity dichotomy;
- zero unclassified configurations;
- class totals equal the complete ordered-pair total; and
- no configuration assigned to more than one class under the disjoint rule.

The enumeration also reproduces

`M(M-1) = N^2(N-1) + N(N-1) + 6*C(N,3) + 6*C(N,4)`

for every tested `N`.

## Independent script

```python
from collections import Counter, defaultdict
from itertools import combinations_with_replacement


def coefficient_configuration(u, v):
    coefficients = Counter(u)
    coefficients.subtract(v)
    ranks = tuple(sorted(t for t, value in coefficients.items() if value))
    vector = tuple(coefficients[t] for t in ranks)
    return ranks, vector


def cell_sizes(N, ranks):
    K = N - 1
    ranks = list(ranks)
    return tuple(
        [ranks[0]]
        + [ranks[i + 1] - ranks[i] for i in range(len(ranks) - 1)]
        + [K - ranks[-1]]
    )


def is_type_s(vector):
    return len(vector) == 2 and set(vector) == {1, -1}


def classify(N, ranks, vector, w0):
    sizes = cell_sizes(N, ranks)
    m = len(vector)
    micro = [index for index, size in enumerate(sizes) if size < w0]

    if len(micro) >= 2:
        return "T1"

    if len(micro) == 1:
        index = micro[0]
        if m == 2:
            return "T2"
        if m == 3:
            return "T3"
        if m == 4:
            if 1 <= index <= 3:
                return "C2a"
            if index == 0:
                return "C2c" if sizes[0] == 0 else "C2b"
            if index == 4:
                return "C2d"

    if not micro:
        return {4: "C1", 3: "C3", 2: "C4"}[m]

    raise AssertionError((N, ranks, vector, sizes, w0))


for N in range(3, 11):
    pair_indices = list(combinations_with_replacement(range(N), 2))
    multiplicities = defaultdict(int)

    for u in pair_indices:
        for v in pair_indices:
            if u != v:
                multiplicities[coefficient_configuration(u, v)] += 1

    M = N * (N + 1) // 2
    assert sum(multiplicities.values()) == M * (M - 1)

    for (_, vector), multiplicity in multiplicities.items():
        expected = N if is_type_s(vector) else 1
        assert multiplicity == expected

    for w0 in (1, 2, 3):
        class_total = 0
        for (ranks, vector), multiplicity in multiplicities.items():
            assert classify(N, ranks, vector, w0) is not None
            class_total += multiplicity
        assert class_total == M * (M - 1)
```

## Exponent reconstruction

Using `N ~ X log^{-1} X`, `M ~ X^2 log^{-2} X`, `w0 ~ log X`, `beta ~ X log^3 X`, one independently obtains:

| Class | Count scale | Bias scale | Total scale |
|---|---:|---:|---:|
| `C1` | `X^4 log^{-4}` | `X^{-4} log^{12}` | `log^8` |
| `C2a` | `X^3 log^{-2}` | `X^{-1} log^9` | `X^2 log^7 = M log^9` |
| `C2b` | `X^3 log^{-2}` | `X^{-1} log^9` | `X^2 log^7 = M log^9` |
| `C2c` | `X^3 log^{-3}` | `X^{-3} log^9` | `log^6` |
| `C2d` | `X^3 log^{-2}` | `X^{-1} log^9` | `X^2 log^7 = M log^9` |
| `C3` | `X^3 log^{-3}` | `X^{-3} log^9` | `log^6` |
| `C4` | `X^3 log^{-3}` | `X^{-2} log^6` | `X log^3` |

This confirms that `C2a`, `C2b`, and `C2d` are exactly binding and that there is no positive power-of-`X` cushion.

## Conclusion

The rebuilt manuscript's ledger classification and multiplicities pass an independent finite reconstruction. This closes the specific audit requirement to reconstruct the `C2` configuration partition without relying on the original audit implementation. It does not close the fresh hostile-review or binary-package gates.
