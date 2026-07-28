# Exact smooth-primitive centring

Date: 28 July 2026  
Status: exact principal subtraction proved; its candidate-projector asymptotic proved from the classical zeta zero-free region, Mertens' theorem and elementary divisor-tail bounds; new-modulus variance estimate open.

## 1. Exact primitive-frequency source

Let

\[
P=\prod_{r\le z}r,
\qquad
Z=P+H,
\]

and let `w_m` be deterministic complex weights supported on `2<=m<=H`.  Put

\[
W_H=\sum_mw_m,
\qquad
\widehat w_q(a)=\sum_mw_m e(am/q).
\]

The exact additive zero mode is

\[
\mu_P^{(0)}
=-W_H\sum_{d\le Z}\frac{\mu(d)\log d}{d}.
\tag{1.1}
\]

The primitive-frequency collapse gives

\[
\sum_mw_m\Lambda(P+m)-\mu_P^{(0)}
=
\sum_{q=2}^{Z}
\Gamma_Z(q)
\sum_{a\bmod q\atop(a,q)=1}
\widehat w_q(a)e(aP/q),
\tag{1.2}
\]

where

\[
\Gamma_Z(q)
=-\frac1q\sum_{u\le Z/q}\frac{\mu(qu)\log(qu)}u.
\tag{1.3}
\]

## 2. Smooth primitive rows

If `q|P`, then

\[
e(aP/q)=1
\]

for every reduced residue `a mod q`.  Therefore

\[
\sum_{(a,q)=1}\widehat w_q(a)e(aP/q)
=
\sum_mw_m c_q(m).
\tag{2.1}
\]

Define the exact smooth primitive block

\[
\boxed{
\mathcal M_P^{\mathrm{sm}}(w)
=
\sum_{q\mid P\atop q>1}
\Gamma_Z(q)
\sum_mw_m c_q(m).
}
\tag{2.2}
\]

## 3. Exact principal centring

### Definition 3.1

Set

\[
\boxed{
\mu_P^{\mathrm{prim}}(w)
=
\mu_P^{(0)}+\mathcal M_P^{\mathrm{sm}}(w).
}
\tag{3.1}
\]

### Theorem 3.2 (exact new-modulus residual)

One has exactly

\[
\boxed{
\sum_mw_m\Lambda(P+m)-\mu_P^{\mathrm{prim}}(w)
=
\sum_{q\le Z\atop q\nmid P}
\Gamma_Z(q)
\sum_{a\bmod q\atop(a,q)=1}
\widehat w_q(a)e(aP/q).
}
\tag{3.2}
\]

### Proof

Split the exact sum (1.2) into the disjoint classes `q|P` and `q` not dividing
`P`.  Use (2.1) on the first class and move it into the centring.  No
approximation is made.  \(\square\)

Every primitive denominator on the right of (3.2) contains at least one prime not
already present in the primorial.  Thus all coherent smooth local frequencies
have been removed before the variance is estimated.

## 4. Ramanujan approximation to the smooth block

Fix `0<delta<1`.  Split the smooth divisors at

\[
Q=P^{1-\delta}.
\]

For `q|P`, `q<=Q`, the long-complementary estimate from the primitive-frequency
theorem gives

\[
\Gamma_Z(q)
=
\frac{\mu(q)}{\varphi(q)}+\varepsilon_Z(q),
\tag{4.1}
\]

where the error has zero-free-region decay, uniformly in this range.

For a fixed physical offset `m<=H`,

\[
\sum_{q\mid P}
\frac{|c_q(m)|}{\varphi(q)}
=
\prod_{r\le z}
\left(1+\frac{|c_r(m)|}{r-1}\right).
\tag{4.2}
\]

If `r|m`, the local factor is `2`; otherwise it is `r/(r-1)`.  Since
`m<=H=poly(z)`, the number of prime divisors of `m` is `O(log z)`, and hence

\[
\sum_{q\mid P}
\frac{|c_q(m)|}{\varphi(q)}
=z^{o(1)}\frac P{\varphi(P)}.
\tag{4.3}
\]

The exponential zero-free-region decay therefore dominates the complete smooth
Ramanujan mass in the physical interval.  Summing over `m` gives

\[
\sum_{q\mid P\atop q\le Q}
\varepsilon_Z(q)
\sum_mw_m c_q(m)
=o(W_H)
\tag{4.4}
\]

