---
title: |
  Bilateral Endpoint Incidences over Finite Fields
subtitle: |
  Defect rigidity, Frobenius orientation, and quadratic emptiness
author:
  - "Edward Stewart Anthony Bozzard (ORCID 0009-0002-4052-0994)"
date: "31 July 2026"
lang: en-GB
abstract: |
  The function-field Fortune programme developed in Papers V and VI reduces
  one degree-one crown to exact nonvanishing problems on sparse polynomial
  families and quotient varieties.  A separate source--orbit route leads to a
  bilateral endpoint incidence among four irreducible moduli.  This paper
  consolidates that incidence theory through its first complete
  nonzero-defect existence theorem.

  We first remove all modular inverses and express simultaneous endpoint
  contact as four polynomial divisibilities.  When the field size q is prime
  and q exceeds the common modulus degree k, the associated quotient
  polynomials possess a unique common defect h of degree at most q-2k.
  The zero-defect locus is exactly the union of the translation and reflection
  families.  It follows that this classification is complete when q<2k, that
  the intermediate strip k<q<2k is empty, and that genuinely new components
  can occur only when q>=2k.  An explicit cubic incidence at (q,k)=(11,3)
  proves that the new components do occur.

  We then distinguish the bounded-degree algebraic relaxation from the
  arithmetic incidence: the relaxation records the values forced by a cyclic
  root ordering but not the requirement that the ordering is the Frobenius
  cycle.  Its geometric dimension therefore does not control the arithmetic
  count.  Finally, for every odd prime power q, we give a computer-assisted
  exact proof that no cross-distinct bilateral endpoint incidence exists at
  k=2.  A faithful four-equation reduction is covered by two open charts; exact
  ideal-membership certificates force a single component on which both
  quadratic discriminants are squares, contradicting irreducibility.

  The remaining existence problem is precisely 3<=k<q with q>=2k.  Its
  decisive arithmetic input is a twisted-Frobenius point theorem, not further
  dimension calculations on the relaxation.  No endpoint dispersion theorem,
  function-field crown, or integer Fortune conjecture is proved.
keywords: ["finite fields", "irreducible polynomials", "Frobenius orientation", "computer-assisted proof", "incidence geometry", "Fortune's conjecture"]
bibliography: references.bib
link-citations: true
reference-section-title: References
---

# 1. Introduction

Papers V and VI of the Fortune programme study the degree-one
function-field crown through exact normal forms, sparse ordered-root geometry,
secondary traces and quotient constructions [@BozzardPaperV; @BozzardPaperVI].
They isolate several rigorous nonvanishing formulations but do not prove the
universal crown.  Subsequent work pursued a logically different route: the
centred source--orbit second moment associated with a completed
function-field detector.  Its endpoint expansion produces a simultaneous
incidence between two ordered pairs of irreducible moduli.

The new incidence problem is not merely another presentation of the Kummer
quotient from Paper VI.  It is an independent transference architecture.  This
distinction matters for the publication lineage.  Every proved construction in
Paper VI remains valid, but its final statement should now be read as terminal
*within the secondary-trace and quotient route*.  The bilateral route creates
a new exact theorem sequence and therefore warrants a separate paper rather
than a revision that retrofits later material into Paper VI.

The purpose of this paper is to freeze the stable part of that sequence.  It
does not report every attempted attack.  Four layers are retained:

1. inverse-free algebraisation of bilateral endpoint contact;
2. the common-defect dichotomy and the complete zero-defect classification;
3. the distinction between a q-uniform algebraic relaxation and true
   Frobenius-oriented points;
4. the all-odd-q quadratic emptiness theorem.

The principal theorem obtained here is the first complete existence result for
the nonzero-defect programme.

> **Quadratic emptiness theorem.**  For every odd prime power q, there is no
> cross-distinct simultaneous bilateral endpoint incidence with modulus degree
> k=2.

The theorem is computer-assisted in a precise algebraic sense.  The reduction
to four equations is certified at the ideal level; the open locus is covered
by two localisation charts; characteristic-zero membership certificates have
explicit lift matrices; their denominator support is finite; and every
exceptional odd characteristic is checked directly.  The final contradiction
is elementary: the surviving component makes both quadratic discriminants
literal squares.

The paper also records two corrections that prevent a misleading research
narrative.  First, the once-proposed implication q>k => emptiness is false:
the first cubic counterexample occurs at (11,3).  Second, positive dimension
of the bounded-degree relaxation does not imply a large incidence count.  The
relaxation drops Frobenius orientation, and its quadratic analogue is
positive-dimensional while its true arithmetic locus is empty for every odd
q.

Throughout, statuses are separated as proved by hand, exact
computer-assisted, finite computation, withdrawn, and open.  No finite census
is promoted to a uniform theorem.

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
for some \(c,d\in\mathbf F_q\).  We call it **cross-distinct** when the
same-modulus diagonal strata and the cross contacts excluded below are absent.
The terminology reflects the second-moment origin of the system; the
incidence theory itself is purely algebraic.

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

Introduce quotient polynomials \(A,B,C,D\).  After putting
\[
\lambda=-\theta/c,\qquad \rho=\theta/d
\]
for nonzero witnesses, the four equations may be written
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

For the remainder of Sections 4--6, assume that \(q\) is an odd prime,
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

