# Hostile review prompt: centred source-to-frame identity

Review `CENTRED_SOURCE_TO_FRAME_IDENTITY_20260728.md` as a standalone mathematical note.

The task is theorem verification, not strategic encouragement. Follow every displayed definition and report any sign, normalisation, conjugation, scaling or quantifier error.

Required checks:

1. Verify Theorem 2.1, including the failed-centre prime-power bound, the variance scale `N H X L(X)`, and the deduction `B_X=o(1)`.
2. Verify that `U_X=D_H B_X` has Fourier coefficient `Psi_j` at frequency `P_j` with the stated signs.
3. Verify Theorem 3.1 and Parseval, including the nonconstant baseline polynomial.
4. Verify the factor `2`, the divisions by `m_a`, and the assertion `sum_{a>=1} m_a=1/2` in the aggregate kernel and frame.
5. Verify `0<=K_X(L)<=1`, `K_X(0)=1`, positive semidefiniteness, and the direct-to-Gram expansion in Theorem 4.1.
6. Verify the lower-frame plus upper-source implication to the block variance.
7. Verify the baseline-before-square identity and assess the precise scope of the coefficient-erasure no-go.
8. Verify the literal square coefficients, the normalised symmetric-square coefficients, and both diagonal-mass formulas in Section 6.
9. Identify any claim that is stronger than the proof, any hidden Hardy--Littlewood assumption, or any assertion that inadvertently revives the old unweighted frame.

Return:

- headline verdict: `PROVED AS STATED`, `REQUIRES AMENDMENT`, or `INVALID`;
- a claim-by-claim table;
- exact quotations for every adverse finding;
- a distinction between mathematical errors, missing hypotheses, and presentational improvements;
- the strongest corrected theorem boundary.

Do not infer a Fortune proof from the finite validator. Do not reject an exact finite identity merely because its analytic hypotheses are open.
