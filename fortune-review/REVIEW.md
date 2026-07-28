# End-to-End Review: Fortune's Conjecture Papers I–VI

**Reviewer:** Claude (AI-assisted review at the author's request)
**Date:** 2026-07-28
**Scope:** the six-paper sequence

| # | Title (short) | Object |
|---|---|---|
| I | Collision Geometry and Spectral Laws | consecutive-prime partial products mod shell primes |
| II | Prime Detection at Primorial Centres (corrected) | candidate collapse, block variance, reciprocal frame |
| III | Pair-Sum Rigidity, Exceptional Sets (corrected) | superincreasing kernel theory, transfer gap |
| IV | Prime Detection Along Random Primorial-Product Paths | random-order reciprocal-frame theorem |
| V | Fortunate Polynomials over Finite Fields | function-field d=1 crown W_p > 0 |
| VI | Secondary Traces and Kummer Quotients | integral layer, Artin–Schreier / Kummer geometry |

A companion document, `MECHANISMS.md`, proposes new mechanisms for progress, informed by
the computations in `scripts/` (all run for this review; outputs quoted below are from
actual runs).

---

## 1. Executive summary

**The sequence is coherent, honest, and unusually well-instrumented.** Claim hygiene is
strong: theorems, conjectural calibrations, computer-assisted results, negative results,
and open targets are consistently separated; two papers carry explicit correction notices
that *withdraw* previously circulated centrings rather than paper over them. Every exact
identity I tested numerically — 30 checks across Papers I, II, III, V — **passed** (§4).

**The honest state of the programme:**

1. The integer problem is reduced, correctly and exactly, to a *prime-pair* variance
   problem at primorial centres (candidate collapse, Paper II). That target is of
   Hardy–Littlewood strength at ~X/log X isolated, exponentially spaced centres. No known
   technique — including GRH — addresses it; the papers say so, and they are right.
2. The reciprocal pair-sum frame (Papers II–IV) is a well-developed *model*, but the
   source→frame bridge was reopened by the corrections and **is currently missing**. This
   makes the frame, and its impressive random-order theorem (Paper IV), *not load-bearing*
   for Fortune at present. This is the single most important strategic fact about the
   programme (§5.1).
3. The function-field d=1 crown (Papers V–VI) is the genuinely promising front: an exact,
   finite, geometric nonvanishing problem (W_p > 0) with all the semisimple and
   congruence routes provably closed. New computations for this review (census to p=199)
   show the quadratic sector N₂(p) behaves like a Poisson(e/2) variable — it *vanishes*
   for about a quarter of primes — which sharpens where the remaining difficulty lives
   (§4.3, and MECHANISMS M1–M2).

**Bottom line.** No error affecting a stated theorem was found. The deepest structural
criticism is priority, not correctness: derandomisation effort (Paper IV's program) is
currently aimed at a target that no theorem connects to Fortune, while the function-field
crown — where every object is finite and computable — still lacks a serious analytic or
p-adic attack. `MECHANISMS.md` proposes both.

---

## 2. The reduction chain, as it actually stands

```
Fortune's conjecture (F_n prime for all n)
  ⇑ (elementary; Paper II Prop 2.1)
prime in (P_n, P_n + p_{n+1}²)  for all large n     [Cramér-scale, sparse centres]
  ⇑ (candidate collapse; Paper II Lem 2.2 — exact)
prime-pair detector Z_j(H) > 0 for all j            [both m and P_j+m prime]
  ⇑ (one-failure variance argument; Paper II Thm 2.4 / Paper III Thm 9.1 — exact)
block variance  Σ_j |Z_j − λ_j|² ≪ N X L(X),  L = o(log X)     [OPEN — HL strength]
  ⇑ (NO THEOREM — "source-to-frame transference", reopened by corrections)
reciprocal frame target  𝔉_X ≪ M X^{o(1)}          [OPEN for increasing order]
  ⇑ (Paper IV — PROVED in expectation over random orderings, loss (log X)^9)
random-order model                                   [derandomisation OPEN]
```

Parallel laboratory (Papers V–VI):

```
function-field d=1 crown:  W_p = N₂ + (N_sq + N_ns)/2 > 0 for all p > 3   [OPEN]
   — equivalent forms: I₄(p) > p−1;  #𝒬_p(F_p) > 1;  q-line nonsaturation
   — provably closed routes: aggregate Betti (fails at p=11), hook fixed points
     (circular), mod-p congruences (blind: W_17 = 17 ≡ 0), split level (empty),
     ordinary divided hook (not virtual), sign-twist compactification.
```

Two facts about this chain deserve emphasis.

**2.1 The missing bridge is the integer-side bottleneck.** Papers II–III are explicit
that no implication currently runs from the frame target to the corrected prime-pair
variance. Until Route A (recentred one-sided detector) or Route B (double von Mangoldt
source) of Paper II produces a theorem, any effort spent on the frame — including
derandomising Paper IV — improves a model, not the conjecture. The model is still
valuable (it is falsifiable structure), but the sequencing matters; see MECHANISMS M7.

**2.2 The function-field problem never decouples.** Over F_q the polynomial primorial
P_d has degree ~q^d: degree and field size are intrinsically coupled, so the crown never
enters the classical "fixed degree, q → ∞" regime where big-monodromy/Chebotarev
methods trivialize short-interval statements. Paper V's d=1, q=p case is the *smallest*
instance of this coupling, not a simplification of it. This is why Sawin-type
square-root cancellation is simultaneously the right neighbouring technology and — as
Paper V proves at p=11 — insufficient in aggregate-Betti form. The lab is a genuine
miniature of the integer difficulty, with one decisive advantage: everything is finite.

---

## 3. Paper-by-paper review

### Paper I — Collision Geometry and Spectral Laws

**Contributions.** Exact fourth-moment identity for the walk (Q_j) mod r; low-transport
collision bounds via the clean "reduced ratio has ≤ k log(2X)/log R shell prime
divisors" mechanism; offset-slice large-sieve-type incidence with diagonal dominance;
average almost-injectivity; a complete Smith-form theorem for interval families
(endpoint-graph gcd of cycle imbalances — a nice, apparently new refinement of gain-graph
rank theory); the pair-overlap decomposition of the two-run energy; closure of the k=3
sector; the exact 4-channel median bilinear identity with matrix M and its independent
prefix null laws; the non-Gaussian spectral law (639/35); block-composition closures;
obstruction theorems against naive van der Corput differencing and multiplier inversion.

**Verified here.** Median-matrix eigenvalues {−1, 4, (19±√281)/2} (numeric); the
fourth-moment law of the two-run spectrum, exhaustively over root orders 3 and 4 at
V=5,6 and combinatorially to V=9 — the coefficients (1, 40, 420, 1736, 2556) and the
limit 639/35 are **exactly right for the alternating kernel**. (A reviewer modelling the
kernel with all-plus signs gets (1, 40, 540, 2800, 4900) and limit 35 — I did this first
and briefly believed the paper wrong. The alternating structure of χ(Q_bQ_d/Q_aQ_c) is
essential; the paper's own phrase "alternating four-endpoint exponent vectors" is
load-bearing and could usefully be displayed as a formula.)

**Assessment.** The strongest purely unconditional paper of the integer sequence. The
divisor-counting mechanism is elementary but used with real care, and the negative
results (§10) prevent several tempting dead ends. The isolated obstruction — a centred
rank-two dispersion estimate across the median variable (HTE4/HWF4) — is exactly
identified. My one structural comment: the Cauchy–Schwarz loss of √V in §5.3 has a
martingale flavour (prefix sums with block increments); see MECHANISMS M4.

### Paper II — Prime Detection at Primorial Centres (corrected)

**Contributions.** Candidate collapse (exact); the corrected detector calibrations
(Z_j, Y_j, T_j) with correctly scaled block-variance criteria; the exact Fourier source
identity (Thm 2.8); the reciprocal frame with exact one-sided residual decomposition
ℰ_a = M(M−1)κ_{2,a} + ℛ_a; exact Lebesgue moments of H₂ (four-copy rigidity); the
globally coupled Möbius detector with negligible high-degree tail; **three important
negative results**: the semiprime-resonance obstruction (density surrogates are
polynomially too large because semiprimes pr, X/√2 ≤ p < r < X, divide every centre),
the exact CRT character-ratio collapse (no de-tensorisation), and conductor migration
(the explicit-formula band moves by a factor ~p_{n+1} per index — no repeated sampling
of any zero range across the block).

**Verified here.** Thm 4.2 fourth moment by enumeration for N = 2..8 and the centred
mass N(N−1)(5N²−N+2)/4; the N=55 value 13,562,560 matches. The correction notice's
arithmetic (μ_j/H → e^γ/2 via Mertens) checks.

**Assessment.** The correction is handled with exemplary honesty, and the corrected
criteria are exact. Two review emphases:

1. *The variance target should be named for what it is.* (2.10)/(12.1) with L = o(log X)
   is a Poissonian-variance statement for prime pairs at ~X/log X isolated centres of
   height e^{cX}. It implies binary-Goldbach-type detection at those centres. Labelling
   it "open" is correct but undersells the calibration: it sits at the strength of
   Hardy–Littlewood variance conjectures (Montgomery–Soundararajan) *restricted to a
   sparse deterministic family*, which is beyond any current or foreseeable averaging
   technique — the paper's own conductor-migration theorem is the proof of that
   statement in explicit-formula language.
2. *The semiprime resonance theorem deserves more prominence*: it is the precise reason
   every future mechanism must keep the prime detector signed through the kernel, and it
   quietly kills a whole family of "positive main term + small error" proposals.

### Paper III — Pair-Sum Rigidity, Exceptional Sets (corrected)

**Contributions.** B-rigidity of superincreasing walks; the difference-multiplicity
dichotomy (multiplicities are exactly N or 1 — no intermediate scale); the exact
two-scale energy decomposition forcing any pair-sum mechanism to control single-walk
energy at scale M/N; moment bounds (2k)!/2^k·M^k with the labelled-lift argument;
sub-Weibull Lebesgue tails with sharp constant √2; exact sixth moment and third
cumulant (74M³); the transfer-gap corollary — the open statement is a *sparse
exceptional-set* property (polynomially many reciprocal atoms must not concentrate on
sets of measure e^{−√t}), not a Lebesgue estimate; corrected prime-pair source and the
aggregated four-form covariance conditions (C1)–(C2).

**Verified here.** Dichotomy histograms at N=8: {1: 812, 8: 56} and N=9: {1: 1332,
9: 72} — exact match; sixth-moment polynomial by enumeration for N = 3..7 — exact match.

**Assessment.** The kernel theory is complete and, in my checks, flawless. The paper's
best insight is negative-space: Corollary 8.1/A.10 shows the Lebesgue theory is *done*
and cannot be improved into the arithmetic statement — the measure μ_{X,a} is supported
on X^{4+o(1)} atoms and the allowed overshoot is a factor e^{√t}t^{−1}X^{o(1)}. The open
problem is a concentration/equidistribution statement about {a(1/q − 1/r)} against the
level sets of a fixed rigid kernel. I flag one presentational hazard: (C1)–(C2) look
like "just two mean values", but they encode four coupled primality conditions; a reader
should be told plainly that (C2) at d-aggregated scale is again HL-strength.

### Paper IV — Random Primorial-Product Paths

**Contributions.** The random-order theorem: E_σ[ℰ_a^σ] ≤ C M (log X)^9 uniformly in
1 ≤ |a| < H, with the aggregate and Frobenius forms; mechanism = exact
rank-conditioning to uniform ordered set partitions, multivariate Cauchy contour decay,
sixth-moment orthogonality bounding exceptional ("bad") ratio characters
(β ≪ X(log X)³), path matching, and a complete configuration ledger closing at exactly
M(log X)^9 with no power-of-X reserve.

**Verification status.** I did **not** line-check the ledger constants (T1–T3, C1–C4,
the 600 log X threshold, the exponent 9); the structure is coherent and the paper's own
§8 correctly identifies the fragility (one lost rank parameter breaks the bound by a
power of X). Given that the binding classes close with zero cushion, an independent
*symbolic* re-derivation of the ledger would be a worthwhile validation artifact — the
kind of finite bookkeeping this programme is unusually well set up to mechanize.

**Assessment.** As a model theorem this is the technical high point of the integer
sequence: it proves the pair-sum architecture is compatible with the critical scale for
*generic* orderings, with effective constants and honest scope (§11: no pointwise claim
for the identity ordering, no Fortune claim). Two strategic observations:

1. The theorem's cancellation source (order entropy) is *exactly* what the increasing
   order lacks; §11's derandomisation question is therefore not an incremental gap but
   the whole problem re-expressed. My small-scale experiments (§4.4) at least show the
   identity ordering is *bulk-typical* for the frame energy at toy scales — there is no
   sign it is an energy outlier, which is consistent with (though far from evidence for)
   derandomisability.
2. Because the source→frame bridge is missing (Paper II/III corrections), even a full
   derandomisation of Theorem 2.1 would today prove no statement about primes. Sequencing
   matters; see MECHANISMS M7.

### Paper V — Fortunate Polynomials over Finite Fields

**Contributions.** The degree barrier (function-field candidate collapse); exact affine
orbit decomposition I₄ = (p−1) + p(p−1)N₂ + ½p(p−1)(N_sq+N_ns) and the crown
W_p > 0; global smoothness of the sparse ordered-root surface (clean truncated
Vandermonde argument); the Sawin-torsor Betti transfer and the **refutation of the
aggregate absolute-Betti strategy at p=11** (B_mid = 82 > 10); the exact sign-hook trace;
the alternating-hook projector normalization (no missing p); fixed-point circularity
(the p-cycle trace inequality *is* the crown); the q-line cell system and the
saturation-defect identity S₀^sat − S₀ = p(N_sq + N_ns).

**Verified here** (independent implementation, dynamical irreducibility test):
p=5: I₄=124, N₂=1, {N_sq,N_ns}={4,6}, W=6; p=7: I₄=426, N₂=1, {10,8}, W=10;
p=11: I₄=1660, N₂=1, {14,14}, W=15 — all match, and the orbit decomposition holds
exactly in each case. (Class labels sq/ns depend on the chosen representative; I
compared as multisets.)

**Assessment.** This is the paper that changes the game: it converts the crown into
exact nonnegative integer coordinates and then *closes the cheap exits* one by one. The
p=11 Betti refutation is a model of how to kill one's own best idea properly. The one
missed opportunity — developed at length in MECHANISMS M1 — is that the depressed family
has a dynamical-systems structure the paper never exploits: a root of
X^p + aX³ + cX + d satisfies α^p = φ(α), φ(x) = −(ax³+cx+d), so Frobenius acts on the
root set as an explicit cubic (quadratic for the N₂ sector) map, and irreducibility says
this action is a single p-cycle.

### Paper VI — Secondary Traces and Kummer Quotients

**Contributions.** The Cartier first moment M_a as an existence certificate and its
identification as the first cyclotomic tangent; the nonsplit tangent extension with
identity Bockstein but **Frobenius blindness** (Φ_λ family — modular data cannot see the
tangent trace); nonexistence of an ordinary divided-hook object (nonintegral Fourier
multiplicities); Hattori–Stallings coefficient extraction Tr_Z(Φσ^{−r}) = p h_r; the
explicit global Artin–Schreier coordinate with σ(y) = y+1 and the irreducibility section
g = 1; the elegant **no-split theorem** (logarithmic-derivative degree count: X_a(F_p) =
∅ for p > 5); the Kummer-form classification (gcd(p−3, p−1) = 2; sign-twist criterion
p ≡ 1 mod 4); the compactified quotient count #𝒬_p(F_p) = 1 + (p−1)W_p and the proof
that standard mod-p congruences cannot decide the crown (W_17 = 17 ≡ 0 mod 17).

**Verified here.** Spot-checked the algebra (gcd computation, no-split degree count,
fixed-progression power sums Σ i^m ≡ 0 for 1 ≤ m ≤ p−2); the point-count ledgers are
consistent with my independent W_p values (W_17 = 17 confirmed independently in the
census, where p=17 gives N₂=1, N_sq=18, N_ns=14).

**Assessment.** A careful negative-space paper: it builds exactly the integral carriers
a secondary-trace attack would need and then proves, one at a time, that none of them
yields an independently computable positive term. The terminal formulation ("one-sided
Kummer-quotient Frobenius theorem") is the right residue. Its own §15 list of closed
continuations is the most useful "do not retry" inventory in the sequence. The natural
next moves that are *not* on the closed list are p-adic: Newton polygons / unit-root
L-functions above the Cartier layer (MECHANISMS M3), and the statistical reframing of
the crown itself (M1–M2).

---

## 4. Independent verification performed for this review

All scripts in `scripts/`; all run on this machine; outputs archived in the session log.

### 4.1 `verify_identities.py` — 30/30 PASS

| Claim | Method | Result |
|---|---|---|
| Paper II Thm 4.2, 4th moment of H₂, N=2..8 | exact enumeration (superincreasing model) | PASS (7 values) |
| Paper II Thm 4.2, centred mass, N=2..8 | enumeration | PASS (7 values) |
| Paper II Thm 4.2 at N=55 = 13,562,560 | formula evaluation | PASS |
| Paper III Thm 3.1 dichotomy, N=8,9 | full difference histogram | PASS (exactly {1: M(M−1)−N²(N−1), N: N(N−1)}) |
| Paper III Rmk A.9 sixth moment, N=3..7 | enumeration | PASS (5 values) |
| Paper I Prop 5.4 median-matrix eigenvalues | numeric linear algebra | PASS |
| Paper I Prop 5.6 spectral moments, V=5,6, q=3,4 | exhaustive over q^V tuples, alternating kernel | PASS |
| Paper V exact counts p=5,7,11 | independent irreducibility code | PASS (I₄, N₂, {N_sq,N_ns}, W_p, orbit decomposition) |

Note on Prop 5.6: with the correct alternating kernel Z̄_aZ_bZ̄_cZ_d the coefficients
(1,40,420,1736,2556) reproduce enumeration exactly through V=9; the all-plus kernel
gives (1,40,540,2800,4900) — the c₈ = 4900 = 70² there is the single all-ones class of
complementary 4-set pairs. The paper is right; the sign structure is essential.

### 4.2 A caveat on what was *not* verified

Paper IV's configuration ledger and its constants; Paper V's sign-hook trace (Thm 7.1),
primitive-hook multiplicities at p=11, and smoothness beyond reading the proof; Paper
VI's cohomological transfers. Nothing suggests errors; these simply exceed what an
independent numeric pass can certify. The repository clone available to this review
contains only template files — none of the frozen proof sources, validators, or ledgers
cited by Papers IV–VI (`RQM_PROOF.md`, claim-status ledgers, census outputs). If those
live elsewhere, the data-availability statements should point at the exact public
location; as cloned, the reproducibility chain is broken at the repository step.

### 4.3 `n2_census.py` — new data on the crown (p ≤ 199)

Quadratic sector N₂(p) = #{d : x^p + x² + d irreducible} for the 44 primes
5 ≤ p ≤ 199:

- values 0..4; **N₂ = 0 at p = 31, 41, 59, 71, 97, 113, 131, 151, 157, 163, 197**
  (11 of 44 ≈ 25.0%);
- mean N₂ = 59/44 ≈ 1.341 vs the heuristic e/2 ≈ 1.359 (≈p/2 admissible d, each
  irreducible with probability ≈ e/p after the no-root conditioning);
- P(N₂ = 0) observed 0.250 vs Poisson(e/2) prediction e^{−e/2} ≈ 0.257.

The quadratic sector is, to the precision this sample can see, **a Poisson(e/2)
variable**: no rigidity, no witness law (the striking d = 2, 4, 8, 16 pattern at
p = 5, 7, 11, 17 is a small-prime accident), and it cannot carry the crown alone.
Consequences for mechanism design are drawn in MECHANISMS M1–M2.

Cubic sectors (p ≤ 31): W_p/p ≈ 0.77–1.43 with mean ≈ 1.1 — the crown's mass is in the
cubic sector, whose expected size is ~p, so failure W_p = 0 is a ~e^{−cp}-type
conspiracy in the random model. The problem is proving any of that.

Integrable-map diagnostics (predictions of the dynamical reframing, all confirmed):
the Chebyshev cubic graph polynomial x^p − (x³ − 3x) factors completely into pieces of
degree ≤ p/2 at every prime 7 ≤ p ≤ 61 (its roots are β + β^{−1} with β^{p∓3} = 1,
forcing small degrees); the special quadratic parameters d ∈ {0, ±2} (power-map /
Chebyshev conjugates) are reducible for every p ≥ 7. "Integrable maps fail; only
generic maps can win" is now an empirical law with a proof sketch (MECHANISMS M1).

### 4.4 `ordering_experiment.py` — where does the increasing order sit?

Fixed-harmonic frame energy ℰ^σ (a = 1, Gaussian ρ, shell [X², 2X²)), identity vs the
ordering ensemble:

| X | K | orderings | E(id) | ensemble mean ± std | percentile of id |
|---|---|---|---|---|---|
| 23 | 6 | all 720 | 9.497 | 10.018 ± 0.807 | 26.5% (z = −0.64) |
| 40 | 10 | 2002 sampled | 21.377 | 22.036 ± 0.892 | 23.9% (z = −0.74) |
| 53 | 12 | 502 sampled | 26.966 | 26.030 ± 0.834 | 86.3% (z = +1.12) |

At toy scales the increasing order is **bulk-typical, not extremal** — mildly low twice,
mildly high once, never past |z| = 1.2. Two readings: (a) nothing visible distinguishes
the identity ordering from a random one for this statistic, which is the best small-scale
news derandomisation could hope for; (b) there is also no monotone rearrangement
structure (sorted ≠ extremal) to exploit, so derandomisation-by-inequality looks
unpromising. Caveat: X ≤ 53 is far from any asymptotic regime.

---

## 5. Consolidated assessment

### 5.1 Load-bearing analysis

| Target | Status | If proved, yields | Blocking difficulty |
|---|---|---|---|
| Block variance (12.1)/(C1)–(C2) | open | **Fortune (all large n)** | HL-strength prime pairs at sparse exponential centres; parity |
| Density-one certificate (8.4) | open | Fortune for density-one n | moving-conductor zero statistics (Thm 8.3 blocks transfer) |
| Source→frame bridge (Routes A/B) | open | makes frame load-bearing | principal-term rebuild at μ_j; signed coupling |
| Frame target 𝔉_X ≪ MX^{o(1)} (increasing order) | open | nothing (without bridge) | derandomisation of Paper IV |
| HTE4 / HWF4 / RQHE4 | open | closes Paper I's program | centred rank-two dispersion; √V median loss |
| Transfer gap (III §8) | open | reciprocal sampling control | sparse exceptional sets vs e^{−√t} level sets |
| Crown W_p > 0 | open | function-field Fortune, d=1 | one-sided Frobenius nonvanishing; all cheap exits closed |

### 5.2 Strengths

- Exact-identity discipline: essentially everything checkable is checkable, and checks
  pass. The correction notices actively repaired a miscalibrated architecture.
- The negative results are the sequence's most durable assets: semiprime resonance, CRT
  ratio collapse, conductor migration, Lebesgue-vs-sampling transfer gap, aggregate-Betti
  refutation, fixed-point circularity, mod-p blindness, no-split, no-divided-hook. They
  fence off a large territory of plausible-but-doomed attacks.
- Paper IV's random-order theorem is a genuine, effective, structurally interesting
  theorem about cumulative prime products, independent of its role here.
- The function-field reduction (Papers V–VI) turns an intractable-looking problem into a
  concrete family of finite questions with a clean frontier statement.

### 5.3 Weaknesses and risks

1. **Bridge before frame** (§2.1): the integer-side effort is currently inverted.
2. **The integer variance targets are aspirationally labelled.** They are conjectures at
   the far edge of Hardy–Littlewood territory; the review recommends stating explicitly,
   in one place, that no path within current analytic technology reaches them, so that
   the frame/lab work is understood as the real programme.
3. **Paper IV's zero-margin ledger** is unaudited (by me); it should be mechanized.
4. **Reproducibility pointer rot** (§4.2): the cited repository does not (in this clone)
   contain the frozen artifacts.
5. **The lab's statistical reality check** (§4.3): N₂ = 0 for ~25% of primes means the
   crown genuinely requires the cubic sector; any mechanism that cannot see ~p-sized
   counts (e.g. anything mod p) is structurally insufficient — Paper VI's blindness
   results are thus not artifacts but the correct shadow of a Poisson-scale truth.

### 5.4 Verdict

As mathematics, the sequence delivers a large body of correct exact structure, several
strong unconditional theorems (Papers I, III, IV kernels; V–VI geometry), and an
honestly mapped frontier. As a programme toward Fortune's conjecture, the integer side
has reached its natural analytic boundary; the live frontier is (i) the missing
source→frame bridge, (ii) derandomisation as a structural question, and above all
(iii) the function-field crown, where this review's computations already sharpen the
target. Concrete proposals follow in `MECHANISMS.md`.
