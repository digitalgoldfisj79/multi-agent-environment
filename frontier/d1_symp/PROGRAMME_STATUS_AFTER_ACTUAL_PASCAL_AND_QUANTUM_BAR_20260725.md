# Programme status after the actual Pascal oscillator and terminal quantum-bar theorem

**Date:** 2026-07-25  
**Branch:** `gpt56/airy-gaussian-independent-audit-20260725`  
**Base:** `claude/airy-next-after-circularity-8jlrek` at `06b5fc04ea8bbd7d18742a999141a6f863518522`, itself based on main PR head `c331f740e06a95e5596639800c931e2629ff9178`.  
**Target:** function-field Fortune `d=1`, presently the primes `p congruent 5 mod 6`.  
**Status:** the prescribed transport programme has been run through every internal phase to a theorem-level obstruction. The crown remains **OPEN**.

## 1. Corrections inherited from the independent audit

The Gaussian computation over all `4806` primes below `10^5` is reproducible and rigorously disproves the proposed constant `C=4`. It does not prove that every absolute constant fails or establish the Gaussian limsup law.

The accompanying audit also corrected:

- the displayed global sign convention in the FFT formula;
- the singular-locus lemma, whose correct domain is `p>3`;
- the overpromotion of scalar Adams covariance to a universal cohomological no-go;
- the proposed scalar fitting of `(M_p,S_p)`, which is non-identifiable before an object-level bridge exists.

These corrections remain authoritative over the earlier numerical write-up.

## 2. Exact reduction of the application wall

The existing Fourier--Cayley localization theorem proves:

1. the canonical zero-frequency term carries the full twist `p-7`;
2. the desired half-twisted Airy constituent is absent there by weights;
3. every possible Airy transport must arise from the nonzero-frequency open sector;
4. finite stationary points are absent, so the only possible source is wild degeneration at root infinity.

Thus the broad nonzero-frequency programme reduces to one formal wild-infinity problem.

## 3. New theorem I: the actual Pascal graph oscillator is solved

Let

\[
 m=\frac{p-7}{2}.
\]

In the intrinsic lower/upper Jordan polarization, the actual high Pascal map has block form

\[
 D=\begin{pmatrix}A&B\\B^{-t}&0\end{pmatrix},
\]

where `B` is triangular and invertible and `B^{-1}A` is symmetric.

Its canonical generating function is

\[
 S_D(x,y)=x^tB^{-1}y-\frac12x^tB^{-1}Ax.
\]

For every extension `F_q/F_p`,

\[
 \boxed{
 \sum_{x,y}\psi_q(S_D(x,y))=q^m,
 \qquad
 \sum_{(x,y)\ne0}\psi_q(S_D(x,y))=q^m-1.
 }
\]

Therefore the actual Pascal punctured oscillator has exact class

\[
 \boxed{
 \mathbf Q_\ell(-m)-\mathbf Q_\ell,
 }
\]

with no quadratic Kummer sign, metaplectic ambiguity or unknown multiplicity.

This closes the linear oscillator, symplectic-conjugacy and Weil-index parts of the programme.

## 4. New no-go: ordinary Morse linearization is impossible

After the first three multiplier/normal levels are removed, the nonlinear high phase has ordinary order at least five in the joint coefficient/normal variables. Its ordinary Hessian is zero.

The actual Pascal generating function has nondegenerate Hessian. Consequently the nonlinear phase cannot be carried to the Pascal kernel by an ordinary formal or etale coordinate change.

The remaining comparison is necessarily a divided-power/Jordan statement, not an ordinary Morse or Hessian theorem.

## 5. New theorem II: the scalar order-`p` quantum bar complex has two terminal lines

For the one-dimensional quantum shuffle algebra at a primitive `p`-th root:

- every bar complex of total degree `n<p` is exact;
- at total degree `p`, precisely two adjacent one-dimensional homology groups survive.

The proof identifies compositions of `p` with cut subsets. All lower merge coefficients are invertible, while every final two-block-to-one-block Gaussian binomial vanishes because `[p]_zeta=0`.

The terminal virtual shape is therefore exactly

\[
 \boxed{
 \text{Tate line}-\text{trivial line},
 }
\]

which is the combinatorial skeleton of the punctured Pascal oscillator.

This is independently aligned with:

- the two parity lines in modular Smith localization;
- the two terminal elementary `p`-divisors in the Dwork/Hasse elimination;
- the two terms `Q_l(-m)-Q_l` in the actual Pascal oscillator.

No identification among the three has been assumed.

## 6. Current literature check

Ma's June 2026 optimal homological-vanishing theorem packages the same alternating-hook irreducibility detector into the braided vector space `C_wedge`.

