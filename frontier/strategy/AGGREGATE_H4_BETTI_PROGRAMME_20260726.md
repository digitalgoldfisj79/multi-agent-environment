# Revised aggregate `h=4` Betti programme after the Sawin and `C_wedge` audits

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Target:** function-field Fortune crown at `d=1`.  
**Status:** programme update with one new exact obstruction and one completed computational probe. The crown remains open.

## 0. Authoritative target

For the full four-parameter interval

\[
\mathcal I_4=
\{T^p-T+aT^3+bT^2+cT+d:(a,b,c,d)\in\mathbf F_p^4\},
\]

let

\[
\pi_+=\bigoplus_{i\ \mathrm{even}}\bigwedge^i\mathrm{Std}_p,
\qquad
\pi_-=\bigoplus_{i\ \mathrm{odd}}\bigwedge^i\mathrm{Std}_p,
\]

and define the aggregate Sawin constant

\[
B_\Lambda=B(\pi_+)+B(\pi_-).
\]

The primary-source audit and exact weighted-count identity prove that

\[
\boxed{B_\Lambda\le p-1}
\]

is sufficient for

\[
\#\{f\in\mathcal I_4:f\text{ irreducible}\}>p-1,
\]

and hence for the `d=1` crown.

This replaces the unnecessarily strong and strategically misleading target `B=o(p)`.

## 1. The correct aggregate complexes

Let `X_p` denote Sawin's interval variety `X_{p,p-4,c}` of dimension four. Define

\[
C_+
=
\left(R\Gamma_c(X_{p,\overline{\mathbf F}_p},\mathbf Q_\ell)
\otimes\pi_+\right)^{S_p},
\]

\[
C_-
=
\left(R\Gamma_c(X_{p,\overline{\mathbf F}_p},\mathbf Q_\ell)
\otimes\pi_-\right)^{S_p}.
\]

The top cohomology line in degree eight and the trivial representation supply the main term `p^4`. Remove that line from `C_+` and call the resulting non-top complex `C_+^circ`.

Then

\[
\boxed{
B_\Lambda
=
\sum_{r=0}^{7}\dim H^r(C_+^\circ)
+
\sum_{r=0}^{7}\dim H^r(C_-).
}
\]

This is a **nonnegative total Betti dimension**. It is not an Euler characteristic and not a Frobenius trace.

## 2. New exact obstruction: virtual classes do not control `B_Lambda`

The repository's alternating-hook construction naturally forms the signed object

\[
[C_+^\circ]-[C_-]
\]

in a Grothendieck group, with an additional alternating sign from cohomological degree when traces are taken.

The Pascal oscillator theorem and scalar quantum-bar theorem identify a terminal virtual shape

\[
\mathbf Q_\ell(-m)-\mathbf Q_\ell,
\qquad
m=\frac{p-7}{2}.
\]

That is valuable, but it cannot by itself bound `B_Lambda`.

### Theorem 2.1 — virtual inflation no-go

Let `A` and `B` be Frobenius complexes and let `Q` be any Frobenius complex. Then

\[
[A\oplus Q]-[B\oplus Q]=[A]-[B]
\]

in the Grothendieck group, and for every positive integer `r`,

\[
\operatorname{Tr}(F^r\mid A\oplus Q)
-
\operatorname{Tr}(F^r\mid B\oplus Q)
=
\operatorname{Tr}(F^r\mid A)
-
\operatorname{Tr}(F^r\mid B).
\]

However,

\[
\sum_i\dim H^i(A\oplus Q)
+
\sum_i\dim H^i(B\oplus Q)
\]

is larger by

\[
2\sum_i\dim H^i(Q).
\]

Hence no identity of signed classes, even together with all Frobenius-power traces, gives an upper bound on the total Betti mass of the two unsigned sectors.

### Corollary 2.2

The existing results

- exact Pascal oscillator class;
- exact scalar terminal two-line bar class;
- Airy trace normalization;
- exact q-line projector traces;

cannot imply

\[
B_\Lambda\le p-1
\]

without a parity-separated statement controlling actual cohomology groups.

There are two independent hiding places for mass:

1. cancellation between even-hook and odd-hook sectors;
2. cancellation between even and odd cohomological degrees.

The prior programme tracked both only after signs were applied.

## 3. Betti-compatible spectral-sequence criterion

The correct replacement for a virtual transport theorem is the following.

### Proposition 3.1

Suppose `C_+^circ` and `C_-` admit finite filtrations with spectral sequences

\[
E_1(+)\Longrightarrow H^*(C_+^\circ),
\qquad
E_1(-)\Longrightarrow H^*(C_-).
\]

If

\[
\boxed{
\sum_{a,b}\dim E_1^{a,b}(+)
+
\sum_{a,b}\dim E_1^{a,b}(-)
\le p-1,
}
\]

then

\[
B_\Lambda\le p-1
\]

and the crown follows.

### Proof

Every later page is obtained as homology of the previous page. Total vector-space dimension cannot increase under taking homology. The total dimension of the abutment is therefore at most the total dimension of `E_1`. This total abutment dimension is exactly `B_Lambda`. `QED`

This criterion converts the geometric target from an abstract Betti estimate into a concrete associated-graded budget.

## 4. Relation to `C_wedge`

Ma's rank-two braided vector space satisfies

\[
C_\wedge^{\otimes p}
\cong
\bigoplus_{k=0}^{p-1}
\left(\bigwedge^k\mathrm{Std}_p\right)^{\oplus2}.
\]

It therefore contains two copies of the aggregate hook package. A comparison built through the full `C_wedge` bar complex must do two things:

