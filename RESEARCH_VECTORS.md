# New exact results and progression vectors for the Fortune programme

**Date:** 2026-07-20
**Status of everything below:** the results in Part A are exact statements with
proof sketches and independent numerical validation (script:
`research_vectors_checks.py`); none is a step toward unconditional Fortune.
The vectors in Part B are ranked proposals. Nothing here proves PGD2 or
Fortune's conjecture. Notation follows Paper II.

---

## Part A — new exact results (verified now)

### A1. Difference-multiplicity dichotomy for the pair-sum walk

**Claim.** For X sufficiently large, every nonzero difference of two distinct
pair sums S_u − S_v has multiplicity in the difference multiset
{S_u − S_v : u ≠ v} equal to exactly

- **N**, if the difference equals P_i − P_k for some i ≠ k
  (the N representations are the "sliding" pairs (S_{ij}, S_{kj}), j < N), or
- **1**, otherwise.

There are exactly N(N−1) differences of the first kind and
M(M−1) − N²(N−1) of the second kind.

*Proof mechanism:* S_u − S_v = S_{u'} − S_{v'} is the four-copy relation
S_u + S_{v'} = S_{u'} + S_v, so Lemma 4.1 (four-copy rigidity) forces
endpoint-multiset equality; classifying the multiset solutions gives exactly
the sliding family. Numerically confirmed at N = 9: multiplicity histogram is
{1: 1332, 9: 72}, with 1332 = M(M−1) − N²(N−1) and 72 = N(N−1) exactly.

**Consequence (exact energy split).** For every harmonic a,

    E_a = N · G_a + S_a,

where G_a = Σ_{i≠k} |Ψ_a(P_i − P_k)|² is the *single-walk* energy (the
F-kernel object, N² terms) and S_a ≥ 0 is the multiplicity-free part. Since
S_a ≥ 0,

    E_a ≤ M X^{o(1)}   ⇒   G_a ≤ (M/N) X^{o(1)} ≈ (N/2) X^{o(1)}.

So single-walk dispersion at scale N is a **necessary sub-target** of PGD2 —
strictly smaller (N² terms instead of M²) and therefore both a cheaper
falsification testbed and a mandatory first checkpoint for any proposed
mechanism. A mechanism that cannot prove G_a ≪ N X^{o(1)} cannot prove PGD2.
This refines the "collapse to the single H₂ polynomial" of the archived
endpoint-sector decomposition into an exact two-scale statement.

### A2. Exact sixth moment and the full moment law

**Claim (exact sixth moment).** Under six-copy rigidity (X large),

    ∫₀¹ |H₂(θ)|⁶ dθ = (45N⁶ − 189N⁵ + 438N⁴ − 597N³ + 443N² − 136N) / 4.

Interpolated exactly from brute-force collision counts at N = 2..9 and
verified on held-out N = 10, 11.

**Claim (third centred moment).**

    ∫₀¹ (|H₂|² − M)³ dθ = N(N−1)²(37N³ − 115N² + 174N − 136) / 4
                         = 74 M³ (1 + O(1/N)).

Verified by brute force at N = 3, 5, 7.

**Claim (general even-moment law).** For every fixed k with k < X/8
(so that 2k-copy rigidity holds),

    ∫₀¹ |H₂|^{2k} dθ = ((2k)! / 4^k) · N^{2k} · (1 + O_k(1/N)),

an exact polynomial in N computable by the same multiset combinatorics
(leading coefficient = [(2k−1)!!·k!]²/(2k)! = (2k)!/4^k; verified at
k = 2, 3, 4). Interpretation: the moments of H₂/√M match those of g²/√2
for a standard complex Gaussian g to leading order, with O_k(1/N)
corrections, at every fixed order the rigidity range allows.
The kernel K = |H₂|² − M is a half-squared-Gaussian object: mean 0, second
moment 5M², third moment 74M³ (Gaussian-model predictions 5 and 74 match the
exact leading coefficients).

### A3. Sub-Weibull Lebesgue tail at all levels, and the transfer gap

**Claim.** There are absolute constants c > 0 (one may take c = 1.3) and C
such that for all C·M ≤ λ ≤ M² and X sufficiently large,

    meas{ θ : K(θ) ≥ λ } ≤ e · exp(−c √(λ/M)).

