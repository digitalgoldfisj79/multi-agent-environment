# Focused integer Fortune claim ledger

**Programme:** `FORTUNE_INT_ISC_FOCUSED_V0_1`  
**Execution status:** gates I0–I6 completed; I7 validation in progress  
**Terminal research target:** `INT-PSLT`

## Inherited proved spine

- candidate collapse below the next-prime square threshold;
- exact equivalence between a prime in the registered interval and a successful prime offset;
- exact shifted von Mangoldt decomposition `Psi_j=Y_j+R_j` with failure contamination `R_j=O(X log X)`;
- exact one-failure block criterion;
- exact identity `Z_j^2=Z_j+2 sum_d C_j(H;d)`;
- exact centred second-moment and four-prime covariance identities.

## New proved reductions and no-go results

### I1 — one-sided lower tail

Define

`lowerTailSq(Z,base) = max(0,base-Z)^2`.

The following are proved in Lean in
`FortuneFormal/Integer/LowerTailCriterion.lean`:

- the lower-tail square is pointwise bounded by the full squared error;
- the summed lower tail is bounded by the full variance;
- a lower-tail total below the squared baseline gap excludes every failed centre.

Therefore the full covariance target is stronger than necessary. Positive surpluses may be
discarded.

### I2 — first moment

A signed sparse first moment is not logically necessary after the I1 reduction. Existing
all-centre and almost-all short-interval theorems do not reach the selected primorial scale
`H=(log P_j)^2`.

### I3 — four-prime lane

Any direct absolute-value implementation has raw scale `N X^2` against target
`N X L(X)` and loses `X/L(X)`. A termwise displacement treatment requires average signed
error `L(X)/X`. The lane is closed absent a new aggregate lower-tail identity.

### I4 — shifted source reduction

Set

\[
B_X=X(\log X)^2
\]

up to an admissible fixed constant, and

\[
\mathcal D_{\Psi}^-(X)=\sum_{j<N}(B_X-\Psi_j(H))_+^2.
\]

The new terminal theorem is:

> **INT-PSLT — primorial selected lower-tail theorem.**
> \[
> \mathcal D_{\Psi}^-(X)=o(B_X^2).
> \]

At a failed centre, `Psi_j=O(X log X)=o(B_X)`, so one failure contributes
`(1+o(1))B_X^2`. Hence INT-PSLT implies eventual Fortune.

INT-PSLT is a lower-arity one-form theorem and asks for a threshold far below the expected
mass `H~X^2`. It is still a genuinely new one-defect-resolution theorem and is not proved.

### I5 — source/orbit geometry

For every `q|A_X`, the primorial walk satisfies `F_X(a/q)=N`. Smooth rational modes are
maximally coherent, so geometry alone cannot supply the required cancellation.

### I6 — adversarial models

Exact one-defect models preserve the block first moment and alter the raw second moment by
only relative `2/N=o(1)` while retaining one failure. Thus local densities, first moments,
relative second moments and dense-centre almost-all theorems are insufficient.

## Terminal open claim

`INT-PSLT` is open. No established theorem in the audited literature supplies its
selected-centre logarithmic-square lower tail.

## Explicitly not claimed

- `INT-PSLT`;
- `INT-LTQ` or `INT-ISC`;
- Fortune's conjecture;
- a uniform prime-number theorem in logarithmic-square intervals;
- Hardy–Littlewood asymptotics at individual primorial centres;
- a function-field-to-integer transfer;
- any contribution from Paper VII cubic incidence or direct `d=1`;
- that a finite experiment establishes an asymptotic theorem.

No open research claim is declared as a Lean axiom in this focused programme.
