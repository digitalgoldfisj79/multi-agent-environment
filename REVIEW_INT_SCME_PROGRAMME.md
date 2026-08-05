# Independent critical review — integer Fortune programme at INT-SCME

**Reviewed state:** branch `gpt56/fortune-int-scme-selected-centre-mean-v01-20260805`
(head `8d5d8f0`), draft PR #59, issues #58 (`INT-SCME`), #60 (`INT-SCVAR`),
#61 (`INT-SCPT`), plus the inherited `INT-SOCG` and `INT-AOD` closeouts.

**Reviewer stance:** independent; no programme conclusion assumed. All exponent
arithmetic re-derived from scratch; collision lemma re-proved; literature ranges
checked against the standard sources.

---

## 1. Summary verdict

The low-level mathematics in this programme is correct. The exponent
bookkeeping in M4/M5, the primorial collision-energy lemma, the microblock
aggregation, the prime-power subtraction, the Barban–Davenport–Halberstam (BDH)
range correction, and the unconditional large-sieve obstruction all check out
under independent re-derivation. The self-correction recorded in
`CORRECTION_RECORD.md` (retracting the invalid use of the `HQ log H` BDH scale
at `Q = H^(2/3)`) is a genuine and important catch.

The high-level logical framing, however, materially overstates what was
achieved, in three ways:

1. **The `INT-SCVAR + INT-SCPT ⇒ INT-SCME` "bridge" is a tautology, not a
   reduction.** Conditional on `INT-SCVAR`, `INT-SCPT` is *equivalent* to
   `INT-SCME`, not smaller than it (§3).
2. **The claimed chain `INT-SCME ⇒ INT-SOCG` does not exist in the record.**
   The `INT-SOCG` closeout itself leaves `INT-LCSK` (all-orders connected
   cumulants) and `INT-PWOC` (composite-modulus walk) open; `INT-SCME` supplies
   only the first-cumulant input (§4).
3. **The terminal status `METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE` is defensible
   only for a narrow claim** — that the *unconditional selected-residue
   variance* route fails — while the closeout language suggests the programme
   isolated two new, smaller obstacles. It did not: one "obstacle" is a named
   open conjecture of Montgomery type, the other is the original problem
   restated (§3, §5).

No error was found that invalidates a stated theorem. The errors are errors of
*framing and logical bookkeeping*, which in a programme of this governance style
are as consequential as analytic errors, because the frontier issues drive the
next allocation of effort.

---

## 2. What was independently verified and is correct

- **Collision-energy lemma.** For consecutive primorial rows at index distance
  `d`, `P_j − P_{j'} = P_{j'}(Π − 1)` with `Π ≤ (2X)^d`, so fewer than `d`
  prime moduli `q > 2X` can collide the pair. Hence
  `Σ_{2X<q≤Q} Σ_a r_q(a)² ≪ RQ/log Q + R³`. Verified: the argument is exact,
  and `verify_collision_multiplicity.py` honestly tests the strict pairwise
  inequality on finite panels.
- **Conditional exponent region (M4).** Re-derived independently: with
  `V(H,Q) ≪ HQ(log H)^C`, per-row relative errors are `X^(δ−ρ/2)` (diagonal)
  and `X^((ρ+δ−1)/2)` (collision), giving admissibility exactly for
  `2δ < ρ < 1−δ`, optimum `ρ = 2/3`, `δ < 1/3`. Confirmed by exact rational
  arithmetic.
- **Unconditional obstruction (M4/M5).** With the large-sieve bound
  `V ≪ (H+Q²)H(log H)^C` and `Q > H^(1/2)` forced (the band must sit above the
  terminal primes, `q > 2X ≈ (2H)^(1/2)`), the relative error exponent is
  `1/2 + 3δ/2 − ρ/2`, positive for every `δ > 0`, `ρ ≤ 1`. Confirmed. The
  structural point is sound and worth keeping: *the post-terminal band begins
  exactly where the large sieve becomes trivial.* This is forced by the
  problem, not by a lane choice.
