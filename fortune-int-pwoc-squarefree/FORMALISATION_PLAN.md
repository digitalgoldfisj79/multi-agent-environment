# Formalisation plan

## Module

`fortune-formal/FortuneFormal/Integer/SquarefreeCompositeEnergyCriterion.lean`

## Stage A — mandatory in the build

Formalise two finite deterministic implications over arbitrary finite index types and real-valued budgets:

1. **row-budget aggregation**
   \[
   \forall i,\ \sum_j C(i,j)\le Rm_i
   \Longrightarrow
   \sum_i\sum_j C(i,j)\le R\sum_i m_i;
   \]

2. **diagonal-plus-collision assembly**
   \[
   E_q\le D_qM+C_q,\qquad
   \sum_q C_q\le RM
   \Longrightarrow
   \sum_qE_q\le\left(\sum_qD_q+R\right)M.
   \]

Every analytic input remains an explicit theorem argument.

## Stage B — permitted only after an exact proof is available

Potential later formalisation:

- the finite Schur/AM-GM kernel estimate;
- additive-character orthogonality for cyclic residue rings;
- squarefree support and divisor-subset cardinality bounds.

No Stage B theorem may be added with an axiom, opaque placeholder or theorem signature that already contains the desired conclusion under another name.

## Prohibited formalisation

The module must not assert:

- a prime or composite large-sieve estimate;
- a source-compatible collision row bound;
- cancellation in Möbius or source coefficients;
- a transfer to RUHL-FM, INT-SOCG or Fortune.

Those are analytic programme gates.

## Validation contract

- Lean toolchain pinned by the inherited `lean-toolchain` file;
- targeted `lake build FortuneFormal.Integer.SquarefreeCompositeEnergyCriterion`;
- root import into `FortuneFormal.lean`;
- full `lake build` before closeout;
- repository scan for `sorry`, `admit`, `axiom`, `unsafe` and disabled linters in new files;
- theorem signatures mirrored in `CLAIM_MATRIX.json`;
- no successful status until both targeted and full builds pass.
