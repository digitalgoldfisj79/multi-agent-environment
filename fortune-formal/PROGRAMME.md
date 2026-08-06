# Fortune Formal Discovery Programme v0.1

**Date:** 4 August 2026  
**Status:** BUILT — NOT YET EXECUTED  
**Base:** Fortune Paper VII canonical head `069f47724a3581dc40cfbc9efa3fafd14181ba3e`

## 1. Research objective

Construct a kernel-checkable formal dependency chain from the definitions of bilateral endpoint incidence through the stable Paper VII theorem package, then expose exactly one active research frontier:

> the cubic true-Frobenius point theorem on the faithful saturated locus, with the Frobenius-orientation condition represented literally rather than replaced by the q-free algebraic relaxation.

The programme is a certification and discovery architecture. It does not assume that formalization itself proves the frontier theorem.

## 2. Separation of research lanes

This branch is isolated from:

- the integer `PBDH_P -> PORS -> PORC/T3` programme;
- the direct function-field `d=1` q-line non-saturation programme;
- Paper VII publication editing.

No result in this branch may be counted toward integer Fortune or direct `d=1` without a separately stated and proved bridge.

## 3. Formal trust model

### 3.1 Trusted kernel

- Lean 4.32.0 kernel;
- mathlib v4.32.0;
- explicit classical axioms already present in Lean/mathlib where used;
- Comparator for an independent exported-proof check at release gates.

### 3.2 Temporary assumptions

At Stage F0, manuscript theorems are represented by named axioms in one file only:

`FortuneFormal/Frontier/Assumptions.lean`.

Every permitted axiom must appear in `AXIOM_LEDGER.json` with:

- exact Lean declaration name;
- corresponding Paper VII claim ID;
- source theorem/certificate;
- removal gate;
- status.

No `sorry`, `admit`, `unsafe`, hidden theorem axiom, or unledgered `axiom` declaration is permitted.

### 3.3 Promotion rule

A claim moves from `ASSUMED` to `FORMALIZED` only when:

1. its axiom is deleted;
2. a theorem of the same type is proved from definitions and previously formalized results;
3. `lake build FortuneFormal` succeeds from a clean checkout;
4. the static verifier reports no trust-boundary regression;
5. an independent reconstruction or Comparator challenge succeeds.

## 4. Frozen mathematical scope

The formal Paper VII package is limited to these claims:

- `P7-IFA1`: inverse-free equivalence and uniqueness of scalar witnesses;
- `P7-BDD1`: unique common bilateral defect and degree bound;
- `P7-BDD2`: zero-defect reflection/translation classification;
- `P7-STRIP`: emptiness for prime `q` with `k < q < 2k`;
- `P7-K2`: quadratic emptiness over every odd prime power.

Supporting formal obligations include polynomial degree arithmetic, monicity, irreducibility, finite-field units, quotient/remainder identities, unique factorization, discriminants, localization charts and the exact certificate-to-theorem bridge.

The finite cubic census, tangent dimensions, empirical count laws and heuristic asymptotics are excluded from the formal theorem package.

## 5. Gate sequence

### F0 — specification freeze

Deliverables:

- compilable Lean package;
- exact theorem interfaces;
- axiom ledger;
- machine-readable programme contract;
- static verifier and CI.

Pass condition: the package compiles with only the ledgered assumptions and no theorem is mislabelled as formalized.

### F1 — foundational definitions

Formalize:

- monic degree-`k` polynomial data over finite fields;
- cross-distinct bilateral quadruples;
- scalar-witness and inverse-free incidence predicates;
- common defect predicate;
- zero/nonzero defect split;
- true Frobenius orientation data as a separate predicate.

Pass condition: no semantic notion used by Paper VII remains an opaque proposition parameter.

### F2 — inverse-free algebraization

Remove assumption `p7_ifa1` by proving equivalence and uniqueness of scalar witnesses.

Required checks:

- all nonzero denominators represented as units;
- no cancellation step silently assumes cross-distinctness beyond the stated open locus;
- field-characteristic hypotheses explicit.

### F3 — defect dichotomy and strip

Remove assumptions `p7_bdd1`, `p7_bdd2`, and `p7_strip`.

Formalize:

- quotient-polynomial construction;
- unique common defect `h`;
- `degree h <= q - 2*k` in the literal parameter convention;
- the `h=0` factorization;
- reflection/translation classification;
- intermediate-strip emptiness.

### F4 — quadratic emptiness

Remove assumption `p7_k2_empty`.

Formal proof architecture:

1. faithful four-equation reduction;
2. two open localization charts;
3. imported exact polynomial identities converted from certificate output into Lean-checkable identities;
4. exceptional-characteristic ledger;
5. ideal-faithfulness bridge;
6. discriminant-square contradiction.

Computer algebra may generate certificates, but Lean must check every imported identity. Calling Singular from CI is not itself a Lean proof.

F4 exit condition: **zero Paper VII axioms remain**.

### F5 — cubic frontier isolation

Define, without assuming geometry not yet proved:

- normalized cubic faithful locus;
- q-free relaxation;
- true Frobenius orientation/sign data;
- base invariant `kappa`;
- the two relative-sign torsors;
- literal true-point predicate;
- weighted amplitude interface kept separate from point existence.

At the end of F5 the only permitted research assumption is:

`cubic_true_frobenius_point_theorem`.

Its statement must be the weakest theorem sufficient for the next application gate. It must not assert a full asymptotic if nonemptiness, non-saturation or a bounded exceptional classification suffices.

### F6 — parallel theorem discovery

Run independent lanes against the exact F5 theorem statement:

- algebraic component and saturation lane;
- finite-cover/torsor/monodromy lane;
- trace-function and character-sum lane;
- dynamical Frobenius fixed-point lane;
- symmetry, congruence, determinant or nonvanishing lane;
- adversarial counterexample lane.

Rules:

- every lane receives the same frozen definitions and target;
- no lane may modify the target after seeing failed evidence without a formal programme amendment;
- computational observations remain `EMPIRICAL` until converted into proof obligations;
- incompatible candidate proofs are tested independently rather than reconciled rhetorically.

### F7 — reconstruction and independent checking

A candidate theorem is accepted only after:

1. a clean human-readable proof is written;
2. a second derivation is produced without access to the first proof trace;
3. the Lean assumption is replaced by a theorem;
4. all downstream modules compile;
5. Comparator accepts the exported challenge;
6. the claim ledger and publication boundary are updated.

## 6. Stopping rules

The programme stops and reports a decisive result when any of the following occurs:

- the formal statement is inconsistent with the manuscript claim;
- a hidden hypothesis is exposed;
- a Paper VII proof cannot be reconstructed from its committed certificates;
- the cubic target is falsified by a literal true-Frobenius counterexample;
- the cubic target is proved;
- the programme reaches one irreducible theorem requiring new mathematics, stated without auxiliary ambiguity.

It must not stop merely because a proof search failed, a Gröbner basis was expensive, or a model returned no candidate.

## 7. Compute protocol

- symbolic and finite-field sentinels before remote compute;
- hard timeout on every paid job;
- one primary paid job per gate unless preregistered otherwise;
- cancel immediately when a premise is invalidated or a cheaper discriminator succeeds;
- preserve job IDs and terminal status in a compute ledger;
- end every execution turn with `RUNNING_REMOTE_JOBS=0`.

## 8. Success hierarchy

1. **Programme built:** contract, package and CI exist.
2. **Paper VII formalized:** all five Paper VII assumptions removed.
3. **Frontier isolated:** one cubic theorem remains.
4. **Frontier proved:** the cubic theorem is kernel-checked.
5. **Application bridge proved:** a separate theorem connects the result to its next endpoint claim.

Only level 4 is a new frontier theorem. None of levels 1–4 proves integer Fortune.