## Theorem 5.1 (zero-defect classification)

Assume \(h=0\).  Then \(\rho=\lambda\), hence \(c+d=0\), and the incidence
belongs to exactly one of the following families.

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

This theorem corrects the earlier interpretation of the two families.  They
are not the whole incidence scheme; they are exactly its zero-defect part.

## Corollary 5.2 (forced zero defect)

If \(q<2k\), then \(h=0\).  Consequently every cross-distinct incidence in
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

The incidence is covariant under the affine group.  For
\(a\in\mathbf F_q^\times\), \(b\in\mathbf F_q\), apply
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

# 10. Relation to Papers V and VI

The publication lineage is as follows.

Paper V proves the exact \(d=1\) crown coordinate
\[
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2}
\]
and shows that several natural cohomological and q-line formulations are
algebraically equivalent to its positivity.  Paper VI constructs secondary
integral carriers and quotient geometry for that same nonvanishing problem.
Those theorems remain intact.

The present paper does not supersede their mathematical statements.  It
supersedes only an editorial implication: Paper VI's one-sided
Kummer-quotient theorem is not the only conceivable continuation of the
function-field programme.  The centred source--orbit architecture yields a
different endpoint incidence and a new theorem sequence.

Accordingly:

- Paper VI is **valid and retained**;
- its terminal theorem is **terminal within its route**;
- Paper VII is a **corrective sequel**, not a replacement;
- no theorem here proves \(W_p>0\) or the universal \(d=1\) crown;
- no theorem here transfers to the integer Fortune conjecture without an
  explicit transference theorem.

# 11. The remaining existence frontier

Combining the exact results gives the following regime table.

| Regime | Status |
|---|---|
| \(k=2\), odd prime powers \(q\) | empty |
| \(k<q<2k\), odd primes \(q\) | empty |
| \(k\ge q\), odd primes \(q\) | translation/reflection classification, with transpose contact at \(k=q\) |
| \(3\le k<q,\ q\ge2k\) | open |

The open region begins with the cubic nonzero-defect components.  The
appropriate next theorem is not a dimension statement for the q-uniform
relaxation.  It is a componentwise count of true Frobenius-oriented points.

A useful cubic theorem would take the form
\[
\#V^{\mathrm{true}}_3(\mathbf F_q)=O(1)
\]
after affine normalisation, or an explicit periodic classification of that
count.  Restoring the affine orbit would then give \(O(q^2)\) ordered
incidences.  A weaker \(O(q)\) normalised count would give \(O(q^3)\) raw
incidences and would require cancellation in the literal endpoint amplitude.

This existence theorem is only the first remaining gate.  The following are
also open:

1. the corrected centred bilateral identity with both Gram diagonals removed;
2. the literal \(\Delta_{PS}\) amplitude on every component;
3. affine-orbit amplitude covariance and cancellation;
4. the endpoint function-field prime-output estimate;
5. frequency restoration, conductor coupling and thinning;
6. every transfer to the integer Fortune conjecture.

# 12. Reproducibility

The computer-assisted theorem is accompanied by:

- the four-equation reduction;
- the two characteristic-zero chart scripts;
- direct lift verifiers for both charts;
- an independent exact rational re-expansion of the lift matrices;
- the ideal-level faithfulness certificate;
- direct exceptional-characteristic certificates;
- a frozen run log and claim-status ledger.

The release verifier reruns the chart identities over \(\mathbf Q\), checks
faithfulness, reruns the exceptional characteristics, verifies the
discriminant-square identities symbolically, and checks that every manuscript
claim is classified in the ledger.

A finite cubic census is included only as a regression and as motivation for
the twisted-Frobenius theorem.  It is not used in the proof of Theorem 9.1.

# 13. Boundary

The stable contribution of this paper is:

- an exact inverse-free coefficient scheme;
- the common-defect theorem;
- a complete classification of zero defect;
- emptiness of the intermediate strip;
- an explicit nonzero-defect cubic counterexample;
- a precise relaxation-versus-orientation distinction;
- the all-odd-q quadratic emptiness theorem.

The following earlier statements are withdrawn:

- universal \(q>k\) emptiness;
- universal \(c+d=0\);
- the use of relaxation dimension as a decision gate for the incidence count;
- the inference that a tangent curve would by itself create \(q^3\)-scale
  true incidence.

The next permitted research target is the cubic twisted-Frobenius point
theorem.  Further Gröbner calculations, tangent jets or relaxation point
counts are secondary unless they enter a proof of that arithmetic theorem.

No function-field crown, endpoint dispersion theorem or integer Fortune
conjecture is claimed.

## AI-assistance disclosure

The research programme used large language models for structured derivation,
software drafting, adversarial review, exact-computation design and editorial
assembly.  Every result labelled as proved is supported by a complete hand
argument or a reproducible exact algebraic certificate.  Human-proof,
computer-assisted, finite empirical, withdrawn and open claims are separated
in the accompanying ledger.  The named author takes responsibility for the
mathematics, code, citations and final presentation.

## Data and code availability

The manuscript, source-fidelity audit, exact certificate scripts,
machine-readable outputs, review records and release checks are maintained in
the public repository `digitalgoldfisj79/multi-agent-environment`.  Frozen
commit identifiers and file hashes are recorded in the release manifest.

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
