# Papers II–III: theorem-by-theorem reconstruction

**Date:** 4 August 2026  
**Authoritative sources:** Paper II and Paper III at commit `b42da323eccd6f995fc9e2f93373beb1274293ac`  
**Audit standard:** exact definitions, proof dependencies, calibration status, implication direction and surviving theorem boundary

## Executive result

The corrected Papers II–III are mathematically coherent at their stated boundary. Their elementary and algebraic claims survive reconstruction. They do **not** contain a proof of the required arithmetic variance estimate, a source-to-reciprocal transfer theorem, or Fortune's conjecture.

The reconstruction sharpens their joint frontier. The two separate conditional estimates `(C1)` and `(C2)` in Paper III can be replaced by one centred signed residual. This residual is the smallest load-bearing integer theorem now visible in the programme.

## Frozen setting

For a dyadic block of primes

\[
X\le \ell_1<\cdots<\ell_N<2X,
\qquad N\asymp X/\log X,
\]

put

\[
A_X=\prod_{p<X}p,
\quad Q_j=\prod_{u\le j}\ell_u,
\quad P_j=A_XQ_j,
\quad H=\eta X^2,
\]

with fixed `0 < eta < 1`. The exact detector is

\[
Z_j(H)=\sum_{2\le m\le H}
  1_{\mathbb P}(m)1_{\mathbb P}(P_j+m).
\]

The explicit baseline used below is

\[
\lambda_j^*(H)=\mathfrak S(P_j)
\int_{\ell_j}^{H}\frac{dt}{\log t\,\log(P_j+t)}.
\]

Its interpretation as the true mean is Hardy–Littlewood calibration. Its size `lambda_j^* asymp X` follows from elementary estimates for the displayed deterministic expression and is all that the one-failure implication uses.

## Paper II reconstruction

### Direct detector spine

| Claim | Status | Reconstruction ruling |
|---|---|---|
| Proposition 2.1: composite Fortunate number is at least the next-prime square | PROVED | Elementary prime-factor exclusion is correct. |
| Lemma 2.2: candidate collapse below `ell_(j+1)^2` | PROVED | If an admissible offset were composite, both prime factors would be at least the next prime. |
| Proposition 2.3: shifted von Mangoldt detector equals the weighted prime-pair detector plus proper-prime-power contamination | PROVED | The coprimality step and the prime-power support are explicit. The uniform remainder `O(X log X)` follows by spacing and summing `O(X/k)` over exponents. |
| Theorem 2.4: unweighted block criterion | PROVED CONDITIONAL IMPLICATION | One failed centre costs at least `c^2 X^2`; the assumed total variance gives `B_X = o(1)`. |
| Theorem 2.5: weighted block criterion | PROVED CONDITIONAL IMPLICATION | Same one-failure argument at gap `asymp H`. |
| Lemma 2.6: failed-centre contamination for the double-von-Mangoldt source | PROVED | Proper-prime-power spacing gives `O(X (log X)^2)`. |
| Theorem 2.7: double-von-Mangoldt block criterion | PROVED CONDITIONAL IMPLICATION | The scale calculation is correct when `H asymp X^2`. |
| Equations 2.19–2.21 | CONJECTURAL CALIBRATION | They are not used as proved prime-pair asymptotics. |

### Exact harmonic source

Theorem 2.8 is correct. For

\[
G_X(\theta)=A_H(\theta)B_X(\theta),
\]

Fourier orthogonality gives exactly

\[
T_j(H)=\int_0^1G_X(\theta)e(-P_j\theta)d\theta.
\]

Squaring and summing produces the exact single-walk kernel `F_X(beta-alpha)`. This is an identity, not an estimate. It does not supply cancellation in the centred variance.

### Reciprocal-frame material

The harmonic decomposition, one-sided residual identity, pair-sum moments, Möbius truncation, character diagonal, ratio-collapse theorem, failure certificate, coherence calculation, conductor migration and Fourier-scale conservation remain exact statements internal to the reciprocal model.

They are no longer on the proved implication chain to Fortune because no theorem maps the corrected prime-pair source to that frame. This is not a cosmetic omission: the missing map must preserve the baseline subtraction and both prime variables.

### Paper II verdict

