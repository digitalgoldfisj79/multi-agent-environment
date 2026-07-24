# Fresh hostile manuscript-only review

## Archive metadata

- Model: `Qwen/Qwen3-14B`
- Hugging Face job: `6a6315847ef3c084649671bb`
- UTC timestamp: `2026-07-24T07:39:06.448438+00:00`
- Manuscript filename: `manuscript.md`
- Manuscript SHA-256: `0c28bc000a8b4ff35f2f47ab53572c3d4e8e5649f7b35cda1d7971818d730be6`
- Prompt SHA-256: `0bfd60eb4e8d4f2f1f2e0ab17c2c31465998744b4504b305b62ef5735da6464c`
- Input scope: the hostile-review prompt plus the exact manuscript only; no audit report, proof source, validator output, prior review, or desired verdict was supplied.
- Output status: unedited model response.

## Exact prompt

You are acting as a hostile referee in analytic and probabilistic number theory.

Read the supplied manuscript as a standalone mathematical paper. Do not assume that omitted arguments exist elsewhere, that computational checks prove asymptotic claims, or that prior reviewers have validated the work.

Your task is to determine whether the main theorem is actually proved in the manuscript as supplied.

Specifically test:

1. whether every hypothesis and normalisation is defined quantitatively;
2. whether all quantifiers and uniformity claims are justified;
3. whether each reduction preserves absolute values, multiplicities, diagonal terms, and normalising factors;
4. whether the character expansion, contour estimate, exceptional-character count, coordinate change, matching argument, and pattern summation are proved rather than asserted;
5. whether the configuration ledger is exhaustive and whether every binding multiplicity is counted correctly;
6. whether the fixed-harmonic estimate really implies the aggregate and Frobenius conclusions;
7. whether any claim of “unconditional” or “no GRH” obscures reliance on random permutation averaging or another substitute hypothesis; and
8. whether the result is materially weaker than its abstract or introduction suggests.

Return exactly four sections:

A. **Verdict:** proved / not proved / indeterminate from supplied text.

B. **Defects:** numbered, classified as fatal, major, or minor, with exact section, equation, or sentence references.

C. **Minimum repairs before specialist circulation:** only repairs necessary to make the manuscript independently reviewable.

D. **Confidence and limitations:** identify any point where your criticism may depend on a convention or missing definition rather than a demonstrated error.

Do not rewrite the manuscript. Do not offer encouragement. Do not infer that a referenced code package or companion paper contains a missing proof unless the supplied manuscript states and cites a precise theorem that legitimately supplies it.

## Unedited response

# A. **Verdict:** not proved

---

# B. **Defects:**

1. **Fatal** - Section 2, Theorem 2.1: The theorem is stated without defining the key quantities $\mathcal E_a^\sigma$, $\mathcal R_a^\sigma$, and $\mathfrak F_X^\sigma$, nor is their dependence on the random permutation $\sigma$ or the parameters $a$, $X$, or $H$ quantitatively defined. This makes the theorem statement incomplete and unverifiable.

2. **Fatal** - Section 2, Theorem 2.1: The constant $C(\eta, \rho)$ is introduced without any definition or justification of its dependence on $\eta$ and $\rho$. This is a critical omission for a quantitative bound.

3. **Fatal** - Section 4: The exact count of configurations is claimed to be $M(M-1) = N^2(N-1) + N(N-1) + 6\binom{N}{3} + 6\binom{N}{4}$, but this expression is not verified or derived. The left-hand side is a simple quadratic expression, while the right-hand side is a more complex sum. This discrepancy is not resolved, and the claim is not justified.