- **BDH/Montgomery–Hooley range correction.** The unconditional `HQ log H`
  variance scale requires `Q ≥ H/(log H)^A`; formulas valid for all `Q ≤ H`
  retain an `H²/(log H)^A` term which dominates `HQ` at `Q = H^(2/3)`. The
  correction record states this accurately. The cited GRH-conditional
  benchmark range `Q ≥ H^(1/2+ε)` is consistent with Friedlander–Goldston,
  *Variance of distribution of primes in residue classes* (Q. J. Math. 47,
  1996).
- **Band main term (M5).** `Σ_{2X<q≤X^{1+δ}} log q/(q−1) = (δ+o(1)) log X` by
  Mertens; main term `(δ+o(1)) H log X`. Correct.
- **Friedlander–Iwaniec scale gap (M2).** The output integers have size
  `exp((1+o(1))X)` while all available progression information in the offset
  variable is polynomial in `X`; the required level of distribution is
  exponentially out of reach. Correct, and robust to the exact FI exponent.
- **M1/M3.** The weighted-mean ⇒ first-cumulant implication and the microblock
  aggregation are exact. (Minor erratum in M1, §7.)

---

## 3. Finding A — the parity-tail "reduction" is circular

This is the central criticism. Define, as in M6,

```
D_Q(n) = Σ_{2X<q≤Q, q prime, q|n} log q,      R_Q(n) = Λ(n) − D_Q(n).
```

Three observations, all immediate from the definitions:

1. `D_Q` **vanishes on every prime output** (a prime `n ≈ e^X` has no divisor
   in `(2X, Q]`). So the band average `𝒟_C(Q)` is *entirely composite mass*,
   and `T_C = 𝒟_C + ℛ_C` is the trivial identity
   `prime mass = composite band mass + (prime mass − composite band mass)`.
2. The pointwise trivial bound is `R_Q(n) ≥ −D_Q(n)`, i.e.
   `ℛ_C ≥ −𝒟_C = −(1/3−ε)H log X` under `INT-SCVAR`. The `INT-SCPT` target
   `ℛ_C ≥ −(1/3−ε−κ)H log X` is therefore *exactly* "beat the trivial bound by
   `κ H log X`" — and `κ H log X` is exactly the `INT-SCME` target.
3. Hence, **conditional on `INT-SCVAR`, `INT-SCPT` ⟺ `INT-SCME`** (up to the
   `o(1)` in the band asymptotic). Without `INT-SCVAR`, `INT-SCPT` is not even
   normalized (its threshold references a band mass that cannot be evaluated).

The `SUCCESSOR.md` / PR #59 / issue #58-comment framing — "the programme
separates **two independent** subordinate inputs" — is therefore wrong as a
statement of logical structure. The decomposition `Λ = D_Q + R_Q` is not
analogous to Vaughan or Heath–Brown: there, the remainder has *bilinear
structure* that admits estimation by different tools. Here `R_Q` carries the
full von Mangoldt function with no structural handle, and M7 itself documents
that every structured method fails on it. Nothing about `INT-SCPT` is easier,
smaller, or differently shaped than `INT-SCME`; it is `INT-SCME` minus a
computable term.

The Lean artefact confirms this diagnosis: `SelectedCentreMeanCriterion.lean`
formalizes the bridge as two `linarith` lemmas over ℝ
(`target ≤ band + tail` from `bandLower ≤ band`, `−tailLoss ≤ tail`,
`target ≤ bandLower − tailLoss`). That is the *entire* formal content of the
"exact formal bridge". It contains no number theory because the bridge contains
none.

