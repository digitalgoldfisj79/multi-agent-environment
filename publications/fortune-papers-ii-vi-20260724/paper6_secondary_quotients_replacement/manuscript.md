---
title: |
  Secondary Traces and Kummer Quotients for the Function-Field Fortune Crown
subtitle: |
  Cyclotomic tangents, Artin--Schreier descent, and an exact nonvanishing frontier
author:
  - "Edward Stewart Anthony Bozzard (ORCID 0009-0002-4052-0994)"
date: "27 July 2026"
lang: en-GB
abstract: |
  The preceding paper reduces the function-field $d=1$ Fortune crown to the
  positivity of
  $$
  W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2},
  $$
  and proves that ordinary aggregate Betti bounds, the alternating-hook
  $p$-cycle fixed-point formula and invariant q-line nonsaturation all return
  exactly to this unknown count.  This paper studies the first integral layer
  discarded by those semisimple formulations.

  For a fixed nonzero cubic coefficient $a$, we introduce the Cartier first
  moment $M_a=\sum_{\mathrm{irr}}c$ and identify it as the first cyclotomic
  tangent of the coefficient Fourier transform.  The coefficient tangent is a
  nonsplit self-extension of the trivial $\mathbf F_p[C_p]$-module, with an
  explicit Tate complex and identity Bockstein; nevertheless a family of
  Frobenius lifts shows that these modular data do not determine the tangent
  trace.  The root-cycle hook satisfies
  $\Theta_p=p\mathbf 1-\operatorname{Reg}_{C_p}$, and its division by $p$ is not
  an ordinary virtual character.  We replace that nonexistent divided object
  by the Hattori--Stallings coefficient trace, proving
  $\operatorname{Tr}_{\mathbf Z}(\Phi\sigma^{-r})=p h_r$.

  On the fixed cubic ordered-root slice we construct a global cyclic transfer
  and an Artin--Schreier coordinate $y$ with $\sigma(y)=y+1$.  The invariant
  $g=y^p-y$ records the Frobenius shift; its level $g=1$ is exactly the
  irreducibility section.  A logarithmic-derivative argument proves that the
  split level is empty for $p>5$, giving
  $\operatorname{card}Y_a(\mathbf F_p)=(p-1)N_a$.  The two cubic arithmetic classes are Kummer
  forms under $\mu_{p-3}$, not universally quadratic sign twists.  Their common
  quotient has $(N_{\mathrm{sq}}+N_{\mathrm{ns}})/2$ rational points on the irreducibility
  level.  Finally, the natural proper root-cycle quotient has one isolated wild
  fixed point and exact count
  $$
  \operatorname{card}\mathscr Q_p(\mathbf F_p)=1+(p-1)W_p.
  $$
  Hence even a favourable standard congruence modulo $p$ permits both the
  failure value $W_p=0$ and known positive cases.  The integral carriers and
  quotient geometry are constructed, but the crown remains equivalent to a
  genuinely one-sided compactly supported Frobenius or rational-point theorem.
keywords: ["Hattori--Stallings trace", "Artin--Schreier", "Kummer theory", "cyclotomic tangent", "finite fields", "Frobenius traces"]
bibliography: references.bib
link-citations: true
reference-section-title: References
---

# 1. Input from the exact crown

Paper V fixes the arithmetic coordinates for the function-field $d=1$ problem
[@BozzardPaperV].  For a prime $p>3$, let
\[
f_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad a\in\mathbf F_p^*.
\]
The irreducible count depends only on the square class of $a$; write these two
counts as $N_{\mathrm{sq}}$ and $N_{\mathrm{ns}}$.  Let $N_2$ be the quadratic normal-form
count.  The full four-parameter interval has
\[
I_4=(p-1)+p(p-1)N_2+
\frac{p(p-1)}2(N_{\mathrm{sq}}+N_{\mathrm{ns}}),
\]
so the crown is exactly
\[
\boxed{
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2}>0.
}
\]
Failure requires $N_2=N_{\mathrm{sq}}=N_{\mathrm{ns}}=0$.

Paper V also establishes three stopping points.  The actual aggregate Betti
constant is already too large at $p=11$; the alternating-hook $p$-cycle fixed
locus has $pI_4+p$ points and therefore reconstructs the unknown count; and the
invariant q-line saturation defect is precisely $p(N_{\mathrm{sq}}+N_{\mathrm{ns}})$.  The
present paper asks whether integral first-order information or quotient geometry
contains a stronger positivity mechanism.

