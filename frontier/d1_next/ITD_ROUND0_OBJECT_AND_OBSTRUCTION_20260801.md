# ITD Round 0 — exact object and surviving theorem

**Date:** 1 August 2026  
**Gate:** `ITD-0`  
**Result:** **ACTIVATED / NEW INTEGRAL COMPARISON REQUIRED**

## 1. Exact integral object

Let `O` be a complete discrete valuation ring carrying the required additive
character and Frobenius structure. The candidate integral carrier is

\[
\mathscr M_p
=R\Gamma_c\left(\mathbf A^1,
\mathscr A_O^{\otimes p}\right)^{\mu_3},
\]

with cyclic permutation action by `C_p` and Frobenius.

Its characteristic-zero cyclic trivial-minus-nontrivial trace realizes the
adjacent Airy Adams virtual class

\[
R_p=U_p-U_{p-2}(-1),
\]

after Chuang's one explicit Tate-line correction at `k=p`.

After reduction to characteristic `p` and Tate/Smith localization, the cyclic
tensor diagonal gives the Frobenius twist of the original rank-two Airy
object. Equivalently, the modular exact sequence is

\[
0\to E^{(1)}\to\operatorname{Sym}^pE
\to\det(E)\otimes\operatorname{Sym}^{p-2}E\to0.
\]

These two endpoints are proved. The missing datum is an integral
Frobenius-compatible comparison between them.

## 2. Exact obstruction to the natural lift

The natural Dwork/connection lift does not have bounded cone. After the
`mu_3` projector its surviving defect has rank `(p-5)/6`, and the endpoint
residue support grows linearly. Abstract modular Smith localization cannot
bound the characteristic-zero trace: pure free cyclic lattices can be Smith
invisible while contributing one full Weil-scale eigenvalue per free copy.

Thus the implication

\[
\text{rank-two modular contraction}
\Longrightarrow
|\operatorname{Tr}(F|R_p)|=O(p^{(p+1)/2})
\]

is false without additional Airy-specific structure.

## 3. The exact theorem now required

One of the following would pass `ITD-0/1`:

1. construct a different perfect `C_p`-equivariant integral Airy complex and
   Frobenius-compatible comparison whose generic cone, after the known Tate
   correction, has uniformly bounded total rank;
2. construct a filtered/Rees comparison whose cone may have rank `O(p)` but
   whose total Frobenius trace is bounded by
   `C p^((p+1)/2)` with absolute `C`;
3. prove an exact cancellation theorem for the free cyclic part
   \[
   \delta_\Phi(K_{free})
   =\operatorname{Tr}(\Phi|K_{free}^{C_p})
   -\operatorname{Tr}(\Phi|(K_{free})_\xi).
   \]

A comparison only modulo the maximal ideal, only in the two-periodic Tate
quotient, or only on the associated graded does not pass.

## 4. Relation to the virtual Rees lane

The wild divided-power Rees theorem left open by `ABT-1` and the integral
Tate-diagonal theorem are two views of the same characteristic-boundary
problem:

- the application view asks for a Frobenius-compatible specialization of the
  nonzero-frequency root-infinity phase to the Pascal oscillator, including
  its q-line correction cones;
- the analytic view asks for an integral lift of modular cyclic contraction
  with controlled generic Frobenius defect.

Neither existing result constructs the needed comparison. The order-`p`
quantum-bar theorem and Ma's homological-vanishing framework identify the
terminal resonance but do not cover the additive wild sparse Rees family.

## 5. Stop ruling

The programme has reached a genuine theorem boundary:

- no missing coefficient dictionary remains;
- no further scalar fit or prime scan can define the comparison;
- the natural bounded-cone construction is already false;
- existing modular, Smith, ordinary Morse and generic short-trace theorems do
  not imply the required integral Weil statement.

The next admissible work must propose an explicit integral/Rees comparison or
an Airy-specific cancellation identity. Computation may test such a proposed
identity, but is not a substitute for it.
