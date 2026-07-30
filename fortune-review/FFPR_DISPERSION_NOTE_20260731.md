# FFPR via the pair-family second moment: exact dispersion structure, a
# conditional q^{(2k−m)/2} gain, and the primorial class-correlation discovery

Contributor: Claude (PR #33 thread; the requested attempt on FFPR by assembly
route (ii) of `FFLKS_SEPARABILITY_INTAKE_AND_NEXT_GATE_20260730.md`)
Date: 2026-07-31
Machine verification: `fortune-review/scripts/ff_ffpr_dispersion_audit.py`,
output archived at `fortune-review/data/ff_ffpr_dispersion_audit.txt`.

## 0. Outcome in one paragraph

The pair-family second moment does not close FFPR at the Fortune endpoint, but
it produces: (i) two exact unconditional structure lemmas (a completion
dichotomy — the FF form of archimedean truncation, with zero error — and a
complete classification of the coincidence classes as {diagonal} ∪
{multiplicative classes S' ≡ c_E·P (mod S)}); (ii) a dispersion theorem,
conditional only on FFV-generic for the class terms, improving the Cauchy
ceiling by q^{(2k−m)/2} and leaving an FFPR deficit of exactly q^{(m−k)/2} —
so FFPR is nearly closed just above the Heisenberg point m = k+1 (deficit
q^{1/2}) and remains q^{(k−1)/2} short at the endpoint m = 2k−1; (iii) a
discovery: **the true primorial puncture t^q − t does not oscillate over the
multiplicative coincidence classes** (class/diagonal mass ratio ≈ +0.69 to
+1.00, against ≈ 0.00 for a fixed puncture) — the puncture-uniformity risk is
now located in a single explicit family of class correlation sums.

## 1. Setup

Endpoint-normalized notation as before: band primes deg k, sources deg
m ≤ 2k−1, Â_P(μ) = Σ_{deg f = m} Λ(f)ψ_P(μf), μ₁ = −θ𝔏̄_P S̄_P,
ν₂ = −θ𝔏̄_S P̄_S. Route (ii): expand the second factor of
T = Σ_{P≠S} Â_P(μ₁)Â_S(ν₂)·φ over f', Cauchy–Schwarz in f' against the
Λ-mass (Σ Λ² ≤ m q^m), drop primality by positivity, and study

    𝔇 = Σ_{f' monic, deg m} | Σ_{P≠S} Â_P(μ₁) ψ_S(ν₂ f') |²,
    |T|² ≤ m q^m · 𝔇.

## 2. Lemma D1 (proved; exact): the completion dichotomy

For pairs of pairs, with h = ν₂/S − ν₂'/S' = (ν₂S' − ν₂'S)/(SS'):

    Σ_{f' monic, deg m} ψ_S(ν₂f') conj(ψ_{S'}(ν₂'f'))
      = q^m · (unimodular constant)   if deg(ν₂S' − ν₂'S) ≤ 2k − m − 1,
      = 0                              otherwise.

Proof: ψ_S(νg) = e_q(res_∞(νg/S)); the free coefficient space of monic
degree-m f' is {deg ≤ m−1}; the linear functional g ↦ res(hg) vanishes on it
iff res(h·t^j) = 0 for j ≤ m−1 iff h = O(t^{−m−1}) iff the displayed degree
bound; a nontrivial additive character sums to zero over a full subspace. ∎
**The FF interval kills all non-coincident cross terms exactly — this is the
"archimedean truncation" of classical dispersion with literally zero error.**
(Machine check: every one of the 6² and 90² pairs of pairs at q = 3, 5.)

## 3. Lemma D2 (proved; exact): the coincidence classes at the endpoint

At m = 2k−1 the criterion reads ν₂S' − ν₂'S = E ∈ F_q, and:

- **E = 0** forces S = S', ν₂ = ν₂', hence (by band-injectivity of P ↦ P̄
  mod S) the full diagonal (P,S) = (P',S').
- **E ≠ 0** forces the multiplicative relation
      S' ≡ c_E · P  (mod S),   c_E = −E·θ̄·𝔏 (mod S),
  with (P',S') then determined up to ≤ q² choices: the off-diagonal
  coincidences are **prime pairs in multiplicative position** — a
  Kloosterman-type thin family, of total size O(q^{2k+3}/k²) against
  #pairs² = q^{4k}/k⁴.

(Machine check: every coincident quadruple at q = 3, 5 is either diagonal or
satisfies S' ≡ c_E P mod S exactly.) For general m the classes are the
E-families deg E ≤ 2k−m−1 with multiplicity ≤ q^{2k−m+1} per pair — large for
m near k (the f'-average cannot resolve frequencies at the Heisenberg point),
small only near the endpoint. This is the quantitative reason dispersion's
usefulness concentrates at large m.

## 4. Theorem D3 (conditional): the dispersion bound and its honest ledger

Assume FFV-generic (|Â| ≪ q^{m/2} poly — the programme's step 3) **for the
class terms only**; the diagonal needs only Parseval + the KR variance input.
Then for k+1 ≤ m ≤ 2k−1:

    𝔇 ≤ q^m·[diagonal mass] + [class mass]
       ≤ k·q^{2m+2k}·poly + q^{4k+1}·q^m·poly,       (diagonal dominates for m ≥ k+1)

    |T(θ)| ≤ (m q^m 𝔇)^{1/2} ≪ q^{3m/2 + k} · poly(k, m).

Ledger against the two benchmarks:

| Benchmark | Value | D3 vs benchmark |
|---|---|---|
| Cauchy+Parseval ceiling | q^{m+2k}/k | **gain q^{(2k−m)/2}** (q^{1/2} at the endpoint, q^{(k−1)/2} at m = k+1) |
| FFPR target | q^{m+3k/2} | **deficit q^{(m−k)/2}** (q^{1/2} at m = k+1, q^{(k−1)/2} at the endpoint) |

Consequence for T3: the coset power saving now holds for
R > 3k/2 + (m−k)/2 — a nonempty (m, R) window for k ≥ 4 with m near k+1:
**the first FFPR-adjacent unconditional-shape savings**, though not yet at the
Fortune endpoint (at m = 2k−1 the window closes: R would need to exceed
2k − 1/2). The endpoint deficit q^{(k−1)/2} is fully attributable to the
Cauchy-in-f' step treating the source at L² — the same structural loss in
both the integer and FF ledgers, now isolated to one inequality.

Numerics (k = 2, endpoint m = 3): dispersion bound / FFPR target = 0.74–1.82
across q = 3, 5 and punctures — sitting at the predicted q^{(k−1)/2} = q^{1/2}
scale; bound beats the Cauchy ceiling by ~3–4× (≈ q^{1/2}·poly).

## 5. The discovery: the primorial does not oscillate over the classes

Measured class-mass/diagonal-mass in 𝔇:

    fixed puncture t(t+1):    q=3: −0.000     q=5: +0.003     (perfect oscillation)
    primorial t^q − t:        q=3: +1.000     q=5: +0.690     (structured, positive)

**For the true primorial puncture, the multiplicative coincidence classes
carry non-oscillating mass comparable to the diagonal.** This does not change
the order of Theorem D3 (𝔇 at most doubles), but it is the first concrete
localization of the puncture-uniformity risk: everything else in the pipeline
is provably or empirically puncture-uniform (L3 covers all averages), and the
one place t^q − t behaves differently is the family

    C(θ) = Σ_{S' ≡ c_E P (mod S)} Â_P(μ₁) conj(Â_{P'}(μ₁'))
    — "class correlation sums over prime pairs in multiplicative position."

The exact value +1.000 at q = 3 suggests an exact small-field identity worth
computing (𝔏 = t³−t is the product of all degree-1 monics; the class
constraint inherits its full symmetry). **Next-gate recommendation: compute
C(θ) exactly for t^q − t before any further estimation** — if the primorial's
class mass is an exact main term, it must be subtracted like every other
density term in this programme (the recurring lesson), and the dispersion
route then plausibly closes with the subtracted classes oscillating.

## 6. Two structural remarks for the remaining q^{(m−k)/2}

1. **Exact reciprocity is available for double dispersion.** ψ_P(μ₁f) is
   e_q(res) of the P-pole of −θf/(𝔏SP); the sum of residues over all poles
   (including ∞) vanishes, so the roles of moduli and numerators exchange
   with zero error — the FF Kloosterman reciprocity is an identity, not an
   approximation. Dispersing in BOTH sources with the roles exchanged is the
   natural route to convert the remaining q^{(m−k)/2} into a class-correlation
   estimate, and no error terms are generated at any completion step.
2. The classes being prime pairs in multiplicative position means the
   remaining estimate is a cousin of bilinear character/Kloosterman sums over
   primes — the object family where Weil/Katz technology and the
   Sawin–Shusterman toolset act in FF.

## 7. Boundary

| Status | Item |
|---|---|
| **PROVED** | Lemma D1 (exact completion dichotomy); Lemma D2 (exact endpoint classification: diagonal + multiplicative classes, sizes counted); the dispersion chain |T|² ≤ mq^m𝔇; the general-m class-multiplicity count q^{2k−m+1} (Heisenberg behaviour). |
| **CONDITIONAL** | Theorem D3: |T| ≪ q^{3m/2+k}poly for k+1 ≤ m ≤ 2k−1, given FFV-generic on the class terms only; FFPR deficit q^{(m−k)/2}; T3 power-saving window R > 3k/2+(m−k)/2. |
| **EMPIRICAL** | Dispersion bound at 0.74–1.82× FFPR target at k=2; class oscillation ≈ perfect for fixed punctures; **primorial class mass +0.69 to +1.00 — structured** (the located uniformity risk); exact +1.000 at q=3 suggesting an identity. |
| **OPEN** | The class correlation sums C(θ) (exact computation for t^q−t first, then estimation); the remaining q^{(m−k)/2} at the endpoint (double dispersion with exact reciprocity is the identified route); FFV-generic itself; FFPR at m = 2k−1; thinning; PORC_FF; FF first-band theorem; integer transfer. |
