# The block-averaged conditional Hardy–Littlewood theorem

**Date:** 2026-07-21.
**Status:** corrects and supersedes the conditional theorem described in
FRONTIER.md §3 (originally from the ms-lemma workbench track). The
correction responds to a cold-review finding: the earlier *pointwise*
first-moment hypothesis was vacuously strong (at any relative error below
\(1/2\) it forces a prime at every centre directly, making the entire
variance and pair-correlation apparatus redundant). The hypotheses below
are **block-averaged**, which is the weakest natural form under which the
truncated-singular-series lemma is genuinely load-bearing. Notation is
that of Paper II, Section 2: block primes \(\ell_1<\cdots<\ell_N\) in
\([X,2X)\), centres \(P_j\), \(H=\eta X^2\),
\(\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m)\), \(E_j(H)=\Psi_j(H)-H\).
For \(0<|d|<H\) set
\(\pi_{2,j}(H;d)=\sum_{2\le m,\,m+d\le H}\Lambda(P_j+m)\Lambda(P_j+m+d)\),
and let \(\mathfrak S_j(d)\) be the truncated singular series of the
proved lemma (local factors \(p(p-2)/(p-1)^2\) for \(p\le\ell_j\),
\(p\nmid d\); \(p/(p-1)\) for \(p\mid d\); vanishing for odd \(d\)).

## Theorem (block-averaged conditional criterion)

Let \(\varepsilon=\varepsilon(X)\ge0\). Assume, for all sufficiently
large \(X\):

**(H1) block-averaged first moment.**
\[
\sum_{j<N}\Psi_j(H)=NH+O(NH\varepsilon).
\]

**(H2) block-averaged pair correlation, uniformly in the shift.** For
every \(0<|d|<H\),
\[
\sum_{j<N}\pi_{2,j}(H;d)
=(H-|d|)\sum_{j<N}\mathfrak S_j(d)+O(NH\varepsilon).
\]

If \(\varepsilon(X)=o(\log X/X)\), then Paper II hypothesis (2.7) holds
with
\[
L(X)\;\le\;2+O(\eta X\varepsilon)+o(1)\;=\;o(\log X),
\]
and consequently, by Paper II Theorem 2.4, every centre in the block
contains a prime in \([P_j+2,P_j+H]\) for all large \(X\); Fortune's
conjecture holds for all sufficiently large \(n\).

Neither (H1) nor (H2) individually implies the conclusion trivially:
(H1) controls only the block *mean* of the \(E_j\), and (H2) controls
correlations on average over the block — a single centre may a priori
fail while the averages hold, and it is exactly the variance mechanism of
Theorem 2.4 that excludes this.

## Proof

Expand the block variance:
\[
\sum_{j<N}E_j(H)^2
=\sum_j\Psi_j^2-2H\sum_j\Psi_j+NH^2.
\tag{1}
\]

**Diagonal.** \(\Psi_j^2=\sum_m\Lambda(P_j+m)^2
+\sum_{m\ne m'}\Lambda(P_j+m)\Lambda(P_j+m')\). Since
\(\Lambda(P_j+m)\le\log(P_j+H)\le(1+o(1))\,2X\) uniformly in the block
(\(\log P_j\le\vartheta(2X)(1+o(1))\)),
\[
\sum_j\sum_m\Lambda(P_j+m)^2
\le(1+o(1))\,2X\sum_j\Psi_j(H)
\overset{\text{(H1)}}{=}(2+o(1))NHX\,(1+O(\varepsilon)).
\tag{2}
\]

**Off-diagonal.** The \(m\ne m'\) part regroups by \(d=m'-m\):
\(\sum_{m\ne m'}\Lambda\Lambda=\sum_{0<|d|<H}\pi_{2,j}(H;d)\) up to the
boundary convention absorbed in (H2)'s error. Summing (H2) over the
\(2(H-1)\) values of \(d\):
\[
\sum_j\sum_{m\ne m'}\Lambda\Lambda
=\sum_{0<|d|<H}(H-|d|)\sum_j\mathfrak S_j(d)+O(NH^2\varepsilon).
\tag{3}
\]
Write \(\mathfrak S_j=1+(\mathfrak S_j-1)\). The 1-part contributes
\(N\sum_{0<|d|<H}(H-|d|)=N(H^2-H)\). The remainder is
\(\sum_jT_j(H)\) with
\(T_j(H)=\sum_{0<|d|<H}(H-|d|)(\mathfrak S_j(d)-1)\), and the **proved
truncated-singular-series lemma** gives \(|T_j(H)|\le2H\log X\) for all
large \(X\), uniformly in \(j\). Hence
\[
\sum_j\sum_{m\ne m'}\Lambda\Lambda
=N(H^2-H)+O(NH\log X)+O(NH^2\varepsilon).
\tag{4}
\]

**Assembly.** By (H1), \(-2H\sum_j\Psi_j=-2NH^2+O(NH^2\varepsilon)\).
Adding (2), (4), \(-2NH^2+O(NH^2\varepsilon)\), and \(NH^2\) in (1):
\[
\sum_{j<N}E_j(H)^2
\le(2+o(1))NHX
+O(NH\log X)+O(NH^2\varepsilon)-NH.
\]
Dividing by \(NHX\) and using \(H=\eta X^2\):
\[
L(X)\le 2+o(1)+O\!\left(\frac{\log X}{X}\right)+O(\eta X\varepsilon)
=2+O(\eta X\varepsilon)+o(1).
\]
With \(\varepsilon=o(\log X/X)\) this is \(o(\log X)\), so (2.7) holds
and Theorem 2.4 applies. Coverage of every \(n\) by dyadic blocks is as
in Paper II. \(\square\)

## Remarks

1. **Where each ingredient is load-bearing.** The diagonal (2) needs only
   (H1) and saturates the budget at \(L\approx2\); the constant 2 is the
   block-maximal \(\log P_j/X\le2+o(1)\) and could be refined to
   \(\int\)-averaged form. The off-diagonal needs (H2) *and* the
   singular-series bound \(|T_j|\le2H\log X\): without the latter, (4)
   would carry an uncontrolled \(N\cdot O(H\cdot?)\) term. This is
   exactly the role the truncated-series lemma was built for, restoring
   the intended content of the conditional bridge.
2. **The threshold is genuinely \(\varepsilon=o(\log X/X)\).** At
   \(\varepsilon\asymp\log X/X\) the term \(O(\eta X\varepsilon)\) is
   \(O(\log X)\) and (2.7) fails to improve on trivial; below it, the
   criterion closes. Unlike the superseded pointwise version, no
   sub-hypothesis here forces the conclusion by itself.
3. **Explicit-constant variant.** If (H1)–(H2) are assumed with a named
   constant \(C_0\) (error \(\le C_0NH\varepsilon\)), the argument gives
   the numerical threshold
   \(L\le2+2C_0\eta X\varepsilon+o(1)\), which combined with the
   explicit-margin form of Theorem 2.4
   (\(L\le(\eta/4C-\epsilon)\log X\) suffices) yields fully effective
   statements; with anonymous \(\ll\)-constants only the asymptotic form
   above is available.
4. **What this does not do.** (H1)–(H2) at the required strength are far
   beyond current technology, unconditionally or on GRH, for these
   exponentially sparse prescribed centres; the theorem is a calibration
   of the conditional boundary, not progress toward it.
