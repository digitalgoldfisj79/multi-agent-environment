# B5 — critical post-level factor incidence

Partition the least factor dyadically. For

\[
R=2^\nu\ell_j,
\]

define

\[
I_j(R)=
\sum_{R<r\le2R\atop r\text{ prime}}
\sum_{s\ge r\atop 0<rs-P_j\le H}
1_{\mathbb P}(rs-P_j)
1_{P^-(s)\ge r}.
\]

The condition `P^-(s)>=r` makes `r` the least prime factor of `rs`. Up to the final truncated dyadic band,

\[
\sum_R I_j(R)=
\sum_{r>\ell_j}M_j(r)=:C_j.
\]

Thus

\[
Z_j(H)=|\mathcal A_j|-C_j.
\]

## Two geometric regimes

### `ell_j<r<=H`

For fixed `r`, the congruence

\[
m\equiv-P_j\pmod r
\]

has at most `H/r+1` offsets in the window. Prime-offset and least-factor restrictions must remain coupled; replacing them by absolute capacities loses the required margin.

### `r>H`

For fixed `r`, there is at most one offset `m` because two such offsets would differ by a nonzero multiple of `r` smaller than `H`. Since `s>=r>H`, the same thin-strip argument gives at most one `r` for fixed `s`. This regime is a sparse matching problem on the hyperbola `rs=P_j+O(H)`.

Neither regime is accessible to the lower sieve because both begin after `sqrt H`.

## Count threshold corresponding to B1

Put

\[
\gamma_j=\left\lceil\frac{B_j}{\log P_j}\right\rceil\asymp\log X.
\]

If

\[
C_j\le|\mathcal A_j|-\gamma_j,
\]

then there are at least `gamma_j` prime outputs, and their von Mangoldt mass reaches the compressed threshold, up to a harmless endpoint adjustment.

This yields the exact remaining theorem.

> **INT-PFLI — primorial factor lower-incidence theorem.**
> \[
> \boxed{
> \sum_{j<N}
> \big(C_j-|\mathcal A_j|+\gamma_j\big)_+^2
> =o\!\left((\min_j\gamma_j)^2\right).
> }
> \]

At a failed row `C_j=|A_j|`, so its summand is `gamma_j^2`. Hence INT-PFLI excludes every sufficiently large failure and implies the compressed `INT-PSLT` criterion.

## Why no single dyadic band suffices

The number of dyadic bands between `ell_j` and `sqrt(P_j+H)` is

\[
K_j=\Theta(\log P_j)=\Theta(X).
\]

The entire required uncovered margin is only

\[
\gamma_j=\Theta(\log X).
\]

Thus the average margin per band is

\[
\gamma_j/K_j=O(\log X/X)=o(1).
\]

An `O(1)` unsigned error in each band already sums to `Theta(X)`, far larger than the total margin. Band-by-band absolute control cannot resolve one failed centre. The necessary information is a signed aggregate across all post-level bands.

## Frontier

The factor-band programme does not reduce the problem to one easy factor interval. It reduces it to INT-PFLI: a selected-centre, signed, post-level thin-hyperbola incidence theorem with total error `o(log X)` in prime-count units.
