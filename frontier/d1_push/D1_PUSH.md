# The d=1 crown push: the door looked through, the certificate sharpened

**Date:** 2026-07-22.
**Method:** five-agent workflow (four worktree-isolated developers + an
adjudicator that re-tested every load-bearing claim with independent
code; zero inter-agent contradictions). Full agent outputs:
`workbench/`. Scripts and data: this directory and `hook_spectra/`.
**Honest scope:** the function-field d=1 crown remains open; everything
below sharpens the two live routes. Integer Fortune is untouched.

## 1. Route B breakthrough: the surviving object is identified (p=5 exact)

First-ever computation of the post-pushforward Frobenius spectra behind
the hook-cohomology door, on the explicit normal-form family
\(f_q(z)=(qz^p+z^3-3z)/(q-2)\):

- **p=5, complete.** All five characteristic polynomials
  \(L_i(T)=\det(1-TF\,|\,H^1_c(U,V_i))\) determined for every generic q,
  out-of-sample validated through j=9. The even/odd cancellation is
  real and fully identified: **every weight-0 constituent cancels except
  the single Kummer class \(\chi(u_q(t^2-1))\), \(u_q=3q(q-2)^2\); the
  weight-1 survivors are exactly \(H^1(B_q)\) (an explicit pair curve)
  on the even side minus \(H^1(D_q)\) (the genus-2 twist curve
  \(w^2=u_q\,g_{q,+}g_{q,-}\)) on the odd side** — verified by
  independent point counts, with the exact fiber-count formula
  \(5\,I_j(q)=5^j-[\chi(u_q)^j+a_j(B_q)-a_j(D_q)]\).
- Surviving rank: 3 at q=1 (where \(H^1(B_1)\) is an isogeny factor of
  \(\mathrm{Jac}\,D_1\)), else 7 = p+2. The q=2 boundary fiber is solved
  in closed form (extra Tate class), closing the normal-form
  reconstruction (checked: \(N_1(5)=4,\ N_2(5)=6\)).
- **p=7, substantial:** \(L_0,L_1,L_6\) exact; \(L_5=(1\mp T)^2\cdot
  L(D_q)\) with \(D_q\) genus 4; \(V_2\) has a unique structured fit
  with one elliptic weight-1 factor at all tested q; unconditional Weil
  lower bound: surviving rank ≥ 14 at q=5.
- **Scaling (p=5,7,11):** rms-estimated surviving rank ≈ 4, 22, 40 —
  linear ~4p. The exponential (Swan-total) scenario is *excluded* by the
  data (would predict rms 27 at p=11 vs observed 6.3). **The door's
  O(p) collapse is empirically supported.** Both ε-families are twist
  readings of one surviving object per q (verified exactly at p=5).

Consequence: the crown becomes a **q-averaged trace bound on two
explicit curve families** (B and D, surfaces of degree O(p) fibered over
the q-line) plus exact Kummer/boundary terms — a polynomial-size
problem. Two proved cautions temper it: pointwise Weil at j=1 cannot
finish (cells with zero irreducible fibers exist, e.g. p=7, q∈{1,6});
and even granting the full collapse, naive Weil II on the q-line gives
only \(N_a=p+O(p)\) — the remaining fight is over the *constant*.

## 2. Route A sharpened: the Cartier certificate

- GCC.1 re-verified independently (1182 cofactor evaluations, 0
  mismatches; the \(X^p-s\) exclusion is load-bearing). Explicit
  trinomial-coefficient formula for the Cartier entries proved.
- \(S_a(p)=\sum_{c,d}C_3\) reduced exactly to survivor coefficients
  \([c^{\alpha(p-1)}d^{\beta(p-1)}]\) of the (p−1)-minor determinant;
  computed fully symbolically for p=5..17 and equal to \(3aN_a(p)\) in
  every case. Small-p closed forms: \(S_a(5)=2a^3\), \(S_a(7)=6a+3a^4\).
- **Proved survivor law:** every survivor coefficient has
  \(i\equiv1\bmod{(p-1)/2}\) in the a-grading, so
  \(S_a=a(A_p+B_p\chi(a))\) — a matrix-side derivation of the two-class
  structure, with \(A_p=3(N_++N_-)/2\), \(B_p=3(N_+-N_-)/2\) mod p.