4. **Major** - Section 5: The multivariate Cauchy-contour estimate is asserted without proof. The inequality
$$
|\mathbb E_\sigma \prod_s\psi_s(W_s)|
\le CK^2
\exp\!\left(
-\sum_{s<s'}\frac{n_sn_{s'}}K
(1-t_{\psi_s\bar\psi_{s'}})
\right)
$$
is not derived or referenced, and the meaning of $t_{\chi}$ is not fully clarified in the context of the contour estimate.

5. **Major** - Section 6: The sixth-moment orthogonality identity is stated without proof or reference to a known theorem. The claim
$$
\sum_{\chi\bmod qr}
\left|\sum_{\ell\in\mathcal L}\chi(\ell)\right|^6
=
\varphi(qr)\,
\#\{\ell_1\ell_2\ell_3=\ell_4\ell_5\ell_6\bmod qr\}
$$
is not justified, and the subsequent bound on the number of characters with $t_\chi \ge 3/4$ is not rigorously derived.

6. **Major** - Section 7: The configuration ledger is claimed to be complete, but the reasoning for the net contribution being $O(M(\log X)^9)$ is not fully justified. The factor $\beta^3$ is introduced without a clear definition or derivation, and the claim that "all other classes have more decay or fewer configurations" is not substantiated.

7. **Major** - Section 8: The dual-row decomposition is asserted without proof. The expression
$$
\mathbb E_\sigma[\mathcal E_a^\sigma]
=
M(M-1)\kappa_{2,a}
+
\sum_{q\ne r}p_{q,a}p_{r,a}
\mathbb E_\sigma\sum_{u\ne v}e_{qr}(bD_{u,v}^\sigma)
$$
is not derived or justified, and the term $\kappa_{2,a}$ is not defined.

8. **Major** - Section 10: The manuscript claims that the theorem does not imply Fortune's conjecture or the reciprocal-frame target for the identity ordering, but it does not provide a rigorous argument for this claim. The connection between the random-order model and the identity ordering is not quantitatively or logically established.

9. **Minor** - Section 3: The expression for $D_{u,v}^\sigma$ is stated without a clear definition of the coefficients $c_s$ or the indices $t_s$. The structure of the difference is not fully clarified.

10. **Minor** - Section 9: The "supporting package" is referenced, but the manuscript does not provide a precise theorem or result from this package that justifies the claims made in the paper. The checks listed are not sufficient to replace a formal proof.

---

# C. **Minimum repairs before specialist circulation:**

1. **Define all key quantities** such as $\mathcal E_a^\sigma$, $\mathcal R_a^\sigma$, and $\mathfrak F_X^\sigma$, including their dependence on parameters and the random permutation $\sigma$.

2. **Provide a rigorous derivation** of the configuration count in Section 4, resolving the discrepancy between the left- and right-hand sides of the claimed identity.

3. **Prove the multivariate Cauchy-contour estimate** in Section 5, including a derivation of the exponential decay bound and a precise definition of $t_{\chi}$.

4. **Justify the sixth-moment orthogonality identity** in Section 6, either by citing a known theorem or providing a derivation.

5. **Provide a rigorous derivation** of the configuration ledger in Section 7, including a precise definition of $\beta$ and a justification for the claimed net contribution.

6. **Prove the dual-row decomposition** in Section 8, including a derivation of the expression for $\mathbb E_\sigma[\mathcal E_a^\sigma]$ and a definition of $\kappa_{2,a}$.

7. **Clarify the relationship** between the random-order model and the identity ordering in Section 10, providing a rigorous argument for the claim that the theorem does not imply Fortune's conjecture.

8. **Remove or justify the reference** to the "supporting package" in Section 9, ensuring that all claims are supported by the manuscript itself or by explicitly cited theorems.

---

# D. **Confidence and limitations:**

- **Confidence in the defects:** The manuscript is missing critical definitions, derivations, and justifications for key claims. The lack of formal proofs for the multivariate contour estimate, the sixth-moment orthogonality identity, and the dual-row decomposition makes the main theorem unverifiable as stated.

- **Limitations of the critique:** The critique assumes that the manuscript is self-contained and does not rely on external references or computational checks. If the manuscript is intended to be a companion to a computational package or a prior paper, this would need to be explicitly stated and cited with precise theorems. However, the current text does not provide such citations or definitions, and thus the critique is based solely on the content of the manuscript as supplied.
