# The k = 2 emptiness theorem, completed: for every odd q there is no
# cross-distinct bilateral endpoint incidence at k = 2

Contributor: Claude (PR #33 thread; Round 15 — completing the branch's
mid-certificate stopping point)
Date: 2026-08-03
Status: **THEOREM** (joint: the branch's reduction and component analysis +
this round's characteristic-uniform certificates). All computations
re-executed and verified in this round; artifacts in
`fortune-review/scripts/ff_round15_k2/` (all Singular sources and the
exact lift verifier) with the run log in
`fortune-review/data/ff_round15_k2_certificates.txt`.

## 0. Statement

**Theorem (k = 2 emptiness).** For every odd prime power q, there is no
cross-distinct simultaneous bilateral endpoint incidence at modulus degree
k = 2 (θ scalar; equivalently, the nonzero-defect quadratic locus of NDC_FF
is empty, in every odd characteristic).

This is the first complete NDC-type existence theorem, it converts my
Round-13 census observation (empty through q = 53) into a law, and it is the
template result for the cubic problem.

## 1. Proof architecture and the division of labour

1. **(Branch, Round 13 — proved.)** For q = 3 (the strip k < q < 2k) the
   incidence is empty by the defect dichotomy. For q ≥ 5 every k = 2
   incidence would be nonzero-defect.
2. **(Reduction — branch and me independently; exact agreement.)** A true
   incidence over F_q (odd), translation-normalized (P = t² + A) and
   homothety-normalized (λ = 1), satisfies the q-free model: for an
   irreducible quadratic X, L ≡ N_X (mod X) exactly with N_X = −(2t + x₁),
   so the four divisibilities become four polynomial equations f₀..f₃ in
   (A, B, C, U), with P = t² + A, S = t² + Bt + C, U = ρ. Faithfulness is
   certified at the ideal level: my independently derived Round-14 model,
   transported to these coordinates, generates the SAME ideal as the
   branch's f₀..f₃ after inverting U (Singular: mutual reduction to zero
   against the two Rabinowitsch bases — `IDEALS_AGREE_ON_U_NONZERO`), and
   the open-locus solution sets coincide exactly at p = 5, 7, 11, 13.
3. **(Open conditions valid at every true incidence.)** U ≠ 0; A ≠ 0 (an
   irreducible P has P(0) ≠ 0); B² − 4C ≠ 0 (S separable); and P ≠ S gives
   B ≠ 0 **or** A − C ≠ 0 — the two localization charts. (B = 0 alone is
   legitimate — trace-zero irreducible S exists — which is exactly why a
   single chart does not suffice and the branch's two-chart design is
   right.)
4. **(Chart certificates — the previously missing step, now complete.)**
   Let T = (U − 1, B + 2, (A − C)² + 4A), the branch's admissible component.
   For each chart K = (f₀..f₃, z·U·A·(B²−4C)·X_chart − 1), X_chart ∈
   {B, A−C}:
   - **Characteristic 0:** reduce(T, std(K)) = (0,0,0) — membership over ℚ
     (the branch's own committed script, run to completion this round in
     seconds), with the explicit lift matrices M satisfying T = K·M —
     re-verified exactly by independent parsing and re-expansion in sympy
     (chart B: confirmed; chart X: confirmed by the exact dict-arithmetic verifier, plus mod-1009 and mod-10007 checks).
   - **Denominator inspection:** the prime support of every denominator in
     both lift matrices is {2, 3, 5, 7, 11, 31, 163}. Hence for every odd
     prime p outside {3, 5, 7, 11, 31, 163}, the identity T = K·M
     specializes mod p, giving membership in characteristic p.
   - **The exceptional primes:** direct mod-p certificates (same reduce
     computation in characteristic p) for p = 3, 5, 7, 11, 31, 163, both
     charts: all reduce to zero.
   Conclusion: **in every odd characteristic, every point of the open
   incidence locus satisfies U = 1, B = −2, (A − C)² + 4A = 0.**
