---
title: "Fortunate Polynomials over Finite Fields"
subtitle: "Exact normal forms, sparse geometry, and the function-field d=1 crown"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "11 August 2026"
lang: en-GB
bibliography: references.bib
link-citations: true
reference-section-title: References
---

**Abstract.** We formulate a finite-field analogue of the Fortunate-number problem in which primes are replaced by monic irreducible polynomials. For the polynomial primorial \(P_d\), a reducible offset coprime to \(P_d\) has degree at least \(2d+2\). At \(d=1\) over \(\mathbf F_p\), where \(P_1=T^p-T\), the degree-at-most-three problem therefore reduces to an exact irreducibility count in a four-parameter affine interval. We prove the orbit decomposition
\[
I_4=(p-1)+p(p-1)N_2+\frac{p(p-1)}2(N_{\mathrm{sq}}+N_{\mathrm{ns}}),
\]
so the nonconstant crown is exactly the positivity of
\[
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2}.
\]

The associated ordered-root compactification is a smooth complete-intersection surface. Its affine short-interval variety is a translation torsor over the corresponding affine cone, giving an exact transfer of nontrivial isotypic compactly supported cohomology. A computer-assisted primitive-hook reconstruction at \(p=11\) shows that a natural aggregate absolute-Betti sufficient criterion already fails there. We prove an exact sign-hook trace, show that the alternating-hook projector is precisely the \(p\)-cycle trace, and compute the corresponding fixed-point count \(pI_4+p\), so the resulting one-sided primitive trace inequality is algebraically equivalent to the crown. Finally, the two depressed cubic square classes are assembled into one q-line system whose invariant saturation defect is exactly \(p(N_{\mathrm{sq}}+N_{\mathrm{ns}})\). Thus the geometry gives several exact reformulations and obstruction theorems, but it does not prove the universal function-field crown. No transfer to the integer Fortune conjecture is claimed.

**Keywords:** function fields; irreducible polynomials; finite fields; complete intersections; Frobenius traces; Fortunate numbers.

# 1. Problem, scope, and principal results

Let \(\mathbf F_q[T]\) play the role of the integers and monic irreducible polynomials the role of primes. For a degree cutoff \(d\), multiply all monic irreducibles of degree at most \(d\) to form a polynomial primorial. The analogue of a Fortunate offset is then the first nonconstant polynomial offset, under a fixed deterministic ordering, that makes the primorial plus the offset irreducible.

This model is not asserted to transfer to the integer Fortune conjecture. Its purpose is intrinsic: the finite coefficient spaces admit exact affine normal forms, ordered-root varieties and Frobenius actions, so one can determine which geometric or representation-theoretic transformations genuinely weaken the nonvanishing problem and which merely restate it.

The paper develops the \(d=1\) case over prime fields \(\mathbf F_p\), \(p>3\). The principal results are:

1. Proposition 2.1 gives the general reducible-offset degree barrier.
2. Theorem 4.1 and Corollary 4.2 reduce the \(d=1\) crown exactly to positivity of three nonnegative normal-form counts.
3. Theorem 5.1 proves global smoothness of the ordered-root complete-intersection surface.
4. Theorem 6.1 identifies the nontrivial isotypic compactly supported cohomology of the affine short-interval variety; the independently reproduced \(p=11\) hook census then refutes one aggregate absolute-Betti proof mechanism.
5. Theorems 7.1--9.1 and Corollary 9.2 identify the sign endpoint, the alternating-hook \(p\)-cycle projector and its exact fixed-point circularity.
6. Theorems 10.1 and 11.1 assemble the depressed cubic square classes into q-line projectors and prove that invariant saturation defect is exactly the cubic irreducible count.

Every labelled theorem below is proved symbolically in the manuscript. Finite computations are separately identified and serve as exact checks or finite-prime certificates. In particular, the \(p=11\) absolute-Betti counterexample uses an exact computer-assisted primitive-hook reconstruction; it is not a uniform theorem inferred from data. The universal positivity statement \(W_p>0\) remains open.

# 2. Polynomial primorials and the degree barrier

Let \(\mathbf F_q[T]\) be a polynomial ring.  Define the degree-\(d\)
polynomial primorial
\[
P_d=\prod_{\substack{\pi\ \mathrm{monic\ irreducible}\\ \deg \pi\le d}}\pi.
\]
Fix any deterministic ordering of nonconstant offsets, first by degree and then
by coefficients, and let \(F(q,d)\) be the first offset \(m\) for which
\(P_d+m\) is irreducible.

