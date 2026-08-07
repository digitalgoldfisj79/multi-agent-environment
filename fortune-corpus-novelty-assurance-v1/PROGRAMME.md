# Fortune Corpus Novelty & Assurance Programme v1.0

Frozen source: `8c506b92ed3a4d43cc647d77480476e1be48af77`, which includes the independently checked cold-verdict assessment on top of export head `6fdbe1c`.

## Purpose

Determine what in the Fortune corpus is actually new, what is correct at publication standard, and what should survive into a final publication portfolio. This is an assurance programme, not a renewed attack on Fortune's conjecture.

## Frozen strategic rule

The integer Fortune frontier is CLOSED. It may reopen only if a new input directly controls the jointly signed selected-centre residual at the frozen Bonferroni scale. A new reformulation, absolute moment bound, detector equivalence, or divisor identity is not an admissible reopening event.

## Evidence classes

- `KERNEL_CHECKED`: Lean kernel checks the stated result without ledgered external axioms.
- `DERIVED_WITH_LEDGERED_AXIOM`: Lean checks the implication but a named external axiom remains.
- `EXACT_COMPUTATIONAL`: finite exact certificate independently reruns.
- `MANUSCRIPT_PROVED_NOT_YET_FORMALIZED`: proof is mathematical manuscript only.
- `OPEN_OR_CONDITIONAL`: hypothesis or theorem remains open.

Novelty classes:

- `NEW`: no prior theorem found with the same conclusion under equal or weaker hypotheses.
- `STRENGTHENING`: prior theorem exists but corpus result strictly strengthens it in a material parameter or structural conclusion.
- `NEW_SPECIALIZATION`: underlying machinery is known but the instantiated theorem/object appears new and nontrivial.
- `KNOWN_SPECIAL_CASE`: result follows from identifiable prior work with no material strengthening.
- `ROUTINE_DERIVATION`: technically correct but not a standalone novelty claim.
- `UNCLEAR`: literature search insufficient; no priority claim permitted.

No theorem is assigned `NEW` from keyword absence alone. Each `NEW` or `STRENGTHENING` verdict requires a closest-known-result record and an explicit difference statement.

## Lane N1 — theorem-level novelty adjudication

1. Freeze a candidate inventory from Papers I–VII and the synthesis.
2. Search by mathematical object and conclusion, not manuscript terminology.
3. For every candidate record:
   - strongest located analogue;
   - source and date;
   - exact hypothesis/conclusion comparison;
   - novelty class;
   - collision risk (`LOW/MEDIUM/HIGH`);
   - recommended claim language.
4. Headline novelty counts are computed only from `NEW`, `STRENGTHENING`, and substantial `NEW_SPECIALIZATION` rows.

Priority literatures include Smith forms of incidence matrices, gain/bidirected graphs, Sidon and superincreasing additive energy, random multiplicative functions and character moments, factorisation statistics over finite fields, symmetric-group/cohomological trace formulae, modular representation theory, Hattori–Stallings traces, Artin–Schreier and Kummer quotients, and Frobenius-incidence geometry.

## Lane A1 — remove the Paper VII trust boundary

Target: eliminate `p7_k2_certified_normalization` from `fortune-formal/FortuneFormal/Frontier/Assumptions.lean`.

Subtargets:

A1.1 Regenerate the two exact Singular lift matrices for the `B != 0` and `A-C != 0` charts.

A1.2 Convert the lift identities into explicit algebraic identities usable by Lean over an arbitrary odd finite field.

A1.3 Prove `Quadratic.CertificateStatement` from `Equations` and `ArithmeticOpen` by the two-chart split.

A1.4 Prove `Quadratic.K2CertifiedNormalizationStatement` from genuine `Datum` normalization rather than asserting it externally.

A1.5 Remove the axiom and run the full formal package plus a trust scan requiring zero `axiom`, `sorry`, `admit`, and unsafe declarations in the FortuneFormal namespace.

A1.3 and A1.4 are deliberately separate: proving emptiness of the q-free model does not by itself prove that every genuine degree-two incidence maps into that model.

## Lane P4 — Paper IV proof-interior audit

Line-audit the random-order theorem with independent recomputation of:

- coefficient-pattern exhaustiveness and exact multiplicities;
- ordered-partition/rank-conditioning identity;
- multivariate contour truncation and losses;
- exceptional-character sixth moment;
- triangular-coordinate and path-matching bijections;
- all-bad configuration domination;
- final logarithmic exponent ledger.

A single unledgered logarithmic loss is a gate failure.

## Lane P6 — Paper VI proof-interior audit

Audit the chain by discipline boundary:

- Cartier moment and q-line projector algebra;
- cyclotomic tangent and modular extension;
- Smith-blindness and no-divided-hook assertions;
- Hattori–Stallings coefficient extraction;
- Artin–Schreier quotient and irreducibility section;
- no-split theorem;
- Kummer classification and common quotient counts;
- unique fixed point and compactified quotient count.

Every cross-field implication must have a named theorem or an explicit proof; analogy is not admissible.

## Lane P7 — Paper VII proof-interior audit

Audit:

- inverse-free algebraisation;
- common-defect derivation and uniqueness;
- zero-defect translation/reflection classification;
- strip corollaries;
- q-free relaxation versus genuine Frobenius orientation;
- two-chart computer certificate;
- normalization from a genuine quadratic incidence;
- final quadratic emptiness theorem.

## Lane R — publication reconstruction

Only after N1, A1, P4, P6 and P7 close:

1. determine the surviving theorem portfolio;
2. decide whether the proposed five-paper structure remains justified;
3. generate four specialist review packets;
4. apply editorial corrections only after the mathematical scope is frozen.

## Stop conditions

The programme stops at the first decisive state:

- `ASSURANCE_READY`: novelty adjudication complete, high-risk proofs audited, and Paper VII axiom removed;
- `PORTFOLIO_REDUCED`: one or more headline clusters are known special cases, requiring publication restructuring;
- `PROOF_REPAIR_REQUIRED`: a proof-interior audit finds a material gap;
- `AXIOM_BOUNDARY_IRREDUCIBLE`: the Paper VII normalization cannot be kernel-closed without formalising a substantially larger algebraisation layer;
- `LITERATURE_UNRESOLVED`: priority cannot responsibly be assessed from accessible literature.

No stop state is a claim that Fortune's conjecture has been proved.