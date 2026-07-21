# A uniform Weil bound for locally admissible factor parity

**Date:** 2026-07-21  
**Status:** proved, conditional only on the standard one-variable Weil bound for quadratic character sums.

## 1. Statement

Let \(p\ge5\) be prime, \(a\in\mathbf F_p^*\), and

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d.
\]

Call \((c,d)\) locally admissible when

\[
H_{a,c,d}(X)=aX^3+(c+1)X+d
\]

has no root in \(\mathbf F_p\). Define

\[
M_a^{\mathrm{loc}}(p)=
\sum_{H_{a,c,d}\ \mathrm{rootless}}
\chi(\operatorname{Disc}F_{a,c,d}).
\]

The local-admissibility theorem in `DISCRIMINANT_MASS.md` shows that every
summand is \(\pm1\), and that

\[
M_a^{\mathrm{loc}}(p)=\frac{2S_a+C_a-R_a-\tau_a}{3},
\]

where \(|S_a|\le2p\), \(|\tau_a|\le1\), and

\[
C_a=\sum_{u,v}
\chi(-4u^3-27v^2)\chi(D_a(u,v)),
\]

\[
R_a=\sum_{x,u}\chi(D_a(u,-x^3-ux)).
\]

Here

\[
D_a(u,v)=\operatorname{Disc}
\bigl(X^p+aX^3+(au-1)X+av\bigr).
\]

### Theorem WP.1

Uniformly in \(a\ne0\),

\[
\boxed{|C_a|\le3p^{3/2}+3p,}
\]

\[
\boxed{|R_a|\le5p^{3/2}+3p.}
\]

Consequently

\[
\boxed{
|M_a^{\mathrm{loc}}(p)|
\le\frac{8p^{3/2}+10p+1}{3}.
}
\]

In particular,

\[
M_a^{\mathrm{loc}}(p)=O(p^{3/2})
\]

with an absolute, effective constant.

## 2. The cross term

Fix \(u\), put

\[
t=au-1,
\qquad
\varepsilon=\chi\!\left(-\frac{t}{3a}\right),
\]

and, when \(t\ne0\), set

\[
B_t=t\left(\varepsilon+\frac{2t}{3}\right)^2.
\]

The discriminant formula gives, up to the harmless constant \(s_p\),

\[
D_a(u,v)=3a^3v^2+B_t.
\]

The cubic-tail discriminant is

\[
\Delta(u,v)=-27v^2-4u^3.
\]

Thus the fixed-\(u\) contribution to \(C_a\) is the quadratic-character
sum of the degree-at-most-four polynomial

\[
P_u(v)=(3a^3v^2+B_t)(-27v^2-4u^3).
\]

For \(t\ne0\), this polynomial is a square over the algebraic closure only
if its two linear factors in \(v^2\) are proportional. The proportionality
condition is

\[
-12a^3u^3+27B_t=0.
\]

Using \(au=t+1\), it reduces exactly to

\[
36(\varepsilon-1)t^2-9t-12=0.
\]

Hence:

- on the \(\varepsilon=1\) branch, the only candidate is
  \(t=-4/3\);
- on the \(\varepsilon=-1\) branch, the candidates satisfy
  \(24t^2+3t+4=0\).

There are therefore at most three exceptional values of \(u\). The case
\(t=0\) gives

\[
P_u(v)=3a^3v^2(-27v^2-4u^3),
\]

which is not a square because \(u=a^{-1}\ne0\).

For every nonexceptional \(u\), the standard Weil bound for a non-square
polynomial of degree at most four gives

\[
\left|\sum_v\chi(P_u(v))\right|\le3\sqrt p.
\]

Using the trivial bound \(p\) on at most three exceptional fibres yields

\[
|C_a|\le3p^{3/2}+3p.
\]

## 3. The root-incidence term

Again fix \(u\) and put \(t=au-1\). Substituting

\[
v=-x^3-ux
\]

into the discriminant gives, up to \(s_p\),

\[
Q_u(x)=3a^3(x^3+ux)^2+B_t.
\]

If \(B_t\ne0\), then \(Q_u\) is not a square polynomial over the algebraic
closure. Indeed, if

\[
R(x)^2=3a^3(x^3+ux)^2+B_t,
\]

then after adjoining a square root of \(3a^3\), the difference of two
squares factors as the nonzero constant \(B_t\). Both factors would have to
be constant, contradicting the cubic degree of \(x^3+ux\).

The condition \(B_t=0\) has at most three solutions:

\[
t=0,\qquad t=-3/2\text{ on the }\varepsilon=1\text{ branch},\qquad
t=3/2\text{ on the }\varepsilon=-1\text{ branch}.
\]

For every other \(u\), the degree-six Weil bound gives

\[
\left|\sum_x\chi(Q_u(x))\right|\le5\sqrt p.
\]

Applying the trivial bound on the at most three exceptional fibres gives

\[
|R_a|\le5p^{3/2}+3p.
\]

## 4. Factor-parity consequence

There are exactly

\[
I_p=\frac{p^2-1}{3}
\]

locally admissible members in each nonzero cubic slice. Since all are
squarefree, Pellet's formula makes the discriminant character equal to
`+1` for an odd number of irreducible factors and `-1` for an even number.
Therefore

\[
N_{a,+}=\frac{I_p+M_a^{\mathrm{loc}}(p)}2,
\qquad
N_{a,-}=\frac{I_p-M_a^{\mathrm{loc}}(p)}2,
\]

and Theorem WP.1 gives

\[
\boxed{
N_{a,+}=\frac{p^2}{6}+O(p^{3/2}),
\qquad
N_{a,-}=\frac{p^2}{6}+O(p^{3/2}).
}
\]

This is an unconditional parity-equidistribution theorem for the exact
locally admissible cubic family.

## 5. Relation to the irreducibility target

The theorem does not distinguish an irreducible polynomial from a
squarefree product of three, five, or more irreducible factors; all have
positive discriminant character in odd degree. It therefore does not by
itself prove FF-Fortune\((p,1)\).

It supplies a precise bridge to a reducible-count or RQM theorem. If one
can prove that the number of locally admissible members having at least
three irreducible factors is strictly below \(N_{a,+}\), an irreducible
member is forced. The required companion estimate now concerns only the
odd reducible sector, not the whole cubic family.

## 6. Possible sharpening

The observed restricted masses are of order \(p\), not \(p^{3/2}\). The
loss comes from summing the one-variable Weil bounds independently over
\(u\). A two-dimensional Kummer-sheaf analysis of \(C_a\) and \(R_a\)
should recover square-root cancellation over \(p^2\) points and give the
expected bound

\[
C_a,R_a=O(p),
\qquad
M_a^{\mathrm{loc}}(p)=O(p).
\]

That geometric sharpening is the next standalone target, but Theorem WP.1
already establishes a rigorous nontrivial asymptotic without any
growing-degree input.