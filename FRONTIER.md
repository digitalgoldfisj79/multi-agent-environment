# Beyond the boundary: three new fronts for the Fortune programme

**Date:** 2026-07-21.
**Method:** nine-agent adversarial workbench — five development tracks run in
parallel, then four independent verification tracks (reconciliation judge,
citation audits, independent re-derivations, from-scratch numerical
reimplementations). Full writeups, per-claim verdicts, and audit reports are
preserved verbatim in `frontier/workbench/*.json`. No fatal flaws were found
on any track; every correction the audits demanded is applied in this
document. Nothing here proves Fortune's conjecture or PGD2, and no unproved
statement is called a theorem.

The question answered here: *is there a way past the problems that have
resisted the programme?* The answer has three parts: a new unconditional
model theorem that removes GRH from the architecture's certification and
pinpoints the true residual wall; a new setting (function fields) where a
first Fortune-type theorem is writable now and a second, full Fortune-type
statement reduces to a concrete open geometric bound; and the completed
unconditional core of the conditional-anchor route. A large-scale numerical
exchangeability test supports the first part.

---

## 1. The RQM assembly target: an unconditional random-order model result

**Statement (status: provable-sketch; every component lemma proved and
independently verified; remaining work is assembly write-up, est. 5–10 pages,
low risk).** Fix \(0<\eta<1\) and the Paper II frame (Section 3) verbatim.
Let \(\sigma\) be a uniformly random ordering of the \(K\) block primes of
\([X,2X)\), and run the entire reciprocal-frame construction along the
\(\sigma\)-path \(P_j^\sigma = A_X\prod_{i\le j}\ell_{\sigma(i)}\). Then,
unconditionally, with effective constants:

1. \(\mathbb E_\sigma[\mathcal E_a^\sigma] \le C(\eta,\rho)\,M(\log X)^{C_0}\)
   uniformly for **every** integer \(1\le|a|<H\);
2. \(\mathbb E_\sigma\bigl[\sum_{a\ge1}\mathcal R_a^\sigma/m_a\bigr] \le
   CM(\log X)^{C_0}\) and \(\mathbb E_\sigma[\mathfrak F_X^\sigma]\le
   CM(\log X)^{C_0}\) — the full weighted aggregate target (12.1)/(3.6) in
   expectation.

By Markov, all but an \(\omega^{-1}\) fraction of the \(K!\) orderings
satisfy the \(\sigma\)-path aggregate target with loss
\((\log X)^{C_0}\omega\).

**Why this goes beyond the archive.** Every prior route died at the same
wall: character or exponential sums over the block primes at length
\(\asymp\sqrt{\mathrm{conductor}}\), where no unconditional method exists.
The mechanism here is different in kind: **order entropy manufactures the
per-character decay, and the only arithmetic input is a *count* of
non-cancelling characters** — obtained from orthogonality and unique
factorization, not from cancellation. The full ingredient list, after
adversarial repair, is remarkably small:

- **Exact rank-conditioning partition identity.** Conditioning on the rank
  positions of the (at most four) indices in a difference \(S_u-S_v\), the
  cell contents of the \(\sigma\)-path are exactly a uniform ordered set
  partition, and the expectation of any product of character values over the
  cells is an exact multinomial coefficient extraction from
  \(\prod_{\ell}\bigl(\sum_s x_s\psi_s(\ell)\bigr)\). No Poissonization, no
  label-interval approximation, no jump-time/fixed-time debt. *Verified
  exhaustively over all \(7!=5040\) orderings of a 7-prime block (agreement
  to \(10^{-15}\), against the true \(\sigma\)-path law).*
