# The exact class correlation C(θ) for the primorial puncture: an exact
# positive integer main term, and the self-referential frequency mechanism

Contributor: Claude (PR #33 thread; the requested exact computation of C(θ)
for 𝔏 = t^q − t — the next gate named in `FFPR_DISPERSION_NOTE_20260731.md` §5)
Date: 2026-07-31
Machine verification: `fortune-review/scripts/ff_class_correlation_exact.py`
(exact arithmetic in Z[ζ_q]; no floating point in any verified statement),
output archived at `fortune-review/data/ff_class_correlation_exact.txt`.

## 0. Outcome in one paragraph

C(θ) is computed exactly at the endpoint configuration (k = 2, m = 3, R = 3,
θ ∈ F_q^*) for q = 3, 5, 7. **The primorial's class correlation is an exact
positive rational integer, independent of θ**: C(θ) = 216, 7250, 67571
against diagonal mass 216, 10500, 148176 (ratios +1.0000, +0.6905, +0.4560).
The mechanism is identified and proved: for 𝔏 = t^q − t and deg P = 2,
**𝔏 ≡ −P′(t) (mod P)** — the primorial replaces the puncture by the modulus's
own derivative, so the sampled frequency is self-referential and the puncture
disappears from the analysis entirely. At q = 3, 5 a stronger per-class exact
law holds (every class term equals |Â_P(μ₁)|² exactly, making C(θ) a sub-sum
of the diagonal); at q = 7 that per-class law fails (294 of 672 classes)
while the aggregate integrality, positivity and θ-independence persist — the
identity is aggregate, not termwise, in general. Consequence for the
dispersion route: 𝔇_primorial = q^m·(Diag + C(θ)) with 0 < C(θ) < Diag
throughout the verified range, so the primorial's second moment is within a
factor 2 of the fixed-puncture value and Theorem D3's order is unchanged —
the located puncture-uniformity risk is resolved, in range, into an exact
bounded main term rather than a failure of cancellation.

## 1. The exact values

Everything below is an identity in Z[ζ_q] (Λ is integer-valued, phases are
q-th roots of unity); the archived output prints exact coefficient vectors.

| q | DiagMass | C(θ) | C/Diag | classes per θ | pairs with a partner | max partners |
|---|---|---|---|---|---|---|
| 3 | 216 | **216** | +1.0000 | 6 | 6/6 | 1 |
| 5 | 10500 | **7250** | +0.6905 | 60 | 60/90 | 1 |
| 7 | 148176 | **67571** | +0.4560 | 672 | 399/420 | 3 |

Machine-verified for every θ ∈ F_q^*: C(θ) is the same exact element for all
θ; it is real and a rational integer; the class set is θ-independent. The
control puncture t(t+1) behaves oppositely: C(θ) is tiny, irrational, and
genuinely θ-dependent (q = 5: C = −50(1+ζ²+ζ³) ≈ +30.9 vs diagonal ≈ 10⁴).

The q = 3 saturation C = Diag is now explained exactly: every pair has
exactly one partner and every class term equals |Â_P(μ₁)|² (below), so the
class sum reproduces the diagonal verbatim.

## 2. Theorem C2 (proved): trace-zero — the Artin–Schreier source

For 𝔏 = t^q − t = ℘(t) and any α ∈ F_{q²}: Tr_{F_{q²}/F_q}(𝔏(α)) =
(α^q − α) + (α^q − α)^q = α^{q²} − α = 0. Moreover 𝔏(α)^q = −𝔏(α): the
values of the primorial on the band lie on the **anti-invariant line**
{w ∈ F_{q²} : w^q = −w} = 𝔏(α)·F_q. (Machine check: all band primes,
q = 3, 5, 7; control traces generically nonzero.)

## 3. Theorem C3 (proved): the self-referential frequency

For every irreducible P = t² + b t + c over F_q:

    t^q ≡ −b − t (mod P),   hence   𝔏 = t^q − t ≡ −(2t + b) = −P′(t) (mod P).

