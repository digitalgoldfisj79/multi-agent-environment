# Primorial Ramanujan-projector collapse

Date: 28 July 2026  
Status: exact candidate projector and truncated-tail bound proved; bulk source factorisation conditional only on the already-proved primitive-coefficient asymptotic; final new-modulus frame estimate open.

## 1. Ramanujan sums

Write

\[
c_q(n)=\sum_{a\bmod q\atop(a,q)=1}e(an/q).
\]

For squarefree `q`, if `g=(q,n)`, then

\[
\boxed{
 c_q(n)=\mu(q/g)\frac{\varphi(q)}{\varphi(q/g)}.
}
\tag{1.1}
\]

In particular, for a prime `r`,

\[
c_r(n)=
\begin{cases}
r-1,&r\mid n,\\-1,&r\nmid n.
\end{cases}
\tag{1.2}
\]

## 2. Exact primorial projector

Let

\[
P=\prod_{r\le z}r
\]

be a squarefree primorial.  Define

\[
\mathcal J_P(m)
=
\sum_{q\mid P}
\frac{\mu(q)}{\varphi(q)}c_q(m).
\tag{2.1}
\]

### Theorem 2.1 (exact projector)

For every integer `m`,

\[
\boxed{
\mathcal J_P(m)
=
\frac P{\varphi(P)}\mathbf1_{(m,P)=1}.
}
\tag{2.2}
\]

### Proof

All functions in (2.1) are multiplicative in the squarefree divisor `q`, so

\[
\mathcal J_P(m)
=
\prod_{r\mid P}
\left(1-rac{c_r(m)}{r-1}\right).
\]

If `r|m`, the local factor is zero.  If `r` does not divide `m`, the local factor
is

\[
1+\frac1{r-1}=\frac r{r-1}.
\]

The product is therefore zero when `(m,P)>1`, and otherwise equals

\[
\prod_{r\mid P}\frac r{r-1}=\frac P{\varphi(P)}.
\]

This proves (2.2).  \(\square\)

## 3. Candidate-offset corollary

Let `z^+` be the next prime after `z`, and assume

\[
2\le m<H<(z^+)^2.
\]

### Corollary 3.1

One has

\[
\boxed{
\frac{\varphi(P)}P\mathcal J_P(m)
=
\mathbf1_{m\text{ prime and }m>z}.
}
\tag{3.1}
\]

### Proof

If `(m,P)=1`, every prime factor of `m` is at least `z^+`.  A composite such `m`
would be at least `(z^+)^2>H`.  Hence `m` is prime.  The converse is immediate.
\(\square\)

Thus the complete smooth Ramanujan spectrum is an exact algebraic projector onto
the candidate offsets required by the Fortune reduction.

## 4. Uniform truncation of the smooth projector

For `Q>=1`, put

\[
\mathcal J_P(m;Q)
=
\sum_{q\mid P\atop q\le Q}
\frac{\mu(q)}{\varphi(q)}c_q(m).
\]

### Theorem 4.1 (large-smooth-divisor tail)

Uniformly for `1<=m<=H` and `1<=Q<=P`,

\[
\boxed{
\left|
\mathcal J_P(m)-\mathcal J_P(m;Q)
\right|
\le
\frac{H}{Q}P^{o(1)}.
}
\tag{4.1}
\]

Here the `o(1)` is as `z->infinity`, uniformly for polynomial `H` in `z`.

### Proof

For a squarefree divisor `q|P`, put `g=(q,m)`.  Formula (1.1) gives

\[
\left|
\frac{\mu(q)}{\varphi(q)}c_q(m)
\right|
=
\frac1{\varphi(q/g)}.
\tag{4.2}
\]

Since `g<=m<=H` and `q>Q`,

\[
q/g>Q/H.
\]

The standard lower bound for Euler's totient gives

\[
\frac1{\varphi(q/g)}
\le
\frac{H}{q}(\log\log P+O(1)).
\]

Therefore

\[
\sum_{q\mid P\atop q>Q}
\left|
\frac{\mu(q)}{\varphi(q)}c_q(m)
\right|
\ll
H\log\log P
\sum_{q\mid P\atop q>Q}\frac1q.
\]

There are `tau(P)=2^{pi(z)}=P^{o(1)}` squarefree divisors, and each term in the
last sum is at most `1/Q`.  This proves (4.1).  \(\square\)

### Corollary 4.2

For every fixed `delta>0`, if

\[
Q=P^{1-\delta},
\qquad H=P^{o(1)},
\]

then

\[
\boxed{
\mathcal J_P(m;P^{1-\delta})
=
\frac P{\varphi(P)}\mathbf1_{(m,P)=1}
+P^{-1+\delta+o(1)}.
}
\tag{4.3}
\]

