# Rough-quotient hyperbola collapse

Date: 28 July 2026  
Status: exact source transformation proved; signed rough-strip discrepancy estimate open.

## 1. Setup

Let

\[
P=\prod_{p\le z}p
\]

be a primorial and assume

\[
z<H<(z^+)^2,
\tag{1.1}
\]

where `z^+` is the next prime after `z`.  Define the physical candidate set

\[
\mathcal C_P(H)=\{m:z<m\le H,\ (m,P)=1\}.
\tag{1.2}
\]

By (1.1), every member of `mathcal C_P(H)` is prime.  Conversely every prime in
`(z,H]` belongs to `mathcal C_P(H)`.  Thus

\[
\mathcal C_P(H)=\{m:z<m\le H,\ m\text{ prime}\}.
\tag{1.3}
\]

For `q in mathcal C_P(H)` and arbitrary weights `w_m` on the candidate source,
put

\[
A_{P,q}(w)=
\sum_{m\in\mathcal C_P(H)\atop q\mid P+m}w_m.
\tag{1.4}
\]

This is the hit term in the exact first-order prime-modulus discrepancy.

## 2. Coprimality transport

### Lemma 2.1

Let `(q,P)=1` and let `m=qk-P`.  Then

\[
\boxed{(m,P)=1\iff(k,P)=1.}
\tag{2.1}
\]

### Proof

For every prime `p|P`, one has

\[
m=qk-P\equiv qk\pmod p.
\]

Since `p` does not divide `q`, one has `p|m` if and only if `p|k`.  Taking the
product over the prime divisors of the squarefree integer `P` proves (2.1).
\(\square\)

This elementary identity transports candidate primality of the short offset to
roughness of the complementary quotient.

## 3. Exact quotient-source identity

For `q in mathcal C_P(H)`, define

\[
\mathcal K_{P,q}(H)=
\left\{
 k\in\mathbb Z:
 P+z<qk\le P+H,\ (k,P)=1
\right\}.
\tag{3.1}
\]

### Theorem 3.1 (rough-quotient source)

The map

\[
m\longmapsto k=\frac{P+m}{q}
\]

is a bijection from

\[
\{m\in\mathcal C_P(H):q\mid P+m\}
\]

onto `mathcal K_{P,q}(H)`.  Consequently

\[
\boxed{
A_{P,q}(w)=
\sum_{k\in\mathcal K_{P,q}(H)}w_{qk-P}.
}
\tag{3.2}
\]

### Proof

If `m` is in the source set and `q|P+m`, then `k=(P+m)/q` is an integer in the
interval (3.1).  Lemma 2.1 gives `(k,P)=1`.

Conversely, if `k` is in (3.1), then `m=qk-P` satisfies `z<m<=H`.  Lemma 2.1
gives `(m,P)=1`, hence `m` is a candidate prime by (1.3), and `q|P+m`.
The two constructions are inverse.  \(\square\)

No prime-distribution theorem is used in (3.2).

## 4. Frozen-weight form

On a mesoscopic centre block the natural Euler weight may be frozen as a row
scalar `beta_P`, up to the already-proved `O(NHX)` aggregate error.  Put

\[
N_P(q)=|\mathcal K_{P,q}(H)|.
\tag{4.1}
\]

Then

\[
A_{P,q}=\beta_P N_P(q).
\tag{4.2}
\]

Let

\[
M_P=|\mathcal C_P(H)|.
\]

The source element `m=q` is the unique zero residue modulo `q` and is never a
factor hit.  Therefore the locally centred first-order discrepancy is exactly

\[
\Delta_{P,q}
=\beta_P
\left(
 N_P(q)-\frac{M_P-1}{q-1}
\right).
\tag{4.3}
\]

The complete frozen first-order term becomes

\[
\boxed{
G_P^{(1)}
=-\beta_P
\sum_{q\in\mathcal C_P(H)}
\frac{q-1}{q-2}
\left(
 N_P(q)-\frac{M_P-1}{q-1}
\right).
}
\tag{4.4}
\]

Thus the prime-progression source is exactly a weighted discrepancy for rough
quotients in short intervals of length `H/q`.

## 5. Exact Möbius-floor formula

By Möbius inversion,

\[
\mathbf1_{(k,P)=1}
=\sum_{d\mid P\atop d\mid k}\mu(d).
\]

### Theorem 5.1

For every `q in mathcal C_P(H)`,

