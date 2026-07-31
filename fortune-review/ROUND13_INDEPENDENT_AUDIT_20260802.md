# Round 13 independent audit: the falsification is confirmed, my two
# extrapolations are retracted, and the defect dichotomy is verified

Reviewer: Claude (continuation of the PR #33 independent review)
Date: 2026-08-02
Audited state: branch `gpt56/fortune-mesoscopic-cotlar-20260728`, head
`170c8ae`: `FF_BILATERAL_DEFECT_DICHOTOMY_AND_ROUND12_CORRECTION_20260730.md`,
the preregistered programme and result notes, the counterexample verifier and
the C++ census. Independent audit artifacts (no shared code):
`fortune-review/scripts/ff_round13_independent_audit.py`, output archived at
`fortune-review/data/ff_round13_independent_audit.txt`.

## 1. Executive verdict, and the retraction

**The falsification is correct and I confirm it independently from the
original local-frequency definitions.** The quadruple
P = t³+4t²+1, S = t³+10t²+9t+1, P′ = t³+10t²+6t+7, S′ = t³+4t²+3t+10 over
F₁₁ consists of four distinct irreducible cubics; my own computation of
μ = −θ(LS)⁻¹ mod P etc. reproduces the branch's stated frequencies exactly
and gives

    μ_a P′ − μ_b P = 2,      ν_a S′ − ν_b S = 8,      c + d = 10 ≠ 0,

with common defect h = 2t⁵+5t⁴+6t²+6t+4 of degree 5 = q − 2k satisfying all
three BDD1 identities. This is a literal simultaneous endpoint incidence and
not an artifact of any enumerator.

**I therefore formally retract the two Round-12 extrapolations:**

1. **Conjecture C12-2** (c + d = 0 universally) — **false**.
2. **The emptiness half of Conjecture C12-6** (q > k ⟹ no cross-distinct
   incidence), and with it the Round-12 headline inference that "in the
   large-field regime the centred bilateral identity has no exceptional
   components" — **false**.

Both statements were carried in my boundary table as EMPIRICAL-EXACT /
OPEN-as-theorems, and the note said plainly that emptiness for k < q was
unproved; the discipline held at the label level. But the *headline* of my
Round-12 note and PR comment bet on the wrong side of the extrapolation, in
the exact way this programme's history warns against: all 13 of my panels
sat in what is now the proved-zero-defect region (q < 2k, plus the
accidentally-empty (7,2), (5,2), (7,3) low-degree-h panels), and I
generalized from a region where a degree obstruction forced the pattern into
the region q ≥ 2k where the new degree of freedom h lives. (11, 3) is the
first configuration my panels could not see, and it kills the shortcut. The
branch's diagnosis — "Round 12 completely classified the zero-defect
component and incorrectly extrapolated it into the nonzero-defect regime" —
is exactly right and I adopt it.

## 2. Verification of the new theorems

### Theorem BDD1 (common defect) — VALID, re-derived and machine-verified

I re-derived the full chain by hand: the scalar-free system (λ = −θ/c,
ρ = θ/d; AP = LS − λP′, BS = LP + ρS′, CP′ = LS′ + λP, DS′ = LP′ − ρS);
cross-contact impossibility for q > k (P = S′ forces P′ | L + λ, an
irreducible Artin–Schreier polynomial of degree q); the substitution giving
P | ρC − λB and S′ | ρC − λB; and the key expansions

    (ρC − λB)·P′S = (ρA − λD)·PS′ = L(ρSS′ − λPP′) + λρ(PS − P′S′),

which force the two defects equal (domain), give the product identity, and
give deg h ≤ q − 2k from deg(ρC − λB) ≤ q. All exact. Machine check: the
three identities verify on every audited incidence — the (11,3)
counterexample, all 20 translation-normalized (11,3) incidences, and (as
h = 0 instances) every reflection point at k = 4, 5 and every translation
point at k = 5, 6 from my Round-12 panels.

### Theorem BDD2 (zero-defect classification) — VALID, re-derived

h = 0 forces ρ = λ (leading coefficients), hence c + d = 0, C = B, A = D,
and AB·PS = (LS − λP′)(LP + λS′) reduces, via the h = 0 product identity, to
AB = L² − λ² = (L − λ)(L + λ). For λ ≠ 0 both factors are irreducible
Artin–Schreier polynomials of degree q, so by unique factorization
{A, B} = {L − λ, L + λ}; the case A = L − λ solves to exactly the
translation family and A = L + λ to exactly the reflection family. **My
Round-12 families are therefore not just examples but exactly the
zero-defect locus** — this upgrades my classification to a theorem on its
true domain and simultaneously explains why it could not extend past
q = 2k. The corollaries check: completeness proved for all k ≥ q; the strip
k < q < 2k proved empty (h forced zero, families impossible by degree, cross
contact impossible); the phase transition at q = 2k exactly located.

### The census — VERIFIED at k = 3 for all q ≤ 37, including the absences

My independent translation-normalized enumeration (count × q; translations
act freely for q ≠ 3; L reduced per prime by Frobenius square-and-multiply)
reproduces the branch's cubic census exactly on all ten rows
q = 5, 7, 11, 13, 17, 19, 23, 29, 31, 37 (0, 0, 220, 0, 544, 684, 0, 1624,
1860, 5328) — **including the nontrivial absences at q = 13 and 23**,
which are the strongest cross-implementation checks
(an off-by-anything bug would almost surely break an exact zero). At q = 11
the full structure verifies: 220 incidences = 2 free AGL(1,11)-orbits of
size 110; every incidence has h ≠ 0 with **deg h = 5 = q − 2k exactly**
(the bound is attained, never slack, on this panel); and the two orbits
carry d/c = 3 and 4 respectively — **reciprocal values mod 11**, i.e. the
two orbits are reversal-partners ((a,b) ↔ (b,a) maps d/c ↦ c/d). Rows
q = 41..59 of the census I did not independently re-run; they
are consistent with the exact orbit arithmetic (every count is a perfect
union of q(q−1)-orbits) and I treat them as the branch labels them:
empirical-exact finite panels from a machine-verified implementation.

### NEW: the quadratic defect locus is empty through q = 53

My audit adds a census the branch did not run: at k = 2 (where q ≥ 2k for
every odd q ≥ 5, so nonzero defect is *permitted* with room deg h ≤ q − 4),
the cross-distinct incidence is **empty for all q ≤ 53**. So the nonzero-
defect phenomenon does not merely switch on at q = 2k — at k = 2 it appears
never to switch on at all (through 53), and at k = 3 it skips q = 13 and 23.
NDC_FF
should therefore aim at stronger structure than a dimension bound: the
existence pattern itself (empty at k = 2; irregular at k = 3) suggests the
defect locus is governed by a finer arithmetic condition worth identifying
before estimating — e.g. whether the (P, S, c, d)-system with h ≠ 0 has a
rational parametrization whose prime-value conditions fail identically at
k = 2. Identifying that condition is my recommended first sub-step of
NDC_FF, alongside the branch's O_k(q²) target.

## 3. Continuity note

The defect polynomial h is the completion of the Round-12 kernel identity:
my §6 observed that the incidence is scalar partial-fraction numerators of
φ_a − φ_b with an L-numerator w, and that c + d = 0 is a degree drop in w.
BDD1 is the uniform, sharpened version (deg h ≤ q − 2k, uniqueness, the
exact product identity), and BDD2 shows the degree drop to *characterize*
the two families rather than merely accompany them. The Round-12
correspondence form, same-modulus exclusion, transpose classification, both
family inclusions and their disjointness were independently accepted by the
branch's audit; the falsified items are exactly the two extrapolations. The
adversarial loop worked as designed — in both directions, again.

## 4. Assessment of the corrected frontier

NDC_FF (classify/bound the nonzero-defect components for fixed k, q ≥ 2k,
retaining literal Δ_PS amplitudes) is the right next gate, and the chain
NDC_FF → corrected CBI_FF → FFPR → θ-restoration → conductor coupling →
thinning is the right order. Two calibrations from the audit data:

1. The finite-orbit pattern (2–6 orbits per prime through q = 59, sizes
   exactly q(q−1)) plus reversal-pairing supports the branch's "dimension
   zero after affine quotient" target; the O_k(q²) count would put the
   nonzero-defect mass at ~q² incidences against ~q^{2k} pairs — far inside
   the endpoint allowance *if* amplitudes behave, which is precisely what
   the retained Δ_PS clause guards.
2. The k = 2 emptiness and the q = 13, 23 absences mean NDC_FF plausibly
   splits into an existence theory (which (q, k) admit defects at all — an
   arithmetic question, maybe class-number or AS-descent flavoured) and an
   amplitude theory. The existence half looks like the cheaper theorem and
   would immediately sharpen the census into a law.

## 5. Boundary

| Status | Item |
|---|---|
| **VERIFIED (this audit, exact)** | The (11,3) counterexample from original definitions (frequencies, witnesses, defect, all BDD1 identities); BDD1/BDD2 re-derivations; h = 0 with c + d = 0 on all Round-12 reflection (k=4,5) and translation (k=5,6) points; the cubic census on all rows q ≤ 37 including the q = 13, 23 absences; the quadratic census empty through q = 53; the (11,3) orbit structure (2 × 110), deg h = q − 2k attained, reciprocal d/c orbit invariants. |
| **RETRACTED (mine)** | C12-2 (universal c + d = 0); the emptiness half of C12-6 and the "diagonal-only large-field identity" inference. The zero-defect halves of Round 12 stand, now as the branch's proved BDD2 classification. |
| **NEW (this audit)** | Quadratic defect census: empty through q = 41 (k = 2); the reversal-pairing of the (11,3) orbits; the recommendation to split NDC_FF into existence + amplitude theories. |
| **NOT INDEPENDENTLY RE-RUN** | Census rows q = 41..59 (accepted as labelled: machine-verified implementation, exact finite panels; all rows q ≤ 37 independently confirmed). |
| **OPEN (concurring)** | NDC_FF; corrected CBI_FF with explicit defect components; endpoint FFPR; θ-restoration; conductor coupling; thinning; every integer interface; Fortune. |
