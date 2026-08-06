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
  These defect results are stated only for odd prime q.  The zero-defect locus
  is exactly the union of the translation and reflection families.  Within the
  range q>k, it follows that the intermediate strip k<q<2k is empty and that
  genuinely new components can occur only when q>=2k.  An explicit cubic incidence at (q,k)=(11,3)
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
