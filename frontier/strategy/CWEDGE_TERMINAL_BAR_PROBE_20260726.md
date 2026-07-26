# Full `C_wedge` terminal-bar probe at the first order-`p` resonance

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** first computation on the correct rank-two braided object underlying the aggregate hook detector.  
**Status:** the definitions and virtual-to-Betti implications are exact. The `p=3,5,7` `H_1` ranks are exact over `Q(zeta_p)`; the full bar profiles at `p=3,5,7` and the `p=11` `H_1` profile are exact finite-field computations stable across three auxiliary characteristics. The `p=11` profile is not yet promoted to a characteristic-zero theorem.

## 0. Why this computation is the highest-value next probe

The corrected Sawin packaging shows that the function-field crown follows from the aggregate nonnegative Betti bound

\[
B_\Lambda=B(\pi_+)+B(\pi_-)\le p-1,
\]

where

\[
\pi_+=\bigoplus_{i\ \mathrm{even}}\bigwedge^i\mathrm{Std}_p,
\qquad
\pi_-=\bigoplus_{i\ \mathrm{odd}}\bigwedge^i\mathrm{Std}_p.
\]

The existing Pascal oscillator and scalar quantum-bar theorem control a signed virtual class. Sawin's `B_Lambda`, however, is a sum of actual cohomology dimensions. The first question is therefore not whether the scalar terminal skeleton has two lines—it does—but whether the complete rank-two hook package remains small before virtual cancellation.

Ma's braided vector space `C_wedge` is the natural object for that test because

\[
C_\wedge^{\otimes n}
\cong
\bigoplus_{k=0}^{n-1}
\left(\bigwedge^k\mathrm{Std}_n\right)^{\oplus2}.
\]

Thus it contains exactly two copies of the complete hook package.

## 1. Exact braided model

Ma defines `C_wedge` as the two-dimensional diagonal braided vector space with basis `v_0,v_1` and

\[
R(v_i\otimes v_j)=(-1)^{ij}v_j\otimes v_i.
\]

For a primitive `p`-th root `zeta`, the bar complex computing

\[
H_*(B_p,(C_\wedge)_\zeta^{\otimes p})
\]

is the reduced bar complex of the quantum shuffle algebra

\[
A\!\left((C_\wedge^*)_{-\bar\zeta}\right).
\]

Since `C_wedge` is self-dual and `bar(zeta)=zeta^{-1}`, the diagonal coefficients used by the verifier are

\[
q_{ij}=\eta(-1)^{ij},
\qquad
\eta=-\zeta^{-1}.
\]

The bar differential preserves the number `k` of `v_1` letters. Every calculation therefore splits into Hamming-weight sectors of dimension `binom(p,k)`.

## 2. Independent calibration against the scalar theorem

Replacing `C_wedge` by the one-dimensional scalar braided space at a primitive `p`-th root reproduces the committed two-line theorem exactly:

\[
\dim H_1=1,
\qquad
\dim H_2=1,
\qquad
H_r=0\ (r\ge3)
\]

at `p=3,5,7`.

This validates the shuffle convention, crossing factors and bar grading independently of `terminal_quantum_bar_verify.py`.

## 3. Full rank-two results

The tables list only nonzero Hamming-weight sectors. An entry `(a,b)` means

\[
\dim H_1=a,
\qquad
\dim H_2=b,
\]

with every higher bar-homology group zero in the finite-field computation.

### `p=3`

| weight `k` | bar homology |
|---:|---:|
| 2 | `(1,1)` |
| 3 | `(1,1)` |

Total terminal homology: `4`.

### `p=5`

| weight `k` | bar homology |
|---:|---:|
| 4 | `(1,1)` |
| 5 | `(1,1)` |

Total terminal homology: `4`.

### `p=7`

| weight `k` | bar homology |
|---:|---:|
| 2 | `(1,1)` |
| 3 | `(2,2)` |
| 4 | `(1,1)` |
| 6 | `(1,1)` |
| 7 | `(1,1)` |

Total terminal homology:

\[
\boxed{12=2(p-1).}
\]

The `H_1` multiplicities at `p=3,5,7` were independently recomputed by exact rank over the cyclotomic fields `Q(zeta_p)`, not only by finite-field reduction.

### `p=11`: first-homology reconnaissance

The full complex is substantially larger, so the first pass computes the terminal indecomposable quotient `H_1` only. The stable modular profile is

| weight `k` | `dim H_1` |
|---:|---:|
| 2 | 1 |
| 3 | 2 |
| 4 | 2 |
| 5 | 4 |
| 6 | 6 |
| 7 | 4 |
| 8 | 1 |
| 10 | 1 |
| 11 | 1 |