Proof: both sides of the first congruence have degree ≤ 1 and agree at the
two roots β, β^q of P (β^q = −b − β since β + β^q = −b, and (β^q)^q = β). ∎
(Machine check: exact for all band P, q = 3, 5, 7.)

Corollaries. (i) μ₁ = −θ·𝔏̄_P·S̄_P = θ·(P′S)⁻¹ mod P and ν₂ = θ·(S′P)⁻¹
mod S (S′ = dS/dt): **the primorial replaces the puncture with the modulus's
own derivative** — the FF form of "the primorial is built from the same
primes as the modulus family," and the exact reason t^q − t resonates where
a fixed puncture oscillates. (ii) Since 𝔏(β)·P′(β) = −(β − β^q)² =
−disc(P) ∈ F_q^*, the effective frequency in the residue-formula coordinates
is ω = θ/(disc(P)·S(β)): **the puncture is eliminated from the primorial
analysis entirely** — at the endpoint laboratory the true-primorial case is
structurally simpler than a generic puncture, not harder. (iii) Honesty
note: this collapse is special to k = 2 (t^q mod P is linear only for
deg P ≤ 2); at k ≥ 3 the congruence 𝔏 ≡ −P′ fails and the resonance
question reopens — the k ≥ 3 analogue is an explicit open item.

## 4. Theorem C5 (proved): the class-existence trace criterion

Fix (P, S) and a candidate S′ (all distinct band primes). The one-sided
coincidence — E₁ := ν₂S′ mod S is a nonzero scalar, equivalently
S′ ≡ c·𝔏P (mod S) for some c ∈ F_q^* — holds **iff**

    Tr_{F_{q²}/F_q}( S′(α_S) · P(α_S^q) ) = 0,

where α_S is a root of S. Proof: S′ ≡ c𝔏P gives S′(α)P(α^q) =
c·𝔏(α)·N(P(α)) with N(P(α)) ∈ F_q, and Tr(𝔏(α)·F_q) = 0 by C2. Conversely
if w := S′(α)P(α^q) has Tr(w) = 0 then w lies on the anti-invariant line
𝔏(α)F_q (1-dimensional, contains 𝔏(α) ≠ 0), and dividing back out gives the
congruence. ∎ (Machine check: exact equivalence over all triples, q = 3, 5, 7.)
A full class needs in addition the symmetric scalar E₂ = −ν₂′S mod S′ with
E₁ = E₂ (then ν₂S′ − ν₂′S ≡ E₁ mod SS′ with degree ≤ 3 < 4 forces the exact
polynomial identity). Counts (per θ): one-sided 6, 120, 1092 → full classes
6, 60, 672 at q = 3, 5, 7. Since the one-sided residues form the line
c·(𝔏P mod S), c ∈ F_q^*, each pair has ≤ q − 1 candidates; the classes are
exactly the primes on a translated line — the thin family is now explicitly
parametrized with no reference to the puncture (𝔏 ≡ −S′_derivative mod S).

## 5. The per-class law (exact at q = 3, 5; aggregate-only at q = 7)

At q = 3 and q = 5, for **every** class ((P,S) → (P′,S′)) and every θ:

    ζ^E · Â_P(μ₁) · conj(Â_{P′}(μ₁′)) = |Â_P(μ₁)|²   exactly,

equivalently Â_{P′}(μ₁′) = ζ^E·Â_P(μ₁) — including the cross-modulus classes
(40 of 60 at q = 5 have P′ ≠ P). Hence there C(θ) is a **sub-sum of the
diagonal**: C = Σ_{classed pairs} |Â_P(μ₁)|², manifestly positive.

