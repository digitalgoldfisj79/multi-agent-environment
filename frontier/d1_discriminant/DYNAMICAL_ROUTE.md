# Constructive dynamics for the d=1 function-field Fortune problem

**Date:** 2026-07-21  
**Status:** exact equivalence proved; affine and global Artin–Schreier semiconjugacy templates eliminated.

## 1. Exact equivalence

Let \(p\) be prime, let \(g\in\mathbf F_p[X]\) have degree below \(p\), and set

\[
f_g(X)=X^p-g(X).
\]

### Theorem DY.1

The polynomial \(f_g\) is irreducible of degree \(p\) over \(\mathbf F_p\)
if and only if a root \(\alpha\) of

\[
\alpha^p=g(\alpha)
\]

has exact composition period \(p\) under \(g\):

\[
g^{\circ p}(\alpha)=\alpha,
\qquad
g^{\circ k}(\alpha)\ne\alpha\quad(1\le k<p).
\]

Indeed, because the coefficients of \(g\) lie in \(\mathbf F_p\),

\[
\alpha^{p^k}=g^{\circ k}(\alpha).
\]

The least positive Frobenius return time is the extension degree of
\(\alpha\). Exact period \(p\) is therefore equivalent to the minimal
polynomial of \(\alpha\) having degree \(p\), and that polynomial must then
be \(f_g\).

For

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d,
\]

the associated map is

\[
g(X)=-aX^3-cX-d.
\]

A single explicit family of such maps with a Frobenius-compatible orbit of
exact period \(p\) would prove the d=1 function-field target.

## 2. Fixed points and the correct local cubic

### Lemma DY.2

If \(g\) has a fixed point \(r\in\mathbf F_p\), then \(X^p-g(X)\) is
reducible, because

\[
r^p-g(r)=r-g(r)=0.
\]

For the cubic map above, the fixed-point equation is

\[
a r^3+(c+1)r+d=0.
\]

Thus the exact local admissibility condition is rootlessness of

\[
H_{a,c,d}(X)=aX^3+(c+1)X+d.
\]

The shift by `+1` is essential when discriminant data are correlated with
local admissibility. It does not alter unrestricted coefficient counts,
because \(c\mapsto c+1\) is a bijection.

## 3. Complete classification of affine attempts

Let

\[
g(X)=uX+v.
\]

### Theorem DY.3

The only irreducible affine examples are

\[
X^p-X-v,
\qquad v\ne0.
\]

They are the constant-offset Artin–Schreier polynomials and are excluded
from the nonconstant Fortune problem.

If \(u\ne1\), the map has the \(\mathbf F_p\)-fixed point
\(v/(1-u)\), so reducibility follows from Lemma DY.2. If \(u=1\), the case
\(v=0\) splits completely, while \(v\ne0\) gives the standard irreducible
Artin–Schreier polynomial.

## 4. No global rational semiconjugacy from translation

The natural source of a period-\(p\) orbit is the translation

\[
\tau(X)=X+1.
\]

Suppose a nonconstant \(R\in\mathbf F_p(X)\) and a rational map
\(g\in\mathbf F_p(X)\) satisfy

\[
R(X+1)=g(R(X))
\]

as a rational-function identity.

### Theorem DY.4

Then \(g\) has rational degree one.

The translation stabilises the subfield
\(K=\mathbf F_p(R)\subset\mathbf F_p(X)\). Because translation has finite
order, the induced endomorphism of \(K\) is an automorphism. Every
\(\mathbf F_p\)-automorphism of the rational function field
\(\mathbf F_p(R)\) is Möbius, so

\[
g(Y)=\frac{aY+b}{cY+d}.
\]

Consequently no global rational conjugacy, quotient or semiconjugacy of
Artin–Schreier translation can produce the required quadratic or cubic
map.

## 5. What remains viable

The global obstruction does not rule out identities on one specific
Artin–Schreier fibre. Two constructive programmes remain.

### Fibre-specific semiconjugacy

Seek \(R_p\) and a cubic \(g_p\) satisfying

\[
R_p(X+1)\equiv g_p(R_p(X))
\pmod{X^p-X-v}.
\]

This congruence may exploit the chosen degree-\(p\) fibre and evade Theorem
DY.4.

### Direct dynatomic factor construction

Seek a cubic \(g_p\) for which \(X^p-g_p(X)\) is exhibited as a factor of
the exact-period-\(p\) dynatomic polynomial, together with an argument
excluding all lower periods.

The first programme is computationally cleaner. For each existing
certified witness, choose a root \(\alpha\) and an Artin–Schreier generator
\(\beta\) with \(\beta^p=\beta+1\). Interpolate the unique polynomial
\(R_p\) of degree below \(p\) satisfying

\[
R_p(\beta+i)=g^{\circ i}(\alpha),
\qquad i\in\mathbf F_p.
\]

The relevant diagnostic is whether \(R_p\) has systematically sparse or
low-complexity support in the monomial, binomial or additive-polynomial
bases. A stable pattern would be a candidate construction; broad failure
would eliminate a principled ansatz class rather than merely add another
negative coefficient search.