*Proof:* Chebyshev with the 2k-th moment. The crude count
∫|H₂|^{2k} ≤ M^k · (2k)!/2^k (each solution's endpoint multiset admits at
most (2k)!/2^k ordered pair-decompositions) needs only 2k-copy rigidity,
valid for k < X/8; optimizing 2k ≍ √(λ/M) stays inside that range even at
the maximal level λ = M² (where √(λ/M) ≈ N/√2 ≈ X/(√2 log X) < X/8).
Numerics at N = 24 (200k exact-arithmetic samples): −log meas / √(λ/M) is
stable at ≈ 1.5 for λ/M = 2..64, matching the Gaussian-model constant √2.

**Consequence (quantified transfer gap).** The level-set target (4.5) of
Paper II demands only μ_{X,a}{K ≥ λ} ≪ M X^{o(1)}/λ, while Lebesgue measure
satisfies exp(−c√(λ/M)). Since supp μ has ≤ π(2H)² = X^{4+o(1)} atoms of
mass ≥ X^{−4+o(1)} each, PGD2 can fail at level λ = tM only if at least
X^{4+o(1)}/t of the X⁴ reciprocal pairs (q, r) land in a θ-set of Lebesgue
measure exp(−c√t). The open problem is thus exactly a *sparse exceptional-set
bound*: the arithmetic sampling points must merely avoid being
exponentially-anomalously concentrated — the allowed overshoot over Lebesgue
is a factor exp(c√t)·(1/t)·X^{o(1)}, i.e. exponentially generous. This
sharpens "transfer problem from Lebesgue to the reciprocal measure" (Paper II
Theorem 4.2 discussion) into a quantitative statement of how little is
actually needed.

### A4. Explicit-constant margin in Theorem 2.4

The proof of Theorem 2.4 gives B_X ≤ 4C·L(X)/(η log X)·(1+o(1)), so the
hypothesis L(X) = o(log X) can be relaxed to

    L(X) ≤ (η/(4C) − ε) · log X.

Meanwhile the Goldston–Montgomery/Montgomery–Soundararajan heuristic value of
the block variance is Σ_j |E_j|² ≈ N·H·log(P_j/H) ≈ NHX, i.e. L ≍ 1.
The criterion therefore carries a genuine factor-log X safety margin: even a
method losing a small constant times log X over the conjectured truth still
proves Fortune for every centre. Worth recording in any revision, since it
widens the class of admissible proof mechanisms.

---

## Part B — progression vectors (ranked)

### B1. Paper III candidate: the exact conditional anchor (most writable)

Neither Paper II nor the phase reports states the clean conditional theorem.
Adapt Montgomery–Soundararajan to the primorial centres:

**Target statement.** Let π₂,j(H; d) = Σ_{m≤H} Λ(P_j+m)Λ(P_j+m+d), and let
𝔖_j(d) be the singular series truncated at the primes ≤ ℓ_j (the local
factors of larger primes are 1 + O(1/X) here, since every p ≤ ℓ_j divides
P_j). Suppose the Hardy–Littlewood approximation

    π₂,j(H; d) = 𝔖_j(d)(H − |d|) + O(H·ε(X))

holds uniformly in j < N and 0 < |d| < H, together with the first-moment
analogue, with **relative error ε(X) = o(log X / X)**. Then hypothesis (2.7)
holds with L(X) = O(1) and Fortune's conjecture follows for all sufficiently
large n.

