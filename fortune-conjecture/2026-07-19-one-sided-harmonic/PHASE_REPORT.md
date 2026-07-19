# Fortune one-sided harmonic and large-values phase — final report

**Date:** 2026-07-19  
**Status:** natural stopping point reached; Fortune and PGD2 remain unproved.

## Objective

Run four final gates suggested by the hostile Claude Fable 5 Max review:

1. formalize the one-sided PGD2 correction;
2. test an aggregate harmonic theorem;
3. determine whether frame weights can create a growing numerator average;
4. test top-level phase alignment and divisor pinning.

## Results

### Gate 1 — PASS: genuine target correction

Exactly,

\[
\mathcal E_a=M(M-1)\kappa_{2,a}+\mathcal R_a.
\]

Only the upper estimate for \(\mathcal R_a\) is load-bearing. The correct target is

\[
\mathcal R_a\le MX^{o(1)}.
\]

STL2 and absolute PGD2 are stronger than necessary.

### Gate 2 — PASS algebraically, STOP as a proof mechanism

A new exact no-truncation weighted reduction is

\[
\mathrm{PC\!-
FROB2}
\le
2\sum_{a\ge1}\frac{\mathcal E_a}{m_a},
\qquad
m_a=\sum_qp_{q,a}.
\]

This is a cleaner theorem boundary. It does not create cross-harmonic cancellation: the right side is a positive sum. Under the actual Gaussian frame its weighted kernel has effective dimension at most 4.33 and 99.99% of its mass in at most nine harmonics.

### Gate 3 — FAIL: harmonic-range growth is illusory

Narrowing the physical interval by a factor \(A\) broadens each translate's Fourier support by \(A\), but summing the \(A\) translates reconstructs the original length-\(H\) transform exactly. Bounding them separately pays the same factor \(A\).

Moving to \(Q=BH\) gives \(B\) harmonics but changes the shell scale to \(BH/\log(BH)\), increases pair conductor by \(B^2\), and does not remove the compulsory \(Q\asymp H\) shell.

No genuine growing independent average in \(a\) survives.

### Gate 4 — FAIL: top-level values do not force divisibility

The proposed threshold gives only

\[
|F|\gg N^{1-\delta/2}=o(N).
\]

It allows diffuse bias and does not force many phases into a narrow arc. Even hypothetical arc constraints have error \(\varepsilon |L|\) after determinant elimination; because \(|L|\) is primorial-sized, exact pinning would require exponentially small arcs unavailable from a power-scale large-value estimate.

The route reconstructs the existing global high-coherence incidence problem rather than producing a divisor theorem.

## Scientific conclusion

This phase produced two durable expository improvements:

1. PGD2 is explicitly one-sided;
2. the harmonic reduction admits an exact no-truncation weighted aggregate form.

It produced no new asymptotic saving and closed both proposed mechanisms for exploiting those improvements.

\[
\boxed{
\text{Internal transformation programme: STOP at this boundary.}
}
\]

The remaining obstruction is a global arithmetic transference theorem for high values of the consecutive-prime prefix-product walk under reciprocal prime-pair sampling. The justified next actions are publication of the obstruction/reduction package and narrowly targeted human specialist consultation.
