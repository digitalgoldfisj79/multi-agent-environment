# Paper VII Zeta23-style formal trust assessment

## Terminal classification

`COMPARATOR_ARCHITECTURE_PASS__GLOBAL_AXIOM_UNCHANGED`

The run materially improves the trust presentation of Paper VII but does not honestly close the sole custom axiom.

## F0 — independent statement layer: PASS

`FortuneFormal/Comparator/P7ChallengeDeps.lean` imports `Mathlib` only.  It independently states the literal degree-k finite-field polynomial datum, cross-distinctness, Frobenius base and inverse-free incidence predicates.

`FortuneFormal/Comparator/P7Challenge.lean` defines the independent quadratic emptiness proposition

`FortuneChallenge.P7.K2EmptyStatement`.

Neither file imports the Paper VII implementation.

## F1 — literal implementation bridge: PASS

`FortuneFormal/Comparator/P7Bridge.lean` defines `toBilateral` by copying every datum field and proof field literally into `FortuneFormal.Bilateral.Datum`.

The following interface equivalences are definitional (`rfl`):

- cross-distinctness;
- Frobenius base;
- inverse-free incidence.

Consequently any proof of the implementation theorem solves the independent challenge.

The bridge then states the honest conditional theorem

`challenge_k2_empty_of_normalization`

with `Quadratic.K2CertifiedNormalizationStatement F` as an **explicit theorem parameter**.  It does not call `p7_k2_certified_normalization`.

## F2/F3 — axiom and trust audit: PASS

GitHub Actions run `31481626194`, comparator job `93747655480`, completed successfully.

Full build:

`Build completed successfully (8688 jobs).`

The axiom output is exactly:

- `challenge_of_bilateral`: `[propext, Classical.choice, Quot.sound]`;
- `challenge_k2_empty_of_normalization`: `[propext, Classical.choice, Quot.sound]`.

The comparator directory contains no declaration matching `axiom`, `sorry`, `admit` or `unsafe`.

The global package scan still finds exactly one custom axiom, the pre-existing

`FortuneFormal.p7_k2_certified_normalization`.

This is the intended result: the independent challenge cannot be made unconditional merely by importing the implementation axiom.

## Relation to the full Lean FRO comparator

This run implements the high-value trust separation from Zeta23—Mathlib-only statement definitions, independent challenge proposition, literal translation, conditional solution and axiom audit—but it does **not** claim a full sandboxed `leanprover/comparator` replay.

A full comparator run would currently certify only the conditional theorem because the unconditional Paper VII implementation still depends on a project axiom.  Running the sandbox at this stage would not eliminate that mathematical boundary.

The correct point to add byte-for-byte challenge/solution comparison and independent-kernel replay is after the normalization boundary is actually proved.

## F4 — attempted axiom closure

### What is already kernel checked

Once a normalized `ModelPoint` lies on `CertifiedComponent`, the discriminant contradiction and K2 emptiness implication are kernel checked.

### Exact computational certificate inventory

The assurance branch already regenerated power-lift identities for the q-free model.  Inspection of the exact output gives six chart identities.

B chart (`gB = U*A*(B^2-4C)*B`):

- `gB^3*(U-1)`: 2,610 multiplier terms, common-denominator support `2^25 3^6 5^4`;
- `gB^3*(B+2)`: 2,793 terms, support `2^25 3^7 5^4`;
- `gB^3*((A-C)^2+4A)`: 4,093 terms, support `2^32 3^7 5^5`.

X chart (`gX = U*A*(B^2-4C)*(A-C)`):

- `gX^2*(U-1)`: 582 terms, support `2^10 3^6 5`;
- `gX^4*(B+2)`: 6,460 terms, support `2^42 3^9 5^7`;
- `gX^4*((A-C)^2+4A)`: 8,845 terms, support `2^50 3^9 5^8`.

Thus the rational denominator prime support is exactly `{2,3,5}` in these compact power lifts.  This confirms that the computational half is finite and suitable in principle for an `EnclOK`-style kernel certificate: clear denominators, encode the six identities as sparse `MvPolynomial Z` equalities, decide the coefficient equality in Lean, and evaluate them in the target field.  Characteristics 3 and 5 still need their separately certified treatment.

### Why the global axiom is not deleted in this run

The existing axiom asserts more than those six ideal-membership identities.  It universally maps every genuine degree-two `Bilateral.Datum` to the normalized q-free `ModelPoint` and proves the arithmetic-open hypotheses needed to select a chart.

That requires formalising, at minimum:

1. affine normalization of monic irreducible quadratics;
2. reduction of `X^q-X` modulo the normalized quadratics;
3. transport of the four inverse-free divisibilities;
4. coefficient extraction yielding `f0=f1=f2=f3`;
5. transfer of irreducibility/distinctness to the arithmetic-open conditions.

These are symbolic algebra theorems, not finite coefficient checks.  Hiding them behind the certificate checker would reproduce the old trust gap under another name.

## F4 ruling

`AXIOM_NOT_CLOSED`.

No custom axiom was removed or weakened in the authoritative package during this bounded run.  The assurance gain is architectural: the unconditional challenge is now independently stated and the exact location of the missing theorem is visible in the type of the conditional bridge.

The next finite formal build, if authorised, should kernelise the six cleared-denominator power-lift identities first.  Only after that should the global axiom be replaced by a strictly narrower **datum-normalization-only** boundary.  The final step is to formalise that normalization theorem and then run the full sandboxed comparator on the unconditional challenge.