Its exceptional-divisibility criterion says an order-`p` twist is completely nonresonant through degrees `2,...,p-1` and becomes potentially resonant at degree `p`, because

\[
 p\mid p(p-1).
\]

Thus the new theorem independently confirms the terminal location of the resonance. It does not supply the missing comparison because it treats multiplicative discriminant/resultant Kummer twists on the full configuration space, whereas the Fortune obstruction is an additive Artin--Schreier phase on a sparse Fourier section with wild root-infinity degeneration.

## 7. Exact post-transport ledger gate

The Kummer bridge gives

\[
 \operatorname{Tr}(F\mid\mathcal D_p)=\frac{T_p}{p^2}.
\]

Hence the correctly transported weight-two Airy constituent has trace

\[
 \boxed{
 \operatorname{Tr}(F\mid\mathcal D_p(m))
 =\frac{T_p}{p^{(p-3)/2}}
 =p\rho_p.
 }
\]

The proved elementary Airy estimate gives

\[
 |p\rho_p|\le2(p-1)\sqrt p=O(p^{3/2}),
\]

already below the `p^2` ledger scale.

For arithmetic class `A`, write

\[
 S_A=S_0+A S_\chi,
 \qquad
 C_A=p-2+B_A,
 \qquad
 d_A=\min(C_A,2p-C_A).
\]

The exact q-line formula

\[
 N_A=C_A-\frac{S_A}{2p}
\]

implies the robust certificate

\[
 |S_A|<2p d_A
 \quad\Longrightarrow\quad
 0<N_A<2p.
\]

If a successful projected transport yields

\[
 S_A=\epsilon_A p\rho_p+E_A,
 \qquad
 \epsilon_A\in\{0,\pm1\},
\]

then it is enough that

\[
 \boxed{
 |E_A|<2p d_A-2(p-1)\sqrt p.
 }
\]

In particular, `B_A=o(p)` and `E_A=o(p^2)` close the crown for all sufficiently large admitted primes using the existing Airy estimate. An absolute Airy constant is not required by this completed conditional gate.

## 8. Why the programme does not yet close the crown

The scalar oscillator and scalar quantum-bar skeleton do not control the rank-two braided `C_wedge` enhancement or the sparse arithmetic projector.

The committed q-line calculation already proves that the middle-hook block is nonzero. Its signed virtual rank is linear in `p`, so a naive termwise Deligne estimate lands at the `p^2` ledger threshold rather than strictly below it.

Neither finite boundary cells nor the raw Airy trace absorb this residual. The exact calibrated projector table disproves the simplest formula equating either q-line projector with the Airy trace plus only `q=2` and `q=infinity` corrections.

## 9. Single remaining theorem

The programme has reduced the application wall to the following statement.

> **Projected wild quantum-bar/Rees comparison theorem.** Construct a Frobenius-compatible filtered model of the nonzero-frequency Artin--Schreier Fourier--Cayley nearby cycles at root infinity whose associated graded is the order-`p` quantum bar complex and whose scalar terminal quotient is the actual Pascal graph oscillator. Prove that after cyclic trivial-minus-nontrivial and arithmetic invariant/quadratic projection:
>
> 1. the two scalar terminal lines realize `D_p(-m)-D_p` with the proved Tate gap;
> 2. every other specialization cone is canonically the q-line/discriminant/affine/`q=2`/`q=infinity` residual;
> 3. the resulting complementary arithmetic trace satisfies `E_A=o(p^2)` for at least one class `A`;
> 4. the boundary count satisfies `B_A=o(p)` or an explicit substitute sufficient for the exact ledger inequality.

This theorem is strictly narrower than the former programme:

- the linear Pascal oscillator is no longer open;
- its multiplicity and sign are no longer open;
- the analytic absolute-constant estimate is no longer the gate;
- the scalar terminal bar homology is no longer open.

What remains is the geometric realization of the scalar resonance inside the actual wild Fourier complex and cancellation of the nonscalar middle-hook residual.

## 10. Stop ruling

The programme has reached a genuine theorem-level obstruction requiring new mathematics in wild Artin--Schreier nearby cycles, quantum shuffle/bar filtrations and sparse arithmetic projection.

### Completed

- independent Gaussian audit;
- exact actual-Pascal block and oscillator theorem;
- classical Morse no-go;
- exact scalar order-`p` quantum-bar homology;
- current-literature applicability audit;
- exact conditional ledger threshold.

### Not completed

- projected wild Rees/bar comparison;
- canonical residual complex;
- `E_A=o(p^2)`;
- uniform boundary control;
- the final crown.

No further internal algebraic normalization, prime sweep, scalar covariance experiment, finite-boundary search or ordinary stationary-phase calculation can discharge the remaining theorem. The next advance must construct the stated filtered comparison or find a different certificate bypassing the middle-hook surface.