The error is pointwise and uniform over the physical interval.

## 5. Splitting a primitive denominator

Let `q` be squarefree.  Write uniquely

\[
q=q_0q_1,
\qquad
q_0=(q,P),
\qquad
q_0\mid P,
\qquad
(q_1,P)=1.
\tag{5.1}
\]

Then

\[
\frac{\mu(q)}{\varphi(q)}c_q(P+m)
=
\left[
\frac{\mu(q_0)}{\varphi(q_0)}c_{q_0}(m)
\right]
\left[
\frac{\mu(q_1)}{\varphi(q_1)}c_{q_1}(P+m)
\right].
\tag{5.2}
\]

The first bracket is the smooth candidate-projector coordinate.  The second
contains only primes not already in the primorial.

## 6. Bulk factorisation of the primitive source

Use the exact primitive-frequency coefficient `Gamma_Z(q)` from
`PRIMITIVE_RATIONAL_FREQUENCY_COLLAPSE_20260728.md`, with `Z=P+H`.
For fixed `delta>0`, its classical zero-free-region asymptotic is

\[
\Gamma_Z(q)
=
\frac{\mu(q)}{\varphi(q)}+\text{negligible error}
\]

uniformly for `q<=Z^{1-delta}`.

Fix a new part `q_1` satisfying

\[
(q_1,P)=1,
\qquad
q_1\le P^{1-2\delta}.
\]

The permitted smooth factors in the bulk satisfy

\[
q_0\le P^{1-\delta}/q_1.
\]

By Theorem 4.1, their omitted projector tail is bounded pointwise by

\[
\frac{Hq_1}{P^{1-\delta}}P^{o(1)}.
\tag{6.1}
\]

Hence, uniformly for the smaller range

\[
q_1\le P^{1-3\delta},
\]

this error is `P^{-2delta+o(1)}` because `H=P^{o(1)}`.

### Theorem 6.1 (bulk candidate projection)

After replacing `Gamma_Z(q)` by its proved Ramanujan asymptotic in the range
`q<=P^{1-delta}`, the sum over all smooth parts `q_0|P` factors pointwise as

\[
\boxed{
\begin{aligned}
&\sum_{q_0\mid P\atop q_0q_1\le P^{1-\delta}}
\Gamma_Z(q_0q_1)c_{q_0q_1}(P+m)\\
&\qquad=
\frac P{\varphi(P)}
\mathbf1_{m\text{ prime},\ m>z}
\frac{\mu(q_1)}{\varphi(q_1)}c_{q_1}(P+m)
+
P^{-\delta+o(1)},
\end{aligned}
}
\tag{6.2}
\]

uniformly for `2<=m<=H` and squarefree `q_1<=P^{1-3delta}` coprime to `P`.
The exponent in the displayed error has been weakened for convenience to absorb
the zero-free-region and truncation errors.

The theorem is a factorisation of the **signed primitive-frequency bulk**, not a
separate positive sieve estimate.

## 7. Consequence for the source

The complete Möbius--log source first collapses to primitive frequencies.  The
smooth component of those primitive frequencies then collapses to the exact
candidate projector.  Schematically, the bulk becomes

\[
\boxed{
\frac P{\varphi(P)}
\sum_{z<m\le H\atop m\text{ prime}}
 w_m
\sum_{q_1\le P^{1-3\delta}\atop(q_1,P)=1}
\frac{\mu(q_1)}{\varphi(q_1)}c_{q_1}(P+m),
}
\tag{7.1}
\]

plus a rigorously negligible coefficient-replacement/projector error and the top
primitive-frequency tail.

This is the corrected residual-preserving candidate source:

1. candidate primality of the offset is imposed algebraically by the complete
   smooth spectrum;
2. the remaining denominator contains only new primes;
3. the Möbius signs and Ramanujan coefficients are retained;
4. no old coefficient-free frame appears.

## 8. New theorem boundary

The remaining analytic object is the signed new-modulus Ramanujan source in
(7.1), together with the top primitive-frequency tail.  This is a prime-pair
correlation at the Cramer physical scale, but its local primorial factors and
candidate projection are now exact rather than heuristic.

A proof must establish a block second moment for (7.1) after the exact principal
term is removed, and then show that the top primitive-frequency tail does not
undo that bound.

## 9. Boundary

Proved exactly:

1. primorial Ramanujan projector (2.2);
2. candidate-offset projector (3.1);
3. pointwise truncation bound (4.1);
4. smooth/new denominator factorisation (5.2).

Proved using the earlier primitive-coefficient asymptotic:

1. bulk candidate projection (6.2).

Open:

1. the signed second moment of the new-modulus source (7.1);
2. the top primitive-frequency tail;
3. the Fortune variance theorem and Fortune's conjecture.