All results below are unconditional unless marked as exact computer-assisted
or open.  No theorem in this paper proves the universal crown.

# 2. A fixed-class Cartier first moment

Fix $a\ne0$ and put
\[
N_a=\operatorname{card}\{(c,d)\in\mathbf F_p^2:f_{a,c,d}\text{ irreducible}\}.
\]
Define the first coefficient moment
\[
\boxed{
M_a=\sum_{f_{a,c,d}\ \mathrm{irreducible}}c
\quad\text{in }\mathbf F_p.
}
\]
If $M_a\ne0$, then the fixed class is nonempty.  This implication is elementary
but useful because the free involution $d\mapsto-d$ forces $N_a$ to be even,
whereas it does not force $M_a$ to vanish.

Let $C_1(f)$ denote the first selected Cartier cofactor associated to a monic
degree-$p$ polynomial.  The cofactor indicator theorem gives pointwise
\[
C_1(f_{a,c,d})=c\,1_{f_{a,c,d}\ \mathrm{irreducible}}.
\]

## Theorem 2.1 (Cartier moment identity)

\[
\boxed{M_a=\sum_{c,d\in\mathbf F_p}C_1(f_{a,c,d}).}
\]
In particular, nonvanishing of this Cartier mass is a sufficient fixed-class
existence certificate.

The theorem does not assert that the mass is always nonzero.  Exact computation
finds nonzero values in both classes throughout a large tested range, apart
from the square class at $p=5$, where $N_{\mathrm{sq}}=4$ but $M_{\mathrm{sq}}=0$.  This is
empirical evidence, not a uniform theorem.

# 3. Translation and reciprocal projectors

Consider the full cubic family
\[
F_{a,b,c,d}(X)=X^p+aX^3+bX^2+cX+d.
\]
Translation $X\mapsto X+t$ sends a depressed representative to coefficients
\[
b_t=3at,
\qquad
c_t=c_0+3at^2,
\qquad
d_t=d_0+(c_0+1)t+at^3.
\]
Every irreducible translation orbit has one depressed representative.  Since
\[
\sum_{t\in\mathbf F_p}b_t^{p-1}c_t
=\sum_{t\ne0}(c_0+3at^2)=-c_0,
\]
one obtains an exact full-family projector.

## Theorem 3.1 (translation projector)

\[
\boxed{
M_a=-\sum_{b,c,d}b^{p-1}c\,
1_{F_{a,b,c,d}\ \mathrm{irreducible}}.
}
\]
Equivalently,
\[
M_a=-\sum_{b,c,d}b^{p-1}C_1(F_{a,b,c,d}).
\]
Thus the depressed first moment is a boundary coefficient of the canonical
full-family Cartier function, not an isolated low-degree monomial of the
depressed determinant.

For $c\ne0$, use the q-line coordinate
\[
q=-3/c.
\]
If $A=\chi(a)$, Paper V shows that the required normal-form reading at $q$ is
$\varepsilon=A\chi(q)$.  Let $I_\varepsilon(q)$ be the irreducible constant-fibre
count in that cell.  Since $c=-3q^{-1}$ and the $c=0$ boundary has zero weight,
we obtain the reciprocal form.

## Theorem 3.2 (reciprocal q-line moment)

\[
\boxed{
M_A=-3\sum_{q\in\mathbf F_p^*}q^{-1}I_{A\chi(q)}(q).
}
\]
The unweighted cell main term cancels because
$\sum_{q\ne0}q^{-1}=0$.  The coefficient $q^{-1}$ is, however, an
$\mathbf F_p$-valued Hasse weight rather than a bounded-rank characteristic-zero
trace function.  This identity therefore does not turn the problem into an
ordinary low-conductor sheaf estimate.

# 4. The first cyclotomic tangent

Let $\zeta$ be a primitive $p$-th root of unity and put
\[
\pi=\zeta-1.
\]
Define the coefficient Fourier value
\[
\mathcal F_a=
\sum_{c,d}1_{f_{a,c,d}\ \mathrm{irreducible}}\zeta^c.
\]
Because
\[
\zeta^c=(1+\pi)^c\equiv1+c\pi\pmod{\pi^2},
\]
we have the following exact tangent formula.