5. **(The reducibility mechanism — hand algebra over ℤ[1/2].)** On T, with
   r = A − C: A = −r²/4, so disc(P) = −4A = r²; and B = −2 gives
   disc(S) = B² − 4C = 4 − 4C = 4 − 4A + 4r = (r + 2)². Both discriminants
   are squares in F_q, so P and S are **reducible** — contradicting the
   irreducibility of a true incidence. ∎

Steps 1–3 and the component identification are the branch's; the
faithfulness certification, the completed chart certificates with lift
verification, the denominator analysis, and the exceptional-prime
certificates are this round's. The mechanism (step 5) is the branch's
observation, given a 2-power-denominator hand proof here.

## 2. Round-trip audit notes

- The branch's `ff_k2_primary_decomposition.sing` reproduces NCOMP = 8
  (one 2-dimensional, six 1-dimensional, one 0-dimensional component),
  confirming the reported decomposition; the lex elimination gives DIM = 2
  for the full (unsaturated) ideal, consistent with my Round-14 measured
  p² + 2(p−2) point counts (2-dim degenerate + 1-dim split components).
- One discrepancy flagged, not load-bearing: `ff_k2_open_saturation.sing`
  prints radical(J_B-chart) = ⟨U−1⟩ only, which understates the chart locus
  (f₁ at U = 1 factors as 2B(A−C)(B+2), so the locus is strictly smaller
  than the hyperplane). The universal-localization certificates supersede
  this output; the branch may want to inspect that script's sat/radical
  chain.
- A syntax-broken intermediate Singular check in this round printed a
  vacuous "VERIFIED" once (error left the flag untouched); it was caught
  and discarded — the committed verification uses the corrected script and
  independent sympy re-expansion. Recorded per the usual discipline.

## 3. Consequences

1. **NDC_FF existence theory, k = 2: closed.** The quadratic nonzero-defect
   locus is empty for all odd q. Combined with Round 13 this makes the
   k = 2 story complete: diagonal rigidity for q = 3, emptiness for all
   q ≥ 5.
2. **Template for k = 3.** The proof shape — q-free model, saturation by
   open conditions valid at true incidences, component containment via
   ℚ-lift + denominator inspection + finitely many mod-p certificates,
   then an arithmetic-obstruction mechanism on the surviving component —
   is exactly what the cubic problem needs, with one substantive
   difference: at k = 3 the surviving components are NOT arithmetic-empty
   (the census's true points exist), so the mechanism step must become a
   *count* (the twisted-Frobenius point theorem of Rounds 13–14) rather
   than a contradiction. The k = 2 case pins the machinery; the k = 3 case
   will need the new arithmetic input.
3. The bilateral incidence at the endpoint is now fully understood for
   k = 2 (all q) and k ≥ q (all q, Round 13); what remains of NDC_FF is
   precisely 3 ≤ k < q with q ≥ 2k, governed by the defect h and, per
   Round 14, by twisted-point counts on the q-uniform relaxation
   components.

## 4. Boundary

| Status | Item |
|---|---|
| **THEOREM (this round completes it)** | k = 2 emptiness for every odd prime power q. |
| **VERIFIED (this audit)** | ℚ-certificates both charts (reduce = 0; lift identities re-expanded exactly); denominator prime support {2,3,5,7,11,31,163}; mod-p certificates at 3, 5, 7, 11, 31, 163 (both charts); ideal-level faithfulness (`IDEALS_AGREE_ON_U_NONZERO`); solution-set equality at p = 5..13; NCOMP = 8; the disc-square hand identities. |
| **FLAGGED** | The open-saturation script's radical printout (understates; superseded). |
| **OPEN** | The cubic (k = 3) twisted-Frobenius point theorem on the relaxation components — now the sole existence-side gate of NDC_FF; the amplitude theory with Δ_PS; corrected CBI_FF; endpoint FFPR; integer interfaces; Fortune. |