Bookkeeping that makes it work: the diagonal Σ_m Λ² ≈ HX per centre already
saturates the NHX budget (allowed, since L = O(1) = o(log X)); the
off-diagonal error budget per centre is H²·ε ≤ HX·o(log X), giving the
threshold ε = o(log X/X). Notable: this is *barely more than a 1/X saving* —
far weaker than square-root cancellation in H (which would be ε ≈ X^{−1}
exactly, up to the log). So the honest headline is: "Fortune follows from
uniform-in-centre HL at quality o(log X/X); square-root-quality HL is a full
log factor stronger than necessary." The mathematical work is the exact
𝔖_j second-moment lemma (the truncated-singular-series analogue of
Montgomery–Soundararajan's Σ(H−d)𝔖(d) asymptotic); everything else is
Theorem 2.4. Risk: low. Value: turns the programme's boundary into a
citable conditional theorem parallel to Goldston–Montgomery.

### B2. GRH model theorem: the i.i.d.-prime walk (provable, isolates the gap)

Replace the deterministic steps ℓ₁ < ℓ₂ < … (consecutive primes in [X, 2X))
by i.i.d. uniform draws from the primes of [X, 2X), keeping the true prime
shell for (q, r). **Claim (provable under GRH):** E[E_a] ≪ M X^{o(1)}, i.e.
PGD2 holds in expectation for the randomized walk.

Sketch: a difference D_uv factors as A_X Q_min(±1 ± R₁ ∓ R₂ …) with the R's
products of later steps; E e_{qr}(bR) expands over characters mod qr with
Gauss-sum coefficients ≤ (qr)^{−1/2}, and each step contributes the factor
|Σ_{ℓ∈P[X,2X)} χ(ℓ)| / π-count, which under GRH is ≪ X^{−1/2+o(1)}. Five
steps of separation beat the (qr)^{1/2} ≈ X² character count; index-gap < 5
pairs contribute O(M·X^{o(1)}) trivially.

Why this is worth doing despite being a model result: it certifies that the
reciprocal-frame architecture is sound (the target is *true* for a generic
walk, conditionally), and it factorizes the remaining difficulty into exactly
two named gaps: (i) **the character-sum wall** — unconditional sums over
primes in [X, 2X) to modulus qr ≈ X⁴ sit at length y ≈ (conductor)^{1/2}·…
where no unconditional method applies (Burgess covers the full interval,
length X = q^{1/2} > q^{1/4}, but not its primes; Vaughan/Heath-Brown Type-II
ranges are absent); and (ii) **derandomization** — consecutive primes versus
i.i.d. primes, where no step-averaging exists. This matches, and makes
precise, the factorial-audit conclusion that the walk sits at the critical
length N ≍ q^{1/2}/log q.

### B3. The T(D) reframing: equidistribution of one huge integer mod many primes

Writing T(D) = Σ_{q~Q prime} p_{q,a} e(aD/q), PGD2 is exactly square-root
cancellation of T on average over the M² structured differences:
E_a = Σ_{u≠v} |T(D_uv)|². Since D_uv = A_X Q_i(R − 1)-type integers, q ∤ D
reduces everything to the distribution of (D mod q)/q as q varies over the
shell primes for fixed exponentially-large structured D. This is the
"equidistribution of a fixed huge integer modulo varying primes" problem —
for which no individual-D technology exists (it is not a Kloosterman-fraction
sum; reciprocity does not apply). This is where genuinely *new mathematics*
would have to live, and the honest statement is that every known
reformulation returns to the same kernel — consistent with the archive's
no-go inventory. Flagged as the locus, not as a route.

### B4. Micro-target: top-level atom counting (from A3)

A3 reduces the top dyadic levels of PGD2 to: show that at most X^{4−δ}/t
pairs (q, r) satisfy K(θ_{q,r}) ≥ tM for t ≥ X^δ. A fully resonant pair
forces all N walk phases into alignment mod qr — an extremely rigid event.
The archived TOP_LEVEL_RESONANCE_GATE shows power-scale large values give
only diffuse phase bias (no divisor pinning), so this counting problem is
likely the same wall — but the *counting* formulation (bounding the number of
resonant pairs, rather than extracting divisibility from one) has not been
separately closed and is the sharpest small question the new tail theorem
isolates.

### B5. Cheap numerics upgrade via A1

The necessary sub-target G_a has N² ≈ X²/log²X terms versus M² ≈ X⁴ for E_a,
so finite panels for the single-walk energy can reach X several times larger
than the X = 350/700/1200 panels in the archive at equal cost. If G_a's
normalized edge ever detaches from the matched random-walk null as X grows,
PGD2 is dead (by A1's necessity); continued agreement is the cheapest
available stress test of the architecture. Diagnostic only, per the
programme's evidence standards.

---

## Verification

`research_vectors_checks.py` (same directory) reproduces: the sixth-moment
polynomial (interpolated N = 2..9, verified held-out at N = 10, 11), the
(2k)!/4^k leading law at k = 2, 3, 4, the third-centred-moment formula
(brute-forced at N = 3, 5, 7), the multiplicity dichotomy at N = 9, and the
sub-Weibull tail constant ≈ 1.5 at N = 24 with exact phase arithmetic.
