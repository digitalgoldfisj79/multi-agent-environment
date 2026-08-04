# Focused INT-ISC programme

**Programme:** `FORTUNE_INT_ISC_FOCUSED_V0_1`  
**Date:** 4 August 2026  
**Base:** `deb6bb5468a951bc5485514c5848abcfcf386594`  
**Parent closeout:** PR #47  
**Primary issue:** #48  
**Status:** I0 PASSED; I1 READY

## Single objective

Determine whether the corrected integer Fortune route can prove, reduce, or rigorously obstruct the centred sparse-covariance theorem `INT-ISC` on the actual increasing primorial centres.

No other research lane is in scope. In particular, this programme may not spend proof-search or compute on:

- Paper VII cubic endpoint incidence;
- direct function-field `d=1`;
- random-order derandomisation;
- additional reciprocal-frame moments without a proved corrected-source bridge;
- finite scans presented as asymptotic evidence.

## Frozen target

For a dyadic block of primes

\[
X\le \ell_1<\cdots<\ell_N<2X,\qquad N\asymp X/\log X,
\]

put

\[
A_X=\prod_{p<X}p,\quad Q_j=\prod_{u\le j}\ell_u,\quad P_j=A_XQ_j,\quad H=\eta X^2
\]

with fixed `0<eta<1`. Define

\[
Z_j(H)=\sum_{2\le m\le H}1_{\mathbb P}(m)1_{\mathbb P}(P_j+m)
\]

and

\[
C_j(H;d)=\sum_{m+d\le H}
1_{\mathbb P}(m)1_{\mathbb P}(m+d)
1_{\mathbb P}(P_j+m)1_{\mathbb P}(P_j+m+d).
\]

The provisional deterministic baseline is

\[
\lambda_j^*(H)=\mathfrak S(P_j)
\int_{\ell_j}^{H}\frac{dt}{\log t\log(P_j+t)}.
\]

The centred residual is

\[
\mathcal R_X=\sum_{j<N}\left[
Z_j+2\sum_{d<H}C_j(H;d)-2\lambda_j^*Z_j+(\lambda_j^*)^2-\lambda_j^*
\right].
\]

The target is

\[
\boxed{\mathcal R_X\ll NXL(X),\qquad L(X)=o(\log X).}
\]

The programme first tests whether this formulation is the weakest sufficient target. Any replacement must be formally shown to imply the one-failure block criterion and must be strictly weaker or more tractable, not merely equivalent notation.

## Validation

Gate I0 passed in clean-clone job `6a7205146b79c09949c2236a`. The scale audit, focused static contract and inherited seven-paper closeout all passed with failure count zero.

## Completion conditions

The programme terminates only with one of:

1. a proof of `INT-ISC`;
2. a reduction to one precise established theorem with every exponent and uniformity condition verified;
3. a strictly smaller sufficient theorem with a proved implication to Fortune;
4. a rigorous obstruction proving that the selected method cannot reach the required loss.

`PROGRAMME.md` contains the ordered gates. `PREREGISTERED_GATES.json` is the machine-readable contract.