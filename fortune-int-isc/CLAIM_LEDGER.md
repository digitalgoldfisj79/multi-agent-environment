# INT-ISC claim ledger

**Status:** programme built, not executed.

## Inherited proved spine

- candidate collapse below the next-prime square threshold;
- exact prime-pair detector and proper-prime-power contamination decomposition;
- exact one-failure block criterion;
- exact identity `Z_j^2 = Z_j + 2 sum_d C_j(H;d)`;
- exact centred second-moment and four-prime covariance identities, kernel checked in `FortuneFormal/Integer/BlockCriterion.lean`;
- deterministic size `lambda_j^* asymp X` for the displayed baseline expression.

## Open primary claim

`INT-ISC`: the centred signed residual on increasing primorial centres is `O(N X L(X))` for some `L(X)=o(log X)`.

## Claims to be decided before full covariance work

1. `INT-WST`: the frozen `INT-ISC` formulation is the weakest currently visible sufficient target, or there is a strictly weaker substitute with a formal implication to Fortune.
2. `INT-FM-NEC`: the necessary selected-centre first-moment consequence can be proved at the scale `N sqrt(X L(X))`, or reduced to one exact missing theorem.
3. `INT-SOURCE`: a centred double-von-Mangoldt source can be transferred to the detector variance without exceeding the loss budget.
4. `INT-PSD`: a deterministic operator/source-orbit theorem strictly smaller than `INT-ISC` exists.

## Explicitly not claimed

- `INT-ISC`;
- Fortune's conjecture;
- Hardy–Littlewood asymptotics at every individual primorial centre;
- a function-field-to-integer transfer;
- any contribution from Paper VII cubic incidence or direct `d=1`;
- that a finite experiment establishes an asymptotic theorem.

No open research claim may be declared as a Lean axiom in this programme.