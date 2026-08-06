# Round 14 audit: the local geometry is a q-free relaxation — its dimension
# does not control the incidence count, and the census stays authoritative

Reviewer: Claude (continuation of the PR #33 independent review)
Date: 2026-08-03
Audited state: branch `gpt56/fortune-mesoscopic-cotlar-20260728`, head
`2983ae1` (root-cycle system, oriented-coefficient reduction, rank data,
formal jet, Singular/msolve infrastructure, QZD_3 verdict).
Independent audit artifacts: `fortune-review/scripts/ff_round14_qfree_audit.py`
with archived outputs `fortune-review/data/ff_round14_*.txt`.

## 1. Executive verdict

The committed formulations are correct and I verified them independently:
the N_F interpolation identity symbolically over ℚ, the canonical (11,3)
point, Jacobian rank 16 (my own linear algebra), and the orientation
invariant at the canonical point. But the round's *inference* — "tangent
dimension 1 ⟹ QZD_3 strongly disfavoured ⟹ incidences potentially q³-scale"
— does not survive scrutiny, for a structural reason the audit pins down and
then quantifies by direct measurement:

**The normalized systems are q-free relaxations.** They contain no q-th
powers (max total degree 4; the oriented-coefficient system is literally
built once over ℚ and only reduced mod q — one variety V for all odd q,
which is also why the rank defect "replicates structurally" at q = 11, 17,
19: it is the same variety each time). The relaxation keeps only the
L-*value* consequence of the Frobenius cycle (L(x_i) = x_{i+1} − x_i as a
cyclic difference) and drops the arithmetic condition that the ordering *is*
the Frobenius cycle. Membership of an incidence in V is exact; the converse
fails: V carries degenerate, split, and — critically — *orientation-
spurious* points (all four cubics irreducible but some η equal to the
anti-Frobenius square root). The true incidences are the V(F_q)-points
satisfying a twisted-Frobenius orientation condition that is **not Zariski
on V**, so no tangent/jet/dimension computation on V can see it.

## 2. The measurements (all exact, complete enumerations)

Complete point counts of V(F_q) via the interpolation-correspondence
parametrization (A-block, B-block, ρ free; C, D unique monic lifts; η_C, η_D
solved from the residual linear systems) — something the Gröbner runs could
not deliver but 20 seconds of enumeration can:

| q | #V(F_q) total | degenerate | split-spurious | irreducible nondegen. | of which TRUE incidences | orientation-spurious |
|---|---:|---:|---:|---:|---:|---:|
| 11 | 12,261 | 8,800 | 3,457 | 4 | **2** (ρ = 7, 8) | 2 |
| 13 | 20,857 | 14,976 | 5,873 | 8 | **0** | 8 |
| 17 | 47,823 | 34,816 | 12,985 | 22 | **2** (ρ = 8, 15) | 20 |

The TRUE column equals the census exactly (incidences/q(q−1) = 2, 0, 2 —
including the q = 13 absence), and the ρ-values are the known orbit
invariants: a complete cross-validation of Round 13 from a different
direction. The orientation invariant η_Aη_D = η_Bη_C holds on only about
half of V(F_q) (6585/12261 at q = 11) — it is a component separator, not an
identity of V, consistent with the branch's syzygy reading on the open
locus. (A first version of my classifier omitted the degeneracy exclusions
and "found" 6402 true points at q = 11 — the diagonal A = B = C = D, where
all four true divisibilities degenerate to 0 ≡ 0. Recorded as a warning:
the diagonal is a fat trivial component of V and of every relaxed test.)

**The k = 2 exhibit (new, decisive as a matter of logic).** The quadratic
analogue is η-free (the cyclic difference is rational: N_F = −2t − A), giving
a tiny q-uniform system. Its variety V₂ is *not* empty over ℚ̄ (nontrivial
Gröbner basis), and its F_p-point count is exactly p² + 2(p − 2) on every
panel p = 5..23 — a two-dimensional degenerate component plus a
one-dimensional split family (exactly p − 2 points) — **with zero true
points at every p**, matching my Round-13 census (empty through q = 53).
So: a q-free relaxation with components of dimension 1 and 2 whose
arithmetic content is nothing at all. Positive relaxation dimension is
compatible with a permanently empty incidence census.

## 3. What this does to the Round-14 verdict

1. **"QZD_3 strongly disfavoured" — assessment corrected.** The evidence
   (rank defect 1, structural replication, 10,000-order jet) is evidence
   about V, and I confirm it is real (the jet varies ρ, the orbit
   invariant, so it is not a group direction — I checked that both group
   actions are already gauge-fixed: translations by Σroots = 0, homothety by
   λ = 1). V plausibly does contain a curve through the canonical point —
   the linear growth of the orientation-spurious class (2, 8, 20 at
   q = 11, 13, 17) looks like that curve's rational points. But QZD_3 as a
   programme gate was about the *incidence count*, and the measured chain is:
   V's F_q-points ~ 10⁴ and growing; the curve's candidate points ~ linear;
   the TRUE incidences 0 or 2 — bounded, exactly as the census says.
   **dim V does not bound, and empirically does not track, the arithmetic
   count.**
2. **The q³ alarm is withdrawn as an inference, retained as an unproved
   possibility.** It would require the *true-point* count on the curve to
   grow linearly, which the data contradicts so far (0–6 orbits through
   q = 59, against orientation-spurious growth). The k = 2 case shows the
   opposite extreme is realizable: positive-dimensional relaxation, zero
   arithmetic points forever.
3. **The correct next gate (replacing QZD_3).** The branch's own report
   names it when discussing the dim-1 contingency: a **twisted-Frobenius
   point theorem**. The audit shows it is needed *regardless* of dim V, and
   sharpens it: classify the V(F_q)-points by orientation type and bound the
   true-orientation class. Equivalently: the arithmetic incidences are the
   fixed points of a Frobenius-twisted structure on V's components, and the
   census (now cross-validated three ways) says their number per q is tiny.
   Proving that — even just "true points = O_k(1) orbits per q on the
   nonzero-defect components" — is NDC_FF's honest core, and the Gröbner
   dimension certificate, while still worth having for V's component
   structure, no longer carries the decision.

## 4. What is verified and what stands

| Status | Item |
|---|---|
| **VERIFIED (this audit, exact)** | N_F identity symbolically over ℚ; canonical point and Jacobian rank 16 (independent linear algebra); orientation invariant at the point; q-freeness/q-uniformity of the system; complete V(F_q) enumerations at q = 11, 13, 17 with the stratification above; TRUE counts = census exactly (incl. the q = 13 zero); V₂ (k = 2): nonempty over ℚ̄, F_p-counts p² + 2(p−2), zero true points p ≤ 23 (census: ≤ 53). |
| **ACCEPTED (branch, confirmed in scope)** | Root-cycle and oriented-coefficient formulations; gauge; rank data; the formal jet as evidence about V; the refusal to promote incomplete Gröbner runs. |
| **CORRECTED (inference, not computation)** | "Tangent dim 1 disfavours QZD_3 as a programme gate": the relaxation's dimension neither bounds nor tracks the incidence count (k = 2 proof-by-example; k = 3 measured stratification). The q³ scale is a possibility, not a lean. |
| **OPEN** | V's actual component decomposition (the Gröbner/msolve certificate — still useful, now demoted from decisive); the twisted-Frobenius point theorem = the true-orientation count (the new decisive gate); the amplitude theory with Δ_PS; corrected CBI_FF; endpoint FFPR; integer interfaces; Fortune. |

## 5. Recommended next computation

Enumerate the orientation-spurious class at more q (cheap with the
correspondence) to pin its growth law — if it is exactly linear with a
stable constant, V's curve component is confirmed *and* measured without
any Gröbner computation, and the separation "curve points ≈ spurious;
true points ≈ census" becomes the precise statement of the twisted-point
theorem to prove. In parallel, the k = 2 emptiness (all q) now looks
provable by hand from the η-free system — four rational equations whose
solution set visibly consists of the degenerate and split families; a
proof would be the first complete NDC-type existence theorem and a
template for k = 3.
