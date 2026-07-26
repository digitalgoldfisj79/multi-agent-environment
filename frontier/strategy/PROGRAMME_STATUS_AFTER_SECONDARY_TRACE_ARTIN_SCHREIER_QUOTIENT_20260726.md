# Programme status after the secondary trace and Artin–Schreier quotient

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Status:** the secondary trace has been constructed and its root-cycle quotient geometry identified. A new no-split theorem removes the identity fibre. The direct low-degree-elimination and Fano-compactification shortcuts are closed. The function-field `d=1` crown remains open.

## Current exact target

For

\[
f_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad a\in\mathbf F_p^*,
\]

let `X_a` be the ordered-root slice and

\[
Y_a=X_a/C_p.
\]

There is an explicit regular function

\[
g:Y_a\to\mathbf A^1
\]

such that `X_a -> Y_a` is the Artin–Schreier torsor

\[
T^p-T=g.
\]

For every `r!=0`, the level `g=r` has exactly one `F_p` point for each irreducible polynomial in the fixed cubic class. Hence

\[
N_a=\#\{g=1\}(\mathbf F_p),
\qquad
M_a=\sum_{g=1}c\pmod p.
\]

## Strongest new theorem

For every `p>5` and every `a!=0`, the ordered-root slice has no `F_p` points:

\[
X_a(\mathbf F_p)=\varnothing.
\]

Indeed, if `f` split completely, its distinct roots would lie among the roots of the cubic

\[
aX^3+(c+1)X+d.
\]

The logarithmic derivative identity `f'R=Pf` would then have left degree at most five and right degree at least `p`.

Consequently the split Artin–Schreier level is empty and

\[
\boxed{\#Y_a(\mathbf F_p)=(p-1)N_a.}
\]

The Hattori–Stallings quotient-defect formula therefore has no identity contribution on the actual target slice.

## What has been closed

The following continuations no longer merit work without a new ingredient:

1. constructing an ordinary divided-hook perfect complex;
2. using modular Tate groups or the coefficient Bockstein alone;
3. appealing to generic trace-surjective or Artin–Schreier structure for point existence;
4. eliminating the quotient to a uniform conic, cubic or other bounded-degree plane curve;
5. applying a standard Fano/rationally-connected point theorem to the natural sparse compactification;
6. extending the exact prime census without a structural prediction.

The low-degree probe reaches total degree `7` in `(c,d)` and degree `5` in `(c,d^2)` by `p=29`; the first relations generally contain extra `F_p` points and track the interpolation threshold.

The natural smooth projective sparse surface is a complete intersection of degrees `2,...,p-4` in `P^(p-3)`, with

\[
K=\mathcal O\left(\frac{(p-7)(p-2)}2\right).
\]

Thus every admitted `p>=11` is in the ample-canonical/general-type range, not the Fano or standard rationally connected regime. A quotient-specific compactification remains logically possible, but it requires a new ramification, regularity and boundary theorem.

## Exact remaining theorem

The route now requires one theorem and no further reformulation:

> **Sparse quotient rational-point theorem.** For every admitted prime, prove that at least one fixed-class quotient surface `Y_+` or `Y_-` has an `F_p` point.

Equivalently, prove that at least one `g=1` level is nonempty.

This must use the special sparse symmetric equations. General free `C_p` actions, trace-surjective algebras and Artin–Schreier torsors allow arbitrary invariant rings and do not imply rational points.

## Research judgement

The secondary-trace construction succeeded and produced genuine structural theorems. It did not by itself improve the probability of the final nonvanishing theorem as much as hoped: the local term is now an honest positive point count, but point existence is still the arithmetic core.

The route remains viable only through one of:

1. a quotient-specific compactification with coniveau/Witt control and a boundary point deficit;
2. an explicit sparse invariant-ring presentation giving a Chevalley–Warning/Ax–Katz mechanism;
3. a new cohomological theorem showing the quotient point count cannot vanish.

The direct natural compactification does not meet the standard automatic point-existence hypotheses. Without one of the three new ingredients above, the mathematically correct action is to stop this branch rather than take higher cyclotomic moments.
