# D4 — finite-moment indistinguishability

Fix an integer `K>=0` and put `n=K+1`. Define two multisets of nonnegative integer counts:

\[
E_K=\bigsqcup_{0\le r\le n\atop r\text{ even}}
\binom nr\{r\},
\qquad
O_K=\bigsqcup_{0\le r\le n\atop r\text{ odd}}
\binom nr\{r\}.
\]

Each multiset has

\[
|E_K|=|O_K|=2^K.
\]

The even panel contains one zero count, with multiplicity `binom(n,0)=1`. The odd panel contains no zero count.

## Moment equality

For every polynomial `p` of degree at most `K`, the `(K+1)`st finite-difference identity gives

\[
\sum_{r=0}^{K+1}(-1)^r\binom{K+1}{r}p(r)=0.
\]

Separating even and odd `r` yields

\[
\sum_{z\in E_K}p(z)=\sum_{z\in O_K}p(z).
\]

Taking `p(z)=z^k` proves equality of ordinary moments through order `K`. Taking

\[
p(z)=(z)_k=z(z-1)\cdots(z-k+1)
\]

proves equality of falling-factorial moments, and therefore of binomial moments `binom(z,k)`, through the same order.

## Padding to an arbitrary block

If `N>=2^K`, append `N-2^K` copies of any fixed positive count `M>K+1` to both panels. The padded panels still have identical ordinary and factorial moments through order `K`, while exactly one panel contains a failed row.

Hence no rule depending only on the first `K` ordinary or factorial moments can exclude a zero row in every `N`-row panel whenever

\[
2^K\le N.
\]

Therefore a moment-only proof of one-defect exclusion requires

\[
\boxed{K>\log_2N.}
\]

Since `N asymp X/log X`, this is

\[
K=\Omega(\log X).
\]

## Scope of the obstruction

This theorem does not rule out a non-moment argument, a genuinely all-orders generating-function estimate, or a rowwise parity-breaking theorem. It rules out every proof whose arithmetic input is compressed to a fixed collection of moments independent of `X`.

The construction is checked exactly with integer arithmetic in `scripts/verify_moment_barrier.py`.
