# Paper VII Zeta23-style formal trust assessment

## Terminal classification

`COMPARATOR_ARCHITECTURE_PASS__SIX_POWER_LIFTS_KERNEL_CHECKED__GLOBAL_NORMALIZATION_AXIOM_REMAINS`

The run materially improves the trust presentation of Paper VII and moves the finite q-free certificate computation into Lean's kernel. It does **not** honestly close the sole custom axiom, because the arithmetic normalization from a genuine bilateral datum to the q-free model remains unformalized.

## F0 — independent statement layer: PASS

`FortuneFormal/Comparator/P7ChallengeDeps.lean` imports `Mathlib` only. It independently states the literal degree-k finite-field polynomial datum, cross-distinctness, Frobenius base and inverse-free incidence predicates.

`FortuneFormal/Comparator/P7Challenge.lean` defines the independent quadratic emptiness proposition `FortuneChallenge.P7.K2EmptyStatement`.

Neither file imports the Paper VII implementation.

## F1 — literal implementation bridge: PASS

`FortuneFormal/Comparator/P7Bridge.lean` defines `toBilateral` by copying every datum field and proof field literally into `FortuneFormal.Bilateral.Datum`.

Cross-distinctness, Frobenius base and inverse-free incidence are transported by definitional (`rfl`) equivalences. Consequently any proof of the implementation theorem solves the independent challenge.

The bridge states the honest conditional theorem `challenge_k2_empty_of_normalization` with `Quadratic.K2CertifiedNormalizationStatement F` as an **explicit theorem parameter**. It does not call `p7_k2_certified_normalization`.

## F2/F3 — axiom and trust audit: PASS

GitHub Actions run `31481626194`, comparator job `93747655480`, completed successfully. A later regression build including `CertificateBridge.lean` also passed.

Full build: `Build completed successfully (8688 jobs).`

The axiom output is exactly:

- `challenge_of_bilateral`: `[propext, Classical.choice, Quot.sound]`;
- `challenge_k2_empty_of_normalization`: `[propext, Classical.choice, Quot.sound]`.

The comparator directory contains no declaration matching `axiom`, `sorry`, `admit` or `unsafe`.

The global package scan still finds exactly one custom axiom, the pre-existing `FortuneFormal.p7_k2_certified_normalization`.

This is the intended trust architecture: the independent challenge cannot become unconditional merely by importing the implementation axiom.

## Relation to the full Lean FRO comparator

This run implements the high-value trust separation from Zeta23—Mathlib-only statement definitions, independent challenge proposition, literal translation, conditional solution and axiom audit—but it does **not** claim a full sandboxed `leanprover/comparator` replay.

A full comparator run would currently certify only the conditional theorem because the unconditional Paper VII implementation still depends on a project axiom. The correct point to add byte-for-byte challenge/solution comparison and independent-kernel replay is after the normalization boundary is actually proved.

## F4 — axiom closure attempt

### 1. Six exact q-free power-lift identities: KERNEL_CHECKED

The assurance branch regenerated six exact Singular lift identities for the q-free model. A new untrusted generator clears the rational denominators and emits literal sparse `MvPolynomial (Fin 4) Z` equalities. Mathlib's reflective `ring` normalizer checks the generated identities in Lean.

B chart (`gB = U*A*(B^2-4C)*B`):

- `gB^3*(U-1)`: 2,610 multiplier terms, denominator support `2^25 3^6 5^4` — **kernel checked** by split-normalization job `93755158829` in run `31484014359`;
- `gB^3*(B+2)`: 2,793 terms, support `2^25 3^7 5^4` — **kernel checked** by split-normalization job `93755158760` in run `31484014359`;
- `gB^3*((A-C)^2+4A)`: 4,093 terms, support `2^32 3^7 5^5` — **kernel checked** in the all-chart run.

X chart (`gX = U*A*(B^2-4C)*(A-C)`):

- `gX^2*(U-1)`: 582 terms, support `2^10 3^6 5` — **kernel checked**;
- `gX^4*(B+2)`: 6,460 terms, support `2^42 3^9 5^7` — **kernel checked**;
- `gX^4*((A-C)^2+4A)`: 8,845 terms, support `2^50 3^9 5^8` — **kernel checked**.

The monolithic `ring` normalization of B1 was cancelled by a runner shutdown after certificate generation had succeeded; it produced no coefficient contradiction. To remove that performance dependency, `fortune-paper7-kernel-fast/generate_b12_split.py` expands the four products separately and checks B1/B2 in smaller Lean lemmas. Both split checks passed in run `31484014359`.

Thus the rational power-lift identities themselves no longer rely on trusting Singular or Python: Singular/Python generate candidate witnesses; Lean verifies the exact polynomial equalities.

### 2. Chart-selection logic: KERNEL_CHECKED

`FortuneFormal/Quadratic/CertificateBridge.lean` defines the two localization factors and the six pointwise chart identities. It proves:

- arithmetic openness makes the selected localization factor nonzero;
- the corresponding three zero-product identities force `U=1`, `B=-2`, and `(A-C)^2+4A=0`;
- therefore `ChartIdentities -> CertifiedComponent` on the arithmetic-open locus;
- universally available chart identities imply the published `CertificateStatement`.

This file compiles in the full FortuneFormal build.

### 3. Characteristic specialization still to formalize

The compact rational lifts have denominator-prime support exactly `{2,3,5}`. Since Paper VII assumes odd cardinality, the rational certificates specialize directly once denominator invertibility is proved in characteristics other than 3 and 5.

The original Round-15 certificate record already includes direct exact mod-3 and mod-5 chart reductions, but those two exceptional-characteristic multiplier certificates have **not yet** been translated into Lean in this run. Accordingly the field-level universal `ChartIdentities` theorem is not yet claimed kernel-checked for all odd finite fields.

### 4. Why the global axiom remains

The existing axiom asserts more than the six ideal-membership identities. It universally maps every genuine degree-two `Bilateral.Datum` to a normalized q-free `ModelPoint` and establishes the arithmetic-open hypotheses needed to select a chart.

That requires formalizing, at minimum:

1. affine normalization of monic irreducible quadratics;
2. reduction of `X^q-X` modulo the normalized quadratics;
3. transport of the four inverse-free divisibilities;
4. coefficient extraction yielding `f0=f1=f2=f3`;
5. transfer of irreducibility/distinctness to the arithmetic-open conditions.

These are symbolic algebra theorems, not finite coefficient checks. Hiding them behind a certificate checker would reproduce the old trust gap under another name.

## F4 ruling

`AXIOM_NOT_CLOSED__COMPUTATIONAL_HALF_KERNELIZED`.

No custom axiom has been deleted or weakened. The assurance gain is nevertheless substantive: the q-free certificate identities and chart-selection implication have moved from external exact computation into kernel-checked mathematics, while the independent challenge makes the remaining normalization theorem explicit.

## Exact next formal build

The remaining closure sequence is now finite and well scoped:

1. kernelize the direct characteristic-3 and characteristic-5 chart certificates;
2. prove specialization of the integer power-lift certificates to finite fields of characteristic not 2, 3 or 5;
3. combine those with `CertificateBridge.lean` to prove `CertificateStatement` axiom-free;
4. replace the current broad axiom by a narrower datum-to-q-free-normalization statement;
5. formalize that normalization theorem;
6. delete the final custom axiom and run the full sandboxed comparator on the unconditional independent challenge.
