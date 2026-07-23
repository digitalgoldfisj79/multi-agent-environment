# Correction: endpoint branch support is not an ordinary A1 Adams difference

**Date:** 2026-07-23  
**Status:** exact correction to the interpretation of `WEIGHTED_ENDPOINT_ESCAPING_A1_THEOREM.md` and `EQUIVARIANT_TAME_THOM_SEBASTIANI_THEOREM.md`. The two escaping `A1` sections and their rank-one stationary-phase objects are exact. However, the nonzero primitive endpoint class cannot be justified by applying `Psi^p(V)-V` to a geometric rank-one `A1` sign line: for odd `p` that class is zero. The missing class is a Fourier–wild-specialization defect.

## 1. Geometric A1 line

Let `V` be the rank-one geometric vanishing-cycle representation of a simple tame `A1` branch. Its local monodromy is the sign character, so

`V^(tensor p)=V`

for odd `p`. Equivalently,

`Psi^p(V)=V`

in the geometric finite-monodromy representation ring. Hence

### Proposition EABC.1

`boxed(Psi^p(V)-V=0)`

for an isolated geometric `A1` sign line.

This is consistent with the previously proved theorem that every finite transposition stratum is annihilated by the Adams defect.

## 2. Why the endpoint can nevertheless contribute

The weighted endpoint is not obtained by first specializing to an isolated geometric `A1` line and then applying Adams. The relevant sequence is:

1. take the p-fold cyclic convolution/Fourier realization of `Psi^p` on the generic family;
2. compactify and specialize through the wild Artin–Schreier central fibre;
3. subtract the original root sheaf and the explicit Artin–Schreier/Tate class.

Fourier transform, cyclic convolution and wild nearby cycles do not reduce to the ordinary operation `Psi^p(V)-V` on the final geometric sign line. The residual class measures precisely the failure of this naive commutation.

The exact inertia identity

`W|I = W_AS^aff + 2(Q-m*1)`

shows that, after the complete wild Artin–Schreier class is removed, the unresolved input is the tame augmentation specialization. `WEIGHTED_ENDPOINT_DECK_DESCENT_THEOREM.md` proves that its geometric stationary support descends through only two sections with trivial/quadratic deck action. It does not determine the Fourier–specialization multiplicity on those sections.

## 3. Correct rank-four formulation

The phrase

`one rank-one Psi^p term minus one rank-one original term per A1 branch`

should be read only as a **candidate effective presentation on the Fourier side**, conditional on a specialization theorem. It is not an application of the ordinary geometric identity `Psi^p(V)-V`.

The required theorem is:

### Fourier–Adams endpoint specialization theorem

After removing the explicit Artin–Schreier/Tate and main/Kummer classes, the specialization cone of the p-fold cyclic Fourier convolution at the weighted endpoint is supported on the two escaping stationary sections, and on each section has an effective presentation by at most two rank-one Weil objects. No additional punctual object is supported at their chart intersections.

This theorem would imply an endpoint effective bound `<=4`. It remains open.

## 4. Consequences for existing files

The following statements remain exact:

- normalized endpoint equation;
- exactly two escaping critical sections;
- their `A1` local type and separated critical values;
- equivariance of tame Thom–Sebastiani;
- rank one of a local Fourier contribution attached to a nondegenerate stationary section;
- quadratic deck descent of the pair.

The following implication is reclassified as conditional:

- identifying the complete primitive endpoint class with a difference of two rank-one objects on each section.

No numerical result or previously proved local-inertia theorem is affected.

## 5. Epistemic classification

### Exact

- `Psi^p(V)-V=0` for the geometric `A1` sign line and odd `p`;
- the endpoint residual is not an ordinary finite-transposition Adams class;
- the missing term is a Fourier–wild-specialization defect;
- the geometric support consists of two sections with quadratic deck action.

### Open

- effective multiplicity on each section;
- chart-intersection punctual cone;
- zero-frequency fixed-diagonal contribution;
- conductor-defect lemma and crown.
