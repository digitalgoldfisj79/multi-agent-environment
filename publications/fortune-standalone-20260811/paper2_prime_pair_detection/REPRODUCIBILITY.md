# Reproducibility boundary — Paper II

The manuscript is mathematically readable without executing code. Computation has only the following roles:

- exact finite enumeration checking the pair-sum fourth-moment count;
- floating-point residual checks of algebraic/Fourier identities;
- finite CRT/character reconstruction checks;
- finite coherence and reciprocal-pair diagnostics.

None of these computations establishes an asymptotic theorem. The Hardy--Littlewood baseline formulae are conjectural analytic calibrations, not computational findings. The final publication bundle must include the corresponding validators and checksums under a separate reproducibility-support directory; their absence from a reader's environment does not change any theorem statement or proof in `manuscript.md`.
