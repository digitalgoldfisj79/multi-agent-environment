# Fresh hostile manuscript-only review — Paper III

- Model: `Qwen/Qwen3-14B-AWQ`
- Hugging Face job: `6a6365fedb23d7a7ec1ca8a6`
- Publication commit: `00d2a67d9963848e35596ea153917e73c2dfeb17`
- Manuscript SHA-256: `1753e5991ccab15142d9bd076554c283a69bfa3bd8aa9448b2edf62f50c4c7cb`
- Prompt SHA-256: `32bd0a46b61552ee94458042806275336505fcf4684c05e2469a81a66013dd6e`
- UTC completion timestamp: `2026-07-24T13:29:08.886894+00:00`

The model received the manuscript and hostile-review prompt only. The answer below is reproduced without editing.

---

**A. Verdict:** Not proved.  

**B. Fatal or major defects:**  
1. **Missing Theorem in Exceptional-Set Corollary (Section 8):** The manuscript relies on an unproven "missing theorem" to bridge the arithmetic transfer gap. The corollary (8.1) assumes a sparse exceptional-set statement that is not established, rendering the conclusion conditional on an unverified hypothesis.  
2. **Unproven Hypotheses (H1) and (H2):** The conditional theorem (10.1) assumes block-averaged first moments (H1) and pair correlations (H2) with relative error $o(\log X/X)$. These hypotheses are not proven in the manuscript and are explicitly stated to be beyond current technology. The theorem is thus conditional on unproven assumptions.  
3. **Inadequate Justification for Sub-Weibull Tail Sharpness:** While the sub-Weibull tail bound (Theorem 6.1) is derived, the claim of sharpness at fixed levels is not rigorously extended to the full range $\lambda \leq M^2$. This could undermine the robustness of the tail estimate for the conditional theorem.  

**C. Minor defects or claim-status corrections:**  
1. **Ambiguity in the Role of the Dickman Sketch (Appendix B):** The "non-load-bearing sketch" of the sharp constant in Lemma B.4 is labeled as such but is used in the manuscript's reasoning. This could mislead readers into thinking the constant is fully proven.  
2. **Lack of Explicit Constants in Conditional Theorem:** The conditional theorem (10.1) uses $o(1)$ terms without specifying explicit constants, which may limit its applicability in computational or effective number theory contexts.  
3. **Unverified Computational Checks:** While the manuscript references computational validations (e.g., `addendum_checks.py`), the exact scope and reproducibility of these checks are not detailed, leaving room for doubt about their thoroughness.  

**D. Minimum repairs:**  
1. **Prove the Missing Exceptional-Set Theorem:** The manuscript must either prove the sparse exceptional-set statement or explicitly label it as an open problem.  
2. **Clarify the Status of (H1) and (H2):** The hypotheses (H1) and (H2) should be explicitly labeled as conditional or conjectural, with a disclaimer that their verification is outside the manuscript's scope.  
3. **Extend Sub-Weibull Tail Analysis:** Provide a rigorous argument or reference for the uniformity of the sub-Weibull tail bound over the full range $\lambda \leq M^2$, or explicitly limit its use to fixed levels.  
4. **Detail Computational Validations:** Include explicit details of the computational checks (e.g., code, parameters, and exact results) to ensure reproducibility and strengthen the manuscript's claims.  

**E. Confidence and limitations:**  
- **Confidence:** The manuscript presents a well-structured and technically rigorous analysis of pair-sum rigidity, moments, and conditional prime detection. The proofs of the dichotomy (Theorem 3.1), sub-Weibull tails (Theorem 6.1), and truncated singular series bound (Theorem 9.1) are solid.  
- **Limitations:** The conclusions are conditional on unproven hypotheses (H1) and (H2), and the missing exceptional-set theorem. The reliance on computational checks without explicit details reduces the manuscript's reproducibility. The sharpness of the sub-Weibull tail is also limited to fixed levels, which may not suffice for the conditional theorem's requirements. The manuscript is thus a significant contribution to the conditional framework but does not establish unconditional results.
