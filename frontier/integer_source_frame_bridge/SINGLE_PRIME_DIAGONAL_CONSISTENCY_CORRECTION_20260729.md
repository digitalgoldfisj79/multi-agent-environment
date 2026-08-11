# Single-prime diagonal consistency correction and restored same-band boundary

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: an exact consistency audit shows that the newly named first-band theorem `SW1BDH(X)` is not a new missing logarithmic-saving theorem for the frozen Fortune first-order coordinate. On the first physical band its local one-residue discrepancy is exactly the already-established same-band diagonal coordinate, with opposite sign. The established diagonal bound is therefore already stronger than the proposed `SW1BDH(X)` target. The genuine open theorem remains the coherent cross-modulus same-band square `SBD(X)` (or a full normalized-survivor transfer which avoids separating first order). Fortune's conjecture remains **OPEN**.

## 1. Why this audit was necessary

The conductor-`p` dilation calculation produced the exact identity

\[
E_{j,p}
=
\sum_m a_{j,m}\xi_p(-mP_j^{-1}),
\]

and rewrote it as one moving residue-class discrepancy. A generic multiplicative large-sieve estimate with logarithmic von Mangoldt-type source weights gives `KHX log X`, suggesting a missing logarithmic saving.

The frozen Fortune first-order coordinate on the branch, however, does not use that substituted source model. Its first physical band uses the constant source coefficient `\beta_j` on the prime set

\[
\mathcal M_Z=\{m:Z<m\le H,\ m\text{ prime}\},
\]

with the self source `m=p` removed at modulus `p`.

The new coordinate must therefore be compared directly with the already-proved frozen discrepancy before introducing a generic source norm.

## 2. Exact first-band identification

For a physical prime `p>Z`, put

\[
N_{P_j,Z}(p)
=
\#\{m\in\mathcal M_Z:\ m\ne p,\ p\mid P_j+m\}.
\]

The established frozen discrepancy and same-band coordinate are

\[
D_j(p)
=
N_{P_j,Z}(p)-\frac{M_Z-1}{p-1},
\qquad
 a_{j,p}
=
\beta_j\frac{p-1}{p-2}D_j(p),
\]

where `M_Z=|\mathcal M_Z|`.

For the ordinary source coordinates on the first physical band, take

\[
a_{j,m}=\beta_j\mathbf 1_{m\in\mathcal M_Z,\ m\ne p}.
\]

The one-residue identity gives

\[
\begin{aligned}
E_{j,p}
&=
-\frac{p-1}{p-2}
\left[
\beta_jN_{P_j,Z}(p)
-
\frac{\beta_j(M_Z-1)}{p-1}
\right]\\
&=
-\beta_j\frac{p-1}{p-2}
\left[
N_{P_j,Z}(p)-\frac{M_Z-1}{p-1}
\right].
\end{aligned}
\]

Hence:

### Theorem 2.1 — exact first-band spectral identification

\[
\boxed{E_{j,p}=-a_{j,p}.}
\]

This includes the self-source exclusion exactly. No asymptotic input is used.

## 3. Consequence for the purported logarithmic gap

Squaring and summing gives

\[
\boxed{
\sum_{j\in B}\sum_{p\in\mathcal P_R}|E_{j,p}|^2
=
\sum_{j\in B}\sum_{p\in\mathcal P_R}|a_{j,p}|^2
=D_{B,R}.
}
\]

The branch already has the first-order diagonal theorem

\[
\sum_R D_{B,R}\ll\frac{KHX}{\log X}.
\]

Therefore the first-band local-mode diagonal satisfies the proposed `SW1BDH(X)` shape with the stronger choice

\[
L(X)=\frac1{\log X}.
\]

The `KHX\log X` estimate in the preceding note is a valid generic large-sieve bound for a broader logarithmically weighted source class. It is not the sharp boundary for the actual frozen first-band Fortune coefficient system.

Accordingly, `SW1BDH(X)` is **RETRACTED AS A NEW FIRST-BAND OBSTRUCTION**.

## 4. What remains open

The open same-band quantity is not the sum of individual squares. It is the square of their coherent sum:

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{p\in\mathcal P_R}E_{j,p}
\right|^2.
}
\]

Using `E_{j,p}=-a_{j,p}`, this is exactly

\[
\sum_{j\in B}|T_{B,R}(j)|^2,
\qquad
T_{B,R}(j)=\sum_{p\in\mathcal P_R}a_{j,p},
\]

whose expansion is

\[
D_{B,R}
+
2\Re\sum_{p<s}C_B(p,s).
\]

The established diagonal theorem controls `D_{B,R}`. The missing theorem is the signed aggregate cross-modulus covariance:

### Open theorem `SBD(X)`

\[
2\Re\sum_{p<s}C_B(p,s)
\ll
D_{B,R}+E_{B,R},
\]

with dyadically summable Fortune-scale errors.

This is the same theorem-level obstruction isolated before the dilation detour.

## 5. Later-band qualification

For later normalized-survivor bands, the coefficient has the form

\[
A^{<R}_{j,m}
=
\text{base source weight}\times
\text{previous-band survivor history}.
\]

It is no longer constant in `m`, and Theorem 2.1 does not identify that weighted coordinate with the original frozen diagonal. A survivor-weighted one-residue estimate can still occur as a conditional martingale component.

That later-band extension is not, however, the first lower-band gate that was just claimed to miss by one logarithm. It belongs to the full deterministic survivor-transfer problem and must remain coupled to the reduced-band correction, higher dilation modes and cross-band covariance.

## 6. Route audit after the correction

Sparse-modulus large-sieve and Barban--Davenport--Halberstam theorems control positive conductorwise or residuewise quadratic energies. Applied here they recover or generalize the already-controlled diagonal. They do not estimate the coherent all-ones modulus vector

\[
\sum_pE_{j,p}
\]

or the signed `p\ne s` covariance.

Similarly, a positive collision/noncollision split remains invalid: the exact finite panel already shows that its two pieces can be more than forty times the signed total.

Thus the next valid choices are unchanged:

1. prove `SBD(X)` by a genuinely joint cross-modulus dispersion theorem for the moving primorial residue; or
2. abandon separate first-order control and estimate the complete normalized-survivor band, retaining first/higher-order and drift/hit cancellation from the outset.

## 7. Exact verification

The committed verifier checks, in rational arithmetic:

1. nine coordinate identities `E_{j,p}=-a_{j,p}` on the centres `30,210,2310`, band primes `13,17,19`, and the full prime source `11<m\le97`;
2. exact equality of the accumulated local-mode energy and established same-band diagonal energy;
3. the self-source exclusion `m=p`;
4. the qualification that a genuinely nonconstant later-band source weight is not covered by the constant-weight identification.

## 8. Boundary

**PROVED EXACTLY**

1. first-band one-residue low mode equals the established frozen coordinate with opposite sign;
2. first-band low-mode diagonal energy equals `D_{B,R}`;
3. self-source exclusion is consistent in both formulations.

**ALREADY PROVED ON THE BRANCH**

1. `\sum_R D_{B,R}\ll KHX/\log X`.

**RETRACTED**

1. `SW1BDH(X)` as a new first-band logarithmic-saving obstruction;
2. the claim that the generic `KHX\log X` large-sieve estimate is the sharp bound currently known for the actual frozen first-band coefficient system.

**OPEN**

1. signed cross-modulus same-band dispersion `SBD(X)`;
2. later-band survivor-weighted conditional coordinates;
3. the full deterministic normalized-survivor transfer;
4. `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.
