# Focused integer Fortune programme closeout

**Programme:** `FORTUNE_INT_ISC_FOCUSED_V0_1`  
**Date:** 4 August 2026  
**Branch:** `gpt56/fortune-int-isc-focused-v01-20260804`  
**Outcome:** `REDUCED_TO_SMALLER_NEW_THEOREM`

## Final ruling

The focused programme has completed every registered research lane. It did not prove
Fortune's conjecture or the original covariance theorem `INT-ISC`. It replaced that
four-prime/full-variance target by a lower-arity one-form theorem and established explicit
obstructions to the available first-moment, four-prime, dispersion and frame routes.

## The reduction

For the registered primorial centres `P_j` and window `H=eta X^2`, define

\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m).
\]

At a centre whose interval contains no prime, candidate collapse and the prime-power
spacing argument give

\[
\Psi_j(H)=O(X\log X).
\]

Choose

\[
B_X=c_0X(\log X)^2
\]

for any fixed admissible `c_0>0`, and define

\[
\mathcal D_{\Psi}^-(X)=\sum_{j<N}(B_X-\Psi_j(H))_+^2.
\]

The terminal theorem is:

> **INT-PSLT — primorial selected lower-tail theorem.**
> \[
> \boxed{\mathcal D_{\Psi}^-(X)=o(B_X^2).}
> \]

At a failed centre the corresponding summand is `(1+o(1))B_X^2`. Therefore INT-PSLT
excludes every failed centre for sufficiently large `X`; candidate collapse then makes the
associated Fortunate numbers prime. The finite prefix is decidable separately.

INT-PSLT is not proved.

## Why this is a better target

- It is a one-form shifted-prime theorem rather than a four-prime covariance theorem.
- It discards all positive surplus.
- It requires weighted prime mass only at scale `X(log X)^2`, while the expected interval
  mass is of scale `H~X^2`.
- It retains the absolute one-defect resolution that Fortune requires.

The theorem is still much stronger than mere existence because any aggregate method must
make one failed row visible. That strength is unavoidable for a block argument.

## Completed gate results

### I1 — target audit

The full variance is not weakest. The one-sided lower-tail criterion `INT-LTQ` is strictly
weaker and sufficient. This implication is kernel checked in
`FortuneFormal/Integer/LowerTailCriterion.lean`.

### I2 — first-moment diagnostic

A signed first moment is not necessary after I1. Existing all-centre theorems work at
power-length intervals, while the required window is `(log P_j)^2`; almost-all theorems do
not restrict to the primorial path.

### I3 — four-prime lane

Raw four-prime bounds live at scale `NX^2`, while the original target is `NXL(X)`. Any
absolute-value implementation loses `X/L(X)`, and termwise displacement control would need
average signed error `L(X)/X`. The lane is closed absent a new aggregate lower-tail identity.

### I4 — shifted source

The exact shifted von Mangoldt source produces INT-PSLT. Generic short-interval, sieve and
explicit-formula methods do not reach it: the variable range is polynomial in `X`, while
the output factor and zero-analysis scales are exponential in `X`.

### I5 — source/orbit and PSD

For every `q|A_X`,

\[
F_X(a/q)=\sum_{j<N}e(P_ja/q)=N.
\]

The primorial walk is maximally coherent on its smooth rational skeleton. Geometry alone
cannot create the missing cancellation; the full local principal term must first be
subtracted.

### I6 — falsification

One-defect models preserve the first moment and alter the raw second moment by relative
`2/N=o(1)` while containing a failed centre. Local densities, relative moment estimates,
dense averages and smooth-modulus geometry are therefore insufficient.

## Exact remaining mathematical input

A proof must supply one-defect resolution on the actual increasing primorial centres,
through one of:

1. INT-PSLT directly;
2. a primorial-specific lower-bound sieve breaking the short-variable/large-output mismatch;
3. a correct Buchstab/Maier principal-term decomposition with a sufficiently small
   lower-tail residual;
4. a zero/source correlation theorem on the primorial logarithmic walk.

No established theorem found in the programme supplies this input.

## Explicitly not claimed

- INT-PSLT;
- INT-LTQ or INT-ISC;
- Fortune's conjecture;
- a prime-number theorem in logarithmic-square intervals;
- a function-field-to-integer transfer;
- relevance of Paper VII cubic incidence or direct function-field `d=1` to this reduction.

## Completion criterion

The programme closes under the preregistered status
`REDUCED_TO_SMALLER_NEW_THEOREM`: the original target was reduced to INT-PSLT, every
admitted lane reached a theorem or explicit obstruction, the implications are recorded,
and the remaining work is one named new theorem rather than an unbounded collection of
reformulations.
