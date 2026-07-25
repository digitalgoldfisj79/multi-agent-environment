# Programme status after the actual Pascal oscillator, quantum bar, and residual-gate audit

**Date:** 2026-07-25  
**Branch:** `gpt56/airy-gaussian-independent-audit-20260725`  
**Corrected source lineage:** `55adf068773c88f81790b295165c417a627c8076` and `89467e2ceb63cd703ad545d15f12d3b10cd755d2`, merged into this branch at `c6334d34d837d89d8d993b6d41c10f8744a3ebef`.  
**Target:** function-field Fortune `d=1`, presently primes `p congruent 5 mod 6`.  
**Status:** the Airy boulder is retired as a necessary quantitative gate. The crown remains **OPEN**. The remaining quantitative problem is the original q-line count deviation, not a smaller residual theorem.

## 1. Authoritative corrections

The complete scan over `4806` primes below `10^5` rigorously disproves the proposed constant `C=4` and every constant below `4.8468292139`. It does **not** prove failure of every absolute constant or establish the Gaussian limsup law.

The corrected source also records:

1. the singular-locus lemma holds for `p>3`, not for every odd prime;
2. scalar Adams covariance refutes only the proposed total-trace cancellation mechanism;
3. `(M_p,S_p)` cannot be obtained by scalar fitting;
4. the next comparison must be object-theoretic.

These corrections supersede the first version of `AIRY_GAUSSIAN_LAW_AND_TARGET_FALSIFICATION_20260725.md`.

## 2. Exact application-side reduction

The Fourier--Cayley localization and finite-critical-point theorems prove:

1. the canonical zero-frequency term carries the full twist `p-7`;
2. the proposed half-twisted Airy class is absent there by weights;
3. any Airy transport must come from the nonzero-frequency sector;
4. the nonzero phase has no finite degree-`p` stationary point;
5. the only possible source is wild degeneration at root infinity.

Thus the broad transport problem is a formal wild-infinity problem on the modular Jordan/divided-power filtration.

## 3. Proved: the actual Pascal graph oscillator

Put

\[
m=\frac{p-7}{2}.
\]

In the intrinsic lower/upper Jordan polarization, the actual Pascal coefficient--normal map has block form

\[
D=\begin{pmatrix}A&B\\B^{-t}&0\end{pmatrix},
\]

where `B` is triangular and invertible and `B^{-1}A` is symmetric. Its canonical generating function is

\[
S_D(x,y)=x^tB^{-1}y-\frac12x^tB^{-1}Ax.
\]

For every `q=p^r`,

\[
\boxed{
\sum_{x,y}\psi_q(S_D(x,y))=q^m,
\qquad
\sum_{(x,y)\ne0}\psi_q(S_D(x,y))=q^m-1.
}
\]

Therefore the punctured actual-Pascal oscillator has exact virtual class

\[
\boxed{\mathbf Q_\ell(-m)-\mathbf Q_\ell}
\]

with multiplicity one and no quadratic Kummer or metaplectic sign.

This solves the linear oscillator normalization. It does not identify the nonlinear wild nearby-cycle complex with that oscillator.

## 4. Proved no-go: ordinary Morse linearization

After the first three multiplier/normal levels are removed, the high nonlinear phase has ordinary order at least five and zero ordinary Hessian. The Pascal generating function has nondegenerate Hessian.

Hence the nonlinear phase is not ordinarily right-equivalent to the Pascal kernel. The missing comparison must use the divided-power/Jordan filtration; ordinary formal Morse theory and classical nondegenerate stationary phase are closed.

## 5. Proved: scalar terminal quantum-bar resonance

For the one-dimensional quantum-shuffle algebra at a primitive `p`-th root:

- every total-degree bar complex below `p` is exact;
- at total degree `p`, exactly two adjacent one-dimensional homology groups survive.

The terminal virtual skeleton is

\[
\boxed{\text{Tate line}-\text{trivial line},}
\]

matching the two terms of the punctured Pascal oscillator. This is a scalar combinatorial skeleton, not yet a geometric realization inside the rank-two braided and arithmetically projected Fortune complex.

## 6. Exact ledger and measured residual

For arithmetic class `A in {+1,-1}`, put

\[
S_A=S_0+A S_\chi,
\qquad
C_A=p-2+B_A,
\qquad
d_A=\min(C_A,2p-C_A).
\]

The exact q-line ledger is

\[
\boxed{N_A=C_A-\frac{S_A}{2p}.}
\]

Consequently

\[
|S_A|<2p d_A
\quad\Longrightarrow\quad
0<N_A<2p.
\]

All quantities are committed at `p=11,17,23,29,53,71`. The verifier `residual_gate_measurement_verify.py` evaluates

\[
E_A=S_A-\epsilon_A p\rho_p,
\qquad \epsilon_A\in\{0,+1,-1\},
\]

for every class and every choice of `epsilon_A`.

The sufficient numerical inequality passes at every committed prime for every `epsilon_A`, except the marginal case `p=11`, `A=+1`, `epsilon_A=+1`, where `132` exceeds the strict Airy-subtracted threshold `131.7`. The raw tolerance usage

