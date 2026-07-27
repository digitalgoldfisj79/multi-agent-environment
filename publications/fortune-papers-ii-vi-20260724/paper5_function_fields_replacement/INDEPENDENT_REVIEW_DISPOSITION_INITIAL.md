# Disposition of the initial Paper V independent review

**Reviewed source blob:** `78d8b8f30a2fc89b2f76940c86252e28bc828399`  
**Reviewer job:** `6a67031edb23d7a7ec1cf70c`  
**Reviewer verdict:** `MAJOR REVISION`  
**Editorial ruling:** the review is not sufficient to adjudicate the mathematics. It repeatedly labels explicitly supplied arguments as absent and asks for a uniform proof in a section that expressly labels finite computations as regressions. Nevertheless, every potentially useful exposition signal is being acted on. The amended source will receive a fresh exact-hash review.

## Finding-by-finding disposition

### 1. Degree barrier

**Reviewer claim:** irreducible factors of `m` were not justified as irreducible.  
**Ruling:** incorrect as a mathematical objection: “irreducible factor” is definitional. The actual inference needing explicit wording is that coprimality with `P_d` excludes every monic irreducible of degree at most `d`.  
**Action:** amend the proof to begin with the unique factorisation of `m` into monic irreducibles and spell out that none divides `P_d`.

### 2. Quadratic orbit size

**Reviewer claim:** uniqueness and the factor `p(p-1)` were not justified.  
**Ruling:** the manuscript gave the two unique normalisations, but did not display the transformed coefficients or stabiliser argument.  
**Action:** add the exact monic affine action, show translation uniquely kills the linear coefficient, scaling uniquely sends the nonzero quadratic coefficient to one, and explain that a stabiliser preserving both normalisations is the identity.

### 3. Cubic square classes

**Reviewer claim:** square-class dependence was asserted without formula.  
**Ruling:** valid exposition finding.  
**Action:** add the exact formula
`lambda^{-1}F_{a,c,d}(lambda T)=T^p+(a lambda^2)T^3+cT+d/lambda`
and explain the bijection between slices whose cubic coefficients differ by a square.

### 4. Truncated Vandermonde rank

**Reviewer claim:** the rank condition was unsupported.  
**Ruling:** the rank was stated but its column-compression proof was omitted.  
**Action:** add the reduction to the `(p-4) x r` matrix on the distinct coordinate values and its nonzero Vandermonde minors.

### 5. Cone/torsor cohomological transfer

**Reviewer claim:** the exact transfer was unsupported.  
**Ruling:** the relevant torsor and localisation statements were present, but the derived shifts were compressed.  
**Action:** add the compactly-supported cohomology of `A^1`, describe the zero-section localisation for the line bundle `O(-1)`, and show explicitly how the shift and Tate twist produce degrees five and six.

### 6. Quadratic character sum in the sign trace

**Reviewer claim:** the sum over `d` lacked justification.  
**Ruling:** valid exposition finding.  
**Action:** insert the standard identity
`sum_d chi((d-u)(d-v))=p-1` for `u=v` and `-1` for `u!=v`, including the nonzero leading factor.

### 7. Hook projector normalisation

**Reviewer claim:** the cancellation was not justified.  
**Ruling:** the class size and character value were stated, but one arithmetic line is useful.  
**Action:** add `p (p-1)!/p! = 1`.

### 8. Fixed-point count

**Reviewer claim:** the fixed-point count was unsupported.  
**Ruling:** incorrect: the degree-one/degree-`p` classification and multiplicities were supplied.  
**Action:** strengthen by defining arithmetic Frobenius, writing the tuple explicitly as `(alpha,F alpha,...,F^(p-1) alpha)`, and stating why prime degree leaves only degrees one and `p`.

### 9--10. q-line and saturation identities

**Reviewer claim:** the q-line theorem and saturation identity were not justified.  
**Ruling:** Finding 9 misidentifies the section: Theorem 10.1 derives the class projectors from the fixed-cell formula; Theorem 11.1 then performs the class sum. The mathematics is present.  
**Action:** add the explicit count of `p-2` generic q-values and display the half-sum giving `(S_0+A S_chi)/2`; keep the one-line algebra proving the saturation identity.

### 11. Finite computation

**Reviewer claim:** the finite regression section requires a general proof for all primes.  
**Ruling:** rejected. The manuscript explicitly states that the computations are exact checks at listed primes and do not replace the general proofs. No universal claim rests on the scans.  
**Action:** sharpen the first sentence of the section to say that all uniform theorems have already been proved symbolically and the computations are regression tests only.

### 12. Terminal frontier

**Reviewer claim:** the paper had not justified why a future theorem must exclude zero.  
**Ruling:** rejected as a mathematical objection. Corollary 4.2 proves that the crown is exactly `W_p>0`; Theorem 11.1 identifies the cubic contribution with the saturation defect. The terminal statement is a restatement of these exact equivalences, not a claimed exclusion theorem.  
**Action:** explicitly cite Corollary 4.2 and Theorem 11.1 in the terminal paragraph.

## Convention findings

The reviewer correctly identified that conventions should be more explicit.

**Actions:**

- define arithmetic Frobenius before the cohomological trace formulas;
- state that `Q_l(-1)` has arithmetic-Frobenius eigenvalue `p`;
- make the sign variable `s_p` refer back to Theorem 7.1;
- repeat the prime restrictions at each theorem boundary;
- retain precise citations to weak Lefschetz and Sawin's formalism.

## Reset ruling

The candidate source will change. Therefore:

1. its previous SHA-256 and review are superseded;
2. all source-fidelity hashes will be regenerated;
3. a new manuscript-only independent review will be run on the amended exact hash;
4. compiled artefacts and QA will be regenerated only after the fresh review is disposed.
