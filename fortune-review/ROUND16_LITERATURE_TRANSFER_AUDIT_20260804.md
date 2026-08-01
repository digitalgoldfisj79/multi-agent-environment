# Round 16 audit: the ρ=1 correction is verified from original definitions
# (and falsifies one of my own panel biconditionals), the two-torsor theorem
# is confirmed on my orientation data, and the q-line falsification is
# reproduced independently

Reviewer: Claude (continuation of the PR #33 independent review; this round
audits draft PR #38)
Date: 2026-08-04
Audited state: branch `gpt56/fortune-monodromy-trace-transfer-20260731`,
head `d807178` (two commits above the TFP3 head `e5ef12c`, which is itself
audited here through its committed notes and verifiers — PR #37's round had
not previously been audited).
Independent audit artifacts: `fortune-review/scripts/ff_round16_audit.py`,
outputs archived in `fortune-review/data/ff_round16_audit_output.txt`.

## 0. Scope statement (post-cutoff literature)

The round under audit imports published results I cannot read: Chuang,
*On the Generalized Arithmetic Picard–Lefschetz Formula* (arXiv:2607.05757,
July 2026) and several of the cited transfer sources postdate my knowledge
window. As with Blomer–Pascadi in Round 2, everything imported from them is
treated **as-cited**: I audit the machine-verifiable repository content, the
internal consistency of the specialization scripts, and every piece of
mathematics I can re-derive; no verdict below depends on the content of a
paper I cannot inspect, and each such dependency is labeled.

## 1. Executive verdict

The round's two corrections are both **real, and both verified here
independently** — and one of them lands on me as well as on PR #37:

1. **ρ = 1 is allowed in nonzero defect.** The two q = 97 records verify
   completely from the original local-frequency definitions (my Round-13
   machinery, no shared code): four distinct irreducible cubics, witness
   constants c = −1, d = 1 (θ = 1, gauge λ = ρ = 1), literal simultaneous
   incidence μ_aP′ − μ_bP = −1, ν_aS′ − ν_bS = 1, nonzero common defect of
   degree 89 ≤ q − 2k = 91 satisfying every BDD1 identity, and full
   Frobenius orientation (σ = (1,1,1,1), κ = +1). Since ρ = λ ⟺ c + d = 0,
   these records falsify the right-to-left half of "h = 0 ⟺ c + d = 0" —
   a biconditional **my own Round-13 note and script docstring carried as a
   panel observation** ("h = 0 ⟺ c + d = 0 throughout"). The forward
   implication (BDD2: h = 0 ⟹ ρ = λ, hence c + d = 0) is a theorem and
   stands; the converse was only ever data through q ≤ 59 and is now dead
   at q = 97. I hereby correct my Round-13 labeling: the ⟸ half should
   have been flagged as panel-empirical, exactly the failure mode this
   collaboration keeps documenting. Two mitigating facts, verified: my
   census enumerator never filtered on c + d or ρ (all counts stand), and
   deg h = 89 < 91 shows the BDD1 degree bound is *not* always attained —
   the (11,3) panel's "always exactly q − 2k" was a panel accident too.
2. **The sign object is two torsors, not one global 8-sheeted cover.** I
   re-derived the symbolic content with my own sympy code: the resultant
   identity Res_t(F, N_e) − e⁴ = −(e² − disc F)·Q/8 with their exact Q, and
   the elimination showing (η_Aη_D − η_Bη_C)·R_AB·R_CD lies in the ideal of
   the four block relations — so the orientation identity is a theorem
   exactly on the cross-distinct separable locus, as stated. The sixteen
   sign vectors split into two disjoint 8-element torsors indexed by
   κ = η_A^F η_D^F/(η_B^F η_C^F), with (1,1,1,1) only in κ = +1.

## 2. The κ panel (new data, my classifier)

On my Round-14 enumeration of the irreducible nondegenerate V(F_q) points,
with Frobenius orientations η^F computed by my own code:

| q | irred. nondegen. points | identity holds | true (σ = all +1) | true κ | spurious κ = +1 | spurious κ = −1 |
|---|---:|---:|---:|---|---:|---:|
| 11 | 4 | 4/4 | 2 (ρ = 7, 8 = census) | +1 | 2 | 0 |
| 13 | 8 | 8/8 | 0 (= census) | — | 4 | 4 |
| 17 | 22 | 22/22 | 2 (ρ = 8, 15 = census) | +1 | 20 | 0 |

Three conclusions. (a) The q-free identity holds on the *entire* irreducible
nondegenerate class — my Round-14 remark that it holds on "only half of
V(F_q)" was about the full variety including degenerate and split points;
on the open locus it is the theorem the sign-cover lemma says it is.
(b) The relative-sign equation σ_Aσ_D = κσ_Bσ_C holds at every point, the
true class is exactly σ = (1,1,1,1), and every true point has κ = +1 — the
branch's claim, confirmed on data they did not use. (c) **Both κ classes
are populated** (q = 13: a clean 4/4 split), so the κ = −1 torsor is not
vacuous and the componentwise-κ obligation in their Chebotarev gate is a
genuine obligation, not bookkeeping.

## 3. The q-line falsification — reproduced independently

With my own irreducibility census (Rabin test, no flint, no shared code)
for f = qz^p + z³ − 3z − (q−2)t, E₁(q) = p(1 − I₁(q)):

    p:        5   7   11  13  17  19  23  29
    ΣE₁/p:   −1  −1  −1   3   3   1   3  −7

This matches their table digit-for-digit, confirms Σ E₁ = −p exactly at
p = 5, 7, 11, its failure from p = 13 on, and the sign flip at p = 29. The
"universal one-line Tate identity" is dead, and the varying quotient
supports their reading that the q-line surface carries a nontrivial trace
that must be computed, not guessed.

## 4. Repository-internal checks and the as-cited boundary

All of the branch's committed verifiers were run from a clean checkout of
`d807178` and pass: `ff_tfp3_rho_one_defect_audit.py`
(TFP3_RHO_ONE_NONZERO_DEFECT_EXACT_PASS; deg h = 89 both records, and the
two records' η-vectors are mirror images — they are each other's transpose
partners at the self-inverse ρ = 1), `ff_tfp3_sign_cover_audit.py`
(TFP3_ORIENTATION_TORSOR_EXACT_PASS), `ff_tfp3_panel_analyse.py` (slope
0.2455643, R² 0.7951651 on q ≥ 29 exactly as reported, labeled alarm-not-
proof), `chuang_specialization_audit.py` (ranks (p − 5)/6 = 1, 2, 3, 4 at
p = 11, 17, 23, 29; correction index set {1} at k = p; empty at k = p − 2;
no inertia-invariant contribution) and `mod_p_adams_sequence_verify.py`
(elementary binomial identities; fully internal, verified). The rank
arithmetic (p+1)/2 − 1 − (⌊p/3⌋ + 1) = (p−5)/6 for p ≡ 5 (mod 6) is a
checkable identity and checks out. What I cannot audit is whether Chuang's
Theorems 4.18/4.21/4.22 say what the specialization script encodes — that
is **as-cited**, and the branch's conclusion built on it ("the missing d=1
cancellation is not an unidentified local Picard–Lefschetz correction") is
conditional on the citation being faithful. The two named open gates
(integral Tate-diagonal lift; Airy-to-hook transport) do not depend on the
citation and stand on repository-internal evidence.

I also verified the committed extended panel's internal arithmetic (every
row has incidences = orbits × q(q−1); every ρ multiset is inversion-
invariant, including the two ρ = 1 entries at q = 97). The q = 97 census
count of 16 orbits and the whole q = 61..101 extension are **not
independently re-runnable at my scale** (my Round-13 independent census
stopped at q = 37); they remain as the branch labels them —
empirical-exact finite panels from a machine-verified implementation whose
q ≤ 37 rows I did reproduce exactly in Round 13.

