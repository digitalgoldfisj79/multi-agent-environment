# θ-independence proved by affine symmetry, and the classification of the
# q = 7 defect orbits: C(θ) = q · (sum of Galois orbit-traces)

Contributor: Claude (PR #33 thread; delivers the two items requested after
`FF_CLASS_CORRELATION_EXACT_NOTE_20260731.md`: θ-independence as a theorem,
and the q = 7 defect-orbit classification)
Date: 2026-08-01
Machine verification: `fortune-review/scripts/ff_theta_defect_orbits_audit.py`
(exact Z[ζ_q] arithmetic throughout), output archived at
`fortune-review/data/ff_theta_defect_orbits_audit.txt`.

## 0. Outcome in one paragraph

Both items are delivered, by one mechanism. The primorial t^q − t is exactly
the polynomial cut out by the F_q-points of the affine line, so it is
**invariant under every translation t → t + a and covariant of weight 1 under
every scaling t → λt**; hence the affine group AGL(1,q) acts on the entire
endpoint configuration, Λ-equivariantly, rescaling θ. This proves
θ-independence of C(θ) and DiagMass (Theorem T1 — for **every** k at the
endpoint m = 2k−1, verified at k = 2 and k = 3), and yields the structure
theorem (T2): at fixed θ, translations preserve every class term, homotheties
act by the Galois automorphisms σ_λ, and the transpose acts by complex
conjugation — so C(θ) is a sum of Galois orbit-traces, hence a **rational
integer divisible by q, unconditionally** (the last empirical input to
integrality is eliminated). The q = 7 defects then classify completely: the
672 classes fall into **16 free AGL(1,7)-orbits of size 42**; law-status is
an orbit invariant; **7 law-orbits** (integer traces 6 × 2352, 1 × 1666,
total +15778) and **9 defect-orbits** (traces 3 × 343, 2 × (−49),
4 × (−1764), total −6125, including both same-P orbits), giving
C = 7·(15778 − 6125) = 7·9653 = 67571 exactly. The defect orbits carry
*negative* mass: the per-class-law failure at q = 7 is precisely what pulls
C/Diag down (1.000 → 0.690 → 0.456). Bonus k = 3 data: the primorial's
C/Diag is +0.163 against the control's +0.141 — without the k = 2 derivative
collapse the primorial is no longer exceptional, confirming the resonance is
derivative-driven.

## 1. Theorem T1 (proved): θ-independence

Let g = (λ, a) ∈ AGL(1,q) act on monic polynomials by T ↦ T_g =
λ^{−deg T}·T(λt + a). This is a Λ-preserving bijection of monic irreducibles
of each degree. The primorial inputs are the two identities (a, λ ∈ F_q):

    𝔏(t + a) = 𝔏(t),        𝔏(λt) = λ·𝔏(t),        𝔏 = t^q − t,

(immediate from 𝔏 = ∏_{c∈F_q}(t − c), the equation of A¹(F_q)). Then for
every pair (P, S) of band primes and every θ ∈ F_q^*, at the endpoint
m = 2k−1:

    Â_{P_g}( μ₁(θ; P_g, S_g) )  =  Â_P( μ₁(λθ; P, S) ),
    E(θ; g·(P,S,P′,S′))         =  λ·E(θ; (P,S,P′,S′)),

and the class set is g-stable. Hence term(θ; g·cls) = term(λθ; cls), and
summing over the bijection: **C(θ) = C(λθ) and Diag(θ) = Diag(λθ) for all
λ ∈ F_q^*** — i.e. both are independent of θ.

Proof of the A-covariance (general k). Let β be a root of P and β_g =
(β − a)/λ the corresponding root of P_g. Then P_g′(β_g) = λ^{1−k}P′(β),
S_g(β_g) = λ^{−k}S(β), and — the primorial step — 𝔏(β_g) =
((β−a)^q − (β−a))/λ = 𝔏(β)/λ. The source bijection f ↦ f_g has f_g(β_g) =
λ^{−m}f(β). By the residue formula, ψ_{P_g}(μ₁(θ)f_g) =
e_q(Tr(−θ f_g(β_g)/(𝔏 S_g P_g′)(β_g))) = e_q(Tr(−θ·λ^{2k−m}f(β)/(𝔏SP′)(β))),
and at m = 2k−1 the exponent is λ¹: the phase at (θ, g·config) equals the
phase at (λθ, config), for every source. Summing with the (integer, invariant)
Λ-weights gives the covariance. For E: evaluating the defining identity at a
root α of S, E = −θS′_partner(α)/(𝔏(α)P(α)), and the same weight count gives
λ·E. ∎

