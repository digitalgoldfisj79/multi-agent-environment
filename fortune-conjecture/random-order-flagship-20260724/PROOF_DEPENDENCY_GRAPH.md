# Proof dependency graph

```mermaid
graph TD
  A[Frame admissibility and PNT shell counts] --> J[Assembly]
  B[Bounded-coefficient rigidity] --> C[Pair-sum difference dichotomy]
  B --> D[Coefficient pattern nonvanishing]
  D --> E[Rank-cell decomposition]
  E --> F[Exact ordered set-partition identity]
  F --> G[Multivariate contour decay]
  H[Gauss/CRT inversion and coefficient norms] --> I[Slot character expansion]
  E --> I
  G --> L[Good-coordinate exponential decay]
  I --> M[Ratio-coordinate bijection]
  K[Sixth-moment orthogonality plus unique factorisation] --> N[Bad-character count beta]
  M --> O[Path matching lemma]
  H --> O
  L --> P[Pattern domination]
  N --> P
  O --> P
  P --> Q[Master per-configuration bound]
  C --> R[Configuration multiplicities]
  Q --> S[Complete ledger]
  R --> S
  S --> T[Per-modulus-pair bias proposition]
  T --> J
  J --> U[Fixed harmonic theorem]
  J --> V[Aggregate theorem]
  V --> W[Frobenius energy theorem]
```

## Minimal cut set

The proof fails if any of the following is removed:

1. exact rank-conditioning rather than an independent-cell approximation;
2. a bad-character count of order at most `X polylog X`;
3. the two-slot Cauchy–Schwarz supremum bound in the interior-micro class;
4. the sliding-family multiplicity count in the short-window `m=2` sector;
5. the endpoint-orphan treatment; or
6. frame nondegeneracy for diagonal and harmonic aggregation.

## Non-load-bearing results

- exact sixth-moment polynomial;
- empirical Monte Carlo order ensembles;
- the block-averaged conditional Hardy–Littlewood proposition;
- the finite check of the sub-Weibull tail;
- any claim about the increasing order or Fortune's conjecture.
