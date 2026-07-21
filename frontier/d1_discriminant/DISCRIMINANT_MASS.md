# Exact discriminant and locally admissible Möbius mass for the d=1 cubic slices

**Date:** 2026-07-21  
**Status:** the full-slice discriminant formulas and the local-admissibility lemmas below are proved algebraically and independently machine-checked.

> **Convention correction.** For
> \(F_{a,c,d}(X)=X^p+aX^3+cX+d\), evaluation on \(\mathbf F_p\) gives
> \(F_{a,c,d}(x)=a x^3+(c+1)x+d\). Therefore the correct local
> admissibility condition is that \(aX^3+(c+1)X+d\) is rootless, not
> \(aX^3+cX+d\). The earlier diagnostic restriction without the `+1`
> was misindexed. The complete-slice theorems were unaffected; all local
> statements in this revision use the canonical convention.

## 1. Setup

Let \(p\ge5\) be prime, \(a\in\mathbf F_p^*\), and

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad c,d\in\mathbf F_p.
\]

Write \(\chi\) for the quadratic character of \(\mathbf F_p\), extended by
\(\chi(0)=0\), and put

\[
s_p=(-1)^{(p-1)/2}.
\]

## 2. Exact discriminant formula

### Theorem DM.1

For \(c\ne0\), put

\[
\varepsilon_c=\chi\!\left(-\frac{c}{3a}\right).
\]

Then

\[
\boxed{
\operatorname{Disc}(F_{a,c,d})
=s_p\left(3ad^2+c\left(\varepsilon_c+\frac{2c}{3}\right)^2\right).
}
\]

For \(c=0\),

\[
\boxed{
\operatorname{Disc}(F_{a,0,d})=s_p\,3ad^2.
}
\]

### Proof

In characteristic \(p\),

\[
F'_{a,c,d}(X)=3aX^2+c.
\]

Let \(u^2=-c/(3a)\). For \(c\ne0\),
\(u^p=\varepsilon_cu\), and

\[
au^3+cu=\frac{2c}{3}u.
\]

Hence

\[
F(u)=d+\left(\varepsilon_c+\frac{2c}{3}\right)u,
\qquad
F(-u)=d-\left(\varepsilon_c+\frac{2c}{3}\right)u.
\]

Since

