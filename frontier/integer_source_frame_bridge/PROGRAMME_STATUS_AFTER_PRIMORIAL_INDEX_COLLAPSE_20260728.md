# Programme status after the primorial-index collapse

Date: 28 July 2026

## What changed

The previous programme status treated exponentially large divisor variables as a
method-level obstruction because they select at most one physical offset per
centre.

That diagnosis omitted the primorial-index recurrence

\[
P_{j+1}=\ell_jP_j.
\]

For a fixed large divisor `d`, the selected offset is the least positive residue

\[
r_j(d)\equiv-P_j\pmod d,
\]

and evolves by

\[
r_{j+1}(d)\equiv\ell_jr_j(d)\pmod d.
\]

If two selected offsets lie in the prime-candidate window `X<m<=H`, then

\[
d\le H\prod_{j\le u<k}\ell_u.
\]

Therefore visits are separated by at least

\[
\left\lceil\frac{\log(d/H)}{\log(2X)}\right\rceil
\]

primorial steps.

At exponential divisor scale, a fixed divisor can occur in only boundedly many
centres.  For a fixed-depth factorisation routed to its largest factor, the centre
multiplicity is `O(R)`, not `N asymp X/log X`.

## Stronger source collapse

The exact identity

\[
\Lambda(n)=\sum_{de=n}\mu(d)\log e
\]

has only two factors.  Grouping complementary ordered pairs by their larger factor
`D` gives

\[
\Lambda(n)=
\sum_{DE=n,\,D\ge E}
W(D,E),
\]

where

\[
W(D,E)=
\begin{cases}
\mu(D)\log E+\mu(E)\log D,&D>E,\\
\mu(D)\log D,&D=E.
\end{cases}
\]

For shifted outputs `n=P_j+m`, every routed `D` satisfies

\[
D\ge\sqrt n>H
\]

for sufficiently large `X`.  Thus a fixed `(j,D)` selects at most one physical
offset, and every `D` touches only boundedly many centres.

The shifted detector is now an exact sparse-column orbit transform:

\[
\Psi_j(H)
=
\sum_D
\mathbf1_{2\le m_j(D)\le H,\,E_j(D)\le D}
W(D,E_j(D)).
\]

No growing Heath--Brown depth is required.

## Consequence for the former obstruction

The following earlier inference is retracted:

> Fixed depth is unusable because exponentially large variables remove the long
> physical average and current fixed-complexity estimates cannot apply.

The correct statement is:

> Fixed depth produces exponentially large factors, but largest-factor routing
> turns them into sparse multiplicative-orbit columns with bounded centre
> multiplicity.

This recovers the factor

\[
N\asymp X/\log X
\]

that the centre-by-centre positive treatment lost.

## What remains

The new exact representation does not yet prove the Fortune variance estimate.
The Möbius signs in `W(D,E)` cancel all non-prime-power outputs and cannot be erased
by absolute values.

The immediate load-bearing problem is now:

\[
\sum_j
\left|
\sum_D X_{j,D}-\mu_j
\right|^2
\ll NHX L(X),
\qquad L(X)=o(\log X),
\]

for the signed sparse-column hyperbola matrix

\[
X_{j,D}
=
\mathbf1_{2\le m_j(D)\le H,\,E_j(D)\le D}
W(D,E_j(D)).
\]

The correct next phase is to derive the baseline and signed dispersion directly in
this two-factor representation.  The growing-depth Heath--Brown route, the old
unweighted frame, HTE4 and Paper IV derandomisation remain secondary.

Fortune's conjecture remains open.
