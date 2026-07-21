# Exact low-degree factor incidence in the d=1 cubic slice

**Date:** 2026-07-21  
**Status:** proved.

## 1. Setup

Let \(p\ge5\) be prime, \(a\in\mathbf F_p^*\), and

\[
F_{c,d}(X)=X^p+aX^3+cX+d,
\qquad (c,d)\in\mathbf F_p^2.
\]

For a squarefree polynomial \(F\), write \(
u_k(F)\) for the number of monic irreducible degree-\(k\) factors of \(F\).

## 2. Every irreducible quadratic is compatible

### Theorem LI.1

Let

\[
h_{s,n}(X)=X^2-sX+n
\]

be monic irreducible over \(\mathbf F_p\). There is exactly one pair \((c,d)\) for which \(h_{s,n}\mid F_{c,d}\), namely

\[
oxed{
c=1-a(s^2-n),
\qquad
d=s(an-1).
}
\]

Consequently

\[
oxed{
\sum_{c,d\in\mathbf F_p}
u_2(F_{c,d})
=rac{p(p-1)}2.
}
\]

### Proof

In the quotient by \(h_{s,n}\),

\[
X^2=sX-n,
\qquad
X^3=(s^2-n)X-sn.
\]

If \(	heta\) is a root, Frobenius exchanges the two conjugates, so

\[
	heta^p=s-	heta.
\]

Therefore, modulo \(h_{s,n}\),

\[
X^p+aX^3
=igl[-1+a(s^2-n)igr]X+igl[s-asnigr].
\]

The displayed \(c,d\) are the unique coefficients cancelling this linear remainder. Uniqueness also follows because a degree-\(\ge2\) polynomial cannot divide a nonzero linear polynomial.

There are exactly \((p^2-p)/2=p(p-1)/2\) monic irreducible quadratics. Summing one incidence for each gives the second statement. QED.

## 3. Frobenius-collinearity criterion

Let \(h\) be monic irreducible of degree \(k\ge3\), let \(	heta\) be one of its roots, and put

\[
y=	heta^p+a	heta^3.
\]

### Lemma LI.2

The polynomial \(h\) divides some \(F_{c,d}\) if and only if

\[
oxed{
\det
egin{pmatrix}
1&	heta&y\\
1&	heta^p&y^p\\
1&	heta^{p^2}&y^{p^2}
\end{pmatrix}=0.
}
\]

When this holds, \(c,d\) are unique.

### Proof

If \(h\mid F_{c,d}\), then every conjugate point

\[
(	heta^{p^j},y^{p^j})
\]

lies on the \(\mathbf F_p\)-line \(Y=-cX-d\), so the determinant vanishes.

Conversely, the first two conjugate points have distinct \(X\)-coordinates because \(k\ge3\). Let \(L\) be their affine line. Vanishing of the determinant places the third point on \(L\). Frobenius sends \(L\) to the line through the second and third points, which is again \(L\). Thus \(L\) is Frobenius-stable and has equation \(Y=-cX-d\) with \(c,d\in\mathbf F_p\). Hence \(F_{c,d}(	heta)=0\), and irreducibility of \(h\) gives \(h\mid F_{c,d}\). QED.

## 4. Exactly one compatible cubic per translation orbit

Let \(h\) be monic irreducible cubic with Frobenius-ordered roots

\[
	heta_0=	heta,\qquad
	heta_1=	heta^p,\qquad
	heta_2=	heta^{p^2}.
\]

Set

\[
e_1=	heta_0+	heta_1+	heta_2,
\qquad
e_2=	heta_0	heta_1+	heta_0	heta_2+	heta_1	heta_2,
\]

and

\[
V=(	heta_1-	heta_0)(	heta_2-	heta_0)(	heta_2-	heta_1).
\]

The Frobenius permutation is a 3-cycle, so \(V\in\mathbf F_p^*\).

### Lemma LI.3

The compatibility determinant of Lemma LI.2 equals

\[
oxed{
3e_2-e_1^2+a e_1V.
}
\]

### Proof

For degree three, \(	heta_3=	heta_0\). Expanding the determinant separates it into

\[
\det(1,	heta_i,	heta_{i+1})
+a\det(1,	heta_i,	heta_i^3).
\]

The first determinant is

\[
3e_2-e_1^2,
\]

while the alternating cubic determinant is

\[
V(	heta_0+	heta_1+	heta_2)=Ve_1.
\]

QED.

Translate every root by \(t\in\mathbf F_p\). Then

\[
e_1(t)=e_1+3t,
\qquad
e_2(t)=e_2+2te_1+3t^2,
\qquad V(t)=V.
\]

Hence

\[
3e_2(t)-e_1(t)^2=3e_2-e_1^2
\]

and the compatibility determinant becomes

\[
C_h(t)=C_h(0)+3aVt.
\]

Because \(3aV
e0\), there is exactly one \(t\in\mathbf F_p\) for which \(C_h(t)=0\).

### Theorem LI.4

Every translation orbit of monic irreducible cubics contains exactly one polynomial dividing a member of the slice \(F_{c,d}\). Consequently

\[
oxed{
\sum_{c,d\in\mathbf F_p}
u_3(F_{c,d})
=rac{p^2-1}{3}.
}
\]

### Proof

The calculation above gives exactly one compatible translate per orbit. Translation acts freely on monic irreducible cubics for \(p\ge5\): a nonzero translation-invariant root set would contain a full additive orbit of size \(p\), impossible for a cubic.

The number of monic irreducible cubics is

\[
rac{p^3-p}{3}.
\]

Every translation orbit has size \(p\), so the number of orbits, and therefore the number of compatible cubics, is

\[
rac{p^3-p}{3p}=rac{p^2-1}{3}.
\]

Each compatible cubic contributes one degree-3 factor incidence. QED.

## 5. Sieve interpretation

The first two unconditioned incidence levels are therefore exact:

\[
\sum_{c,d}
u_2(F_{c,d})
=rac{p^2}{2}+O(p),
\qquad
\sum_{c,d}
u_3(F_{c,d})
=rac{p^2}{3}+O(1).
\]

These are precisely the degree-2 and degree-3 cycle-density main terms expected from random factorization, but here they follow from elementary algebra and Frobenius geometry.

For the parity-breaking sieve, the next quantities are their locally admissible and discriminant-weighted versions:

\[
L_{a,k}=
\sum_{(c,d)\in\mathcal A_a}
u_k(F_{c,d}),
\]

\[
L_{a,k}^{\chi}=
\sum_{(c,d)\in\mathcal A_a}
\chi(\operatorname{Disc}F_{c,d})\,
u_k(F_{c,d}),
\qquad k=2,3.
\]

Theorems LI.1 and LI.4 reduce both to fixed two-variable character sums. Proving

\[
L_{a,2}=rac{p^2}{6}+O(p^{3/2}),
\qquad
L_{a,3}=rac{p^2}{9}+O(p^{3/2})
\]

and corresponding signed estimates is now a finite Weil-sum problem. Sharpening those errors to \(O(p)\), and extending the incidence control multiplicatively, is the next sieve layer.
