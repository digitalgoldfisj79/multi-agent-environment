# Independent and reproducibility checks — Paper I

## Exact source and archive

- Final manuscript SHA-256: `0e0f8a0d89209b8f4dd8c589526a89d57bd536f4889fdcd9c902a09b1a62f157`
- Zenodo archive SHA-256: `651b17c92371b73eae5f224fdea78f85c6ea82bb94da6514d2b482a6b441a166`
- Deposited anonymous source SHA-256: `12c990cd754d27a202ae956de74cb761514b3e65062b7710da3174932400aad1`

## Direct Zenodo rerun

Hugging Face CPU job `6a638a047ef3c0846496797f` downloaded the two files directly from the live Zenodo API, verified the published SHA-256, extracted the archive into a fresh container and ran:

```text
python scripts/verify_manifest.py
python scripts/run_all_checks.py --with-cpp
```

Result: `ALL REQUESTED CHECKS PASSED`.

The run included every shipped Python validator, the independent external-audit implementation and both C++ production drivers. It reproduced all recorded non-runtime columns.

## Exact independent panels

The independent audit implementation, written separately from the production validators, returned:

1. Proposition 2.1 fourth-moment identity — passed at `r=101`, residual `1.14e-13`, exact diagonal `325`;
2. Lemma 3.1 transport identity — all 784 exhaustive sorted-pair cases passed;
3. Proposition 3.6 second-factorial polynomial — exact for `M=3,...,9`;
4. Theorem 4.1 rank and Smith form — 40 families passed, including designed nonunit invariant `2`;
5. Corollary 4.2 finite-group occupancy — four exact rational panels passed;
6. pair-overlap identity — residual `1.42e-13`, and `sum N_k=P^2` exactly;
7. Theorem 5.2 template counts, transport constants and gap identity — all exact;
8. Proposition 5.4 median matrix, eigenvalues and full bilinear identity — residual `2.66e-15`;
9. Theorem 5.5 eight event weights, all 28 Smith pairs, finite-group means/variances, cross-median covariance and total variance — all passed;
10. Proposition 5.6 balance coefficients — exact generic/order-3/order-4/order-5 coefficients `(1,40,420,1736,2556)` and quadratic correction `(1,60,1350,13020,44730)`;
11. block packing identities — all tested panels exact; and
12. Proposition 10.3 multiplier asymptotic — ratios converge to one, with displayed test residuals below `3e-7`.

## Complete portable validator panels

The portable archive also reports and reruns:

- 5,516 referee-repair assertions;
- complete spectral checks through the required support sizes;
- 150 pair-overlap checks;
- 2,610 disjoint-median checks;
- 840 median-dispersion checks;
- 2,370 distinct-residue/atlas checks;
- 665 collision second-factorial checks; and
- 12 independent cold-review checks.

The C++ pair-overlap driver ran 87 modulus panels through `X=700`; the C++ median driver reproduced all recorded non-runtime columns.

## Previous cold review

The deposited external audit pre-registered twelve independent tests, hand-traced the asymptotic exponent arithmetic and found no substantive mathematical error. It identified seven packaging defects in an earlier archive. The deposited portable archive records those repairs:

- relative, non-self-referential manifest;
- all validator and C++ inputs included;
- complete order-3/order-4 spectral enumeration through `V=8`;
- regenerated and visually checked manuscript binaries;
- corrected published bibliographic metadata; and
- the previously orphaned referee-repair generator included.

## Scope

These checks validate the finite identities, enumerated constants, integral-rank computations, packaged reproducibility and numerical production panels. They do not prove the explicitly open HTE4, HWF4, FBHE4 or RQHE4 estimates, do not provide the signed prime-detection bridge, and do not prove Fortune's conjecture.

## Gate result

**Independent finite reconstruction and deposited-archive reproducibility: passed.**
