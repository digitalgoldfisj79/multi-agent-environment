# Hostile independent review: punctured-centre full-band Fortune reduction

Reviewer: Claude (fresh-model cold review, per
`FRESH_MODEL_REVIEW_PROMPT_PUNCTURED_CENTRE_20260729.md`)
Date: 2026-07-29
Reviewed state: branch `gpt56/fortune-mesoscopic-cotlar-20260728`,
mathematical base head `224d670d`, packet head `742b03d4`, PR #33.

Material read in full: the review packet and prompt;
`PRIME_SOURCE_TWO_LEVEL_IDENTITY_AND_PUNCTURED_CENTRE_20260729.md`;
`PUNCTURED_CENTRE_FULL_BAND_GATE_20260729.md`;
`PROGRAMME_STATUS_AFTER_PUNCTURED_CENTRE_FULL_BAND_GATE_20260729.md`;
`NEXT_PROGRAMME_FULL_BAND_TYPEII_DISPERSION_20260729.md`;
both named verifiers. All load-bearing identities were re-derived by hand and
re-verified with an independent implementation
(`fortune-review/scripts/punctured_centre_audit.py`, output in
`fortune-review/data/punctured_centre_audit.txt`); no code was shared with the
branch verifiers. Notation below follows the packet: H = eta X^2, Y = ceil(sqrt H),
first-band primes p > X, centres P_j with largest prime factor in [X, 2X),
block size K << log X.

---

## 1. Executive verdict

**A valid new reduction containing one repairable support-scoping flaw, with the
remaining gap genuinely open (no existing theorem closes it).**

Specifically:

- The exact algebra — two-level identity, one-small-variable resummation,
  punctured-centre transport, source-diagonal formula, punctured Gram,
  residue-energy identity — is **correct**. I re-derived each from definitions and
  re-verified all of them exactly with independent code (Section 2).
- The claim that the one-variable collision strata collapse into the removed
  product diagonal, and hence that "only the genuinely two-variable determinant
  stratum survives" (packet Section 8; prompt core claim 6), is **established only
  for cells with all four variables below p** — essentially the top dyadic slice
  d ~ Y. For d << Y the m-range H/d exceeds every first-band prime and the collapse
  is **false as stated**; explicit counterexamples are machine-verified below. The
  committed verifier caps m at Y and therefore cannot see this. No committed note
  reclassifies the unbalanced cells. This is a hole in the reduction narrative,
  not in any proved identity — and it is repairable by standard long-variable
  completion at conductor p — but until the unbalanced ledger exists, "the
  remaining low-mode kernel is p | dm - d'm' with d != d', m != m'" is an
  overstatement.
- The remaining analytic target is real and open. My literature audit (Section 4)
  agrees with the branch: nothing closes it. Two sharpenings the branch should
  record: (i) the fixed-modulus estimate (5.2) is a **GRH consequence** per
  modulus (so it is true, and fixed-modulus counterexample hunting is pointless;
  the open content is unconditional uniformity at Siegel-Walfisz-forbidden ranges
  plus cross-modulus coherence); (ii) the "puncture" (4.2), while exact, does not
  by itself produce the interval-localized inverted numerators that
  Kloosterman-fraction technology needs — P_j/d is of size e^{theta(z_j)}/d, so
  only its residue exists analytically. Its dividend so far is bookkeeping
  (injectivity, multiplicity <= K, the clean centre-pair criterion), not access to
  reciprocity.

Nothing reviewed here constitutes progress on, or an obstruction to, Fortune's
conjecture itself; the branch is explicit about this and I concur.

---

## 2. Claim-by-claim audit

Verdicts on the eight core claims of the review prompt, then the packet's review
tasks A-F.

### Claim 1 (packet 3.1/3.2): two-level identity and resummation — **VALID**

Derivation (independent). Let M = mu_{<=Y}, A = M\*1, B = mu_{>Y}\*1, so
eps = mu\*1 = A + B. Convolution-squaring the idempotent eps gives

    eps = eps*eps = A*A + 2 A*B + B*B = A*A + 2A*(eps - A) + B*B
        = 2A - A*A + B*B .

