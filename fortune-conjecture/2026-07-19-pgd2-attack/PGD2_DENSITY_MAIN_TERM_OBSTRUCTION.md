# PGD2 prime-pair density main-term obstruction

## Density model

Let \(I=[H,2H)\), \(H=X^2/2\), and use the fixed-harmonic smooth weight \(w_a(n)\). Define

\[
D_\rho=\sum_{n\in I}\frac1{\log n}\sum_{b\ne0}w_b(n),
\qquad
\widetilde p_{n,a}=\frac{w_a(n)}{D_\rho\log n}.
\]

The Hardy--Littlewood density replacement for the distinct-prime sector is

\[
\mathcal R_a^{\rm HL}
=
\sum_{n\ne m}
\widetilde p_{n,a}\widetilde p_{m,a}
\mathfrak S(m-n)
\left(
\left|H_2\!\left(a\left(\frac1n-\frac1m\right)\right)\right|^2-M
\right).
\]

## Resonant semiprime family

Let

\[
\mathcal A_X=
\{n=pr:\ X/\sqrt2\le p<r<X,\ p,r\ \text{prime}\}.
\]

Every \(n\in\mathcal A_X\) lies in \([H,2H)\), is odd and divides

\[
A_X=\prod_{p<X}p.
\]

Since every primorial-prefix centre \(P_j\) is divisible by \(A_X\), for distinct \(n,m\in\mathcal A_X\),

\[
e(P_j/n)=e(P_j/m)=1
\quad\text{for every }j,
\]

and therefore

\[
H_2\!\left(a\left(\frac1n-\frac1m\right)\right)=M.
\]

The kernel equals \(M^2-M\). Also \(m-n\) is even and
\(\mathfrak S(m-n)\ge 2C_2>0\).

By the prime number theorem,

\[
|\mathcal A_X|\asymp \frac{X^2}{\log^2X}\asymp M,
\qquad
\widetilde p_{n,a}\asymp H^{-1}
\quad(n\in\mathcal A_X).
\]

Consequently the resonant positive contribution is

\[
\gg
(M^2-M)\frac{|\mathcal A_X|^2}{H^2}
\asymp \frac{M^2}{\log^4X}.
\]

The kernel is bounded below by \(-M\), while the singular series has subpower maximum. Hence all negative terms together are
\(\gg -MX^{o(1)}\). Thus

\[
\boxed{
\mathcal R_a^{\rm HL}
\gg
\frac{M^2}{\log^4X}-MX^{o(1)}.}
\]

Since

\[
\frac{M}{\log^4X}\asymp\frac{X^2}{\log^6X},
\]

the density main term is polynomially above the PGD2 target.

## Finite audit

Exact complete density panels were run through \(X=120\); Monte Carlo panels with one million weighted pairs were run at \(X=150,200,300\). The Hardy--Littlewood main term divided by \(M\) was approximately

\[
0.8185,\quad1.1892,\quad2.5938
\]

at \(X=150,200,300\), with standard errors below \(0.022M\). These values are pre-asymptotic diagnostics; the obstruction above is algebraic/asymptotic and does not rely on the panel.

## Decision

A conventional decomposition

\[
\text{prime-pair measure}
=
\text{Hardy--Littlewood density main term}
+
\text{small dispersion error}
\]

cannot prove PGD2. The error must cancel a polynomially large resonant-composite main term. Any viable detector argument must preserve the complete signed primality cancellation through the final reciprocal estimate.
