# Proposed New Mechanisms for Progress on Fortune's Conjecture

Companion to `REVIEW.md`. Each mechanism states: the target it attacks, why it is new
relative to Papers I–VI, concrete first steps, and an honest risk assessment. Empirical
claims below come from `scripts/` runs performed for this review (p-census to 199,
ordering experiments, identity verification).

Priority order (argued in §Roadmap): **M1 → M3 → M7 → M4 → M6 → M5 → M2′**, with M1/M3
on the function-field crown as the main line.

---

## M1. The dynamical reframing: Frobenius as an explicit polynomial map

### The observation

Let f = X^p + aX³ + cX + d over F_p (Paper V's depressed family; the quadratic sector
X^p + X² + d is the same with φ quadratic). If α is any root of f, then

    α^p = −(aα³ + cα + d) =: φ(α),        φ ∈ F_p[x],  deg φ ≤ 3.

Since φ has F_p-coefficients, Frobenius commutes with φ, so for every l ≥ 1:

    α^{p^l} = φ^l(α)     (φ^l = l-fold composition).

**Consequences (all elementary, none used in Papers V–VI):**

1. *Frobenius acts on the p-element root set of f as the map φ.* f is irreducible
   ⟺ φ permutes the roots of f in a single p-cycle.
2. *Factor degrees are φ-periods*: deg_{F_p}(α) = min{l : φ^l(α) = α}. Hence

       f irreducible  ⟺  gcd(φ^l(x) − x, f) = 1  for all l ≤ p/2,

   which incidentally gives an O(p) -step irreducibility test whose step is one
   composition h ↦ φ(h) mod f (used in `n2_census.py`; this is how the census to
   p = 199 costs seconds, not hours).
3. *The crown is a statement in arithmetic dynamics*: W_p > 0 says that among the ~p³
   maps φ(x) = −(ax³+cx+d) (plus the quadratic sector), at least one has its
   "skew-Frobenius graph" {x^p = φ(x)} consisting of a single p-cycle.

The quadratic sector is, up to the conjugation x ↦ −x, the Mandelbrot family
ψ_d(x) = x² + d over F_p. The crown's hardest-to-kill sector is thus the best-studied
family in arithmetic dynamics (functional graphs of x²+c mod p; arboreal Galois
representations; Jones, Boston–Jones, Juul et al.).

### The integrable/generic dichotomy — now a proved-and-verified law

For special ("integrable") φ the equation x^p = φ(x) is solvable in closed form and
forces reducibility. Example (Chebyshev): if φ = T₃ (x³ − 3x) and α = β + β^{−1}, then
in characteristic p, α^p = β^p + β^{−p} and T₃(α) = β³ + β^{−3}, so α^p = φ(α) ⟺
β^{p−3} = 1 or β^{p+3} = 1. All roots are β + β^{−1} with β a root of unity of order
dividing p ∓ 3, so all factor degrees divide ord(p mod (p∓3))-type quantities — far
below p. **Census confirmation:** x^p − (x³−3x) factors entirely into degrees ≤ p/2 at
every prime 7 ≤ p ≤ 61; the quadratic specials d ∈ {0, ±2} are reducible at every
p ≥ 7. Power maps are analogous (β^{p∓3} ↦ β^{p−3} with α = β).

So: *integrable maps provably fail; the crown needs one generic map per prime.* This is
structurally identical to "special L-functions have zeros forced by symmetry; generic
ones don't" — and it suggests the right question is not "which (a,c,d) works" but "can
the family conspire to be simultaneously degenerate".

### What the statistics now say (census, p ≤ 199)

- Quadratic sector: N₂(p) ~ Poisson(e/2) to the visible precision (mean 1.341 vs
  e/2 ≈ 1.359; P(N₂=0) = 0.250 vs e^{−e/2} ≈ 0.257; zeros at
  p = 31, 41, 59, 71, 97, 113, 131, 151, 157, 163, 197). **No rigidity, no witness law.**
