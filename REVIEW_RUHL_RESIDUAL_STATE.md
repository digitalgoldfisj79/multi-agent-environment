# Independent review — programme state at FORTUNE_RUHL_SELECTED_TUPLE_RESIDUAL_V0_1

**Reviewed state:** branch `gpt56/fortune-ruhl-selected-tuple-residual-v01-20260806`,
head `d1f2b98`, PR #65 (open, mergeable), stacked on the LCSK tree-graph,
PWOC-SF and RUHL-FM consolidation branches; frontier correction commit
`6f33a24` and `EXTERNAL_REVIEW_RESPONSE.md` also reviewed.

**Relation to prior review:** `REVIEW_INT_SCME_PROGRAMME.md` (commit `029cc8c`)
was accepted in full; this review assesses the four programmes executed since.

---

## 1. Summary verdict

**The governance response was correct and complete, the new mathematics is
sound, and — for the first time in this audit trail — the claims match the
content with no hidden strengthening found.** The cycle produced one genuine
conditional theorem with sharp explicit constants, three honest structural
obstructions, and zero unconditional progress, exactly as its own ledger now
states ("conditional architecture sharpened; unconditional distance to Fortune
unchanged"). PR #65's terminal ruling and its `DIRECT_NEXT_STEP.md` stop-order
are the right call. I recommend merging PR #65 as written.

Everything below was independently re-derived or recomputed; all spot-checked
figures reproduce exactly.

## 2. What this cycle actually established

### 2.1 RUHL-FM consolidation — the conditional theorem (verified correct)

Theorem R1 is a correct, fully elementary finite implication. I checked each
step: the terminating binomial expansion `(1−q)^z = Σ (−q)^k (z)_k/k!`; the
even-Bonferroni upper truncation (valid for `0 ≤ q ≤ 1`); the integral-form
Taylor remainder `0 ≤ S_K(x) − e^{−x} ≤ x^{K+1}/(K+1)!` for even `K` (valid
for all `x ≥ 0`, no term-monotonicity needed); the stratum aggregation to
detector < 1 and zero-row exclusion. Corollary R2's constant checks exactly:
`β = 5`, `ε = 0.10`, `ρ_b ≤ 1.10` gives `α = 5·ln(5/(e·1.3·1.1)) = 1.2588 >
1.20`, confirming the parent programme's `β = 10` was valid but non-minimal.

The `FRONTIER_MAP.md` strength audit is honest where it most matters: the
signed RUHL condition "is close to an upper bound on the truncated detector
discrepancy itself … should not be advertised as a deep reduction." That
sentence is the correct self-application of the circularity finding from the
previous review.

### 2.2 PWOC-SF — small real theorem plus honest impossibility

The fixed-order squarefree collision extension (`R_β ≤ U_r·C(n−1, r+1)` under
the bounded-weight contract) is a genuine if modest extension of the
prime-modulus walk lemma, with the divisor-subset growth stated rather than
hidden, and the hockey-stick summation kernel-checked. The adversarial W0
result (a weight concentrated on one gap-dividing modulus makes uniform
`R_β = o(D_β)` impossible for unrestricted weights) is correct and useful. The
decisive honest finding is negative: no source coefficient family exists in
the repository to which the theorem could attach — `SOURCE_WEIGHT_CONTRACT_NOT_
AVAILABLE`, `NO_TRANSFER_TO_RUHL_OR_SOCG` are accurate labels.

### 2.3 LCSK tree-graph — a correct and informative refutation

The counterexample is exact. For a same-residue triple at one post-terminal
prime `p`, the connected coefficient is the third cumulant of a shared
Bernoulli(1/p) event, `κ₃ = (p−1)(p−2)/p³ ≍ 1/p`, while any spanning-tree
majorant with edge constant `C` totals `3C²/p²`. The ratio is exactly
`(p−1)(p−2)/(3C²p) → ∞` — I verified the stated `(p−2)/(3C²)` asymptotic in
exact arithmetic at `p = 101, 1009, 10007`. So the pair-to-all-orders
tree-graph route to `INT-LCSK` is dead, and the Brun–Titchmarsh hyperedge
fallback's `D_r ≍ X/(log X)^{1+1/(r−1)}` correctly shows absolute-value
ledgers lose the fixed `δ`. `INT-LCSK` now demonstrably requires *signed*
higher-body cluster input — a real narrowing of the search space, which is
what a negative result is for.

### 2.4 RUHL selected-tuple residual (PR #65) — the direct lane closed honestly

Three findings, all verified:

- **R1 (tautology made exact).** `ℰ_{b,K} = avg B_K(Z_j;q_b) − avg
  T_K(q_bλ_j)` is an exact identity (checked; also regression-tested in exact
  rational arithmetic by the committed script). The signed condition *is* the
  truncated detector discrepancy; the document says so plainly.
- **R2 (strength inversion).** Since `q_b|E_{b,1}| ≤ 𝒜_{b,K}`, the sharp
  absolute envelope forces `|E_{b,1}| < Δ_b/q_b`. I recomputed the registered
  panel independently: allowance `0.6877` at `X = 100`, `0.9159` at `X = 10⁶`
  — matching the claimed `0.688` and `0.916`. So termwise-absolute RUHL
  demands the deterministic model predict a size-`X` mean to additive accuracy
  `< 1`: strictly stronger than `INT-SCME`. The conditional hypothesis is
  therefore *harder* at first order than the wall it was hoped to bypass —
  an important and correctly drawn conclusion.
- **R4 (Heath–Brown dichotomy).** The frozen identity and its convolution
  proof are correct (`δ−A` supported above `z`, hence `(δ−A)^{*J}` above
  `z^J`), and the committed verifier genuinely checks the identity on finite
  panels. The scale table reproduces exactly (`J_min = 73, 543, 4343, 36192`;
  `log₁₀ 2^{J_min} = 21.98, 163.46, 1307.37, 10894.88`). The dichotomy —
  logarithmic order leaves divisor variables beyond `H`; forcing `z ≤ H`
  costs coefficient mass `exp(Θ(X/log X))` against a margin `≍ log X/X`;
  keeping cancellation recombines to `Λ` — is rigorous *as a closure of the
  termwise-absolute implementation*, and the nonclaims section correctly
  scopes it as such.

The Lean module matches its description: three elementary real/`Finset`
lemmas, now advertised at exactly their actual scope. The validation-language
inflation criticized in the previous review has been fixed.

## 3. Where we are, in plain terms

The programme now consists of:

1. **One honest conditional theorem** (unconditional as a finite
   implication): sharp even-Bonferroni criterion ⇒ `INT-AOD` ⇒ eventual
   Fortune, with explicit constants (`β = 5` certificate) and a precise
   statement of the conjectural input it needs.
2. **A ring of verified obstructions** around every standard mechanism
   family: BDH/large-sieve variance (post-terminal band), direct
   Friedlander–Iwaniec (exponential scale gap), Vaughan/Heath–Brown termwise
   (cancellation loss), switching (almost-primes only), pair-tree cluster
   expansion (triple counterexample), absolute hyperedges (vanishing δ),
   unrestricted-weight PWOC (adversarial example).
3. **Zero unconditional progress toward Fortune**, correctly labelled.

Every surviving lane terminates at one of four statements, and their
relations are now correctly recorded: `INT-SCME` (Cramér-scale mean);
signed higher-body clusters for `INT-LCSK`; a source contract for PWOC-SF2;
the jointly signed tuple residual for RUHL — the last being close to the
detector target itself and containing a strengthened SCME at first order.
There is no remaining bookkeeping illusion of a smaller frontier.

## 4. Watch items and minor errata (none affect conclusions)

1. **Frozen-geometry drift.** R2 states `M_b ≍ X/log X`, while the inherited
   stratum geometry has `n_b ≍ X/(log X)^{5/2}` with `B = polylog(X)`. With
   the inherited values, `Δ_b/q_b` is `O((log X)^c)` rather than `O(1)`. The
   conclusion is unaffected — polylog allowance against a size-`X` mean still
   forces near-constant relative accuracy, strictly stronger than `INT-SCME`
   — but the panels' `M = X/ln X` normalization should be reconciled with the
   inherited `n_b B` or the discrepancy noted in R2.
2. **One-sided slack at first order.** `E_{b,1}` enters `ℰ_{b,K}` with
   coefficient `−q_b`, so an *excess* actual mean helps the detector; the
   weakest first-order requirement is one-sided (`E_{b,1} > −Δ_b/q_b + …`),
   not two-sided. This does not change the difficulty class — a lower bound
   to additive `O(polylog)` accuracy on a size-`X` mean is still far beyond
   `INT-SCME` — but R2's "absolute value" phrasing gives away a sign that a
   future signed attack would exploit, and the ledger may as well record it.
3. **Stacked merge order.** PR #65's base is the LCSK branch, itself stacked
   on PWOC-SF and the consolidation. Merge from the bottom of the stack up,
   or re-target PR #65 at the default branch after the intermediate merges.
4. The `ρ_b ≤ 1.10` registered ratio (model means within 10% across a
   stratum) is a frozen modelling assumption inside the conditional
   certificate; harmless while everything is conditional, but it should
   travel with the theorem statement whenever R1 is quoted.

## 5. Recommendation

- **Merge PR #65.** Its claims are accurate, its negative results are real,
  and its stop-order is correct.
- **Honor `DIRECT_NEXT_STEP.md`.** No new autonomous programme inside the
  existing mechanism families; the admissibility bar (a genuinely new signed
  selected-centre tuple theorem with a proved implication to the frozen
  margin) is the right gate, and this review found no candidate that clears
  it.
- **The one justified next artefact is expository, not exploratory:** a
  single self-contained document (paper-shaped) assembling Theorem R1 with
  its constants, the detector chain to eventual Fortune, the primorial
  collision lemmas, and the obstruction ring — each obstruction stated with
  its exact scope. That is a publishable conditional-and-barriers package,
  and it is the only deliverable this line of work can currently support.
