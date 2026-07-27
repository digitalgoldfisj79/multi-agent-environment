# Disposition of the initial Paper VI independent review

**Reviewer job:** `6a6704d3db23d7a7ec1cf729`  
**Verdict:** `MAJOR REVISION`  
**Editorial ruling:** the response is not a reliable theorem audit. It repeatedly asks for proofs that the manuscript already gives and, in Finding 1, confuses the proved implication `M_a != 0 => N_a > 0` with the expressly open claim that `M_a` is uniformly nonzero. Nevertheless, the manuscript will be expanded at every compressed transition and then submitted to a fresh exact-text reviewer.

## Dispositions

1. **Cartier moment.** Rejected as a mathematical objection. The theorem is the sum of a pointwise cofactor identity; sufficiency follows because a nonempty weighted sum cannot be nonzero when there are no summands. The manuscript explicitly says uniform nonvanishing is open. Add a two-line proof.
2. **Translation projector.** The orbit computation was present before the theorem. Add a labelled proof summing over each unique translation orbit.
3. **Reciprocal q-line moment.** The identity follows by substituting `c=-3/q`; the observation about Hasse weight is not part of the theorem. Add the substitution as a proof and separate the interpretive sentence.
4. **Cyclotomic tangent.** The binomial expansion was already displayed. Add a labelled proof.
5. **Nonsplit extension.** Add the explicit contradiction: an invariant lift of the quotient generator would have to be `1+u pi`, but `(tau-1)(1+u pi)=pi !=0`.
6. **Frobenius blindness.** Add explicit verification that every `lambda` gives a distinct coefficient and all modular invariants are unchanged.
7. **Divided-hook obstruction.** The fractional Fourier multiplicities were already computed. Add the sentence that virtual characters have integral multiplicities in the irreducible-character basis.
8. **Hattori--Stallings extraction.** A proof was already present. Expand the regular-lattice matrix trace by one line.
9. **Artin--Schreier quotient.** Add `sigma(g)=(y+1)^p-(y+1)=g` and explain that a free `C_p` torsor with such a coordinate is the pullback of the universal Artin--Schreier torsor.
10. **Irreducibility section.** Add the degree argument: nonzero shift makes the Frobenius orbit have length `p`; conversely choosing a first root of an irreducible and quotienting rotations yields one point on each nonzero level.
11. **No-split theorem.** A complete degree contradiction was present. Add why the reduced logarithmic derivative numerator is nonzero and why `deg P>=0` makes the right side degree at least `p`.
12. **Sign-twist criterion.** The even/odd exponent proof was present. Expand the Kummer cocycle and coboundary computation.
13. **Common quotient counts.** Add a formal torsor-fibre proof: each rational quotient point has rational lifts in exactly one form and exactly `gcd(p-3,p-1)=2` lifts.
14. **Unique fixed point.** A proof was present. Add the difference equation derivation and power-sum verification.
15. **Compactified count.** Add the full partition of quotient points by Frobenius shift and identify each of the boundary/open contributions before summing.

## Dependencies and conventions

The amended manuscript will:

- define the Frobenius convention before the first trace statement;
- identify Brown's periodic Tate complex as a standard input;
- define the Hattori--Stallings trace sufficiently for the coefficient proof;
- state the Artin--Schreier and Kummer descent facts used;
- repeat `p>5` and admitted-prime restrictions at the relevant results;
- state again that finite checks are regressions, not proof inputs.

## Reset ruling

The source will change, so the initial review and source hash are superseded. A fresh quote-required manuscript-only review will be run on the amended exact hash before any internal technical pass is considered.