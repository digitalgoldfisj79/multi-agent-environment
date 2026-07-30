# Round 11 independent audit: Route A closure, the characteristic-three
# resonant family, the Δ panel, and the inverse-free scheme — all verified

Reviewer: Claude (continuation of the PR #33 independent review)
Date: 2026-08-01
Audited state: branch `gpt56/fortune-mesoscopic-cotlar-20260728`, head `2739aad`,
notes `FF_ROUTE_A_CLOSED_BY_PROJECTIVE_OCCUPANCY_20260730.md`,
`FF_PRIMORIAL_RESONANT_COMPONENT_20260730.md`,
`FF_PRIMORIAL_RESONANT_DELTA_PANEL_20260730.md`,
`FF_BILATERAL_INCIDENCE_INVERSE_FREE_SCHEME_20260730.md`, together with the
falsification, scale-correction, Gate-1 and corrected-map notes.
Independent audit artifacts (no shared code with the branch verifiers):
`fortune-review/scripts/ff_round11_independent_audit.py`, output archived at
`fortune-review/data/ff_round11_independent_audit.txt` (all PASS, exit 0).

## 1. Executive verdict

**All four Round-11 claims are accepted.** Every load-bearing identity was
re-derived by hand and re-verified with an independent implementation, and
every published exact panel number — including the twelve-digit k = 5
Δ-aggregates — reproduces exactly. The corrections directed at my earlier
artifacts are accepted and adopted (§3). The audit adds two structural
results the branch can use in Gates 2–3: a small provable lemma pinning the
resonant/transpose intersection to k = 3 (§4.2), and a probe showing the
Δ-panel involution invariance is a **product-level** identity only — the
individual local factors are not preserved — which constrains the shape of
any uniform proof (§4.3).

## 2. Claim-by-claim verdicts

### Claim 1 — Route A closed by projective occupancy: **VALID**

- **Theorem PO2** re-derived from the quadratic-character count (the u = 0
  bijection; Σ_λ χ(D_λ) = −1; the square-class of Δ as x² − D with x = b − 2v)
  and machine-verified for every degree-2 irreducible at q = 3, 5, 7, 11:
  occupancies split ((q−3)/2, (q−1)/2) with multiplicity (q+1)/2 each.
- **The transfer step** was verified in its strongest combinatorial form: for
  every P, the sampled-frequency multiset {μ_PS(θ)} over (θ ≠ 0, S ≠ P) is
  constant on every projective line of F_q[t]/P, and the multiset of
  line-counts equals the occupancy multiset of Theorem PO2 (q = 3, 5, 7, 11,
  primorial puncture). The mass inequality Σ_θ M_samp ≥ ((q−3)/2)·M_full
  follows for arbitrary nonnegative |Â|² weights — no genericity enters.
- **The variance bookkeeping** V_all(P) = G(3;P) + q⁴/(q²−1) re-derived
  (mean shift q³/(q²−1) → q with vanishing cross term) and verified exactly
  in rational arithmetic for every band prime at q = 3, 5, 7, along with
  N_P(0) = 0. Numeric corroboration of the Keating–Rudnick scale: G/q³ =
  0.514, 0.752, 0.834 (rising toward deg P − 1 = 1) and M_full/q⁷ = 0.296,
  0.384, 0.420 (rising toward 1/2). Scope note: I re-verified the *scale*
  numerically and the identity chain exactly, but could not independently
  re-check the cited theorem numbering (arXiv:1204.0708, Thm 2.2(ii))
  offline; given the numeric trend and that my own L2 theorem used the same
  input, I accept "PROVED FROM PUBLISHED INPUT" as labelled.
- **All seven M_samp panel values** reproduced exactly with my own Z[ζ_q]
  implementation, including (11,2,3) = 3,993,000 in Z[ζ_11] and the k = 3, 4
  entries: 216 / 10500 / 148176 / 3993000 / 21384 / 9697500 / 1907874. The
  exact inequality (q−1)M_samp ≥ ((q−3)/2)M_full holds with margin on every
  panel (e.g. q = 7: 889056 vs 691488).
- **The conclusion's arithmetic** — max_θ M_samp ≥ (1/4+o(1))q⁷ against the
  Route A allowance q⁶·O(1) — is correct, and the panel ratios M_samp/q^{3k}
  = 0.30, 0.67, 1.26, 2.25 at q = 3, 5, 7, 11 display the forced linear
  growth directly. **SAD_FF is dead as a uniform pointwise route; Route B
  (centred bilateral) is the sole main line.** I concur, and note this is
  the correct resolution of the question my Round-8/9 notes left open in the
  direction my finite panels already suggested: the deterministic sampled
  diagonal sits at the natural scale, and the endpoint deficit cannot be
  bought back by sampled-mass miracles.

### Claim 2 — the characteristic-three resonant family: **VALID, one wording correction**

- **Theorem PRC1** re-derived (the two mod-P/mod-P′ congruences plus the
  degree-< 2k divisibility trick) and machine-verified for **every** generated
  prime point at k = 3, 4, 5 and both θ ∈ F_3^*: μP′ − μ′P = −θε⁻¹ and
  νS′ − ν′S = +θε⁻¹ exactly. Point counts 2 / 12 / 72 with even ε-split
  reproduce; the char-3 monicity mechanism (−1−1 = 1) checks.
- **Completeness at (3,4):** my full 306² pair-of-pairs scan finds exactly 12
  non-diagonal, non-transpose simultaneous incidences and they coincide as a
  set with the generated family. The (5,3) panel's total diagonal collapse
  (1560 = 1560 diagonal, no transpose, no other) and the (3,3) panel
  (56 + 2 transpose + 0 other) also reproduce exactly.
- **The Gram phase and dimension bound**: G(c) = ψ(c)B_m re-checked (trivial
  once c is scalar and deg cf < 2k), G_μG_ν = B_m² verified; the ledger
  N_res ≤ 2·3^{2k−3}, B_m ≤ m·3^m, ratio ≤ 2m²·3^{−k−3} re-derived — correct.
- **Correction (wording, not substance):** the construction says "assume
  P, S, P′, S′ are distinct irreducibles", but at k = 3 the family is
  *entirely transpose-degenerate* (see Lemma R11-L1 below): both points have
  P′ = S and S′ = P, so only two distinct primes occur. The correct running
  hypotheses are the pairwise ones (P ≠ S, P′ ≠ S′, P ≠ P′, S ≠ S′), which
  is also exactly what Theorem IFA1 needs. With that reading, the k = 3 row
  of the resonant table and the (3,3) row of the falsification table
  (transpose = 2, other = 0) are consistent rather than in tension.

### Claim 3 — the Δ panel: **VALID**

- Independent implementation of X_a = Â_P(μ)Â_S(ν), Δ_PS (the exact f = f′
  term — same convention as my Round-7 assembly diagonal), and B_a = X_a −
  Δ_PS. Involution invariance X_a = X_b, Δ_a = Δ_b, B_a = B_b verified
  exactly for all 2 / 12 / 72 points at k = 3 / 4 / 5.
- **All fifteen aggregate entries match exactly**, e.g. at k = 5:
  XX = 308,039,038,452, XD = DX = −92,518,064,244, DD = 35,233,974,972,
  BB = 528,309,141,912, with BB = XX − XD − DX + DD and BB ≥ 0, and
  BB/3^{2m+3k} = 0.00132 / 0.0000893 / 0.0000950 — all far inside the raw
  dimension bound 2m²3^{−k−3} (= 0.0686 / 0.0448 / 0.0247). The corrected
  component is coherent-positive and dimensionally small, exactly as stated.
- I concur with the note's own framing: this is finite-exact evidence that
  the resonant component must be carried explicitly (no symmetry discards
  it), not a uniform theorem.

### Claim 4 — Theorem IFA1 (inverse-free algebraization): **VALID**

Re-derived (same two-congruence + degree argument as PRC1) and verified by
independent scans over every cross-distinct pair-of-pairs at (3,2), (5,2),
(7,2), (3,3), (3,4) — 252,554 quadruples, 666 incidences — with both
directions of the equivalence and uniqueness of the scalar witness c checked
against all candidate scalars. The resonant subfamily satisfies the scheme
with (c, d) = (−θε⁻¹, +θε⁻¹) at k = 3, 4, 5 for both θ. The reformulation is
correct and, I agree, the right Gate-2 object: the classification problem is
now quadratic coefficient geometry with unique scalar witnesses, and no
modular inversion obstructs a scheme-theoretic decomposition.

## 3. Corrections to my artifacts: accepted

1. **Δ_PS omission.** My Round-8 dispersion verifier's T computed the
   uncorrected product aggregate (the f = f′ term was not subtracted).
   Accepted. Cross-validation: the branch's T_corr values (270 / 7600 /
   39788 at q = 3/5/7) equal my Round-7 assembly script's archived values
   exactly — my Round-7 chain had the correct subtraction; my Round-8
   verifier dropped it. The D1/D2 structure lemmas are unaffected; the D3
   numeric ledger rows labelled |T| should be read as the uncorrected
   aggregate.