## Theorem 4.1 (cyclotomic tangent)

\[
\boxed{
\mathcal F_a=N_a+\pi M_a+O(\pi^2),
\qquad
\frac{\mathcal F_a-N_a}{\pi}\equiv M_a\pmod\pi.
}
\]

Thus the first moment is the first integral derivative of the irreducibility
Fourier transform.  Semisimplification at $\pi=0$ retains $N_a$ but discards
precisely the extension data in which $M_a$ lives.

Scaling shows that, for $a\ne0$, $M_a$ depends only on $\chi(a)$.  Extending the
cofactor sum to $a=0$ gives $M_0=1$.  Hence the canonical polynomial function
of $a$ has exactly three modes:
\[
\boxed{
M(a)=1+U_pa^{p-1}+V_pa^{(p-1)/2}.
}
\]
Simultaneous vanishing in the square and nonsquare classes is equivalent to
$U_p=-1$ and $V_p=0$, or $M(a)=1-a^{p-1}$.  This sharpens the failure pattern
but does not exclude it.

# 5. The tangent coefficient module

Let
\[
\mathcal O=\mathbf Z_p[\zeta],
\qquad R=\mathcal O/(\pi^2),
\qquad k=\mathcal O/(\pi)\cong\mathbf F_p.
\]
Since $v_\pi(p)=p-1$, one has $p=0$ in $R$ for $p\ge5$.  Let
$C_p=\langle\tau\rangle$.  The coefficient Fourier character modulo $\pi^2$
is the rank-one $R[C_p]$-module
\[
R_{\mathrm{tan}}=R,
\qquad \tau x=(1+\pi)x.
\]
The filtration by $\pi$ gives
\[
0\longrightarrow k\longrightarrow R_{\mathrm{tan}}
\longrightarrow k\longrightarrow0.
\]
In a suitable $k$-basis, $\tau$ is one nontrivial unipotent Jordan block.

## Theorem 5.1 (nonsplit tangent extension)

The displayed sequence represents the nonzero class in
\[
\operatorname{Ext}^1_{k[C_p]}(k,k)
\cong H^1(C_p,k)\cong k.
\]
In particular it is nonsplit.

For a cyclic module, the periodic Tate complex alternates $\tau-1$ and the norm
$\mathcal N=1+\tau+\cdots+\tau^{p-1}$ [@BrownCohomology].  Here
\[
\tau-1=\pi,
\qquad
\mathcal N=0\quad\text{in }R,
\]
so the complex is
\[
\cdots\xrightarrow0R\xrightarrow\pi R\xrightarrow0R
\xrightarrow\pi R\xrightarrow0\cdots.
\]
Since $\ker\pi=\pi R=\operatorname{im}\pi$, both Tate parities are one-dimensional:
\[
\widehat H^{\mathrm{even}}(C_p,R_{\mathrm{tan}})\cong k,
\qquad
\widehat H^{\mathrm{odd}}(C_p,R_{\mathrm{tan}})\cong k.
\]
Lifting the quotient generator $1$ and applying $\tau-1$ gives $\pi$; division
by $\pi$ therefore makes the coefficient Bockstein the identity.

# 6. Frobenius blindness and the precision shift

The tangent module does not determine its arithmetic Frobenius coefficient.
For any $\lambda\in k$, define
\[
\Phi_\lambda(x)=(1+\lambda\pi)x.
\]
Every $\Phi_\lambda$ commutes with $\tau$, acts identically on the two graded
lines and Tate groups, and preserves the same nonsplit extension and Bockstein.
Its trace is nevertheless
\[
1+\lambda\pi.
\]

## Theorem 6.1 (tangent Smith blindness)

Reduction modulo $\pi$, the two Tate groups, the extension class, the
coefficient Bockstein and cyclic equivariance do not determine the first
cyclotomic Frobenius tangent.  The missing coefficient ranges over all of
$\mathbf F_p$ in the family $\Phi_\lambda$.

