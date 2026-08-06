
The cross contacts \(P=S'\) and \(S=P'\) are impossible in this range.  For
example, if \(P=S'\), the second inverse-free equation gives
\[
P'\mid (L+\lambda)P.
\]
Since \(P'\ne P\), this forces \(P'\mid L+\lambda\), contradicting
\(\deg P'=k<q\).  The other case is symmetric.

## Theorem 4.1 (common-defect theorem)

Every cross-distinct incidence has a unique polynomial \(h\) satisfying
\[
\rho C-\lambda B=hPS',
\]
\[
\rho A-\lambda D=hSP',
\]
and
\[
hPP'SS'
=
L(\rho SS'-\lambda PP')+\lambda\rho(PS-P'S').
\]
Moreover,
\[
\deg h\le q-2k.
\]

### Proof

Substitute the first two quotient equations into the third.  Direct
elimination gives
\[
L(\rho C-\lambda B)S+
(\lambda L^2-\rho CA-\lambda^2\rho)P=0.
\]
Coprimality implies
\[
P\mid \rho C-\lambda B.
\]
The reverse substitution gives
\[
S'\mid \rho C-\lambda B.
\]
As \(P\) and \(S'\) are distinct, their product divides the same difference:
\[
\rho C-\lambda B=h_1PS'.
\]
The symmetric calculation gives
\[
\rho A-\lambda D=h_2SP'.
\]

Multiplying the first identity by \(P'S\), and the second by \(PS'\),
shows that both sides expand to
\[
L(\rho SS'-\lambda PP')+\lambda\rho(PS-P'S').
\]
The polynomial ring is a domain, hence \(h_1=h_2=:h\), and the product
identity follows.  Finally, the quotient differences have degree at most
\(q\), while \(PS'\) and \(SP'\) have degree \(2k\); therefore
\(\deg h\le q-2k\).  Uniqueness is immediate. \(\square\)

The polynomial \(h\) is the **bilateral defect**.  It separates the
previously observed elementary families from the genuinely new large-field
geometry.

# 5. Zero-defect rigidity

## Theorem 5.1 (zero-defect classification over prime fields)

Under the standing assumptions that \(q\) is an odd prime and \(q>k\), assume
\(h=0\).  Then \(\rho=\lambda\), hence \(c+d=0\), and the incidence belongs
to one of the following families.

**Translation family.**  There is a polynomial \(R\) such that
\[
P'=P+LR,\qquad
S=P+\lambda R,\qquad
S'=S+LR.
\]

**Reflection family.**  There is a polynomial \(Q\) such that
\[
P'=LQ-P,\qquad
S=P+\lambda Q,\qquad
S'=LQ-S.
\]

### Proof

The leading coefficients of
\(\rho C-\lambda B=0\) give \(\rho=\lambda\).  Thus \(C=B\) and, from the
second defect equation, \(A=D\).  The definitions of \(\lambda,\rho\) give
\(c+d=0\).

Eliminating the prime moduli from the quotient equations now yields
\[
AB=L^2-\lambda^2=(L-\lambda)(L+\lambda).
\]
For nonzero \(\lambda\), both factors are monic irreducible
Artin--Schreier polynomials of degree \(q\).  Since \(A\) and \(B\) are monic
of degree \(q\), unique factorisation gives
\[
\{A,B\}=\{L-\lambda,L+\lambda\}.
\]

If \(A=L-\lambda\), the first quotient equation gives the translation
relations after defining the residual polynomial \(R\).  If
\(A=L+\lambda\), it gives the reflection relations after defining \(Q\).
The remaining quotient equations force the displayed formulas for \(S'\).
\(\square\)

This classification is not asserted for non-prime odd prime powers; in that
setting the factorisation of \(L^2-\lambda^2\) can have additional components.

This theorem corrects the earlier interpretation of the two families.  They
are not the whole incidence scheme; they are exactly its zero-defect part.

## Corollary 5.2 (forced zero defect in the prime large-field strip)

Under the standing assumptions that \(q\) is an odd prime and \(q>k\), if
\(q<2k\), then \(h=0\).  Consequently every cross-distinct incidence in
that range is translation or reflection, apart from the separately explicit
transpose contact when \(k=q\).

### Proof

The degree bound in Theorem 4.1 gives
\(\deg h\le q-2k<0\), hence \(h=0\).  Apply Theorem 5.1. \(\square\)

## Corollary 5.3 (empty intermediate strip)

If
\[
k<q<2k,
\]
then there is no cross-distinct bilateral endpoint incidence.

### Proof

Corollary 5.2 forces the translation/reflection classification.  In either
family a nonzero polynomial multiplied by \(L\) must have degree at most
\(k\), impossible because \(\deg L=q>k\). \(\square\)

The genuinely new region is therefore
\[
q\ge2k,\qquad k\ge3.
\]

# 6. Nonzero defect and affine normalisation

The first nonzero-defect example occurs over \(\mathbf F_{11}[t]\) at
\(k=3\):
\[
P=t^3+4t^2+1,\qquad
S=t^3+10t^2+9t+1,
\]
\[
P'=t^3+10t^2+6t+7,\qquad
S'=t^3+4t^2+3t+10.
\]
All four cubics are distinct and irreducible.  With
\[
\theta=1,\qquad c=2,\qquad d=8,
\]
one has
\[
\lambda=5,\qquad \rho=7,
\]
so \(c+d\ne0\) and \(\lambda\ne\rho\).  Direct evaluation of the original
local frequencies gives
\[
\mu P'-\mu'P=2,\qquad
\nu S'-\nu'S=8.
\]
The common defect is
\[
h=2t^5+5t^4+6t^2+6t+4,
\]
with the maximal possible degree
\[
\deg h=5=q-2k.
\]
Thus neither \(q>k\Rightarrow\) emptiness nor universal \(c+d=0\) is true.

The incidence is covariant under the affine group.  For \(a\in\mathbf F_q^\times\), \(b\in\mathbf F_q\), apply
\[