2. **"C(θ) ≤ Diag, factor ≤ 2".** Finite-panel observation, not a theorem —
   accepted; this matches my own boundary tables (C ≤ Diag was always in the
   EMPIRICAL-EXACT row), and the corrected-map wording is the right one.
3. **Plancherel mass scale.** The all-frequency mass is q^{m+k}-scale (the
   factor q^k is part of the identity); any of my wording that read the
   left side at q^m scale is corrected. The identity itself (my L2) stands.
4. **First-dispersion diagonal floor.** The exponent ledger — any
   positive-Cauchy-then-class-control route is confined to q^{3m/2+k} — is
   correct and I adopt it; combined with Claim 1 it retires the last
   variance-flavoured shortcut. My Round-8 §6.1 "double dispersion with
   exact reciprocity" survives only in its centred bilateral (CBEA) form,
   which is what the branch has now made precise.

## 4. New structural results from this audit

### 4.1 (verification strength) The transfer step as a multiset identity

The audit verifies the Route A transfer in a form stronger than the mass
inequality: sampled-frequency counts are constant on every projective line
and realize the occupancy multiset exactly. Any future refinement (e.g.
θ-restricted sampling, other punctures with unit values) can reuse this
combinatorial skeleton unchanged.

### 4.2 Lemma R11-L1 (proved): the resonant/transpose intersection is exactly k = 3

