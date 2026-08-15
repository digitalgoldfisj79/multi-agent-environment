---
title: "Bilateral Endpoint Incidences over Finite Fields"
subtitle: "Defect rigidity, Frobenius orientation, and quadratic emptiness"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "11 August 2026"
lang: en-GB
bibliography: references.bib
link-citations: true
reference-section-title: References
---

**Abstract.** We study a simultaneous bilateral endpoint incidence among four distinct irreducible polynomials of common degree over finite fields. The local formulation initially contains modular inverses; we remove them exactly and express simultaneous contact as four polynomial divisibilities. For odd prime field size \(q\) with \(q>k\), the quotient polynomials possess a unique common defect \(h\) of degree at most \(q-2k\). The zero-defect locus is exactly the union of translation and reflection families, implying that the intermediate strip \(k<q<2k\) is empty. An explicit incidence over \(\mathbf F_{11}\) at \(k=3\) shows that nonzero-defect components genuinely occur.

We distinguish the bounded-degree algebraic relaxation from the arithmetic incidence: the relaxation retains value identities associated with a cyclic ordering but does not impose that this ordering is the Frobenius cycle. Its dimension therefore cannot determine the true incidence count. For modulus degree \(k=2\), a faithful q-free four-equation reduction and a two-chart exact ideal-membership certificate force all arithmetic-open solutions onto a component where both quadratic discriminants are squares, contradicting irreducibility. This gives a computer-assisted exact quadratic-emptiness theorem over every odd prime power. The accompanying Lean development kernel-checks the q-free power-lift identities and the chart-selection/discriminant logic; the full datum-to-normal-form reduction remains represented by one explicit custom normalization axiom, so the Lean theorem is not axiom-free.

The remaining arithmetic region is \(3\le k<q\) with \(q\ge2k\). The next relevant problem is a twisted-Frobenius point theorem on the true oriented components, not another dimension calculation on the relaxation. No function-field crown, endpoint dispersion theorem, or integer Fortune theorem is proved.

**Keywords:** finite fields; irreducible polynomials; Frobenius orientation; computer-assisted proof; incidence geometry.

# 1. Scope and theorem roadmap

Let \(\mathbf F_q[t]\) be a polynomial ring of odd characteristic. This paper studies an algebraic incidence that arises naturally when two endpoint contacts are imposed simultaneously on two ordered pairs of irreducible moduli. The incidence theory is treated here as an independent finite-field problem: no prior function-field Fortune manuscript is needed for its definitions or proofs, and no theorem below is asserted to transfer to the integer Fortune conjecture.

There are four layers.

1. The modular inverses are removed exactly, producing a bounded-degree coefficient scheme.
2. In odd prime fields with \(q>k\), a common bilateral defect gives a sharp zero-defect classification and an empty intermediate strip.
3. The q-uniform root-cycle relaxation is separated from the true Frobenius-oriented arithmetic locus; an explicit cubic example proves that nonzero-defect components exist.
4. At \(k=2\), exact algebraic certificates plus a discriminant contradiction prove emptiness over every odd prime power.

The quadratic theorem is computer-assisted in the algebraic-certificate sense, not a finite census. Its mathematical proof package contains the faithful reduction, chart cover, ideal-membership certificates and exceptional-characteristic checks. The formal Lean package currently has a narrower trust boundary: it verifies the q-free chart identities and downstream contradiction but still assumes the genuine-incidence-to-certified-normal-form reduction through the single ledgered axiom `p7_k2_certified_normalization`.

# 2. Bilateral endpoint incidence

Let \(\mathbf F_q[t]\) be a polynomial ring over a finite field of odd
characteristic.  Let \(P,S,P',S'\) be monic irreducible polynomials of common
degree \(k\), with
\[
P\ne P',\qquad S\ne S'.
\]
Let \(L\) be coprime to all four moduli and let
\(\theta\in\mathbf F_q^\times\).  Define the four local completion
frequencies
\[
\mu=-\theta(LS)^{-1}\pmod P,\qquad
\mu'=-\theta(LS')^{-1}\pmod {P'},
\]
\[
\nu=-\theta(LP)^{-1}\pmod S,\qquad
\nu'=-\theta(LP')^{-1}\pmod {S'}.
\]
The representatives are chosen with degree less than \(k\).

