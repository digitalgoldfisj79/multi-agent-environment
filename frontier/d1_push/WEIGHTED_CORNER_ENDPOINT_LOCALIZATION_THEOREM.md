# Endpoint localization on the weighted Artin–Schreier corner

**Date:** 2026-07-23  
**Status:** exact local classification for every prime `p>=5`. The two endpoints of the weighted exceptional divisor are respectively a tame `(p-1,1)` collision and the infinity point of a linear Artin–Schreier cover. Hence neither introduces a new local Adams representation. The remaining open issue is global derived gluing/effective Betti cancellation, not an unidentified local boundary type.

## 1. Exceptional equation

In the weighted blow-up of `WEIGHTED_CORNER_ARTIN_SCHREIER_THEOREM.md`, the exceptional divisor has equation

`F_0(R,S,z)=R z^p-S z^(p-1)-RS=0.`

On `RSz!=0`, the reciprocal coordinate `x=1/z` gives

`x^p+R^(-1)x-S^(-1)=0`,

a tame Kummer form of the universal Artin–Schreier cover.

The closure has two endpoint charts.

## 2. The R=0 endpoint: tame `(p-1,1)` type

Set `S=1`. Then

`R z^p-z^(p-1)-R=0`,

so

`boxed(R=z^(p-1)/(z^p-1).)`

Near `z=0`, the denominator is a unit and

`R=-z^(p-1)(1+O(z^p)).`

Thus `p-1` sheets form one tame cluster with ramification index `p-1`; the remaining sheet is outside this local chart and is fixed by local inertia. Every local inertia element therefore has cycle type contained in `(p-1,1)` and is never a `p`-cycle.

### Theorem WCE.1

For the Adams defect `W=Psi^p(P)-P`,

`boxed(W|_(I_(R=0))=0)`

in the rational representation ring.

The tame normal deformation `u^(p-3)` does not change this conclusion because `p-3` is prime to `p`.

## 3. The S=0 endpoint: Artin–Schreier infinity

Set `R=1`. Then

`z^p-Sz^(p-1)-S=0`,

or

`boxed(S=z^p/(1+z^(p-1)).)`

For `x=1/z` and `b=1/S`, this becomes exactly

`boxed(b=x^p+x.)`

After a tame scalar extension sending the coefficient of `x` to `-1`, this is `w^p-w=b`.

The geometric monodromy is `C_p`. Restricted to this group, the Adams defect is

`W_AS=p*1-Reg_(C_p)`

`    =(p-1)*1-sum_(psi!=1)L_psi.`

The nontrivial linear Artin–Schreier sheaves have zero compactly supported cohomology on the affine `b`-line, while the constant summand contributes

`(p-1)Q_l(-1)`.

### Theorem WCE.2

The `S=0` endpoint carries exactly the elementary Artin–Schreier Adams boundary class. It has no additional primitive local representation beyond the already isolated Artin–Schreier/Tate orbit.

## 4. Complete local boundary inventory

Combining:

1. finite branch/collision annihilation;
2. formal constancy along finite `c` at wild infinity;
3. the Artin–Schreier open exceptional divisor;
4. WCE.1 at `R=0`;
5. WCE.2 at `S=0`;

shows that every geometric local boundary type of the weighted compactification is explicit. There is no unidentified degree-growing local inertia representation left.

This does **not** by itself prove that the global primitive Adams complex has bounded effective virtual Betti degree. Nontrivial global extension or gluing classes can remain even when all local representation types are known. The terminal task is therefore:

> compare the global localization triangle with the exact Kummer, pair, D and Artin–Schreier summands, and bound the effective degree of the residual weight-at-most-three complex uniformly in `p`.

## 5. Audit

`weighted_corner_endpoint_audit.py` verifies the two exact chart equations, their leading ramification orders, and the Adams character on the resulting cycle types for every audited prime.

## 6. Epistemic classification

- endpoint chart equations: exact algebra;
- tame `(p-1,1)` local type: exact local expansion;
- Adams annihilation at the tame endpoint: exact character theory;
- Artin–Schreier endpoint model and Adams class: exact;
- completeness of local boundary types for this weighted compactification: exact at the stated charts;
- global derived gluing and uniform effective Betti bound: open;
- function-field `d=1` crown: open.
