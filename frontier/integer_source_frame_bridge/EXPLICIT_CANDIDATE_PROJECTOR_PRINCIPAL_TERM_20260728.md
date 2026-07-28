# Explicit candidate-projector principal term

Date: 28 July 2026  
Status: explicit finite centring and its asymptotic proved; variance of the source around this centring remains open.

## 1. Candidate projector

Let

\[
P=\prod_{r\le z}r,
\qquad
2\le m<H<(z^+)^2.
\]

The exact primorial Ramanujan projector is

\[
\frac{\varphi(P)}P
\sum_{q\mid P}
\frac{\mu(q)}{\varphi(q)}c_q(m)
=
\mathbf1_{m\text{ prime},\ m>z}.
\tag{1.1}
\]

Thus the smooth primitive spectrum selects the candidate prime offsets exactly.

## 2. Explicit finite principal term

For deterministic weights `w_m`, define

\[
\boxed{
\mu_P^{\mathrm{cand}}(w)
=
\frac P{\varphi(P)}
\sum_{z<m\le H\atop m\text{ prime}}w_m.
}
\tag{2.1}
\]

For the sharp one-sided detector `w_m=1`,

\[
\boxed{
\mu_P^{\mathrm{cand}}(H)
=
\frac P{\varphi(P)}
\bigl(\pi(H)-\pi(z)\bigr).
}
\tag{2.2}
\]

This is explicit, positive and centre-dependent only through the primorial cutoff
`z`.

It is the `q_1=1` component obtained after:

1. collapsing the exact Möbius--log source to primitive rational frequencies;
2. replacing the long-complementary coefficient by its proved Ramanujan
   coefficient `mu(q)/phi(q)`;
3. summing the complete smooth divisor spectrum `q|P`.

No Hardy--Littlewood conjecture is used to define (2.1)--(2.2).

## 3. Asymptotic size

Mertens' product theorem gives

\[
\frac P{\varphi(P)}
=
\prod_{r\le z}\left(1-\frac1r\right)^{-1}
=
(e^\gamma+o(1))\log z.
\tag{3.1}
\]

The prime number theorem gives, uniformly for

\[
H=\eta X^2,
\qquad z\asymp X,
\qquad 0<\eta<1,
\]

\[
\pi(H)-\pi(z)
=
\frac H{\log H}(1+o(1)).
\tag{3.2}
\]

Since `log H=2log X+O(1)` and `log z=log X+O(1)`, equations
(2.2)--(3.2) yield

\[
\boxed{
\mu_P^{\mathrm{cand}}(H)
=
\left(\frac{e^\gamma}{2}+o(1)\right)H.
}
\tag{3.3}
\]

In particular, for sufficiently large `X`,

\[
\mu_P^{\mathrm{cand}}(H)\ge cH
\]

for an absolute `c>0`, uniformly over the dyadic primorial block.

## 4. Agreement with the Hardy--Littlewood local principal

The prime-pair singular series for the forms `m` and `P+m` is

\[
\mathfrak S(P)
=
\frac P{\varphi(P)}
\prod_{r>z}\left(1-\frac1{(r-1)^2}\right).
\tag{4.1}
\]

The tail product is absolutely convergent and

\[
\sum_{r>z}\frac1{(r-1)^2}\ll\frac1z.
\]

Therefore

\[
\boxed{
\prod_{r>z}\left(1-\frac1{(r-1)^2}\right)
=1+O(1/z).
}
\tag{4.2}
\]

The Hardy--Littlewood local principal is

\[
\mu_P^{\mathrm{HL}}(H)
=
\mathfrak S(P)
\int_z^H\frac{dt}{\log t}.
\tag{4.3}
\]

Using the PNT to compare the prime count with the logarithmic integral and (4.2),
one obtains

\[
\boxed{
\mu_P^{\mathrm{HL}}(H)
-
\mu_P^{\mathrm{cand}}(H)
=o(H)
}
\tag{4.4}
\]

uniformly in the Fortune block.

Equation (4.4) compares two explicit/local-model expressions.  It does not assert
that the actual shifted-prime source has either asymptotic.

## 5. Smooth-subtracted explicit centring

The deterministic smooth sector satisfies

\[
G_P(H)=(\log2+o(1))H.
\]

Define

\[
\boxed{
\mu_P^{\mathrm{red,cand}}(H)
=
\mu_P^{\mathrm{cand}}(H)-G_P(H).
}
\tag{5.1}
\]

Then

\[
\boxed{
\mu_P^{\mathrm{red,cand}}(H)
=
\left(
\frac{e^\gamma}{2}-\log2+o(1)
\right)H.
}
\tag{5.2}
\]

Since

\[
\frac{e^\gamma}{2}-\log2>0,
\]

this is a uniform positive reduced centring.

## 6. Correct variance target

The principal-subtraction obligation is now discharged: use the explicit finite
quantity (2.2), or equivalently (5.1) after exact smooth subtraction.

The remaining load-bearing theorem is

\[
\boxed{
\sum_j
\left|
\sum_{m=2}^{H}\Lambda(P_j+m)
-
\mu_{P_j}^{\mathrm{cand}}(H)
\right|^2
\ll NHX\,L(X),
\qquad L(X)=o(\log X).
}
\tag{6.1}
\]

An `o(H)` alteration of the centring is harmless only if its block-square total is
also absorbed at the right side of (6.1).  Formula (2.2), rather than merely its
asymptotic constant, should therefore be retained in the exact programme.

## 7. What has and has not been solved

Solved:

1. explicit candidate projection;
2. explicit finite positive centring;
3. asymptotic constant `e^gamma/2`;
4. agreement with the Hardy--Littlewood local principal up to `o(H)`;
5. positive smooth-subtracted constant `e^gamma/2-log 2`.

Not solved:

1. the actual source asymptotic at every primorial centre;
2. the variance estimate (6.1);
3. the signed primitive-frequency frame bound;
4. Fortune's conjecture.
