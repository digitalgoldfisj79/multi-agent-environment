# The collapse lemma: the p ≡ 2 (mod 3) half-theorem is one cubic sum

**Date:** 2026-07-23. **Status:** Lemma 1 and its numerical corollaries are
**PROVED** (elementary, half a page) and **VERIFIED COMPUTATIONALLY** in
exact arithmetic (`collapse_verify.py`). The absolute-constant estimate and
the final nearby-cycle application ledger remain **OPEN**.

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

## 2. Corollaries (PROVED numerically; categorical application still separate)

1. **Full constancy in b.** D_b is literally independent of b ≠ 0.
2. **Numerical punctual relation.** D_0 = −(p−1)D_{b≠0}. Thus D_0 is not
   an independent numerical estimate in this sector. This does **not** by
   itself prove that every punctual nearby-cycle constituent disappears;
   the original categorical ledger must still be checked.
3. **Analytic reformulation.** The target
   |D_b| ≤ C·p^{(p−3)/2} is equivalent to

\[
|T_p| \;\le\; C\,p^{(p-1)/2}.
\]

This is square-root cancellation for one cubic sum on a hyperplane of
cardinality p^{p−1}. It is the remaining analytic input for the proposed
p ≡ 2 (mod 3) half-theorem. The final implication to FF-Fortune(p,1)
remains **CONDITIONAL** until the endpoint/main/Tate/Artin–Schreier and
nearby-fibre transport is written without gaps.

## 3. Exact verification

`collapse_verify.py` computes Σ_u S_p(u,1) independently and checks it
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
(sup 2.682; working conjecture |T_p| ≤ 4·p^{(p−1)/2}).

## 4. Current route after audit

The ambient Fermat fixed-character shortcut previously sketched here is
**INVALID** for the required object. The trace-zero condition is a linear
section. Eliminating one coordinate gives

\[
\sum_{i=1}^{p-1}x_i^3-\left(\sum_{i=1}^{p-1}x_i\right)^3,
\]

which is not diagonal. Independent binary cubic-character labels describe
the ambient tensor product, not the cohomology of this `(1,3)` linear
section. See `frontier/d1_halftheorem/FAST_COLLAPSE_AND_FERMAT_AUDIT.md`.

A new exact result is proved in
`frontier/d1_symp/VIRTUAL_ADAMS_LOCAL_COLLAPSE_AND_FAILURE_CERTIFICATE.md`:
for the rank-two cubic Airy sheaf A,

\[
\Psi^p(A)=\operatorname{Sym}^p A-\det(A)\otimes\operatorname{Sym}^{p-2}A
\]

has **zero virtual Swan conductor at infinity**. On the quadratic inertia
cover, the p-th Adams operation raises the two order-p wild characters to
the p-th power and kills them exactly, leaving an actual tame rank-two
local inertia representation.

This is genuine virtual cohomological cancellation, but it is local. It
does not globalize naively: in the geometric `SL_2` representation ring,
`Psi^p(Std)=Sym^p-Sym^{p-2}` has a negative irreducible multiplicity and
is not an actual rank-two representation.

The focused exact quotient probe
`frontier/d1_symp/virtual_quotient_probe.py` reconstructs the two global
L-polynomials modulo split coefficient primes. At p=11 their common-factor
degree is at most one, so at least six residual eigenvalues remain after
all factor cancellation. Therefore the especially simple “at most four
residual eigenvalues” model is false. The absolute trace bound may still
hold through structured Frobenius phase cancellation.

## 5. Honest boundary

**PROVED:** the collapse identity, integrality, full nonzero-fibre
constancy, and local Adams Swan cancellation.

**VERIFIED COMPUTATIONALLY:** exact collapse checks and the small-prime
virtual-quotient factor probe.

**OPEN:**

\[
|T_p|\le C p^{(p-1)/2}
\]

with absolute C; a global cross-symmetric-power Frobenius-correlation
theorem; and the final categorical application ledger. Function-field
sibling only; integer Fortune untouched.
