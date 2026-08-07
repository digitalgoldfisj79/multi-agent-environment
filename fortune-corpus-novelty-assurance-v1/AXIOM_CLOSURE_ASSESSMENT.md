# Paper VII axiom-closure assessment

## Result

`AXIOM_BOUNDARY_IRREDUCIBLE_AT_CURRENT_FORMAL_ABSTRACTION`

This does **not** mean the axiom is mathematically irreducible or suspected false. It means that the assurance programme cannot honestly delete the sole external axiom without formalising a substantially larger algebraisation layer than is presently represented in `FortuneFormal`.

## What has been closed

The external boundary was decomposed into two logically separate assertions.

### A. q-free certificate

For a `Quadratic.ModelPoint` satisfying `f0=f1=f2=f3=0` and the arithmetic-open chart conditions, the exact Singular computations force

- `U=1`,
- `B=-2`,
- `(A-C)^2+4A=0`.

Both chart lift matrices were regenerated and independently re-expanded exactly over `Q`. A second power-lift certificate reduces the characteristic denominator support to `{2,3,5}`. The subsequent discriminant contradiction is already kernel-checked in Lean.

At the mathematical/computational level this part of the axiom is therefore closed to high assurance.

### B. genuine Datum normalization

The present axiom quantifies over `Quadratic.Datum F`, not merely over a `ModelPoint F`. It asserts that every genuine cross-distinct inverse-free degree-two incidence over an odd finite field can be normalized into a model point satisfying the exact q-free equations and all arithmetic-open conditions.

The manuscript proves this by explicit polynomial algebra. The current Lean development does not contain the necessary definitions and lemmas for:

1. monic irreducible quadratic coefficient normalisation under translation and homothety;
2. the remainder of `X^q-X` modulo an irreducible quadratic;
3. transport of the four divisibility conditions through that normalisation;
4. coefficient extraction yielding `f0,f1,f2,f3`;
5. translation of irreducibility/distinctness into the model's discriminant nonsquare/open conditions.

Replacing the axiom by a new theorem whose proof simply assumes any of those items would move rather than remove the trust boundary.

## Why the raw certificate is not imported directly

The exact chart lifts are large. Importing megabytes of Gröbner coefficients into Lean is possible in principle but would be poor proof engineering and would still leave the Datum-normalization boundary. The compact power lifts are better, but their denominators require characteristic handling and still do not address genuine normalization.

## Recommended formal route

Create a separate `Quadratic.Algebraisation` layer and formalise, in order:

1. degree-two monic polynomial normal form;
2. Frobenius remainder lemma;
3. endpoint-divisibility coefficient identities;
4. model-open-condition lemmas;
5. compact certificate identities, preferably after deriving smaller human-readable polynomial combinations or using a verified normalization tactic;
6. remove `p7_k2_certified_normalization` only when `K2CertifiedNormalizationStatement` is proved from the actual `Datum` hypotheses.

## Assurance status

The sole axiom has been narrowed from an opaque external theorem to one explicit formalisation project. Its computational half is independently certified; its mathematical normalization is written explicitly in the manuscript; its remaining deficiency is formal representation, not an identified mathematical gap.
