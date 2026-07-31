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

Combining the exact results gives the following regime table.  The row
\(k\ge q\) is an imported predecessor theorem recorded for context; its
separate proof is not reproduced in this paper and is not used in the quadratic
theorem.

| Regime | Status |
|---|---|
| \(k=2\), odd prime powers \(q\) | empty |
| \(k<q<2k\), odd primes \(q\) | empty |
| \(k\ge q\), odd primes \(q\) | predecessor classification: translation/reflection, with transpose contact at \(k=q\); not reproved here |
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
- a complete classification of zero defect in the odd-prime range \(q>k\);
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