- Cubic sector: N_sq + N_ns ≈ 2.2p on average (p ≤ 31), so W_p ≈ 1.1p. In the random
  model, P(W_p = 0) ≈ e^{−cp}: failure at even one large prime is a massive conspiracy;
  Σ_p P(fail) converges extremely fast. The crown is "true with overwhelming margin";
  the entire difficulty is deterministic positivity.

### Proposed work

1. **(Theorem-level, cheap)** Write up the skew-Frobenius correspondence and the
   integrable classification: determine exactly which (a,c,d) give φ conjugate to
   power/Chebyshev/Lattès-type maps and prove those f reducible for p beyond a small
   bound. This yields the first *structural* theorem about which interval members fail,
   and shrinks the crown to the non-special locus.
2. **(Average over p — the realistic milestone)** Prove the crown for **almost all p**
   via vertical statistics: for the quadratic family, the l-th obstruction
   "gcd(ψ^l(x) − x, x^p − ψ(x)) ≠ 1 for all admissible d" is governed by the reduction
   mod p of finitely many *fixed* integral dynamical resultants (the l-periodic
   polynomials of x²+d and their compositions with the graph condition). Effective
   Chebotarev/large-sieve over the parameter d and the prime p simultaneously is a
   plausible route to: "for all p outside a density-zero set, W_p > 0". No result of
   this shape exists in Papers I–VI, and nothing in their closed-routes lists blocks it.
3. **(Connect to existing dynamics literature)** The condition "φ-orbit structure of the
   graph x^p = φ(x)" is a cousin of the factorization statistics of iterates studied by
   Boston–Jones ("settled" polynomials) and of Juul's Galois-of-iterates theorems. A
   dynamical-monodromy statement of the form "for non-special φ, the Galois group of
   x^p − φ(x) over F_p(a,c,d) is as large as the geometry allows" would put the crown
   in reach of a Hilbert-irreducibility-over-F_p argument. First step: compute these
   Galois groups for small p symbolically and formulate the precise largeness statement.

**Risk.** The almost-all-p statement (2) is genuinely plausible but the "for all
admissible d simultaneously" quantifier is where parity-like difficulty could
reappear; (3)'s function-field Hilbert irreducibility has known pathologies at small
q. Even so, this is the first mechanism in the programme with a *statistical* route to
an unconditional theorem about infinitely many p.

---

## M2′. Quadratic-sector rigidity — **proposed, tested, and refuted by this review**

The original proposal M2 ("N₂(p) = 1 with a lawful witness d(p); prove it and the crown
follows") was based on N₂ = 1 at p = 5, 7, 11 with witnesses 2, 4, 8 (and 16 at p=17).
The census **kills it**: N₂(199 census) takes values 0..4, vanishes for ≈25% of primes,
and matches Poisson(e/2). The witness sequence 2,4,8,16 is a small-prime accident.

Retained value:

- It is now an *empirical theorem* that any crown mechanism must engage the cubic
  sector; nothing that ignores N_sq + N_ns can work (this includes any future "mod p"
  or "single-orbit" idea — reinforcing Paper VI's blindness results from the statistics
  side).
- The Poisson(e/2) law itself is a sharp, provable-looking target: "N₂(p) has Poisson
  moments as p → ∞" is a clean unconditional statement (cf. rootless-polynomial
  densities) that would be the first distributional theorem about the interval, and its
  method (moments of irreducible counts in the special family x^p + x² + d) is a
  warm-up for the cubic sector.

This section is kept deliberately: a mechanism proposed, computed, and refuted within a
day is the lab working as intended.

---

## M3. The p-adic slope route past Paper VI's blindness theorems

### Rationale

Paper VI proves the semisimple/ℓ-adic and mod-p layers cannot see the crown (Frobenius
blindness; W_17 ≡ 0 mod 17 kills mod-p congruences). What is *not* closed — and not
attempted — is the p-adic slope filtration **above** mod p:

- The Cartier moment M_a (Paper VI §2) is exactly a Hasse–Witt/Cartier-operator datum:
  the unit-root (slope-0) information of the level curves {g = r} ⊂ Y_a.
- The counts N_a = #{g=1}(F_p) obey Dwork-style trace formulas whose eigenvalue slopes
  are constrained by Newton-above-Hodge (Adolphson–Sperber for the associated
  exponential sums; Wan's theorems on generic Newton polygons and unit-root
  L-functions).
