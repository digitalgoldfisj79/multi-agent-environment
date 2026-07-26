# Uniform trace-four obstruction at the first dense Artin--Schreier endpoint

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Status:** **PROVED.** The function-field `d=1` crown remains **OPEN**.

## Theorem

Let `p >= 11`, `p = 5 mod 6`, and let `alpha` satisfy

\[
\alpha^p-\alpha=1.
\]

There is no polynomial `R` of degree

\[
n=(p+1)/2
\]

for which `beta=R(alpha)` has minimal polynomial

\[
X^p+aX^3+cX+d,
\qquad a\ne0.
\]

Equivalently, there is no degree-`(p+1)/2` polynomial Artin--Schreier semiconjugacy to a genuine cubic map.

## Proof

Normalize the leading coefficient and translate the input as in the previously proved endpoint reduction. Write

\[
R(Z)=rZ^nS(Z^{-1}),
\qquad
S(T)=1+s_3T^3+s_4T^4+\cdots+s_nT^n,
\qquad r\ne0,
\]

and put `lambda=a r^2`.

Let

\[
C_j=[T^j]S^3.
\]

The endpoint cubic-gap ledger gives

\[
C_j=0\quad(n+2\le j\le p-2),
\qquad
C_{p-1}=C_p=-1.
\]

Let `P` be the truncation of `S^3` through degree `n+1`. The exact reciprocal semiconjugacy identity is

\[
S^3+\lambda^{-1}T^{p+1}
\left((1+T)^nS\left(\frac{T}{1+T}\right)+cS+\delta T^n\right)
=P(1-T^{p-1}-T^p).
\]

Put

\[
B=C_{p+2},
\qquad C=C_{p+3}.
\]

The sparse-Wronskian coefficient at degree `p+2` gives

\[
B=-5s_3.
\]

The reciprocal identity gives

\[
B=-3s_3-\lambda^{-1}n.
\]

Since `n=1/2` in `F_p`,

\[
\lambda^{-1}=4s_3,
\]

so `s_3` is nonzero. At the next degree,

\[
C+3s_3+3s_4=-\lambda^{-1}\binom n2.
\]

Because

\[
\binom n2=-1/8,
\]

we obtain

\[
C+3s_3+3s_4=s_3/2.
\]

Now `4n=2p+2`. In the exponent range needed below, the only nonzero traces of powers of `alpha` are

\[
\operatorname{Tr}(\alpha^{p-1})
=
\operatorname{Tr}(\alpha^{2p-2})
=
\operatorname{Tr}(\alpha^{2p-1})=-1.
\]

Therefore

\[
r^{-4}\operatorname{Tr}(R(\alpha)^4)
=-[T^{p+3}]S^4-[T^4]S^4-[T^3]S^4.
\]

The low terms are `4s_4` and `4s_3`. Since `S^4=S S^3`, the cubic gap gives

\[
[T^{p+3}]S^4=C-s_3-s_4.
\]

Hence

\[
\operatorname{Tr}(R(\alpha)^4)
=-r^4(C+3s_3+3s_4)
=-r^4s_3/2\ne0.
\]

But Newton identities for `X^p+aX^3+cX+d` give

\[
\operatorname{Tr}(\beta^m)=0
\qquad(1\le m\le p-4).
\]

In particular `Tr(beta^4)=0`, a contradiction.

Thus degree `(p+1)/2` is impossible uniformly. Combining with the previous strict half-degree barrier gives

\[
\boxed{\deg R\ge(p+3)/2.}
\]

The surviving polynomial corridor is

\[
\boxed{(p+3)/2\le\deg R\le p-2,\qquad \deg R\nmid p-1.}
\]

## Verification

`artin_schreier_dense_endpoint_trace4_verify.py` checks the scalar identities for all admitted primes below `500` and evaluates the exact `p=11,17` cubic-gap candidates. Their fourth traces are respectively `6,10` and `2,12`, all nonzero. The finite calculations are regressions; the theorem is uniform.
