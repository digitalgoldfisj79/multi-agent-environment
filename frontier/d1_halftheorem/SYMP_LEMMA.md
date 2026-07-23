# The Sym^p moment lemma: a linear-complexity target for the first infinite Fortune-type theorem

**Date:** 2026-07-23. **Status:** problem statement (specialist-ready) +
exact empirical calibration. Nothing here is proved beyond the displayed
identities; the Lemma is open.

## 1. What it implies

By the committed WTCK reduction
(`frontier/d1_push/WILD_TRACE_CUBIC_KUMMER_REDUCTION_THEOREM.md` on
branch `gpt56/d1-push-weight0-collapse-20260722`) together with the phase
plan's remaining steps, a uniform weight-3 bound for the p ≡ 2 (mod 3)
nonzero-fibre constant — plus the b=0 punctual separation — yields the
Cyclic-Adams weight-three estimate and hence **FF-Fortune(p, 1) for every
prime p ≡ 2 (mod 3)**: the first infinite family of Fortune-type results
in any setting. The probe `HALF_THEOREM_PROBE.md` showed this constant is
a genuine arithmetic quantity (no fixed ledger line), so the bound below
is the minimal missing analytic ingredient.

## 2. Exact reduction to a symmetric-power moment

Fix p ≥ 5 and b ∈ F_p^*. For (u, v) ∈ F_p × F_p^*, let

\[
S_1(u,v)=\sum_{x\in\mathbb F_p}\psi(ux+vx^3),\qquad \psi=e_p,
\]

whose L-function has degree 2 with inverse roots
\(\alpha_{u,v},\beta_{u,v}\) of weight 1 (\(|\alpha|=|\beta|=\sqrt p\)),
determinant \(\alpha\beta = p\,\eta_{u,v}\) with \(|\eta_{u,v}|=1\)
explicit (quadratic-character/Gauss-sum unit of the cubic sum). The WTCK
recurrence identity gives, exactly,

\[
D_b \;=\; N_b-p^{\,p-2}
\;=\;-\,p^{-2}\!\!\sum_{v\ne0,\,u}\psi(-vb)\,\bigl(\alpha_{u,v}^{\,p}+\beta_{u,v}^{\,p}\bigr).
\]

Using \(\operatorname{tr}\mathrm{Sym}^k = \sum_{i=0}^k\alpha^i\beta^{k-i}\)
and the elementary identity
\(\alpha^p+\beta^p=\operatorname{tr}\mathrm{Sym}^p-\alpha\beta\cdot
\operatorname{tr}\mathrm{Sym}^{p-2}\):

\[
p^2 D_b=-\sum_{v\ne0,\,u}\psi(-vb)\Bigl[\operatorname{tr}\mathrm{Sym}^p(\mathrm{Fr}_{u,v})
-p\,\eta_{u,v}\operatorname{tr}\mathrm{Sym}^{p-2}(\mathrm{Fr}_{u,v})\Bigr],
\]

a **twisted p-th symmetric-power moment of the rank-2 cubic-sum (Airy)
local system over the two-parameter (u,v)-plane**. Its geometric
monodromy is SL₂ (Katz, *Exponential Sums and Differential Equations*,
for the Airy/cubic family), Sym^p has rank p+1, and the Swan conductors
of Sym^p along the boundary of the parameter space grow **linearly** in
p. The exponential-rank obstruction that blocked every previous
formulation is absent here.

## 3. The Lemma (open)

**Lemma (Sym^p moment bound).** There is an absolute constant C such
that for every prime p ≥ 5 and every b ∈ F_p^*,

\[
\Bigl|\sum_{v\ne0,\,u}\psi(-vb)\,\bigl(\alpha_{u,v}^{\,p}+\beta_{u,v}^{\,p}\bigr)\Bigr|
\;\le\; C\,p^{(p+1)/2},
\]

equivalently \(|D_b|\le C\,p^{(p-3)/2}\).

Expected mechanism: Grothendieck–Lefschetz for Sym^p (and the
p·η·Sym^{p-2} correction) of the Airy sheaf on the (u,v)-plane, with the
additive twist ψ(−vb) contributing one square-root saving in v; the
required total saving over the trivial bound \(2p^{2}\cdot p^{p/2}\) is
\(p^{3/2}\). The scaling action \(x\to\lambda x\), \((u,v)\to(\lambda^{-1}u,
\lambda^{-3}v)\) reduces the family to one parameter times a torus, so
the computation can also be organized as a one-variable Katz-style
Euler-characteristic ledger. Delicate points: (i) the exact Swan/Euler
bookkeeping of Sym^p at the boundary (dims must come out O(p), constants
absolute); (ii) weight drops at the degenerate locus (v = 0 excluded;
27u³+... discriminant locus); (iii) the b=0 punctual term is *excluded*
here (b ≠ 0) and must be separated in the application (phase-plan step
4) — its normalized values oscillate and grow (table below).

For p ≡ 1 (mod 3) the same framework with the two cubic Kummer χ₃-twists
of the v-line bounds the two character coefficients — the full-crown
(line 2) version.

## 4. Exact calibration (this session's independent computation)

All values exact via the degree-two recurrence in Z[ζ_p]
(`halftheorem_probe.py`); the p ≡ 2 (mod 3) nonzero-fibre deviation is a
single constant per prime (proved support; verified exactly):

| p  | D_{b≠0}/p^{(p−3)/2} | D_0/p^{(p−3)/2} |
|----|---------------------|-----------------|
| 5  | 0                   | 0               |
| 11 | −2.0000 (extremal)  | +20.0           |
| 17 | −1.7059             | +27.3           |
| 23 | +1.0605             | −23.3           |
| 29 | +2.6823             | −75.1           |
| 41 | −1.5852             | +63.4           |
| 47 | +0.1260             | −5.8            |
| 53 | −0.9223             | +48.0           |

Sup of |D_{b≠0}|-normalized over 8 primes: **2.682**. The oscillation
profile is consistent with a trace on a rank-2 sector with
equidistributing Frobenius angles; the value −2.0000 at p=11 is exactly
extremal for a single weight-3 pair, and 2.682 > 2 shows rank ≥ 2.
**Conjecture: C = 4** (rank-2 bound). The p ≡ 1 (mod 3) by-product data
(p = 7, 13, 19: three cube-class values each) are in the probe log.

## 5. Why this is the recommended door

Every prior formulation of the crown carried an exponential-rank
obstruction (hook cohomology 2^{p−1}, Cartier determinant 2^p-term
expansions, dynatomic degree 3^p). This lemma is the first formulation in
the programme whose objects have **linear rank and linear conductor**,
whose parameter space is a fixed surface, and whose truth is calibrated
by exact data with a factor-~1.5 margin below the conjectural constant.
It is squarely within the Katz exponential-sums toolbox.

Boundary: proves line 1 (half the primes) when combined with the
committed WTCK reductions and the punctual separation; line 2 needs the
χ₃-twisted analogue; the integer conjecture is untouched by any of this.