- The failure configuration is not just "W_p = 0" but (by Paper VI §4) the sharpened
  pattern M(a) = 1 − a^{p−1}, i.e. U_p = −1, V_p = 0: *total degeneracy of the
  Cartier layer in both cubic classes simultaneously.* Slope theory is precisely the
  technology for excluding total degeneracy in families.

### Proposed work

1. **Compute** the Cartier/Hasse–Witt matrices of the Artin–Schreier level curves
   {y^p − y = g} over the (c,d)-family for p up to a few hundred (finite linear algebra;
   same cost class as the census). Empirical questions: do the slopes of the family's
   Frobenius follow Wan's generic Newton polygon? Is the observed nonvanishing of M_a
   (Paper VI reports only one exception, sq class at p=5) a generic-Newton statement?
2. **Formulate** the crown-sufficient slope statement: a lower bound "the unit-root part
   of H¹_c of the level curve is nonzero for at least one (a,c,d)" — equivalently, not
   all members of the family are supersingular-at-level-1. Family-wide supersingularity
   is exactly the kind of statement Newton-polygon theory refutes (dimension counts on
   Newton strata à la Katz/Oort-style, adapted to wild AS families).
3. **Target congruence depth 2**: since mod p is blind but W_p ≈ 1.1p = O(p), the value
   of W_p is determined by information at p-adic precision 2 (Witt vectors of length 2 /
   Berthelot–Bloch–Esnault slope-<2 cohomology of 𝒬_p). Concretely: express
   #𝒬_p(F_p) = 1 + (p−1)W_p through rigid cohomology of the quotient with its single
   wild point, and compute the slope-<1 part from (1); the discrepancy from ≡ 1 mod p²
   is a function of W_p mod p (nonzero for 5 ≤ p ≤ 31 except p=17 in our data —
   determine how often W_p ≡ 0 mod p before investing further).

**Why new:** Papers V–VI stay in ℓ-adic étale cohomology and characteristic-0
representation rings; the one p-adic object introduced (the cyclotomic tangent) is shown
undetermined by *modular* data — but slope data is exactly the refinement the blindness
family Φ_λ does not preserve. **Risk:** wild ramification makes the AS-family Newton
theory delicate (Swan conductors ~p); it is possible the generic Newton polygon
degenerates on this special sparse family — but determining that is itself decisive
information, and step (1) is cheap.

---

## M4. Martingale structure for HTE4/HWF4, and HWF4 in the random-order model

### The √V loss is a martingale artefact

Paper I §5.3: separate Cauchy–Schwarz over the median m loses √V because it treats the
median channels {L_m(χ)} as unrelated vectors. But F_m(χ) = Σ_{j≤m} χ(Q_j) is a
*path* whose increments F_{m+1} − F_m are single terms (or single blocks, in the
block-decomposed HWF4 form): with respect to the filtration by prefixes, the
median-channel vectors are (deterministic functions of) a process with orthogonal-ish
increments under the (r, χ)-average — Paper I's own Theorem 3.4 (average
almost-injectivity) is exactly an increment-orthogonality statement at second order.

**Proposal:** prove HWF4 (the hereditary weighted fourth moment,
Σ_i L_i (|F_i^R|² − N_i^R)² averaged over shell characters ≪ π(R,2R)V³m·X^{o(1)}) by a
Burkholder/Doob square-function argument in the character average: fourth moments of a
process with L²-orthogonal increments are controlled by the square function plus the
increment fourth moments, and the latter are short-support objects controlled by Paper
I's Theorem 6.1 (support families of size ≤ V^{5/2}). The missing ingredient is an
almost-orthogonality of increments at *fourth* order — which is exactly the k ∈ {1,2}
overlap sectors of the pair-overlap decomposition, i.e. the same objects, but now
localized to short blocks where Theorem 6.1 already wins. A careful bookkeeping of
this bootstrap (long moments from short moments + martingale inequality) is the most
promising purely-unconditional route left inside Paper I's world.

### HWF4 generically

