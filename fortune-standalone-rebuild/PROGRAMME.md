# Fortune standalone-paper rebuild programme

**Programme:** `FORTUNE_STANDALONE_PAPERS_V1`  
**Date:** 11 August 2026  
**Branch:** `gpt56/fortune-standalone-papers-v1-20260811`

## Objective

Rebuild the authoritative Fortune manuscripts so that every paper is independently readable and independently auditable. A referee must not need another paper in the series, an internal programme note, a prior correction notice, or the repository to understand any definition, theorem statement, proof, assumption, computational claim, or logical boundary that is load-bearing for that manuscript.

The cross-paper and Zeta23-style audits are inputs to this rebuild, not publication substitutes.

## Standalone acceptance gate

A manuscript passes only if all of the following hold.

1. **Self-contained problem statement.** The paper defines Fortune's conjecture or its function-field analogue as needed, fixes all notation locally, and states exactly what the paper proves and does not prove.
2. **No logical cross-paper dependency.** Companion papers may be cited as related work or provenance, but no load-bearing definition, lemma, calculation, correction, or theorem may be imported merely as `Paper I`, `Paper II`, etc. Any such item must be restated and, where needed, reproved in the paper or in its own appendix.
3. **No internal-programme shorthand in the exposition.** Labels such as `INT-ISC`, `D1-QLINE-NONSAT`, `RUHL-FM`, `P7-CUBIC-TF`, etc. may appear in a reproducibility appendix but not as unexplained mathematical content in the main article.
4. **Authoritative statement only.** Superseded theorem statements and obsolete centring/main terms are removed from the logical flow. Historical correction notices may be retained only as a short provenance note, never as something required to reconstruct the theorem sequence.
5. **Proof-status separation.** Every substantive claim is visibly one of: proved in the manuscript; exact computational/certificate evidence; derived under a named hypothesis; or open. The prose must not blur these classes.
6. **Evidence is localised.** Finite computations, Lean results and machine certificates are described in a reproducibility appendix with exact scope. The mathematical paper must remain readable without executing them.
7. **References are complete locally.** Every external theorem used is cited in the paper's own bibliography. Companion Fortune papers are not used as surrogates for original literature.
8. **Referee-readable narrative.** The introduction motivates the object, explains the principal mechanism, gives a theorem roadmap, and makes the terminal obstruction intelligible without knowledge of the research programme.
9. **No overclaim.** No paper claims Fortune, full function-field `d=1`, an integer transfer, or axiom-free Paper VII quadratic emptiness unless actually established.
10. **Standalone verification check.** A deterministic script scans each rebuilt manuscript for unresolved series-only references, undefined programme labels, stale superseded terminology and missing evidence-boundary sections.

## Rebuild policy by paper

### Paper I — collision geometry

Recast as a standalone structural/additive-combinatorial paper about consecutive-prime partial products. Supply its own setup, exact collision identities, transport/divisor incidence results, interval endpoint-graph rank/Smith theorem and null-law calculations. State HTE4/HWF4/FBHE4/RQHE4 as open analytic continuations only if they materially clarify the boundary. Remove any implication that these results themselves prove a prime-offset theorem.

### Paper II — primorial-centre prime detection

This needs a substantial rebuild. Start from the Fortune problem itself; derive the composite-offset square threshold and candidate collapse locally; define the unweighted and weighted two-prime detectors; prove the exact detector decomposition and variance-to-no-failure criteria locally. The reciprocal frame becomes a secondary structural section, clearly separated from the exact detector. The paper must not rely on Paper I for the cumulative-product path or Paper III for the covariance interpretation. The corrected prime-pair centring is the only authoritative one.

### Paper III — pair-sum rigidity and covariance kernel

Make the superincreasing pair-sum theory the primary standalone mathematical object. Include the bounded-coefficient rigidity lemma, the `N-or-1` difference-multiplicity dichotomy, energy decomposition, moment/tail theory and the four-prime covariance expansion with all notation introduced locally. Reintroduce the primorial/Fortune application from first principles near the end rather than assuming Paper II. The Lebesgue-tail model and arithmetic sampling measure must remain explicitly distinct.

### Paper IV — random primorial-product paths

Rebuild around the random-permutation theorem as an independent probabilistic/analytic result. Define the random model, reciprocal energy and configuration taxonomy locally. Give a clean section explaining why the increasing primorial order is not controlled. Do not position this as a step that conditionally closes Fortune.

### Paper V — function-field fortunate polynomials

Use only the replacement manuscript as source. Define the polynomial primorial and function-field `d=1` problem locally; prove the reducible-offset degree barrier and degree-at-most-three reduction; derive the quadratic/cubic affine-orbit formulae and crown variable locally. Integrate the finite `p=5,7,11` census and `p=7` singular-locus evidence in a clearly marked computational appendix. State strict q-line nonsaturation/cubic positivity as the terminal open theorem. No integer transfer is suggested.

### Paper VI — secondary traces and Kummer quotients

Use only the replacement manuscript as source. Reconstruct enough of the Paper V setup locally that the trace/quotient theory can be understood without Paper V: define the relevant cubic family, failure counts and target nonvanishing. Then present tangent modules, divided-hook/Hattori--Stallings extraction, Artin--Schreier/Kummer quotients and point-count identities. Make explicit that the quotient-open formulation is equivalent to, not weaker than, the one-sided cubic positivity frontier. Include the independent finite algebraic regressions as a reproducibility appendix.

### Paper VII — bilateral endpoint incidence

Produce one continuous manuscript, not four manuscript fragments plus ledgers. Define the endpoint-incidence problem, inverse-free algebraisation, defect, orientation and quadratic/cubic loci locally. Integrate IFA1/BDD1/BDD2/strip-emptiness and the quadratic discriminant argument into a normal theorem sequence. The exact normalization/certificate boundary must be stated in the paper itself: quadratic emptiness is Lean-derived from `p7_k2_certified_normalization`, not axiom-free. The cubic true-Frobenius theorem remains open. No bridge to Papers V/VI or integer Fortune is implied.

### Conditional-and-barriers synthesis

Rebuild last, after Papers I--VII are frozen. It should be independently readable as a synthesis/research-boundary article: exact finite Bonferroni criterion; corrected RUHL arithmetic interface `E=A+S`; signed first-order term; beta=5 certificate with assumptions; source-identity weighted-residual obstruction; and the final selected-centre signed tuple/covariance frontier. It should cite the standalone papers as related established components, but re-state every implication it actually uses.

## Execution order

1. Freeze source manifest and supersession map.
2. Rebuild Papers II and III first because they carry the corrected integer logical spine and currently expose the most series-language.
3. Rebuild Papers V and VI next, integrating their now-rerun finite evidence.
4. Rebuild Paper VII into one article with its explicit normalization boundary.
5. Rebuild Papers I and IV as independent structural/random-model articles.
6. Rebuild the conditional-and-barriers synthesis last against the frozen standalone set.
7. Run standalone dependency scanner, theorem/evidence ledger check, reference check and full Lean/certificate regression.
8. Produce publication bundle with one authoritative manuscript directory per paper plus a separate reproducibility-support directory.

## Terminal rule

The rebuild is editorial and proof-architectural. It must not silently turn into a new theorem-discovery programme. Any genuinely new mathematical gap discovered during reconstruction is recorded as a gap; it is not papered over by importing an unpublished programme claim or by weakening the statement without an explicit disposition.