B is supported on n > Y (an integer n <= Y has no divisor > Y), so B\*B is
supported on n > Y^2. Hence eps = 2A - A\*A exactly on n <= Y^2. Convolving with
Lambda and using Lambda\*(M\*1) = M\*(mu\*1)\*log = M\*log, and the fact that
convolution at n samples the identity only at arguments <= n <= H <= Y^2, gives
(3.1). For (3.2): 2M\*log - M\*M\*1\*log = M\*log + M\*(eps - M\*1)\*log and
eps - M\*1 = mu_{>Y}\*1, which is exact everywhere; so (3.2) holds on the same
range. Cross-check: mu\*log = M\*log + mu_{>Y}\*log and
mu_{>Y}\*log = mu_{>Y}\*1\*Lambda = M\*(mu_{>Y}\*1)\*log + (mu_{>Y}\*1)^{\*2}\*Lambda,
whose last term is supported above Y^2 — consistent.

Endpoint conventions (review task A): Y = ceil(sqrt H) gives Y^2 >= H, and the
B\*B support bound is strict (a, b >= Y+1 forces ab > Y^2 >= H), so no endpoint
correction is lost even when Y^2 = H. At n = 1 both sides vanish. The log
convention (log = 1\*Lambda) is used consistently. Machine check: independent
implementation confirms (3.1) and (3.2) for every n <= H on panels X = 11, 17, 23,
and separately confirms the epsilon-level identity and the B\*B support claim —
12/12 PASS.

### Claim 2: only one explicitly small Mobius variable — **VALID, with a reading caution**

True of the identity: the only Mobius factor restricted below Y is the single d.
Caution: this must not be read as "only one hard variable". The second family
mu_{<=Y}\*mu_{>Y}\*1\*log carries an unbounded Mobius variable a > Y; equivalently
c_d(m) = (mu_{>Y}\*1\*log)(m) = log m - (mu_{<=Y}\*1\*log)(m), a divisor-bounded but
sign-bearing coefficient. The overlap bookkeeping of the provisional three-variable
identity is genuinely gone (an algebraic gain); the arithmetic depth has moved
into c_d, not vanished.

### Claim 3 (packet 4.1): every nonzero d divides every centre — **VALID**

Trivial and correct: mu(d) != 0 forces d squarefree; d <= Y < X forces every prime
factor of d below X; every prime below X divides every P_j in the block.

### Claim 4 (packet 4.2/4.3): punctured-centre transport — **VALID**

For p > X: (d, p) = 1, so p | P_j + dm iff p | d(P_j/d + m) iff p | P_j/d + m,
using that P_j/d is an integer by Claim 3. Machine-checked (their verifier and
mine agree). Note for Section 4: the Gram (7.1) below never actually uses
d | P_j — it survives cross-multiplication for arbitrary units d. What the
divisibility adds at this stage is exactness of bookkeeping (integer punctured
centres, injectivity of d -> P_j/d mod p, residue multiplicity <= K per block),
not new analytic leverage.

### Claim 5 (packet 6.1-6.3): source-product diagonal Fortune-admissible — **VALID WITH CONDITIONS**

The formula D_{j,R} = (M_Z - H_{j,R}) delta_R^2 + H_{j,R} is immediate from the
two-valued survivor coordinate. The scale claim (6.2) follows with room to spare
(ledger in Section 3: the true size is ~ K H, even below the claimed K H log X).
Two conditions must be recorded:

1. **beta_j << log X is an unaudited import** from earlier branch notes; I did not
   re-derive it and it should be within the scope of any final write-up.
2. The diagonal computed is that of the **fully recombined** source (prime
   indicator + sparse prime-power correction). This is the correct diagonal for
   the target (10.1) as stated. But any proof strategy that estimates dyadic
   (d, m)-cells separately and sums with absolute values acquires per-cell
   diagonals whose sum is **not** D_{j,R}; cross-cell diagonal terms reappear.
   The branch's own prohibition on triangle inequality across cells covers this,
   but the admissibility statement should say explicitly that it is a property of
   the recombined amplitude only. (This is packet review task C; with these two
   caveats, task C passes.)

