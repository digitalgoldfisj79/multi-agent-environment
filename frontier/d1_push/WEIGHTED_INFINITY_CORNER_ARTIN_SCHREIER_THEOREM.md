# Weighted infinity corner and its Artin–Schreier boundary orbit

**Date:** 2026-07-23  
**Status:** exact weighted-leading-form and arithmetic p-cycle classification for every prime `p>=5`. The only p-cycle contribution on the weighted infinity exceptional divisor is the known Artin–Schreier orbit. The theorem removes a new primitive p-cycle source at the corner, but a full derived localization comparison is still required to identify the corner complex with this fibrewise trace classification.

## 1. Descended cover and weighted scaling

Fix `a in F_p^*`, put

`m=(p-1)/2`,

and consider

`R_a(c,Y)=Y(Y^m+aY+c)^2=e`.

The weights forced by the three leading terms at `c=e=infinity` are

`wt(Y)=2`, `wt(c)=p-1`, `wt(e)=2p`.

Introduce a weighted boundary parameter `r` and variables `C,Z,E` by

`Y=r^(-2)Z`,

`c=r^(-(p-1))C`,

`e=r^(-2p)E`.

Since `2m=p-1`, substitution gives the exact equation

`boxed(E=Z(Z^m+C+a r^(p-3)Z)^2.)`

Thus the exceptional leading cover at `r=0` is

### Theorem WIC.1 — weighted corner model

`boxed(E=Z(Z^m+C)^2.)`

Geometrically, over the locus `C!=0`, the family is Kummer-isotrivial: after adjoining `lambda` with `lambda^m=C` and setting

`Z=lambda W`, `E=lambda^p E_0`,

it becomes

`E_0=W(W^m+1)^2`.

The different `C in F_p^*` are arithmetic forms of this one geometric boundary cover.

## 2. Square-value lift

On the square-value locus write

`Z=X^2`, `E=D^2`.

Then

### Lemma WIC.2 — boundary root-negation factorization

`boxed(Z(Z^m+C)^2-D^2`

`=(X^p+CX-D)(X^p+CX+D).)`

This is the `a=0` limiting form of the exact root-negation descent.

## 3. Frobenius permutation of the linearized factor

Let

`L_(C,D)(X)=X^p+CX+D`

with `C,D in F_p`.

If `C=0`, the polynomial is inseparable and lies on the boundary discriminant. Assume `C!=0`. Its roots form an affine torsor under the `p`-element kernel of

`X^p+CX`.

Choose a nonzero kernel element `omega`, so

`omega^(p-1)=-C`.

After identifying the root torsor with `F_p` by `alpha+t omega`, arithmetic Frobenius acts as an affine map

`t -> delta-Ct`

for some `delta in F_p`. Its multiplier is `-C`.

If `C!=-1`, this affine map has a fixed point and all other orbit lengths divide the multiplicative order of `-C`, hence divide `p-1`. It is not a p-cycle.

If `C=-1`, then

`L_(-1,D)(X)=X^p-X+D`,

and Frobenius acts on the roots by translation

`x -> x-D`.

For `D!=0` this is one p-cycle; for `D=0` it is the identity.

### Theorem WIC.3 — exact corner p-cycle classification

For `C,D in F_p`, with the fibre separable,

`boxed(L_(C,D) is irreducible of degree p`

` iff C=-1 and D!=0.)`

Equivalently, on the square-value exceptional cover,

`boxed(Z(Z^m+C)^2-E is irreducible`

` iff C=-1 and E is a nonzero square.)`

## 4. Adams-defect trace on the exceptional divisor

Let `W=psi^p(P)-P` be the p-cycle Adams defect. On an unramified exceptional fibre its trace is `p` precisely in the case of WIC.3 and zero otherwise.

After applying the square-value projector `1+chi(E)`, the complete rational-point trace on the exceptional family is

`sum_(C,E!=0)(1+chi(E))Tr(Frob_(C,E)|W)`

`=sum_(E nonzero square) 2p`

`=p(p-1).`

Thus the corresponding irreducible count is

`p(p-1)/p=p-1`.

### Corollary WIC.4 — no new primitive corner orbit

The weighted corner p-cycle contribution is exactly the familiar Artin–Schreier orbit

`X^p-X+D`, `D in F_p^*`,

already isolated in the affine-orbit ledger. It contributes `p-1` irreducible polynomials and no additional primitive family.

## 5. Geometric interpretation

The finite part of the wild infinity divisor is formally constant by `INFINITY_FORMAL_RIGIDITY_THEOREM.md`. WIC.1 describes its only weighted corner degeneration. WIC.3 shows that the p-cycle detector on the square-value exceptional divisor is supported on one arithmetic Kummer form, `C=-1`, and there reduces to the elementary Artin–Schreier translation cover.

Consequently a primitive cyclic-Adams boundary class cannot be justified by new p-cycle fibres on the exceptional divisor. Any remaining corner term must arise from derived nearby-cycle or exceptional-divisor bookkeeping and must be compared against the already known Artin–Schreier/Kummer boundary class.

The next exact localization statement should prove that, after subtracting that class, the primitive corner complex is zero or has uniformly bounded weight-three cohomology.

## 6. Audit

`weighted_infinity_corner_audit.py` verifies:

- the weighted substitution identity for every audited prime;
- the square-value factorization;
- exhaustive factorization of `X^p+CX+D` for all `C,D in F_p`;
- irreducibility exactly at `C=-1,D!=0`;
- the total projected trace `p(p-1)`.

## 7. Epistemic classification

- weighted scaling and exceptional equation: exact algebra;
- geometric Kummer isotriviality over `C!=0`: exact after the stated base change;
- affine Frobenius permutation: exact;
- p-cycle/irreducibility classification over `F_p`: exact;
- identification with the Artin–Schreier orbit: exact;
- equality of the full derived corner localization class with this fibrewise boundary trace: open;
- Cyclic-Adams Weight-Three Lemma: open;
- function-field d=1 crown: open.
