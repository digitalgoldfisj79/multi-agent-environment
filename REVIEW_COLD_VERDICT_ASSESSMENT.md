# Assessment of the external cold verdict on the Fortune corpus

**Assessed document:** the "cold verdict" review of Papers I–VII plus the
conditional-and-barriers synthesis (12m50s session, delivered 2026-08-06).
**Corpus state checked against:** branch `gpt56/fortune-export-package-20260806`
(head `6fdbe1c`).
**Reviewer:** the same independent reviewer as `REVIEW_INT_SCME_PROGRAMME.md`
(`029cc8c`) and `REVIEW_RUHL_RESIDUAL_STATE.md` (`021a6aa`).

---

## 1. Verdict on the verdict

**Every checkable factual claim in the cold verdict reproduces against the
repository, most of them exactly.** Its strategic conclusions agree with my
two prior line-level reviews on all overlapping ground, and its
recommendations are the ones I would give. I endorse it, with the scoping
caveats in §4.

## 2. Inventory claims — all verified

| Claim | Repository check |
|---|---|
| 33,543 words, Papers I–VII + synthesis | 33,534 by `wc -w` over the eight authoritative manuscripts (counting-method noise) |
| Labelled statements: I=25, II=24, IV=14, V=11, VI=16, VII=7, synthesis=1 | Exact matches, per-paper heading conventions accounted for |
| III=13 "several repeated in Appendix A" | 6 headed statements in main text; Appendix A ("Complete kernel-theory proof") restates the kernel results — duplication confirmed, count convention differs by ±1 |
| References: 10 / 18 / 4 / 3 / 7 / 6 / 4 / 0 | Exact — Paper II and V–VII counts via their `references.bib` (18, 7, 6, 4); synthesis has no bibliography |
| Lean: ~2,900 lines, 77 declarations, one axiom | 2,931 lines across 33 files; exactly 77 `theorem`/`lemma` declarations; exactly one `axiom p7_k2_certified_normalization` (`Frontier/Assumptions.lean:14`) |
| Paper IV title overstates Fortune relevance | Title is literally "Prime Detection Along Random Primorial-Product Paths" — the retitle recommendation is apt |
| Paper VI stale "six-paper sequence" reference | Present at manuscript line 880 |
| Paper V opening frames the integer gap as "derandomisation" | Present (abstract line 11 and §1); the criticism is correct — the corrected Paper II source-to-frame bridge is independently open, per the RUHL/R2 results I verified previously |
| `x^{39/40}` L-function-free short-interval benchmark | Real: Matomäki–Merikoski–Teräväinen, arXiv:2401.17570, proves primes in `(x − x^{39/40}, x]` without L-functions — a fair illustration of the gulf to the `(log x)²` window |

A factual layer this clean is rare in reviews of this genre; it materially
raises my confidence in the verdict's unverifiable judgment calls.

## 3. Agreement on substance

Three of the verdict's central judgments coincide with what I previously
verified at line level on the integer spine:

1. **"Unconditional distance to Fortune essentially unchanged."** Matches my
   two prior reviews. The corpus's own ledgers now say the same.
2. **The characterization of the negative knowledge** (targets shown
   equivalent to the selected-centre problem, stronger than the needed mean,
   absolute-value-fragile, or third-body-blocked) is precisely the R1/R2
   tautology-and-inversion, LCSK triple-cluster, and Heath–Brown dichotomy
   structure I independently re-derived and confirmed.
3. **"Do not reopen the integer programme without a theorem controlling the
   jointly signed selected-centre residual at the frozen Bonferroni scale"**
   is the repository's own `DIRECT_NEXT_STEP.md` bar, which I endorsed at the
   time and still endorse.

The publication strategy (repackage as five papers; theorem-by-theorem
"closest known result and exact difference" sections; four specialist human
reviewers by field; close the Paper VII axiom before any new formalization;
the specific editorial corrections) is sound and I have nothing to subtract
from it.

## 4. Scoping caveats

1. **The proof interiors of Papers IV–VII remain unverified by anyone at line
   level.** My reviews line-verified the integer-programme spine (the
   material underlying Papers I–II and the synthesis). The cold verdict
   states it read the corpus end to end but did not line-read the supporting
   files; reading is not proof-checking. Its own risk ranking (Paper IV's
   logarithmic-slack ledger, Paper VI's multi-field chain, Paper VII's
   certificate boundary) identifies the right targets, but "no new fatal
   contradiction found" should be read as scoped to that reading depth.
2. **The originality counts (20–30 plausibly original, 12–15 headline) are
   judgment, not fact.** With bibliographies this thin (4–10 entries for
   Papers III–VII), collision risk with existing literature — Smith normal
   forms of incidence matrices, gain-graph theory, energy methods on
   multiplicative walks, Frobenius-incidence geometry — is the single
   largest threat to the claimed portfolio value. The verdict says this
   itself; it deserves to be the headline caveat rather than a middle
   paragraph.
3. **Two model reviewers now agree with each other and with the repository's
   own ledgers.** That is consistency, not validation. The four-specialist
   human review allocation is the correct next epistemic step, and no further
   general-purpose model review of this corpus is likely to add information.

## 5. Recommended immediate actions (concurring, in order)

1. Close the `p7_k2_certified_normalization` axiom (finite, well-defined,
   highest assurance-per-effort).
2. Execute the five-paper repackaging with the literature-audit sections
   before any submission.
3. Commission the four specialist reviews.
4. Apply the listed editorial corrections (Paper IV title, Paper V opening,
   Paper VI stale sequence reference, Paper III appendix duplication,
   synthesis bibliography and notation).
5. Hold the integer Fortune frontier closed under the existing admissibility
   bar.
