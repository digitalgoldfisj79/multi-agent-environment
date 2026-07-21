# The d = 1 function-field Fortune attack: results, refutations, and the true wall

**Date:** 2026-07-21.
**Method:** an inline verified reduction (this session) followed by a
seven-agent adversarial workbench (~1.07M tokens, 233 tool calls): five
development tracks (cubic ledger, quadratic exact theory, dataset,
literature, adversary) and two verification tracks (judge, audit), with all
disagreements adjudicated by independent re-derivation and recomputation.
Full agent outputs: `frontier/d1_workbench/`. Dataset:
`frontier/d1_data/`. No fatal flaws survived audit; every claim below
carries its adjudicated status.

**Target.** FF-Fortune(p, 1): for the function-field primorial
\(P_1 = T^p - T\) over \(\mathbb F_p\), the minimal nonconstant \(m\) with
\(P_1 + m\) irreducible is itself irreducible. Proved reduction: it
suffices that some \(T^p + aT^3 + bT^2 + cT + d\) with \((a,b)\ne(0,0)\)
be irreducible (the family with \(\deg m\le3\) *is* the full sparse family;
degree-1 offsets never work; a degree-2/3 minimal offset is automatically
irreducible).

---

## 1. What is now proved (all doubly verified)

**Theorem D1.0 (base case).** FF-Fortune(3, 1) holds unconditionally:
every degree-1 offset fails, \(T^3+T^2-T+1\) is irreducible over
\(\mathbb F_3\), and a minimal degree-2 offset is automatically
irreducible. (At \(p=3\) the general machinery needs corrections — the
degree-3 coefficient collides with the leading term and the master
identity acquires a \(-(Q-p)\) term from the zero polynomial — so \(p=3\)
is handled separately and everything below assumes \(p\ge5\).)