A resonant point has P′ = S iff 2P = (L − ε)Q iff P = L − ε and Q is the
constant 2 — forcing k = 3 (and then S′ = P automatically, with P = t³−t−ε
the two Artin–Schreier cubics). Similarly P′ = P and S′ = S are impossible
(they force L | P), and S = P′ reduces to the same equation as P′ = S. Hence:
**for k ≥ 4 all four primes of a resonant point are pairwise distinct, and
the resonant family is disjoint from the diagonal and transpose strata; at
k = 3 it lies entirely inside the transpose stratum.** (Machine check: 0/2
four-distinct at k = 3; 12/12 and 72/72 at k = 4, 5.) For Gate 2 this means
the transpose stratum can be split off cleanly with no double-counting
against the resonant component except in the single case (q, k) = (3, 3).

### 4.3 Probe: the involution invariance is product-level only

For the resonant points, factorwise equality Â_{P′}(μ′) = Â_P(μ) fails for
12/12 points at k = 4 (conjugate-factorwise holds for only 48/72 at k = 5),
while the product identity X_a = X_b holds for all 84. So the invariance is
a genuine coupling of the two local factors, not a per-modulus symmetry.
Consequence for the branch's open item "general proof of involution
invariance": modulus-by-modulus arguments (Frobenius/affine transport on a
single Â) cannot prove it; the natural candidates are (i) the exact
residue-sum reciprocity on θf/(LSP)-type kernels, which couples the P- and
S-factors by construction, or (ii) a direct identity on the Gram pairing.
This is also mild evidence that the eventual centred bilateral identity will
see the resonant component as a single coupled object rather than through
its factors.

## 5. Assessment of the stopping point

The four-step "next new mathematics" list (decompose the coefficient scheme
with same-modulus strata separate; uniform corrected-amplitude bound on the
resonant graph; exact centred bilateral identity before positivity; residual
bilinear/sheaf estimate) is, in my judgment, correctly ordered and correctly
scoped — with Lemma R11-L1 slotting into step 1 and the product-level
constraint of §4.3 into steps 2–3. One cheap next measurement worth taking
before step 2: extend the Δ panel to k = 6 (192 points, ~16k sources —
feasible) to test whether the corrected ratio BB/3^{2m+3k} stays at the
~10⁻⁴ plateau seen at k = 4, 5 or resumes the 3^{−k} decay; the two
behaviours point to different uniform-bound targets in Gate 3.

## 6. Boundary

| Status | Item |
|---|---|
| **VERIFIED (this audit, exact)** | PO2 and its occupancy split (q ≤ 11); the sampled-line transfer multiset identity; V_all = G + q⁴/(q²−1); all seven M_samp panels; M_full panels and the exact inequality (q ≤ 7); PRC1 identities and counts (k ≤ 5, both θ); completeness of the family at (3,4); the (5,3) diagonal collapse; the (3,3) transpose pair; Δ-panel invariance and all aggregates (k ≤ 5); IFA1 equivalence + uniqueness on five panels; the resonant witnesses (c, d). |
| **PROVED (this audit)** | Lemma R11-L1 (resonant ∩ transpose = k = 3 exactly; four-distinctness for k ≥ 4). |
| **EMPIRICAL (this audit)** | Product-level-only involution invariance (factorwise fails). |
| **ACCEPTED CORRECTIONS** | Δ_PS omission in my Round-8 verifier; C ≤ Diag as finite-panel; Plancherel-mass wording; the diagonal-floor ledger. |
| **OPEN (unchanged, concurring with the branch)** | Gates 2–6: coefficient-scheme decomposition; uniform corrected resonant amplitude; centred bilateral identity (CBEA_FF); residual bilinear/sheaf estimate; corrected endpoint FFPR; PORC_FF; FF first-band theorem; every integer interface; Fortune. |