At source degree \(2k-1\), the two endpoint contacts are scalar if
\[
E_\mu=\mu P'-\mu'P\in\mathbf F_q,\qquad
E_\nu=\nu S'-\nu'S\in\mathbf F_q.
\]
A simultaneous bilateral incidence is a tuple for which
\[
E_\mu=c,\qquad E_\nu=d
\]
for some \(c,d\in\mathbf F_q\).  We call it **cross-distinct** when
\[
P,S,P',S'\quad\text{are pairwise distinct}.
\]
Thus this term excludes the pair diagonals \(P=S\), \(P'=S'\), the
same-source contacts \(P=P'\), \(S=S'\), and the cross contacts
\(P=S'\), \(S=P'\).  The terminology reflects the second-moment origin of
the system; the incidence theory itself is purely algebraic.

# 3. Inverse-free algebraisation

The modular inverses in the definition are useful analytically but obscure the
geometry.  They can be removed exactly.

## Theorem 3.1 (inverse-free equivalence)

For \(c\in\mathbf F_q\),
\[
E_\mu=c
\]
if and only if
\[
P\mid cLS+\theta P',\qquad
P'\mid cLS'-\theta P.
\]
Similarly, for \(d\in\mathbf F_q\),
\[
E_\nu=d
\]
if and only if
\[
S\mid dLP+\theta S',\qquad
S'\mid dLP'-\theta S.
\]
The witnesses \(c\) and \(d\) are unique.

### Proof

Assume \(E_\mu=c\).  Reduction modulo \(P\) gives
\(\mu P'=c\).  Since \(\mu=-\theta(LS)^{-1}\pmod P\), this is equivalent to
\[
cLS+\theta P'\equiv0\pmod P.
\]
Reduction modulo \(P'\) gives \(-\mu'P=c\), equivalently
\[
cLS'-\theta P\equiv0\pmod {P'}.
\]

