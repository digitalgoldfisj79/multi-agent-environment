# Programme status after full-source completion sequence

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

## Result

The Fable repair sequence has been executed through the exact long-cell completion, determinant reordering, actual-coefficient calibration and higher-conductor compatibility gates.

The unbalanced-cell flaw is closed. The source-cell decomposition resums exactly to the von Mangoldt function before estimation:

\[
\sum_{d\le Y}\mu(d)c_Y(n/d)=\Lambda(n).
\]

Consequently, the completed physical coordinate is the ordinary prime progression discrepancy

\[
D_p(-P_j)
=
\psi(H;p,-P_j)-\frac{\Psi_p(H)}{p-1},
\]

with the band-prime source `n=p` reinserted as the explicit drift `log p/(p-2)`.

## Main correction

The proposed uncentred signed-determinant form is not the correct full-source theorem. After source recombination its hit term contains a density main term of order

\[
H^2/\log X,
\]

which is polynomially above the desired scale. The exact required kernel is centred:

\[
\mathbf 1_{\exists p\in\mathcal P_R:p\mid n-n'}
-
\sum_{p\in\mathcal P_R}\frac1{p-1}.
\]

## New physical boundary

The first physical diagonal is now the prime-restricted variance

\[
\mathcal V_{\mathcal P_R}(H)
=
\sum_{p\in\mathcal P_R}
\sum_{a\in\mathbb F_p^\times}
\left|
\psi(H;p,a)-\frac{\Psi_p(H)}{p-1}
\right|^2.
\]

The required theorem is

\[
\boxed{
\mathcal V_{\mathcal P_R}(H)
\ll HX X^{o(1)},
\qquad H\asymp X^2.
}
\]

The standard sparse-modulus/character large sieve gives `HX log H`, losing one logarithm. Existing sparse BDH estimates save logarithms from the `H^2` scale but remain polynomially too large at the square-root transition. No directly applicable published prime-modulus variance theorem was found that supplies the missing logarithm.

## Higher-conductor boundary

Even the physical theorem above would not finish the first band. The exact complete survivor remains

\[
\mathcal F_{j,R}
=
(V_R^{-1}-1)\psi(H)
+V_R^{-1}
\sum_{\varnothing\ne S\subseteq\mathcal P_R}
(-1)^{|S|}
\sum_{n\le H,\ Q_S\mid P_j+n}\Lambda(n).
\]

For `|S|\ge2`, `Q_S>H`, so each term samples at most one source value. The physical and one-point components have sign-indefinite covariance; finite panels confirm that the first/higher cross term changes sign and is not negligible.

## Audit

### PROVED EXACTLY

- true-range long-cell completion;
- resummation to direct `Lambda` residue classes;
- character completion to ordinary `Lambda` character sums;
- exact self-coordinate isolation;
- centred determinant reordering;
- complete source/high-conductor inclusion--exclusion interface.

### PROVED FROM CLASSICAL INPUT

- the uncentred full-source determinant target is too large by a polynomial factor.

### COMPUTATIONALLY VERIFIED

- formal identities on `X=11,17,23`;
- actual-source variance panels through `X=337`;
- prime-band variance ratios remain bounded on those panels;
- full survivor first/higher/cross recombination.

### CLOSED OR REPLACED

- the unbalanced support gap;
- the arbitrary Möbius fourth-moment formulation after full source recombination;
- uncentred `SDD(X)` as the final physical theorem;
- separate positive physical/high-conductor bounds.

### OPEN

- the prime-band centred BDH estimate at `H\asymp X^2`;
- primorial-centre cross-modulus restriction;
- coherent physical/high-conductor contraction;
- the first physical-band theorem, `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

## Decisive stopping theorem

The exact and directly applicable classical stages of this sequence are exhausted. The next genuinely new arithmetic input is:

\[
\boxed{
\text{one-logarithm prime-modulus BDH saving at the square-root transition,}
}
\]

followed by the already-explicit signed one-point conductor transfer.
