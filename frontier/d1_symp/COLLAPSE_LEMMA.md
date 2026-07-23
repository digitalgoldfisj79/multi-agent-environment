# The collapse lemma: the p ≡ 2 (mod 3) half-theorem is one cubic sum

**Date:** 2026-07-23. **Status:** Lemma 1 and its corollaries are
**PROVED** (elementary, half a page) and **VERIFIED-NUMERICALLY** in
exact arithmetic (`collapse_verify.py`). Section 4 (the route to the
remaining bound) is a research plan, not a result.

## 1. Statement

Fix a prime p ≥ 5 with p ≡ 2 (mod 3), ψ = e_p, Tr = Tr_{F_{p^p}/F_p}.
For (u,v) ∈ F_p × F_p^* put S_p(u,v) = Σ_{x∈F_{p^p}} ψ(Tr(ux+vx³)),
and let D_b (b ∈ F_p) be the WTCK deviation, p²D_b = Σ_{v≠0,u}
ψ(−vb)S_p(u,v). Define

\[
T_p \;=\; \sum_{x\in\mathbb F_{p^p},\; \mathrm{Tr}(x)=0}\psi\bigl(\mathrm{Tr}(x^3)\bigr).
\]

**Lemma 1.** (i) T_p ∈ ℤ. (ii) D_b = −T_p/p for **every** b ≠ 0.
(iii) D_0 = (p−1)T_p/p = −(p−1)·D_b.

**Proof.** *Scaling.* For λ ∈ F_p^*, substituting x → λx in S_p and
using F_p-linearity of Tr gives S_p(u,v) = S_p(λu, λ³v). Since
p ≡ 2 (mod 3), gcd(3, p−1) = 1, so cubing is a bijection of F_p^*:
every (u,v) with v ≠ 0 is uniquely (λu₀, λ³) with λ = v^{1/3},
u₀ = u·v^{−1/3}, and S_p(u,v) = S_p(u₀, 1). Reindexing (u,v) ↔ (u₀,λ),

\[
p^2 D_b=\Bigl(\sum_{\lambda\ne0}\psi(-\lambda^3 b)\Bigr)
\Bigl(\sum_{u_0\in\mathbb F_p}S_p(u_0,1)\Bigr),
\qquad
\sum_{\lambda\ne0}\psi(-\lambda^3b)=\sum_{\mu\ne0}\psi(-\mu b)=
\begin{cases}-1,&b\ne0\\ p-1,&b=0.\end{cases}
\]

*u-line collapse.* Since Tr(ux) = u·Tr(x) for u ∈ F_p, orthogonality
of characters gives Σ_{u∈F_p} S_p(u,1) = Σ_x ψ(Tr x³)·Σ_u ψ(u·Tr x)
= p·T_p. Combining, p²D_b = c_b·p·T_p with c_b as displayed — (ii), (iii).

*(i).* T_p ∈ ℤ[ζ_p] is an algebraic integer. For t ∈ F_p^* the Galois
map σ_t: ζ_p → ζ_p^t sends T_p to Σ_{Tr x=0}ψ(t·Tr(x³)); substituting
x = sy with s = t^{1/3} (unique cube root) preserves {Tr = 0} and turns
t·Tr(y³) into Tr((sy)³), so σ_t(T_p) = T_p for all t. A Galois-fixed
algebraic integer in ℚ(ζ_p) is a rational integer. ∎

## 2. Corollaries (all PROVED, p ≡ 2 mod 3 throughout)

1. **Full constancy in b.** D_b is literally independent of b ≠ 0 —
   the probe's empirical finding, and WTCK.4's cube-class support law
   in this sector, drop out of (ii) with no cohomology.
