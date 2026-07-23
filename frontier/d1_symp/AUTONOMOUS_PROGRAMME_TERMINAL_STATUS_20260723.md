# Autonomous `d=1` programme — terminal status after all decision gates

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-collapse-integration-20260723`  
**Scope:** function-field `d=1` Fortune sibling, primarily `p == 2 mod 3`.

## 0. Stop criterion

The programme was instructed to continue through:

1. the two-variable alternating correspondence;
2. the `mu_3`-projected Dwork defect;
3. the global character/period decomposition;
4. literature and realization-theoretic matching;

and to stop only when the surviving step required genuinely new mathematics rather than another derivation, computation or application of a known theorem.

That criterion has now been met.

## 1. Frozen target

For `p=6r+5`, define

\[
U_k=H_c^1(\mathbb A^1_{\overline{\mathbb F}_p},\operatorname{Sym}^k\mathcal A)^{\mu_3}.
\]

The Chuang audit proved

\[
\dim U_p=\dim U_{p-2}=r=\frac{p-5}{6}
\]

and

\[
\boxed{
-pT_p=
\operatorname{Tr}(F_p|U_p)
-p\operatorname{Tr}(F_p|U_{p-2}).
}
\]

The theorem required for the half-sector remains

\[
\boxed{|T_p|\le C p^{(p-1)/2}}
\]

with an absolute `C`.

## 2. Gate 1 — add two variables

### Result: CLOSED

Because each one-variable Airy contribution lies in odd cohomological degree, geometric alternation in the final two variables gives the ordinary `Sym^2(A)`, not `det(A)`.

Clebsch--Gordan gives

\[
\operatorname{Sym}^{p-2}\mathcal A\otimes\operatorname{Sym}^{2}\mathcal A
\cong
\operatorname{Sym}^{p}\mathcal A
\oplus
\det\mathcal A\otimes\operatorname{Sym}^{p-2}\mathcal A
\oplus
\det(\mathcal A)^2\otimes\operatorname{Sym}^{p-4}\mathcal A.
\]

The residual `mu_3`-invariant `Sym^(p-4)` sector has rank

\[
\frac{p+1}{6}.
\]

Hence the natural variable-addition correspondence has a linearly growing cone.

File: `TWO_VARIABLE_ALTERNATING_CORRESPONDENCE_FAILURE.md`.

## 3. Hodge gate — characteristic-zero correspondences

### Result: CLOSED

Sabbah--Yu's odd Airy Hodge spectrum gives first coordinates

\[
\left\{\frac{p+2i}{3}\right\}
\]

for `k=p`, whereas the Tate-twisted `k=p-2` spectrum gives

\[
\left\{\frac{p+1+2j}{3}\right\}.
\]

Equality would require `2(i-j)=1`. Therefore the spectra are disjoint and

\[
\operatorname{Hom}_{\mathrm{HS}}
\left(
H^1(\operatorname{Sym}^{p}\mathrm{Ai}),
H^1(\operatorname{Sym}^{p-2}\mathrm{Ai})(-1)
\right)=0.
\]

No characteristic-zero algebraic correspondence can explain the desired pairing. Any successful relation must exist only at the exceptional reduction `k=char=p`.

File: `HODGE_OBSTRUCTION_TO_CROSS_K_CORRESPONDENCE.md`.

## 4. Gate 2 — projected Dwork defect

### Result: CLOSED

On Haessig's primitive target basis

\[
c_j=a v^{p-2-2j}w^{2j},
\]

the `mu_3` character is `zeta_3^(1+j)`. The invariant indices are exactly

\[
j\equiv2\pmod3,
\]

and there are `(p-5)/6` of them.

The principal lift defect maps invariant source monomials onto every one of these classes. Its projected rank is therefore

\[
\frac{p-5}{6},
\]

full rank on the actual surviving trace space.

The modular Adams sequence, its `p`-divisible lift defect and the `mu_3` projector do not provide a bounded cone.

File: `MU3_PROJECTED_DWORK_DEFECT.md`.

## 5. Gate 3 — character and period decomposition

### Result: exact terminal reduction; bounded collapse CLOSED

For the local Airy trace `t_u`, let `D_p(X,p)` be the Dickson polynomial. Then

\[
-pT_p=\sum_{u\in\mathbb F_p}D_p(t_u,p).
\]

Cyclotomic Galois symmetry splits the nonzero parameters into square and nonsquare orbits, giving exactly two real-cyclotomic field traces.

The exact script `airy_period_orbit_probe.py` proves at `p=11,17,23,29` that each orbit polynomial has degree `(p-1)/2` and that the Dickson remainder has maximal degree `(p-3)/2`. Thus no bounded-degree Gaussian-period reduction occurs in either orbit.

A cancellation between the two full field traces remains possible, but proving it is a new period theorem.

File: `CHARACTER_ORBIT_AND_EXTENSION_BOUND.md`.

## 6. New unconditional theorem obtained before stopping

Additive orthogonality over `K=F_(p^p)` gives

\[
T_p=\frac1p\sum_{b\in\mathbb F_p}
\sum_{x\in K}\psi_K(x^3+bx).
\]

The `b=0` term vanishes and the degree-three Weil bound applies to every nonzero `b`. Hence

\[
\boxed{
|T_p|
\le
\frac{2(p-1)}{\sqrt p}\,p^{(p-1)/2}.
}
\]

Together with the Chuang reduction,

\[
\boxed{
|T_p|
\le
\min\left\{
\frac{p-5}{3},
\frac{2(p-1)}{\sqrt p}
\right\}
p^{(p-1)/2}.
}
\]

This improves the loss from `O(p)` to `O(sqrt(p))` for large `p`, but not to `O(1)`.

## 7. Exact analytic form of the new theorem required

Write the local Airy eigenvalues as

\[
\alpha_u=\sqrt p\,e^{i\theta_u},
\qquad
\beta_u=\sqrt p\,e^{-i\theta_u}.
\]

Then

\[
D_p(t_u,p)=2p^{p/2}\cos(p\theta_u).
\]

The desired absolute-constant estimate is equivalent to

\[
\boxed{
\left|
\sum_{u\in\mathbb F_p^\times}
\cos(p\theta_u)
\right|
\le C'\sqrt p.
}
\]

This is square-root cancellation for a trace family whose symmetric-power frequency equals the characteristic.

Known results control:

- fixed symmetric power as `p` varies;
- separate weights and conductors;
- local inertia and ordinary Dwork decompositions;
- fixed-order Weil-sum moments.

They do not give a bound uniform in the boundary regime `k=p` after cancellation between the positive and negative Adams constituents.

## 8. Why this is now genuinely new mathematics

All available routine mechanisms have been exhausted:

- local monodromy: exact cancellation but no global trace control;
- variable addition: linearly growing Clebsch--Gordan residual;
- characteristic-zero geometry: Hodge Hom group zero;
- modular Adams lift: full-rank invariant defect;
- Gaussian periods: full orbit degree;
- individual Weil estimates: only `O(sqrt(p))` coefficient;
- standard moment identities: return to the same hyperplane/cubic linear section;
- current Airy-moment literature: no cross-`k` theorem at `k=p`.

The next step must prove one of the following equivalent new statements:

1. a wild characteristic-`p` Frobenius correlation between `U_p` and `U_{p-2}(-1)`;
2. square-root cancellation in the edge-frequency Airy Chebyshev sum;
3. cancellation between the two full real-cyclotomic Dickson field traces;
4. a new arithmetic Picard--Lefschetz/Dwork identity acting only at `k=char=p`.

No further computation can establish the required uniform theorem. Computation is now useful only for testing a proposed new identity.

## 9. Status

- **PROVED:** all reductions and failure certificates above.
- **VERIFIED COMPUTATIONALLY:** full-degree period obstruction at `p=11,17,23,29`.
- **PROVED:** new `O(sqrt(p))` coefficient bound.
- **OPEN / NEW MATH REQUIRED:** absolute-constant coefficient and hence the `p == 2 mod 3` analytic half-theorem.
- **PENDING AFTER THAT:** the endpoint/main/Tate/Artin--Schreier/nearby-cycle application ledger.

This is the genuine terminal point of the autonomous programme under the stated stop rule.