**Consequences.** Issue #61 should not stand as a subordinate target parallel
to issue #60. It should either be closed as `EQUIVALENT_TO_INT_SCME_GIVEN_
INT_SCVAR`, or explicitly re-labelled as such. Any future programme that
"attacks INT-SCPT" is attacking INT-SCME under a different name, and the ledger
should say so to prevent effort from being booked twice against the same wall.

---

## 4. Finding B — the chain `INT-SCME ⇒ INT-SOCG` is not established

The working chain quoted in the frontier documents,

```
INT-SCVAR + INT-SCPT ⇒ INT-SCME ⇒ INT-SOCG ⇒ INT-AOD ⇒ eventual Fortune,
```

fails at its second link, by the programme's own records:

- The `INT-AOD` closeout defines `INT-SOCG` as **two** requirements per
  stratum: the mean lower bound `c_{1,b} ≥ L_b ≥ cX` **and** the all-orders
  connected-cumulant bound `|c_{k,b}| ≤ c_{1,b} k! D_b^{k−1}` with
  `D_b ≪ X/(log X)^{1+δ}` for *every* `k ≥ 2`.
- The `INT-SOCG` closeout proves the repeated-column factorial–Stirling
  transform (radius cost one) and subcriticality of the *pairwise* (`k = 2`)
  local interaction, and then states plainly: "The all-orders local connected
  tree or hypergraph theorem `INT-LCSK` **remains open**", and "the weighted
  squarefree-composite extension [`INT-PWOC`] **remains open**".

So `INT-SCME` supplies the first-cumulant input only. Issue #58's language
("sole primary integer frontier"; all-orders connectivity as "secondary open
targets") and the SCME README's phrase "the completed `INT-SOCG -> INT-SCME`
reduction" invert the logical structure: what was completed is the *isolation
of a necessary input*, not a reduction of `INT-SOCG` to `INT-SCME`.

This matters for difficulty triage. `INT-LCSK` is an all-orders
Hardy–Littlewood-type correlation statement, uniform in the order up to
`k ≍ log X`, on the deterministic primorial path. There is no reason to regard
it as easier than the mean — on current technology it is plausibly *harder*
(the mean needs one positivity statement; `INT-LCSK` needs a full family of
correlation asymptotics/bounds). Booking it as "secondary" hides roughly half
of the remaining distance to `INT-SOCG` behind the label of the other half.

For completeness: the links that *do* hold up are
`INT-SOCG ⇒ INT-AOD` (the exponential-detector argument, with the
row-dependent-temperature part kernel-checked) and
`INT-AOD ⇒ eventual Fortune` (a zero-free row gives a prime offset
`m ≤ H = X²/2 < p_next²`, and any composite least-offset below `p_next²` would
carry a prime factor ≤ ℓ_j dividing `P_j`; hence the least offset is prime for
every sufficiently large terminal prime). Those two implications are sound.

---

## 5. Finding C — difficulty class of the remaining objects, stated plainly

- **`INT-SCVAR`** (issue #60) is a Montgomery-type variance conjecture:
  `V(H,Q) ≪ HQ(log H)^C` at `Q = H^(2/3−o(1))` restricted to prime moduli
  `q > 2X ≈ (2H)^(1/2)`. Unconditionally it sits strictly beyond
  Montgomery–Hooley (correctly documented). Under GRH it lies within the
  Friedlander–Goldston range `Q ≥ H^(1/2+ε)`, so it is *conditionally*
  available. It is the less hopeless of the two inputs — but it is a named
  open conjecture, not a programme-sized "subordinate target".
- **`INT-SCPT`** (issue #61) is `INT-SCME` itself (Finding A). And
  `INT-SCME`, stripped of apparatus, asks for positive prime mass in windows
  of length `H ≍ (log P_j)²` around the exponentially sparse deterministic
  centres `P_j = ℓ_j#`, with only polynomial-in-`X` (i.e. polylog-in-`P_j`)
  averaging available over rows. This is Cramér-scale territory: no known
  technique — unconditionally *or under GRH* — detects primes in polylog
  windows around specified points, and the row-averaging here is exponentially
  too thin to change the regime. The M2 scale-gap audit says this in effect;
  the closeout should say it outright instead of presenting a "two-wall"
  picture in which both walls look like technical estimates. The true picture:
  **wall 1 is GRH-hard; wall 2 is the entire original problem.**

Consequently the honest reading of the terminal status is narrower than the
closeout suggests: what was *proved* is that the selected-residue
Cauchy–variance mechanism cannot run unconditionally (correct, and the
computation is clean); what was *not* achieved is any reduction, conditional
or otherwise, of `INT-SCME` to something smaller than itself.

---

## 6. Finding D — validation gives less assurance than its vocabulary implies

- The "8,655/8,685 Lean jobs" are overwhelmingly mathlib compilation. The new
  formal content on this branch is two `linarith` lemmas over ℝ (§3). The
  phrase "full Lean package … formal trust audit passed" is accurate but
  decorates arithmetic-free content with proof-assistant authority.