## Proposition 2.1 (reducible-offset degree barrier)

If \(m\) is reducible and \((m,P_d)=1\), then
\[
\deg m\ge 2d+2.
\]
Consequently, if some irreducible value \(P_d+m\) occurs with
\(1\le\deg m\le 2d+1\), then the least admissible offset in that range is
irreducible.

### Proof

Factor \(m\) uniquely, up to units and ordering, as a product of monic
irreducible polynomials.  Coprimality with \(P_d\) means that none of these
irreducible factors occurs among the factors of \(P_d\); hence each has
degree at least \(d+1\).  Because \(m\) is reducible, at least two factors
occur when multiplicity is counted.  Their degrees add, giving
\(\deg m\ge2(d+1)\).  The final assertion follows immediately.  \(\square\)

This is the exact function-field analogue of the elementary integer observation
that every prime factor of a composite Fortunate offset must exceed the current
primorial prime.

# 3. The \(d=1\) interval

From now on let the base field be \(\mathbf F_p\), with \(p>3\) prime.  The
product of all monic linear polynomials is
\[
P_1=\prod_{a\in\mathbf F_p}(T-a)=T^p-T.
\]
A nonconstant linear offset has the form \(uT+v\) with \(u\ne0\).  On
\(\mathbf F_p\),
\[
(T^p-T+uT+v)(x)=ux+v,
\]
so the polynomial has the rational root \(-v/u\) and is reducible.  Hence a
Fortunate offset must have degree at least two.  By Proposition 2.1, any
successful offset of degree two or three is automatically irreducible.

The complete degree-at-most-three interval is
\[
\mathcal I_4=
\left\{
T^p-T+aT^3+bT^2+cT+d:
(a,b,c,d)\in\mathbf F_p^4
\right\}.
\]
Let \(I_4(p)\) denote the number of irreducible polynomials in this interval.
The subfamily \(a=b=0\) contains exactly \(p-1\) irreducible constant-offset
Artin--Schreier polynomials \(T^p-T+d\), \(d\ne0\).  These do not correspond to
nonconstant Fortunate offsets.  Therefore the \(d=1\) crown is
\[
\boxed{I_4(p)>p-1.}
\]

We next rewrite this inequality in exact nonnegative coordinates.

# 4. Affine normal forms and the exact crown

## 4.1 The quadratic sector

