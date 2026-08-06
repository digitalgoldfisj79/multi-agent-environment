# C0 execution — source freeze

**Status:** `PASSED`

The execution began from branch head `3f01256a2d2fa0b4cb530b157b349eb7efa90115`, PR #57, issue #56 and the closed parent occupancy-dual programme.

Frozen inherited facts:

1. For row-dependent preregistered temperatures `0 < tau_j <= tau_A`,
   \[
   \sum_j e^{-\tau_j Z_j}<1
   \]
   excludes every zero row and implies the frozen uniform `INT-AOD` detector.
2. Ordinary cumulants satisfy
   \[
   c_{k,b}=\sum_{m_1,\ldots,m_k}\operatorname{Cum}_b(I_{m_1},\ldots,I_{m_k}),
   \]
   over all ordered offset tuples, including repetitions.
3. Factorial cumulants are not identified with ordinary joint cumulants over globally distinct columns. The rejected identity remains prohibited.

The parent and current static sentinels were rerun before analytic work. The first baseline diagnostic exposed a SymPy API defect in `run_selected_centre_cumulants.py`; it was corrected from the obsolete `method="primes"` call to `primorial(ell, nth=False)`. No mathematical statement changed.
