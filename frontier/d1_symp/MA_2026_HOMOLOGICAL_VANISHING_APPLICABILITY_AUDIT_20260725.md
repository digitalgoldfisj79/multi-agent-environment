# Applicability audit: Ma's 2026 optimal homological vanishing theorem

**Date:** 2026-07-25  
**Branch:** `gpt56/airy-gaussian-independent-audit-20260725`  
**External source:** Zhao Yu Ma, *Optimal homological vanishing: cancellation of character sums and Patterson's conjecture over F_q[t]*, arXiv:2606.26440v1 (24 June 2026).  
**Status:** exact comparison with the hypotheses and resonance criterion of the published preprint.  
**Ruling:** the theorem gives a useful conceptual model for the alternating-hook detector, but does not prove the sparse Fourier--Cayley transport or residual `o(p^2)` estimate. Its exceptional-divisibility criterion becomes resonant exactly at degree `n=p` for an order-`p` twist.

## 1. Direct point of contact

The paper writes the squarefree irreducibility indicator as

\[
 \mathbf 1_{\mathrm{irr}}(f)
 =\frac1n\sum_{k=0}^{n-1}(-1)^k
 \operatorname{Tr}\left(\operatorname{Frob}_f\mid\bigwedge^k\operatorname{Std}_n\right).
\]

It packages the hook representations into the two-dimensional braided vector space `C_wedge`, with

\[
 C_\wedge^{\otimes n}
 =\bigoplus_{k=0}^{n-1}
 \left(\bigwedge^k\operatorname{Std}_n\right)^{\oplus2}.
\]

This is the same alternating-hook character used in the `d=1` root-cover ledger. The paper's quantum-shuffle and bar-complex technology is therefore genuinely adjacent to the configuration-space side of the programme.

## 2. Exact resonance criterion

For a braided vector space whose braid action factors through `S_n`, Proposition 6.1(c) states that the twisted homology

\[
 H_i(B_n,V_\zeta^{\otimes n})
\]

vanishes for every `i` unless

\[
 \operatorname{ord}(\zeta)\mid n(n-1).
\]

For a primitive `p`-th root of unity:

\[
 p\nmid n(n-1)
 \qquad(2\le n\le p-1),
\]

but

\[
 p\mid p(p-1).
\]

Hence the theorem gives complete nonresonant vanishing through degree `p-1` and ceases to force vanishing at the first load-bearing degree

\[
 \boxed{n=p.}
\]

The determinantal form in Section 6.2 makes the same point: the quantum shuffle operator can become singular only when a factor

\[
 1-\zeta^{i(i-1)}
\]

vanishes. For a primitive `p`-th root and `2\le i\le p`, the unique possible terminal value is `i=p`.

This matches the repository's independent Dwork and Pascal findings: every lower elimination is nonresonant and the defect appears only at the terminal characteristic-equals-degree step.

## 3. Why the theorem does not apply directly

There are three exact mismatches.

### 3.1 Multiplicative versus additive twist

Ma's arithmetic comparison uses Kummer local systems pulled back by discriminants and resultants. Their complex analytifications are scalar braid twists.

The `d=1` Fourier--Cayley phase is instead the Artin--Schreier exponential

\[
 \mathcal L_\psi\left(\sum_m\lambda_m s_m\right),
\]

whose obstruction is wild irregularity at root infinity. It is not a discriminant Kummer character and does not become the scalar braid twist used in Proposition 6.1.

### 3.2 Full configuration space versus sparse section

The theorem controls local systems on the full configuration space `Conf_n`. The Fortune family is the codimension-`p-4` sparse coefficient section, enforced globally by Fourier integration. Pulling a vanishing theorem from `Conf_p` to this highly nongeneric section is exactly the missing Fourier--Cayley transport problem; it is not formal.

### 3.3 Uniform quantitative scale

The paper's general arithmetic application combines homological vanishing with a trivial total Betti bound exponential in `n`. In the regime `n=p` and base field size also `p`, that factor is not an `o(p^2)` bound for the two-dimensional sparse ledger. A new sparse or projected Betti theorem would still be required.

## 4. What the paper contributes to the programme

The paper supplies two useful pieces of guidance.

1. It independently confirms that the alternating-hook detector belongs naturally to a quantum-shuffle/bar-complex framework rather than the rejected ordinary deletion Koszul complex.
2. It identifies the degree-`p`, order-`p` case as the first terminal resonance of the shuffle determinant.

This suggests a refined candidate mechanism:

> construct a wild Artin--Schreier analogue of the quantum bar complex on the Fourier--Cayley formal boundary and identify its unique terminal order-`p` homology with the actual Pascal oscillator, while showing that the other bar filtration pieces map to the q-line and finite-boundary residual.

That statement is new mathematics. It is not a consequence of Ma's theorem because the additive wild phase and sparse Fourier section lie outside its comparison hypotheses.

## 5. Stop ruling

### Not a bypass

The 2026 homological-vanishing theorem does not prove:

- the divided-power Rees invariance theorem;
- the Airy transport;
- `E_A=o(p^2)`;
- the crown.

### Genuine new connection

The order-`p` shuffle resonance and the characteristic-`p` Pascal/Dwork resonance are structurally aligned. Any future proof should test whether the actual Pascal generating function is the unique terminal homology class of an additive wild quantum-bar filtration.

Until that comparison is constructed, invoking homological vanishing would merely rename the terminal defect.