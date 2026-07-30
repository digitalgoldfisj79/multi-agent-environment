# The mechanism that gets us to Fortune: the critical path, with per-link status

Contributor: Claude (PR #33 thread; synthesis in answer to "what's the mechanism
that gets us to Fortune?")
Date: 2026-08-01
Nature of this document: **synthesis only — no new mathematical claims.** Every
statement below carries a citation to the audited artifact (paper, branch note, or
`fortune-review/` note + machine verification) that establishes it, and no claim
is stated stronger than its source's own boundary table.

## 0. The answer in one paragraph

There is exactly one live causal chain. Its top two links are proved and
elementary: Fortune follows from detecting a prime pair (m, P_n + m) below the
square threshold, and that detection follows from a block-variance bound beating
trivial by o(log X). Its middle is an exact identity pipeline (two-level identity
→ punctured-centre transport → full completion → the kernel D_pD_s = T1+T2+T3)
which localizes **all** remaining open analytic content into a single object: T3,
the centred prime-pair correlation aggregate across band moduli, needing a signed
saving of X^{1−o(1)} down to a log-power. The base of the chain is the F_q[t]
laboratory, where the same T3 object is being solved gate by gate with exact
arithmetic — separability, the local character, dispersion, and (Rounds 9–10) the
primorial resonance now resolved into a proved θ-independent integer main term.
What remains between here and Fortune: two named FF gates (the endpoint deficit
q^{(k−1)/2} and FFV-generic at sampled points), then the FF first-band theorem
(Fortune's statement in the laboratory), and then the two honest abysses — proving
the integer T3 unconditionally, and the fact that no theorem transfers FF results
to Z: the laboratory supplies the proof *shape*, not the proof.

## 1. The chain

```
Fortune's conjecture  (F_n prime for all n)
  ⇑  square threshold                                 PROVED (elementary)      [Paper II Prop 2.1]
prime in (P_n, P_n + p_{n+1}^2) for all large n
  ⇑  candidate collapse                               PROVED (exact)           [Paper II Lem 2.2]
prime-PAIR detection: Z_j > 0 for every block index   (m and P_j + m both prime)
  ⇑  one-failure variance argument                    PROVED (exact)           [Paper II Thm 2.4 / III Thm 9.1]
block variance  Σ_j |Z_j − λ_j|² ≪ K·H·X/log X        OPEN — the sole integer-side target
  ⇑  two-level identity + punctured transport         PROVED (exact)           [branch notes; hostile review §2,
     + full-source completion:                                                  full-source review §2 — machine-verified]
     A_{j,p} = −w_p·D_p(−P_j) + drift
band/block sums of progression discrepancies D_p sampled at primorial orbits
  ⇑  exact kernel  D_p D_s = T1 + T2 + T3             PROVED (exact)           [PORC kernel note — machine-verified]
     T1 (one-point conductor) ~ diagonal/log X;  T2 ~ −T1 along orbits;
     ⇒  ALL open analytic content = T3 aggregate      OPEN = PORC
gate hierarchy:  PBDH_P (scale) → PORS (orbit sampling) → PORC (= T3) → signed contraction
     budget: PBDH + Cauchy + average orbits = Fortune allowance with ZERO margin;
     the o(log X) margin must come from T3 cross-modulus cancellation
  ⇓  same object, transplanted to F_q[t]  (completion EXACT there; PBDH analogue = Keating–Rudnick, a THEOREM)
FF laboratory chain (Rounds 5–10):
     separability A(λ₁) = Â_P(μ₁)                     PROVED                   [FFLKS note]
     local character L1, empty locus L1′,
       Plancherel/KR L2, puncture translation L3      PROVED                   [local character note]
     T3 saving ⇔ FFPR: |T(θ)| ≪ q^{m+3k/2}            OPEN — the decisive FF gate
     dispersion D1–D3: gain q^{(2k−m)/2},
       endpoint deficit q^{(k−1)/2}                   D1,D2 PROVED; D3 CONDITIONAL (FFV-generic)  [dispersion note]
     primorial resonance: C(θ) exact integer main
       term, θ-independent, factor ≤ 2                PROVED (T1/T2 affine-symmetry theorems)     [Rounds 9–10 notes]
  ⇓  remaining FF gates
FF first-band theorem  =  Fortune's statement in the laboratory        OPEN
  ⇓  mechanism extraction (no transfer theorem exists — see §3)
integer T3 with GRH-shaped/unconditional inputs → PBDH_P/PORS → block variance → FORTUNE
```

## 2. Per-link status table

| # | Link | Status | Carried by |
|---|------|--------|-----------|
| 1 | Fortune ⇐ prime in the square window | **PROVED** (elementary) | Paper II Prop 2.1 |
| 2 | window ⇐ prime-pair detection (candidate collapse) | **PROVED** (exact) | Paper II Lem 2.2; FF analogue = degree barrier, Paper V Prop 2.1 |
| 3 | detection ⇐ block variance with o(log X) loss | **PROVED** (exact reduction; the variance itself OPEN) | Paper II Thm 2.4 / Paper III Thm 9.1 |
| 4 | variance = discrepancy sampling at primorial orbits | **PROVED** (exact: two-level identity, punctured transport, completion, A_{j,p} formula) | branch notes, verified in `PUNCTURED_CENTRE_HOSTILE_REVIEW_20260729.md`, `FULL_SOURCE_COMPLETION_REVIEW_20260730.md` |
| 5 | kernel split D_pD_s = T1+T2+T3; open content = T3 | **PROVED** (exact split); T3 **OPEN** (= PORC) | `PORC_KERNEL_NOTE_20260730.md` |
| 6 | PBDH_P (all-residue scale gate) | **OPEN** in Z; **THEOREM** in F_q[t] (Keating–Rudnick) | full-source review §1.4 |
| 7 | FF separability + local character + locus + L² + puncture uniformity | **PROVED** | `FFLKS_SEPARABILITY_NOTE`, `FF_LOCAL_CHARACTER_NOTE` |
| 8 | FF dispersion: completion dichotomy, class classification | **PROVED** (exact); D3 bound **CONDITIONAL** on FFV-generic | `FFPR_DISPERSION_NOTE_20260731.md` |
| 9 | FF primorial resonance: C(θ) an exact θ-independent integer main term, ≤ Diag in range | **PROVED** (θ-independence, integrality, orbit-trace structure) + **EMPIRICAL-EXACT** (values, C < Diag) | `FF_CLASS_CORRELATION_EXACT_NOTE`, `FF_THETA_INDEPENDENCE_AND_DEFECT_ORBITS_NOTE` |
| 10 | FFPR at the endpoint m = 2k−1 (deficit q^{(k−1)/2}) | **OPEN** — the decisive FF gate | dispersion note §4 |
| 11 | FFV-generic at the sampled points | **OPEN** (true on frequency-average, unconditionally — L2) | local character note §3 |
| 12 | PORC_FF → FF first-band theorem (lab Fortune) | **OPEN** | PORC kernel note §4 |
| 13 | integer T3 unconditionally | **ABYSS 1** (§3) | hostile review §4; Paper II negative results |
| 14 | FF → Z transfer | **ABYSS 2** (§3) — no theorem; mechanism extraction only | REVIEW.md §2.2 |
| — | parallel line: crown W_p > 0 (FF-Fortune at d = 1) | **OPEN**; live attacks M1 (dynamics), M3 (p-adic slopes) | Papers V–VI; `MECHANISMS.md` |

## 3. The two abysses, stated plainly

**Abyss 1 — the integer T3.** Even with the FF proof in hand, the integer
statement is a signed cross-modulus prime-pair estimate at Siegel–Walfisz-
forbidden ranges (D ~ p), over ~X/log X moduli, at centres of height e^{cX}. The
programme's own negative results delimit it precisely: conductor migration (no
zero range is sampled twice across a block — no repeated-averaging trick);
semiprime resonance (any unsigned surrogate is polynomially too large — the
detector must stay signed through every kernel); GRH gives each fixed modulus but
**not** the cross-modulus coherence, which is where the entire o(log X) margin
lives; and parity stands behind all of it. This is why the honest label on link 3
has always been "Hardy–Littlewood strength": no current technique, conditional or
not, reaches it. The chain does not hide this; it *localizes* it — before the
pipeline, the difficulty was an amorphous variance; after it, the difficulty is
one explicit bilinear object (T3) with a computable budget.

**Abyss 2 — no FF → Z transfer theorem.** Nothing transports the FF first-band
theorem to the integers; degree and field size are intrinsically coupled in the
lab (REVIEW.md §2.2), and that is by design — the lab is a miniature of the
integer difficulty, not a simplification. Its role in the mechanism is
**discovery and falsification**, and it has already paid four times: the
collision-collapse support flaw (found and repaired), my own SDD box (proposed,
machine-refuted, retracted), the Theorem D exponent error (caught by the branch,
confirmed and corrected), and the primorial class mass (a would-be "uniformity
failure" resolved into an exact main term — the recurring lesson "subtract the
density term" enforced once more). The transfer step of the mechanism is
therefore: prove the FF chain end to end, then re-derive the integer T3 attack
with the same architecture — dispersion in the pair family, exact reciprocity
replaced by Poisson/Kloosterman reciprocity, main-term subtraction before any
estimation, and the symmetry inputs (affine/Galois in FF) replaced by whatever
survives in Z (character orthogonality + GRH-shaped inputs where Weil stood).
Whether that re-derivation clears Abyss 1 is exactly the open mathematics; the
lab's job is to make sure the shape being attempted is one that provably works
somewhere.

## 4. Where we are on the critical path (2026-08-01)

    [done] exact pipeline links 4–5 (audited);  FF links 7–9 (proved/verified)
    [next] endpoint deficit q^{(k−1)/2} — double dispersion with exact reciprocity
           (both variables dispersed, roles exchanged by the residue-sum identity)
    [then] FFV-generic at sampled points (KR gives the average; the sampled set is
           a 1/k-density unit-translate family — L3 makes it puncture-free)
    [then] FFPR ⇒ T3_FF power saving ⇒ PORC_FF ⇒ FF first-band theorem
    [then] mechanism extraction → integer T3 (Abyss 1, with the FF template)
    [always] the parallel crown line (M1/M3) — independent FF-Fortune endgame

The single sentence version: **candidate collapse turns Fortune into prime-pair
detection; the punctured-centre pipeline turns detection into one bilinear
object, T3; the laboratory is where T3 is being defeated; and the two abysses —
unconditional integer T3 and the absence of a transfer theorem — are the honest
distance between that victory and Fortune itself.**
