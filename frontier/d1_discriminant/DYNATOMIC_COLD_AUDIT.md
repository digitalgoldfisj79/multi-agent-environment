# Cold audit of the fixed-period dynatomic package

**Date:** 2026-07-21  
**Status:** core Morton inputs and committed ramification certificates independently checked; full publication audit still open.

## 1. Scope

This audit addresses the load-bearing inputs used in the simultaneous factor-degree 2--5 sieve:

1. full wreath-product monodromy for the unicritical family;
2. linear disjointness of distinct dynatomic periods;
3. transfer from the unicritical specialization to the generic centered two-parameter family;
4. independence of the local cubic field from periods 2--5;
5. the computational ramification certificates.

It does not claim to be a line-by-line publication audit of every Lang--Weil twist or Kummer argument.

## 2. Primary-source check

Bridy and Garton, *Dynamically Distinguishing Polynomials* (2017), explicitly record the following consequences of Morton's *Galois Groups of Periodic Points* (1998):

- for `f(X)=X^k+c` over `Q(c)`, the nth dynatomic Galois group is the full wreath product
  `C_n wr S_(r_k(n))`;
- for distinct periods n and n', the corresponding splitting fields are linearly disjoint.

Their discussion attributes the wreath-product statement to Morton's Theorems B and 9 and the cross-period disjointness to Morton's Theorem D.

For k=3 this gives the exact specialized inputs used for periods 2,3,4,5.

### Audit verdict

The repository's use of Morton for the unicritical specialization is supported by the published secondary statement and is not an invented theorem attribution.

A final paper should cite Morton's original theorem text directly as well as Bridy--Garton.

## 3. Transfer to the centered two-parameter family

The generic centered family is

`g_(c,d)(X)=X^3+cX+d`.

Specializing `c=0` gives the unicritical family `X^3+d`.

For a separable specialization, the specialized Galois group embeds into the generic group. On the other hand, dynamical cycle structure gives the universal upper bound

`G_n <= C_n wr S_(r_3(n))`.

Since the specialization already attains this full upper bound, the generic group is also full.

For several periods, the generic compositum is a subgroup of the product of the period groups. Morton's specialized compositum attains the full direct product. Therefore the generic compositum also has the full direct-product group.

### Audit verdict

The specialization sandwich is logically sound provided separability at the generic point of the specialization is stated. The committed audits establish the required separability for the periods actually used.

## 4. Independent rerun of ramification certificates

Hugging Face job:

`6a5fb698d09dc1f57c6bfc8a`

The three committed Sage scripts were downloaded afresh from the branch and executed in a clean Sage container.

### Periods 2 and 3

`mixed_dynatomic_local_audit.sage` returned:

- period-2 degree 6, derivative gcd degree 0;
- period-3 degree 24, derivative gcd degree 0;
- the chosen parameter lies on the local discriminant divisor.

### Period 4

`quartic_factorial_audit.sage` returned:

- dynatomic degrees `(72,24)` in `(X,d)`;
- discriminant factor metadata `[(4,2),(4,3),(16,4),(24,4)]`;
- gcd of the local branch polynomial with the full dynatomic discriminant equal to 1.

### Period 5

`quintic_local_audit.sage` returned:

- dynatomic degree 240;
- derivative gcd degree 0 at the selected local-discriminant point.

All three scripts passed exactly as claimed.

### Audit verdict

The computational claims that the local discriminant divisor is not a ramification component of the period-2,3,4,5 dynatomic product are independently reproduced.

## 5. Kummer and signed-moment layer

The signed arguments use raw degree-p discriminant classes with branch components among

`c=0`, `Fplus=0`, `Fminus=0`.

The intended argument is that each raw Kummer field has a branch component not present in the dynatomic/local compositum. This excludes containment and keeps every signed twist geometrically nontrivial.

The local root cover has odd degree three, so a nonsquare in the base function field cannot become a square after pullback.

### Audit verdict

The field-theoretic mechanism is correct. The remaining publication task is to present, for every raw class, one explicit smooth generic point of its branch divisor where the dynatomic/local compositum is unramified. The current files give the ingredients but compress this verification too aggressively.

## 6. Fixed versus growing period

The audit supports the package only for a fixed finite set of periods.

For fixed S, all covers, fibre powers, exceptional loci, and Lang--Weil constants have fixed complexity. Nothing in Morton or in the finite ramification audits supplies uniform control when

`S={2,...,floor(p/3)}`.

The fixed-set theorem is therefore a sound consolidation target, but it does not address the crown's growing-period obstruction.

## 7. Overall verdict

Current classification:

- **Supported by primary-source theorem:** unicritical wreath monodromy and cross-period disjointness.
- **Sound algebraic transfer:** maximal monodromy and direct-product monodromy for the generic centered family at each fixed finite set of periods.
- **Independently machine-reproduced:** local ramification disjointness for periods 2--5.
- **Plausible but requiring fuller written ledger:** every raw signed Kummer independence claim and every finite-field twist used for factorial moments.
- **Not supplied by this package:** any uniformity as the maximum period grows with p.

No contradiction or fatal defect was found in the fixed-period 2--5 foundation during this audit.
