# Corrected source-to-frame audit

Date: 27 July 2026  
Branch: `gpt56/fortune-mainterm-correction-programme-20260727`

## Ruling

The old pair-sum reciprocal frame is not presently a proved reduction of the Fortune detector. Candidate collapse adds a second prime condition on the offset. Any exact source decomposition must retain both prime factors and their shared offset variable.

This does not refute the internal reciprocal-frame theorems. It changes their status from principal Fortune route to independent deterministic model until a new transference theorem is proved.

## Exact corrected source

For

\[
T_j(H)=\sum_{2\le m\le H}\Lambda(m)\Lambda(P_j+m),
\]

let

\[
A_H(\theta)=\sum_{2\le m\le H}\Lambda(m)e(-m\theta)
\]

and let `B_X` be the finite Fourier transform of `Lambda(n)` on the union of all shifted intervals under consideration. Then

\[
T_j(H)=\int_0^1 A_H(\theta)B_X(\theta)e(-P_j\theta)\,d\theta.
\]

Consequently the exact block second moment has kernel

\[
F_X(\beta-\alpha)=\sum_{j<N}e((\beta-\alpha)P_j),
\]

not the pair-sum polynomial as its first harmonic object. The pair-sum kernel may reappear only after an additional lift or fourth-moment operation.

## Failure contamination

If a centre contains no prime output, every nonzero term in `T_j` has `P_j+m` equal to a proper prime power. There is at most one such power for each exponent, giving

\[
T_j(H)=O(X(\log X)^2).
\]

The conjectural main term is

\[
\nu_j(H)=\mathfrak S(P_j)H\asymp H\log X.
\]

Thus a random-scale variance

\[
\sum_j|T_j-\nu_j|^2
\ll NHX(\log X)^2L(X),\qquad L(X)=o(\log X),
\]

still excludes every failed centre.

## Why the old frame does not yet transfer

The old frame has rows depending on the output-side reciprocal shell and columns indexed by pair sums of `P_j`. Its coefficients do not contain the factor `A_H`, or any equivalent exact encoding of offset primality. Paper II's semiprime-resonance theorem already shows that this factor cannot be replaced by a positive density without losing the required centring.

Therefore one of the following must be proved:

1. an exact two-sided divisor/Mobius decomposition of the double-von-Mangoldt source;
2. a signed inequality eliminating the offset-prime factor without replacing it by density;
3. a new frame whose rows retain both divisor systems.

No such theorem is currently in the repository.

## Next mathematical gate

Expand both von Mangoldt factors with a common truncation and delay absolute values until after the principal prime-pair main term is removed. The first milestone is a finite exact identity of the form

\[
\sum_j|T_j-\nu_j|^2
=\mathcal D_{\rm small}+\mathcal R_{\rm signed}+\mathcal E_{\rm trunc},
\]

where `R_signed` retains the coupled divisor variables and `E_trunc=o(NHX(log X)^2 log X)` at the all-centres threshold.

Until this identity exists, further work on HTE4 or random-order derandomisation is not on the critical path.