Remarks. (i) The proof needs only the affine symmetry of 𝔏 — not the k = 2
congruence 𝔏 ≡ −P′ (mod P) — so it holds for **all k** at the endpoint;
machine-verified at k = 2 (q = 3, 5, 7; every pair × every g) and k = 3.
(ii) At general m the same computation gives C(θ) = C(λ^{2k−m}θ): full
θ-independence whenever gcd(2k−m, q−1) = 1, and always at the endpoint.
(iii) The control t(t+1) satisfies neither identity, and its C(θ) is
genuinely θ-dependent — the symmetry is precisely primorial.

## 2. Theorem T2 (proved): the orbit-trace structure and integrality

Fix θ. Since every phase in a class term has exponent F_q-linear in θ,
σ_s(term(θ; cls)) = term(sθ; cls) (per-term θ-covariance; machine-verified).
Composing with T1:

1. **Translations preserve every class term**: term(θ; (1,a)·cls) =
   term(θ; cls).
2. **Homotheties act by Galois**: term(θ; (λ,0)·cls) = σ_λ(term(θ; cls)).
3. **The transpose** cls = ((P,S),(P′,S′)) ↦ ((P′,S′),(P,S)) is an involution
   of the class set with E ↦ −E and term ↦ conj(term) (so C(θ) is real).

