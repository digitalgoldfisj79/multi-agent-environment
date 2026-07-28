# Prime-offset rough-modulus collapse

Date: 28 July 2026  
Status: exact candidate-sector decomposition proved; joint prime-modulus/large-column variance estimate open.

## 1. Prime-offset source

Let `p_j` be the largest prime dividing the primorial centre `P_j`, and let
`p_j^+` be the next prime.  Choose

\[
H< (p_j^+)^2.
\]

Define the prime-offset weighted source

\[
T_j^{\mathrm{pr}}(H)
=
\sum_{p_j<p\le H\atop p\ \mathrm{prime}}
(\log p)\Lambda(P_j+p).
\tag{1.1}
\]

The omitted prime and prime-power offsets at most `p_j` belong to the deterministic
small-offset/proper-prime-power sector already separated by the corrected detector.

## 2. Roughness of every output divisor

### Lemma 2.1

If `p>p_j` is prime, then

\[
\boxed{
\gcd(P_j+p,P_j)=1.
}
\tag{2.1}
\]

Consequently every prime divisor of `P_j+p` is greater than `p_j`.

### Proof

The gcd equals `gcd(p,P_j)`.  Since `p` is a prime larger than every prime divisor
of `P_j`, the gcd is one.  If a prime `r<=p_j` divided `P_j+p`, it would divide both
`P_j` and `P_j+p`, contradicting (2.1).  \(\square\)

## 3. Small squarefree divisors are prime

The Möbius--log identity uses only squarefree divisors.

### Theorem 3.1 (rough-modulus collapse)

Let

\[
d\le H,
\qquad
\mu(d)\ne0,
\qquad
d\mid P_j+p
\]

with `p_j<p<=H` prime.  Then either `d=1` or `d` is a prime satisfying

\[
p_j<d\le H.
\]

### Proof

By Lemma 2.1, every prime factor of `d` is at least `p_j^+`.  If `d` had two
distinct prime factors, squarefreeness would give

\[
d\ge(p_j^+)^2>H,
\]

contrary to `d<=H`.  Hence `d` has at most one prime factor.  \(\square\)

The `d=1` term has coefficient `mu(1)log 1=0` and contributes nothing.

## 4. Exact small/large divisor decomposition

Apply

\[
\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d
\]

to every output in (1.1).

### Theorem 4.1

One has exactly

\[
\boxed{
T_j^{\mathrm{pr}}(H)
=
\mathcal S_j^{\mathrm{pr}}+
\mathcal L_j^{\mathrm{pr}},
}
\tag{4.1}
\]

where the small-modulus part is the prime-modulus sum

\[
\boxed{
\mathcal S_j^{\mathrm{pr}}
=
\sum_{p_j<p\le H\atop p\ \mathrm{prime}}
\log p
\sum_{p_j<q\le H\atop q\ \mathrm{prime}}
\log q\,\mathbf1_{q\mid P_j+p},
}
\tag{4.2}
\]

and the large-modulus part is

\[
\boxed{
\mathcal L_j^{\mathrm{pr}}
=-
\sum_{p_j<p\le H\atop p\ \mathrm{prime}}
\log p
\sum_{H<d\le P_j+p\atop d\mid P_j+p}
\mu(d)\log d.
}
\tag{4.3}
\]

### Proof

Split the Möbius--log divisor sum at `d=H`.  Theorem 3.1 shows that every nonzero
small-divisor term has `d=q` prime, in which case `-mu(q)log q=log q`.  The
remaining terms are exactly (4.3).  \(\square\)

## 5. Structure of the two sectors

### Small sector

Equation (4.2) involves only prime moduli in the polynomial range

\[
p_j<q\le H\asymp X^2.
\]

For fixed `q`, the inner prime offset lies in the single residue class

\[
p\equiv-P_j\pmod q.
\]

This sector is therefore accessible to prime-distribution and dispersion tools at
the physical scale `H`; no exponentially large coefficient or high-depth
convolution remains.

### Large sector

For `d>H`, a fixed pair `(j,d)` selects at most one offset

\[
p=m_j(d)=d\left\lceil\frac{P_j}{d}\right\rceil-P_j.
\]

On the candidate range, the primorial shrinking-target theorem bounds the number
of centres touched by a fixed exponential-scale `d`.  Thus (4.3) is a signed
sparse-column sum.

## 6. Exact cancellation requirement

The small sector (4.2) is nonnegative, whereas the large sector (4.3) retains the
Möbius signs.  For a composite output, their sum cancels to zero unless the output
is a prime power.  For a prime output, the top divisor `d=P_j+p` in (4.3) supplies
the surviving `log(P_j+p)` weight.

Therefore the two sectors cannot be estimated independently by positive
majorants.  The load-bearing theorem is a **joint** covariance estimate preserving
the cancellation between prime small divisors and sparse large divisors.

## 7. Consequence for method selection

The candidate-sector source now has the cleanest available architecture:

1. a polynomial prime-modulus dispersion problem;
2. an exponential sparse-column Möbius problem;
3. an exact signed coupling between them.

This removes composite small moduli entirely.  The remaining parity difficulty is
localized in the coupling to (4.3), rather than spread across a generic divisor
convolution.

## 8. Boundary

Proved:

1. every candidate output is coprime to the primorial centre;
2. every active squarefree divisor `d<=H` is prime;
3. the exact decomposition (4.1)--(4.3);
4. the prime-modulus versus sparse-large-column architecture.

Open:

1. the joint signed covariance estimate for (4.2) and (4.3);
2. the resulting all-centres variance theorem;
3. Fortune's conjecture.
