# Cold-review revision notes

**Manuscript:** *Prime Detection at Primorial Centres*  
**Revision date:** 20 July 2026  
**Review source:** Claude cold review.

The cold review found no mathematical error in the theorem layer and classified the manuscript as conditionally ready subject to a short pre-submission list. The following changes were made.

1. **Lemma 2.2:** restricted the equivalence to admissible offsets `m >= 2`, removing the offset-one edge case.
2. **Factorial literature statement:** removed the unverified quantitative claim that classical individual bounds are non-saving at the critical length. The revised text makes only the verified structural comparison.
3. **Scale notation:** added an explicit convention explaining the local uses of `H ~ X^2` and the fixed representative `H = X^2/2` in the Möbius shell.
4. **Validation table:** labelled the one-sided residual as an absolute floating-point residual on `O(M^2)`-scale quantities and recorded its relative scale.
5. **Prime-indicator equivalence:** added the missing forward-direction sentence `n >= H > X`, so a prime `n` cannot divide `A_X`.
6. **Semiprime normalization:** displayed `D_rho ~ H/log H` and the cancellation giving `p_tilde_{n,a} ~ H^{-1}`.
7. **Reproducibility:** refreshed the stale one-sided-phase `run_all_checks.txt`, regenerated its manifest and checksums, and included the revised phase package in the Paper II supplement.
8. **Reduction provenance:** tied the pair-lift/principal-cancellation input explicitly to the supplementary phase reports.

The bibliography database contains 17 entries. The review's statement that it contained 16 entries was a reviewer-side count discrepancy and required no manuscript change.

The revised manuscript and supplement were recompiled, rerendered, and revalidated. No proof of Fortune's conjecture is claimed.

## Release checksums

- Paper II Rev. 1 package: `8bda577e3c95c511f5f812542d0cc51442cab5744c7a6526cb652e679a336108`
- Refreshed one-sided phase package: `a5e1f055e926c690350c717e89ee99bd31b1fcbaa4e3d4305c95a0ef8c27f7bd`
