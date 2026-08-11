# Programme status after the four-point dilation gate

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the proposed four-point collision collapse has been run through its exact algebraic and lower-band gates. The collision kernel is proved, but it is the common-dilation/conductor-diagonal covariance rather than the complete deterministic square. The omitted cross-conductor terms have now been recovered as an exact signed dilation spectrum. Their total model energy and their low-conductor collision localization are proved. The deterministic sampling theorem remains open; Fortune's conjecture remains **OPEN**.

## 1. Exact four-point kernel

For ordinary source--centre pairs `\alpha=(j,m)` and `\beta=(k,n)`, put

\[
r_{\alpha,\beta,p}
\equiv
\frac{mP_k}{nP_j}\pmod p.
\]

The common-dilation covariance and conductor diagonal are exactly

\[
\mathcal K_R(\alpha,\beta)
=
\prod_{p:r_p=1}\frac{p-1}{p-2}
\prod_{p:r_p\ne1}\frac{(p-1)(p-3)}{(p-2)^2}
-1.
\]

For `P_k=P_jL_{jk}`,

\[
r_p=1
\iff
p\mid mL_{jk}-n.
\]

Self source coordinates reduce exactly to the band with their self primes removed, plus the already-isolated drift.

## 2. Critical correction

The positive kernel above is obtained by common-dilation averaging. In the character expansion this forces `Q=Q'` and `\chi=\psi`, so all Möbius signs square away.

The deterministic square contains the omitted terms

\[
Q\ne Q'
\quad\text{and}\quad
\chi\ne\psi.
\]

Therefore a collision-only `TT^*` or Linnik-dispersion argument would prove a model diagonal estimate, not `SMHLS(X)`.

## 3. Exact completion

The deterministic product has the exact dilation-frequency expansion

\[
g_R(ry)\overline{g_R(y)}
=
\mathcal K_R(r)
+
\sum_{\theta\ne1}\mathcal D_\theta(r)\theta(y).
\]

The nontrivial `\theta` modes contain every cross-conductor term and preserve the signed coefficient convolution.

Their exact total energy is

\[
\sum_{\theta\ne1}|\mathcal D_\theta(r)|^2
=
\delta_R^2
+
\kappa_R(r)(1-\delta_R)^2
-
\kappa_R(r)^2,
\]

where `\delta_R=V_R^{-1}-1` and `\kappa_R=\mathcal K_R`.

## 4. Low dilation conductors

At `H=\eta X^2`, every dilation conductor with at least two band primes exceeds `H`. The low spectrum is exactly `\operatorname{cond}\theta=p`.

For `p\asymp R`:

- away from `p\mid mP_k-nP_j`, the summed single-prime mode energy is `O(R^{-3})` up to the reduced-band collision factor;
- at a collision prime it is `O(R^{-1})`.

Thus the completed signed low spectrum genuinely localizes on

\[
p\mid mL_{jk}-n.
\]

This is the usable remnant of the proposed dispersion route.

## 5. Sharp no-go for generic transfer

The translations of the survivor residual span the full mean-zero space on

\[
\Omega_R=\prod_p\mathbb F_p^\times.
\]

Point evaluation relative to normalized complete-dilation energy has squared norm exactly

\[
|\Omega_R|-1.
\]

Hence no bounded arbitrary-weight transfer from the model average to the deterministic point can hold. Any proof must use the rigid prime source and primorial geometry.

## 6. Finite gate

All exact verifiers pass. On a 51-point prime-source panel with band `[13,17,19]`,

\[
|T|^2\approx10.3154,
\qquad
T_{\rm diagonal}\approx5.02963,
\qquad
T_{\rm cross}\approx5.28580.
\]

The cross-conductor defect is not a lower-order correction and can have either sign.

## 7. Current boundary

**PROVED EXACTLY**

- four-point common-dilation kernel;
- collision reduction `p\mid mL_{jk}-n`;
- self-coordinate reduction;
- signed dilation-Wigner completion;
- exact mode-energy identity;
- low single-prime mode localization;
- sharp arbitrary-weight point-evaluation obstruction.

**CLOSED**

- collision-only dispersion after conductor diagonalization;
- arbitrary-weight model-to-point transfer.

**OPEN**

- deterministic sampling of the nontrivial dilation modes;
- a joint low-mode large-sieve/collision-dispersion theorem preserving the `\theta` sum;
- `SMHLS(X)` / `PCRST(X)`;
- `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

Authoritative note:

- `frontier/integer_source_frame_bridge/FOUR_POINT_DILATION_KERNEL_AND_SIGNED_AUTOCORRELATION_20260729.md`
