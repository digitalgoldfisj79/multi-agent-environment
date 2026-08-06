# Claim ledger — integrated Fortune formal programme

**Updated:** 6 August 2026  
**Lean:** 4.32.0  
**Compliance state:** papers I–VII and the conditional synthesis mapped to explicit evidence classes  
**Formal boundary:** ONE PAPER VII AXIOM REMAINS

## Evidence classes

- `KERNEL_CHECKED`: proved in compiled Lean without `sorry`, `admit` or hidden assumptions;
- `DERIVED_WITH_LEDGERED_AXIOM`: Lean implication from the single named external certificate boundary;
- `EXACT_COMPUTATIONAL`: exact finite verification, not a uniform theorem;
- `MANUSCRIPT_PROVED_NOT_YET_FORMALIZED`: written proof retained but not represented end-to-end in Lean;
- `OPEN_OR_CONDITIONAL`: excluded from the proved corpus.

## Kernel-checked paper spine

| Lean declaration or module | Paper/programme claim |
|---|---|
| `FortuneFormal.Bilateral.p7_ifa1_concrete` | Paper VII inverse-free endpoint equivalence |
| `FortuneFormal.Bilateral.p7_bdd1_concrete` | Paper VII common-defect theorem at corrected prime-Frobenius scope |
| `FortuneFormal.Bilateral.p7_bdd2_concrete` | Paper VII zero-defect classification at odd-prime scope |
| `FortuneFormal.Bilateral.p7_strip_concrete` | Paper VII intermediate-strip emptiness |
| `FortuneFormal.Quadratic.certifiedComponent_not_arithmeticOpen` | quadratic discriminant contradiction on the certified component |
| `FortuneFormal.Integer.no_failure_of_variance_below_baseline_gap` | corrected Papers II–III one-failure criterion |
| `FortuneFormal.Integer.centered_second_moment_identity` | exact centred variance identity |
| `FortuneFormal.Integer.four_prime_covariance_identity` | exact four-prime covariance residual identity |
| `FortuneFormal.Integer.AdaptiveOccupancyCriterion` | deterministic occupancy implications used by the conditional detector |
| `FortuneFormal.Integer.SquarefreeCompositeEnergyCriterion` | fixed-order squarefree collision and energy implications |
| `FortuneFormal.Integer.LocalConnectedTreeObstruction` | exact order-three local tree obstruction and exponent gap |
| `FortuneFormal.Integer.RuhlSelectedTupleResidualCriterion` | absolute first-order allowance, signed one-sided implication, exact residual split and weighted polynomial identity |

The formal modules include additional supporting lemmas; this table lists the publication-facing load-bearing interfaces.

## ASSUMED pending formalization

Exactly one permitted external boundary remains:

`FortuneFormal.p7_k2_certified_normalization`.

It states that a genuine quadratic incidence produces an arithmetic-open q-free point on the externally certified component. The derived theorem `p7_k2_empty_from_external_certificate` is therefore not axiom-free. No other manuscript theorem is imported as an axiom.

Papers I, IV, V and VI remain selectively formalized or unformalized at theorem level. Their authoritative manuscripts and exact regressions are retained, but they must not be described as wholly kernel checked.

## Exact-computational evidence

- corrected Papers II–III source and covariance regressions;
- replacement Papers V–VI reconstruction suites;
- Paper VII polynomial and finite-field certificates;
- beta=5 RUHL truncation certificate under `epsilon=0.10`, `U/L<=1.10`;
- fixed-order squarefree collision panels;
- connected-local exact rational panels through order eight;
- finite Heath--Brown identity and source-scale tables.

These computations do not prove the corresponding uniform analytic frontiers.

## Open analytic frontiers

- `INT-ISC` / jointly signed selected-centre covariance and tuple control;
- `INT-SCME`, `INT-LCSK` and full source-attached `INT-PWOC` where separately invoked;
- `D1-QLINE-NONSAT` and the universal function-field crown;
- `P7-CUBIC-TF`;
- any function-field-to-integer transfer;
- Fortune's conjecture.

## Review corrections incorporated

- the exact RUHL arithmetic split is `E=A+S`; an appended correction after both differences is double counting;
- the signed first-order RUHL condition is one-sided, although the independent absolute envelope is two-sided;
- Heath--Brown coefficient mass proves an exponentially weighted residual requirement, not universal failure of every termwise implementation;
- LCSK Python regressions now genuinely exercise connected local coefficients through order eight; Lean remains explicitly scoped to the order-three obstruction;
- the finite RUHL margin search is diagnostic and cannot invalidate a passing asymptotic exponent certificate.

## Explicitly not claimed

The programme does not claim full formalization of all seven manuscripts, an axiom-free Paper VII quadratic theorem, any open analytic frontier, a transfer theorem, Fortune's conjecture, peer review or publication acceptance.
