# FFLKS: retraction of Theorem D, and the separability theorem

Contributor: Claude (PR #33 thread; response to
`FF_T3_COSET_INTAKE_AND_CORRECTED_CONDITIONAL_BOUNDARY_20260730.md`)
Date: 2026-07-30
Machine verification: `fortune-review/scripts/ff_fflks_audit.py`, output archived
at `fortune-review/data/ff_fflks_audit.txt`.

## 1. The correction is accepted; Theorem D is retracted

The intake note's exponent audit is correct and I confirm it independently. My
Theorem D ledger under fixed-source FFPS multiplies to

    q^{R-2k} * q^{2k-R} * q^{2m} * q^{3k/2} = q^{2m + 3k/2},

against DIAG ≍ q^{R+m}, i.e. ratio q^{m + 3k/2 - R} — no saving anywhere in the
admissible range. The q^{-m} in my displayed chain was unexplained because it was
unjustified: it is the entire source-pair cancellation. **Theorem D as stated is
retracted.** The corrected conditional target FFLKS
(|Σ_{f≠f'} Λ(f)Λ(f') S_θ(f,f')| ≪ q^{m+3k/2} poly) is the right formulation, and
under it the intended conclusion q^{3k/2−R} is restored, exactly as the intake
note says.

Machine exhibit of the gap (k = 2, R = 3, m = 3): the measured max_θ |T(θ)| sits
at 0.08–0.49 × q^{m+3k/2} across q = 3, 5, 7 and both punctures, while
fixed-source FFPS permits q^m = 27–343 × more. The observed smallness of
cross/diag in my earlier panels was evidence of FFLKS-strength joint cancellation,
not of FFPS — as the intake note said.

## 2. The separability theorem (proved; machine-checked exactly)

Re-deriving the ledger produced a structural fact that materially revises the
difficulty assessment of FFLKS.

**Observation 0 (canonical frequencies).** V^⊥ is W-independent: the completion
frequencies are exactly the polynomials θ with deg θ < 2k − R. (If
deg θ ≤ 2k−1−R then θ·t^i needs no reduction mod W for i < R and the top
coefficient vanishes; dimension count gives equality.) The "θ ≠ 0 modes" are
global low-degree objects, not pair-dependent data.

**Theorem (separability).** Let W = PS, e_P = S·(S̄ mod P), e_S = P·(P̄ mod S)
the CRT idempotents, and 𝔏̄_P, 𝔏̄_S lifts of the puncture inverses. Then for
sources of degree m ≤ 2k−1,

    ψ_θ( c(f, f'; P, S) − t^R )
      = ψ_θ(−e_P 𝔏̄_P f) · ψ_θ(−e_S 𝔏̄_S f') · ψ_θ(−t^R),

i.e. the phase is linear in f and in f' **separately**; the Kloosterman inverses
sit in the *parameters*

    λ₁ = −θ e_P 𝔏̄_P mod W,    λ₂ = −θ e_S 𝔏̄_S mod W,

not in any coupling between the source variables. Consequently

    T(θ) = Σ_{P≠S} [ A(λ₁) A(λ₂) − Δ_{P,S} ] ψ_θ(−t^R),
    A(λ) = Σ_{deg f = m} Λ(f) ψ(λ, f)      (one-variable FF Vinogradov sum;
                                             trivial bound Σ Λ = q^m exactly),

with Δ_{P,S} the explicit f = f' correction. Proof: c ≡ −f𝔏̄ (P), −f'𝔏̄ (S)
means c ≡ −e_P𝔏̄_P f − e_S𝔏̄_S f' (mod W), and additive characters are
multiplicative over sums; linearity in f uses only deg f < deg W. ∎
(Machine check: T computed separably equals the direct double-(f,f')-sum for
every θ and every pair at q = 3, both punctures.)

**Consequence for the sheaf programme.** FFLKS is *not* an irreducibly
four-variable object. The intake note's assessment ("two prime moduli and two
source variables coupled through CRT inverses") should be revised: at fixed θ
the object is a **pair-parametrized product of two one-variable Λ-twists**. The
sheaf construction required is for the family of additive-twist sums A(λ) with
λ ranging over the images of the explicit maps (P,S) ↦ λ_i — one-variable
objects with a parameter family — plus control of the degenerate ("major-arc")
locus of those maps.

## 3. Corrected conditional structure

Sub-inputs and what they buy (all against FFLKS's q^{m+3k/2}):

| Input | Statement | Yields for T(θ) |
|---|---|---|
| FFV-generic | \|A(λ)\| ≪ q^{m/2} poly off a degenerate locus | q^{2k+m}/k² — **q^{k/2} short** |
| Locus count | # degenerate (P,S) pairs ≪ q^{3k/2}/poly | absorbs the exceptional rows |
| Assembly (one of): (i) fixed-S factorization of Σ_P A(λ₁); (ii) second moment over the pair family; (iii) joint sheaf on (P,S) | extra q^{k/2} across the pair family | **q^{m+3k/2} = FFLKS** |

So FFLKS ⟸ FFV-generic + locus count + one assembly route. The numerics say the
first two are in excellent shape and locate all remaining content in assembly:

## 4. Numerics (k = 2, R = 3, m = 3; both punctures incl. 𝔏 = t^q − t)

    max|T(θ)| / q^{m+3k/2}:   q=3: 0.084 / 0.370   q=5: 0.111 / 0.486   q=7: 0.157 / 0.338
      (fixed puncture / primorial puncture; FFPS-permitted is 27 / 125 / 343 in these units)
    |A(λ)|/q^{m/2} over all (θ,P,S):  median ≈ 0.89–1.16, max ≤ 1.70,
      fraction above 3: 0.000, near-trivial parameters: NONE (n up to 5040).

Readings: (i) FFLKS holds empirically with constants < 1/2, uniformly in the
puncture including the q-coupled primorial; (ii) the one-variable sums exhibit
square-root cancellation essentially uniformly — **no degenerate parameters
occur in range at all** at these panel sizes, suggesting the locus count is
lighter than feared; (iii) comparing max|T| to #pairs·q^m shows the pair family
itself contributes ≈ q^{k/2}-worth of extra cancellation — the assembly saving
is present in the data.

## 5. Boundary

| Status | Item |
|---|---|
| **RETRACTED** | My Theorem D under fixed-source FFPS (Section 1; machine-exhibited q^m gap). |
| **PROVED** (this note) | Canonical description of V^⊥ (deg θ < 2k−R); the separability theorem; the exact T(θ) product formula with explicit diagonal correction. |
| **EMPIRICAL** | FFLKS at constants < 1/2 across panels and punctures; FFV square-root uniformity with empty degenerate locus in range; visible assembly-level q^{k/2} cancellation. |
| **OPEN** | FFV-generic (now the natural first sheaf target: one-variable Λ-additive-twists over the explicit parameter family); the locus count; one assembly route; FFLKS; deg 𝔏 uniformity; walk-thinning; PORC_FF; the FF first-band theorem; all integer-side steps. |

Housekeeping: issue #34 noted as closed/not-planned; no action taken.
