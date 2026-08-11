# Rough-quotient hyperbola collapse

Date: 29 July 2026  
Status: **PROVED EXACTLY** as a source transformation for a general frozen lower cutoff; the signed same-band dispersion estimate is **OPEN**.

## 1. General-cutoff setup

Let

\[
P=\prod_{p\le z}p
\]

be a primorial. Let `Z` be a frozen physical cutoff satisfying

\[
z\le Z<H<(z^+)^2,
\tag{1.1}
\]

where `z^+` is the next prime after `z`. Define

\[
\mathcal C_{P,Z}(H)=\{m:Z<m\le H,\ (m,P)=1\}.
\tag{1.2}
\]

Every composite integer below `(z^+)^2` has a prime factor at most `z`, so

\[
\boxed{\mathcal C_{P,Z}(H)=\{m:Z<m\le H,\ m\text{ prime}\}.}
\tag{1.3}
\]

The distinction between `z` and `Z` is load-bearing on a mesoscopic block: `z` is the largest prime factor of the centre `P`, while `Z=z_B` is the common frozen candidate and modulus cutoff.

For `q\in\mathcal C_{P,Z}(H)` and arbitrary weights `w_m`, put

\[
A_{P,Z;q}(w)=\sum_{m\in\mathcal C_{P,Z}(H)\atop q\mid P+m}w_m.
\tag{1.4}
\]

## 2. Coprimality transport

### Lemma 2.1

Let `(q,P)=1` and write `m=qk-P`. Then

\[
\boxed{(m,P)=1\iff(k,P)=1.}
\tag{2.1}
\]

For each prime `p\mid P`, one has `m\equiv qk\pmod p`; since `p\nmid q`, divisibility by `p` is equivalent on both sides. This proves the claim. \(\square\)

## 3. Quotient bijection

Define

\[
\mathcal K_{P,Z;q}(H)=\{k\in\mathbb Z:P+Z<qk\le P+H,\ (k,P)=1\}.
\tag{3.1}
\]

### Theorem 3.1

The map

\[
m\longmapsto k=\frac{P+m}{q}
\]

is a bijection from

\[
\{m\in\mathcal C_{P,Z}(H):q\mid P+m\}
\]

onto `\mathcal K_{P,Z;q}(H)`. Consequently

\[
\boxed{A_{P,Z;q}(w)=\sum_{k\in\mathcal K_{P,Z;q}(H)}w_{qk-P}.}
\tag{3.2}
\]

The strict lower endpoint and closed upper endpoint are preserved exactly, and Lemma 2.1 transports coprimality. No prime-distribution theorem is used. \(\square\)

## 4. Frozen local centring

Put

\[
N_{P,Z}(q)=|\mathcal K_{P,Z;q}(H)|,
\qquad
M_Z=|\mathcal C_{P,Z}(H)|.
\tag{4.1}
\]

After mesoscopic weight freezing, the common candidate weight is a row scalar `\beta_P`, so the hit term is `\beta_PN_{P,Z}(q)`. The source element `m=q` is the unique zero residue modulo `q`; it is never a factor hit because `(P,q)=1`. Hence

\[
\boxed{
\widetilde\Delta_{P,Z;q}
=\beta_P\left(N_{P,Z}(q)-\frac{M_Z-1}{q-1}\right).
}
\tag{4.2}
\]

The frozen physical first-order term is

\[
\boxed{
\widetilde G_{P,Z}^{(1)}
=-\beta_P\sum_{q\in\mathcal C_{P,Z}(H)}\frac{q-1}{q-2}
\left(N_{P,Z}(q)-\frac{M_Z-1}{q-1}\right).
}
\tag{4.3}
\]

## 5. Möbius-floor and sawtooth identities

Möbius inversion gives

\[
\mathbf1_{(k,P)=1}=\sum_{d\mid P\atop d\mid k}\mu(d).
\]

### Theorem 5.1

For every `q\in\mathcal C_{P,Z}(H)`,

\[
\boxed{
N_{P,Z}(q)=\sum_{d\mid P}\mu(d)
\left(\left\lfloor\frac{P+H}{qd}\right\rfloor-
\left\lfloor\frac{P+Z}{qd}\right\rfloor\right).
}
\tag{5.1}
\]

This counts the integers `\ell` in `(P+Z)/(qd)<\ell\le(P+H)/(qd)`. \(\square\)

Let

\[
\psi(x)=x-\lfloor x\rfloor-\frac12.
\]

Using `\lfloor y\rfloor-\lfloor x\rfloor=(y-x)+\psi(x)-\psi(y)` gives

\[
\boxed{
\begin{aligned}
N_{P,Z}(q)
={}&\frac{H-Z}{q}\frac{\varphi(P)}P\\
&+\sum_{d\mid P}\mu(d)
\left[\psi\!\left(\frac{P+Z}{qd}\right)-
\psi\!\left(\frac{P+H}{qd}\right)\right].
\end{aligned}
}
\tag{5.2}
\]

The signed boundary sum is not a disposable positive error. It contains the complete correction between naive rough density and the exact candidate progression count.

## 6. Rough hyperbolic strip

### Theorem 6.1

For frozen unit weights,

\[
\boxed{
\sum_{q\in\mathcal C_{P,Z}(H)}N_{P,Z}(q)
=\sum_{\substack{Z<q\le H\\P+Z<qk\le P+H\\(qk,P)=1}}1.
}
\tag{6.1}
\]

The variable `q` is automatically prime by (1.1), and both `q` and `k` are `P`-rough. This follows by summing the quotient bijections and using `(qk,P)=1\iff(q,P)=1` and `(k,P)=1`. \(\square\)

## 7. Reciprocal phase separation

A Fourier component of either sawtooth endpoint has phase

\[
e\!\left(\frac{h(P+t)}{qd}\right),\qquad t\in\{Z,H\}.
\tag{7.1}
\]

Because `d\mid P`, writing `P=dP_d` gives

\[
\boxed{
e\!\left(\frac{h(P+t)}{qd}\right)
=e\!\left(\frac{hP_d}{q}\right)e\!\left(\frac{ht}{qd}\right).
}
\tag{7.2}
\]

The first factor carries the primorial centre; the second carries the physical endpoint.

## 8. Exact boundary

**PROVED EXACTLY**

1. general-cutoff candidate equality (1.3);
2. coprimality transport (2.1);
3. quotient bijection (3.2);
4. frozen local centring (4.2)--(4.3);
5. Möbius-floor and sawtooth identities (5.1)--(5.2);
6. rough-strip identity (6.1);
7. reciprocal phase separation (7.2).

**COMPUTATIONALLY VERIFIED**

The companion verifier checks all identities with `Z>z` on complete finite panels and exact rational arithmetic for the floor and sawtooth formulas.

**OPEN**

1. cancellation in the complete signed smooth-divisor boundary sum;
2. the uniform same-band Bessel/dispersion theorem;
3. covariance with the normalized rough coordinate and ordered Buchstab tail;
4. Fortune's conjecture.
