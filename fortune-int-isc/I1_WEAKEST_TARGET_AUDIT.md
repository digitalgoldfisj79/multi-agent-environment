# Gate I1 — weakest-sufficient-target audit

**Date:** 4 August 2026  
**Programme:** `FORTUNE_INT_ISC_FOCUSED_V0_1`  
**Ruling:** the full centred variance `INT-ISC` is not the weakest useful sufficient theorem

## 1. Full variance target

Write

\[
V_X=\sum_{j<N}(Z_j-\lambda_j)^2,
\qquad cX\le \lambda_j\le CX.
\]

The original target was

\[
V_X\ll NXL(X),\qquad L(X)=o(\log X).
\]

Since one failed centre has `Z_j=0`, it contributes at least `c^2X^2`; because
`N\asymp X/\log X`, the target excludes every failure.

## 2. Strictly weaker quadratic lower-tail target

Define

\[
D_X^-=
\sum_{j<N}\bigl(\lambda_j-Z_j\bigr)_+^2,
\qquad u_+=\max(0,u).
\]

Pointwise,

\[
(\lambda_j-Z_j)_+^2\le (Z_j-\lambda_j)^2,
\]

so `INT-ISC` implies

\[
\boxed{D_X^-\ll NXL(X),\qquad L(X)=o(\log X).}
\tag{INT-LTQ}
\]

At a failed centre, `Z_j=0`, and the corresponding summand is
`\lambda_j^2\ge c^2X^2`.  The right side is

\[
NXL(X)\asymp X^2\frac{L(X)}{\log X}=o(X^2),
\]

so `INT-LTQ` excludes every failure.

This implication and the pointwise domination by the full variance are formalized in
`FortuneFormal/Integer/LowerTailCriterion.lean`.

## 3. Strictness

`INT-LTQ` is genuinely weaker, not equivalent notation.  For example, if
`Z_j=2\lambda_j` at every centre, then

\[
D_X^-=0,
\qquad
V_X=\sum_j\lambda_j^2\asymp NX^2.
\]

Thus arbitrarily large positive surplus is invisible to the new target.

The same example shows that the sparse signed first-moment estimate

\[
\sum_j(Z_j-\lambda_j)=O\bigl(N\sqrt{XL(X)}\bigr)
\]

is **not necessary** for `INT-LTQ` or for the one-failure argument.  Gate I2 was a
necessary consequence of the overstrong full variance target, not a necessary step toward
Fortune.

## 4. Shifted-prime formulation

Candidate collapse also gives an exact one-form formulation.  Put

\[
\Theta_j(H)=\sum_{2\le m\le H}\theta(P_j+m),
\]

where `theta(n)=log n` for prime `n` and zero otherwise.  For sufficiently large `X`,

\[
\Theta_j(H)>0\quad\Longleftrightarrow\quad Z_j(H)>0.
\]

Indeed, any prime `P_j+m` in the registered window forces `m` to be prime.  Therefore
the existence problem is a selected-centre prime theorem in intervals of length

\[
H\asymp X^2\asymp (\log P_j)^2,
\]

not intrinsically a four-prime theorem.  Four-prime correlations arise only when one
chooses the full second moment of `Z_j`.

A barrier based at the weight of one prime is essentially equivalent to the conclusion
itself.  A barrier based at the conjectural mean is quantitatively stronger but has analytic
room.  `INT-LTQ` is retained as the primary non-tautological target, while the shifted
Chebyshev formulation is the preferred analytic source.

## 5. Rejected alternatives

- **Signed first moment alone:** positive surpluses can hide a failed centre.
- **Density-one success:** insufficient because the block must contain zero failures.
- **Average in `H`:** insufficient unless the averaging theorem has a monotone or pointwise
  consequence at the registered square-boundary window.
- **Raw upper-bound sieve:** controls abundance from above and cannot produce the needed
  lower tail.
- **A threshold at one prime weight:** valid but essentially restates eventual Fortune.
- **Full absolute residual control:** stronger than both the original one-sided residual and
  `INT-LTQ`.

## 6. Gate ruling

Gate I1 passes with a strict target substitution:

- `INT-ISC` is retained as an optional stronger theorem;
- `INT-LTQ` becomes the primary quantitative target;
- the shifted-prime lower-tail theorem becomes the principal analytic route;
- I2 is retired as a mandatory gate and retained only as a diagnostic audit;
- I3–I5 may proceed without first proving a sparse signed first moment, provided every lane
  preserves the one-sided lower tail.

This ruling does not prove `INT-LTQ` or Fortune.  It removes an unnecessary upper-tail and
first-moment burden from the programme.
