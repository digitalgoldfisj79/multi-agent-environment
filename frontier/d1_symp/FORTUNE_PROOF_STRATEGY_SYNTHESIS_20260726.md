# Fortune proof-strategy synthesis

**Date:** 2026-07-26
**Provenance:** 16 agents, ~2.34M tokens, 358 tool calls. Five route designs
(function-field crown; function-field provable window; integer sieve; integer
conditional; reformulation), each stress-tested by two independent adversarial
reviews — one refutation pass, one feasibility pass — then synthesised.
**Status of this document:** produced by the design pass. It is reproduced
verbatim below. It is *not* uniformly verified. Read section 0 of this header
first.

## 0. Verification status — read before quoting anything

**Independently re-verified by me:**

- The window statement is strictly stronger than Fortune, not equivalent
  (one direction only).
- `T^p - T` is the **zero** map on `F_p`, not bijective, so
  `FRONTIER.md:151-153`'s justification of the degree-1 micro-lemma is wrong.
  Checked at `p = 5,7,11`. The lemma itself is true for a simpler reason.
- The deviation growth. On the committed 60-prime table
  `frontier/d1_data/scripts/N3_checkpoint.json` (`5 <= p <= 293`) the log-log
  slope of the deviation against `p` is **0.698** (max class) / **0.738** (min
  class), the ratio to `sqrt p` grows `1.30 -> 1.65 -> 1.92 -> 2.64`, and the
  ratio to `p` settles near `0.075`. Not `sqrt p`.
- That same table reproduces my independent census
  (`qline_census_reconciliation_verify.py`) exactly at every overlapping prime.

**Arithmetic I checked but did not verify against sources:**

- The Buchstab constant: `omega(2) = 1/2`, expected count `(e^gamma/2) p_n =
  0.8905 log N`, reciprocal `2e^{-gamma} = 1.1229`. The identification with
  Granville's refinement of Cramer's constant is consistent but I did not read
  Granville.
- `B >= (1 - e/3)p = 0.094p` from the proved degree-1 local factor, which is
  what makes `FRONTIER.md`'s `B(pi) = o(p)` target false rather than open.

**NOT verified — treat as claims to be checked:**

- The reading of Sawin arXiv:1809.05137 Prop 4.2 (per-irreducible vs
  aggregate `B(pi)`). This is the document's own highest-value action and it
  gates the whole function-field programme.
- The claimed Wan-Zhang 2025 improvement and its matching lower bound.
- The `CONDITIONAL_HL_BLOCK.md` main-term defect (`mu_j` vs `H`).
- The packaging table's claim that the fixed-class (`h=2`) target requires
  `B < 1` and is therefore unprovable by any Weil-type bound. This is the
  single most consequential unverified claim in the document, because it would
  retire the packaging I have been measuring all session.
- Maier's theorem as applied here; the `P_2` non-existence argument.

**Internal inconsistency to be aware of.** The route-verdict table (appendix)
records that `ff-window` — FRONTIER's "Target Theorem 1", claimed writable now
— was downgraded from `provable-now` to `needs-major-breakthrough` by **both**
adversarial reviewers. The synthesis nonetheless lists writing it as Step 6
("Weil only; a few pages"). Either the reviewers judged a stronger form than
Step 6 states, or Step 6 is too optimistic. Resolve before acting on Step 6.

**Corrections this document forced to my own earlier assessment**, all now
retracted in `FORTUNE_STRATEGY_RETRACTIONS_20260726.md`: the claimed
equivalence; "Fortune follows immediately from Cramer"; and the
`deviation <= C sqrt p` with `C <= 34` endgame, which fails because the
deviation is not `sqrt p`-scale.

---

# How I would try to prove Fortune's conjecture, and where I would stop

**Scope note.** Everything below is grounded in files I read and computations I ran in this repository today. Where I re-derived or re-measured something myself I say so; where I am relying on the committed record or on a review I did not verify, I say that too.

---

## 0. Verdict, up front

**Integer Fortune is out of reach with current technology.** Not by a constant, not by a logarithm — by an exponential in `log N`, and the failure is *categorical* (wrong quantifier) rather than quantitative. I would not spend further effort on it beyond writing up the no-gos.