\[
\boxed{
N_P(q)=
\sum_{d\mid P}\mu(d)
\left(
\left\lfloor\frac{P+H}{qd}\right\rfloor
-
\left\lfloor\frac{P+z}{qd}\right\rfloor
\right).
}
\tag{5.1}
\]

### Proof

Insert the Möbius identity into (4.1), write `k=d\ell`, and count the integers
`ell` in the resulting half-open interval.  \(\square\)

Let

\[
\psi(x)=x-\lfloor x\rfloor-\frac12.
\]

Since

\[
\lfloor y\rfloor-\lfloor x\rfloor
=(y-x)+\psi(x)-\psi(y),
\]

(5.1) gives the exact sawtooth decomposition

\[
\boxed{
\begin{aligned}
N_P(q)
={}&
\frac{H-z}{q}\frac{\varphi(P)}P\\
&+
\sum_{d\mid P}\mu(d)
\left[
\psi\!\left(\frac{P+z}{qd}\right)
-
\psi\!\left(\frac{P+H}{qd}\right)
\right].
\end{aligned}
}
\tag{5.2}
\]

The second line is not an error term that may be bounded positively.  At the
physical cutoff it carries coherent main-term information, just as the nonzero
primitive frequencies corrected the additive zero mode in the earlier source
analysis.

## 6. Exact rough hyperbolic strip

Summing the hit counts over all physical new primes gives a symmetric lattice
form.

### Theorem 6.1

For frozen unit weights,

\[
\boxed{
\sum_{q\in\mathcal C_P(H)}N_P(q)
=
\sum_{\substack{z<q\le H\\P+z<qk\le P+H\\(qk,P)=1}}1.
}
\tag{6.1}
\]

Both variables in the right side are primorial-rough.  Moreover `q` is
automatically prime because `q<=H<(z^+)^2`.

### Proof

The first equality is the disjoint sum of the bijections in Theorem 3.1.  Since
`P` is squarefree,

\[
(qk,P)=1\iff(q,P)=1\text{ and }(k,P)=1.
\]

The condition `(q,P)=1` in the physical range is equivalent to candidate
primality.  \(\square\)

Thus the first-order source is a signed count of two rough factors in the
microscopic hyperbolic strip

\[
P+z<qk\le P+H.
\]

## 7. Reciprocal phase form

A truncated Fourier expansion of `psi` in (5.2) produces phases

\[
e\!\left(\frac{h(P+t)}{qd}\right),
\qquad t\in\{z,H\}.
\tag{7.1}
\]

Because `d|P`, one may write `P=dP_d`, giving

\[
\boxed{
e\!\left(\frac{h(P+t)}{qd}\right)
=e\!\left(\frac{hP_d}{q}ight)
 e\!\left(\frac{ht}{qd}ight).
}
\tag{7.2}
\]

The large primorial centre has therefore been moved out of the short prime source
and into an explicit reciprocal phase indexed by one new prime `q` and one smooth
divisor `d|P`.

This is a different analytic object from the old coefficient-free frame and from
a positive sieve majorant.  All Möbius signs and local centring remain present.

## 8. Consequence for the research programme

The load-bearing first-order theorem can be restated as a block second-moment
bound for (4.4), with `N_P(q)` represented by (5.1) or (5.2).  In particular:

1. no prime or von Mangoldt weight remains inside the quotient interval;
2. the moving residue class `-P mod q` has been replaced by a rough quotient
   interval;
3. the core oscillation is a Möbius-weighted reciprocal sawtooth sum;
4. the physical scale is `|mathcal K_{P,q}|=H/q<=X`;
5. the complete smooth divisor sum is load-bearing and may not be truncated by a
   positive majorant without a new argument.

The immediate next question is whether the signed divisor sum in (5.2) admits a
mesoscopic Bessel or dispersion theorem over the primorial prefix orbit.

## 9. Boundary

Proved exactly:

1. coprimality transport (2.1);
2. source-to-quotient bijection (3.2);
3. frozen first-order identity (4.4);
4. Möbius-floor and sawtooth identities (5.1)--(5.2);
5. rough hyperbolic-strip identity (6.1);
6. reciprocal phase separation (7.2).

Not proved:

1. cancellation in the signed smooth-divisor sawtooth sum;
2. the mesoscopic second moment of (4.4);
3. coupling to the normalized rough coordinate and Buchstab tail;
4. Fortune's conjecture.
