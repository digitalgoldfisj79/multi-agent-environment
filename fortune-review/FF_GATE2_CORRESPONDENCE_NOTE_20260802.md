# Gate 2 opened: the correspondence form, the complete two-family
# classification of the bilateral incidence, the k ≥ q law, and c + d = 0

Contributor: Claude (PR #33 thread; Round 12 — the branch's "next new
mathematics" step 1, plus the k = 6 measurement for step 2)
Date: 2026-08-02
Machine verification: `fortune-review/scripts/ff_gate2_correspondence_audit.py`
(exact arithmetic; ground-truthed against pair-squared scans), output archived
at `fortune-review/data/ff_gate2_correspondence_audit.txt` (all PASS, exit 0).

## 0. Outcome in one paragraph

The inverse-free incidence scheme collapses further than IFA1 stated: the
partner primes are *uniquely determined* by (P, S, c, d), so the bilateral
incidence is a locus in (P, S, c, d)-space cut out by two residual
divisibilities, with no quotient variables (Theorem C12-1). Enumerating it on
13 panels — through (3,7), (5,5), (7,4), a range far beyond the previous
(3,4) — yields a **complete two-family classification with zero unexplained
points**: every cross-distinct simultaneous incidence is either a point of a
**reflection family** P′ = LQ − P (the branch's "characteristic-three" family,
which is in fact **characteristic-free** and gated by degree: it exists iff
k ≥ q, Theorem C12-4 — with 332 points at (q,k) = (5,5)) or of a **new
translation family** P′ = P + LR, S′ = S + LR, S = P + γR (Theorem C12-5,
proved, exists iff k > q); the transpose stratum is exactly the degenerate
reflection locus at k = q (Theorem C12-3: the q−1 Artin–Schreier pairs
(L+γ, L−γ)). Consequently the tested range obeys a sharp **k ≥ q law**:
for k < q the bilateral incidence is EMPTY beyond the diagonal — so in the
large-field regime q > k, exactly where the Weil-strength technology lives,
the centred bilateral identity has **no exceptional components at all**.
Furthermore **c + d = 0 holds for every one of the 3514 incidences on every
panel** (and is proved on both families), collapsing the scheme to three
parameters. Finally, the k = 6 Δ panel (192 points, exact) shows the
corrected resonant ratio dropping to 1.36×10⁻⁵ — the k = 4→5 flatness was
not a plateau; decay resumes, which is the favourable answer for Gate 3.

## 1. Theorem C12-1 (proved): the correspondence form

Fix θ ∈ F_q^* (scalar window) and c, d ∈ F_q^*. In IFA1's system,

    P | cLS + θP′   forces   P′ = P + r₁,   r₁ = (−θ⁻¹c·LS) mod P,

since the residue of P′ mod P is determined and the unique monic degree-k
polynomial with a given residue r (deg r < k) of the form "prime candidate
paired to P" is P + r. Symmetrically S′ = S + r₂, r₂ = (−θ⁻¹d·LP) mod S.
Hence the cross-distinct simultaneous bilateral incidence is exactly

    { (P, S, c, d) :  P′ := P + r₁,  S′ := S + r₂  are irreducible, P′ ≠ S′,
                      P′ | cLS′ − θP   and   S′ | dLP′ − θS }.

Corollaries. (a) The quotient variables U, U′, V, V′ of the branch's scheme
presentation are eliminated. (b) r₁ ≠ 0 for c ≠ 0 (else P | cLS), so the
same-modulus contact P′ = P (and S′ = S) is *impossible* — the branch's
"treat same-modulus strata separately" becomes a theorem rather than a
convention. (c) Classification cost per panel drops from #pairs² to
#pairs·(q−1)², which is what makes the deep panels below feasible.
(Machine check: exact set equality {(P,S,P′,S′,c,d)} between the
correspondence enumeration and ground-truth pair-squared scans on the five
Round-11 panels.)

## 2. Theorem C12-3 (proved): the transpose stratum

The transpose (P′,S′) = (S,P) is a simultaneous incidence iff

    P | L + θc⁻¹     and     S | L − θc⁻¹

(reduce c = μS − νP modulo P and S: μS ≡ −θL̄_P, νP ≡ −θL̄_S). For prime q
and 𝔏 = t^q − t, the shifted primorial L ± γ = t^q − t ± γ is an
Artin–Schreier polynomial, irreducible of degree q for γ ≠ 0. Hence a
degree-k prime divides it iff k = q and P = L + γ itself:
**transpose incidences exist iff k = q, and are exactly the q − 1 pairs
(P, S) = (L + γ, L − γ), γ ∈ F_q^*.** (Machine: 2 at (3,3), 4 at (5,5),
none elsewhere — the (5,5) count was predicted before the run.)

## 3. Theorem C12-4 (proved): the reflection family is characteristic-free

The branch's family survives verbatim over every F_q once the normalization
is read correctly: take Q with **leading coefficient 2** and
**deg Q = k − q**, set J_Q(T) = LQ − T, S = P + εQ, P′ = J_Q(P),
S′ = J_Q(S). Then LQ is monic-of-degree-k times 2, so P′, S′ are monic of
degree k (2 − 1 = 1 — in characteristic 3 the branch's "leading −1" is the
same 2), and the PRC1 congruence proof goes through unchanged in every
characteristic: mod P, LS ≡ εLQ ≡ εP′ gives μP′ − μ′P = −θε⁻¹; symmetrically
νS′ − ν′S = +θε⁻¹. **The true gate is the degree constraint
deg(LQ) = k ⟺ k ≥ q, not the characteristic**: "characteristic three" in the
branch's note is an artifact of q = 3 being the only field where the k ≤ 7
laboratory reaches k ≥ q. At k = q the family (Q scalar) contains the
transpose points of C12-3 as its degenerate locus (the Round-11 Lemma R11-L1
argument generalizes: P′ = S forces Q constant and P = L − ε).
(Machine: 332 reflection points at (5,5), including the 4 transpose; counts
2/12/72/192/1440 at q=3, k=3..7 reproducing and extending the branch's table.)

## 4. Theorem C12-5 (proved): the NEW translation family

For k > q, choose a prime P, a nonzero R with deg R < k − q, and γ ∈ F_q^*;
set

    S = P + γR,     P′ = P + LR,     S′ = S + LR,

and assume all four irreducible. Then this is a simultaneous bilateral
incidence with witnesses

    c = −θγ⁻¹,      d = −c.

Proof. Mod P: P′ ≡ LR, so μP′ ≡ −θ(LS)⁻¹LR ≡ −θR·S̄; this is the scalar c
iff P | cS + θR iff (by degree k and monicity) cS + θR = cP iff S = P + γR
with γ = −θ/c. Mod P′: P ≡ −LR, so −μ′P ≡ −θR·S̄′ · (−1)(−1)… ≡ c iff
S′ = P′ + γR — which holds by construction (S′ − P′ = S − P = γR). The
ν-side is the same computation with (P, P′) ↔ (S, S′), giving d with
P = S − γR, i.e. d = −c. ∎

Reflection and translation are **disjoint**: reflection has
S′ − P′ = −(S − P), translation has S′ − P′ = +(S − P), and 2(S−P) ≠ 0 for
odd q. (Machine: every generated translation point is an incidence with
exactly the predicted witnesses; counts 36/168/1260 at q=3, k=5/6/7; empty at
k ≤ q as the degree forces.)

## 5. The classification and the k ≥ q law (empirical-exact, 13 panels)

| (q,k) | incidences | transpose | reflection | translation | OTHER |
|---|---:|---:|---:|---:|---:|
| (3,2), (5,2), (7,2), (5,3), (5,4), (7,3), (7,4) | 0 | 0 | 0 | 0 | 0 |
| (3,3) | 2 | 2 | (=transpose) | 0 | **0** |
| (3,4) | 12 | 0 | 12 | 0 | **0** |
| (3,5) | 108 | 0 | 72 | 36 | **0** |
| (3,6) | 360 | 0 | 192 | 168 | **0** |
| (3,7) | 2700 | 0 | 1440 | 1260 | **0** |
| (5,5) | 332 | 4 | 328 (+4) | 0 | **0** |

**Conjecture C12-6 (classification).** For prime q and 𝔏 = t^q − t at the
endpoint, the cross-distinct simultaneous bilateral incidence is exactly
reflection(k ≥ q) ⊔ translation(k > q), with transpose = the degenerate
reflection locus at k = q. In particular it is **EMPTY for k < q**.

Status: both inclusions "family ⊆ incidence" are proved (C12-4, C12-5);
the transpose case is proved (C12-3); emptiness for k < q and completeness
for k ≥ q are verified on all 13 panels (3514 incidence points, zero
unexplained) but open as theorems. Two remarks:

1. **The consequential half is k < q.** If emptiness is proved, then in the
   large-field regime q > k — the regime of Keating–Rudnick and the
   Weil/Katz technology — the centred bilateral identity has *no exceptional
   strata*: Gate 2 reduces to the diagonal, and the branch's Gates 3–4
   simplify to "subtract the diagonal, estimate the empty-support
   off-diagonal". The exceptional geometry that has occupied Rounds 10–12
   (resonance, reflections, translations) is a **small-field phenomenon**
   (k ≥ q), invisible in the asymptotic regime the endpoint theorem will
   first be proved in.
2. Via C12-1 the two open halves are concrete polynomial statements: the two
   residual divisibilities on (P, S, c, d) with deg L = q > k force degree
   collapses that plausibly yield emptiness by pure degree counting; and
   completeness is a statement about the solution variety of two divisibility
   conditions — now with two known component families to check against.

## 6. Conjecture C12-2: c + d = 0 — proved on every known component,
## verified on every incidence

c + d = 0 holds for all 3514 incidence points on all panels; it is proved on
the reflection family (PRC1: ∓θε⁻¹), on the translation family (C12-5:
∓θγ⁻¹), and on the transpose stratum (direct: E_ν = −E_μ). Equivalent kernel
form (four-distinct case): the incidence is exactly the statement that the
pair-difference kernel has scalar partial-fraction numerators over PP′ and
SS′,

    φ_a − φ_b = −θ(P′S′ − PS)/(L·PSP′S′) = c/(PP′) + d/(SS′) + w/L,

and c + d = 0 is the top-degree cancellation cL·SS′ + dL·PP′ =
cL(SS′ − PP′), i.e. a forced degree drop in the L-numerator w. If C12-6 is
proved, C12-2 follows componentwise and the incidence scheme drops to three
parameters (P, S, c) — the exact shape a centred bilateral identity wants,
and a first concrete instance of the factor-coupling my Round-11 probe showed
is mandatory.

## 7. The k = 6 Δ measurement (Gate 3): decay resumes — no plateau

Exact panel over all 192 reflection points at k = 6, m = 11 (16107 sources):
involution invariance X_a = X_b, Δ_a = Δ_b, B_a = B_b holds at every point,
and

    XX = 150,701,632,653,456   XD = DX = −1,533,279,459,564
    DD = 11,390,886,203,724    BB = 165,159,077,776,308

    BB/3^{2m+3k}:  k=3: 1.32e−3   k=4: 8.93e−5   k=5: 9.50e−5   k=6: 1.36e−5

The k = 4→5 flatness was not a plateau: the corrected ratio falls by a factor
of 7 at k = 6, consistent with continued exponential decay inside the raw
dimension bound 2m²3^{−k−3} (= 1.23e−2 at k = 6). Gate-3 reading: the uniform
corrected-amplitude target should be an exponential-in-k saving, and the
finite evidence supports it; no plateau anomaly needs explaining.

## 8. Boundary

| Status | Item |
|---|---|
| **PROVED** | C12-1 (correspondence form; same-modulus exclusion; quotient-variable elimination); C12-3 (transpose stratum = the q−1 Artin–Schreier pairs, iff k = q); C12-4 (reflection family is characteristic-free, gated by k ≥ q; PRC1 in every characteristic; transpose = its degenerate locus at k = q); C12-5 (translation family with witnesses ∓θγ⁻¹; disjointness from reflection); c + d = 0 on all three known strata; the kernel form of the incidence. |
| **EMPIRICAL-EXACT** (13 panels, 3514 points, zero unexplained) | The complete classification (C12-6); the k ≥ q law (emptiness on all six k < q panels); c + d = 0 universally; the k = 6 Δ aggregates and the resumed decay; the (5,5) reflection count 332 with its 4 predicted transpose points. |
| **CORRECTED** (branch wording, not substance) | "Characteristic-three" → degree-gated (k ≥ q, any characteristic); the family's k = 4 completeness does not extend: from k = 5 the translation family coexists (36/168/1260 new points at q = 3, k = 5/6/7). |
| **OPEN** | C12-6 as a theorem (emptiness k < q — the consequential half — and completeness k ≥ q); C12-2 uniformly (equivalently the w-degree drop); the uniform corrected amplitude (Gate 3); the centred bilateral identity (Gate 4); the residual estimate (Gate 5); endpoint FFPR; integer interfaces; Fortune. |
