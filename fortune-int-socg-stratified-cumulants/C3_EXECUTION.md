# C3 execution — equality patterns

**Status:** `PASSED_REDUCED_TO_CORRECT_FACTORIAL_CUMULANTS`

Let

\[
K_b(t)=\log\mathbb E_b e^{tZ_J}
      =\sum_{k\ge1}c_{k,b}\frac{t^k}{k!},
\]

and define the factorial-cumulant generating function

\[
F_b(u)=\log\mathbb E_b(1+u)^{Z_J}
      =\sum_{r\ge1}f_{r,b}\frac{u^r}{r!}.
\]

The exact scalar identity

\[
K_b(t)=F_b(e^t-1)
\]

gives

\[
\boxed{
c_{k,b}=\sum_{r=1}^k S(k,r)f_{r,b},
}
\]

where `S(k,r)` is a Stirling number of the second kind.

This is not the rejected claim that factorial cumulants equal ordinary joint cumulants over globally distinct columns. Correctly,

\[
M_r=\mathbb E_b(Z_J)_r
=
\sum_{m_1,\ldots,m_r\ \mathrm{distinct}}
\mathbb E_b\prod_{i=1}^r I_{m_i}(J),
\]

and

\[
f_{k,b}
=
\sum_{\pi\in\Pi_k}
(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{C\in\pi}M_{|C|}.
\]

Products of distinct-offset factorial moments may share columns across different partition blocks; that combinatorics is retained exactly.

## Universal radius conversion

Ordered set partitions admit the coefficientwise bound

\[
r!S(k,r)\le k!\binom{k-1}{r-1}.
\]

Indeed, order the blocks, put each block internally in increasing order, concatenate to a permutation, and record the `r-1` separator positions. Hence, for every real `D>=0`,

\[
\sum_{r=1}^k S(k,r)r!D^{r-1}
\le k!(D+1)^{k-1}.
\]

Therefore

\[
|f_{r,b}|\le c_{1,b}r!D_{F,b}^{r-1}
\quad(r\ge2)
\]

implies

\[
\boxed{
|c_{k,b}|
\le c_{1,b}k!(D_{F,b}+1)^{k-1}.
}
\]

All repeated-column ordinary-cumulant patterns cost only an additive `1` in the dependence radius. They are not an independent scale obstruction.

The transform and coefficient bound are checked exactly over rational finite panels through order eight and symbolically through order twenty-four by `verify_factorial_stirling.py`.
