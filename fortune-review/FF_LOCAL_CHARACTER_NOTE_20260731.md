# The local character, the empty degenerate locus, and the FFPR assembly target

Contributor: Claude (PR #33 thread; delivers steps 1, 2 and most of 5 of
`FFLKS_SEPARABILITY_INTAKE_AND_NEXT_GATE_20260730.md`, and sharpens step 4)
Date: 2026-07-31
Machine verification: `fortune-review/scripts/ff_local_character_audit.py`,
output archived at `fortune-review/data/ff_local_character_audit.txt`.

## 1. Theorem L1 (step 1, complete): the character is purely local

Let psi_P denote the standard additive character of the residue field
F_q[t]/P, psi_P(x) = e_q(coeff_{k-1}(x mod P)). Then for deg f = m < 2k:

    psi_theta( -e_P Lbar_P f )  =  psi_P( mu_1 · f ),
    mu_1 = -theta · Lbar_P · Sbar_P  in  F_q[t]/P,

and symmetrically psi_theta(-e_S Lbar_S f') = psi_S(nu_2 f'),
nu_2 = -theta·Lbar_S·Pbar_S. Consequently

    A(lambda_1) = Ahat_P(mu_1),   Ahat_P(mu) := sum_{deg f = m} Lambda(f) psi_P(mu f):

**the separated source factor is an additive Fourier coefficient of the
prime-count mod P, at the frequency mu_1.** The entire dependence on
(theta, S, puncture) enters through the single residue-field parameter mu_1.

Proof. lambda_1 f = -theta e_P Lbar_P f with e_P = S·(Sbar_P); mod W = PS,
S·x = S·(x mod P), so theta lambda-product reduces to S·(mu_1 f mod P) with
deg(mu_1 f mod P) <= k-1; the top coefficient of the monic-S product extracts
coeff_{k-1}. ∎ (Machine check: exact over 72-15,120 samples per configuration,
q = 3, 5, 7, both punctures.)

## 2. Corollary L1' (step 2, main part): the degenerate locus is EMPTY

mu_1 != 0 always: theta != 0 has deg theta < 2k - R <= k = deg P, so
theta != 0 mod P, and Lbar, Sbar are units. **The local conductor is always
full; there is no Artin-Schreier-degenerate or trivial parameter anywhere in
the family.** This upgrades the earlier empirical "zero degenerate parameters
in 5040 samples" to a theorem, and discharges the algebraic half of step 2.

Residual analytic half: could |Ahat_P(mu)| be enhanced at special mu (e.g.
low-degree representatives, the short-interval-type resonances)? Probe (all
mu != 0, per modulus): |Ahat|/q^{m/2} by deg(mu): deg 0: mean = max = 1.000
exactly; deg 1: mean 0.87-0.96, max <= 1.70. Flat — no analytic enhancement in
range. (The exact value 1.000 at scalar frequencies is itself a curiosity worth
a later exact computation; it is not an enhancement.)

## 3. Theorem L2: FFV holds on frequency-average, unconditionally (identity)

Since sum_{r mod P}(N(r) - q^{m-k}) = 0 exactly (FF PNT identity: sum Lambda
over degree m is q^m), Plancherel gives the exact identity

    sum_{mu != 0} |Ahat_P(mu)|^2  =  q^k · sum_{r mod P} |N(r) - q^{m-k}|^2,

(machine check: both sides equal to 12 digits at q = 3, 5, 7). The right side
is the all-residue additive variance of Lambda mod P — Keating-Rudnick's
object; with their published input it is q^m·min(m, k-1)(1+o(1)) in large q.
So **FFV-generic is true on average over mu at exactly the conjectured scale;
what is open is only the value at the ~q^k/k sampled points mu_1(S).**

## 4. Theorem L3 (step 5 at L^2, free): puncture-uniformity by translation

The puncture enters mu_1 only through the unit factor Lbar_P: changing
L -> L' translates the sampled frequency multiset {mu_1(S)}_S by the unit
Lbar'/Lbar (machine-checked multiset identity). Hence **every mu-averaged
statement — L2, any restricted second moment over a union of translates — is
automatically uniform in the puncture, including L = t^q - t.** Uniformity is
a live question only for specific-point statements. (Consistent with the
assembly numerics below: averages identical across punctures; specific-point
savings differ.)

## 5. The sharpened step 4: FFPR

Substituting L1, the assembly target becomes fully explicit. Define

    T(theta) = sum_{P != S, deg = k}
               Ahat_P(-theta Lbar_P Sbar_P) · Ahat_S(-theta Lbar_S Pbar_S)
               · psi_theta(-t^R)  +  (explicit f = f' corrections).

**FFPR (FF prime-pair reciprocity estimate) — the decisive open target:**
|T(theta)| << q^{m + 3k/2} · poly(k, m), uniformly in theta and the puncture.

What is now proved about its structure:

1. **S -> Sbar mod P is injective on the band** (deg(S - S') < k = deg P), so
   for fixed P the sampled frequencies are q^k/k distinct nonzero points — a
   1/k-density subset of F_q[t]/P.
2. **Cauchy + Parseval (+ L2) gives |T| <= q^{m+2k}·min(m,k-1)/k — exactly
   q^{k/2}·(1/poly) short of FFPR.** No worst-case argument can close this
   (the earlier no-go); the saving must come from cancellation across the pair
   family. Measured realized saving (Cauchy bound / actual max|T|): 2.4, 6.4,
   7.8 at q = 3, 5, 7 for the fixed puncture — tracking q^{k/2} = 3, 5, 7
   almost exactly; 0.8, 1.4, 3.7 for the primorial puncture — growing, with
   smaller constants (the specific-point uniformity question is real).
3. **Recommended attack surface:** expand Ahat_P via Gauss sums into
   multiplicative characters mod P; the S-dependence becomes chi-bar(S)
   evaluated AT the prime S, so the pair sum contains
   sum_{deg S = k, S prime} chi-bar(S) x (S-local factors) — character sums
   over primes, where Weil-strength q^{k/2} savings live. The obstruction to a
   one-line finish is that the S-local factor carries its own character family
   (the bilinear structure); the three assembly routes of the intake note act
   here, with the pair-family second moment now expressible entirely in
   residue-field Fourier data with known L^2 norms.

End-to-end cross-validation: T(theta) recomputed through the local-character
chain reproduces the archived separability-route values exactly (max|T| =
60.9 / 1736.4 / 18510.7 fixed puncture, 270.0 / 7600.0 / 39788.0 primorial,
q = 3/5/7) — the completion -> separability -> localization chain is
consistent from end to end.

## 6. Boundary

| Status | Item |
|---|---|
| **PROVED** | L1 (local character; A = Fourier coefficient of primes mod P); L1' (degenerate locus empty — algebraic half of step 2 discharged); L2 (Plancherel identity; FFV on frequency-average); L3 (puncture-uniformity of all frequency-averaged statements); band-injectivity of S -> Sbar mod P; the Cauchy+Parseval ceiling q^{m+2k}poly/k. |
| **INPUT** | Keating-Rudnick AP-variance for L2's asymptotic scale (large q). |
| **EMPIRICAL** | Flat frequency-locus profile (no analytic enhancement in range); realized assembly saving tracking q^{k/2}; weaker constants at the primorial puncture for specific points. |
| **OPEN** | FFPR (the q^{k/2} pair-assembly estimate — now the single decisive FF gate); specific-point FFV beyond averages; analytic-locus classification beyond tested range; thinning (coset -> squarefree products -> walk analogue); PORC_FF; FF first-band theorem; all integer-side steps. |
