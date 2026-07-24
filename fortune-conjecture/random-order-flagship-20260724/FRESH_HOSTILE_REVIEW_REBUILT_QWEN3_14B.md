# Fresh hostile manuscript-only review of rebuilt Paper IV

## Archive metadata

- Model: `Qwen/Qwen3-14B`
- Hugging Face job: `6a631c94db23d7a7ec1ca052`
- UTC timestamp: `2026-07-24T08:09:04.438197+00:00`
- Manuscript filename: `manuscript.md`
- Manuscript SHA-256: `c7e337fd38a58cac2e98a2237eae6ad48681241f167504a546cb6fa978cbb7fa`
- Prompt SHA-256: `0bfd60eb4e8d4f2f1f2e0ab17c2c31465998744b4504b305b62ef5735da6464c`
- Input scope: exact hostile prompt plus exact rebuilt manuscript only.
- Output status: unedited response.

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

# A. Verdict: **not proved**

The manuscript presents a detailed and complex argument for a theorem in analytic number theory, but it **does not fully prove** the main theorem (Theorem 2.1) as stated. While the paper provides a detailed structure and a number of lemmas and propositions, **key components of the proof are either asserted without proof or rely on unverified claims**. The manuscript is **not self-contained** in the sense that it **does not provide complete proofs** for all of the critical steps required to establish the main result.

---

# B. Defects:

1. **Major** - **Section 3, Lemma 3.3 (complete coefficient-pattern list)**: The lemma lists the possible nonzero coefficient vectors, but **it is not proved** that these are the only possible configurations. The proof is asserted to be "realised by an ordered pair of two-element multisets," but this is not demonstrated in the manuscript.

2. **Major** - **Section 3, Lemma 3.4 (exact multiplicities)**: The lemma asserts that the multiplicity is $N$ for type S and $1$ for other configurations, and that the total number of configurations sums to $M(M-1)$. However, **this is not proved** in the manuscript. The claim is made without a rigorous derivation of the multiplicities or the total count.

3. **Major** - **Section 4, Lemma 4.1 (rank-conditioning identity)**: The identity is stated and used in the proof, but **it is not proved** in the manuscript. The proof is claimed to be "standard" or "follows from uniform distribution over ordered set partitions," but this is not demonstrated.

4. **Major** - **Section 4, Lemma 4.2 (multivariate contour bound)**: The bound is stated and used in the proof, but **it is not proved** in the manuscript. The derivation of the exponential decay is asserted without a complete proof.

5. **Major** - **Section 5, Lemma 5.1 (Gauss coefficients and norms)**: The lemma provides bounds on the Gauss coefficients, but **it is not proved** in the manuscript. The derivation of the bounds is asserted without a complete proof.

6. **Major** - **Section 6, Lemma 6.1 (triangular coordinate bijection)**: The bijection is claimed to be a "triangular matrix with diagonal entries $\pm1$," but **this is not proved** in the manuscript. The proof is asserted without a detailed derivation.

7. **Major** - **Section 6, Lemma 6.2 (path matching lemma)**: The lemma provides a bound on the sum over patterns, but **it is not proved** in the manuscript. The derivation of the bound is asserted without a complete proof.

8. **Major** - **Section 6, Lemma 6.3 (all-bad pattern domination)**: The lemma asserts that the sum over all patterns is at most twice the all-bad bound, but **this is not proved** in the manuscript. The derivation is asserted without a complete proof.

9. **Major** - **Section 7, Proposition 6.4 (per-configuration bound)**: The bound is stated and used in the proof, but **it is not proved** in the manuscript. The derivation of the bound is asserted without a complete proof.

10. **Major** - **Section 9, Theorem 2.1 (random-order reciprocal-frame theorem)**: The theorem is stated as the main result, but **it is not proved** in the manuscript. The proof is asserted to follow from Proposition 2.2 and other lemmas, but **the critical steps are not fully demonstrated**.

11. **Major** - **Section 10 (Effective constants and verification)**: The manuscript claims that the constants are effective and that the conditions are verified, but **this is not proved** in the manuscript. The verification is asserted without a complete proof.

12. **Major** - **Section 11 (Scope and derandomisation)**: The manuscript discusses the implications of the result, but **it does not prove** that the result is not applicable to the increasing primorial order or that the identity permutation is nonexceptional. These are **asserted without proof**.

---

# C. Minimum repairs before specialist circulation:

1. **Provide complete proofs** for all lemmas and propositions that are used in the proof of the main theorem. This includes:
   - Lemma 3.3 (complete coefficient-pattern list)
   - Lemma 3.4 (exact multiplicities)
   - Lemma 4.1 (rank-conditioning identity)
   - Lemma 4.2 (multivariate contour bound)
   - Lemma 5.1 (Gauss coefficients and norms)
   - Lemma 6.1 (triangular coordinate bijection)
   - Lemma 6.2 (path matching lemma)
   - Lemma 6.3 (all-bad pattern domination)
   - Proposition 6.4 (per-configuration bound)

2. **Provide a complete proof** of Theorem 2.1 (random-order reciprocal-frame theorem), including all steps that are currently asserted without proof.

3. **Clarify the role of the supporting code** and ensure that it is not used as a substitute for a complete mathematical proof. The manuscript should not rely on computational checks to validate asymptotic claims.

4. **Provide a detailed derivation** of the effective constants and the conditions under which they are valid. This includes a rigorous derivation of the bounds on the constants and the conditions under which they hold.

5. **Clarify the relationship between the random permutation model and the increasing primorial order**. The manuscript should not assert that the result does not apply to the increasing primorial order without a complete proof.

---

# D. Confidence and limitations:

- **Confidence in the structure**: The manuscript presents a **well-structured and detailed argument** for the main theorem, and the **approach is mathematically sound** in principle.

- **Limitations in the proof**: The manuscript **does not provide complete proofs** for the key lemmas and propositions that are used in the proof of the main theorem. This makes it **impossible to verify the correctness of the result** without further information.

- **Dependence on conventions**: The manuscript **relies on standard conventions** in analytic number theory, such as the use of character sums and contour integration, but **does not provide a complete derivation** of these techniques in the context of the problem.

- **Dependence on external references**: The manuscript **cites a previous paper** [1] for a comparison theorem, but **does not provide a complete proof** of the theorem or its application in the current context.

- **Dependence on computational checks**: The manuscript **mentions supporting code** that performs finite checks, but **does not use it as a substitute for a complete mathematical proof**. The manuscript should not be interpreted as relying on computational checks to validate asymptotic claims.

## Disposition note

The raw verdict is not accepted as a controlling audit result. The reviewer repeatedly states that lemmas are “not proved” even though each named lemma is followed by an explicit proof in the supplied manuscript. It also misidentifies Proposition 6.4 as being in Section 7 and demands a proof that the random-order theorem is inapplicable to the increasing-order path, although the manuscript makes only the logically narrower statement that its argument does not establish that case. A stronger-model review is therefore required. The external Paper II dependency remains a legitimate item to verify precisely.