**FF-Fortune(p,1) is reachable in principle but not in practice today.** It is a well-posed, finitely-checkable-per-`p` geometric statement. However — and this is the single most decision-relevant finding of this review — **the target as currently written in `FRONTIER.md` (`B(π) = o(p)`) is false**, and must be replaced by a sharp-constant statement whose constant nobody has yet pinned. There is also an unresolved reading of Sawin's Proposition 4.2 that may void the entire geometric packaging. That reading is cheap to settle and gates everything else.

The two targets must not be blurred: the integer problem lacks a mechanism; the function-field problem has a mechanism and lacks a bound.

---

## Part I — The integer conjecture

### I.1 The logic, stated correctly (a correction the repo needs)

The briefing, and several notes, call the window statement an *equivalence*. It is not.

Re-derived: if `1 < m < p_{n+1}²` is composite, its least prime factor is `≤ √m < p_{n+1}`, hence `≤ p_n`, hence divides `p_n#`, hence divides `p_n# + m`, which exceeds it. Therefore

> a prime in `(p_n#, p_n# + p_{n+1}²)` ⟹ `F_n < p_{n+1}²` ⟹ `F_n` prime.

The converse **fails**: Fortune permits `F_n ≥ p_{n+1}²` and prime. The window statement is *strictly stronger* than Fortune. Nobody has any handle on the other branch, so in practice all work targets the stronger statement — but it must be labelled that way. "Sufficient condition strictly stronger than the target" is the exact failure mode that has already consumed three routes in this repository.

### I.2 The correct heuristic — the free sieve is a *penalty*, not a bonus

`log N = θ(p_n) ~ p_n` and the window has length `(1+o(1))(log N)²`: Cramér scale, constant 1.

Admissible offsets are `1` together with the primes in `(p_n, p_{n+1}²]`. That is a survivor count at Buchstab parameter `u = log H / log p_n → 2`, where `ω(2) = 1/2 ≠ e^{-γ} = 0.5615`. So the expected count is

```
e^γ ω(2) · H/log N  =  (e^γ/2) p_n  =  0.8905 · log N,
```

which is **11% fewer than a generic interval of the same length**. The `e^γ log p_n` sieve boost is slightly over-cancelled by the thinning of admissible offsets. I measured this: for `n = 4…24` the observed count of primes in `(p_n#, p_n# + p_{n+1}²)` runs at ratio ≈ 0.9 to the generic `H/log N` (e.g. `n=24`: 108 observed vs 118.9 generic), and every `F_n` in that range is prime with enormous margin.

Two consequences worth recording:

* Fortune is true with an expected count growing linearly in `log N`; per-centre model failure probability `N^{-0.89}`, summable over the `~log Y/loglog Y` primorials below `Y`. The margin is probabilistic and huge. It is *not* a structural cushion.
* `1/(e^γ/2) = 2e^{-γ} = 1.1229` is exactly Granville's refinement of Cramér's constant — the same small-prime-divisibility mechanism, reciprocal. Since Granville conjectures `limsup gap/(log p)² ≥ 1.1229 > 1`, **Cramér's conjecture as currently believed does not imply Fortune.** Any proof must be local to primorial centres.

### I.3 Routes refuted, and by what