Let
\[
N_2(p)=\operatorname{card}\{d\in\mathbf F_p:T^p+T^2+d\ \text{is irreducible}\}.
\]
Consider the sector \(a=0\), \(b\ne0\).  In
\(T^p-T+bT^2+cT+d\), translation \(T\mapsto T+t\) changes the total
linear coefficient \(c-1\) to \(c-1+2bt\).  Since \(2b\ne0\), exactly
one \(t\in\mathbf F_p\) makes it zero.  The depressed polynomial then has
the form \(T^p+bT^2+d'\).  Monic affine scaling acts by
\[
\lambda^{-1}f(\lambda T)=T^p+(b\lambda)T^2+d'/\lambda,
\]
because \(\lambda^p=\lambda\).  Exactly one nonzero \(\lambda\), namely
\(b^{-1}\), sends the quadratic coefficient to one.  A stabiliser preserving
both the zero linear coefficient and the normalisation \(b=1\) must therefore
have \(t=0\) and \(\lambda=1\).  Thus every irreducible quadratic-tail
orbit has a unique representative \(T^p+T^2+d\), and its orbit has size
\(p(p-1)\).  Adding the \(p-1\) constant Artin--Schreier values gives
\[
I_{a=0}=(p-1)+p(p-1)N_2(p).
\]

## 4.2 The depressed cubic sectors

For \(a\ne0\), translation by \(-b/(3a)\) uniquely removes the quadratic
coefficient.  Write
\[
F_{a,c,d}(T)=T^p+aT^3+cT+d
\]
and
\[
N_a(p)=\operatorname{card}\{(c,d)\in\mathbf F_p^2:F_{a,c,d}\ \text{is irreducible}\}.
\]
For \(\lambda\in\mathbf F_p^*\), monic scaling gives
\[
\lambda^{-1}F_{a,c,d}(\lambda T)
=T^p+(a\lambda^2)T^3+cT+d/\lambda.
\]
It is a coefficient-wise bijection preserving irreducibility.  Hence two
nonzero cubic coefficients give isomorphic depressed slices exactly when
their ratio is a square, and \(N_a(p)\) depends only on
\(A=\chi(a)\in\{+1,-1\}\).  Choose one square and one
nonsquare representative, and denote the corresponding counts by
\(N_{\mathrm{sq}}(p)\) and \(N_{\mathrm{ns}}(p)\).

Every depressed polynomial has exactly \(p\) translates in the full cubic
sector, and each square class contains \((p-1)/2\) nonzero values of \(a\).
Hence
\[
I_{a\ne0}=\frac{p(p-1)}2\bigl(N_{\mathrm{sq}}(p)+N_{\mathrm{ns}}(p)\bigr).
\]

The involution \(T\mapsto-T\), followed by multiplication by \(-1\), sends
\(d\mapsto-d\) and preserves irreducibility.  The fixed locus \(d=0\) is
reducible because the polynomial is divisible by \(T\).  Consequently each
\(N_A(p)\) is even.

## Theorem 4.1 (exact orbit decomposition)

For every prime \(p>3\),
\[
\boxed{
I_4(p)=(p-1)+p(p-1)N_2(p)
+\frac{p(p-1)}2\bigl(N_{\mathrm{sq}}(p)+N_{\mathrm{ns}}(p)\bigr).
}
\]

### Proof

The constant/linear, quadratic and nonzero cubic sectors are disjoint and
exhaust the interval.  The preceding orbit calculations give their respective
contributions.  \(\square\)

Define
\[
\boxed{W_p=N_2(p)+\frac{N_{\mathrm{sq}}(p)+N_{\mathrm{ns}}(p)}2.}
\]
Then Theorem 4.1 becomes
\[
I_4(p)=(p-1)+p(p-1)W_p.
\]

## Corollary 4.2 (exact crown and failure certificate)

The function-field \(d=1\) crown is equivalent to
\[
\boxed{W_p>0.}
\]
A failure prime must satisfy
\[
\boxed{N_2(p)=N_{\mathrm{sq}}(p)=N_{\mathrm{ns}}(p)=0.}
\]

### Proof

The first equivalence follows from \(I_4>p-1\).  The three counts are
nonnegative integers, so \(W_p=0\) is equivalent to their simultaneous
vanishing.  \(\square\)

This is the arithmetic coordinate system used throughout the remainder of the
paper.

# 5. The sparse ordered-root surface

Let \(x_1,\ldots,x_p\) be ordered roots.  The interval condition fixes the first
\(p-4\) elementary symmetric functions.  Because \(1,\ldots,p-4\) are units in
characteristic \(p\), Newton identities give the equivalent affine variety
\[
X_p=\{s_1=s_2=\cdots=s_{p-4}=0\}\subset\mathbf A^p,
\qquad
s_m=\sum_{i=1}^p x_i^m.
\]
It has expected dimension four.

Put
\[
H=\{s_1=0\},\qquad
L=\mathbf A^1(1,\ldots,1),\qquad
W=H/L.
\]
On the nested zero locus, the remaining power sums are invariant under diagonal
translation.  The translation quotient is the affine cone
\[
C_p=\{s_2=s_3=\cdots=s_{p-4}=0\}\subset W
\]
on the projective surface
\[
Y_p=\{s_2=s_3=\cdots=s_{p-4}=0\}
\subset\mathbf P(W)\cong\mathbf P^{p-3}.
\]
The multidegree is
\[
(2,3,\ldots,p-4),
\]
so the expected dimension is two.

## Theorem 5.1 (global smoothness)

For \(p\ge11\), the affine cone
\[
\widetilde Y_p=\{s_1=\cdots=s_{p-4}=0\}\subset\mathbf A^p
\]
has singular locus exactly the diagonal line \(L\).  Consequently
\(Y_p\) is a smooth complete-intersection surface.

### Proof

At a point \(x\), let \(\alpha_1,\ldots,\alpha_r\) be the distinct coordinate
values, with multiplicities \(n_1,\ldots,n_r\).  After multiplying rows by
units, the Jacobian is the truncated Vandermonde matrix
\[
\bigl(x_i^{m-1}\bigr)_{1\le m\le p-4,\ 1\le i\le p},
\]
Columns belonging to equal coordinate values coincide.  After retaining
one column for each distinct value, the column rank is that of the
\((p-4)\times r\) matrix \((\alpha_j^{m-1})\).  Every square minor of
order at most \(\min(r,p-4)\) formed from its first rows is a nonzero
Vandermonde determinant, so the rank is \(\min(r,p-4)\).  The required
Jacobian rank is \(p-4\); a failure therefore requires \(r\le p-5\).

The defining equations give
\[
\sum_{j=1}^r n_j\alpha_j^m=0
\qquad(1\le m\le p-4).
\]
The equation for \(m=0\) also holds in \(\mathbf F_p\), since
\(\sum_jn_j=p=0\).  Taking the first \(r\) equations
\(m=0,\ldots,r-1\), the coefficient matrix is an invertible Vandermonde
matrix.  Thus every \(n_j=0\) in \(\mathbf F_p\).  If \(r\ge2\), then
\(1\le n_j<p\), a contradiction.  Hence \(r=1\), so all coordinates are equal.
Conversely every diagonal point lies on the cone and has deficient Jacobian
rank.  The affine quotient by \(L\) therefore has only its vertex singular, and
projectivisation removes that vertex.  \(\square\)

Throughout the cohomological sections, \(F\) denotes the Frobenius
operator normalised so that its fixed points are the \(\mathbf F_p\)-points
in the Grothendieck--Lefschetz formula and \(\mathbf Q_\ell(-1)\) has
eigenvalue \(p\).  Cohomology is taken with \(\mathbf Q_\ell\)-coefficients
for \(\ell\ne p\).

By weak Lefschetz [@SGA2; @MilneEtale],
\[
H^1(Y_p,\mathbf Q_\ell)=H^3(Y_p,\mathbf Q_\ell)=0,
\]
and
\[
H^2(Y_p,\mathbf Q_\ell)
=\mathbf Q_\ell(-1)\oplus H^2_{\mathrm{prim}}(Y_p,\mathbf Q_\ell).
\]
The symmetric group acts trivially on \(H^0\), the hyperplane line and \(H^4\).
Therefore every nontrivial irreducible \(S_p\)-representation occurs only in
primitive middle cohomology.

# 6. The affine cone transfer and the absolute-Betti obstruction

Sawin's short-interval formalism associates a compactly supported cohomological
constant to the affine ordered-root variety [@Sawin2021].  In the present
interval, this variety is exactly \(X_p\), not an auxiliary compactification.
The translation map
\[
q:X_p\longrightarrow C_p
\]
is an \(S_p\)-equivariant torsor under \(\mathbf A^1\), on which \(S_p\) acts
trivially.  It is Zariski locally the projection
\(U\times\mathbf A^1\to U\).  Since
\(H_c^2(\mathbf A^1,\mathbf Q_\ell)=\mathbf Q_\ell(-1)\) and the other
compactly supported groups vanish, proper base change gives
\[
Rq_!\mathbf Q_\ell\cong\mathbf Q_\ell(-1)[-2].
\]

Let \(\rho\) be a nontrivial ordinary representation of \(S_p\), and put
\[
M_\rho=\operatorname{Hom}_{S_p}
\bigl(\rho,H^2_{\mathrm{prim}}(Y_p,\mathbf Q_\ell)\bigr).
\]
The punctured cone is the \(\mathbf G_m\)-bundle associated to
\(\mathcal O_{Y_p}(-1)\).  Apply the localisation triangle for the zero
section in the total line bundle and the Gysin map given by its first Chern
class.  On a nontrivial \(\rho\)-isotypic component, the cone vertex
contributes nothing and the ambient cohomology of \(Y_p\) is concentrated
in \(M_\rho\subset H^2\).  The resulting two adjacent compactly supported
groups are
\[
H_c^3(C_p)_\rho\cong M_\rho,
\qquad
H_c^4(C_p)_\rho\cong M_\rho(-1).
\]
Tensoring these two groups with
\(H_c^2(\mathbf A^1)=\mathbf Q_\ell(-1)\) shifts degree by two and adds
one Tate twist.  This yields the following exact transfer.

## Theorem 6.1 (nontrivial Sawin-cone transfer)

For every nontrivial \(\rho\),
\[
\boxed{
H_c^5(X_p)_\rho\cong M_\rho(-1),
\qquad
H_c^6(X_p)_\rho\cong M_\rho(-2),
}
\]
and all other \(\rho\)-isotypic compactly supported cohomology groups vanish.
Consequently the relevant absolute Betti constant is
\[
\boxed{B(\rho)=2\dim M_\rho.}
\]

This has an immediate negative consequence.  An exact computer-assisted
primitive-hook reconstruction at \(p=11\) gives
\[
(m_0,\ldots,m_{10})=(0,0,0,0,0,6,14,12,6,3,1).
\]
After removing the sign hook, the primitive non-sign multiplicity mass is
\(41\).  Theorem 6.1 therefore gives
\[
\boxed{B_{\mathrm{mid}}=82>10=p-1.}
\]
Thus the sufficient aggregate strategy based on the bound
\(B_{\mathrm{mid}}\le p-1\) is false for the actual Fortune variety at the
admitted prime \(p=11\).  This refutes an absolute-Betti proof mechanism, not
the crown itself: Frobenius traces can still cancel inside a large cohomology
space.

# 7. The exact sign endpoint

For completeness we record the sign contribution to the full interval.  Write
\[
f_{a,b,u,d}(T)=T^p+aT^3+bT^2+uT+d,
\]
where \(u=c-1\), and extend the quadratic character by \(\chi(0)=0\).  Define
\[
S_{\mathrm{sgn}}(p)=
\sum_{a,b,u,d\in\mathbf F_p}
\chi\bigl(\operatorname{Disc}f_{a,b,u,d}\bigr).
\]

## Theorem 7.1 (sign-hook trace)

For every odd prime \(p>3\),
\[
\boxed{
S_{\mathrm{sgn}}(p)=
\frac{1-\chi(-1)}2\,\chi(-6)\,p^2(p-1).
}
\]
In particular, for \(p\equiv5\pmod6\),
\[
S_{\mathrm{sgn}}(p)=
\begin{cases}
0,&p\equiv5,17\pmod{24},\\
+p^2(p-1),&p\equiv11\pmod{24},\\
-p^2(p-1),&p\equiv23\pmod{24}.
\end{cases}
\]

### Proof

The sector \(a=0\) has total character sum zero after summing over the constant
coefficient.  Assume \(a\ne0\).  The derivative is
\[
g(T)=3aT^2+2bT+u.
\]
Let its roots be \(r,s\), and put \(\delta=b^2-3au\).  As a polynomial in
\(d\), the resultant is
\[
(3a)^p(d+F(r))(d+F(s)),
\qquad
F(T)=T^p+aT^3+bT^2+uT.
\]
For a nonzero scalar \(\kappa\), the standard quadratic-character identity is
\[
\sum_{d\in\mathbf F_p}\chi(\kappa(d-u)(d-v))
=\begin{cases}
(p-1)\chi(\kappa),&u=v,\\
-\chi(\kappa),&u\ne v.
\end{cases}
\]
Indeed, in the first case every term except the double root is the square
class \(\chi(\kappa)\); in the second, translation and scaling reduce to
\(\sum_x\chi(x(x-1))=-1\).  Applying this with
\(\kappa=\varepsilon_p3a\) gives
\((p-1)\chi(\varepsilon_p3a)\) when \(F(r)=F(s)\), and
\(-\chi(\varepsilon_p3a)\) otherwise, where
\(\varepsilon_p=(-1)^{(p-1)/2}\).

Writing \(\Delta=r-s\), direct use of the symmetric functions of \(r,s\)
gives
\[
F(r)-F(s)=\Delta^p-\frac a2\Delta^3.
\]
For \(\delta\ne0\), one has \(\Delta^p=\chi(\delta)\Delta\), so the collision
condition is
\[
2\delta=9a\chi(\delta).
\]
For fixed \(a\), the number of nonzero collision values is
\[
n(a)=\mathbf1_{\chi(2a)=1}+\mathbf1_{\chi(-2a)=-1},
\]
and every \(\delta\) has exactly \(p\) preimages \((b,u)\).  The fixed-\(a\)
contribution is therefore
\[
p^2\chi(\varepsilon_p3a)n(a).
\]
If \(\chi(-1)=1\), then \(n(a)=1\) and the remaining character sum over
\(a\) vanishes.  If \(\chi(-1)=-1\), the two conditions coincide; on the
\((p-1)/2\) contributing values one has \(\chi(a)=\chi(2)\).  Since then
\(\varepsilon_p=-1\), the sum is \(\chi(-6)p^2(p-1)\).  \(\square\)

# 8. Alternating hooks and the \(p\)-cycle projector

Let \(V\) be a finite-dimensional characteristic-zero \(S_p\)-representation
with an endomorphism \(F\) commuting with \(S_p\).  Put
\[
M_i=\operatorname{Hom}_{S_p}(\wedge^i\operatorname{Std},V).
\]
Character projection gives
\[
\sum_i(-1)^i\operatorname{Tr}(F\mid M_i)
=
\frac1{p!}\sum_{g\in S_p}
\det(1-g\mid\operatorname{Std})\operatorname{Tr}(Fg\mid V).
\]
If the cycle lengths of \(g\) are \(\lambda_1,\ldots,\lambda_r\), then
\[
\det(1-tg\mid\operatorname{Std})
=\frac{\prod_j(1-t^{\lambda_j})}{1-t}.
\]
At \(t=1\) this vanishes unless \(g\) is one \(p\)-cycle, when it equals
\(p\).  The class has \((p-1)!\) elements, and all its elements are conjugate.
Its total scalar in the projector is explicitly
\[
\frac{p(p-1)!}{p!}=1.
\]
Thus the character value, class size and projector denominator cancel
exactly.

## Theorem 8.1 (alternating-hook projector)

For any \(p\)-cycle \(\sigma\),
\[
\boxed{
\sum_{i=0}^{p-1}(-1)^i\operatorname{Tr}(F\mid M_i)
=\operatorname{Tr}(F\sigma\mid V).
}
\]
There is no missing factor of \(p\).

# 9. Fixed points and exact circularity

The safe fixed-point calculation is on the affine variety \(X_p\).  Let
\(F(x)=x^p\) on geometric points and let
\(\sigma=(1\ 2\ \cdots\ p)\).  An \(F\sigma\)-fixed tuple is uniquely
of the form
\[
(\alpha,F\alpha,\ldots,F^{p-1}\alpha)
\]
for some \(\alpha\in\mathbf F_{p^p}\).  The degree of \(\alpha\) over
\(\mathbf F_p\) divides the prime \(p\), so it is one or \(p\).

- Degree \(p\) produces an irreducible polynomial in \(\mathcal I_4\), and each
  irreducible contributes \(p\) choices of the first root.
- Degree one gives the diagonal tuples and the \(p\) polynomials
  \((T-a)^p=T^p-a\).

## Theorem 9.1 (exact fixed-point count)

\[
\boxed{\operatorname{card}\operatorname{Fix}(F\sigma\mid X_p)=pI_4(p)+p.}
\]
The extra \(p\) is the prime-power correction.  Equivalently,
\[
\sum_{f\in\mathcal I_4}\Lambda(f)=pI_4+p.
\]

Let
\[
S_{\mathrm{sgn}}=s_pp^2(p-1),
\qquad s_p\in\{0,+1,-1\},
\]
and let \(T_{\mathrm{mid}}\) be the alternating primitive hook trace after
removing the trivial and sign endpoints.  The affine cone transfer gives
\[
E_{\mathrm{mid}}=p(p-1)T_{\mathrm{mid}},
\]
while the complete decomposition is
\[
pI_4+p=p^4+s_pp^2(p-1)+p(p-1)T_{\mathrm{mid}}.
\]
Solving and using Theorem 4.1 yields
\[
\boxed{
T_{\mathrm{mid}}=p\bigl(W_p-(p+1+s_p)\bigr).
}
\]
Therefore
\[
T_{\mathrm{mid}}>-p(p+1+s_p)
\quad\Longleftrightarrow\quad
W_p>0.
\]

## Corollary 9.2 (fixed-point circularity)

The one-sided primitive trace inequality obtained from the alternating-hook
\(p\)-cycle fixed locus is exactly equivalent to the function-field crown.  It
is not a smaller analytic target.

This is a useful obstruction theorem: it prevents a fixed-point rewrite from
being mistaken for progress while retaining the \(p\)-cycle trace as a possible
location for genuinely new cancellation.

# 10. The q-line cell system

We now resolve the two depressed cubic coefficient classes into one geometric
q-line family.  Fix \(a\ne0\), put \(A=\chi(a)\), and consider
\[
F_{a,c,d}(X)=X^p+aX^3+cX+d.
\]
For \(c\ne0\), define
\[
q=-\frac3c,
\qquad
r=-\frac{c}{3a}=\frac1{aq},
\qquad
\varepsilon=\chi(r)=A\chi(q).
\]
Choose a fixed nonsquare \(\eta\).

If \(\varepsilon=+1\), choose \(\lambda^2=r\).  Scaling \(X=\lambda Z\)
and dividing by \(\lambda\) gives the split normal form
\[
G_{q,+,\delta}(Z)
=Z^p+q^{-1}Z^3-3q^{-1}Z+\delta.
\]
If \(\varepsilon=-1\), write \(r=\eta s^2\); the corresponding rational
nonsplit form is
\[
G_{q,-,\delta}(Z)
=Z^p+(\eta q)^{-1}Z^3-3q^{-1}Z+\delta.
\]
In both cases the constant parameter map is bijective and irreducibility is
preserved.  Let
\[
I_\varepsilon(q)=
\operatorname{card}\{\delta\in\mathbf F_p:G_{q,\varepsilon,\delta}\ \text{irreducible}\}.
\]
The locus \(c=0\) is denoted \(q=\infty\).  Then
\[
N_A=I_A(\infty)+I_{A\chi(2)}(2)
+\sum_{q\in\mathbf F_p^*\setminus\{2\}}I_{A\chi(q)}(q).
\]

For \(q\ne2\), multiply the split form by \(q\) and write the constant as
\(-(q-2)t\).  The resulting ordered-root cover lies over
\[
U_q=\mathbf P^1_t\setminus\{+1,-1,\infty\}.
\]
Let \(\mathcal L_{i,\varepsilon}\) be the local system associated to the hook
representation \(\wedge^i\operatorname{Std}\) in the split or nonsplit
arithmetic reading, and define the alternating virtual module
\[
\mathcal H_{q,\varepsilon}
=\sum_{i=0}^{p-1}(-1)^i
H_c^1(U_{q,\overline{\mathbf F}_p},\mathcal L_{i,\varepsilon}),
\qquad
E_\varepsilon(q)=\operatorname{Tr}(F\mid\mathcal H_{q,\varepsilon}).
\]
The hook character has trace \(p\) on an irreducible fibre and zero on every
other cycle type.  Its generic virtual rank is zero, \(H_c^0=0\), and the sole
invariant line contributes \(H_c^2=\mathbf Q_\ell(-1)\).  Grothendieck--Lefschetz
therefore gives
\[
\boxed{pI_\varepsilon(q)=p-E_\varepsilon(q)\qquad(q\ne2).}
\]

Define the boundary count
\[
B_A=I_A(\infty)+I_{A\chi(2)}(2)
\]
and the two global q-line projectors
\[
S_0=
\sum_{q\ne0,2}\bigl(E_+(q)+E_-(q)\bigr),
\]
\[
S_\chi=
\sum_{q\ne0,2}\chi(q)\bigl(E_+(q)-E_-(q)\bigr).
\]
For each generic \(q\), the selected reading satisfies
\[
E_{A\chi(q)}(q)=\frac12\Bigl(E_+(q)+E_-(q)
+A\chi(q)(E_+(q)-E_-(q))\Bigr).
\]
Summing over the \(p-2\) values \(q\in\mathbf F_p^*\setminus\{2\}\)
gives \(\tfrac12(S_0+A S_\chi)\).  Substituting
\(I_\varepsilon(q)=1-E_\varepsilon(q)/p\) into the finite cell assembly
yields the exact ledger.

## Theorem 10.1 (q-line class projectors)

For \(A\in\{+1,-1\}\),
\[
\boxed{
N_A=(p-2)+B_A-\frac{S_0+A S_\chi}{2p}.
}
\]
Thus \(S_0\) is the invariant class-sum trace and \(S_\chi\) is the quadratic
anti-invariant class-difference trace.  They are not two unrelated geometric
families.

# 11. Saturation equals the cubic count

Adding the two formulas in Theorem 10.1 eliminates the anti-invariant trace:
\[
N_{\mathrm{sq}}+N_{\mathrm{ns}}=2(p-2)+B_{\mathrm{sq}}+B_{\mathrm{ns}} -\frac{S_0}{p}.
\]
Define the formal saturation value
\[
S_0^{\mathrm{sat}}
=p\bigl(2(p-2)+B_{\mathrm{sq}}+B_{\mathrm{ns}}\bigr).
\]

## Theorem 11.1 (saturation-defect identity)

\[
\boxed{S_0^{\mathrm{sat}}-S_0=p(N_{\mathrm{sq}}+N_{\mathrm{ns}}).}
\]
In particular,
\[
S_0^{\mathrm{sat}}-S_0\in2p\mathbf Z_{\ge0},
\]
and
\[
S_0<S_0^{\mathrm{sat}}
\quad\Longleftrightarrow\quad
N_{\mathrm{sq}}+N_{\mathrm{ns}}>0.
\]

### Proof

The identity is the class-sum ledger multiplied by \(p\).  Nonnegativity gives
the weak inequality.  The parity follows from the fixed-point-free involution
\(d\mapsto-d\) on each irreducible depressed class.  \(\square\)

Because each boundary irreducible is included in its complete class count,
\(0\le B_A\le N_A\).  Under hypothetical saturation, both cubic counts and
both boundary counts vanish, so the failure value simplifies to
\[
S_0=2p(p-2).
\]
Combining with the quadratic sector,
\[
\boxed{
W_p=N_2+\frac{S_0^{\mathrm{sat}}-S_0}{2p}.
}
\]
Therefore when \(N_2=0\), strict invariant q-line nonsaturation is exactly the
full crown.  A useful q-line theorem must supply genuinely new one-sided
Frobenius information; divisibility, parity or integrality already contained in
the ledger cannot distinguish zero from a positive \(2p\)-multiple.

# 12. Exact computation and reproducibility

Every uniform statement presented above as proved is established symbolically in the manuscript. The computations in this section are independent regression checks or explicitly finite computer-assisted certificates; they are not used to extrapolate a theorem from finitely many primes.

A clean-room implementation written for this manuscript exhaustively tests
irreducibility in the full \(p^4\) interval at \(p=5,7,11\) using the
prime-degree Frobenius criterion.  It obtains

- At \(p=5\): \(I_4=124\), \(N_2=1\), \(N_{\mathrm{sq}}=4\), \(N_{\mathrm{ns}}=6\), and \(W_p=6\).
- At \(p=7\): \(I_4=426\), \(N_2=1\), \(N_{\mathrm{sq}}=10\), \(N_{\mathrm{ns}}=8\), and \(W_p=10\).
- At \(p=11\): \(I_4=1660\), \(N_2=1\), \(N_{\mathrm{sq}}=14\), \(N_{\mathrm{ns}}=14\), and \(W_p=15\).

It also checks the alternating-hook character on every cycle type for every
prime up to \(11\).  A separate C++ program enumerates all
\(7^7=823543\) affine root vectors at \(p=7\); among the \(5047\) points of
the sparse cone, exactly the seven diagonal points are singular.

Additional finite-prime censuses may be included in the reproducibility package. Such results are exact only at their listed primes and do not replace the missing uniform theorem.

The supporting package includes:

- the frozen source manifest and claim-status ledger;
- the independent reconstruction note;
- the Python irreducibility and hook-character verifier;
- the independent C++ singular-locus verifier;
- machine-readable outputs and SHA-256 checksums.

# 13. Exact frontier

The results reduce the function-field \(d=1\) problem to exact nonnegative coordinates, but do not prove their universal nonvanishing.

Several natural mechanisms are closed as independent reductions.

1. **Aggregate absolute Betti control.** For the actual affine short-interval variety, the exact transfer of Theorem 6.1 and the computer-assisted \(p=11\) hook reconstruction give \(B_{\mathrm{mid}}=82>10=p-1\). Thus the proposed sufficient inequality \(B_{\mathrm{mid}}\le p-1\) is false at an admitted prime.
2. **Alternating-hook fixed-point control.** Theorem 9.1 and Corollary 9.2 show that the corresponding one-sided primitive trace inequality is exactly equivalent to \(W_p>0\); the fixed-point rewrite does not weaken the crown.
3. **Congruence-only q-line nonsaturation.** Theorem 11.1 gives
   \[
   S_0^{\mathrm{sat}}-S_0=p(N_{\mathrm{sq}}+N_{\mathrm{ns}}),
   \]
   so integrality, parity and divisibility already present in the ledger cannot distinguish zero from the first positive admissible value.

The exact crown is
\[
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2}>0.
\tag{13.1}
\]
Equivalently, when \(N_2=0\), the remaining cubic problem is strict invariant q-line nonsaturation. A successful continuation must therefore provide genuinely new one-sided Frobenius or arithmetic information that excludes the simultaneous zero state; another exact change of coordinates is not progress unless it weakens that requirement.

The universal function-field crown remains open. No theorem in this article implies the integer Fortune conjecture.

# AI-assistance disclosure

Large language models were used for literature triage, symbolic and computational cross-checking, adversarial review, software drafting and editorial assembly. Proved, computer-assisted, conjectural and open statements are separated explicitly. The named author takes responsibility for the mathematics, citations, code and final presentation.

# Data and code availability

The reproducibility package contains the independent finite-field reconstruction, irreducibility and hook-character verifier, singular-locus verifier, machine-readable outputs, source manifest and checksums. None of these files is required to read the symbolic proofs in the manuscript. Exact finite outputs are not extrapolated into a uniform theorem.
