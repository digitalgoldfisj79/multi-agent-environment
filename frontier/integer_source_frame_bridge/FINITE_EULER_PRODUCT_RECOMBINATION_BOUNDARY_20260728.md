# Finite Euler-product recombination boundary

Date: 28 July 2026  
Status: exact Dirichlet-series recombination and Perron representation proved; direct recombination is equivalent to the original prime short-interval problem.

## 1. Two quotient factors

Let

\[
P=\prod_{p\le z}p,
\qquad
Y=\sqrt{P+H}.
\]

For `Re(s)>1`, the Dirichlet series of the primorial-rough quotient variable is

\[
\boxed{
\mathcal R_P(s)
=
\sum_{(k,P)=1}\frac1{k^s}
=
\zeta(s)\prod_{p\le z}(1-p^{-s}).
}
\tag{1.1}
\]

The signed Euler-divisor series is

\[
\boxed{
\mathcal E_{z,Y}(s)
=
\sum_{Q\in\mathcal Q(z,Y)}\frac{\mu(Q)}{Q^s}
=
\prod_{z<p\le Y}(1-p^{-s}).
}
\tag{1.2}
\]

## 2. Exact full recombination

### Theorem 2.1

For `Re(s)>1`,

\[
\boxed{
\mathcal R_P(s)\mathcal E_{z,Y}(s)
=
\zeta(s)\prod_{p\le Y}(1-p^{-s}).
}
\tag{2.1}
\]

The Dirichlet coefficient of `n^{-s}` on either side is

\[
\boxed{
\sum_{Qk=n\atop Q\in\mathcal Q(z,Y),\ (k,P)=1}\mu(Q)
=
\mathbf1_{P^-(n)>Y},
}
\tag{2.2}
\]

where `P^-(n)` is the least prime factor, with `P^-(1)=infinity`.

### Proof

Multiply the Euler products (1.1)--(1.2).  Every factor for `p<=Y` cancels the
corresponding factor of `zeta(s)`, leaving the right side of (2.1).  Its
coefficient is one exactly when no prime `p<=Y` divides `n`.  Equality with the
convolution coefficient gives (2.2).  \(\square\)

Equation (2.2) is the coefficient form of the full rough-quotient Euler collapse.

## 3. Prime identification in the Fortune interval

Let

\[
P+z<n\le P+H,
\qquad Y=\sqrt{P+H}.
\]

### Corollary 3.1

\[
\boxed{
\mathbf1_{P^-(n)>Y}=\mathbf1_{n\text{ prime}}.
}
\tag{3.1}
\]

### Proof

A composite `n<=P+H=Y^2` has a prime divisor at most `sqrt(n)<=Y`.  Conversely a
prime `n>P+z>Y` has no prime divisor at most `Y`.  \(\square\)

Moreover, `n` coprime to all primes at most `Y` is automatically coprime to `P`,
so `m=n-P` is a candidate offset.  The source condition does not need to be
reinserted after full recombination.

## 4. Exact Perron representation

Put

\[
\mathcal F_Y(s)=\zeta(s)\prod_{p\le Y}(1-p^{-s}).
\tag{4.1}
\]

Its coefficients are `1_{P^-(n)>Y}`.  In the standard Perron limiting sense,

\[
\boxed{
\sum_{P+z<n\le P+H}\mathbf1_{n\text{ prime}}
=
\frac1{2\pi i}
\int_{c-i\infty}^{c+i\infty}
\mathcal F_Y(s)
\frac{(P+H)^s-(P+z)^s}{s}\,ds,
\quad c>1.
}
\tag{4.2}
\]

For the logarithmically weighted detector,

\[
\boxed{
\sum_{P+z<n\le P+H}\log n\,\mathbf1_{n\text{ prime}}
=
\frac1{2\pi i}
\int_{c-i\infty}^{c+i\infty}
[-\mathcal F_Y'(s)]
\frac{(P+H)^s-(P+z)^s}{s}\,ds.
}
\tag{4.3}
\]

Endpoint conventions may equivalently be implemented with finite-height Perron
formulae and their standard half-weight corrections; the interval here is the
same strict-lower, inclusive-upper interval as in the quotient identities.

## 5. Method boundary

The finite Euler product (4.1) is not a new black-box estimate for (4.2).  By
Corollary 3.1 its coefficients are already the prime indicator throughout the
Fortune interval.  Therefore a direct contour estimate strong enough to prove a
positive value in every such interval would solve the original short-interval
problem in this special primorial family.

This gives a precise architectural boundary:

1. the full quotient identity is exact and removes all artificial coefficient
   complexity;
2. complete recombination of every Euler layer returns the original prime
   detector;
3. positive or absolute estimates after complete recombination cannot exploit the
   intermediate martingale cancellation;
4. a viable proof must use structure before complete recombination—mesoscopic
   primorial sampling, ordered Buchstab increments, same-band rough-quotient
   dispersion, or an equivalent signed covariance identity.

## 6. Boundary

Proved exactly:

1. quotient and Euler-divisor Dirichlet series (1.1)--(1.2);
2. finite Euler-product recombination (2.1);
3. coefficient identity (2.2);
4. prime identification (3.1);
5. Perron representations (4.2)--(4.3).

Method-level conclusion:

1. fully recombined Perron analysis is not a shortcut supplied by the quotient
   collapse; it is another exact form of the prime short-interval problem;
2. the useful information lies in the intermediate signed decomposition.

Open:

1. deterministic centred sampling before complete recombination;
2. Fortune's conjecture.