There are also two distinct cyclic directions.  The coefficient Fourier group
weights $c$ by $\zeta^c$.  The root-cycle hook has value $p$ on a full
$p$-cycle and zero on other cycle types, so the raw Fourier-hook trace is
\[
\mathcal H_a=p\mathcal F_a.
\]
The cyclotomic product formula gives
\[
p=u\pi^{p-1},
\qquad u\in\mathcal O^*.
\]
Consequently
\[
\boxed{
\mathcal H_a=u\pi^{p-1}N_a+u\pi^pM_a+O(\pi^{p+1}).
}
\]
The count first appears at order $p-1$, and the first moment at order $p$.
An undivided hook construction modulo $\pi^2$ therefore sees neither.  It must
either retain precision through $\pi^{p+1}$ or perform a canonical secondary
division by the root-cycle factor $p$.

# 7. The divided hook is not an ordinary object

Let $V$ be the augmentation representation of the regular root cycle and put
\[
\Theta_p=\lambda_{-1}(V)=\sum_{i=0}^{p-1}(-1)^i\wedge^iV.
\]
Its character is zero at the identity and $p$ at every nonidentity element.
Therefore, in the characteristic-zero representation ring,
\[
\boxed{
\Theta_p=p\mathbf1-\operatorname{Reg}_{C_p}.
}
\]
The normalised nonidentity indicator $\Theta_p/p$ has Fourier multiplicity
$(p-1)/p$ at the trivial character and $-1/p$ at each nontrivial character.

## Theorem 7.1 (no ordinary divided-hook complex)

The class function $\Theta_p/p$ is not the character of a virtual
finite-dimensional representation of $C_p$ over any characteristic-zero field.
Consequently no ordinary perfect integral complex realises the divided hook.

The desired moment can still be written at trace level:
\[
\boxed{
M_a\equiv\frac{\mathcal H_a-pN_a}{p\pi}\pmod\pi.
}
\]
The theorem says only that this operation is secondary; it cannot be represented
by tensoring with an ordinary divided-hook object.

# 8. Hattori--Stallings division

Let $A=\mathbf Z[C_p]$.  For a bounded finite free $A$-complex $P$ and an
$A$-linear endomorphism $\Phi$, let
\[
h_\Phi=\sum_{r=0}^{p-1}h_r\sigma^r\in A
\]
be its alternating Hattori--Stallings trace [@Hattori1965; @LuckL2].

## Theorem 8.1 (exact coefficient extraction)

For every $r$,
\[
\boxed{
\operatorname{Tr}_{\mathbf Z}(\Phi\sigma^{-r}\mid P)=p h_r.
}
\]

### Proof

Write $\Phi$ as a matrix over $A$.  Its Hattori--Stallings trace is the sum of
the diagonal group-ring entries.  On a regular lattice, multiplication by
$\sigma^j$ followed by $\sigma^{-r}$ has ordinary trace $p$ if $j=r$ and zero
otherwise.  Summing the diagonal coefficients proves the formula.  $\square$

Thus $h_r$ is a canonical integral divided trace at a fixed root-cycle shift.
If a normaliser makes all nonidentity coefficients equal to $h_*$, then
\[
\boxed{
h_*=
\frac{\operatorname{Tr}(\Phi\mid P_{C_p})
-\operatorname{Tr}_{\mathbf Z}(\Phi\mid P)/p}{p-1}.
}
\]
In a bi-equivariant root-cycle/coefficient model, evaluating the coefficient
generator at $1+\pi$ and taking its first derivative recovers
$N_a+\pi M_a$ after the root-cycle coefficient extraction.  The algebraic
carrier therefore exists; what remains is a non-tautological geometric
nonvanishing theorem.

# 9. A global Artin--Schreier quotient

Let $X_a$ be the ordered-root slice
\[
e_1=\cdots=e_{p-4}=0,
\qquad e_{p-3}=a,
\qquad e_{p-2}=0,
\]
with remaining coefficients $e_{p-1}=c$ and $e_p=-d$.  Let
$\sigma(x_i)=x_{i+1}$.

## Proposition 9.1 (free root-cycle action)

For $a\ne0$, the $C_p$-action on $X_a$ is free.

### Proof

A tuple fixed by a nonidentity element is fixed by the full cyclic group, hence
all coordinates are equal.  But then
\[
e_{p-3}=\binom p3r^{p-3}=0
\]
in characteristic $p$, contradicting $e_{p-3}=a$.  $\square$

