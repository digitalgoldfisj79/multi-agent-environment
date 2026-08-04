# B1 — explicit prime-power threshold compression

Let `P=P_j`, `U=P+H`, and suppose `H<2 sqrt(P)`. Put

\[
K=\left\lfloor\frac{\log U}{\log 2}\right\rfloor.
\]

At a failed centre the shifted von Mangoldt source is

\[
\Psi_j(H)=R_j(H)=\sum_{P<p^k\le P+H,\ k\ge2}\log p.
\]

## Lemma B1.1 — one power per exponent

For fixed `k>=2`, consecutive `k`-th powers near `P` are separated by

\[
(a+1)^k-a^k\ge k a^{k-1}\ge 2\sqrt P.
\]

Hence the interval contains at most one prime `k`-th power for each exponent `k`.

## The explicit cap

If `p^k<=U`, then `log p<=log U/k`. Therefore

\[
\boxed{
R_j(H)\le C_j:=\log U\sum_{k=2}^{K}\frac1k.
}
\]

Define

\[
B_j:=2C_j.
\]

At a failed centre, `Psi_j<=B_j/2`, so

\[
(B_j-\Psi_j)_+^2\ge B_j^2/4.
\]

Consequently the variable-threshold theorem

\[
\boxed{
\sum_{j<N}(B_j-\Psi_j(H))_+^2=o\!\left((\min_{j<N}B_j)^2\right)
}
\]

excludes every failed centre for sufficiently large `X`.

Since `log U asymp X` and `K=Theta(X)`, one has

\[
B_j\asymp X\log X.
\]

This removes one full logarithm from the deliberately loose threshold in issue #50.

## Boundary

The cap sums over all possible exponents independently. Improving it uniformly below order `X log X` would require a theorem limiting simultaneous distinct perfect powers in a window of polynomial length around an exponential centre. No such theorem is assumed here.
