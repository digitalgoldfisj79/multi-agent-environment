# Recentered one-sided source identity

Date: 27 July 2026  
Status: exact finite identity proved; corrected principal-term transference open.

## Detector

For a primorial centre `P_j`, let

\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m).
\]

Below `H<ell_{j+1}^2`, candidate collapse gives

\[
\Psi_j(H)=Y_j(H)+R_j(H),
\]

where `Y_j` is the output-weighted prime-pair detector and
`R_j(H)=O(X\log X)` is supported on proper output prime powers. Thus
`Psi_j` remains an exact, one-sided Fortune detector after recentering at the
prime-pair baseline

\[
\mu_j(H)=\mathfrak S(P_j)\int_{\ell_j}^{H}\frac{dt}{\log t}\asymp H.
\]

No explicit factor `Lambda(m)` is required for this formulation: offset
primality is encoded by candidate collapse on the prime-output support.

## Exact Fourier identity

Choose a finite interval containing all output values and put

\[
B_X(\theta)=\sum_n b_X(n)e(n\theta),
\qquad b_X(n)=\Lambda(n)
\]

on that interval and zero outside it. Define the finite interval kernel

\[
D_H(\theta)=\sum_{2\le m\le H}e(-m\theta).
\]

Then, exactly,

\[
\boxed{
\Psi_j(H)=\int_0^1D_H(\theta)B_X(\theta)e(-P_j\theta)\,d\theta.
}
\tag{1}
\]

Indeed, expansion and orthogonality force `n=P_j+m`.

Let

\[
F_X(\theta)=\sum_{j<N}e(\theta P_j),
\qquad
U_X(\theta)=D_H(\theta)B_X(\theta),
\qquad
M_X(\theta)=\sum_{j<N}\mu_j e(-P_j\theta).
\]

Squaring (1), summing over the block, and expanding the deterministic baseline
gives

\[
\boxed{
\begin{aligned}
\sum_{j<N}|\Psi_j-\mu_j|^2
={}&\iint_{[0,1]^2}
U_X(\alpha)\overline{U_X(\beta)}
F_X(\beta-\alpha)\,d\alpha d\beta\\
&-2\Re\int_0^1U_X(\alpha)M_X(-\alpha)\,d\alpha
+\sum_{j<N}\mu_j^2.
\end{aligned}
}
\tag{2}
\]

Thus the first exact path kernel is again the single-walk sum `F_X`.

## Relation to the old reciprocal frame

The old reciprocal pair-sum frame was obtained after a further pair lift and a
principal cancellation centred at the ordinary short-interval mean. Equation
(2) shows that candidate collapse does not refute a one-sided route. It does,
however, reopen its load-bearing principal term:

- the baseline is `mu_j`, not `H`;
- `mu_j/H` varies slowly with `j` and tends conjecturally to `e^gamma/2`;
- the correction is a square-root-sieve/Buchstab boundary phenomenon, not a
  constant that may be discarded before the pair lift;
- no theorem currently shows that subtracting this corrected principal term
  leaves the previously defined pair-sum residual.

The next exact obligation on Route A is therefore:

> Reconstruct the pair lift from (2), carry the nonconstant baselines `mu_j`
> through every diagonal and off-diagonal term, and identify whether the
> resulting residual equals the old reciprocal energy plus an explicitly
> controlled correction.

## Two-route programme

- **Route A — recentered one-sided source.** Start from (1)--(2), derive the
  corrected principal cancellation, and test whether the old pair-sum frame
  survives.
- **Route B — double-von-Mangoldt source.** Start from
  `T_j=sum Lambda(m)Lambda(P_j+m)` and its exact two-sided divisor/Fourier
  frames. Output-side small-prime sieve blindness prevents a naive symmetric
  truncation.

Neither route currently proves the required block variance. Route A is the
more direct test of whether Papers I--IV can be salvaged; Route B is the more
explicitly symmetric prime-pair source.