- **The named gap:** the empirical support/cancellation law
  \(\alpha+2\beta\le(p+1)/2\) (weighted degree \((p^2+2p-9)/2\)) sits
  strictly *below* the naive assignment bound (excess 1,2,9,14,29,38 at
  p=5..19) — an exact, unexplained cancellation mechanism inside the
  Cartier determinant.
- **Honest negatives:** 289 elliptic curves and 180 truncated
  hypergeometric candidates all fail to match \(S_a(p)\) mod p over 30
  primes; no match to standard factorial/binomial constants. By
  contrast the discriminant-character mass has a fully **proved closed
  form** (\(\chi(3a)p\) for p≡1 mod 4; \(2\chi(-3a)p\cdot[\chi(2a)=1]\)
  for p≡3 mod 4) — the disc locus is genus-0 exact, so parity/disc
  sieves cannot see the \(N_a\) fluctuation.
- **Certificate completeness (new):** \(N_a\) is even and p odd, so
  \(N_a=p\) is *unconditionally excluded*; the mod-p certificate can
  fail only if \(N_a\in\{0,2p,4p,\dots\}\). (Correction: this
  session's earlier briefing claimed "\(N_a<p\)" as size control —
  **false**, first exceedance at p=7, e.g. \(N_1(127)=156\); the parity
  protection is what actually saves the route.) All cofactors other
  than \(C_3, C_1\) vanish identically on the depressed slice; among
  moment certificates only the bare count is parity-protected.

## 3. Soft spots closed; one new subtlety

Both prior audit gaps are now CONFIRMED by dedicated re-derivation:
Wall B's ledger reproduced row-for-row at p=5..13 with independently
computed invariants, and the wild-inertia theorem
(\(I_\infty=C_p\rtimes C_{(p-1)/2}\), single jump (p−3)/2, tame
transpositions at t=±1) verified by direct local computation over all
parameters at p=5,7. New subtlety worth recording: the *arithmetic*
Galois group at infinity can exceed the geometric inertia by an
unramified quadratic (e.g. p=5,a=1,c=0) — the branch doc's claim stands
as geometric, but a naive discriminant-square test over
\(\mathbb F_p((s))\) would falsely refute it.

## 4. Missed-items sweep: no missed route; four small new results

No obvious missed route to the crown. New: (i) the parity-protection
lemma (above); (ii) a proved partition rule: the two a-classes cover
complementary halves of the 2(p−1) normal-form cells (q,ε), determined
by p mod 4 — joint failure requires all 2(p−1) per-cell counts to
vanish, and an exhaustive congruence search finds no coupling relation
beyond 2|N_a; (iii) the constructive no-go classification is TRUE
(proved symbolically: any cubic affinely conjugate to an odd cubic over
the closure has an F_p-rational fixed point — zero constructive room);
(iv) the irreducible (c,d)-locus shows no correlation with any tested
character invariant (~700k-member tests; the one 2.9σ candidate failed
replication with flipped sign).

## 5. The decisive lemma (adjudicated)

**Weight-0 collapse lemma (general p):** all weight-0 Frobenius
constituents of the hook ledger cancel after even/odd semisimplification
except the single Kummer class \(\chi(u_q(t^2-1))\). Proved at p=5,
consistent at p=7, and *purely tame/combinatorial* (puncture permutation
modules + cyclotomic data — no wild subtleties). Its proof mechanism —
an explicit parity-reversing correspondence — is the prototype for the
weight-1 sector and hence for the entire O(p) collapse. Next after
that: assemble the identified B- and D-families over the q-line and
fight the \(N_a=p+O(p)\) constant.

## 6. State of the crown after this round

Proved for p < 1200. For general p, per a-class, the crown is
equivalent to \(N_a\notin\{0,2p,4p,\dots\}\) and attackable by two now
much sharper routes: (A) prove the Cartier support/cancellation law and
evaluate the survivor sum; (B) prove the weight-0 collapse lemma, then
the weight-1 correspondence, then win the constant battle on two
explicit O(p) curve families. Route B changed character this round —
from "prove an unspecified exponential-to-linear miracle" to "prove
that *this specific, empirically verified* list of survivors is
complete." That is the first time in the programme the door has had a
shape.
