# Programme status after the single-prime dilation attack

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the proposed conductor-`p` large-sieve/collision-dispersion programme has been run through its exact algebraic and standard analytic gates. The low dilation layer is now an exact first-order survivor martingale projection. Its leading term is a one-residue prime-distribution discrepancy. The classical multiplicative large sieve gives the correct polynomial scale but loses one logarithm relative to the Fortune target. Collision and noncollision terms cannot be separated positively without destroying large signed cancellation. Fortune's conjecture remains **OPEN**.

## 1. Exact low-mode collapse

For

\[
s_p(z)=\frac{p-1}{p-2}\mathbf1_{z\ne1},
\qquad
\xi_p=s_p-1,
\]

the complete conductor-`p` layer is

\[
\mathcal L_p(r,y)
=
[\xi_p(r_py_p)\xi_p(y_p)-\kappa_p(r_p)]
+
\kappa_{-p}(r)
[s_p(r_py_p)s_p(y_p)-(1+\kappa_p(r_p))].
\]

Thus it is the first-order conditional projection of the full pair survivor process: a local deterministic-point defect plus an exact reduced-band correction.

## 2. Arithmetic interpretation

For

\[
x_{j,m,p}\equiv-mP_j^{-1}\pmod p,
\]

one has

\[
x_{j,m,p}=1
\iff
p\mid P_j+m.
\]

For arbitrary source weights,

\[
\sum_m a_{j,m}\xi_p(x_{j,m,p})
=
-\frac{p-1}{p-2}
\left[
\sum_{m\equiv-P_j\pmod p}a_{j,m}
-
\frac1{p-1}\sum_{(m,p)=1}a_{j,m}
\right].
\]

The low-mode theorem is therefore a survivor-weighted one-residue Barban--Davenport--Halberstam problem at prime moduli `p\asymp X`.

## 3. Standard analytic gate

The multiplicative large sieve yields

\[
\sum_{j\in B}\sum_{p\asymp X}
\left|
\sum_m A^{<R}_{j,m}\xi_p(x_{j,m,p})
\right|^2
\ll
KHX\log X
\]

at `H\asymp X^2`, already in the unsieved logarithmic prime-source baseline.

The Fortune variance programme requires

\[
KHX\,L(X),
\qquad
L(X)=o(\log X).
\]

The remaining first-order theorem therefore requires a genuine logarithmic saving beyond the generic large sieve.

## 4. Collision/noncollision gate

The individual-mode model energy localizes at

\[
p\mid mP_k-nP_j.
\]

After summing the complete conductor-`p` character family, the layer depends on endpoint hits `p\mid P_j+m` and `p\mid P_k+n`. Collision and noncollision pieces both contain the dense drift/sparse-hit cancellation.

On the frozen 51-point panel,

\[
\mathcal L_{\rm total}\approx-0.590395,
\]

but

\[
\mathcal L_{\rm coll}\approx-13.4166,
\qquad
\mathcal L_{\rm noncoll}\approx12.8262.
\]

Their absolute split is about `44.45` times the signed total. A positive collision/noncollision proof is therefore rejected unless it preserves the interface cancellation.

## 5. Remaining theorem

### `SW1BDH(X)`

Prove the survivor-weighted one-residue discrepancy estimate

\[
\sum_{j\in B}\sum_{p\in\mathcal P_R}
\left|
\sum_m A^{<R}_{j,m}\xi_p(-mP_j^{-1})
\right|^2
\ll
KHX\,L(X),
\qquad
L(X)=o(\log X),
\]

jointly with:

- the exact reduced-band correction;
- self coordinates;
- the zeroth coordinate;
- the higher dilation spectrum and later cross-band covariance.

`SW1BDH(X)` is the first-order lower-band component of `SMHLS(X)` / `PCRST(X)`.

## 6. Boundary

**PROVED EXACTLY**

- first-order conditional-projection identity;
- tensor decomposition;
- endpoint collapse;
- weighted one-residue discrepancy identity;
- sharp first-order point-evaluation obstruction.

**PROVED FROM CLASSICAL INPUT**

- the generic `KHX log X` large-sieve bound.

**COMPUTATIONALLY VERIFIED**

- 1152 complete-group exact identities;
- the exact 51-point collision/noncollision and local/correction decomposition.

**CLOSED**

- generic large sieve without a logarithmic saving;
- positive collision/noncollision separation;
- arbitrary-weight first-order model-to-point transfer.

**OPEN**

- `SW1BDH(X)`;
- the reduced-band correction at the same scale;
- higher dilation conductors;
- `SMHLS(X)` / `PCRST(X)`;
- `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

Authoritative note:

- `frontier/integer_source_frame_bridge/SINGLE_PRIME_DILATION_LAYER_AND_LOG_GAP_20260729.md`