## 5. Assessment of the corrected gates

1. **The 6-step Chebotarev gate is the right formalization** of what
   Rounds 14–15 established informally: my Round-14 conclusion was that
   the decisive object is a twisted-Frobenius orientation condition that is
   not Zariski on the relaxation; the κ = +1 torsor with the all-positive
   σ class *is* that condition, now with the correct two-torsor structure.
   The gate's ordering (saturated curve theorem → componentwise κ → torsor
   → étaleness/monodromy → Chebotarev) matches the k = 2 template from
   Round 15, with the mechanism step replaced by a count, exactly as my
   Round-15 note predicted the cubic case would require.
2. **The linear-growth alarm is honestly labeled and my Round-14 caution
   needs updating in the other direction.** In Round 14 I wrote that the
   true count was "bounded, exactly as the census says" through q = 59.
   The extended panel (6..24 orbits over q = 61..101, OLS slope ≈ 0.25) now
   disfavours boundedness. Both statements are finite-panel readings; the
   branch's "empirically disfavoured, not refuted" is the correct label
   for O(1) today, and my earlier lean toward boundedness should be read
   as superseded by more data — the third time on this programme that a
   panel extrapolation flipped (mine at Round 12/13, theirs at Round 14,
   mine again here). Note the alarm cuts against the *programme's own
   earlier hope*: if the true class really has positive Chebotarev
   density, then NDC_FF's sparsity route dies and everything moves to the
   Δ_PS amplitude clause — which is what their "downstream boundary"
   correctly says.