1. descend canonically from multiplicity two to multiplicity one;
2. preserve the separation needed to bound `B(pi_+)+B(pi_-)`, rather than only their signed difference.

Before descent, the doubled budget corresponding to Sawin's target is

\[
\boxed{2(p-1).}
\]

The completed terminal-bar probe gives:

| `p` | computed full `C_wedge` terminal homology | doubled budget |
|---:|---:|---:|
| 3 | 4 | 4 |
| 5 | 4 | 8 |
| 7 | 12 | 12 |

At `p=11`, the stable modular first homology alone has dimension

\[
22>20=2(p-1).
\]

Thus the literal full `C_wedge` bar complex is not automatically within the required budget. If the `p=11` result lifts to characteristic zero, an additional quotient, differential or weight exclusion is mandatory.

## 5. Updated programme in dependency order

### Phase 0 — completed: freeze the exact full-interval target

- Use Sawin's aggregate even/odd hook representations.
- Use the exact target `B_Lambda<=p-1`.
- Do not require `B=o(p)`.
- Do not infer a lower bound on `B_Lambda` from a finite trace defect or the rootless-tail heuristic.

### Phase 1 — completed: expose the virtual-to-Betti gap

- Distinguish `C_+^circ` and `C_-` before hook signs.
- Distinguish every cohomological degree before Euler signs.
- Record that the Pascal and scalar bar theorems live in a signed Grothendieck class and do not bound unsigned mass.

### Phase 2 — active: determine terminal rank-two bar homology

1. Prove the `p=11` first-homology profile over `Q(zeta_11)` or find the modular rank-drop explanation.
2. Derive a representation-theoretic formula for
   \[
   H_1\left(B_p,A((C_\wedge^*)_{-\bar\zeta})\right)
   \]
   by Hamming weight.
3. Determine whether higher homology at the first resonance is always concentrated in the two terminal bar degrees.
4. Establish the asymptotic size of the complete terminal homology.

**Early stop:** if the characteristic-zero total necessarily exceeds `2(p-1)` and no canonical quotient is available, the unmodified `C_wedge` spectral-sequence route cannot prove Sawin's bound.

### Phase 3 — construct the parity-separated wild Rees comparison

Construct actual filtered complexes, not only a `K_0` identity:

\[
F^\bullet C_+^\circ,
\qquad
F^\bullet C_-.
\]

The associated graded must separately identify:

1. scalar Pascal terminal classes;
2. nonscalar `C_wedge` terminal classes;
3. sparse-section specialization cones;
4. discriminant and affine boundaries;
5. the `q=2` and `q=infinity` pieces;
6. the full-codimension zero-frequency term.

The comparison must state Frobenius weights, Tate twists, hook parity and cohomological degree for every piece.

### Phase 4 — find the missing reduction mechanism

If the raw `C_wedge` page exceeds budget, test the following in order:

1. **Multiplicity-two descent.** Identify a canonical involution or idempotent selecting one copy of each hook.
2. **Sparse-section differential.** Determine whether Fourier enforcement of `s_4=...=s_{p-4}=0` creates an additional differential killing terminal classes.
3. **Weight exclusion.** Prove that some bar classes land in the top main-term line or outside Sawin's non-top degrees `0,...,7`.
4. **Arithmetic projector.** Test whether invariant/quadratic descent annihilates excess sectors before total Betti mass is counted.

A trace cancellation after all signs have been applied is not sufficient.

### Phase 5 — close the linear budget

Calculate the total `E_1` dimension of both aggregate sectors. The target is the single inequality

\[
\sum\dim E_1(+)+\sum\dim E_1(-)\le p-1.
\]

This is the point at which Pascal/quantum-bar geometry would become an actual proof of the Sawin bound.

### Phase 6 — q-line role

Continue the fixed-class q-line only for:

- exact projector identities;
- detecting which aggregate classes survive arithmetic descent;
- congruence and parity certificates;
- validating the Tate/integrality ledger;
- testing proposed differentials against exact small-prime traces.

Do not target a generic fixed-class `B<1` estimate.

### Parallel publication track

Write the centre-preserving function-field window theorem

\[
h>\frac n2+\log_qn+O(1)
\]

separately. It is useful context but does not advance the degree-three crown and should not interrupt Phases 2–5.

## 6. Current scientific position

### Proved

1. Sawin's correct aggregate package and exact sufficient bound `B_Lambda<=p-1`.
2. The actual Pascal oscillator normalization.
3. The scalar order-`p` two-line bar theorem.
4. The virtual-to-Betti no-go above.
5. The spectral-sequence dimension criterion.
6. Exact terminal `H_1` for the rank-two `C_wedge` model at `p=3,5,7`.

### Exact computer-assisted

1. Full rank-two bar homology at `p=3,5,7` over three auxiliary finite fields.
2. Stable `p=11` first-homology profile of dimension `22` over three auxiliary fields.

### Open

1. Characteristic-zero certification of the `p=11` profile.
2. A general formula for terminal `C_wedge` homology.
3. Parity-separated wild Rees comparison.
4. A mechanism reducing the aggregate associated-graded mass to `p-1`.
5. The crown.

## 7. Highest-value next theorem

The programme now targets the following sharply falsifiable statement.

> **Terminal aggregate reduction theorem.** Determine the characteristic-zero terminal homology of the order-`p` `C_wedge` quantum-shuffle complex, construct the canonical multiplicity-one and sparse-section quotient relevant to the Sawin interval variety, and prove that its parity-separated total associated-graded dimension is at most `p-1`.

The immediate first lemma is the exact `p=11` lift. It decides whether the naïve doubled bar budget survives its first nontrivial stress test or already requires a new geometric differential.