Every $(p-3)$-subset of $\mathbf F_p$ has a free orbit under translation.
Choose one representative from every orbit and put
\[
t=\sum_{S\ \mathrm{representative}}\prod_{i\in S}x_i.
\]
Then
\[
\sum_{j=0}^{p-1}\sigma^j(t)=e_{p-3}=a.
\]
Define
\[
U=\sum_{j=0}^{p-1}j\sigma^j(t),
\qquad y=-U/a.
\]
Reindexing gives $(\sigma-1)U=-a$, and hence
\[
\boxed{\sigma(y)=y+1.}
\]

## Theorem 9.2 (explicit Artin--Schreier quotient)

The function
\[
\boxed{g=y^p-y}
\]
is $C_p$-invariant, and the quotient map
\[
X_a\longrightarrow Y_a=X_a/C_p
\]
is represented in the root-cycle direction by
\[
\boxed{T^p-T=g.}
\]
The construction is trace-surjective.

Let $z\in Y_a(\mathbf F_p)$ and choose $x$ above it.  There is a unique
$r\in\mathbf F_p$ with $F(x)=\sigma^r x$.  Since $y$ is defined over
$\mathbf F_p$,
\[
y(x)^p=y(Fx)=y(\sigma^r x)=y(x)+r,
\]
so $g(z)=r$.

## Theorem 9.3 (irreducibility section)

For every $r\ne0$, projection to $(c,d)$ gives a bijection
\[
\boxed{
\{g=r\}(\mathbf F_p)
\longleftrightarrow
\{(c,d):f_{a,c,d}\text{ irreducible}\}.
}
\]
In particular,
\[
N_a=\operatorname{card}\{g=1\}(\mathbf F_p),
\qquad
M_a=\sum_{z\in\{g=1\}(\mathbf F_p)}c(z)\pmod p.
\]
The first moment is therefore an ordinary weighted rational-point sum on an
honest quotient level.

# 10. The split level is empty

The level $g=0$ would correspond to a polynomial in the fixed slice that splits
completely over $\mathbf F_p$.

## Theorem 10.1 (no-split theorem)

For every prime $p>5$ and every $a\ne0$,
\[
\boxed{X_a(\mathbf F_p)=\varnothing.}
\]
Consequently
\[
\boxed{\operatorname{card}Y_a(\mathbf F_p)=(p-1)N_a.}
\]

### Proof

Suppose
\[
f=X^p+aX^3+cX+d
\]
splits over $\mathbf F_p$.  For $x\in\mathbf F_p$,
\[
f(x)=ax^3+(c+1)x+d.
\]
All distinct roots of $f$ therefore lie among the roots of one nonzero cubic.
Let $R$ be the squarefree product of the distinct root factors, so
$\deg R\le3$.  In reduced form the logarithmic derivative is
\[
\frac{f'}f=\frac PR,
\qquad P\ne0,
\]
because $f'=3aX^2+c$ is nonzero.  Hence
\[
f'R=Pf.
\]
The left side has degree at most five, while the right side has degree at least
$p$.  Thus $p\le5$, a contradiction.  The quotient has no $r=0$ points, and
each of its $p-1$ nonzero levels has $N_a$ points by Theorem 9.3.  $\square$

The Artin--Schreier structure alone does not force the $g=1$ level to be
nonempty.  It is the special sparse geometry, not trace-surjectivity in the
abstract, that must supply any future point theorem.

# 11. The two classes are Kummer forms

Put $n=p-3$.  Scalar dilation sends
\[
a\mapsto\lambda^na,
\qquad c\mapsto\lambda^2c,
\qquad d\mapsto\lambda^3d.
\]
The Artin--Schreier coordinate is invariant under transport between fixed
fibres.  The geometric fibres are therefore forms classified by
\[
H^1(\mathbf F_p,\mu_n)
\cong\mathbf F_p^*/(\mathbf F_p^*)^n.
\]
Since
\[
\gcd(n,p-1)=\gcd(p-3,p-1)=2,
\]
there are exactly two classes: the square and nonsquare cubic coefficients.

## Theorem 11.1 (sign-twist criterion)

The element $-1\in\mu_n$ represents the nontrivial arithmetic form if and only
if
\[
\boxed{p\equiv1\pmod4.}
\]
For $p\equiv3\pmod4$, it is a coboundary; the nonsquare fibre requires a
nonquadratic Kummer cocycle.

### Proof

In exponent notation, Frobenius coboundaries are multiples of
$p-1\equiv2\pmod n$, so the two cohomology classes are even and odd exponents.
The sign element has exponent $n/2=(p-3)/2$, which is odd precisely when
$p\equiv1\pmod4$.  $\square$

Thus the two coefficient classes are not universally quadratic sign twists.
Let $D_p$ be the full $\mu_n$-quotient of the $g=1$ level and let $U_p$ be the
quotient of the complete fixed-cubic root-cycle open.  A rational quotient point
has lifts in exactly one of the two arithmetic forms, and the number of rational
lifts is
\[
\operatorname{card}\mu_n(\mathbf F_p)=2.
\]

## Theorem 11.2 (common Kummer quotient counts)

\[
\boxed{
\operatorname{card}D_p(\mathbf F_p)=\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2},
\qquad
\operatorname{card}U_p(\mathbf F_p)=\frac{p-1}{2}(N_{\mathrm{sq}}+N_{\mathrm{ns}}).
}
\]

