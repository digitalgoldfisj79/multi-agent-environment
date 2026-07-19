# D3 — factorial-walk transfer audit

## Question

Can the factorial exponential/character-sum technology of Garaev–Luca–Shparlinski and successors be transferred from
\[
n!=\prod_{m\le n}m
\]
to the prime-prefix walk
\[
P_j=P_0\prod_{m\le j}p_m,
\qquad p_m\in[X,2X)?
\]

## Core mechanism in the factorial proofs

The 2004 individual character-sum proof averages shifts \(n\mapsto n+k\) and uses
\[
\frac{(n+k)!}{n!}=\prod_{i=1}^k(n+i).
\]
After Cauchy–Schwarz, the off-diagonal terms are complete character sums of bounded-degree rational functions, so the Weil bound applies.

The 2005 additive-moment proof uses the same shift identity. Orthogonality reduces the moment to zeros of a polynomial
\[
\Phi_{k_1,\ldots,k_{2\ell}}(n)
=\sum_{\nu\le\ell}\prod_{i\le k_\nu}(n+i)
-\sum_{\nu>\ell}\prod_{i\le k_\nu}(n+i),
\]
whose degree is \(O(K)\). Polynomial root counting supplies the saving.

The 2024 improvement again works with the polynomial image sets
\[
X_j=\{(x+1)(x+2)\cdots(x+j)\},
\]
and controls their images and intersections using algebraic geometry/Lang–Weil.

## Prime-walk analogue

For the primorial walk,
\[
\frac{P_{j+k}}{P_j}=\prod_{i=1}^k p_{j+i}.
\]
This is not a bounded-degree polynomial or rational function of the index \(j\). The code audit computes its interpolation degree modulo a representative shell prime. For every tested \(X\in\{100,200,350,700,1200,2000,5000,10000\}\) and \(k\in\{1,2,3,4,6\}\), the factorial quotient has degree exactly \(k\), while the prime quotient has the maximal degree permitted by the sample length. This is diagnostic, not the logical proof of non-transfer; the logical point is that the published arguments require an explicitly available bounded-degree algebraic family, and no such family exists for consecutive-prime indices.

## Range obstruction

The headline 2004 individual estimate is
\[
|T|\ll N^{3/4}q^{1/8}(\log q)^{1/4}.
\]
In the Fortune regime
\[
q\asymp X^2,\qquad N\asymp\frac{X}{\log X},
\]
so
\[
\frac{N^{3/4}q^{1/8}(\log q)^{1/4}}{N}
\asymp(\log X)^{1/2}.
\]
It is asymptotically worse than the trivial bound. The computed ratio rises from 2.31 at \(X=100\) to 3.65 at \(X=10000\).

The average additive-character moments in the factorial papers average over every additive character modulo one fixed prime. PGD2 needs a fixed small numerator, an average over varying shell-prime denominators, exact centring, and pair-sum frequencies. Those are different averages.

## Decision

\[
\boxed{\text{Direct factorial-method transfer: STOP.}}
\]

This was a valuable missed literature line, but it does not provide a usable theorem in the critical range. A surviving research possibility would require a new algebraic lifting that replaces a block of consecutive primes by a multivariable prime tuple while preserving order and the signed detector. No published factorial theorem identified here performs that step.