- The Python verifiers are exact rational-arithmetic regressions of the
  programme's *own bookkeeping* (exponent inequalities, the band-plus-tail
  identity on synthetic numbers, finite collision panels). They are genuinely
  useful — this layer caught the BDH range error — but none of them verifies
  a statement about primes at scale, and the sentinel names
  (`FULL_CLEANROOM_PASS` etc.) should not be read as mathematical validation
  of the analytic claims. The `M8` factor-profile script is properly labelled
  diagnostic-only.

---

## 7. Minor errata

- **M1** ("every proper prime power in `(P_j, P_j+H]` is a square"): false as
  stated — a cube or higher power can land in the interval. Harmless: powers
  `p^k`, `k ≥ 3` near `P_j` are spaced `≫ P_j^{2/3} ≫ H` apart, so there are
  `O(1)` of them per row, within the claimed `O(X(log X)²)` budget. Wording
  should be "squares dominate; higher powers contribute `O(1)` terms per row".
- **Issue #58**, "When `H < 2√P_j`": trivially true (`H = X²/2` vs
  `√P_j = e^{(1+o(1))X/2}`); stating it as a hypothesis suggests a constraint
  that does not exist.
- **M5/issue #60 normalization**: `E_q(a)` is defined against `H/(q−1)` while
  the band application needs `(θ(H) − θ(U_b))/(q−1)`; consistent at the stated
  `o(1)` precision, but the definitions should match.

---

## 8. Is there a materially better route?

Within unconditional technology: **no.** The audit's closures of
Bombieri–Vinogradov, BDH, direct Friedlander–Iwaniec, Vaughan/Heath–Brown, and
switching are each correct, and the underlying reason is uniform: every known
method supplies distribution information at scales polynomial in the *offset*
window, while prime detection here is indexed at the *output* scale
`exp((1+o(1))X)`. No decomposition rearranges that gap. The programme should
resist any future lane that reintroduces the gap in disguised form (as the
retracted first draft did, and as the `INT-SCPT` framing risks doing).

What the programme *has* within reach, and currently undervalues, is the
**clean conditional theorem**. The genuinely novel, checkable content produced
across the three closeouts is:

1. the exponential-detector machinery `INT-SOCG ⇒ INT-AOD ⇒ eventual Fortune`
   (sound, partially kernel-checked);
2. the `RUHL-FM` route already recorded in the `INT-AOD` closeout: row-uniform
   Hardy–Littlewood factorial-moment estimates through order `Θ(log X)` imply
   `INT-AOD` by even Bonferroni truncation — "a complete conditional
   implication";
3. the primorial collision-energy lemma and the post-terminal large-sieve
   obstruction (publishable as an explicit barrier computation).

Consolidating (1)–(3) into a single self-contained statement — *"uniform
all-order Hardy–Littlewood correlations on the primorial path (plus, where
used, a Montgomery-type variance at `Q = H^{2/3−o(1)}`) imply that all
sufficiently large fortunate numbers are prime"* — with the conjectural inputs
stated once, precisely, and honestly labelled as strong open conjectures,
would be a real result of the recognized conditional genre, and is a materially
better use of the next execution cycle than iterating on `INT-SCPT`, which
Finding A shows cannot produce progress distinct from `INT-SCME` itself.

## 9. Recommended ledger actions

1. Amend PR #59 / `FINAL_STATUS.md` / `SUCCESSOR.md`: replace "two independent
   subordinate targets" with "one open variance conjecture (`INT-SCVAR`,
   GRH-hard, conditionally available) plus a statement (`INT-SCPT`) equivalent
   to `INT-SCME` given `INT-SCVAR`".
2. Re-label or close issue #61 accordingly; keep issue #60 as the only genuine
   subordinate object.
3. Correct the chain language in issue #58 and the SCME README: `INT-SCME` is
   a necessary input to `INT-SOCG`, not equivalent to it; `INT-LCSK` and
   `INT-PWOC` must appear at the same frontier level.
4. Add a one-paragraph difficulty statement to the frontier: the mean target
   is prime detection in `(log P)²`-windows at exponentially sparse structured
   centres — beyond GRH-scale technology — so all unconditional lanes must be
   evaluated against that bar before execution.
5. Keep the correction-record discipline; it worked.