for bounded or polylogarithmic weights.

## 5. Exact-coefficient tail

For `q|P`, formula (1.3) gives the elementary bound

\[
|\Gamma_Z(q)|
\ll
\frac{\log Z}{q}
\left(1+\log\frac Zq\right).
\tag{5.1}
\]

Also, with `g=(q,m)`, the squarefree Ramanujan formula gives

\[
|c_q(m)|
=
\frac{\varphi(q)}{\varphi(q/g)}
\le H z^{o(1)}.
\tag{5.2}
\]

Writing `v=P/q`,

\[
\sum_{q\mid P\atop q>Q}\frac1q
=
\frac1P
\sum_{v\mid P\atop v<P^\delta}v
\le
P^{-1+\delta+o(1)}.
\tag{5.3}
\]

Combining (5.1)--(5.3), uniformly for `m<=H=poly(z)`, gives

\[
\sum_{q\mid P\atop q>Q}
|\Gamma_Z(q)c_q(m)|
=P^{-1+\delta+o(1)}.
\tag{5.4}
\]

After the physical offset sum, this is still `o(W_H)`.

## 6. Candidate-projector asymptotic

Equations (4.4) and (5.4) permit replacement of the exact smooth block by the
complete Ramanujan projector:

\[
\mathcal M_P^{\mathrm{sm}}(w)
=
\sum_{q\mid P\atop q>1}
\frac{\mu(q)}{\varphi(q)}
\sum_mw_m c_q(m)
+o(W_H).
\tag{6.1}
\]

The exact projector identity gives

\[
\sum_{q\mid P}
\frac{\mu(q)}{\varphi(q)}c_q(m)
=
\frac P{\varphi(P)}\mathbf1_{(m,P)=1}.
\]

Removing the `q=1` term and summing over `m`,

\[
\mathcal M_P^{\mathrm{sm}}(w)
=
\frac P{\varphi(P)}
\sum_{(m,P)=1}w_m
-W_H+o(W_H).
\tag{6.2}
\]

The zero mode satisfies

\[
\mu_P^{(0)}=W_H+o(W_H).
\]

Therefore:

### Theorem 6.1 (candidate-principal asymptotic)

\[
\boxed{
\mu_P^{\mathrm{prim}}(w)
=
\frac P{\varphi(P)}
\sum_{(m,P)=1}w_m
+o(W_H).
}
\tag{6.3}
\]

When `2<=m<H<(z^+)^2`, coprimality is equivalent to `m` being a prime greater
than `z`.  Hence

\[
\boxed{
\mu_P^{\mathrm{prim}}(w)
=
\frac P{\varphi(P)}
\sum_{z<m\le H\atop m\text{ prime}}w_m
+o(W_H).
}
\tag{6.4}
\]

For sharp weights,

\[
\mu_P^{\mathrm{prim}}(H)
=
\frac P{\varphi(P)}
(\pi(H)-\pi(z))+o(H)
=
\left(\frac{e^\gamma}{2}+o(1)\right)H.
\tag{6.5}
\]

Thus the exact finite centring (3.1) has the correct candidate-projector
asymptotic without invoking a Hardy--Littlewood prime-pair asymptotic.

## 7. Correct final source

Define

\[
\boxed{
\mathcal E_P^{\mathrm{new}}(w)
=
\sum_mw_m\Lambda(P+m)-\mu_P^{\mathrm{prim}}(w).
}
\]

Then (3.2) is an exact formula for `mathcal E_P^new` using only primitive
frequencies containing at least one new prime.

The Fortune variance target is now

\[
\boxed{
\sum_j
|\mathcal E_{P_j}^{\mathrm{new}}(1)|^2
\ll NHX\,L(X),
\qquad L(X)=o(\log X).
}
\tag{7.1}
\]

This is the precise residual-preserving source after complete principal
subtraction.

## 8. Boundary

Proved exactly:

1. smooth primitive block (2.2);
2. exact finite centring (3.1);
3. exact new-modulus residual (3.2).

Proved from classical published input and elementary divisor estimates:

1. replacement of the smooth exact coefficients by Ramanujan coefficients;
2. negligible top smooth-divisor tail;
3. candidate-projector asymptotic (6.3)--(6.5).

Open:

1. the signed second moment (7.1) of the new-modulus residual;
2. cancellation between primitive denominators carrying different new primes;
3. Fortune's conjecture.
