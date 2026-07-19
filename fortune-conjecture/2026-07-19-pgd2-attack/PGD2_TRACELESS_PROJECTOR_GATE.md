# PGD2 traceless-projector gate

## Exact projector identity

Let

\[
z_{q,a}=\bigl(e(aS_u/q)\bigr)_{u\in\mathcal P_2},
\qquad x_{q,a}=M^{-1/2}z_{q,a},
\]

and

\[
A_{q,a}=x_{q,a}x_{q,a}^{*}-\frac{I_M}{M}.
\]

Then \(\operatorname{Tr}A_{q,a}=0\), and for every pair of moduli

\[
\boxed{
M^2\operatorname{Tr}(A_{q,a}A_{r,a})
=
\left|H_2\!\left(a\left(\frac1q-\frac1r\right)\right)\right|^2-M.}
\]

The identity was checked in 60 independent complex-vector systems; maximum absolute error was \(2.85\times10^{-14}\).

## Pair-coordinate split

Split unordered pairs into off-diagonal edges \(j<k\), of dimension

\[
M_\mathrm{o}=\binom N2,
\]

and loops \(j=k\), of dimension \(N\). Put

\[
O(\theta)=\sum_{j<k}e(\theta(P_j+P_k))
=\frac{F(\theta)^2-F(2\theta)}2,
\]

\[
D(\theta)=\sum_j e(2\theta P_j)=F(2\theta).
\]

Then

\[
\boxed{
|H_2(\theta)|^2-M
=
\bigl(|O(\theta)|^2-M_\mathrm{o}\bigr)
+\bigl(|D(\theta)|^2-N\bigr)
+2\Re\bigl(O(\theta)\overline{D(\theta)}\bigr).}
\]

The loop block is trivially admissible, because its complete distinct-row contribution is bounded by \(O(N^2)=O(M)\). The off-diagonal block still has dimension \(M_\mathrm{o}\asymp M\) and contains the all-distinct four-endpoint sector. It therefore has no dimensional surplus.

The mixed block has only \(O(N^3)\) endpoint triples and is below the random target scale, but no unconditional reciprocal-prime estimate was obtained for it. More importantly, separating it from the edge block discards the exact symmetric-square cancellation already identified in the endpoint-sector phase.

## Complete finite audit

The exact fixed-harmonic distinct-row decomposition was computed at
\(X=40,60,80,100,120,150\). Each component was much larger in absolute mass than its signed value. Depending on the cell, absolute/signed conditioning ratios ranged from about \(52\) to above \(10^3\), with an accidental ratio above \(7\times10^4\) when the signed edge value was extremely close to zero.

The all-row centred block energies were almost exactly matched by their deterministic row-diagonal contributions. The desired distinct-row residual is the small signed difference between them.

## Decision

\[
\boxed{\text{Traceless projector form: exact and useful notation, but no rank reduction.}}
\]

The loop sector is closed. The leading edge sector is PC-FROB2 on a pair space of the same asymptotic dimension, and edge/mixed separation is badly conditioned. Route I stops.