\[
\max_A\frac{|S_A|}{2p d_A}
\]

is respectively

\[
0.56,\ 0.33,\ 0.43,\ 0.33,\ 0.25,\ 0.10.
\]

This is useful calibration, but it does not constitute an asymptotic theorem.

## 7. The residual gate is the original main-term problem

When `B_A=0`, the ledger identity gives

\[
S_A=2p(p-2-N_A).
\]

Therefore

\[
\boxed{|S_A|<2p d_A
\iff
|N_A-(p-2)|<p-2.}
\]

Since the Airy contribution is only `O(p^{3/2})`, the condition `E_A=o(p^2)` is equivalent, at this scale, to

\[
\boxed{N_A-(p-2)=o(p)}
\]

when `B_A=0`; in general the centre is `p-2+B_A`, with the same conclusion if `B_A=o(p)`.

Thus the residual gate is **not a smaller theorem**. It is the original error-versus-main-term assertion for a count of roughly `p^2` polynomials with irreducibility probability roughly `1/p`.

The committed deviations are of square-root size: `1` through `13`, compared with `1.5 sqrt(p)=5.0` through `12.6`. This is consistent with the original `D1_ATTACK.md` picture. The Pascal and quantum-bar results identify the terminal skeleton and remove the absolute Airy estimate as a prerequisite; they do not bound the q-line deviation.

## 8. The p-adic constraint on an Airy coefficient

The Kummer bridge gives

\[
\operatorname{Tr}(F\mid\mathcal D_p)=\frac{T_p}{p^2}.
\]

Twisting by `m=(p-7)/2` gives

\[
\operatorname{Tr}(F\mid\mathcal D_p(m))
=\frac{T_p}{p^{2+m}}
=\frac{T_p}{p^{(p-3)/2}}
=p\rho_p.
\]

There is no exponent discrepancy: the two normalizations agree because

\[
2+m=\frac{p-3}{2}.
\]

Using the proved valuation `v_p(T_p)=(p+4)/3`,

\[
\boxed{
v_p(p\rho_p)
=\frac{p+4}{3}-\frac{p-3}{2}
=-\frac{p-17}{6}.
}
\]

This is verified exactly at `p=11,17,23,29,53,71`, giving valuations `1,0,-1,-2,-6,-9` respectively. In particular, `p rho_p` is not a `p`-adic integer for `p>17`.

Therefore any proposed identity

\[
S_A=\epsilon_A p\rho_p+E_A
\]

must satisfy the following dichotomy.

### Integral residual interpretation

If `E_A` is the trace of an honest untwisted integral q-line/boundary complex, then `E_A` is an algebraic integer. Since `S_A` is an integer, negative `p`-adic valuation of `p rho_p` forces

\[
\boxed{\epsilon_A=0\qquad(p>17).}
\]

Under this interpretation the Airy class appears in neither raw arithmetic projector and is irrelevant to the crown.

### Tate-normalized virtual interpretation

A nonzero `epsilon_A` is possible only if `E_A` is a Tate-normalized **virtual** trace carrying the compensating valuation

\[
\boxed{v_p(E_A)=-\frac{p-17}{6}.}
\]

This is compatible with the Fourier--Cayley normalization: the open-sector and zero-frequency pieces are individually Tate twisted, and only their total recovers the integral raw q-line trace. But the object-level comparison must state these twists explicitly. It may not identify `E_A` directly with an untwisted point-count residual.

The existing scalar data cannot choose between the two interpretations; defining the residual category and its Tate normalization is part of the missing theorem.

## 9. Revised theorem-level obstruction

The remaining transport theorem is now:

> **Projected wild Rees comparison with integrality ledger.** Construct a Frobenius-compatible Rees model of the nonzero-frequency Artin--Schreier nearby cycles at root infinity. Identify its scalar terminal quotient with the actual Pascal oscillator and its associated graded with the order-`p` quantum-bar complex. After cyclic and arithmetic projection, determine whether the Airy term occurs in the raw integral projector or only in a Tate-normalized virtual decomposition, and prove the exact valuation ledger of every complementary term.

Even a successful comparison does **not** finish the crown. One still needs one of:

1. a direct q-line/singular-series theorem proving
   \[
   N_A=p-2+B_A+o(p)
   \]
   for at least one class;
2. a weaker one-sided or congruence certificate excluding `N_+=N_-=0`;
3. a constructive irreducibility theorem bypassing q-line error control.

The first is the original main-term problem in its sharp form.

## 10. Final ruling

### Completed

- corrected Gaussian and singular-locus record;
- actual Pascal block and all-power oscillator normalization;
- ordinary Morse no-go;
- scalar order-`p` quantum-bar homology;
- exact residual measurement at all committed primes;
- proof that the absolute Airy constant is not the quantitative gate;
- exact p-adic constraint on any transported Airy coefficient.

### Open

- projected wild Rees comparison and its exact Tate/integrality ledger;
- determination of whether `epsilon_A` is zero in the raw projectors;
- a genuine bound on the q-line count deviation;
- the function-field `d=1` crown.

The programme has reached a theorem-level obstruction, but the correct obstruction is now explicit: **transport normalization plus the original q-line error-versus-main-term theorem.**