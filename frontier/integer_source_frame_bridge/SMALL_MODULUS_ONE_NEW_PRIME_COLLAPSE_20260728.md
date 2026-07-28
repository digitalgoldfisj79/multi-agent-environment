# Small-modulus one-new-prime collapse

Date: 28 July 2026  
Status: exact small-modulus decomposition proved; prime-modulus dispersion estimate open.

## 1. Classification of squarefree small moduli

Let `P_j` be the primorial centre, let `p_j` be its largest prime factor, and let
`p_j^+` be the next prime.  Assume

\[
H<(p_j^+)^2.
\]

### Theorem 1.1

If

\[
d\le H,
\qquad
\mu(d)\ne0,
\]

then exactly one of the following holds:

1. `d|P_j`;
2. there is a unique prime `q>p_j` and a unique squarefree `s|P_j` such that
   
   \[
   \boxed{d=qs.}
   \tag{1.1}
   \]

### Proof

Because `d` is squarefree, split its prime factors into those at most `p_j` and
those greater than `p_j`.  The product of the first group is a squarefree divisor
`s` of `P_j`.  If the second group contained two primes, their product would be at
least `(p_j^+)^2>H`, contradicting `d<=H`.  Hence that group is empty or consists
of one prime `q`.  Uniqueness follows from unique factorisation.  \(\square\)

## 2. Incidence coordinates

For weights `w_m` on `2<=m<=H`, put

\[
A_{j,d}(w)=\sum_{m=2}^{H}w_m\mathbf1_{d\mid P_j+m}.
\]

### Smooth columns

If `s|P_j`, then

\[
\boxed{
A_{j,s}(w)=
\sum_{2\le m\le H\atop s\mid m}w_m.
}
\tag{2.1}
\]

Thus the smooth column is independent of the residue of the centre.

### One-new-prime columns

If `d=qs` as in (1.1), write `m=st`.  Since `s|P_j`,

\[
qs\mid P_j+m
\Longleftrightarrow
q\mid P_j/s+t.
\]

Therefore

\[
\boxed{
A_{j,qs}(w)=
\sum_{2\le st\le H\atop t\equiv-P_j/s\pmod q}w_{st}.
}
\tag{2.2}
\]

The only non-primorial modulus variable is the single prime `q`.

## 3. Exact small-source decomposition

The small-modulus part of the minimal Möbius--log source is

\[
\mathcal M_{j,\le H}(w)
=-\sum_{d\le H}\mu(d)\log d\,A_{j,d}(w).
\]

### Theorem 3.1

One has exactly

\[
\boxed{
\begin{aligned}
\mathcal M_{j,\le H}(w)
={}&-
\sum_{s\mid P_j\atop s\le H}
\mu(s)\log s
\sum_{2\le m\le H\atop s\mid m}w_m\\
&+
\sum_{p_j<q\le H\atop q\ \mathrm{prime}}
\sum_{s\mid P_j\atop s\le H/q}
\mu(s)(\log q+\log s)
\sum_{2\le st\le H\atop t\equiv-P_j/s\pmod q}w_{st}.
\end{aligned}
}
\tag{3.1}
\]

### Proof

Apply Theorem 1.1 to every squarefree modulus.  In the second case

\[
\mu(qs)=-\mu(s),
\qquad
\log(qs)=\log q+\log s,
\]

and use (2.1)--(2.2).  \(\square\)

## 4. Deterministic smooth term

For the sharp weight `w_m=1`, the first line of (3.1) has the alternative exact
form

\[
\boxed{
-
\sum_{s\mid P_j\atop s\le H}
\mu(s)\log s\,\#\{m\le H:s\mid m\}
=
\sum_{m=2}^{H}\Lambda(\gcd(m,P_j)).
}
\tag{4.1}
\]

The identity follows by applying

\[
-\sum_{s\mid g}\mu(s)\log s=\Lambda(g)
\]

to `g=gcd(m,P_j)` and interchanging finite sums.

This term depends only on the offset range and the primorial cutoff.  It may be
incorporated into a refined deterministic baseline before any dispersion estimate.

## 5. Analytic consequence

The minimal source now has three—not generic—pieces:

1. an explicit smooth divisor term (4.1);
2. a polynomial range containing one prime modulus `q` and primorial divisors `s`;
3. the `d>H` one-point sparse-column range.

The centre-dependent polynomial piece has fixed arithmetic complexity.  There is
no sum over arbitrary composite moduli and no growing divisor-function order.

The next load-bearing estimate is a signed coupling of the one-new-prime term in
(3.1) with the sparse `d>H` Möbius columns.  The deterministic smooth term should
be subtracted exactly rather than bounded as an error.

## 6. Boundary

Proved:

1. the classification theorem for all squarefree `d<=H`;
2. exact incidence coordinates (2.1)--(2.2);
3. the exact source decomposition (3.1);
4. the deterministic smooth identity (4.1).

Open:

1. prime-modulus dispersion for the second line of (3.1);
2. its signed cancellation with the large-modulus sector;
3. the Fortune variance theorem and Fortune's conjecture.