Independently: Paper IV's machinery (rank conditioning, contour decay, ledger) was
built for the pair-sum kernel, but nothing in it is specific to pair sums. Running the
same proof for the hereditary square function should give

    E_σ[HWF4 energy] ≪ π(R,2R) V³ m (log X)^{O(1)},

i.e. **HWF4 holds for almost all orderings**. Payoff: HWF4 — a strictly simpler,
single-walk object — becomes the canonical derandomisation target, unifying Papers I
and IV on one statement (Paper I proves it *sufficient* for edge closure; Paper IV's
method proves it *generic*). First step: redo Paper IV's configuration taxonomy for
4-tuples from one walk instead of pair-sum differences (the coefficient patterns are the
m = 2, 3, 4 cases already enumerated in Paper IV Lemma 3.3).

**Risk:** the martingale bootstrap may lose a log-power per scale and there are ~log X
scales; the generic-HWF4 claim needs its own zero-margin ledger. Both are
well-scoped, falsifiable, medium-effort projects.

---

## M5. Split the derandomisation barrier: GRH input + a named "prime-walk
equidistribution" hypothesis

Paper IV's only arithmetic input on characters is the sixth-moment bound
β ≪ X(log X)³ for "bad" ratio characters (t_χ ≥ 3/4). Under GRH for Dirichlet
L-functions mod qr, *every* nonprincipal character is good
(Σ_{ℓ∈[X,2X)} χ(ℓ) ≪ X^{1/2+ε}), so β = 1. Rerunning the ledger with β = 1 collapses
the bad-pattern classes entirely — but the σ-average is still doing the real work:
pointwise (for the increasing order) the objects are sums along the deterministic walk,

    Σ_j χ(Q_j),   Q_j = ℓ_1⋯ℓ_j   (increasing order),

and GRH controls the *increments* χ(ℓ), not the equidistribution of the *partial-sum
path* (χ(Q_j))_j on the unit circle. That is a genuinely different statement — a
deterministic-walk analogue of Weyl equidistribution:

**PWE (prime-walk equidistribution, to be formalized):** for all but
O(π(R,2R)/X^δ) shell primes r and all but X^{o(1)} characters χ mod r,
|Σ_{j≤V} χ(Q_j)| ≪ V^{1/2} X^{o(1)}.

Proposed work: (1) make PWE precise and prove PWE + GRH ⇒ the frame target for the
increasing order, by auditing exactly which ledger steps used order entropy (prediction:
only the contour bound, which PWE replaces); (2) study PWE itself — its second moment
over (r, χ) is Paper I Theorem 3.4 (true unconditionally!); its fourth moment is HWF4
(M4). So the PWE ladder is: 2nd moment ✓, 4th moment = HWF4, pointwise = open.

**Why valuable even if PWE is hard:** it converts "derandomisation" from a vague gap
into a hierarchy of moment statements, the first rung of which is already proved, and it
cleanly separates the GRH-shaped input from the genuinely new input. **Risk:** PWE at
pointwise strength may be as deep as anything else here; the audit (1) could also reveal
irreducible uses of order entropy — which would itself be a publishable no-go theorem.

---

## M6. Ordering extremality: experiment done, inequality route closed, concentration
route open

Experiment (`ordering_experiment.py`, §4.4 of REVIEW.md): at X = 23/40/53, the
increasing order's frame energy sits at the 26th/24th/86th percentile of the ordering
ensemble (|z| ≤ 1.2). Conclusions:

1. **No rearrangement inequality**: sorted order is not extremal for the frame energy;
   attempts to prove ℰ^id ≤ (mean) by a monotone-rearrangement argument are
   empirically dead. (Negative result, worth recording so nobody tries.)
2. **Concentration is the remaining probabilistic hope**: prove Paper IV's suggested
   second moment E_σ[(ℰ_a^σ)²] ≪ M²(log X)^{O(1)} — the same partition/contour method
   over 8-endpoint configurations (the taxonomy grows but stays finite) — giving
   ordering-concentration. Concentration never reaches a specific permutation, but
   combined with any future *invariance* principle (e.g. an exchange argument showing
   ℰ changes by o(std) under adjacent transpositions of far-apart primes) it would
   shrink the derandomisation gap to a purely local statement. The experiment's
   bulk-typicality is consistent with such an invariance.
