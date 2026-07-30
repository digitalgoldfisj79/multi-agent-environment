# Review addendum: full-source completion and the corrected physical target

Reviewer: Claude (continuation of the PR #33 cold review, comment 5124074182)
Date: 2026-07-30
Reviewed state: branch `gpt56/fortune-mesoscopic-cotlar-20260728`, head `7237374`,
notes `FULL_SOURCE_COMPLETION_AND_CENTERED_DETERMINANT_20260730.md` and
`FABLE_REVIEW_INTAKE_AND_CORRECTED_BOUNDARY_20260730.md`, plus the new verifiers.

Independent audit artifacts: `fortune-review/scripts/full_source_completion_audit.py`
(no shared code with the branch verifiers), output archived at
`fortune-review/data/full_source_completion_audit.txt`, branch
`claude/fortunes-conjecture-mechanisms-fuuz4z`. All numeric statements below come
from that run.

---

## 1. Executive verdict

**The repair is accepted; the correction to my proposal is accepted and formally
adopted; the corrected target PBDH_P(X) is the right physical-diagonal object; and
the review identifies where the genuinely load-bearing difficulty now sits (it is
not primarily the one-logarithm saving).**

Four points:

1. **The unbalanced-cell support flaw is closed at amplitude level.** The completion
   identities are exact and I have re-verified all of them independently (Section 2).
   The structural outcome is the right one: once the true ranges are restored and the
   signs kept, the "Möbius-weighted fourth moment" I audited last round collapses to
   the ordinary von Mangoldt progression discrepancy. The bilinear object was an
   artifact of the balanced-slice truncation; the branch is correct to retire it.
2. **Retraction.** The branch's Section 5 rejection of my uncentred SDD(X) box is
   correct, and I strengthen it: the statement is false not only for the recombined
   full source but *cellwise*, in both regimes I proposed it for. Machine exhibit
   (Section 3): the D = 1 cell with gamma = Lambda gives E/(DM) = 455 / 1553 / 3885
   at X = 101 / 199 / 307, and E equals 0.83-0.93 of the density prediction
   dens x (sum gamma)^2 — the kernel is all main term; the mid-D Möbius cell gives
   |E|/(DM) = 13 / 19 / 31 and growing. My own Step 1 ("identify the density-predicted
   main term and remove it exactly") was the operative content; the Step 2 box that
   dropped the centring is hereby formally retracted. The centred kernel
   W_R(Delta) = 1[exists p | Delta] - lambda_R of the branch's (4.4) is the correct
   object, and "the density subtraction is not optional" is the right slogan.
3. **PBDH_P(X) is correctly calibrated but its inferential role should be stated
   precisely.** Budget arithmetic (Section 4) shows that PBDH_P plus Cauchy over the
   band plus *average-residue behaviour of the orbit samples* lands the first-order
   block energy at ~ K H X / log X — exactly at the Fortune allowance with zero
   margin. So PBDH_P is the right scale gate, but the statement that decides anything
   is the orbit restriction: the primorial-centre samples D_p(-P_j) must behave like
   typical residues, with enough cross-modulus cancellation to recover a log-power of
   margin. This is the integer-side reappearance of the programme's recurring
   structure (Paper III's transfer gap; the Lebesgue-vs-sampling split): the
   all-residue theory is one log from closed; the sparse arithmetic sampling is the
   open mathematics. The branch's OPEN list contains this; I am promoting it from a
   list item to the headline.
4. **Literature (Section 5): the claim "no directly applicable published theorem" is
   corroborated**, with the two nearest genres named and mapped, plus one relevant
   correction of scope: the Fiorilli–Martin disproof of Hooley's conjecture lives at
   q of size log log x and does not threaten the band-averaged target; and the
   function-field analogue of exactly this variance statement is *proved*
   (Keating–Rudnick, via Katz equidistribution) — which makes the function-field
   PBDH analogue the one place in this programme where the remaining physical
   theorem is already a theorem, and strengthens the case for the laboratory route.

Fortune's conjecture remains open; nothing here changes that, and the branch says so.

---

## 2. Audit of the new claims

All verified with the independent implementation; formal identities checked in exact
prime-exponent arithmetic, analytic identities to 1e-9.

| Claim | Verdict | Check |
|---|---|---|
| (1.2) Lambda = sum_{d|n, d<=Y} mu(d) c_Y(n/d), n <= H | **VALID** | exact, all n, X = 11/17/23 — PASS |
| (2.2) completion to psi(H;p,a), true ranges m <= H/d | **VALID** | exact, every residue a, two band primes per panel — PASS (6/6) |
| (2.5) character collapse to sum Lambda chi | **VALID** | all chi mod p per panel, complex check to 1e-7 — PASS |
| (2.6) n = p is the only non-unit source | **VALID** | immediate from p^2 > H; used below |
| (3.1) A_{j,p} = -w_p D_p(-P_j) + log p/(p-2) | **VALID** | against direct survivor evaluation at actual primorial centres, max deviation 5.3e-15 — PASS. Derivation note: the identity uses Psi_p + log p = psi(H) via (2.6), so the drift term is exactly the self source |
| (4.2)/(4.6) centred determinant reordering | **VALID** | direct O(H^2) pair-sum equals the variance, X = 11/17 — PASS |
| (5.1)-(5.2) uncentred form >= H^2/log X | **VALID** | re-derived (Cauchy-Schwarz per modulus + Mertens over the band); empirically R/H^2 = 0.104-0.123 across X = 101..307, stable — the density main term is the object itself |
| (6.1) large sieve gives V << HX log H | **VALID** | re-derived; note all nonprincipal chi mod prime p are primitive, so there is no small-conductor contamination — the prime-moduli family is clean for large-sieve purposes |
| Diagnostics V/(HX) in [0.36, 0.69] | **REPRODUCED** | my band convention gives 0.52-0.59 across X = 101..307 (their range brackets mine; convention-dependent constants) |

One small presentational point: (2.5) should be accompanied by the remark that the
left side is *not* of the product form M(chi)C(chi) — the hyperbola constraint
m <= H/d couples the variables — which is precisely why last round's fixed-modulus
energy analysis (mine included) was analysing a model object rather than the source.
The branch's conclusion is the right one; stating the reason will prevent the next
reviewer from re-deriving (5.2)-style targets.

## 3. The retraction exhibit (machine-verified)

For the record, the exhibit that kills the uncentred box in both proposed regimes:

```
D = 1 cell, gamma = Lambda on (M, 2M], M = H/2, band p in (X, 2X]:
  X = 101:  E/(DM) =  455.26,   E / (dens * (sum gamma)^2) = 0.828
  X = 199:  E/(DM) = 1553.21,   ratio = 0.901
  X = 307:  E/(DM) = 3884.82,   ratio = 0.932
mid-D Mobius cell (alpha = mu on (D,2D], gamma = Lambda on (M,2M], 4DM ~ H):
  X = 101 (D=22, M=92):   E/(DM) = -13.35
  X = 199 (D=44, M=180):  E/(DM) = -19.05
  X = 307 (D=68, M=277):  E/(DM) = -31.46
```

The first family converges to pure density (ratio -> 1): no amount of Möbius
weighting on a variable of bounded dyadic length can fight a positive coefficient on
the long variable. The second shows the signed density term
(sum_{d~D} mu(d))(...) is nowhere near X^{o(1)}-small. Uncentred determinant
dispersion is dead; only centred formulations (the branch's (4.4), or cellwise
versions with the density term subtracted *before* recombination) are admissible
targets from here on.

## 4. The role of PBDH_P(X): scale gate, not decision point

Write E1(B) = sum_{j in B} |sum_{p in R} A_{j,p}|^2 for the first-order block
energy (higher conductors excluded; they remain coupled, per the branch's Section 8,
and nothing here touches that). Using (3.1) and ignoring the explicit drift:

- Cauchy over the ~ X/log X band primes: E1 <= (X/log X) sum_j sum_p w_p^2 |D_p(-P_j)|^2.
- If the orbit samples were *average* residues, sum_{j,p} |D_p(-P_j)|^2 would be
  ~ K (X/log X) x V/((p-1) x #p) ~ K V / X ~ K H (using V ~ HX).
- Total: E1 ~ (X/log X) x K H = K H X / log X — the Fortune block allowance, exactly,
  with no margin for the required o(log X) loss.

Consequences, stated as sharply as I can:

1. PBDH_P(X) at H X^{1+o(1)} is **necessary-scale**: if it failed by a power, the
   route is dead; the finite panels (V/(HX) ~ 0.5, flat) say it will not fail.
2. PBDH_P(X) is **not sufficient**, even for the first-order physical component: the
   decision point is the pair (orbit restriction, cross-modulus covariance). Either
   the Cauchy step must be beaten (cross-modulus cancellation in sum_p D_p(-P_j)) or
   the orbit samples must be shown better-than-average by a log-power. This is a
   sparse-sampling statement of exactly the shape this programme has met twice
   before (reciprocal-frame transfer gap; balanced-slice artifacts).
3. New diagnostic (branch has not run this): the empirical covariance test of
   {D_p(-P_j)}_p over the centre block against a random-residue control, X = 101/199/307,
   K = 5-6 centres. Result: the orbit statistic |sum_p D_p|^2 / sum_p D_p^2 fluctuates
   in [0.4, 1.8] versus the Cauchy bound #p = 18-54, and is statistically
   indistinguishable from the random control at this scale. Read: no evidence of the
   conspiratorial positive correlation that would make the Cauchy loss real — the
   cross-modulus cancellation the route needs is present generically in the panels —
   but K <= 6 makes this weak evidence. Scaling this diagnostic (larger K, more X,
   both statistics tracked over blocks) is cheap and should become a standing
   verifier before any proof attempt: it is the closest thing available to a
   falsification test for the orbit-restriction step.

## 5. Literature audit for PBDH_P(X)

Searched this round (parameter maps below): Hooley's BDH series and its restricted-
moduli descendants, Montgomery–Hooley ranges, sparse-moduli large sieves,
function-field variance, and the modern variance literature.

1. **Montgomery–Hooley asymptotic** (all moduli): V_all(x;Q) ~ Q x log Q proved for
   x (log x)^{-A} <= Q <= x. At Q ~ sqrt(x) — our regime — the asymptotic is far
   outside every proved range; only large-sieve upper bounds survive, with the log.
   ([Wikipedia summary](https://en.wikipedia.org/wiki/Barban%E2%80%93Davenport%E2%80%93Halberstam_theorem))
2. **Restricted-moduli Montgomery–Hooley**: Baker–Freiberg, *Sparser variance for
   primes in arithmetic progression* ([arXiv:1706.07319](https://arxiv.org/abs/1706.07319)):
   asymptotics for moduli [F(n)], F(t) = t^c (c > 1, non-integer) or
   exp((log t)^gamma), gamma < 3/2 — the closest genre to a prime-restricted
   variance, but the moduli sets are Piatetski-Shapiro-type (amenable to exponential
   sums in the modulus), not primes, and the ranges remain near-classical. No prime-
   moduli analogue located. Baier–Zhao's BDH for square moduli
   ([arXiv:math/0602116](https://arxiv.org/abs/math/0602116)) matches the branch's
   description: its large-sieve input carries the same sqrt(H)-driven loss at
   H ~ X^2.
3. **Hooley's conjecture and its disproof**: Hooley conjectured G(x;q) << x log q for
   x >= q. Fiorilli–Martin, *Disproving Hooley's conjecture*
   ([EMS JEMS](https://ems.press/journals/jems/articles/8095586); see also
   [arXiv:2407.01045](https://arxiv.org/abs/2407.01045) for weaker forms) construct
   violations — but **at q ~ log log x**, a Siegel-adjacent small-modulus regime.
   This does not threaten PBDH_P (p ~ sqrt(H)); it does warn that per-modulus
   statements admit conspiracies, i.e. the band average in PBDH_P is not merely
   convenient but likely essential. Under GRH, de la Bretèche–Fiorilli
   ([arXiv:2009.05760](https://arxiv.org/abs/2009.05760)) give matching-order
   variance bounds in wide ranges — conditional support for the HX scale.
4. **Function field**: Keating–Rudnick, *The variance of the number of prime
   polynomials in short intervals and in residue classes*
   ([arXiv:1204.0708](https://arxiv.org/abs/1204.0708), IMRN 2014) **prove** the
   FF analogue of Hooley's conjecture in the large-base limit via Katz
   equidistribution, in ranges covering the analogue of x = q^beta, 1 < beta < 2 —
   i.e. exactly the PBDH_P regime. Extensions: [arXiv:2208.07173](https://arxiv.org/abs/2208.07173)
   (short residue classes), [arXiv:2102.06415](https://arxiv.org/abs/2102.06415)
   (variance of sums in F_q[t]). **The physical-diagonal theorem this branch needs is
   a proved theorem in the function-field laboratory.**
5. **Harper's general-sequence BDH** ([JLMS 2025](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.70293))
   — asymptotics under non-concentration hypotheses, moduli ranges near-classical;
   wrong shape for a prime-band at Q ~ sqrt(x), as noted last round.
6. **A fact worth recording in the branch notes**: pointwise GRH gives only
   V_P << (X/log X) x H log^4 X ~ H X log^3 X — *worse than the unconditional large
   sieve*. The one-log saving is not a GRH-shaped statement; it is an averaged
   square-root-cancellation statement about the family {chi mod p : p in band}, whose
   natural home is asymptotic-large-sieve technology
   (Conrey–Iwaniec–Soundararajan genre, cf. [arXiv:1211.6725](https://arxiv.org/abs/1211.6725))
   — the one modern toolset built to remove exactly this log for primitive-character
   families. Whether the ASL's smooth-weight requirements can be met by a dyadic
   prime band at Q^2 ~ H is, to my knowledge, unexamined — it is the most concrete
   unexplored lead this audit found.

**Conclusion**: the branch's "no directly applicable published theorem" stands.
Nearest misses: Baker–Freiberg (wrong moduli set), Keating–Rudnick (right theorem,
wrong ring), CIS asymptotic large sieve (right log, unverified applicability).

## 6. Recommended next gates

1. **Standing covariance verifier** (Section 4.3): scale the orbit-vs-random
   diagnostic; it is the falsification test for the load-bearing step.
2. **Function-field PBDH first**: formulate the band variance for F_q[t] primorial
   centres and check whether Katz-equidistribution inputs already close the FF
   physical diagonal. A proved FF first-band theorem would be the programme's first
   end-to-end component and would sharpen exactly what the integer side is missing
   (this is the laboratory thesis of the wider review, now with a named target).
3. **ASL lead** (Section 5.6): a literal parameter check of asymptotic-large-sieve
   machinery against the band family. Outcome either way is decisive for whether
   the one-log saving is technology or new mathematics.
4. Centred-only determinant work: any future cellwise estimates inherit the
   density subtraction; the uncentred route is closed (Section 3).

## 7. Corrected boundary (updates only)

| Status | Items |
|---|---|
| **PROVED** (new) | Completion identities (1.2)/(2.2); character collapse (2.5); n = p isolation; A_{j,p} formula; centred determinant reordering (4.2)-(4.6); uncentred-form lower bound R_R >> H^2/log X. |
| **VERIFIED ONLY** | All of the above on panels (branch: X = 11..23 formal + X <= 337 diagnostics; independently here: X = 11..23 exact + X <= 307 diagnostics). |
| **HEURISTIC / EMPIRICAL** | V/(HX) ~ 0.5 flat; orbit-vs-random covariance indistinguishability (K <= 6, weak); expected HX scale of PBDH_P. |
| **OPEN** | PBDH_P(X) (one-log saving; necessary-scale, not sufficient); **orbit restriction + cross-modulus covariance (the decision point)**; signed physical/higher-conductor contraction; first physical-band theorem; NSMT(X); Fortune variance theorem; Fortune's conjecture. |
| **RETRACTED** | My uncentred SDD(X) box (this document, Section 3, machine-verified in both regimes). The branch's Gate U2 statement of a signed determinant dispersion should likewise be carried forward only in centred form. |

---
*Sources for Section 5:* linked inline above.