**Sieve theory (`int-sieve`) — dead.** For `A` = an interval of length `H`, `|A_d| = H/d + r_d` with `|r_d| ≤ 1`, so the usable level is `D ≤ H^{1-o(1)} = (log N)^{2-o(1)}`. Prime detection needs level exceeding `N` (the linear sieve needs `s = log D/log z > 2` at `z = N^{1/2}`, i.e. `D > N`; Friedlander–Iwaniec's asymptotic sieve for primes needs `N^{1-o(1)}` plus bilinear data). Worse, at `D = H` the linear sieve reaches `z = D^{1/2} = p_{n+1}` — exactly the free primorial sieve. **Residual sieve capacity is zero**, by the same square-root relation that gives the sieve for free.

Maynard–Tao is *structurally* void, not merely short: GPY-type weights produce primes for *some* `n` in a range; Fortune prescribes one centre per `n` and supplies no range to average over.

The consolation prize is also unavailable: the `P_2` relaxation of Fortune is **false**, because `q | m` with `q ≤ p_n` gives `p_n# + m = q·(N/q + m/q)`, so composite offsets are not excluded once "prime" is relaxed to "`P_2`". The Chen-style ladder does not exist here.

*Caveat to state carefully in any write-up:* "no sieve can do this" must be phrased as "no sieve whose only input is `|A_d|` for `d ≤ D`". Harman's sieve — which powers BHP's 0.525 — consumes Type II data as well.

**Almost-all / exceptional-set — dead.** Primorials below `Y` number `~log Y/loglog Y`, at most one per dyadic range. An almost-all theorem informs a *prescribed* centre only if its exceptional set has size `< 1`; Selberg's RH result at window `(log x)^{2+ε}` allows exceptional sets of size `Y^{1-o(1)}`. The gap is a full power of `Y`. This route was already run and stopped in `origin/archive/fortune-almost-all-20260719`.

The deeper point: **Maier (1985) proves unconditionally that the naive asymptotic fails at exactly this window scale, via matrices built on primorial moduli.** The exceptional set is provably non-empty and is constructed out of the very arithmetic feature that defines our centres. So no *general* short-interval equidistribution theorem can be the vehicle; the argument must be centre-specific.

**The conditional anchor (`CONDITIONAL_HL_BLOCK.md`) — calibration, not progress, and currently mis-normalised.** The proof is arithmetically correct; I re-read it and the `ε = o(log X/X)` threshold is right, with (H1) and (H2) binding equally. But:

1. *The main term is wrong.* `E_j = Ψ_j − H` uses main term `H`. Since `H = ηX² < ℓ_j²`, the admissible offsets are exactly the primes in `(ℓ_j, H]`, so the correct main term is `μ_j = e^γ H log ℓ_j / log H → (e^γ/2)H = 0.8905H` — the same Buchstab `u→2` effect as §I.2. As written, (H1) is false at a *constant* relative error `0.1095` against a budget `o(log X/X)`. This is repairable (recentre at `μ_j`), but nothing in that track should be quoted until it is.
2. *After every repair, the surviving hypothesis is strictly stronger than the conclusion.* It asks `Σ_j Ẽ_j² < (1−δ) min_j μ_j²` — the whole block variance below the cost of **one** failing centre. Zero exceptional-set tolerance means the "block average" is a pointwise-strength demand in average clothing, at RMS accuracy a factor `√N` tighter than Fortune needs.
3. *(H2) has no models per-shift and is trivial aggregated.* Per shift the budget `o(H)` sits below the natural CLT standard deviation by a factor `~√(X/log X)`. Aggregated over `d` — the only form the proof uses — the identity `Σ_{0<|d|<H} π_{2,j}(H;d) = Ψ_j² − Σ_m Λ²` makes it *identical* to the variance conclusion.

Total profit of the architecture over the conjectured Montgomery–Soundararajan value: **one factor of `log X`**, already committed at `RESEARCH_VECTORS.md` A4. Remark 4 of the file says as much.

**Moving the centre to multiples of `p_n#` — not progress.** The elementary reduction does survive verbatim on every multiple. But the qualitative theorem falls out of Dirichlet in two lines: fix a prime `m` with `p_n < m < p_{n+1}²`; infinitely many primes `P ≡ m (mod p_n#)`; then `N = P − m` has `F(N) ≤ m < p_{n+1}²`, hence prime. Linnik + Selberg sieve + Paley–Zygmund buys only a density upgrade — and the "strong Linnik" input (positive density in *every* class at `x = d^{O(1)}`) is not a theorem: a Siegel zero depletes the `χ₁ = +1` classes, and the range needed to defeat it (`log X ≫ √d`) is exponentially past the range the first moment permits (`log X ≪ (log d)²`). Independently: dilation **destroys the difficulty invariant**. At the true centre each admissible offset supplies exactly one candidate; after dilation it supplies `d⁴`. The window is preserved nominally; the problem is not.

### I.4 The ceiling, unambiguously

Integer Fortune requires a **pointwise** lower bound for primes in a window of length `(1+o(1))(log N)²` at a **prescribed, exponentially sparse** family of centres. Unconditionally we reach `N^{0.525}` (BHP); on RH, `N^{1/2} log N`; Guth–Maynard gives `N^{17/30}` for all `x` and `N^{2/15}` almost-all. Every conditional hierarchy in the standard toolkit (RH, GRH, GUE/pair correlation, Goldston–Montgomery, Montgomery–Soundararajan, HL-on-average) is an *average over `x`* with exceptional set of relative density at best `(log X)^{-O(1)}`; our centres have relative density `e^{-Θ(log N)}`.

The current best statement about `F_n` that anyone can prove: `F_n` is `p_{n+1}`-rough, so `F_n < p_{n+1}^{k+1} ⟺ Ω(F_n) ≤ k`, and BHP gives `Ω(F_n) ≤ (0.525+o(1)) log N/loglog N` (RH: `1/2`). The conjecture says `1`. The ratio diverges, and every rung of the ladder below "Cramér" is a polylog window, hence unreachable.

**Exactly what would have to change** — one of:

* **(i)** a prime-detection principle whose input is *not* a level of distribution. Sieve theory cannot supply this; the ceiling `D ≤ H` is information-theoretic for an interval.
* **(ii)** a transference theorem carrying almost-all-`x` short-interval asymptotics to a prescribed set of density `e^{-Θ(log N)}` — the "derandomization" wall already named at `FRONTIER.md` §5(4)(a), and provably obstructed in its uniform form by Maier.
* **(iii)** a Type-II/bilinear input for `{p_n# + m : m ≤ (log N)²}`. There is no candidate: no multiplicative parametrisation, the shift is a single fixed integer rather than an averaged parameter, and the set has only `(log N)²` elements.

Absent one of those, nothing in this repository or in the literature moves Fortune. **This is a known open problem in disguise — specifically, function-field-free Cramér at a prescribed point — and it is strictly harder than the target it is meant to serve.**

---

## Part II — FF-Fortune(p, 1)

### II.1 What is solid

Proved reduction; `p = 3` by hand; machine-certified for every odd `p < 1200`. The crown is exactly

> `#irred₄ > p − 1`, where `#irred₄ = #{(a,b,c,d) ∈ F_p⁴ : X^p + aX³ + bX² + cX + d irreducible}`.

The `a = b = 0` slice contributes exactly `p − 1` (for `c ≠ −1` the map `x ↦ x^p + cx = (1+c)x` is bijective on `F_p`, so a root always exists; only `c = −1, d ≠ 0` gives the `p−1` Artin–Schreier polynomials). **I re-verified `#irred₄ = 124, 426, 1660` at `p = 5, 7, 11` by exhaustive from-scratch enumeration**, matching the orbit assembly `(p−1) + p(p−1)N(p) + p(p−1)(N₊+N₋)/2` exactly.

Also solid: the quadratic family cannot carry it (`N(p) = 0` for 61 of 238 primes `≤ 1499`); the Airy analytic boulder is retired; exact-identity attempts (Hayes/Clausen) collapse to tautologies.

### II.2 Two corrections to the committed target, both load-bearing

**(1) `B_A = 0` is not uniform.** I ran `frontier/d1_symp/residual_gate_measurement_verify.py`: `B₊ = 0` uniformly, but **`B₋ = 6, 4, 6, 2` at `p = 11, 17, 23, 29`** — all `≡ 5 mod 6`. The live sufficient condition is `|N_A − C_A| < d_A = min(C_A, 2p − C_A)` with `C_A = p − 2 + B_A`, **not** `|N_A − (p−2)| < p−2`. The deviation list in the briefing is also a garble of two rows; the committed rows are `dev(+) = 5,3,9,9,5,3` and `dev(−) = 1,5,5,1,13,7`.

**(2) The deviation is not `~1.5√p`; it has a systematic linear component.** From the committed `N3` table (60 primes, `5 ≤ p ≤ 293`), measured by me:

| window | mean `σ_p = (N₊+N₋)/(2p)` | mean `max_A|N_A−(p−2)|/√p` | mean `max_A|N_A−(p−2)|/(p−2)` |
|---|---|---|---|
| `p < 50` | 0.984 | 1.30 | 0.397 |
| `50 ≤ p < 120` | 0.900 | 1.65 | 0.186 |
| `120 ≤ p < 200` | 0.912 | 1.92 | 0.153 |
| `200 ≤ p < 300` | 0.872 (s.e. 0.010) | 2.64 | 0.168 |

The normalised deviation *grows* against `√p` and *settles* against `p`. This is not new to the repo — `D1_ATTACK.md:95` already records relative error `≈ −0.16`, and Theorem D1.5 already *proves* the degree-1 local factor `(p²−1)/3` with leading constant `e/3 = 0.906`. **But it is inconsistent with `FRONTIER.md` §2 and §5(4)(b), which still state the sufficient condition as `B(π) = o(p)`.** On the proved local factor alone, any true bound `|Σ_I Λ − p⁴| ≤ B p³` forces `B ≥ (1 − e/3)p = 0.094p`. So `B(π) = o(p)` is **not merely open — it is false** unless the proved degree-1 stratum fails asymptotically.

The correct target is the sharp-constant form `B ≤ (1−δ)p`. The available window is a factor between about 6 and 11, and **the constant is currently unpinned**, between `0.094` (proved local factor) and `0.158` (the limit of the committed density fit `0.842 + 0.618/√p`). You cannot state the theorem you want to prove until this is settled.

### II.3 The packaging table — why the currently-pursued packaging is self-defeating

In the repo's reading of Sawin Prop 4.2, `|Σ_I Λ − p^h| ≤ B(π) p^{(h+2)/2}` at `n = p`, so "error < main" needs `B < p^{h/2 − 1}`:

| packaging | required `B` | true effective value |
|---|---|---|
| `h = 4` (full interval, `deg m ≤ 3`) | `< p` | `≈ 0.12p` — window ~8 |
| `h = 3` (average over the cubic coefficient `a`) | `< √p` | `≈ 0.12√p` |
| `h = 2` (fixed arithmetic class — the `N_A` q-line ledger) | **`< 1`** | below the minimum any Betti sum can take |

**Conclusion: the fixed-class target `|N_A − C_A| < d_A` cannot be closed by any Weil / Betti / Lang–Weil / Chebotarev bound, in principle.** It admits only an exact cancellation or congruence theorem. This is corroborated internally: the hook trace `E_ε(q) = Tr(F | H¹_c(U_q, hook))` takes values in `pZ`, and Frobenius weights on `H¹_c` of a curve with weight-0 coefficients are `≤ √p`, so whenever the count is not 1 the effective dimension is `≥ √p` and any fibrewise Weil bound on the q-line reproduces the trivial bound up to a factor 2.

The additive structure is also already spent: `X = {α ∈ A^p : e₁ = … = e_{p−4} = 0}` is a cone, `S_p`-stable, and (because `p₀ = p = 0` in characteristic `p`) stable under diagonal additive translation, so it carries a free `AGL(1)` action whose quotient is precisely the repo's 2-parameter normal-form surface. Quotienting *lowers the weight* and makes the requirement strictly harder. Any Betti gain must come from wild ramification on the 4-dimensional `X`, not from the group action.

### II.4 The caveat that gates everything

`Λ` detects a `p`-cycle in `S_p`, and `1_{p\text{-cycle}} = (1/p) Σ_{i=0}^{p-1} (−1)^i χ_{hook_i}` — **`p` hook characters**, which is precisely what the repo's own hook-projector machinery uses (`HOOK_Q_LINE_CLASS_PROJECTORS_20260724.md`). Sawin's Prop 4.2 has main term `q^{n−m} dim(π^{S_n})`, i.e. it is stated *per irreducible* `π`. If `B(π)` is per-`π` and the `Λ`-error aggregates over the `p−1` nontrivial hooks, the aggregate is `≥ p−1` by counting alone, and `B ≤ p−1` is satisfiable only in the extremal case where every hook sheaf has total compactly-supported Betti number exactly 1. In that case **the `h=4` geometric route as currently posed is void, not merely hard.** This cannot be resolved from the repository.

---

## The recommended programme, in order

**Step 0 — [bookkeeping] Correct the record before anything is quoted again.**
`FRONTIER.md` §2/§5(4)(b): replace `B(π) = o(p)` with the sharp-constant form (pending Step 1). Retract "the strongest Fortune-type statement provable in any setting today" — BHP gives the `Z`-analogue unconditionally at exponent 0.525; the honest claim is `1/2` vs `0.525`. Fix `FRONTIER.md:151–153`: the degree-1 micro-lemma does *not* hold because "`T^p − T` is bijective" (it is the **zero** map on `F_p`); the correct one-line reason is that a linear `m = aT + b` vanishes at `−b/a`, and so does the centre — which also shows the lemma holds at every multiple of `T^p−T`. Fix the ledger prose (`B₊ = 0` uniform, `B₋ ≠ 0`). Recentre `CONDITIONAL_HL_BLOCK.md` at `μ_j = e^γ H log ℓ_j/log H`, or withdraw (H1)/(H2) and keep only the one-sided recentred variance criterion with a pointer to `RESEARCH_VECTORS.md` A4.

**Step 1 — [new theorem / decisive literature check] Settle the reading of `B(π)`.** See "highest-value next action" below.

**Step 2 — [bookkeeping] Relocate the proved local factor into the main term.** State `Σ_I Λ = σ_p p⁴ + residual`, where `σ_p` is the local-density product whose degree-1 factor is exactly `(p²−1)/(3p²)` divided by `(1−1/p)^p → e/3`. This buys ~9%; its real value is that it moves a genuine weight-8 main-term constituent out of "error", after which the residual is the honest `p^{7/2}`-scale object and the Betti requirement relaxes from constant-sharp to `o(p)` *on the residual*.

**Step 3 — [bookkeeping, compute] Pin the constant.** Extend the `N3` census past `p = 293` with an independent implementation (fixed-cubic Frobenius recursion, `O(p³)` per test, `~2p⁵` per prime — needs C, not Python) to decide whether `σ_p → e/3 = 0.906` or the fit limit `0.842`. Realistic reach with a few days of compute: `p ≲ 400–500`. Without this you cannot state the theorem's constant, and you cannot tell whether the window is 6 or 11.

**Step 4 — [new theorem, out of reach with current technology] The crown.** `B ≤ (1−δ)p` for the compactly supported Betti sum of the hook-isotypic cohomology of `X = {α ∈ A^p : e₁ = … = e_{p−4} = 0}` over `F_p`. Available: Katz `3(p+2)^{2p−4}`. The reviews cite a January-2025 improvement (Wan–Zhang) that is still `p^{O(p)}` at `(n,r,d) = (p, p−4, ~p)` and comes with a *matching class lower bound* `(d−1)^n ≈ p^p` — I did not verify that paper, but if it holds, then no general-purpose estimate can ever supply this bound, and it must be an exact, structure-specific determination of monodromy for a wildly ramified family. The best wild-ramification Betti technology is linear in rank, and the hook ranks are `C(p−1,i)`. Classification: **Katz-monograph scale, not a thesis problem, no template, no smaller warm-up case** (the `h=2` sibling is empirically *false* a quarter of the time — `N(p) = 0` for 61/238 primes).

**Step 5 — [new theorem, cheap probe, near-zero prior] The one estimate-free mechanism.** A congruence or mass formula putting `#irred₄ − (p−1)` in a nonzero residue class mod some `M`. Known obstructions: every standard source of congruences on point counts (group actions, Chevalley–Warning, Ax–Katz, Newton polygon) yields *divisibility*, i.e. residue 0 — and the one exact congruence that exists here, `2p | #irred_a`, gives exactly that. Any mechanism generic enough would also force `N(p) > 0`, which is false. So the mechanism must distinguish cubic from quadratic. Exactly two free statistics exist (the discriminant/sign character, closed form via Stickelberger; and the `F_p`-root count, i.e. the cubic tail); a third would be needed. **Probe once, cheaply, then stop.**

**Step 6 — [bookkeeping] Write Target Theorem 1 at `d = 1`.** For every `p` there is `m` with `2 ≤ deg m ≤ ⌈p/2⌉ + O(1)` and `T^p − T + m` irreducible. Weil only; a few pages; the exact minimal admissible window is `n/2 + log_q n − O(1)`, a full `log_q n` tighter than `FRONTIER.md` claims. It is the only statement that keeps the true centre. The window is a factor `~p/6` too wide; advertise it as nothing more.

**Step 7 — [do not do].** Anything that moves the centre (dilates, multiples): the qualitative statement is two lines of Dirichlet and dilation destroys the difficulty invariant. Any "almost all centres" FF statement: `T^p−T` is provably atypical (no degree-1 offset ever works there, and it is Katz's worst-case additive centre). Any re-attack at fixed `a`: that packaging needs `B < 1`.

---

## Single highest-value next action

> **Retrieve Sawin, arXiv:1809.05137, and pin down exactly what `B(π)` quantifies in Proposition 4.2 — one irreducible `π`, or the aggregate over the `p` hook representations into which `Λ`'s `p`-cycle class function decomposes — then re-derive from scratch, in that normalisation, the sufficient condition for `#irred₄ > p−1`.**

Why this rather than the census or the geometry. It is a half-day literature check with three outcomes, all decisive:

* **If `B` is aggregated:** the crown becomes the sharp-constant statement of Step 4, the programme has a well-posed (if Katz-monograph-hard) target, and Steps 2–3 are the correct preparation.
* **If `B` is per-`π`:** the `Λ`-error is `≥ p−1` by counting alone, `FRONTIER.md`'s standing target is not merely false-with-a-constant but structurally unattainable, the `h=4` geometric route as posed is void, and the only survivors are the congruence probe (Step 5) and constructive dynamics. That saves an unbounded amount of Betti-bound effort.
* **Either way** it fixes the one number — the required constant — without which no theorem statement can be written down.

No other action in the programme has the property that everything downstream (whether to spend days of compute on Step 3; whether Step 4 is a target at all) depends on its answer.

---

## Refutation ledger

| Claim / route | Refuted by |
|---|---|
| "Fortune ⟺ prime in `(p_n#, p_n#+p_{n+1}²)`" | Only ⟸ holds; Fortune permits `F_n ≥ p_{n+1}²` and prime |
| "The primorial's free sieve makes the window prime-rich" | Buchstab at `u=2`: `e^γω(2) = 0.89 < 1`; measured ratio ≈ 0.9 for `n ≤ 24` |
| "Cramér ⟹ Fortune" | Granville's `2e^{-γ} = 1.1229 > 1` — same mechanism, reciprocal constant |
| Sieve route (Maynard–Tao, almost-primes, APs mod `p_n#`, exceptional sets) | Level ceiling `D ≤ H^{1-o(1)}`; GPY needs a range to average over; the `P_2` relaxation is false; primorial density `log Y/loglog Y` |
| Block-averaged conditional HL | Wrong first-moment normalisation (Buchstab `u→2`); per-shift (H2) has no models; aggregated (H2) ≡ the conclusion; surviving criterion strictly stronger than the target, zero exceptional-set tolerance; total profit one `log X`, already committed |
| Dilated-centre "Fortune-type theorems" | Two-line Dirichlet argument gives the qualitative statement; dilation replaces one candidate per offset with `d⁴` |
| `B(π) = o(p)` (`FRONTIER.md`) | Proved degree-1 local factor `e/3` + measured density force `B ≥ 0.094p`; `D1_ATTACK.md:95` already had `−0.16` |
| "deviation `~1.5√p`" (briefing) | Committed table: relative deficit settles at `0.15–0.17` with no decay; `dev/√p` grows 1.30 → 2.64 |
| "`B_A = 0` uniformly for `p ≡ 5 mod 6`" (briefing) | Repo verifier: `B₋ = 6,4,6,2` at `p = 11,17,23,29`, all `≡ 5 mod 6` |
| Airy absolute-constant target; Hayes/Clausen exact identities; rank-four Adams realisation; fixed-`a` estimates | Previously closed in-repo; the `h=2` packaging additionally needs `B < 1`, below any Betti sum |

---

## Honest bottom line

Fortune's conjecture is true with an enormous but purely probabilistic margin — `0.89 log N` expected primes where one suffices. Neither target is close to proof, but for different reasons and they should be tracked separately.

**The integer conjecture is out of reach and I would stop working on it.** The only known reduction lands on a Cramér-strength pointwise statement at an exponentially sparse family of centres; sieve theory has zero residual capacity there by an information-theoretic ceiling; every averaged conjecture in the hierarchy has the wrong quantifier; and the uniform form of the statement one would want is provably false by Maier, whose counterexamples are built out of primorials. Three specific things would have to change (§I.4); none has a candidate mechanism.

**The function-field crown is a real target with a real defect in its current statement.** It is one theorem away — but that theorem is not the one written in `FRONTIER.md`, it needs an exponential-to-linear collapse *plus* a constant sharp to within a factor of about 8, and there is an unresolved reading of the key proposition that may void the packaging entirely. Settle the reading first. Everything else is downstream of it.

---

## Appendix: route verdicts

Each route was designed, then reviewed twice independently (refutation pass, feasibility pass).

| route | design verdict | survived refutation | survived feasibility | corrected verdicts |
|---|---|---|---|---|
| `ff-crown` | needs-major-breakthrough | no | no | needs-major-breakthrough, needs-major-breakthrough |
| `ff-window` | provable-now | no | no | needs-major-breakthrough, needs-major-breakthrough |
| `int-sieve` | dead | no | no | dead, dead |
| `int-conditional` | dead | no | no | dead, dead |
| `reformulate` | provable-now | no | yes | dead, provable-now |

Every route was refuted by at least one reviewer. Only `reformulate` survived either pass.