**Theorem D1.1 (master identity).** With \(Q=p^p\), counting
root-incidences and using that roots of degree-\(p\) polynomials in
\(\mathbb F_Q\) have degree 1 or \(p\) (p prime):
\(p\cdot\#\mathrm{irred}_4 = C - p^4\), where \(C\) counts
\((\theta,a,b,c)\in\mathbb F_Q\times\mathbb F_p^3\) with
\(\theta^p + a\theta^3 + b\theta^2 + c\theta \in \mathbb F_p\). Verified
exactly at \(p=3,5,7\). The wild term linearizes:
\(\mathrm{Tr}(t\theta^p)=\mathrm{Tr}(t^{1/p}\theta)\), giving the full
character expansion into complete cubic Weil sums
\(W(ut, vt, wt+t^{1/p})\) over \(\mathbb F_Q\).

**Theorem D1.2 (orbit structure).** The affine group \(x\mapsto\lambda
x+\alpha\) acts on the family preserving irreducibility; Fortune-relevant
orbits have trivial stabilizers. Hence, exactly,
\(\#\mathrm{irred}_2 = p(p-1)N(p) + (p-1)\) with
\(N(p)=\#\{d:\ x^p+x^2+d\ \text{irreducible}\}\), the \((p-1)\) being the
excluded Artin–Schreier orbit. New (judge): the involution
\(f(T)\mapsto -f(-T)\) acts freely on the relevant slices, so
\(2p \mid \#\mathrm{irred}_a\) for \(a\ne0\), \(p\ge5\) — confirmed by
every slice count in all datasets.

**Theorem D1.3 (quantized Kloosterman identity — the surprise).** With
\(\eta\) the quadratic character of \(\mathbb F_Q\), \(G_Q\) its Gauss sum
(Hasse–Davenport: \(G_Q=G_p^p\)):
\[
N(p) \;=\; p^{-p}\,G_Q\,S(p),\qquad
S(p)=\sum_{\tau\in\ker\mathrm{Tr}\setminus0}
\eta(\tau)\,e_p\bigl(-\tfrac14\mathrm{Tr}(\tau^{2-p})\bigr),
\]
and moreover the hyperplane decomposition \(S(p)=\frac1p\sum_u T_u\) has
**every** piece exactly evaluated:
\(T_u=\eta(-1)G_Q\,(R(u)-1)\) where \(R(u)\in\{0,1,2,p\}\) is the
\(\mathbb F_Q\)-root count of \(x^p+x^2+u\). So
\(S(p)=\eta(-1)G_Q\,N(p)\): the twisted Kloosterman-type sum over
\(\mathbb F_{p^p}\) is *quantized* — its final value is exactly
determined by an integer root count (term-by-term the sum does exhibit
cancellation; the point is that the total collapses to the quantized
lattice \(\eta(-1)G_Q\cdot\mathbb Z_{\ge0}\)), so no analytic estimation
can decide its positivity. Verified exactly at \(p=3,5,7\) (at \(p=7\):
117,648 terms over \(\mathbb F_{7^7}\), \(S(7)=i\cdot7^{7/2}\) on the
nose). The literature agent found no prior occurrence of this object or
identity; however, the adjacent literature connecting Kloosterman/Gauss
sums to counts of irreducible polynomials with prescribed trace and norm
(notably the Moisio line of work, and recent norm-trace counting in
finite algebras) is substantial, so novelty should be treated as a
*candidate pending a dedicated primary-source review* of that corpus,
not as established.

**Theorem D1.4 (exact ledger and reduction of the Target).**
\[
\#\mathrm{irred}_4=(p-1)+p(p-1)N(p)+(p-1)\bigl(p^2-p^{3-p}\bigr)
+p^{2-p}\!\!\sum_{a\ne0}R_a,
\]
with \(R_a\) an explicit incidence character sum over
\(V_t=\{\mathrm{Tr}(t\theta)=\mathrm{Tr}(t\theta^2)=0\}\)
(\(|V_t|=p^{p-2}\) exactly; \(\#\mathrm{irred}_a\) depends only on
\(\chi(a)\)). Consequently the Target follows from **Lemma L**:
\(|\sum_{a\ne0}R_a| < (p-1)(p^p-p)\). Empirically the sum is
\(\approx -0.16\,(p-1)p^p\) — a factor ~6 inside the required bound.

**Theorem D1.5 (local structure).** For \(x\in\mathbb F_p\), a family
member equals its cubic tail at \(x\); hence the linear-factor structure
is exactly the splitting of the tail, and the number of rootless
\((c,d)\) per slice is exactly \((p^2-1)/3\) — a deterministic
singular-series factor with leading constant \(\tfrac13 e\approx0.906\),
which correctly postdicts both the observed slice density
(\(0.842+0.618/\sqrt p\) fit, residuals clean under pair-Poisson variance
\(2p\)) and the observed quadratic-family mean \(N\approx1.18\).

**Verification.** FF-Fortune(p, 1) is machine-certified for **every odd
prime \(p<1200\)**: \(N(p)\ge1\) gives quadratic witnesses where
possible, and explicit certified cubic witnesses (e.g.
\(T^{97}+T^3+1\); \((a,b,c,d)=(1,0,10,58)\) at \(p=401\)) cover all 53
quadratic-failure primes; all witnesses independently re-certified by the
audit with different code, and the \(N(p)\) table (238 primes to 1500)
reproduced by three independent implementations.

## 2. What was refuted (including my own proposals)

1. **The quadratic family cannot carry the theorem.** \(N(p)=0\) occurs —
   first at \(p=31\), for 61 of 238 primes \(\le1499\) (25.6%),
   all 61 exhaustively re-confirmed by the audit. The small-\(p\) pattern
   \(N\in\{1,2\}\) that motivated the normal-form attack was an accident
   of the first seven primes. Statistically \(N(p)\) is close to
   Poisson(\(e/2\)) conditioned on the rootless count (the zero-fraction
   matches 0.257 vs 0.256 observed) with a genuine mild underdispersion —
   but nothing classifies the zero set (no congruence pattern mod any
   \(k\le60\); no standard residue-symbol correlation).
2. **The cubic ledger has no polynomial room.** My briefing's error
   budget was wrong by an exponential factor: the needed saving over
   per-term Weil on the \(u\ne0\) aggregate is \(\sim2p^{p/2-1}\), not
   \(p^{1/2+\varepsilon}\). The \(\alpha=0\) strata do **not** contain the
   \(p^3\) main term — they sum to exactly \(\#\mathrm{irred}_2\), which
   vanishes precisely at the quadratic-failure primes.
3. **Every exact averaging device is circular.** The phase is linear in
   \(t\), so complete \(t\)-averages are Plancherel deltas reconstructing
   the unknown count; the second moment is diagonal-dominated with
   \(\mathrm{RMS}|W|=\sqrt Q\) exactly (verified to the digit at
   \(p=5\)); Cauchy–Schwarz returns the trivial bound with zero gain. The
   \(\gamma\)-completion trick I proposed is structurally impossible
   (\(\gamma\) ranges over a \(p\)-point line at fixed \(t\);
   \(L_w(t)=wt+t^{1/p}\) is bijective on \(\ker\mathrm{Tr}\) iff
   \(w\ne-1\); \(\alpha,\beta\) co-move with \(t\)).
4. **The elementary route exactly reproves Artin–Schreier and nothing
   more.** The only positivity-evaluable stratum (\(t\in\mathbb F_p^*\))
   contributes exactly the excluded \((p-1)\).
5. **The wall is the same wall.** Via the equivalent reformulation
   \(p\cdot\#\mathrm{irred}_4=\#\{\theta\notin\mathbb F_p:\theta^p\in
   \mathrm{span}_{\mathbb F_p}(1,\theta,\theta^2,\theta^3)\}\), the error
   is a bilinear-phase character sum over a codimension-4, degree-\(\le4\)
   variety in \(\mathbb A^{2p}\) requiring square-root cancellation with
   constant \(\le p^2\), where general Betti/complexity bounds are
   exponential in \(2p\) (dynatomic model: degree \(3^p\)). The
   fixed-\(q\), growing-degree obstruction of the Sawin framework returns
   in elementary clothing.

## 3. The adjudicated frontier

The judge's verdict: **hard-but-well-posed** — and *not* critical in the
strong sense the cubic writeup initially claimed. The truth has a stable
positive density with a *derivable* leading constant (Theorem D1.5), the
fluctuating part decays relatively like \(p^{-1/2}\) (pair-Poisson, not
random-sign-critical), and failure of the Target at a prime would require
the conjunction of an \(\sim\!\sqrt{p}\)-sigma downward fluctuation, the
exact quantized vanishing of both slice invariants (each in
\(2p\,\mathbb Z_{\ge0}\)), and \(N(p)=0\). Ranked residual routes:

1. **Singular-series main term.** Prove
   \(\#\mathrm{irred}_a=\sigma_a(p)\,p^2(1+o(1))\) with
   \(\sigma_a\) bounded below — the deterministic component now has a
   candidate local-statistics derivation; the residual is *any*
   \(o(p^p)\) bound on the fluctuating part of \(R_a\). This is the
   growing-dimension square-root-cancellation wall, precisely isolated.
2. **Mass formulas.** Stickelberger/discriminant character sums over the
   4-dimensional family to exclude the exact vanishing event without
   asymptotics.
3. **Constructive dynamics.** \(T^p-g(T)\) is irreducible iff
   \(x^p=g(x)\) has a solution of exact \(g\)-composition-period \(p\)
   (proof confirmed); a single explicit \(g\)-family with a provable
   period-\(p\) orbit for every \(p\) would finish it outright.

## 4. Honest bottom line

The proper run produced real theorems — the quantized Kloosterman
identity D1.3 is, to the best of a thorough literature search, a new
phenomenon, and the exact ledger reduces FF-Fortune(p,1) to one clean
inequality with a factor-6 empirical margin — and it *disproved* both of
my proposed shortcuts honestly: the quadratic family fails for a quarter
of primes, and the cubic ledger needs exponential savings that no current
technology provides. FF-Fortune(p,1) now stands: proved for \(p=3\),
machine-certified for all \(p<1200\), reduced to Lemma L in general, with
the obstruction identified exactly as fixed-\(q\) square-root cancellation
in growing dimension — the precise point where the function-field problem
is honest about being the same depth as its integer sibling, while still
offering three structured routes the integer problem does not have.
