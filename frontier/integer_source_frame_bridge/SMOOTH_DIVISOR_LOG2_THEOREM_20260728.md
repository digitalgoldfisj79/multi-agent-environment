# Smooth-divisor log-two theorem

Date: 28 July 2026  
Status: asymptotic theorem proved from the prime number theorem; reduced positive baseline identified.

## 1. Deterministic smooth sector

Let `P_j` be squarefree primorial with largest prime factor `z=p_j`.  For the sharp
weight on `2<=m<=H`, define

\[
G_j(H)
=
\sum_{m=2}^{H}\Lambda(\gcd(m,P_j)).
\tag{1.1}
\]

By the small-modulus one-new-prime theorem, this is exactly the contribution of
all squarefree moduli `d<=H` whose prime factors already divide `P_j`.

Assume

\[
H/z\longrightarrow\infty,
\qquad
H\le(1-\delta)z^2
\tag{1.2}
\]

for some fixed `delta>0`.  These hold uniformly in the Fortune dyadic block when
`H=eta X^2`, `0<eta<1`, and `z in [X,2X)` after the harmless adjustment to the
actual next-prime square threshold.

## 2. Exact prime-power representation

Because `P_j` is squarefree, `Lambda(gcd(m,P_j))` is nonzero precisely when the
gcd is a single prime `r<=z`.  Write `m=r n`.  The condition

\[
\gcd(n,P_j/r)=1
\]

forces every prime factor of `n` to be either `r` or greater than `z`.
Since `m<=H<z^2`, the integer `n` contains at most one prime factor greater than
`z`.  Hence, uniquely,

\[
n=r^{k-1}
\quad\hbox{or}\quad
n=r^{k-1}q,
\qquad k\ge1,\ q>z\ \hbox{prime}.
\]

Therefore:

### Proposition 2.1

One has exactly

\[
\boxed{
G_j(H)
=
\sum_{r\le z\atop r\ \mathrm{prime}}
\log r
\left[
\left\lfloor\frac{\log H}{\log r}\right\rfloor
+
\sum_{k\ge1}
\bigl(\pi(H/r^k)-\pi(z)\bigr)_+
\right].
}
\tag{2.1}
\]

All sums are finite.

## 3. Main contribution

The `k=1` prime-pair term is

\[
S_1
=
\sum_{r\le H/z\atop r\ \mathrm{prime}}
\log r\,[\pi(H/r)-\pi(z)].
\tag{3.1}
\]

Uniformly for `r<=H/z`, the argument `H/r` is at least `z`.  The prime number
theorem therefore gives

\[
\pi(H/r)
=
\frac{H/r}{\log(H/r)}(1+o(1))
\]

uniformly through this range.  Partial summation with `theta(t)~t` gives

\[
\sum_{r\le H/z}
\frac{\log r}{r\log(H/r)}
=
\int_2^{H/z}\frac{dt}{t\log(H/t)}+o(1).
\]

The integral is

\[
\log\log H-\log\log z+o(1)
=
\log\frac{\log H}{\log z}+o(1).
\tag{3.2}
\]

The subtracted term satisfies

\[
\pi(z)\theta(H/z)
\ll
\frac z{\log z}\frac Hz
=
O(H/\log z)
=o(H).
\tag{3.3}
\]

Thus

\[
\boxed{
S_1
=
H\log\frac{\log H}{\log z}+o(H).
}
\tag{3.4}
\]

## 4. Remaining terms

The pure-prime-power contribution in (2.1) is bounded by

\[
\sum_{k\ge1}\theta(\min(z,H^{1/k}))
\ll z\log H=o(H).
\tag{4.1}
\]

For `k>=2`, the prime number theorem upper bound gives

\[
\begin{aligned}
&\sum_{r\le z}\log r
\sum_{k\ge2}(\pi(H/r^k)-\pi(z))_+\\
&\qquad\ll
\frac H{\log z}
\sum_{r\ \mathrm{prime}}
\sum_{k\ge2}\frac{\log r}{r^k}
\ll\frac H{\log z}
=o(H),
\end{aligned}
\tag{4.2}
\]

because the double series converges.

## 5. The theorem

### Theorem 5.1 (smooth-divisor asymptotic)

Under (1.2),

\[
\boxed{
G_j(H)
=
H\log\frac{\log H}{\log p_j}+o(H),
}
\tag{5.1}
\]

uniformly when the ratios in (1.2) are uniform.

In the Fortune block `H=eta X^2` and `p_j in [X,2X)`, so

\[
\frac{\log H}{\log p_j}=2+o(1)
\]

uniformly.  Consequently,

\[
\boxed{
G_j(H)=(\log2+o(1))H.
}
\tag{5.2}
\]

## 6. Refined exact centring

Let the full Möbius--log principal term be

\[
\mu_j^{\mathrm{mob}}=H+o(H).
\]

Subtract `G_j(H)` exactly from both the source and its baseline.  The centred
residual is unchanged, while the reduced baseline becomes

\[
\boxed{
\mu_j^{\mathrm{red}}
=
\mu_j^{\mathrm{mob}}-G_j(H)
=
(1-\log2+o(1))H.
}
\tag{6.1}
\]

Since `1-log2>0`, the reduced detector retains a uniform positive baseline.

The source left after this exact subtraction contains only:

1. the one-new-prime small-modulus term from the second line of the exact
   decomposition (3.1) in `SMALL_MODULUS_ONE_NEW_PRIME_COLLAPSE_20260728.md`;
2. the signed one-point sector `d>H`.

## 7. Consequence for Fortune

The smooth squarefree divisor sector is no longer part of the analytic variance
problem.  It is an explicitly evaluated deterministic term.  The load-bearing
estimate is now a joint signed variance theorem for one prime modulus coupled to
sparse large Möbius columns, around the positive baseline

\[
(1-\log2)H.
\]

## 8. Boundary

Proved:

1. exact representation (2.1);
2. asymptotic (5.1);
3. uniform Fortune-block constant `log 2`;
4. positive reduced baseline (6.1).

Open:

1. the joint one-new-prime/large-column variance estimate;
2. Fortune's conjecture.