Conversely, the two divisibilities imply that
\[
\mu P'-\mu'P-c
\]
vanishes modulo both \(P\) and \(P'\).  Because the moduli are distinct
degree-\(k\) irreducibles, \(PP'\) divides this polynomial.  Its degree is
strictly less than \(2k\), so it is zero.  The proof for \(E_\nu\) is
identical.  Uniqueness follows from the displayed identities. \(\square\)

For a cross-distinct incidence the witnesses are automatically nonzero.  If,
for example, \(E_\mu=0\), then \(\mu P'=\mu'P\).  Since \(P\) and
\(P'\) are distinct irreducibles of degree \(k\) while
\(\deg\mu,\deg\mu'<k\), divisibility forces \(\mu=\mu'=0\), contrary
to \(\theta\ne0\).  The same argument applies to \(E_\nu\).

Introduce quotient polynomials \(A,B,C,D\).  We may therefore put
\[
\lambda=-\theta/c,\qquad \rho=\theta/d.
\]
The four equations may be written
\[
AP=LS-\lambda P',\qquad
BS=LP+\rho S',
\]
\[
CP'=LS'+\lambda P,\qquad
DS'=LP'-\rho S.
\]
This formulation will be used throughout.  It is a coefficient scheme of
bounded algebraic degree once the quotient coefficients are included.

# 4. The common defect

**Prime-field scope.**  For the remainder of Sections 4--6, assume that \(q\) is an odd prime,
\[
L=t^q-t,
\]
and \(q>k\).  The primality hypothesis is retained because the zero-defect
classification uses the degree-\(q\) Artin--Schreier factors
\(L\pm\lambda\).

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
t\longmapsto at+b
\]
to all four root sets.  Then
\[
\lambda\longmapsto a\lambda,\qquad
\rho\longmapsto a\rho,
\]
and
\[
h(t)\longmapsto a^{2-2k}h((t-b)/a).
\]
When \(q\ge2k\), so the characteristic exceeds \(k\), every orbit has a
unique gauge representative satisfying
\[
\lambda=1,\qquad [t^{k-1}]P=0.
\]
The dilation is forced by \(\lambda\), and the translation is forced by the
trace coefficient of \(P\).  The raw incidence count therefore contains an
exact \(q(q-1)\) affine factor before the remaining finite cyclic root
rotations are considered.

A bounded-degree root formulation is also available.  Choose ordered root
cycles
\[
\alpha,\beta,\alpha',\beta'
\]
of length \(k\).  On the root-separation open locus, the four divisibilities
are equivalent to
\[
(\alpha_{i+1}-\alpha_i)\prod_j(\alpha_i-\beta_j)
 =\lambda\prod_j(\alpha_i-\alpha'_j),
\]
\[
(\alpha'_{i+1}-\alpha'_i)\prod_j(\alpha'_i-\beta'_j)
 =-\lambda\prod_j(\alpha'_i-\alpha_j),
\]
\[
(\beta_{i+1}-\beta_i)\prod_j(\beta_i-\alpha_j)
 =-\rho\prod_j(\beta_i-\beta'_j),
\]
\[
(\beta'_{i+1}-\beta'_i)\prod_j(\beta'_i-\alpha'_j)
 =\rho\prod_j(\beta'_i-\beta_j),
\]
for \(i\) modulo \(k\).  These equations have degree at most \(k+1\),
independent of \(q\).

# 7. The relaxation is not the arithmetic locus

The bounded-degree root equations must be interpreted correctly.  They retain
the value identity
\[
L(x_i)=x_{i+1}-x_i
\]
that follows when the ordering is a Frobenius cycle.  They do **not** impose
\[
x_{i+1}=x_i^q.
\]
Consequently they define one q-uniform algebraic variety \(V_k\), reduced in
different characteristics, whereas a true incidence is a point of \(V_k\)
whose four orderings have the required Frobenius orientation.

This distinction invalidates an inference that initially appeared plausible:
the geometric dimension of \(V_k\) does not determine the incidence count.
It may control the size of the relaxation while saying little about its
twisted-Frobenius fixed points.

For \(k=3\), complete enumerations of the oriented-coefficient relaxation give

| \(q\) | \(\#V_3(\mathbf F_q)\) | irreducible nondegenerate | true | orientation-spurious |
|---:|---:|---:|---:|---:|
| 11 | 12,261 | 4 | 2 | 2 |
| 13 | 20,857 | 8 | 0 | 8 |
| 17 | 47,823 | 22 | 2 | 20 |

The true column matches the independent incidence census after affine
normalisation.  These are exact finite measurements, not a uniform theorem.

The quadratic analogue makes the logical point decisive.  Its q-uniform
relaxation is nonempty over an algebraic closure and has
\[
q^2+2(q-2)
\]
rational points on the tested prime panels, including positive-dimensional
degenerate and split components, while the true incidence set is empty.  The
next section proves the emptiness uniformly.

The correct general problem is therefore a **twisted-Frobenius point
theorem**: classify or bound the points on the relevant components whose root
orderings are the actual Frobenius cycles.

# 8. Quadratic reduction

Let \(q\) now be an arbitrary odd prime power and set \(k=2\).  After
translation and homothety normalisation, write
\[
P=t^2+A,\qquad
S=t^2+Bt+C,\qquad
U=\rho.
\]
A true cross-distinct incidence maps into a q-free four-equation system
\[
f_0(A,B,C,U)=f_1(A,B,C,U)
=f_2(A,B,C,U)=f_3(A,B,C,U)=0.
\]
The explicit polynomials are recorded in Appendix A and in the certificate
source.  The reduction is faithful on \(U\ne0\): after adjoining an inverse
of \(U\), the ideal generated by these four polynomials agrees with an
independently derived incidence ideal in both directions.

The open conditions required at a true incidence are
\[
U\ne0,\qquad A\ne0,\qquad B^2-4C\ne0,
\]
and
\[
P\ne S.
\]
The last condition is equivalent to
\[
B\ne0\quad\text{or}\quad A-C\ne0.
\]
Thus the open locus is covered by two charts.

Define the target component
\[
T=\bigl(U-1,\ B+2,\ (A-C)^2+4A\bigr).
\]

## Lemma 8.1 (two-chart containment; exact computer-assisted)

In every odd characteristic, every point of the open four-equation locus lies
on \(T\).

### Certificate

For the \(B\)-chart, adjoin
\[
z\,U\,A\,(B^2-4C)\,B-1.
\]
For the \(A-C\)-chart, adjoin
\[
z\,U\,A\,(B^2-4C)\,(A-C)-1.
\]
Over \(\mathbf Q\), a standard basis on each chart reduces all three
generators of \(T\) to zero.  Singular also produces explicit lift matrices
\(M\) such that
\[
T=K M,
\]
where \(K\) is the corresponding five-generator chart ideal.  An independent
exact rational-arithmetic verifier re-expands both matrix identities.

Across the two lift matrices, the prime support of all denominators is
\[
\{2,3,5,7,11,31,163\}.
\]
Therefore the identities specialise to every odd characteristic outside
\[
\{3,5,7,11,31,163\}.
\]
For each of these six exceptional odd primes, direct standard-basis
certificates on both charts again reduce the three target generators to zero.
This proves the containment in every odd characteristic.

The computation is an exact ideal-membership proof.  It does not infer a
uniform statement from sampled solutions. \(\square\)

The q-free chart identities entering this argument have subsequently been regenerated as exact power-lift certificates and checked in Lean; Section 12 states precisely which normalization step remains outside the kernel.

# 9. The quadratic emptiness theorem

## Theorem 9.1 (quadratic emptiness)

For every odd prime power \(q\), there is no cross-distinct simultaneous
bilateral endpoint incidence at modulus degree \(k=2\).

### Proof

Suppose a true incidence exists.  By the faithful reduction and the two-chart
cover, Lemma 8.1 gives
\[
U=1,\qquad B=-2,\qquad (A-C)^2+4A=0.
\]
Put
\[
r=A-C.
\]
Then
\[
A=-\frac{r^2}{4}.
\]
The discriminant of \(P=t^2+A\) is
\[
\operatorname{disc}(P)=-4A=r^2.
\]
Also \(C=A-r\), so
\[
\operatorname{disc}(S)=B^2-4C
=4-4C
=4-4A+4r
=(r+2)^2.
\]
Both discriminants are squares in \(\mathbf F_q\).  Therefore both
quadratics split over \(\mathbf F_q\), contradicting their irreducibility.
\(\square\)

The theorem converts the previously observed empty census into a
characteristic-uniform law.  It is also the first complete existence theorem
for the nonzero-defect endpoint programme.

# 10. Scope relative to Fortune-type nonvanishing problems

The bilateral incidence can occur inside a broader function-field investigation of Fortune-type prime-output questions, but the present theorem sequence is logically independent of the normal-form and quotient constructions used in other approaches. In particular, quadratic endpoint emptiness does not imply positivity of any separate function-field crown, and the explicit cubic incidence does not by itself provide an endpoint dispersion estimate.

Accordingly, this article makes only the following scope claims:

- the incidence definitions and all hand proofs are local to this manuscript;
- the quadratic theorem is an exact computer-assisted incidence theorem with the formal trust boundary described in Section 12;
- no theorem here proves a universal function-field Fortune statement;
- no theorem here transfers to the integer Fortune conjecture without a separate transference theorem.

# 11. Remaining existence frontier

The results proved here give the following self-contained regime summary.

| Regime | Status in this paper |
|---|---|
| \(k=2\), odd prime powers \(q\) | empty by Theorem 9.1 |
| \(k<q<2k\), odd primes \(q\) | empty by Corollary 5.3 |
| \(3\le k<q,\ q\ge2k\) | open; explicit nonzero-defect cubic examples exist |

The range \(q\le k\) is not classified in this manuscript and is not needed for Theorem 9.1 or the intermediate-strip result.

The open region begins with cubic nonzero-defect components. The appropriate next theorem is not a dimension statement for the q-uniform relaxation. It is a componentwise count or classification of points whose cyclic root orderings are the actual Frobenius cycles. A useful cubic theorem would, after affine normalisation, prove a bounded or explicitly periodic count of true oriented points; restoring the affine orbit would then convert this to an incidence bound.

Even such an existence theorem would be only one gate in a larger endpoint-dispersion programme. The literal endpoint amplitudes, affine-orbit cancellation, frequency restoration and any transfer to an integer problem remain separate questions. None is asserted here.

# 12. Reproducibility and formal trust boundary

The computer-assisted quadratic theorem is accompanied by the q-free four-equation reduction, two localisation charts, exact ideal-membership data, faithfulness checks, exceptional-characteristic certificates, and symbolic discriminant-square verification. These are algebraic certificates rather than sampled-solution evidence. The finite cubic censuses in Section 7 are regression and motivation only.

A subsequent formal-assurance pass separated the certificate calculation from the normalization theorem more sharply. Six q-free power-lift identities—three target identities on each chart—were regenerated with exact denominator clearing and checked by the Lean kernel over integer multivariate polynomials. The chart-selection theorem taking those six identities to the certified component is also kernel checked. A compact rational lift has denominator-prime support contained in \(\{2,3,5\}\); the original direct characteristic certificates cover the exceptional odd characteristics needed by the mathematical proof package.

The Lean formalization should nevertheless be described precisely. It does **not** yet prove Theorem 9.1 from Mathlib alone. The file `FortuneFormal/Frontier/Assumptions.lean` contains the single custom axiom

`p7_k2_certified_normalization`,

whose content is the remaining genuine-incidence-to-certified-q-free-normal-form reduction. From that axiom the kernel derives the discriminant contradiction and the quadratic emptiness statement. Thus:

- the q-free polynomial certificate layer is kernel checked;
- the chart-selection and discriminant contradiction are kernel checked;
- the full formal theorem remains `DERIVED_WITH_LEDGERED_AXIOM`, not axiom-free;
- the manuscript's computer-assisted theorem continues to rely on the independently reproducible normalization/faithfulness proof package until that reduction is formalised.

No finite computation is promoted to a uniform theorem merely by testing primes.

# 13. Boundary

The stable contribution of this paper is:

- an exact inverse-free coefficient scheme;
- the common-defect theorem;
- a complete zero-defect classification for odd prime \(q>k\);
- emptiness of the intermediate strip \(k<q<2k\);
- an explicit nonzero-defect cubic incidence;
- a precise relaxation-versus-Frobenius-orientation distinction;
- an exact computer-assisted quadratic-emptiness theorem for every odd prime power.

The following stronger statements are explicitly not claimed: universal \(q>k\) emptiness; universal \(c+d=0\); control of true incidence counts from relaxation dimension; a function-field crown; an endpoint dispersion theorem; or the integer Fortune conjecture.

The next mathematically meaningful target is the cubic twisted-Frobenius point theorem. Further Gröbner calculations or relaxation point counts are useful only insofar as they enter such an arithmetic proof.

# AI-assistance disclosure

Large language models were used for structured derivation, software drafting, adversarial review, exact-computation design, formal-assurance work and editorial assembly. Human-proof, computer-assisted, formally kernel-checked, finite empirical and open claims are distinguished explicitly. The named author takes responsibility for the mathematics, code, citations and final presentation.

# Data and code availability

The reproducibility package contains the source-fidelity audit, certificate scripts, q-free power-lift identities, Lean formalisation, machine-readable outputs, review records and release checks. Frozen commit identifiers and file hashes are recorded in the publication support manifest.

# Appendix A. The quadratic four-equation system

With variables \(A,B,C,U\), the faithful q-free reduction is generated by
\[
\begin{aligned}
f_0={}&-4A^2BU+6A^2B-2A^2U+4A^2+4AB^3+4AB^2U+2AB^2\\
&+4ABCU-8ABC-4AC+2BC^2+2C^2U,
\end{aligned}
\]
\[
\begin{aligned}
f_1={}&-4A^2U+4A^2+2AB^2+6ABU-2AB+8ACU-8AC\\
&-2B^2C-2BCU-2BC-4C^2U+4C^2,
\end{aligned}
\]
\[
\begin{aligned}
f_2={}&-2A^2B-2A^2U-2AB^3U-AB^3-2AB^2U^2-2AB^2U\\
&+4ABCU+4ACU^2-B^3C-2B^2CU-4BC^2U+2BC^2\\
&-4C^2U^2+2C^2U,
\end{aligned}
\]
\[
\begin{aligned}
f_3={}&4A^2U-4A^2+2AB^2U-4AB^2-2ABU^2-2ABU\\
&-8ACU+8AC-B^4-2B^3U-2B^2CU+4B^2C\\
&-2BCU^2+6BCU+4C^2U-4C^2.
\end{aligned}
\]
The two chart ideals are obtained by adjoining respectively
\[
zUA(B^2-4C)B-1
\]
and
\[
zUA(B^2-4C)(A-C)-1.
\]
