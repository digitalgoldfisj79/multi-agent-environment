# Paper IV proof-interior audit

## Verdict

`INTERNAL_AUDIT_PASS_HUMAN_SPECIALIST_REQUIRED`

No material discrepancy was found in the random-order reciprocal-frame theorem at the level accessible to this programme. This is not a human peer-review certificate and does not promote the manuscript to formal verification.

## Independently reproduced support

The committed clean-room scripts in `frontier/rqm_workbench/` were rerun against the frozen corpus. They reproduce:

- the exact ordered-partition/rank-conditioning law by direct enumeration at toy scale, with floating comparison errors at machine roundoff;
- the character expansion averaged over all 720 orderings in the `K=6` panel;
- Gauss-coefficient normalization checks;
- the exceptional-character sixth-moment orthogonality count;
- matching/configuration exponent arithmetic;
- the final binding cases at exactly `M (log X)^9`;
- failure of the deliberately over-optimistic old exponent ledger.

## Proof-interior checks

### P4.1 Coefficient patterns

The manuscript's coefficient cases are exhausted by multiplicities `m=2,3,4`; the corresponding multiplicity identity agrees with the exact enumeration.

### P4.2 Ordered-partition conditioning

The conditioning identity was checked against direct permutation averaging. The rank/order bookkeeping is exact in the finite panels.

### P4.3 Contour truncation

The multivariate contour decomposition was checked for sign and direction of every displayed loss. No unledgered logarithmic factor was found in the route to the final exponent.

### P4.4 Exceptional characters

The sixth-moment lemma reduces the congruence to integer equality because the relevant triple products are below the modulus product; unique factorisation then gives the stated `O(K^3)` multiplicity. The finite orthogonality check reproduces the formula exactly.

### P4.5 Path matching

The triangular-coordinate map and path-matching classification reproduce under exhaustive small-panel enumeration. No omitted configuration class was found.

### P4.6 Final ledger

The complete configuration ledger `T1-T3/C1-C4` was rechecked. The binding cases `C2a`, `C2b`, and `C2d` land at the stated ninth logarithmic power; there is no spare power available to absorb a missing factor.

## Risk statement

Paper IV remains intrinsically high-sensitivity because the theorem has logarithmic rather than power-saving slack. A specialist should therefore focus on:

1. whether every analytic estimate invoked in the contour/character treatment is uniform in exactly the manuscript's parameter range;
2. whether any convention change in primitive/imprimitive characters changes a multiplicity;
3. whether the all-bad domination step silently discards a logarithmic factor.

The assurance programme found no such defect.

## Novelty consequence

The sixth-moment/orthogonality machinery is standard support technology. The apparent novelty, if it survives specialist literature review, is the assembled theorem for reciprocal-frame averages along a uniformly random ordering of primorial factors and its path-matching architecture.
