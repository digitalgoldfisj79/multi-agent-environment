# O8 — falsification and finite-panel diagnostics

## Adversarial incidence matrices

For every proposed proof, identify the exact statistics it uses and construct a binary incidence matrix `I_jm` that matches those statistics while retaining one zero row whenever possible.

Required adversarial families include:

1. fixed factorial-moment matches inherited from the even/odd binomial construction;
2. matrices with the same row sum mean and variance but one zero row;
3. matrices with matched column degrees and pairwise column overlaps;
4. matrices with matched low-order connected cumulants;
5. matrices satisfying the same detector-weight budget but differing in zero-row status.

If the proposed inequality also proves the false panel has no zero row, the method is rejected.

## Exact small primorial panels

For registered finite values of `X`, compute exactly where feasible:

- `P_j`, `H`, and candidate prime offsets;
- row counts `Z_j`;
- the occupancy generating polynomial `sum_j s^(Z_j)`;
- its real and complex zeros;
- factorial moments and cumulants;
- uniform Bernoulli and exact hypergeometric detector values;
- column degrees and overlap graph;
- admissible pre-output weight profiles;
- connected tuple coefficients through the exact feasible order;
- the Type I/II surrogate scales from O7.

Large integer primality must use a deterministic or certified method at the tested range. Every panel records software version, seed where relevant, and exact input hashes.

## Method-selection rules

Finite panels may:

- expose algebraic mistakes;
- falsify proposed inequalities;
- estimate coefficient growth;
- identify whether connected cumulants appear substantially smaller than raw moments;
- choose between O4 and O7 for the expensive phase.

They may not:

- establish asymptotic positivity;
- justify an unproved Poisson model;
- promote a fitted decay law to a theorem;
- alter preregistered thresholds after results are observed.

## Decisive diagnostic

The programme proceeds to expensive connected-correlation work only if both conditions hold on the exact panels:

1. the connected norm is materially smaller than the raw factorial-moment norm after the primorial main term is removed;
2. an adversarial matrix matching the measured low-complexity statistics can still be distinguished by the proposed connected or dual certificate.

Failure of either condition triggers an explicit method obstruction rather than a larger blind computation.