2. **Punctual separation dissolved.** D_0 = −(p−1)·D_{b≠0} is an exact
   identity. Step 4 of the WTCK phase plan ("separate the b=0
   punctual term") is bookkeeping after all *in this sector* — the
   growing, oscillating D_0 values in the probe table are exactly
   −(p−1) times the constant.
3. **Reformulation of the half-theorem.** The target
   |D_b| ≤ C·p^{(p−3)/2} is equivalent to

   \[
   |T_p| \;\le\; C\,p^{(p-1)/2},
   \]

   square-root cancellation (in the hyperplane point count p^{p−1})
   with an absolute constant, for the single cubic sum T_p. Combined
   with the committed WTCK reduction, **this one inequality implies
   FF-Fortune(p,1) for all p ≡ 2 (mod 3)**.

## 3. Exact verification

`collapse_verify.py` computes Σ_u S_p(u,1) independently (only the
p pairs (u,1), same degree-2 recurrence, exact ℤ[ζ_p]) and checks it
against the full double-sum deviations:

```
p=5:  T_p = 0                       both identities, all b: OK
p=11: T_p = 322102 = 2·11^5         both identities, all b: OK
p=17: T_p = 11899821517 = 29·17^7   both identities, all b: OK
p=23: T_p = -1010446643080743       both identities, all b: OK
p=29: T_p = -798145148362709627351  p·D_b = -T_p vs committed D_b: OK
ALL COLLAPSE IDENTITIES VERIFIED EXACTLY
```

Normalized values T_p/p^{(p−1)/2} for p = 5,…,53:
0, +2.0000, +1.7059, −1.0605, −2.6823, +1.5852, −0.1260, +0.9223
(sup 2.682; conjecture |T_p| ≤ 4·p^{(p−1)/2}).

## 4. Route to the bound (research plan — nothing here is proved)

Over 𝔽̄_p, Weil restriction diagonalizes the trace form:
F_{p^p} ⊗ 𝔽̄_p ≅ 𝔽̄_p^p via x ↦ (x, x^p, …), under which Tr(x) = Σx_i,
Tr(x³) = Σx_i³, and arithmetic Frobenius acts as (p-power) ∘ (cyclic
shift σ). So T_p is the exponential sum of the **split diagonal cubic
on the hyperplane Σx_i = 0, for the form twisted by the cyclic shift**
— Fermat-motive territory, where Frobenius acts *monomially* on
Jacobi-sum classes indexed by cube-character vectors a ∈ (ℤ/3)^p.
Two structural observations make an exact evaluation plausible:

- p ≡ 2 (mod 3) means multiplication by p negates ℤ/3-characters, so a
  Frobenius-fixed class needs a_{i+1} = −a_i cyclically, forcing
  a_0 = (−1)^p a_0 = −a_0 = 0: **no fixed primitive classes** (p odd).
  Monomially-permuted non-fixed classes contribute 0 to the twisted
  trace, however many there are — the exponential-dimensional
  primitive part may vanish identically from T_p.
- The coordinate-vanishing strata of {Σx_i = 0} are permuted by σ, and
  p prime means the only σ-stable coordinate subsets are ∅ and all —
  non-stable strata also contribute 0.

If both filters survive rigorous bookkeeping (the object is Fermat ×
Artin–Schreier on a hyperplane, so the mixed Gauss-sum version of the
monomial calculus is needed; Davenport–Hasse relations control the
Gauss sums over F_{p^p}), T_p collapses to an explicitly evaluable sum
of O(1) monomials of weight ≤ (p−1)/2 — a closed form, hence the bound,
hence the half-theorem. The data profile (bounded oscillation, sup
2.68 < 4, the exactly-extremal −2 at p=11) is consistent with a trace
of ≤ 4 such monomials. **Consistency check the framework passes:** for
p ≡ 1 (mod 3), multiplication by p fixes ℤ/3-characters, and the fixed
classes are exactly the two constant vectors (a,…,a), a ∈ {1,2} —
matching the two cubic-character coefficients known to appear in that
sector. References: Weil, *Numbers of solutions of equations in finite
fields*; Katz, *Gauss Sums, Kloosterman Sums, and Monodromy*; Shioda's
Fermat-motive calculus; Davenport–Hasse.

This section is the specialist hand-off: the p ≡ 1 (mod 3) analogue
(χ₃-twists of the v-line, three cube-class values, two fixed classes)
is the same computation without the vanishing shortcut.

## 5. Honest boundary

Lemma 1 closes two of the four WTCK phase-plan steps for p ≡ 2 (mod 3)
and compresses the half-theorem into one inequality, but the
inequality itself — the crown's remaining analytic content — is open.
Function-field sibling only; integer Fortune untouched.