3. Rerun the experiment at larger X (needs the mod-q cumulative-product trick already
   in the script; cost is linear in #orderings sampled) before investing in (2), to
   check the percentile does not drift systematically.

---

## M7. Bridge first, and test it in the function-field laboratory

The integer-side strategic inversion (REVIEW §2.1): no theorem connects the frame to
the corrected prime-pair source. Rather than attacking Route A/B in the integers —
where the principal-term rebuild needs unavailable prime-pair asymptotics — build the
**entire pipeline in F_q[T] first**, where every quantity is finitely computable:

1. Define the analogue: centres P^σ_j = (polynomial primorial prefix products), offsets
   in the candidate-collapse window (degree ≤ 2d+1, Paper V Prop 2.1), detector =
   irreducibility counts; frame = reciprocal pair-sum energy with shell = irreducibles
   of the appropriate degree; all over small q where everything is enumerable.
2. Compute both sides exactly for many blocks: does frame energy at the critical scale
   *empirically* co-vary with detector variance? If yes, the lab data will suggest the
   correct principal term for Route A (the recentred one-sided detector) — the missing
   ingredient in Paper II's programme. If no, that is strong evidence the frame is the
   wrong deterministic proxy and the programme should be re-pointed before more
   derandomisation work (this is exactly the falsification the integer setting cannot
   provide).
3. Separately, the *function-field random-order theorem* (Paper IV's proof transplanted
   to F_q[T]) should be provable with the same ledger and cleaner character theory —
   worth doing because in F_q[T] the "identity ordering" question can be *brute-forced*
   for small blocks: one can literally check whether the increasing order is exceptional
   among all orderings for the true detector, not just the frame.

**Why new:** Papers V–VI use the function field only for the d=1 crown; the frame/source
machinery of Papers II–IV has no function-field counterpart yet, and it is the cheapest
place to close the programme's central logical gap. **Risk:** low technical risk;
the risk is interpretive (small-q artifacts), mitigated by varying q.

---

## Roadmap

| Step | Mechanism | Type | Cost | Blocks on | Payoff if it works |
|---|---|---|---|---|---|
| 1 | M1.1 integrable classification + skew-Frobenius writeup | theorem, cheap | weeks | — | first structural theorem about interval membership |
| 2 | M3.1 Cartier/Hasse–Witt + Newton-slope census | computation | days | — | decides whether slope route is live |
| 3 | M1.2 almost-all-p crown | theorem, hard | months | 1 | first unconditional "W_p > 0 for density-one p" |
| 4 | M7.1–2 function-field bridge testbed | computation + theorem | weeks | — | fixes integer-side priority; principal term for Route A |
| 5 | M4 HWF4: martingale proof attempt + random-order HWF4 | theorem | months | — | unifies I+IV; canonical derandomisation target |
| 6 | M6.2 E_σ[(ℰ)²] concentration | theorem | months | — | ordering concentration |
| 7 | M5 PWE formalization + GRH audit | theorem/no-go | weeks–months | 5 helps | converts derandomisation into a moment ladder |
| 8 | M3.2–3 unit-root nonvanishing / depth-2 congruence | theorem, hard | open-ended | 2 | plausibly the crown itself |

Guiding principles distilled from the review and the day's computations:

- **The lab is cheap and it talks back**: M2′ went from conjecture to refutation in one
  census run. Every mechanism above with a computational step (2, 4, and the M6/M1
  numerics) should be run before any long proof attempt.
- **Nothing mod p, nothing semisimple, nothing aggregate-Betti** can decide the crown —
  that combination of Paper VI's theorems with the Poisson statistics should be treated
  as a design constraint, not a suggestion.
- **On the integer side, moment ladders beat point targets**: the PWE ladder
  (2nd ✓ / 4th = HWF4 / pointwise) and the concentration ladder (mean ✓ Paper IV /
  variance = M6.2) are the two places where each rung is a self-contained theorem.
