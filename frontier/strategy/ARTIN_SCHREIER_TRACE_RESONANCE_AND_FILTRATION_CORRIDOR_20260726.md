# Artin--Schreier trace resonance and the surviving polynomial corridor

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** polynomial/Tschirnhaus constructive route for function-field Fortune `d=1`.  
**Status:** the trace-resonance theorem and corridor below are **PROVED**. The crown remains **OPEN**.

## 1. Setup

Let

\[
M_p(Z)=Z^p-Z-1
\]

and let `alpha` be one of its roots. The conjugates of `alpha` are

\[
\alpha+i,\qquad i\in\mathbf F_p.
\]

Suppose

\[
\beta=R(\alpha),\qquad R\in\mathbf F_p[Z],\qquad \deg R<p,
\]

has degree `p` over `F_p` and minimal polynomial

\[
X^p+aX^3+cX+d,
\qquad a\ne0.
\]

Equivalently, `R` is a polynomial Artin--Schreier construction for a cubic-tail witness.

## 2. Trace filtration of the Artin--Schreier basis

For every `j>=0`,

\[
\operatorname{Tr}(\alpha^j)
=
\sum_{i\in\mathbf F_p}(\alpha+i)^j.
\]

Using

\[
\sum_{i\in\mathbf F_p}i^k
=
\begin{cases}
0,&0\le k\le p-2,\\
-1,&k=p-1,
\end{cases}
\]

one obtains

\[
\boxed{
\operatorname{Tr}(\alpha^j)=0
\quad(0\le j\le p-2),
}
\]

and

\[
\boxed{
\operatorname{Tr}(\alpha^{p-1})=-1.
}
\]

Consequently, for every polynomial `P` of degree at most `p-1`,

\[
\boxed{
\operatorname{Tr}(P(\alpha))
=-[Z^{p-1}]P(Z).
}
\]

This is the first nonzero step of the Artin--Schreier trace filtration.

## 3. Sparse minimal polynomials force low power traces to vanish

Let

\[
s_m=\operatorname{Tr}(\beta^m).
\]

Newton's identities for the monic degree-`p` polynomial

\[
X^p+aX^3+cX+d
\]

show that

\[
\boxed{s_m=0\qquad(1\le m\le p-4).}
\]

Indeed, all coefficients of `X^(p-1),...,X^4` vanish, so the first `p-4` Newton equations have zero right side and no lower coefficient contribution.

## 4. Trace-resonance obstruction

Write

\[
n=\deg R,
\qquad
R(Z)=rZ^n+\text{lower terms},
\qquad r\ne0.
\]

Assume

\[
n\mid p-1,
\qquad n\ge2,
\]

and put

\[
m=\frac{p-1}{n}.
\]

For `p>=7`,

\[
1\le m\le\frac{p-1}{2}\le p-4.
\]

The polynomial `R(Z)^m` has degree exactly `p-1` and leading coefficient `r^m`. The trace filtration therefore gives

\[
\operatorname{Tr}(\beta^m)
=
\operatorname{Tr}(R(\alpha)^m)
=-r^m\ne0.
\]

This contradicts the required Newton vanishing.

### Theorem 4.1 — divisor-degree resonance

For every prime `p>=7`, no polynomial Artin--Schreier construction for a cubic-tail degree-`p` minimal polynomial can have degree

\[
\boxed{
n\mid p-1,\qquad n\ge2.
}
\]

The obstruction is exact: the first nonzero Artin--Schreier trace level is hit by the power `m=(p-1)/n`.

## 5. Improved linear corridor

The previously proved half-degree theorem states that for

\[
p\equiv5\pmod6,\qquad p\ge17,
\]

a polynomial semiconjugacy must satisfy

\[
\deg R\ge\frac{p-1}{2}.
\]

The endpoint `(p-1)/2` divides `p-1`, so Theorem 4.1 excludes it. Therefore:

### Corollary 5.1 — strict half-degree barrier

For every prime

\[
p\equiv5\pmod6,\qquad p\ge17,
\]

any polynomial Artin--Schreier construction satisfies

\[
\boxed{
\deg R\ge\frac{p+1}{2}.
}
\]

The separately proved `p=11` endpoint calculation already gives

\[
\deg R\ge6=\frac{p+1}{2}.
\]

At the other end, the first Newton identity gives `Tr(beta)=0`. Since

\[
\operatorname{Tr}(R(\alpha))=-[Z^{p-1}]R,
\]

the unique representative of `R(alpha)` cannot have degree `p-1`. Hence

\[
\deg R\le p-2.
\]

Combining:

### Corollary 5.2 — surviving polynomial corridor

For every admitted prime `p>=11`, a polynomial construction can survive only in the corridor

\[
\boxed{
\frac{p+1}{2}\le\deg R\le p-2,
\qquad
\deg R\nmid p-1.
}
\]

Thus the remaining polynomial route occupies the dense upper half of the Artin--Schreier basis. It cannot begin at the exact half-degree resonance and cannot use any divisor degree.

## 6. Strategic consequence

This does not refute dense polynomial construction. It proves that any such proof must control a genuinely linear number of coefficients:

1. no bounded-degree polynomial template survives;
2. no polynomial below half degree survives;
3. the half-degree endpoint is killed by trace resonance;
4. all divisor degrees are killed uniformly;
5. the surviving degrees are nondivisors in `[(p+1)/2,p-2]`.

The first unresolved degree is therefore

\[
\boxed{n=(p+1)/2.}
\]

A further constructive advance must solve or obstruct the full semiconjugacy equations at that degree; it cannot arise from another low-degree ansatz.

## 7. Verification

`artin_schreier_trace_resonance_verify.py` checks, for every admitted prime below `300`:

- the inequality `(p-1)/n<=p-4` for every divisor degree `n>=2`;
- the exact coefficient trace `Tr(R(alpha)^m)=-r^m` on deterministic nonmonomial regressions;
- exclusion of the half-degree endpoint;
- the resulting corridor `[(p+1)/2,p-2]`.

The frozen output is

`artin_schreier_trace_resonance_results_20260726.json`.