At q = 7 this per-class law **fails**: it holds for 294 of 672 classes per θ
(all 84 same-P classes fail; exactly half of the 588 cross-P classes hold),
with failing terms still exact algebraic integers (e.g. −q^m·ζ). Yet the
aggregate C(θ) remains an exact positive rational integer. The correct
general statement is therefore aggregate: the class terms conspire to an
integer, not term-by-term to diagonal terms. Classifying the q = 7 orbit
structure (which classes carry which root-of-unity defects, and why they
cancel) is the identified next algebraic question.

## 6. Lemma C6 (proved): Galois covariance, and why C(θ) is rational

For σ_s : ζ → ζ^s (s ∈ F_q^*, Gal(Q(ζ_q)/Q)): **σ_s(C(θ)) = C(sθ)**.
Proof: every phase entering C(θ) — the class constant ζ^E and every source
phase in Â_P(μ₁), Â_{P′}(μ₁′) — has exponent F_q-linear in θ (E, μ₁, μ₁′
are all linear in θ), and θ → sθ maps the class family bijectively to
itself. ∎ (Machine check: exact for both punctures, including the control at
q = 5, where C(θ) is irrational and the covariance is nontrivial:
σ₂C(1) = C(2).) Combined with the verified θ-independence for t^q − t, this
forces C(θ) ∈ Q ∩ Z[ζ_q] = Z: **rationality is proved modulo
θ-independence, which is machine-verified exactly in range** (and is the
one remaining unproved input to integrality).

## 7. Consequence for the dispersion programme

The Round-8 second moment now reads, for the true primorial, exactly:

    𝔇 = q^m·( DiagMass + C(θ) ),      0 < C(θ) < DiagMass  (verified range),

so 𝔇_{t^q−t} ≤ 2·q^m·DiagMass: **the primorial's pair-family second moment
is within a factor 2 of the fixed-puncture value, uniformly in θ** — with
the factor an exact, decreasing ratio (1 → 0.69 → 0.46 for q = 3 → 5 → 7).
Theorem D3's conditional bound and its ledger (gain q^{(2k−m)/2}, endpoint
deficit q^{(m−k)/2}) therefore apply verbatim to 𝔏 = t^q − t. The recurring
programme lesson ("a non-oscillating piece must be treated as a main term")
is fulfilled in the strongest possible way here: at the level of the second
moment nothing needs to be subtracted — the class mass is absorbed into a
constant ≤ 2 — and the puncture-uniformity risk flagged in Round 8 is, at
the endpoint laboratory, resolved into exact bounded structure. What
survives as risk is precisely: (a) proving C(θ) ≤ DiagMass (or the observed
decay of C/Diag) for all q, now a clean self-contained question about primes
on the explicit lines of §4 with self-referential frequencies; and (b) the
k ≥ 3 analogue, where the C3 collapse is unavailable.

## 8. Boundary

| Status | Item |
|---|---|
| **PROVED** | C2 (trace-zero; anti-invariant line); C3 (𝔏 ≡ −P′ mod P; self-referential frequency; puncture elimination at k = 2); C5 (trace criterion for class existence; classes = primes on explicit ≤(q−1)-point lines); C6 (Galois covariance σ_sC(θ) = C(sθ)); rationality of C(θ) given θ-independence; C1 (class constant ζ^E — machine identity, all classes). |
| **EMPIRICAL-EXACT** (machine identities in Z[ζ_q], q = 3, 5, 7, all θ) | C(θ) = 216, 7250, 67571 — positive rational integers; θ-independence; C/Diag = 1, 0.6905, 0.4560; per-class law at q = 3, 5; its aggregate-only form at q = 7 (294/672); partner statistics. |
| **OPEN** | θ-independence as a theorem (would complete integrality); per-class-law classification at general q (the q = 7 defect orbits); C(θ) ≤ Diag (or C/Diag decay) for all q; the k ≥ 3 primorial resonance (no C3 collapse); the endpoint deficit q^{(k−1)/2} (double dispersion with exact reciprocity); FFV-generic; FFPR at m = 2k−1; thinning; PORC_FF; FF first-band theorem; integer transfer. |
