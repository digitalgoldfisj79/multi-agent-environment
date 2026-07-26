# Main d=1 status after the boulders-first execution

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-boulders-hayes-first-20260725`  
**Target:** FF-Fortune `(p,1)` for every prime `p`.  
**Ruling:** the crown remains **OPEN**. The programme has reached a theorem-level obstruction requiring genuinely new characteristic-`p` Frobenius mathematics.

## 1. Exact target

It is sufficient to prove that for every prime `p>=3` there is an irreducible polynomial

\[
T^p+aT^3+bT^2+cT+d,
\qquad(a,b)\ne(0,0),
\]

over `F_p`. Equivalently, there is a successful offset of degree two or three from

\[
T^p-T.
\]

The theorem is machine-certified for the existing finite range, but no finite calculation proves the uniform statement.

## 2. Outcome of the first analytic boulder

The proposed two-parameter Hayes correlation route has been completely resolved.

### 2.1 Universal rank-four Hayes system

The degree-at-most-four Hayes polynomials are the Frobenius polynomials of

\[
\mathscr H
=R^1\pi_!
\left(
\mathcal L_\chi(x)
\otimes
\mathcal L_\psi(wx^3+ux+v/x)
\right).
\]

Its generic rank is four. The two parameter planes used in the terminal correlation reduce exactly to the `w=1` family projected to nonsquare `v`, plus a degree-drop correction.

### 2.2 Reciprocal quartic and orientation cover

For

\[
L(z)=1+C_1z+C_2z^2+C_3z^3+C_4z^4,
\]

put

\[
a=\chi(v/(3w)),
\qquad b=\chi(-1).
\]

The exact coefficient identities are

\[
C_3=paC_1,
\qquad
C_4=p^2ab.
\]

In the opposite-sign sector `a=-b`, one also has `C_2=0` and a fixed quadratic factor splits off. The arithmetic nonsquare projector selects the same-sign reciprocal sector.

The orthogonal orientation character is

\[
\mathcal L_\chi(-v/(3w)),
\]

and its double cover is

\[
y^2=-v/(3w).
\]

### 2.3 Exact Spin/tensor factorisation

On the orientation cover, the rank-four family factorises through the rank-two cubic Airy system

\[
\mathscr E
=R^1\varpi_!\mathcal L_\psi(4r^3+tr).
\]

With

\[
t_+=u+6y,
\qquad t_-=u-6y,
\]

the off-diagonal orientation family is, after the explicit Gauss twist,

\[
t_+^*\mathscr E\otimes t_-^*\mathscr E.
\]

The diagonal is the corresponding symmetric-square degree-drop fibre.

After summing the parameter plane, the off-diagonal and diagonal terms telescope and give

\[
\sum_{u,y}\operatorname{Tr}(F^p|\mathscr K_2)
=
\frac{\chi(-1)}{G_p^p}
\left[
\left(\sum_tJ_p(t)\right)^2-p^{p+1}
\right].
\]

The one-dimensional Salie boundary cancels the scalar term, while

\[
\sum_tJ_p(t)=-pT_p.
\]

Therefore the entire Hayes correlation is an explicit scalar multiple of

\[
p^2T_p^2.
\]

### Ruling

\[
\boxed{
\text{The two-parameter Hayes route is exactly circular.}
}
\]

It does not manufacture a new factor-`p` cancellation. It squares the original missing one-parameter Airy cancellation.

Read:

- `UNIVERSAL_HAYES_SHEAF_AND_ONE_FAMILY_REDUCTION_20260725.md`;
- `HAYES_QUARTIC_FUNCTIONAL_EQUATION_AND_SQUARE_CLASS_DICHOTOMY_20260725.md`;
- `HAYES_ORIENTATION_COVER_AND_TELESCOPING_CORRELATION_20260725.md`;
- `HAYES_ORIENTATION_TENSOR_FACTORIZATION_AND_CIRCULARITY_20260725.md`.

## 3. Direct Airy boulder

The irreducible analytic theorem remains

\[
\boxed{
|T_p|\le C p^{(p-1)/2}
}
\]

or equivalently

\[
\boxed{
\left|
\operatorname{Tr}(F|U_p)
-p\operatorname{Tr}(F|U_{p-2})
\right|
\le C p^{(p+1)/2}.
}
\]

The boulders-first run confirms the following exact boundary.

1. The modular rank-two Adams collapse is real.
2. The natural integral Dwork lift has generic defect rank `p-1` before projection and linear surviving rank after projection; bounded-rank compression is false for that lift.
3. Arithmetic Picard--Lefschetz contributes exactly one Tate line at `k=p` and none at `k=p-2`.
4. After removing that line, the two generic Airy motives are equal-weight and Hodge-disjoint. There is no characteristic-zero motivic correspondence pairing them.
5. The combined projective Salie sum is exactly
   \[
   T_p^2/p^{(p+1)/2},
   \]
   so it is another exact reformulation, not an independent cancellation source.

Thus the remaining statement is a genuinely new characteristic-`p`, Frobenius-dependent numerical correlation between Hodge-disjoint motives, or an Airy-specific integral Smith-defect theorem controlling the free cyclic Frobenius trace.

## 4. Application boulder

The application-side coefficient transport is already complete in the stronger global form

\[
R\pi_!\mathcal L
\cong
 i_!\mathcal O(-(p-4))[-2(p-4)].
\]

It controls all nonsplit Jordan extensions, Frobenius and cyclic projectors before passage to the residual complex. The residual object is exactly the finite-flat cubic-tail ordered-root cover and its q-line plus boundary decomposition.

What remains is not another coefficient elimination. It is the same Airy-specific integral Smith defect:

- at the cubic origin it is the terminal Airy trace;
- after Fourier integration it is the nonzero-frequency q-line contribution.

The simple formula identifying either global q-line projector with the normalized Airy trace plus only `q=2` and `q=infinity` corrections is exactly false in the calibrated cases. Substantial generic nonzero-frequency trace remains.

Hence the analytic and application boulders are two specialisations of one missing theorem, not independent tasks that can be completed in either order.

## 5. Constructive bypasses tested

### 5.1 Fixed boundary and fixed q cells

Both finite boundary readings can vanish simultaneously; this happens at `p=53` and `p=71`.

The natural fixed interior values

\[
q_0\in\{-5,-4,-3,-2,-1,1,3,4,5,6,7\}
\]

all have an admitted prime at which the complete split q-cell contains no irreducible fibre. The last survivor, `q_0=5`, fails at `p=53`.

Therefore neither a fixed boundary nor any tested low-height fixed interior cell can carry a uniform witness theorem.

### 5.2 Artin--Schreier Tschirnhaus transforms

Let

\[
\alpha^p-\alpha=1.
\]

A complete trace calculation proves that no polynomial transform

\[
\beta=h(\alpha)
\]

of degree two, three or four can satisfy

\[
\operatorname{Tr}(\beta^m)=0
\qquad(1\le m\le p-4)
\]

for admitted `p>=11`. Every non-affine Möbius transform fails already at the first trace. Affine transforms give only the excluded Artin--Schreier linear/constant tail.

Thus a constructive escape must use a transform of degree at least five, a genuinely multivariate construction, a more complicated rational transformation, or a different extension.

Read:

- `ARTIN_SCHREIER_LOW_DEGREE_TSCHIRNHAUS_NO_GO_20260725.md`;
- `FIXED_INTERIOR_QLINE_CELL_NO_GO_20260725.md`.

## 6. What remains genuinely live

There are now three logically distinct possibilities.

### A. New integral Smith-defect theorem

Construct an Airy-specific Frobenius-compatible integral filtration of the free cyclic part and prove

\[
|\delta_F(K_{free})|
\le C p^{(p+1)/2}
\]

with an absolute constant.

This would simultaneously solve the analytic Airy trace and its application transport.

### B. New Frobenius-correlation theorem

Prove directly

\[
\left|
\operatorname{Tr}(F|U_p)
-p\operatorname{Tr}(F|U_{p-2})
\right|
\ll p^{(p+1)/2}
\]

using characteristic-`p` arithmetic not induced by a characteristic-zero motivic morphism.

### C. A genuinely different constructive or mass-formula proof

Produce one explicit cubic-tail irreducible for each `p` without estimating the Airy defect, or exclude simultaneous failure of both arithmetic classes by a new exact invariant. The fixed-cell, boundary-only, low-degree Artin--Schreier and known Cartier-support variants are closed.

## 7. Verification record

Exact remote checks performed in this execution include:

1. `6a64f7fddb23d7a7ec1cca64`: quartic Hayes functional equations and square-class dichotomy;
2. `6a6504317ef3c08464968f58`: symmetric-square and orientation tensor factorisation at `p=5,11,17`;
3. `6a650303db23d7a7ec1ccdd4` and `6a65063f7ef3c08464968fcb`: Artin--Schreier trace no-go through quartic transforms;
4. `6a650597db23d7a7ec1cceca`: fixed q-cell first-failure table.

## 8. Honest stopping point

The programme has not proved `d=1`.

It has, however, hit the main boulders in the correct order and obtained decisive information:

- the proposed bounded-state Hayes route is closed by an exact tensor-factorisation theorem;
- the direct bounded-rank Adams lift is closed by a proved linear-rank defect;
- the projective character formulation is the exact square of the same trace;
- the application comparison is the same integral Smith defect after Fourier integration;
- the simplest constructive escapes are closed through quartic transforms and fixed q-cells.

Further progress requires a genuinely new theorem of type A, B or C above. Another equivalent averaging, associated-graded calculation, local conductor computation or low-prime pattern would not move the crown.
