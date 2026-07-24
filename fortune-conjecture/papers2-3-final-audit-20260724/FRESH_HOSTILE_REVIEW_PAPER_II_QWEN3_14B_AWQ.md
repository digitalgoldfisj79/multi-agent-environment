# Fresh hostile manuscript-only review — Paper II

- Model: `Qwen/Qwen3-14B-AWQ`
- Hugging Face job: `6a6365fedb23d7a7ec1ca8a6`
- Publication commit: `00d2a67d9963848e35596ea153917e73c2dfeb17`
- Manuscript SHA-256: `632bb8f4fd89a51020069327a11fe57f8ae882e57bd4ae1a9ed0829030c32ce1`
- Prompt SHA-256: `3e8b31b537ca364afead5631f7e2c2b6afd0749d07bf504fabe2ba93719554d6`
- UTC completion timestamp: `2026-07-24T13:26:54.424769+00:00`

The model received the manuscript and hostile-review prompt only. The answer below is reproduced without editing.

---

**A. Verdict:**  
- **Proved:** The results actually claimed (Theorems 2.4, 3.2, 4.2, 5.2, 6.1, 7.1–7.2, 8.1–8.3, 9.1, 9.2) are **proved** with exact proofs, combinatorial identities, and rigorous bounds.  
- **Not proved:** The **imported source-to-frame transference** (used in the reciprocal frame analysis) is **not re-proved** and is explicitly disclaimed as an open step.  
- **Indeterminate:** The **Fortune conjecture** is not claimed, and the open targets (12.1, 12.2) are left as unresolved boundaries.  

---

**B. Fatal or Major Defects**  
1. **Imported transference step (Section 3.6):**  
   - **Location:** The manuscript relies on an unproven "source-to-frame transference" step (Equation 3.6) to connect the reciprocal frame to the variance bound in Theorem 2.4. This is a **major defect** because the manuscript does not re-prove this critical link, leaving the reciprocal frame analysis incomplete.  
   - **Invalid inference:** The manuscript assumes the equivalence between the Frobenius energy (3.6) and Theorem 2.4 without justification, which is **invalid** unless the transference is explicitly proved.  

2. **Semiprime resonance obstruction (Theorem 6.1):**  
   - **Location:** The proof assumes that semiprimes in $\mathcal{A}_X$ divide every $P_j$, but this is only valid if $P_j$ includes all primes up to $X$. If $P_j$ is a primorial prefix (e.g., $P_n = \prod_{p \le p_n} p$), then $X$ must be chosen such that $p_n \ge X$. The manuscript does not clarify this dependency, risking **invalidity** if $X$ is not aligned with $p_n$.  

---

**C. Minor Defects or Claim-Status Corrections**  
1. **Imported transference step (Section 3.6):**  
   - **Claim-status correction:** The manuscript explicitly disclaims the imported transference step as unproven (see "Do not treat explicitly open targets..."). This is a **minor defect** in the sense that the manuscript avoids overstating its results.  

2. **Assumption in Theorem 7.1 (character diagonal):**  
   - **Claim-status correction:** The theorem assumes that no off-diagonal pairs $P_i, P_j$ collide modulo any prime factor of $m$. This is a **conditional assumption**, not a universal claim. The manuscript correctly states this as a condition, but it is worth noting that this assumption is **not universally true** for all $m$.  

3. **Fourier-scale conservation (Proposition 9.1):**  
   - **Minor defect:** The identity is tautological, but the manuscript uses it to argue against long harmonic averaging. This is a **valid argument**, but the tautology might be considered a **minor defect** in the sense of not providing new insight.  

---

**D. Minimum Repairs**  
1. **Re-prove or clarify the imported transference step (Section 3.6):**  
   - The manuscript must either re-prove the source-to-frame transference or explicitly state that it is an **open assumption**. This is critical for the reciprocal frame analysis.  

2. **Clarify the alignment between $X$ and $p_n$ in Theorem 6.1:**  
   - The manuscript must specify whether $X$ is chosen such that $p_n \ge X$ to ensure that semiprimes in $\mathcal{A}_X$ divide all $P_j$. This is a **minor repair** to avoid ambiguity.  

3. **Add a disclaimer for Theorem 7.1’s conditional assumption:**  
   - The manuscript should explicitly note that Theorem 7.1’s result holds **only if** no off-diagonal pairs collide modulo any prime factor of $m$. This is a **minor repair** to avoid misinterpretation.  

---

**E. Confidence and Limitations**  
- **Confidence:** The manuscript is **highly confident** in the proofs of its claimed theorems (e.g., Theorem 2.4, 4.2, 5.2, 6.1, 8.1–8.3). These proofs are rigorous, combinatorial, and use standard analytic number theory techniques.  
- **Limitations:**  
  - The **imported transference step** (Section 3.6) is a **critical limitation** that prevents the manuscript from fully closing the reciprocal frame analysis.  
  - The **Fortune conjecture** remains unproven, and the manuscript correctly avoids claiming it.  
  - The **open targets** (12.1, 12.2) are unresolved, and the manuscript does not attempt to prove them.  
  - The **semiprime resonance** and **CRT character diagonal** results are exact but conditional on specific assumptions (e.g., no collisions modulo primes).  

--- 

**Final Summary:**  
The manuscript **proves** all its explicitly claimed theorems with rigorous arguments, but **fails to re-prove the imported transference step**, which is a **major defect**. The results are **indeterminate** for the Fortune conjecture and the open targets (12.1, 12.2). The manuscript is **confident** in its proofs but **limited** by unresolved transference and conditional assumptions.
