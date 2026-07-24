# Part III. Failure certificates, calibration, and open theorems

## 10. Exact failure certificates

The spectral and structural audits close the following direct mechanisms.

1. **Uniform common Frobenius factor.** No growing common factor appears through ranks one to four, apart from an isolated central factor at \(p=23\).
2. **Torsion or bounded-period phases.** The normalised trace \(29/17\) is not of root-of-unity algebraic-integral type.
3. **Uniform Newton-slope pairing.** The \(p=17\) spectra give a concrete exception.
4. **Characteristic-zero cross-\(k\) correspondence.** This is obstructed by the disjoint Hodge spectra.
5. **Bounded-cone modular lift.** The projected Dwork defect has full rank.
6. **Bare cyclic-shift localisation.** The target correspondence is shift composed with Frobenius and reconstructs the original extension-field locus.
7. **Bounded-degree Gaussian-period reduction.** The tested orbit polynomials have full degree.

These are failures of proof strategies, not evidence that the absolute trace estimate is false.

## 11. Statistical calibration

For primes \(p\equiv5\pmod6\) up to \(10^5\), the normalised values have RMS close to one and a maximum \(3.4273\). Under an iid standard-normal calibration with 4806 observations,
\[
\mathbb E\max|Z_i|=3.8418853,
\]
and the observed maximum is at approximately the \(5.33\) percentile.

The sweep is compatible with a bounded sequence, slow unbounded growth, or eventual Gaussian extremes. It cannot decide the uniform theorem and should not be extended without a concrete structural identity to test.

## 12. Two terminal theorem gaps

### Analytic theorem

Prove
\[
\left|
\operatorname{Tr}(F|U_p)
-p\operatorname{Tr}(F|U_{p-2})
\right|
\le Cp^{(p+1)/2}
\]
with \(C\) independent of \(p\).

Equivalent formulations include edge-frequency Airy Chebyshev cancellation, a characteristic-\(p\) Frobenius correlation, and cancellation between two full real-cyclotomic Dickson traces.

### Application theorem

Construct an object-level comparison between the cubic Airy boundary complex and the post-pushforward hook/nearby-cycle complex controlling irreducible fibres. It must include:

- main, Tate, and Artin--Schreier subtraction;
- the punctual \(b=0\) term;
- the arithmetic quadratic twist at infinity;
- the \(q=2\) and \(q=\infty\) boundary cones;
- the final positivity certificate.

Without the exact transport coefficient, it is unknown whether the full Fortune crown requires an absolute constant or could tolerate logarithmic slack.

## AI-assistance disclosure

The research programme used large language models for structured literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. Every mathematical claim included as a theorem was checked against an explicit proof or an independently reproducible exact computation. Conjectural, conditional, computational, and negative results are labelled separately. The named author takes responsibility for the content, citations, code, and final presentation.

## Data, code, and reproducibility

The source record is the public repository `digitalgoldfisj79/multi-agent-environment`, branch `gpt56/d1-gate-bridge-terminal-20260724`. The Zenodo package contains the single-file manuscript source, compiled PDF, DOCX and LaTeX, exact PREREG-8 scripts and checkpoints, claim-status ledger, source manifest, metadata, and checksums.

## References

1. C. D. Haessig and A. Rojas-León, *L-functions of symmetric powers of the generalized Airy family of exponential sums: ell-adic and p-adic methods*, arXiv:0908.1240.
2. C. Sabbah and J.-D. Yu, *Hodge properties of Airy moments*, arXiv:2112.13405.
3. Y. Qin, *Hodge numbers of motives attached to Kloosterman and Airy moments*, arXiv:2302.05365.
4. P.-H. Chuang, *On the Generalized Arithmetic Picard--Lefschetz Formula*, arXiv:2607.05757.
