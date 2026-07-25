# Conditional ledger gate after the actual Pascal oscillator theorem

**Date:** 2026-07-25  
**Branch:** `gpt56/airy-gaussian-independent-audit-20260725`  
**Scope:** exact quantitative consequence of a successful projected wild-infinity transport.  
**Status:** the scale conversion and ledger inequalities below are **PROVED**. Their application to the crown is conditional on the still-open divided-power transport and residual decomposition.

## 1. Exact Airy scale after transport

For `p congruent 5 mod 6`, put

\[
 \rho_p=\frac{T_p}{p^{(p-1)/2}},
 \qquad
 m=\frac{p-7}{2}.
\]

The all-power Kummer bridge proves

\[
 \operatorname{Tr}(F\mid\mathcal D_p)=\frac{T_p}{p^2}.
\]

The actual Pascal oscillator theorem proves that the required transported Airy class is one punctured oscillator copy,

\[
 \mathcal D_p(-m)-\mathcal D_p,
\]

and the localization triangle converts this to the sparse weight-two constituent

\[
 \mathcal D_p(m).
\]

Its base-field Frobenius trace is therefore

\[
 \boxed{
 \operatorname{Tr}(F\mid\mathcal D_p(m))
 =p^{-m}\frac{T_p}{p^2}
 =\frac{T_p}{p^{(p-3)/2}}
 =p\rho_p.
 }
\]

Thus a single transported Airy constituent is of q-line size `p rho_p`. There is no undetermined factor `M_p` in the oscillator normalization: the linear kernel has multiplicity one and exact sum `p^m`.

This does not yet say which invariant/quadratic arithmetic projector receives the constituent, or determine the complementary trace.

## 2. Existing unconditional Airy estimate on the q-line scale

The proved elementary estimate is

\[
 |\rho_p|
 \le \frac{2(p-1)}{\sqrt p}.
\]

Consequently

\[
 \boxed{
 |p\rho_p|
 \le 2(p-1)\sqrt p.
 }
\]

The transported Airy contribution is therefore `O(p^(3/2))`, already `o(p^2)`.

The numerical Gaussian model predicts the smaller typical size

\[
 |p\rho_p|\asymp p\sqrt{\log p},
\]

but no numerical conjecture is needed for the conditional gate below.

## 3. Exact robust q-line certificate

For `A in {+1,-1}`, write

\[
 S_A=S_0+A S_\chi,
 \qquad
 C_A=p-2+B_A.
\]

The proved q-line ledger is

\[
 \boxed{
 N_A=C_A-\frac{S_A}{2p}.
 }
\]

Since `N_A` is a nonnegative integer and failure of the parity certificate requires

\[
 N_A\in2p\mathbf Z_{\ge0},
\]

it is enough to prove

\[
 0<N_A<2p.
\]

Define the two-sided margin

\[
 \boxed{
 d_A(p)=\min\{C_A,2p-C_A\}
 =\min\{p-2+B_A,p+2-B_A\}.
 }
\]

Whenever `d_A(p)>0`, the magnitude-only sufficient condition is exactly

\[
 \boxed{
 |S_A|<2p\,d_A(p).
 }
\]

Indeed this inequality gives simultaneously

\[
 C_A-\frac{|S_A|}{2p}>0
\]

and

\[
 C_A+\frac{|S_A|}{2p}<2p.
\]

## 4. Residual threshold after a successful bridge

Suppose the projected wild-infinity theorem gives a canonical decomposition

\[
 \boxed{
 S_A=\epsilon_A p\rho_p+E_A,
 \qquad
 \epsilon_A\in\{0,+1,-1\},
 }
\]

where `E_A` is the trace of the canonically defined complementary q-line and boundary complex. The coefficient set allows the Airy constituent to lie in either arithmetic projector, but excludes a multiplicity not present in the actual Pascal oscillator.

Using the unconditional Airy estimate, the parity certificate follows whenever

\[
 \boxed{
 |E_A|
 <2p\,d_A(p)-2(p-1)\sqrt p.
 }
\]

This is the exact post-transport decision gate.

### Asymptotic consequence

If for one arithmetic class

\[
 B_A=o(p)
\]

and

\[
 E_A=o(p^2),
\]

then

\[
 d_A(p)=p+o(p)
\]

and the right-hand side is

\[
 2p^2-O(p^{3/2})+o(p^2)>0.
\]

Hence the existing `2 sqrt(p)` coefficient bound closes the parity certificate for all sufficiently large `p`.

More strongly, any uniform estimate

\[
 |E_A|\le(2-\delta)p^2
\]

with fixed `delta>0`, together with `B_A=o(p)`, also suffices beyond an explicit cutoff depending only on `delta` and the boundary bound.

## 5. Calibrated scale check

The exact normalized Airy trace in the existing projector table is

\[
 \frac{T_p}{p^{(p-3)/2}}=p\rho_p,
\]

not `rho_p` itself. At the calibrated primes:

| `p` | `p rho_p` | `S_0` | `S_chi` | `B_+` | `B_-` |
|---:|---:|---:|---:|---:|---:|
| 11 | `22` | `-44` | `-66` | 0 | 6 |
| 17 | `29` | `34` | `-136` | 0 | 4 |
| 23 | `-561/23` | `322` | `92` | 0 | 6 |
| 29 | `-65419/841` | `-232` | `-290` | 0 | 2 |

The data confirms two points:

1. the transported Airy scale is much smaller than the `p^2` ledger margin;
2. neither raw projector equals the Airy trace, so the complementary complex `E_A` is genuinely load-bearing and cannot be replaced by the two finite boundary cells.

## 6. Correct dependency graph

The programme no longer needs to ask whether an unknown scalar multiplicity is `1`, `sqrt(p)` or `p`. The actual Pascal graph fixes the oscillator multiplicity and normalization.

The remaining obligations are:

1. prove projected divided-power Rees invariance, transporting the actual nonlinear wild phase to the Pascal oscillator;
2. identify which arithmetic projector contains the Airy copy;
3. define and control the complementary trace `E_A`;
4. bound the explicit boundary count `B_A`;
5. apply the boxed residual inequality.

The analytic problem reopens only if the canonical residual fails to satisfy an `o(p^2)` estimate.

## 7. Ruling

### Proved here

- the exact conversion from `T_p` to the transported q-line trace `p rho_p`;
- the unconditional `O(p^(3/2))` bound for that constituent;
- the exact two-sided ledger margin with arbitrary finite boundary `B_A`;
- the exact sufficient inequality for the canonical residual `E_A`.

### Not proved here

- the divided-power transport theorem;
- a canonical decomposition of either arithmetic projector;
- `E_A=o(p^2)`;
- a uniform boundary estimate;
- the crown.

The analytic absolute-constant target is not part of the conditional gate. The new load-bearing estimate is on the complementary projected surface trace, at the much more forgiving `o(p^2)` scale.