3. **The two-programme separation is right** and matches my mechanism map:
   the TFP3/Paper VII line and the direct d=1 Airy line were separate
   crown approaches on the map from the start, and the ruling that neither
   credits the other without an explicit bridge theorem is the same
   discipline the map encodes. The Papers V–VII disposition (freeze, no
   retrofits, Paper VIII only after a theorem) is the right publication
   posture.

## 6. Boundary

| Status | Item |
|---|---|
| **VERIFIED (this audit, exact, independent code)** | Both q = 97 ρ = 1 records from original local-frequency definitions (incidence, defect deg 89, BDD1, Frobenius orientation, κ = +1); the resultant/cofactor identity and the elimination proof of the orientation identity; the two-torsor combinatorics; the κ panel at q = 11, 13, 17 (identity on the full open class, true = census, true ⊂ κ = +1, both κ classes populated); the q-line quotients −1,−1,−1,3,3,1,3,−7 at p = 5..29; the committed panel's orbit and ρ-inversion arithmetic. |
| **CORRECTED (mine)** | The ⟸ half of "h = 0 ⟺ c + d = 0" (Round-13 panel observation, now falsified at q = 97); "deg h always = q − 2k" ((11,3) accident); my Round-14 "orientation invariant holds on only half" (true of full V, not of the open class); my Round-14 boundedness lean (superseded by the extended panel). |
| **CONFIRMED (branch, run from clean checkout)** | All five committed verifiers pass with outputs matching the notes; the ρ = 1 verifier correction; the extended-panel fit numbers. |
| **AS-CITED (cannot audit)** | Chuang arXiv:2607.05757 content (the specialization script's fidelity to Thms 4.18/4.21/4.22); the Bary-Soroker / BBSR / Sawin–Shusterman transfer readings. The rejection of direct short-trace import rests on repository-internal rank arithmetic and is not as-cited. |
| **NOT RE-RUNNABLE AT MY SCALE** | The q = 61..101 census rows (my independent census reproduced q ≤ 37 exactly in Round 13; the extension is accepted as labeled). |
| **OPEN (concurring with the branch)** | The saturated faithful curve theorem; componentwise κ; the finite-étale torsor and its monodromy; effective Chebotarev for the all-positive class (or confinement); the Δ_PS amplitude theory (now decisive if density is positive); the integral Tate-diagonal lift; Airy-to-hook transport; the d=1 crown; every integer interface; Fortune. |
