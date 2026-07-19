# Primorial-centre zero-average gate

## Status

The proposed almost-all programme hoped that averaging over the primorial index would create cancellation in

\[
\mathcal Z_N(t)=\sum_{n\le N}e^{it\log P_n}.
\]

At the zeta pair-correlation scale, it does not.

## Critical-scale coherence theorem

Let \(L_n=\log P_n=\vartheta(p_n)\). For every fixed real \(c\),

\[
\boxed{
\frac1N\sum_{n\le N}\exp\left(ic\frac{L_n}{L_N}\right)
\longrightarrow
\int_0^1e^{icu}\,du.
}
\]

This follows from the prime number theorem and the nth-prime asymptotic, which give \(L_{\lfloor uN\rfloor}/L_N\to u\), followed by a Riemann-sum argument.

Thus, with \(t=c/L_N\),

\[
|\mathcal Z_N(t)|\sim N\left|\frac{e^{ic}-1}{ic}\right|
\]

unless \(c\in2\pi\mathbb Z\). The kernel is generically order \(N\), not \(N^{1/2}\), at frequency scale \(1/\log P_N\). This is the natural zeta pair-correlation spacing when the explicit-formula height satisfies \(\log T\sim\log P_N\).

## Conductor migration

For

\[
T_n=\frac{P_n}{p_{n+1}^2-2},
\]

one has the exact identity

\[
\frac{T_{n+1}}{T_n}
=
\frac{p_{n+1}(p_{n+1}^2-2)}{p_{n+2}^2-2}
\sim p_{n+1}\to\infty.
\]

Hence fixed-ratio spectral bands around \(T_n\) are eventually pairwise disjoint. The high zeros dominating index \(n\) are not reused across a long block of primorial indices.

## Finite diagnostic

Using 200 normalized consecutive zeta-zero gaps from zero indices 50 through 250, the \(N=10000\) panel gives:

- median \(|\mathcal Z_N|/N=0.18566\);
- mean \(0.24897\);
- 90th percentile \(0.55000\);
- correlation \(0.99612\) with the exact limiting sinc profile.

The median unnormalized magnitude is about \(1857\), versus \(\sqrt N=100\).

## Decision

\[
\boxed{
\text{The primorial-index average does not create the anticipated independent zero average.}
}
\]

This closes the proposed mechanism, not the possibility of an almost-all Fortune theorem. A surviving conditional route would require a bespoke sparse-centre, moving-conductor zero-correlation theorem.