### Claim 6 (packet 8.1-8.2): collision collapse and determinant stratum — **VALID WITH CONDITIONS; INVALID as stated in the prompt's unscoped form**

The positive part: for d, d' <= Y < X < p automatically, and **whenever also
m, m' < p**, the argument is correct: p | d(m - m') with (d, p) = 1 and
|m - m'| < p forces m = m'; symmetrically for m = m'. In that regime the only
surviving stratum is d != d', m != m', p | dm - d'm', and since
|dm - d'm'| < H < X^2 < pq, at most one first-band prime divides a nonzero
determinant. All of this I re-verified.

The flaw: **m < p is not a property of the source; it is a property of one dyadic
slice.** Under the (d, m) split forced by the reduced identity, m ranges up to
H/d. Only cells with d ~ Y have m <= H/d ~ sqrt(H) < X < p. For d << Y the
m-range exceeds every first-band prime, and the one-variable stratum is populated
far beyond the product diagonal: p | d(m - m') has the full family of solutions
m' = m + kp. Machine-verified counts of such collisions with m != m' on the true
cell range m, m' <= H/d (my audit script, band p in (X, 2X], d <= Y squarefree):

    X = 11 (H = 96):   942 one-variable collisions; e.g. p = 13, d = d' = 1, m = 1, m' = 14
    X = 17 (H = 231):  5255; e.g. p = 19, d = d' = 1, m = 1, m' = 20
    X = 23 (H = 423): 15979; e.g. p = 29, d = d' = 1, m = 1, m' = 30

On the verifier's tested range m, m' <= Y the count is 0 on every panel — i.e.
the committed verifier (`punctured_centre_offdiagonal_verify.py`, which caps
m at Y in both the transport loop and the collision loops) tests **exactly the
slice on which the claim is true** and none of the slices on which it fails.
This answers packet review task E: cells with a variable at or above p were
neither excluded nor reclassified; they were overlooked (or silently deferred
without a ledger entry). The gate note's phrase "in every critical balanced
cell" hedges correctly, but no committed document defines which cells are
"critical", proves the remaining cells negligible, or reduces them to a
different kernel.

Why this matters and why it is repairable: at conductor p the long-variable
cells (M >= p) admit exact completion of the m-sum (finite Fourier on F_p, no
error term), converting them into dual sums of length ~ M/p against
Kloosterman-type phases in the punctured centre. The expected outcome is a
similar determinant kernel in the dual variable — but that must be derived and
its scale ledger recomputed, because the branch's "closed as black-box: direct
Kloosterman insertion" verdict currently cuts against the only standard tool for
this regime. Until then, statements of the form "the remaining low-mode kernel
is (8.2)" must be scoped to the balanced slice.

Product equality with d != d', m != m' (last item of task E): occurs (dm = d'm'
with cross factorizations), is removed with the integer product diagonal n = n'
by definition, and my counts exclude it; no issue found.

### Claim 7 (packet 9.1): weighted residue-energy identity — **VALID**

Standard orthogonality on the character group of F_p^x; the centring term is the
chi_0 contribution. Two audit notes: (i) the identity requires both coefficient
supports on units mod p — automatic for d <= Y < p, **not** automatic for m once
m >= p (multiples of p in the m-range must be, and in my checks are, excluded);
this is another place the balanced-slice assumption leaks in silently.
(ii) The committed verifier checks only the Parseval-free centring identity
(energy = congruence energy - (AC)^2/(p-1)), not the character-sum form; my audit
script verifies the character form itself at p = 101 and p = 199 with Mobius
coefficients and m-ranges exceeding p (PASS, agreement to 1e-9).

### Claim 8: no identified black box closes the coherent estimate — **VALID (I concur), with two sharpenings**

See Section 4. Sharpening 1: fixed-modulus (5.2) follows from GRH for the
characters mod p (GRH gives |sum_{d<=D} mu(d) chi(d)| << D^{1/2} p^eps for every
chi; then (1/(p-1)) sum_chi |C(chi)|^2 = sum_{m = m' mod p} c c' << ||c||^2 (1 + M/p)
by the divisor-bounded coefficients, giving (5.2) with D M X^{o(1)}). So (5.2) is
true, per modulus, on GRH; what is open is unconditional uniformity at the
Siegel-Walfisz-forbidden range D ~ p, and — even granting every fixed modulus —
the coherent cross-modulus and cross-conductor contraction, which GRH does not
supply. Sharpening 2: the at-most-one-collision-prime property means the
band-summed off-diagonal is exactly a signed count over the determinant variety
(Section 5), which is the cleanest known formulation of the remaining content.

---

## 3. Scale ledger

All entries recomputed from definitions; eta fixed, logs base e, ~ means up to
absolute constants and (log X)^{O(1)} where stated.

| Quantity | Value | Notes |
|---|---|---|
| Source length | H = eta X^2 | packet Section 1 |
| Small-variable length | Y = ceil(sqrt H) ~ sqrt(eta) X | Y < X for large X; verified |
| Second-variable length | M = H/d, from ~ sqrt H (d ~ Y) up to H (d = 1) | **exceeds p ~ X except on the top slice** |
| Centre-block length | K ~ log X | |
| First-band modulus count | pi(2X) - pi(X) ~ X / log X | |
| Prime-source count | M_Z ~ H / log H ~ X^2 / (2 log X) | |
| Band hit count | H_{j,R} ~ M_Z sum_{p in R} 1/p ~ X^2 / log^2 X | sum_{X<p<=2X} 1/p ~ log 2 / log X |
| delta_R | V_R^{-1} - 1 ~ 1 / log X | |
| Source diagonal sum_j beta_j^2 D_{j,R} | ~ K X^2 = K H / eta | branch's K H log X is safe but loose by log |
| Fortune first-band block allowance | ~ K H X / log X = eta K X^3 / log X | consistent with the variance criterion at loss o(log X); conservative |
| Diagonal margin | allowance / diagonal ~ X / log X (branch: X / log^2 X with their looser bound) | Gate B genuinely passes |
| Trivial off-diagonal | per centre (M_Z delta_R + H_{j,R})^2 ~ X^4 / log^4 X; block total ~ K X^4 / log^2 X | |
| Exact remaining loss | trivial / allowance ~ X / (eta log X) = **X^{1 - o(1)}** | matches the branch ledger |
| Unsigned fixed-modulus energy (ACZ regime) | centred, unweighted intervals: ~ DM p^{o(1)} — reaches target scale **only because centring removes the (DM)^2/p main term** | see Section 4.1 |
| Mobius-weighted energy | centring vacuous (A ~ 0); required saving on the determinant stratum: factor DM/p ~ X of **sign cancellation** | the open content |
| Best justified unconditional off-diagonal | nothing below trivial by more than (log X)^{O(1)} for the coherent full-band form | |
| Blomer-Pascadi insertion (as cited by branch) | saving c^{-1/32}, c = ps ~ X^2, i.e. X^{-1/16} | short of X^{1-o(1)} by exponent factor ~ 16; branch's assessment confirmed arithmetically (I could not independently verify the cited arXiv:2607.24311 itself — post-dates my verifiable literature; treated as-cited) |

One correction of emphasis to the packet's Section 6.2-6.3: with the sharper
diagonal count the margin is X/log X, not X/log^2 X; nothing depends on this.

---

## 4. Literature audit

For each candidate, the literal parameter map and the failure point. Ranges
below: D ~ Y ~ X (small variable), M ~ H/D, DM ~ H ~ X^2, moduli p ~ X prime,
~X/log X moduli, K ~ log X centres, coefficients alpha = mu on [1, Y],
gamma = c_d (divisor-bounded, signed, from (3.2)).

**4.1 Ayyad-Cochrane-Zheng (congruence x1 x2 = x3 x4 mod p, J. Number Theory
1996; Cochrane-Zheng refinements).** Map: solutions of dm = d'm' (mod p) in boxes
[1,D] x [1,M]^2 x [1,D]; ACZ give (DM)^2/p + O(DM p^{o(1)})-type counts, i.e. the
**centred** unweighted energy is ~ DM p^{o(1)}. Applies literally to unweighted
intervals at exactly our parameters. Fails for (5.2) because the proof is a count
(positivity); with alpha = mu the centring term (AC)^2/(p-1) is ~ 0 (A ~ 0), so
the structured mass (DM)^2/p is not subtracted by the mean — it must be
annihilated by the Mobius signs, which no counting theorem sees. My audit
script's empirical table illustrates the regime split at p up to 401: unweighted
uncentred/(DM) ~ DM/p (30.7 / 60.5 / 92.7 / 121.5 against DM/p = 30.0 / 59.7 /
91.9 / 120.7), collapsing to ~ 0.45 after centring; Mobius-weighted energies are
~ 1 x DM with centred = uncentred to three decimals (A, C in {-4,...,4}).
**Partial: explains the unweighted saving; inapplicable to the signed target.**

**4.2 Fourth moments of character sums (Cochrane-Zheng; Burgess-regime
literature).** A Cauchy split of (5.2) needs sum_chi |M_D(chi)|^4 << D^2 p^{o(1)}
at D ~ p. But sum_chi |M_D|^4 = (p-1) x (signed count of d1 d2 = d3 d4 mod p),
which is the same signed-energy problem — circular. **Inapplicable.**

**4.3 Multiplicative energy of intervals/sets mod p (Garaev; Bourgain-Garaev).**
Unsigned; same (DM)^2/p main-term issue as 4.1. **Inapplicable to the signed
target.**

**4.4 Mobius orthogonal to characters at range ~ conductor.** Siegel-Walfisz
gives cancellation in sum_{d<=D} mu(d) chi_p(d) only for p << (log D)^A — here
p ~ D, hopeless unconditionally. GRH gives square-root cancellation for every
chi, and hence (5.2) per modulus (Section 2, Claim 8). Halasz/pretentious and
Matomaki-Radziwill technology give o(D) for individual chi only with severe
conductor restrictions. Klurman-Mangerel-Teravainen (short APs, average over
moduli) and related results allow exceptional moduli sets that cannot be
afforded against ~X/log X specific band primes, and their ranges do not cover
d ~ p with uniformity. **Open at exactly the needed strength; the clean
statement of the obstruction.**

**4.5 Dispersion to large moduli (Bombieri-Friedlander-Iwaniec; Drappeau;
Maynard-era refinements).** Map: these treat primes/sequences in APs with
moduli to x^{1/2+delta}, crucially using well-factorable weights or fixed
residue classes. Here the moduli are single primes p ~ X = (H)^{1/2}/sqrt(eta)
— **at** the classical barrier with no factorability available — and the residue
classes -P_j (equivalently -P_j/d) vary with both j and d across the block
("conductor migration" in the programme's earlier language). No BFI-type input
applies without factorable moduli or fixed shifts. **Inapplicable.**

**4.6 Kloosterman fractions / bilinear forms in Kloosterman sums
(Duke-Friedlander-Iwaniec 1997; Bettin-Chandee; Fouvry-Kowalski-Michel;
Kerr-Shparlinski school).** These require the inverted variable to occupy an
archimedean interval of controlled size (numerators |a| <= A, denominators
~ C, with A C-type conditions). The punctured numerators P_j/d are of size
e^{theta(z_j)}/d — exponentially large; only their residues exist. No literal
parameter map is possible. **Inapplicable literally** (consistent with the
branch's own no-go item 5, and the reason the "puncture" is not yet an analytic
gain).

**4.7 Blomer-Pascadi bilinear Kloosterman (arXiv:2607.24311, as cited by the
branch).** I cannot independently verify this reference (it post-dates my
reliable literature coverage); taking the branch's quoted saving c^{-1/32} at
square-root ranges at face value, insertion at c = ps ~ X^2 yields X^{-1/16}
against a required X^{1-o(1)}. **Insufficient by a large exponent factor even
if literally applicable; branch's arithmetic confirmed.**

**4.8 General-sequence Barban-Davenport-Halberstam (Harper 2025).** Gives
variance asymptotics over all moduli q <= Q for sequences satisfying
non-concentration hypotheses. Here: moduli restricted to primes in one dyadic
band; the "sequence" (band survivors at shifted primorial centres) changes with
the centre; the required statement is a signed coherent contraction, not a
variance asymptotic; the hypotheses are unverified for this sequence.
**Inapplicable without new work; and the wrong shape.**

**4.9 All-order sieve-survivor / conductor recombination.** I know of no
literature object matching the coherent signed recombination of g_R across
conductor orders (the branch's E_{B,R} summability requirement). The nearest
relatives (Selberg sieve Gram analyses, Motohashi-style identities) do not
track sign coherence between physical and composite conductors at a sparse
family of centres. **No match.**

**Conclusion of the audit:** claim 8 stands. The remaining theorem is new
mathematics; its minimal unconditional core is isolated in Section 5.

---

## 5. Best path forward

Per packet Section 14D, choosing **exactly one**: option **2 — derive a stronger
all-order cancellation identity before estimating (9.1)** — with a mandatory
step 0 that is bookkeeping, not mathematics.

**Step 0 (mandatory repair; blocks everything else).** Build the unbalanced-cell
ledger. For cells with M = H/D >= p (all but the top dyadic slice), complete the
m-sum at conductor p exactly (finite Fourier on F_p; no error term), obtaining
dual sums of length M/p against phases in the punctured centre; derive the
resulting kernel and rerun the finite verifier with the true m-ranges
(m <= H/d, not m <= Y). Only after this does "the surviving low-mode kernel"
have a theorem-grade meaning. My audit script already provides the violating
enumeration to build on. Prediction to test on panels: the completed unbalanced
cells reproduce a determinant-type kernel in (d, dual variable), so the
determinant formulation survives with a second parameter regime — but this must
be proved, not assumed.

**Step 1 (the structural-cancellation identity).** Use the
at-most-one-collision-prime property to reorder the band-summed off-diagonal
exactly as a sum over the determinant variety:

    sum_{p in R} (off-diagonal collision mass at p)
      = sum_{Delta != 0} R_c(Delta) * w_R(Delta),

where R_c(Delta) = sum_{dm - d'm' = Delta} mu(d) mu(d') c(m) conj(c(m')) is the
signed representation function and w_R(Delta) in {0, 1} indicates a band prime
factor (weight 1/p variants included). The proposed exact move, in the spirit
the prompt demands (structural cancellation before generic inequalities): the
band indicator w_R is itself one coordinate of the survivor system the branch
has already recombined exactly — 1 - w_R(Delta) is a survivor condition on Delta
for the same band. Recombine w_R with the g_R-machinery **before** estimation
and hunt for the identity in which the main term of sum R_c(Delta) w_R(Delta)
cancels against the already-extracted diagonal, leaving a genuinely centred
object. Concretely: compute, on the finite panels, the decomposition of
sum_Delta R_c(Delta) w_R(Delta) into (i) the term predicted by density
w_R ~ sum_{p in R} 1/p and (ii) the remainder, with the actual mu/c
coefficients; if (i) is removed exactly by a survivor identity, the residual
object is the one worth an analytic campaign.

**Step 2 (the first statement of genuinely new mathematics).** After steps 0-1
the irreducible core, stated so it can be attacked or refuted independently of
all Fortune scaffolding, is a signed determinant dispersion estimate:

    SDD(X). For alpha = mu on (D, 2D], gamma divisor-bounded on (M, 2M],
    D <= sqrt(H), DM ~ H = eta X^2, prove

    sum_{X < p <= 2X} 1/p * | sum_{d, m : p | dm - a_p, dm != a_p-diagonal ...} |
    — equivalently, in energy form:

    E := sum_{d,d' ~ D} mu(d) mu(d') sum_{m,m' ~ M, dm != d'm'}
         gamma(m) conj(gamma(m')) 1[ exists p in (X, 2X] : p | dm - d'm' ]
      << D M X^{o(1)} .

    (Each quadruple meets at most one band prime, so E is a bona fide signed
    count on the determinant variety localized to band-divisible values.)

Calibration milestones, in order: (a) verify SDD numerically for X up to a few
hundred with the actual coefficients (exact enumeration is cheap; this either
calibrates the X^{o(1)} or produces the packet's requested actual-coefficient
counterexample — either outcome is decisive); (b) prove the half-signed case
gamma = 1 (Mobius in d only) — plausibly accessible via divisor-switching on
dm - d'm' = Delta and classical bilinear technology, and already new; (c) the
full mu x mu case; (d) only then cross-conductor coherence (the branch's Phase
F/H), where I note for expectation-calibration that parity re-enters at
cross-band recombination, not at the first band — the first-band theorem SDD is
plausibly on the provable side of parity.

Why not the other three options of 14D: option 1 (fixed-modulus fourth moment)
is GRH-true per modulus, so proving it unconditionally for every p attacks
Siegel-Walfisz-at-range-p head on — the hardest known formulation of the same
content; option 3 (counterexample hunting) is bounded by the GRH observation to
the cross-modulus regime, where finite panels are too small to be decisive;
option 4 (bypassing the determinant kernel) discards the one exact structure
(at-most-one-collision-prime) that makes the band sum a single clean object.

---

## 6. Corrected boundary

| Status | Items |
|---|---|
| **PROVED** | Two-level identity (3.1); resummation (3.2); transport (4.1)-(4.3); source-diagonal formula (6.1); diagonal admissibility (6.2) **conditional on the imported beta_j << log X and stated for the recombined amplitude**; punctured Gram (7.1); residue-energy identity (9.1); collision collapse and determinant kernel (8.1)-(8.2) **restricted to cells with max(d, d', m, m') < p**; at-most-one-collision-prime for distinct products below H. |
| **VERIFIED ONLY** | All of the above on finite panels X = 11..37 (branch verifiers) and independently re-verified here (X = 11, 17, 23 + character-form of (9.1) at p = 101, 199); note the branch verifier tests the collision claims only on the balanced slice m <= Y. |
| **HEURISTIC / EMPIRICAL** | Row-to-diagonal ratio diagnostics; my Section 4.1 energy table; the expectation that completed unbalanced cells reproduce a determinant kernel; the Hardy-Littlewood-type calibrations inherited from the wider programme. |
| **OPEN** | Unconditional (5.2) at D ~ p (GRH-true per modulus); SDD(X) / the band-averaged signed determinant estimate; coherent cross-conductor survivor contraction (10.1) with summable E_{B,R}; signed source-cell recombination at theorem scale; first physical-band theorem; NSMT(X); Fortune variance theorem; Fortune's conjecture. |
| **RETRACTED OR NEEDS CORRECTION** | Prompt core claim 6 and packet Section 8 in their unscoped form ("the one-variable collision strata disappear", "only the determinant stratum survives"): **false on the true cell ranges** (machine-verified counterexamples, Section 2 Claim 6); must be restated with the max-variable < p hypothesis and accompanied by an unbalanced-cell ledger. The framing of the puncture as an analytic (rather than bookkeeping) gain should be softened until a derivation uses d | P_j beyond injectivity/multiplicity. The verifier's m <= Y caps should be documented as a known blind spot or widened. |

---

*Independent audit artifacts: `fortune-review/scripts/punctured_centre_audit.py`
and `fortune-review/data/punctured_centre_audit.txt` on branch
`claude/fortunes-conjecture-mechanisms-fuuz4z`.*