Consequently C(θ) = Σ_orbits (orbit sum), and each orbit sum is
(#translations in the orbit)·Tr_{F/Q}(term of a representative) for the
appropriate fixed field F — a rational algebraic integer. Hence
**C(θ) ∈ Z unconditionally** (the previous note's remaining empirical input,
θ-independence, is no longer needed for integrality — and is itself now
proved). Moreover translations act freely on monic quadratics (t → t+a fixes
t² + bt + c only if 2a = 0), so at k = 2 every orbit has size divisible by q:
**q | C(θ) and q | DiagMass.** Verified: C = 216 = 3·72, 7250 = 5·1450,
67571 = 7·9653; Diag = 3·72, 5·2100, 7·21168. (All orbits in range are in
fact free of size q(q−1).)

## 3. The classification of the q = 7 defect orbits

At θ = 1 the 672 classes decompose into **16 free orbits of size 42 =
|AGL(1,7)|** (machine: orbit sums equal q·Tr(rep) exactly and total to C;
law-status, same-P status and the χ-signature below are constant on every
orbit). At q = 3, 5 there are 1 and 3 orbits, **all law-orbits** — which is
*why* the per-class law held there; the new phenomenon at q = 7 is the
appearance of defect orbits. The table (Tr = Tr_{Q(ζ₇)/Q}, exact integers;
χ-signature = Legendre symbols of the pairwise resultants in the order
(P,S), (P′,S′), (P,P′), (S,S′), (P,S′), (S,P′)):

| orbit | law | same-P | Tr(term) | Tr\|A\|² | transpose ↦ | χ-signature |
|---|---|---|---|---|---|---|
| 2, 5 (pair) | ✓ | – | 2352 | 2352 | each other | (−1,−1,1,−1,−1,−1) |
| 3 (self), 4, 6 (pair) | ✓ | – | 2352 | 2352 | see left | (−1,−1,−1,−1,1,1) |
| 7 (self) | ✓ | – | 2352 | 2352 | itself | (−1,−1,1,−1,1,1) |
| 13 (self) | ✓ | – | 1666 | 1666 | itself | (1,1,−1,1,−1,−1) |
| 0 (self), 1, 10 (pair) | ✗ | – | **343** | 2058, 2058, 1666 | see left | (1,1,−1,1,−1,−1) |
| 8, 9 (pair) | ✗ | – | **−49** | 1666 | each other | (1,1,−1,1,−1,−1) |
| 11 (self), 12 (self) | ✗ | – | **−1764** | 2352 | itself | (−1,−1,±1,−1,1,1) |
| 14, 15 (self) | ✗ | ✓ | **−1764** | 2352 | itself | (−1,−1,0,−1,−1,−1) |

    C(θ)/7 = [6·2352 + 1666] + [3·343 − 2·49 − 4·1764] = 15778 − 6125 = 9653.

Findings. (i) **The defect orbits carry negative integer mass** (−6125
against the law-orbits' +15778): the q = 7 law-failure is not noise but a
signed correction, and it is exactly what drives the observed decay of
C/Diag in q (1.000, 0.690, 0.456) — the two same-P orbits alone contribute
−2·1764. (ii) All four trace values are divisible by q² = 49
(2352 = 48·49, 1666 = 34·49, 343 = 7·49, 1764 = 36·49); consequently
**q^m | C(θ)** — and indeed q^m | C and q^m | Diag at all three q
(216 = 27·8, 7250 = 125·58, 67571 = 343·197; 216 = 27·8, 10500 = 125·84,
148176 = 343·432). Observed, unexplained — recorded as open. (iii) The
χ-signature has a clean meaning — its first entry is χ_q(Res(P,S)) =
χ_{F_{q²}}(S(β)), the F_{q²}-square-class of the effective frequency
ω = θ/(d_P S(β)) — and it is an orbit invariant, but it does **not** by
itself decide law-status (law-orbits 3, 4, 6 share the signature of
defect-orbit 12; law-orbit 13 shares that of defect-orbits 0, 1, 8, 9, 10):
the finer separating invariant is the identified open question. (iv) Both
same-P orbits fail the law with the *same* trace −1764 and are
self-transpose; all law-orbits have Tr(term) = Tr|A|² by definition of the
law.

## 4. k = 3: the theorem generalizes, the resonance does not

At k = 3, m = 5, q = 3 (band of 8 cubics, 56 pairs, scalar θ): T1's
A-covariance and θ-independence verify exactly, as the k-uniform proof
predicts, and the class-constant lemma re-verifies by direct f′-sums. The
exact values:

    primorial t³−t:  Diag = 21384, C = 3483  (C/Diag = +0.163, 8 classes)
    control t(t+1):  Diag = 25488, C = 3600  (C/Diag = +0.141, 4 classes)

Reading: **without the k = 2 collapse 𝔏 ≡ −P′ (mod P), the primorial is no
longer exceptional** — its class-correlation ratio is control-comparable
(+0.16 vs +0.14), against the k = 2 picture (primorial 0.46–1.00 vs control
≈ 0.00). This confirms the resonance is derivative-driven and k = 2-specific,
and it is *good news* for the programme: at k ≥ 3 the primorial behaves like
a generic puncture, so puncture-uniformity is easier, not harder, away from
the k = 2 laboratory. (Caveat: the k = 3 class family is very thin — E-scalar
is a strong constraint — so these are small-sample exact values, not
asymptotics.)

## 5. Consequences and what remains

The dispersion ledger for the true primorial is now, unconditionally:
𝔇 = q^m·(Diag + C) with C = C(θ) a θ-independent integer multiple of q (in
range, of q^m), computable as q·Σ(orbit traces). The open quantitative
question "C < Diag for all q" is reduced to a *finite* algebraic question per
q: bound ~q³/6-many integer orbit-traces (each a trace of
ζ^E·Â_P(μ₁)·conj(Â_{P′}(μ₁′)) over Q(ζ_q)/Q). Open items, sharpened:
the finer orbit invariant separating law from defect (the χ-signature is
constant but insufficient); the sign mechanism of the −1764-type orbits;
the observed q^m | C(θ) divisibility; C ≤ Diag for all q; and the k ≥ 3
programme now proceeds without a primorial-specific obstruction.

## 6. Boundary

| Status | Item |
|---|---|
| **PROVED** | T1: θ-independence of C(θ) and Diag (all k at the endpoint; via affine symmetry of t^q − t); T2: translations preserve terms, homotheties act by Galois, transpose acts by conjugation; C(θ) ∈ Z unconditionally, real; q | C, q | Diag at k = 2; orbit sums = Galois traces. |
| **EMPIRICAL-EXACT** (machine identities, Z[ζ_q]) | The 16-orbit classification at q = 7 (table above; law/same-P/χ constant per orbit; all orbits free); 1 and 3 all-law orbits at q = 3, 5 (explains the small-q per-class law); defect mass −6125 vs law mass +15778; q² | traces and q^m | C, Diag at q = 3, 5, 7; k = 3 values (primorial no longer exceptional). |
| **OPEN** | The finer orbit invariant deciding law vs defect; the sign mechanism of the −1764 orbits; the q^m-divisibility of C(θ); C(θ) ≤ Diag for all q; asymptotics of C/Diag; the endpoint deficit q^{(k−1)/2} (double dispersion); FFV-generic; FFPR at m = 2k−1; thinning; PORC_FF; FF first-band theorem; integer transfer. |