This is a positive geometric carrier, but its rational-point theorem is exactly
cubic positivity.  The class difference is a Kummer-local-system trace rather
than ordinary cohomology of the common quotient.  The Kummer decomposition is
therefore the same invariant/anti-invariant arithmetic split already present in
the q-line ledger; it creates no third, smaller Frobenius target.

# 12. The projective quotient

Let
\[
\mathscr Y_p=
\{s_2=s_3=\cdots=s_{p-4}=0\}\subset\mathbf P(W)
\]
be the smooth sparse surface of Paper V, and put
\[
\mathscr Q_p=\mathscr Y_p/C_p.
\]
The open where $s_{p-3}\ne0$ is the common fixed-cubic Kummer quotient.

## Theorem 12.1 (unique projective fixed point)

Every nonidentity root-cycle element has exactly one fixed point on
$\mathscr Y_p$, represented by
\[
\boxed{[0,1,2,\ldots,p-1].}
\]
The quotient map is free in codimension one and has one isolated wild quotient
point.

### Proof

A fixed class in
\[
W=\{\sum x_i=0\}/\mathbf F_p(1,\ldots,1)
\]
satisfies $x_{i+1}-x_i=t$.  Modulo diagonal translation and projective scaling,
the unique nonzero solution is the displayed arithmetic progression.  It lies
on the sparse surface because
\[
\sum_{i\in\mathbf F_p}i^m=0
\qquad(1\le m\le p-2).
\]
The fixed-space calculation is the same for every nonidentity element of the
cyclic group.  $\square$

The source has canonical bundle
\[
K_{\mathscr Y_p}
=\mathcal O_{\mathscr Y_p}\left(\frac{(p-7)(p-2)}2\right),
\]
which is ample for admitted $p\ge11$.  Because the quotient singularity is wild,
this does not automatically prove that $\mathscr Q_p$ is $\mathbf Q$-Gorenstein,
canonical, Witt-rational or that a resolution inherits the same positivity.
Those are separate local questions and are not assumed below.

# 13. The exact compactified count

Away from the unique fixed point, a rational point of $\mathscr Q_p$ is a free
root-cycle orbit stable under Frobenius.  It has a unique shift
$r\in\mathbf F_p$ with $F(x)=\sigma^r x$.  For $r\ne0$, each nonlinear
irreducible affine orbit contributes one point.  The number of such affine
orbits is
\[
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2}.
\]
For $p>5$ there is no additional free $r=0$ orbit, by the same
logarithmic-derivative argument as in Theorem 10.1.  The entire linear
Artin--Schreier orbit compactifies to the one fixed progression point.

## Theorem 13.1 (compactified quotient count)