Paper II correctly ends with three possible variance targets. None is proved. The direct unweighted target is the cleanest logical interface; the double-von-Mangoldt target is the cleanest analytic source; the recentered shifted detector remains a possible one-sided route. The old reciprocal estimate is not load-bearing without a new theorem.

## Paper III reconstruction

### Kernel theory

| Claim | Status | Reconstruction ruling |
|---|---|---|
| Lemma 2.1 / A.1: bounded-coefficient rigidity | PROVED | The largest-index term dominates the geometric tail when `X > B+1`. |
| Theorem 3.1 / A.3: difference multiplicity is `N` or `1` | PROVED | Endpoint-multiset rigidity gives the sliding family and excludes intermediate multiplicities. |
| Corollary A.4: two-scale energy decomposition | PROVED | Directly follows by grouping differences by multiplicity. |
| Lemma 5.1 / A.6: high moment bound | PROVED | Labelled endpoint lifts give the stated combinatorial upper bound. |
| Theorem 6.1 / A.7: sub-Weibull Lebesgue tail | PROVED | Markov plus the moment bound; valid only in the stated level range. |
| Exact fourth and sixth moments | PROVED | Finite endpoint-multiset enumeration. |
| Corollary 8.1 / A.10: sparse sampling gap | PROVED NO-GO | Lebesgue-small exceptional sets may still contain polynomially many prescribed reciprocal atoms. |
| Theorem 9.1: corrected all-centres criterion | PROVED CONDITIONAL IMPLICATION | Same valid one-failure argument as Paper II. |
| Equation 10.1: four-prime expansion | PROVED | Ordered off-diagonal pairs are uniquely indexed by positive displacement. |
| Conditions C1–C2 imply the variance target | PROVED CONDITIONAL IMPLICATION | Substitution into the exact second-moment expansion is correct. |

### Critical correction retained

The old first moment `NH` is not a valid calibration for the unweighted prime-pair detector. The corrected detector has mean scale `X` per centre. Paper III states this explicitly and does not claim that its reciprocal exceptional-set theorem controls the corrected arithmetic source.

## The single exact integer residual

For

\[
C_j(H;d)=\sum_{m+d\le H}
1_{\mathbb P}(m)1_{\mathbb P}(m+d)
1_{\mathbb P}(P_j+m)1_{\mathbb P}(P_j+m+d),
\]

one has pointwise

\[
Z_j^2=Z_j+2\sum_{1\le d<H}C_j(H;d).
\]

Define

\[
\mathcal R_X=
\sum_{j<N}\left[
Z_j+2\sum_{d<H}C_j(H;d)
-2\lambda_j^*Z_j+(\lambda_j^*)^2-\lambda_j^*
\right].
\]

Then, exactly,

\[
\boxed{
\sum_{j<N}|Z_j-\lambda_j^*|^2
=
\sum_{j<N}\lambda_j^*+\mathcal R_X.}
\]

This identity has been separately reconstructed in Lean in `FortuneFormal/Integer/BlockCriterion.lean`.

The unique mainline theorem is therefore:

> **INT-ISC — Integer centred sparse-covariance theorem.** There is a function `L(X)=o(log X)`, with `L(X)>=1`, such that
> \[
> \mathcal R_X\ll NXL(X)
> \]
> uniformly for the primorial block and `H=eta X^2`.

Because `sum lambda_j^* asymp NX`, INT-ISC gives the required variance bound and therefore every centre succeeds. It combines C1–C2 into one signed statement and forbids loss of centring.

## Dependency chain after reconstruction

\[
\text{INT-ISC}
\Longrightarrow
\sum_j|Z_j-\lambda_j^*|^2\ll NXL(X)
\Longrightarrow
Z_j>0\ \forall j
\Longrightarrow
F_n\text{ prime eventually}.
\]

The finitely many earlier indices are decidable by direct computation. Thus INT-ISC is sufficient for Fortune.

No reverse implication is claimed, and INT-ISC may be substantially stronger than Fortune.

## What was not found

The reconstruction found no hidden derivation of INT-ISC in Papers I–IV, no valid source-to-reciprocal bridge, and no theorem connecting the function-field papers or Paper VII to this integer residual.

## Publication ruling

Papers II–III should be retained as corrected conditional/structural papers. Their abstracts and theorem boundaries are materially accurate. A future consolidated integer paper should make INT-ISC the sole boxed frontier and move most reciprocal-model material to a clearly labelled structural or no-go section.