\[
\operatorname{Res}(F,F')=(3a)^pF(u)F(-u)=3aF(u)F(-u)
\]

and

\[
\operatorname{Disc}(F)=(-1)^{p(p-1)/2}\operatorname{Res}(F,F'),
\]

the formula follows. The case \(c=0\) is immediate.

## 3. Exact complete-slice mass

Define

\[
M_a(p)=\sum_{c,d\in\mathbf F_p}
\chi\bigl(\operatorname{Disc}(F_{a,c,d})\bigr).
\]

Put \(\delta_a=\chi(2a)\). Then

### Theorem DM.2

\[
\boxed{
M_a(p)=
\begin{cases}
p\chi(3a),&p\equiv1\pmod4,\\
-2p\chi(3a),&p\equiv3\pmod4\text{ and }\chi(2a)=1,\\
0,&p\equiv3\pmod4\text{ and }\chi(2a)=-1.
\end{cases}}
\]

The number of zero discriminants in the complete slice is

\[
\boxed{
Z_a(p)=
\begin{cases}
p-\chi(2a),&p\equiv1\pmod4,\\
p,&p\equiv3\pmod4.
\end{cases}}
\]

For fixed \(c\), the discriminant is \(Ad^2+B_c\), with \(A=s_p3a\).
The standard quadratic-character sum in \(d\), followed by the elementary
classification of the values of \(c\) for which \(B_c=0\), gives both
formulas.

By Pellet's formula, because \(p\) is odd,

\[
\sum_{c,d}\mu(F_{a,c,d})=-M_a(p).
\]

## 4. Correct local admissibility

Set

\[
H_{a,c,d}(X)=aX^3+(c+1)X+d.
\]

For every \(x\in\mathbf F_p\),

\[
F_{a,c,d}(x)=H_{a,c,d}(x).
\]

Thus absence of linear factors of \(F_{a,c,d}\) is exactly rootlessness of
\(H_{a,c,d}\).

### Theorem LA.1 — local admissibility forces squarefreeness

If \(H_{a,c,d}\) has no root in \(\mathbf F_p\), then

\[
\operatorname{Disc}(F_{a,c,d})\ne0.
\]

#### Proof

Suppose \(F\) has a repeated root \(\beta\). From \(F'(\beta)=0\),

\[
\beta^2=-\frac{c}{3a}\in\mathbf F_p,
\]

so \(\beta\in\mathbf F_{p^2}\).

If \(\beta\in\mathbf F_p\), then \(H(\beta)=F(\beta)=0\), contradicting
local admissibility.

Otherwise \(\beta^p=-\beta\). Writing \(t=\beta^2\), the equation
\(F(\beta)=0\) becomes

\[
(-1+at+c)\beta+d=0.
\]

Since \(1,\beta\) are linearly independent over \(\mathbf F_p\), one has
\(d=0\). But then \(H(0)=0\), again a contradiction. Therefore a locally
admissible member is squarefree.

This is stronger than the earlier numerical observation: the restricted
zero-discriminant count is identically zero for every \(p\ge5\) and every
\(a\ne0\).

## 5. Exact number of locally admissible cubics

Write a locally admissible cubic in monic form

\[
q_{u,v}(X)=X^3+uX+v,
\qquad
u=(c+1)/a,\quad v=d/a.
\]

Let

\[
\rho=\chi(-3).
\]

### Theorem LA.2 — uniform fixed-\(u\) count

For every \(u\ne0\),

\[
\boxed{
\#\{v:q_{u,v}\text{ is irreducible}\}=\frac{p-\rho}{3}.
}
\]

For \(u=0\),

\[
\boxed{
\#\{v:X^3+v\text{ is irreducible}\}
=\frac{(1+\rho)(p-1)}{3}.
}
\]

Consequently

\[
\boxed{
\#\{(c,d):H_{a,c,d}\text{ is rootless}\}
=\frac{p^2-1}{3}.
}
\]

#### Proof for \(u\ne0\)

Consider \(\phi_u(x)=x^3+ux\). For each output value, the fibre size is the
number of roots of \(X^3+uX+v\). Ordered collisions with distinct inputs are
controlled by

\[
\phi_u(x)=\phi_u(y),\quad x\ne y
\iff x^2+xy+y^2=-u.
\]

The nondegenerate binary quadratic form on the right has exactly
\(p-\rho\) solutions for nonzero right-hand side. Removing the diagonal and
combining the zeroth, first and second fibre moments gives

\[
n_0=\frac{p-\rho}{3},
\]

independently of the square class of \(-u/3\). Here \(n_0\) is the number
of output values with empty fibre. Those output values are precisely the
irreducible cubics. The case \(u=0\) follows from whether the cube map is
bijective or has image of index three.

## 6. Restricted discriminant mass and factor parity

Define

\[
\mathcal A_a=\{(c,d):H_{a,c,d}\text{ is rootless over }\mathbf F_p\}
\]

and

\[
M_a^{\mathrm{loc}}(p)=
\sum_{(c,d)\in\mathcal A_a}
\chi\bigl(\operatorname{Disc}(F_{a,c,d})\bigr).
\]

By Theorem LA.1 every summand is \(\pm1\). Therefore the exact numbers of
locally admissible members with square and nonsquare discriminant are

\[
\boxed{
N_{a,+}=\frac12\left(\frac{p^2-1}{3}+M_a^{\mathrm{loc}}(p)\right),
\qquad
N_{a,-}=\frac12\left(\frac{p^2-1}{3}-M_a^{\mathrm{loc}}(p)\right).
}
\]

Pellet's formula identifies these with odd and even factor parity,
respectively. In particular, every irreducible member lies in the `+`
class, while a locally admissible reducible member in that class has at
least three irreducible factors.

## 7. Exact complete-sum decomposition

Let

\[
\Delta(u,v)=-4u^3-27v^2,
\]

and define

\[
D_a(u,v)=\operatorname{Disc}
\bigl(F_{a,\,au-1,\,av}\bigr).
\]

Put

\[
S_a=\sum_{u,v}\chi(D_a(u,v)),
\]

\[
C_a=\sum_{u,v}\chi(\Delta(u,v))\chi(D_a(u,v)),
\]

\[
R_a=\sum_{x,u}\chi\bigl(D_a(u,-x^3-ux)\bigr),
\]

and

\[
\tau_a=\chi(D_a(0,0)).
\]

### Theorem LA.3 — exact restricted-mass identity

\[
\boxed{
M_a^{\mathrm{loc}}(p)=\frac{2S_a+C_a-R_a-\tau_a}{3}.
}
\]

Moreover \(S_a=M_a(p)\), so the first term is already known exactly from
Theorem DM.2.

#### Proof

For \(q_{u,v}=X^3+uX+v\), let \(r(u,v)\) be its number of distinct roots in
\(\mathbf F_p\). The exact irreducibility indicator is

\[
\mathbf1_{q_{u,v}\ \mathrm{irred}}
=
\frac{2+\chi(\Delta(u,v))-r(u,v)
-\mathbf1_{(u,v)=(0,0)}}{3}.
\]

For squarefree cubics this is the three-way Frobenius-cycle classification;
for singular cubics the final correction handles the triple-root case.
Multiplying by \(\chi(D_a(u,v))\) and summing gives the displayed identity.
The root-incidence term is exactly \(R_a\).

This replaces the vague “discriminant mass” proposal by two explicit
complete character sums, \(C_a\) and \(R_a\), plus known elementary terms.

## 8. Trace–norm form over \(\mathbf F_{p^3}\)

Let \(K=\mathbf F_{p^3}\). For \(\alpha\in K\) with
\(\operatorname{Tr}(\alpha)=0\), \(\alpha\ne0\), put

\[
u_\alpha=-\frac12\operatorname{Tr}(\alpha^2),
\qquad
v_\alpha=-\operatorname{Norm}(\alpha).
\]

Then \(X^3+u_\alpha X+v_\alpha\) is the minimal polynomial of \(\alpha\),
and each irreducible depressed cubic occurs exactly three times. Hence

\[
\boxed{
M_a^{\mathrm{loc}}(p)
=
\frac13
\sum_{\substack{\alpha\in K^*\\\operatorname{Tr}(\alpha)=0}}
\chi\bigl(D_a(u_\alpha,v_\alpha)\bigr).
}
\]

This is the canonical trace–norm form for comparison with prescribed
trace/norm and Kloosterman literature.

## 9. Algebraic-geometric next target

For \(c\ne0\), write

\[
\operatorname{Disc}(F)=s_p\{P(c,d)+\chi(-c/(3a))Q(c)\},
\]

where

\[
P(c,d)=3ad^2+c+\frac49c^3,
\qquad
Q(c)=\frac43c^2.
\]

The identity

\[
\chi(P+\eta Q)
=
\frac12\left[
\chi(P+Q)+\chi(P-Q)
+\eta\{\chi(P+Q)-\chi(P-Q)\}
\right]
\]

for \(\eta=\pm1\) converts the nested character into ordinary Kummer
character sums. Thus \(C_a\) and \(R_a\) are finite combinations of
complete, fixed-degree character sums on two-dimensional varieties.

The next proof target is a uniform bound

\[
C_a,R_a=O(p)
\]

through a geometric nondegeneracy analysis. That would give the rigorous
parity-equidistribution statement

\[
M_a^{\mathrm{loc}}(p)=O(p),
\qquad
N_{a,\pm}=\frac{p^2}{6}+O(p).
\]

This does not alone prove irreducibility, but it is precisely compatible
with a reducible-count or RQM assembly: any proof that the locally
admissible members with at least three factors are fewer than \(N_{a,+}\)
would force an irreducible member.

## 10. Reproducibility

Run

```bash
python frontier/d1_discriminant/discriminant_mass_check.py
```

The verifier uses only the Python standard library and checks the
pointwise discriminant formula, complete-slice formulas, local
squarefreeness, the fixed-\(u\) count, and the exact restricted-mass
identity.