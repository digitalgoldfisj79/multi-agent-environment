# Exact two-level prime-source identity and punctured-centre collapse

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the provisional three-small-variable Heath--Brown decomposition is unnecessary at the Fortune scale.  An exact two-level identity is available because `H < X^2`.  It resums to a source decomposition containing only one small Mobius variable, and every nonzero small Mobius variable divides every primorial centre.  The source-overlap problem is therefore removed exactly.  The full-band off-source-diagonal dispersion theorem remains **OPEN**.

## 1. Two-level identity

Put

\[
H=\eta X^2,\qquad 0<\eta<1,
\]

and choose

\[
Y=\lceil\sqrt H\rceil.
\]

For all sufficiently large `X`,

\[
H\le Y^2,\qquad Y<X.
\]

Let `mu_<=Y` denote the Mobius function restricted to integers at most `Y`.  For every `n<=H`,

\[
\boxed{
\Lambda(n)
=
2(\mu_{\le Y}*\log)(n)
-
(\mu_{\le Y}*\mu_{\le Y}*1*\log)(n).
}
\tag{1.1}
\]

This is the `k=2` Heath--Brown identity.  It follows from

\[
\mu_{\le Y}*1=\varepsilon-R_Y,
\qquad
R_Y:=\mu_{>Y}*1,
\]

because `R_Y*R_Y` has no support below `Y^2`.  Multiplying

\[
\varepsilon=2(\mu_{\le Y}*1)-(\mu_{\le Y}*1)^2
\]

by `Lambda=mu*log` gives (1.1).

## 2. Exact resummation

The same algebra gives the more useful identity

\[
\boxed{
\Lambda
=
\mu_{\le Y}*\log
+
\mu_{\le Y}*\mu_{>Y}*1*\log
\qquad (n\le H).
}
\tag{2.1}
\]

Indeed,

\[
2\mu_{\le Y}*\log
-
\mu_{\le Y}*\mu_{\le Y}*1*\log
=
\mu_{\le Y}*\log
+
\mu_{\le Y}*(\varepsilon-\mu_{\le Y}*1)*\log.
\]

Since

\[
\varepsilon-\mu_{\le Y}*1=\mu_{>Y}*1,
\]

(2.1) follows.

The original overlap configurations between two small Mobius variables have therefore been resummed exactly into the single large-Mobius term.  They must not be treated as separate Type-III errors.

## 3. Exact source ledger

The source has only two signed families.

### Family I

\[
\sum_{d\ell=n\atop d\le Y}\mu(d)\log\ell.
\tag{3.1}
\]

### Family II/III

\[
\sum_{daec=n\atop d\le Y<a}
\mu(d)\mu(a)\log c.
\tag{3.2}
\]

The variables `e,c` are unrestricted positive integers subject to the product constraint.  Dyadic subdivision may classify (3.2) as Type I, balanced Type II or Type III, but the coefficient and sign are fixed by (3.2).  No generic synthetic Type-II coefficient may replace it before the full signed sum is recorded.

## 4. Punctured-centre collapse

If `mu(d) != 0` and `d<=Y<X`, then `d` is squarefree and every prime factor of `d` is below `X`.  Hence for every primorial centre in the block,

\[
\boxed{d\mid P_j.}
\tag{4.1}
\]

For every first-band prime `p>X`,

\[
\boxed{
dP_j^{-1}\equiv(P_j/d)^{-1}\pmod p.
}
\tag{4.2}
\]

Equivalently,

\[
\boxed{
p\mid P_j+dm
\iff
p\mid P_j/d+m.
}
\tag{4.3}
\]

Thus the small Mobius variable is not an arbitrary inverse-orbit coefficient.  It punctures the primorial centre exactly.

Under the reduced identity (2.1), there is only one such small variable.  The repeated-prime residual which appeared in the provisional two-small-variable expansion disappears.

## 5. Prime indicator and prime powers

For `n>=2`,

\[
\frac{\Lambda(n)}{\log n}
=
\begin{cases}
1,&n\text{ prime},\\
1/a,&n=q^a,\ a\ge2,\\
0,&\text{otherwise}.
\end{cases}
\]

Therefore the exact prime source is recovered from (2.1) after subtracting the explicit prime-power correction.  Its support has cardinality `O(sqrt H)` and its contribution is polynomially below the Fortune block budget after the frozen coefficient is restored.  It is retained in the verifier and may not be silently discarded.

## 6. Consequence for the full-band programme

Gate A passes in a stronger form than planned:

1. `Lambda` is reconstructed exactly on the full source range;
2. only one small Mobius variable remains;
3. that variable divides every centre and converts `P_j` to `P_j/d` exactly;
4. the overlap ledger is closed by algebra rather than an estimate;
5. the remaining hard source is the large-Mobius multilinear family (3.2), coherently recombined with (3.1).

The next exact object is therefore the punctured-centre full-band amplitude

\[
\sum_{d\le Y}\mu(d)
\sum_m c_d(m)
\,g_R\!\left(-m(P_j/d)^{-1}\right),
\tag{6.1}
\]

with the actual signed coefficient `c_d` supplied by (3.1)--(3.2).

## 7. Verification

The committed verifier checks in exact integer log-signatures:

1. (1.1) for every `n<=H`;
2. the reduced identity (2.1) for every `n<=H`;
3. `Y<X` and `H<=Y^2`;
4. divisibility `d|P_j` for every nonzero small Mobius variable;
5. the punctured-centre congruence (4.2);
6. the complete prime-power correction support.

Panels: `X=11,17,23,29,37`.

## 8. Boundary

**PROVED EXACTLY**

- two-level Heath--Brown identity;
- reduced one-small-variable identity;
- exact source-family ledger;
- small-Mobius divisibility into every centre;
- punctured-centre transport;
- exact prime-power correction.

**CLOSED**

- the provisional three-small-variable decomposition;
- separate estimation of overlap classes between small Mobius variables;
- treating the small Mobius inverse as an arbitrary coefficient.

**OPEN**

- full-band punctured-centre off-source-diagonal dispersion;
- the large-Mobius multilinear contraction;
- high-conductor deterministic sampling after source-diagonal removal;
- `FBPOTD(X)`, `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.