- **Cauchy-contour/Stirling decay.** The coefficient extraction is bounded
  by \(CK^2\exp\bigl(-\sum_{s<s'}(n_sn_{s'}/K)(1-t_{\psi_s\bar\psi_{s'}})\bigr)\),
  with \(t_\chi = |\sum_{\ell}\chi(\ell)|/K\) — pairwise-cell decay in the
  *ratio* characters.
- **Character counting at constant deficit.** Only characters with
  \(t_\chi\ge 3/4\) escape the decay, and an elementary sixth-moment count
  (products of three block primes are \(<(2X)^3<qr\), so unique
  factorization applies) bounds these by \(O(X\log^3X)\) per modulus
  \(qr\). **No zero-density theorem, no explicit formula, and no GRH are
  needed anywhere.** (An optional cosmetic strengthening to \(X^{o(1)}\)
  bad characters can cite the log-free density of Chen, arXiv:2507.08296,
  whose Theorem 1.4 was verified verbatim.)
- **Gauss sums/CRT, and trivial counting of degenerate configurations**
  (pairs with two or more micro cells number only \(X^{2+o(1)}\)).

**Corrections applied from the adversarial review.** (i) The original
sketch's Steps 3–4 as literally written do *not* close — the zero-density
route reaches character deficit \(\sim1/\log X\) while the assembly needs
deficit at the \(\log^2X/X\) scale; the repair moves the badness threshold
to the constant \(1/4\), where the sixth-moment count suffices. (ii) A
claimed \(X^{1/3}\) safety margin in the binding case (one macro cell, three
bad ratio characters) was refuted by the reconciliation judge: the margin
there is **polylog only**, and the manuscript must track it. (iii) The
constant-slot term of the sketch was wrong (\(Q_{\min}\) is itself random);
the repair uses five cells and four character slots.

**Honest scope (to be stated verbatim in any write-up).** The
\(\sigma\)-path centres are not primorials; this is a model theorem about
the architecture. It is the first unconditional PGD2-type estimate in any
model, it removes GRH from the i.i.d.-model input (vector B2), and it
certifies that the reciprocal-frame target is *true generically at the
critical length*. It relocates rather than shrinks the Fortune-relevant
difficulty: a single order has zero entropy, and the mechanism contributes
nothing pointwise. The forward-looking mathematics it opens is the variance
version \(\mathbb E_\sigma[(\mathcal E_a)^2]\ll M^2X^{o(1)}\) (same
machinery, ~8 cells), which would upgrade expectation to concentration over
orderings.

## 2. Function fields: a first Fortune-type theorem, and the open crown

Define \(P_d=\prod\{\,f\in\mathbb F_q[T]\text{ monic irreducible},\ \deg f\le
d\,\}\), \(n=\deg P_d=\sum_{e\le d}e\,\pi_q(e)\sim q^d\), and the Fortunate
element \(F(q,d)\) as the minimal nonconstant \(m\) (by degree, then
lexicographic) with \(P_d+m\) irreducible. **Proved reduction:** any
reducible \(m\) coprime to \(P_d\) has all irreducible factors of degree
\(\ge d+1\), hence \(\deg m\ge 2d+2\); so an irreducible value \(P_d+m\)
with \(\deg m\le 2d+1\) forces \(F(q,d)\) irreducible — the exact analogue
of \(F_n\ge p_{n+1}^2\).

**The coupling obstruction, verified against the literature.** The centre
degree \(n\sim q^d\) grows with \(q\), and this defeats every existing
short-interval technology *by an explicitly computed margin*: Lang–Weil
saves only \(\sqrt q\) against a main term thinned by \(1/n\)
(Bank–Bary-Soroker–Rosenzweig, arXiv:1302.0625); Sawin's interval-variety
bounds (arXiv:1809.05137) carry a Betti factor \((n+2)^{2n-h}\), exponential
in \(n\) at \(h=2d+2\); Sawin–Shusterman (arXiv:1808.04001) needs squarefree
averaged moduli while our family is a single class modulo the perfect power
\(T^{\,n-h}\); Ha (arXiv:1601.06867) needs \(\sim n/4\) prescribed
coefficients where we have \(n-O(\log_q n)\); Keating–Rudnick
(arXiv:1204.0708) is a \(q\to\infty\) variance average. All five statements
were re-read and verified verbatim by two independent agents.

**Target Theorem 1 (provable-sketch; writable now).** Unconditionally, for
every \(q\) and all large \(d\): \(F(q,d)\) exists and is either irreducible
or of degree in \([2d+2,\ n/2+2\log_qn+O(1)]\). The only input is the Weil
Riemann Hypothesis (the one tool whose error is polynomial in the centre
degree). Over \(\mathbb Z\) the analogous exponent-\(1/2\) window statement
requires RH (unconditionally, Baker–Harman–Pintz reach exponent 0.525) — so
this is the strongest Fortune-type statement provable in any setting today,
phrased with that comparison made carefully.

**Target Theorem 2 (open crown; genuinely new mathematics, passes the
archive stop-rule).** For every prime \(p\ge3\) there exists \(m\) with
\(\deg m\in\{2,3\}\) such that \(T^p-T+m\) is irreducible over
\(\mathbb F_p\). With the proved reduction (and the proved micro-lemma that
*no degree-one offset ever works at \(d=1\)* — the affine additive map
\(T^p-T\) is bijective, the same solvable-monodromy mechanism as BBR's
counterexamples), this would give **full FF-Fortune for \(d=1\) over every
prime field** — the first complete Fortune-type theorem for an infinite
family in any setting. The precise obstruction was identified: the family is
Sawin's 4-dimensional interval variety at the additive centre \(T^p-T\), and
the theorem follows from a polynomial-in-\(p\) bound \(B(\pi)=o(p)\) on its
compactly supported Betti sum, versus Katz's generic
\(3(p+2)^{2p-4}\). A fixed 4-dimensional variety with extra
additive/\(S_p\) structure, finitely checkable per \(p\); wild
characteristic-\(p\) geometry, entirely disjoint from the archive's closed
reciprocal-frame kernel. Eighteen exact-arithmetic cases (\(p\le19\),
\(n\le145\)) confirm the conjecture, with \(\deg F(q,d)\sim\log_qn\) —
mirroring \(F_n\sim\log P_n\) exactly.

## 3. The conditional anchor, now with its unconditional core proved

The Paper III route (vector B1) is complete at the lemma level; both the
derivation and the numerics were independently re-done by the auditor.

- **Truncated singular series (proved).** At a primorial centre (divisible
  by exactly the primes \(\le\ell_j\)) the pair \((P_j+m,P_j+m+d)\) has
  local factor \(p(p-2)/(p-1)^2\) for \(p\le\ell_j\), \(p\nmid d\), and
  \(p/(p-1)\) for \(p\mid d\); primes \(p>\ell_j\) contribute \(1+O(1/X)\)
  in total.
- **Second-moment lemma (proved).**
  \(T_j(H)=\sum_{0<|d|<H}(H-|d|)(\mathfrak S_j(d)-1) =
  -2C_jH\sum_{u\mid \mathrm{odd}(P_j),\,u<H/2}1/\varphi_2(u)+O(H)\), with
  the load-bearing bound \(|T_j(H)|\le 2H\log X\). The sharp constant is the
  Dickman integral \(I(2)=3-2\log2\approx1.6137\) (provable-sketch,
  non-load-bearing, numerically confirmed to 4–6% and improving) — *not*
  the untruncated \(-H\log H\); the truncation at \(\ell_j\sim2X\ll H^{1/2}\)
  changes the logarithm scale, and the numerics confirm the truncated
  constant against the untruncated overshoot in every tested case.
- **Conditional theorem — SUPERSEDED (see `CONDITIONAL_HL_BLOCK.md`).**
  The theorem as originally stated hypothesized a *pointwise* first-moment
  approximation \(\Psi_j(H)=H+O(H\varepsilon)\) at every centre. A cold
  review correctly observed that this hypothesis is vacuously strong: at
  any \(\varepsilon<1/2\) it directly forces
  \(\Psi_j(H)\ge H/2>o(H)\) beyond the prime-power contamination, hence a
  prime at every centre — the conclusion — with no variance argument, no
  pair correlation, and no singular-series input. (Equivalently,
  \(|E_j|\ll H\varepsilon\) pointwise makes the block variance trivial
  already at \(\varepsilon=o(\sqrt{\log X/X})\).) The pair-correlation
  machinery becomes genuinely load-bearing only under **block-averaged**
  hypotheses: first and second moments averaged over the \(N\) centres,
  uniformly in the shift \(d\). The corrected theorem — block-averaged HL
  with relative error \(\varepsilon=o(\log X/X)\) implies (2.7) with
  \(L\le2+O(\eta X\varepsilon)+o(1)=o(\log X)\), hence Fortune for all
  large \(n\) — is stated and proved in full in
  `CONDITIONAL_HL_BLOCK.md`, where the truncated-singular-series lemma
  \(|T_j(H)|\le2H\log X\) does exactly the work it was built for.

The corrected headline: Fortune follows from *block-averaged*
Hardy–Littlewood at primorial centres at relative accuracy
\(o(\log X/X)\); the earlier pointwise phrasing overstated the depth of
the conditional bridge.

## 4. Order-ensemble numerics: the increasing order is exchangeable

Experiment (`frontier/order_ensemble.py`, seed 20260721; audited, exactly
reproduced, and independently reimplemented from spec): for
\(X\in\{300,1000,3000,10000\}\) (up to \(K=1033\) block primes — the true
critical length \(K\asymp q^{1/2}/\log q\)), 40 prime moduli
\(q\in[X^2,2X^2]\), harmonics \(a\in\{1,2,3\}\), the normalized walk energy
\(V=|\sum_j e_q(aA_XQ_j)|^2/K\) was compared between the increasing order,
the decreasing order, a \(q\)-dependent adversarial order, and 200 uniform
random orders per modulus.

Findings (audited): the random-order null is Exp(1) to within sampling error
(cell means 0.986–1.023, sds 0.951–1.019) — the walk is Steinhaus-generic at
the critical length; the increasing order's percentiles within the ensemble
are uniform (all 36 per-cell KS statistics below critical, pooled mean
percentile 0.52 with the mild lean shared by all tested orders, i.e.
ensemble noise); no exploitable structure separates the true order from a
random one at these scales. One design flag: the originally specified
adversarial order (sort by \(\ell\bmod q\)) is *definitionally* the
increasing order since \(q>2X\) — caught, confirmed for all 160 moduli, and
replaced by a genuinely \(q\)-dependent adversary (also generic). Also
recorded: at a single modulus the single-walk energy is an exact linear
function of \(V\) (\(G=K(V-1)\)), so \(V\) carries all the information.

This is the evidence one wants before investing in the RQM assembly: no
finite-size derandomization obstruction is visible. It is also the honest
flip side: order-genericity offers no lever the true order visibly lacks.

## 5. The frontier map after this round

1. **Complete the RQM assembly** (write-up G1; days of work, low risk,
   polylog margin in the binding case must be tracked). It is the
   epistemically cleanest artefact the programme can currently produce:
   unconditional, GRH-free, first of its kind, honest about scope.
2. **Write Target Theorem 1** (function-field Fortunate window via Weil RH)
   — the first Fortune-type theorem in any setting, available now.
3. **Write Paper III** (conditional anchor) from the proved lemmas of §3.
4. **The two named walls, precisely isolated and strictly disjoint:**
   (a) *derandomization* — from almost-all orderings to the single
   increasing order (equivalently, from random nested subsets to the value
   initial segments \(\{\ell\le y\}\)); the concentration upgrade
   \(\mathbb E_\sigma[(\mathcal E_a)^2]\) is the one tractable-looking step
   toward it, and the top-level atom counting of the Paper II addendum
   (Corollary A.10) is its arithmetic shadow;
   (b) *the Betti bound* \(B(\pi)=o(p)\) for Sawin's interval variety at the
   additive centre — wild ramification geometry, new territory, finitely
   checkable per \(p\), and the single obstacle to the first full
   Fortune-type theorem (\(d=1\) function fields).
5. **Stop-rule compliance:** all three fronts were explicitly audited
   against the archive's no-go inventory; none restates the closed kernel.
   The \(q\)-fixed, \(d\to\infty\) function-field regime was checked and
   flagged as the integer critical-length wall in disguise — it is *not* a
   route.

## Provenance

Nine agents, ~1.16M tokens, 117 tool calls. Verification highlights: the
partition identity checked against the true \(\sigma\)-path law over all
5040 orderings of a 7-prime block; Chen arXiv:2507.08296 Theorem 1.4 read
and confirmed verbatim; five function-field papers re-read verbatim by two
agents independently; the \(T_j(H)\) identity reproduced in exact rational
arithmetic at seven parameter choices by two independent implementations;
the order-ensemble JSON reproduced bit-identically and cross-validated by a
from-scratch reimplementation. One exponent error, one overstated constant,
one definitional flag, and three cosmetic misstatements were caught by the
audits and are corrected above. Full detail: `frontier/workbench/`.
