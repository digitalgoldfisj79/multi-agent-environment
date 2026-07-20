# Review: Fortune's-conjecture research programme (archive/fortune-* branches)

**Reviewed:** 2026-07-20
**Scope:** all seven `archive/fortune-*` branches, with primary focus on
`archive/fortune-paper2-20260720` (*Prime Detection at Primorial Centres*, Rev. 1)
and its supporting phase branches dated 2026-07-19.

## Summary verdict

The mathematics is sound everywhere I could check it, and the epistemic
hygiene is excellent: every unproved target is labelled as such, no proof of
Fortune's conjecture is claimed anywhere, finite computations are explicitly
excluded from the proofs, and the no-go results are correctly scoped to
specific proof routes rather than overclaimed as impossibility theorems.
The main defects found are reproducibility blemishes: the manuscript's
validation table cites numbers that the shipped supplement does not
reproduce, and two of the validators cited in that table are absent from the
repository entirely.

## Verification performed

1. **Shipped validation suite re-run.** All five validators in the Paper II
   supplement pass, and their output matches `validation_results.txt`
   bit-for-bit (the suite is deterministic). Note the suite silently depends
   on `sympy`, which is not declared anywhere.

2. **Independent checks written from the theorem statements** (not the
   shipped code), all passing:
   - Theorem 4.2: the five-row multiset table sums symbolically to
     N(3N³−2N²+2N−1)/2, and the centred formula (4.4) equals
     ∫|H₂|⁴ − M² exactly, with limiting constant 5.
   - Proposition 5.1: partial alternating-binomial identity, exhaustively
     for s, k ≤ 40.
   - Theorem 7.2: character-ratio collapse and the full additive-phase
     reconstruction, brute-forced over all multiplicative characters for
     q = 7, 11, 13 with random a, x, y.
   - Theorem 7.1: character diagonal equals the K_m kernel, prime moduli.
   - Proposition 3.2: dual-row identity ℰ_a = M(M−1)κ₂,ₐ + ℛ_a on random
     weighted systems.

3. **Proof-level spot checks by hand** (correct as stated): Proposition 2.1,
   Lemma 2.2, Lemma 2.3, Theorem 2.4 (including the quantifier arithmetic
   B_X ≪ L(X)/log X), Lemma 4.1 (four-copy rigidity via the superincreasing
   bound 4Σ_{i<j}P_i < P_j), Theorem 5.2 (including the
   binom(s−1,k) ≤ binom(s,k+1) step and the Mertens/Stirling endgame),
   Theorem 6.1 (semiprime resonance — the counting and normalisation
   D_ρ ≍ H/log H, p̃ ≍ 1/H both check out), Theorems 8.1–8.3, Lemma 9.2,
   and the ε-elimination inequality (9.4).

4. **Bibliography.** All 17 entries correspond to real publications.
   The two least-familiar ones were verified against external databases:
   Harper, *Simple Barban–Davenport–Halberstam type asymptotics for general
   sequences*, JLMS (2025), DOI 10.1112/jlms.70293 — exists, title exact;
   arXiv:2401.17570 is indeed Matomäki–Merikoski–Teräväinen, *Primes in
   arithmetic progressions and short intervals without L-functions*.
   No fabricated citations found.

5. **Not verifiable from this environment:** the Zenodo DOIs
   (10.5281/zenodo.21457113 and 21426465) — outbound network policy blocked
   doi.org/zenodo. The binary phase-package ZIPs exist in the repo only as
   `.sha256` files; their contents could not be audited.

## Findings

**F1 (reproducibility, minor).** The validation table in Part 4 does not
match the shipped supplement's output. Table: one-sided residual 1.30×10⁻⁹,
Fourier-scale residual 1.31×10⁻¹³, coherence "correlation 0.99612".
Shipped suite (deterministic): 8.486×10⁻⁹, 8.598×10⁻¹⁴, and a *max-error*
metric (0.068 at N=10,000) — the shipped coherence script computes no
correlation at all. The numbers evidently come from earlier phase-package
runs. Either regenerate the table from the shipped suite or ship the runs
that produced the table.

**F2 (reproducibility, minor).** The CRT-diagonal (residual < 2×10⁻¹²) and
character-ratio (< 2.3×10⁻¹⁴) validators cited in the table are not in the
Paper II supplement and not anywhere in the repository — the crt-detensor
branch contains only markdown reports. I re-derived and confirmed both
identities independently, so the mathematics stands, but a reader of the
archive cannot reproduce those two rows.

**F3 (wording, trivial).** The table row "Theorem 4.2 at N=55: exact value
13,562,560" overstates what the script does: brute-force verification runs
only for N ≤ 12; at N=55 the script merely evaluates the closed form. (A
direct N=55 count is cheap — 1540 pair sums — and would be worth adding.)

**F4 (structural).** The sufficiency of the reciprocal-frame target (3.6)
for the prime-detection architecture — the chain PGD2 ⇒ … ⇒ Fortune — rests
on "pair-lift and principal-cancellation reductions" that live in the
supplementary phase reports, not in the manuscript. Cold-review note 8
acknowledges this, but a referee still cannot check the load-bearing
reduction from the paper alone. The paper is careful to keep Theorem 2.4
(which is self-contained) separate from this conditional architecture,
which is the right call.

**F5 (significance, context).** Theorems 2.4, 8.2 and 8.3 are elementary
(Chebyshev, a Riemann sum, and an exact ratio respectively); their value is
observational. The genuinely non-trivial content is the exact fourth moment
(4.2), the one-sided decomposition (3.14), the growing-degree Möbius
truncation (5.2), the semiprime resonance obstruction (6.1), and the
character-ratio collapse (7.2/7.3). The paper itself frames all of this
honestly as a boundary map rather than progress on cancellation, and the
concluding claim — that the obstacle is a genuinely new transference
theorem, not another reformulation — is well supported by the seven-branch
record of closed routes.

**F6 (packaging, minor).** `run_all_checks.py` needs `sympy` (and the
environment had none); add a requirements note. The repo template files
(`agent.py`, `environment.py`, `main.py`) ride along on every archive
branch and could be dropped from the packages.

**F7 (disclosure, advisory).** The phase reports record heavy AI
involvement ("hostile Claude Fable 5 Max review", "Claude cold review",
autonomous attack phases). For a Zenodo record this is fine; if the
manuscript is submitted to a journal, most now require an explicit
AI-assistance disclosure statement — worth adding to the front matter.

## Assessment of the programme arc

The 2026-07-19 phase branches (pgd2-attack → crt-detensor →
factorial-transfer → one-sided-harmonic → almost-all) show a disciplined
pattern: each phase pre-registers gates, applies stop rules ("stop if the
result merely restates PC-FROB2"), records exact exponent ledgers, and
closes routes with either exact algebra or clearly-labelled finite
conditioning diagnostics. The distinction maintained throughout between
exact algebraic losses and finite diagnostics, and the standing instruction
not to call PGD2/SHF2/PC-FROB2 theorems, directly addresses the failure
modes (false precision, "consistent with" dressed as "demonstrated by")
that this workflow was designed to avoid. Paper II is a faithful
distillation of that record.

**Recommendation:** fix F1–F3 and F6 before any journal submission; F4
would need the pair-lift reduction written out in the manuscript or a
citable companion. As a supporting-materials preprint the package is in
good shape.
