# Formalisation plan

The analytic M5 theorem depends on classical Barban–Davenport–Halberstam and prime-number-theorem inputs and is recorded in the theorem ledger rather than reimplemented in Lean.

The exact logical bridge is formalized in

`FortuneFormal/Integer/SelectedCentreMeanCriterion.lean`.

Kernel-checked statements:

- `selectedCentreMean_lowerBound_of_band_and_tail`;
- `selectedCentreMean_of_normalized_parityTail`.

They certify that the proved divisor-band lower bound plus `INT-SCPT` yields the required positive selected-centre mean. No analytic premise is silently promoted, and no new axiom is introduced.