For every $p>5$,
\[
\boxed{
\operatorname{card}\mathscr Q_p(\mathbf F_p)=1+(p-1)W_p.
}
\]
Its boundary and cubic open satisfy
\[
\boxed{
\operatorname{card}(\mathscr Q_p\setminus U_p)(\mathbf F_p)=1+(p-1)N_2,
}
\[
\boxed{
\operatorname{card}U_p(\mathbf F_p)=\frac{p-1}{2}(N_{\mathrm{sq}}+N_{\mathrm{ns}}).
}
\]

The three formulas are mutually exact.  In particular,
\[
\operatorname{card}\mathscr Q_p(\mathbf F_p)\equiv1-W_p\pmod p.
\]
A hypothetical standard congruence
\[
\operatorname{card}\mathscr Q_p(\mathbf F_p)\equiv1\pmod p
\]
would imply only $W_p\equiv0\pmod p$.  This permits the failure value $W_p=0$.
It also occurs in a positive case: exact computation gives
\[
W_{17}=17,
\qquad
\operatorname{card}\mathscr Q_{17}(\mathbf F_{17})=273\equiv1\pmod{17}.
\]
Therefore even a successful standard proper-point congruence cannot distinguish
the crown from its exact failure configuration.

# 14. Reproducibility and exact checks

A clean-room script independently verifies the algebraic carriers and finite
ledgers used in this paper.

1.  Over the dual numbers $\mathbf F_p[\epsilon]/(\epsilon^2)$ at
    $p=5,7,11$, it checks $\tau^p=1$, zero norm, equality of kernel and image of
    $\tau-1$, and the full family of arbitrary Frobenius tangents.
2.  It records the nonintegral divided-hook Fourier multiplicities at the same
    primes.
3.  Random free group-ring matrices at $p=5,7$ verify the
    Hattori--Stallings coefficient formula.
4.  Direct finite checks find no squarefree completely split fixed-cubic case at
    $p=7,11$.
5.  The Kummer sign criterion is checked at $p=5,11,17,23,29$.
6.  The compactified point-count ledger is reconstructed at
    $p=7,11,17,23$, including the positive congruence example at $p=17$.

These are exact regressions of proved formulas.  They do not replace the missing
uniform rational-point theorem.  The release package contains the source
manifest, claim-status ledger, independent reconstruction, scripts,
machine-readable outputs and checksums.

# 15. The terminal theorem

The paper has constructed the integral and geometric objects that the ordinary
semisimple analysis could not see:

- the fixed-class Cartier tangent;
- the nonsplit coefficient extension and its Bockstein;
- the Hattori--Stallings divided root-cycle trace;
- the Artin--Schreier quotient whose $g=1$ level is irreducibility;
- the Kummer quotient packaging the class sum;
- the proper quotient with exact point count $1+(p-1)W_p$.

None supplies an independently computable positive term.  The exact remaining
statement can be formulated as follows.

> **One-sided Kummer-quotient Frobenius theorem.**  For every admitted prime,
> prove that the compactly supported Frobenius trace on the specific cubic
> quotient open cannot attain its zero-point value.

Arithmetically this is
\[
\boxed{N_{\mathrm{sq}}+N_{\mathrm{ns}}>0}
\]
whenever the quadratic sector has failed, or equivalently strict invariant
q-line nonsaturation.  It is a genuinely new nonvanishing theorem, not another
projector, congruence or quotient reformulation.

The following continuations are closed without a new ingredient:

1. a universal quadratic sign-twist compactification;
2. an ordinary divided-hook perfect complex;
3. coefficient Tate/Bockstein data without a secondary Frobenius trace;
4. generic Artin--Schreier trace-surjectivity as a point theorem;
5. standard proper-point congruences;
6. automatic Fano, rational-connected or Witt-rational claims at the wild point;
7. higher cyclotomic moments or larger finite scans without a structural
   prediction.

The function-field $d=1$ crown remains open.  This conclusion is the terminal
boundary of the present six-paper sequence, not a claim that Fortune's
conjecture has been proved.

## AI-assistance disclosure

The research programme used large language models for structured literature
triage, symbolic and computational cross-checking, adversarial review, software
drafting and editorial assembly.  Every result labelled as proved was checked
against a complete proof source or an independently reproducible exact
calculation.  Proved, published, computer-assisted, empirical, open and refuted
claims are separated in the accompanying ledger.  The named author takes
responsibility for the mathematics, citations, code and final presentation.

## Data and code availability

The manuscript source, proof-source manifest, claim-status ledger, independent
reconstruction, verification code, machine-readable outputs, review record,
compiled artefacts and checksums are maintained in the public repository
`digitalgoldfisj79/multi-agent-environment`.  Exact frozen commits are recorded
in the release manifest.