Hence

\[
\boxed{\dim H_1=22.}
\]

The same profile was obtained in the three auxiliary characteristics `1013`, `2003` and `3037`, each containing a primitive `22`-nd root.

This exceeds the doubled Sawin budget already in first homology:

\[
22>2(p-1)=20.
\]

Because reduction modulo an auxiliary prime can introduce extra rank loss, agreement across three primes is strong evidence but not by itself a proof that the characteristic-zero dimension is `22`. An exact cyclotomic lift or a representation-theoretic formula is the next decisive check.

## 4. Scientific interpretation

### What survives

The full rank-two terminal object is drastically smaller than the raw exponential bar complex. At `p=3,5,7`, all homology remains concentrated in two adjacent bar degrees. The scalar two-line resonance is therefore genuinely embedded in a much larger aggregate cancellation pattern.

At `p=7`, the complete `C_wedge` terminal dimension lands exactly on the doubled geometric budget `2(p-1)`. This is the first direct evidence that an aggregate bar filtration might be quantitatively relevant to Sawin's bound.

### What fails

The implication

> scalar bar homology has two lines, therefore the aggregate hook Betti sum is small

is false. The rank-two enhancement creates additional terminal sectors.

The stable `p=11` result is more serious. If it lifts to characteristic zero, the literal unquotiented `C_wedge` bar complex is already over the doubled target in `H_1` alone. It therefore cannot be the final `E_1` page of a direct spectral-sequence proof of

\[
B_\Lambda\le p-1
\]

without at least one additional mechanism:

1. a canonical quotient selecting one copy of each hook and removing more than the formal factor of two;
2. a further differential arising from the sparse Fourier section or wild Rees geometry;
3. a weight truncation showing that some terminal bar classes cannot contribute to Sawin's non-top compactly supported cohomology;
4. an arithmetic projector annihilating the excess sectors.

### What is not implied

This computation does not refute the aggregate `h=4` route. The Ma bar complex is a model on full configuration space, whereas the Fortune object is a sparse Artin--Schreier Fourier section. The required comparison may contain exactly the extra quotient or differential identified above.

It also does not bound `B_Lambda`: no Betti-compatible comparison from this bar complex to Sawin's interval variety has been constructed.

## 5. New decision gate

The next theorem should no longer be stated as a virtual Airy transport alone. It must be a **parity-separated, Betti-compatible filtered comparison**.

Let `C_+` and `C_-` denote the actual aggregate Sawin complexes after removal of the top main-term line. A sufficient mechanism is a filtration whose spectral sequence satisfies

\[
E_1\Longrightarrow H^*(C_+)\oplus H^*(C_-)
\]

and

\[
\sum_{a,b}\dim E_1^{a,b}\le p-1.
\]

Total dimension cannot increase under passage to later pages, so this would prove `B_Lambda<=p-1`.

A signed Grothendieck identity does not suffice.

For a comparison built through the doubled `C_wedge` model, the preliminary budget is

\[
\sum\dim E_1(C_\wedge)\le2(p-1),
\]

followed by a proved multiplicity-two descent. The `p=11` probe is designed precisely to test this condition.

## 6. Highest-value next step

The next action is now sharply defined:

> Determine the characteristic-zero terminal `H_1` of the order-`11` `C_wedge` twist exactly, and identify the excess two dimensions representation-theoretically. Then test whether the sparse Fourier--Cayley/Rees construction canonically kills those classes or whether they survive in the aggregate Sawin complex.

There are two decisive outcomes.

- If the modular dimension `22` drops to at most `20` over `Q(zeta_11)`, the raw aggregate bar budget remains viable and the modular loss must be explained.
- If `22` is exact, a literal bar-to-Sawin spectral sequence is impossible without an additional quotient or differential. The excess classes become the concrete target of the geometric comparison.

This is substantially narrower than attempting the full crown or another broad Betti estimate.

## 7. Verification

`cwedge_terminal_bar_probe.py`:

1. reconstructs every quantum-shuffle differential from braid crossings;
2. splits the complex by Hamming weight;
3. checks the scalar terminal theorem;
4. computes complete finite-field bar homology at `p=3,5,7` in three auxiliary characteristics;
5. computes exact `H_1` ranks over `Q(zeta_p)` at `p=3,5,7`;
6. computes the `p=11` `H_1` profile, with `--thorough` running all three auxiliary characteristics.

The default run passed in the independent working checkout.
