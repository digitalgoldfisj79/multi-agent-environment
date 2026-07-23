# Formal rigidity of the wild infinity family

**Date:** 2026-07-23  
**Status:** exact theorem for every prime `p>=5` and every `a!=0`. The complete formal degree-`p` cover at infinity is independent of the finite parameter `c`, after a unique formal change of the root coordinate. This strengthens the previously proved parameter-independent inertia group and removes all variation along the finite part of the infinity divisor. Only the corner `c=infinity` can carry nonconstant infinity-localization data.

## 1. Local equation at infinity

For

`F_(a,c,t)(X)=X^p+aX^3+cX-t`,

put

`y=1/X`,  `s=1/t`.

The cover at `t=infinity` is

`boxed( s=s_c(y):=y^p/(1+a y^(p-3)+c y^(p-1)). )`

The denominator is a unit in the formal power-series ring. The earlier wild-inertia theorem derived from this equation:

- different exponent `2p-4`;
- geometric inertia `C_p semidirect C_((p-1)/2)`;
- one lower jump `(p-3)/2`.

Those invariants were already independent of `c`. The present theorem proves that the entire formal map germ is independent of `c`.

## 2. Formal coordinate equation

Seek a formal change

`y=zU(z)`,  `U(z) in 1+z^2 k[[z]]`,

such that

`s_c(zU(z))=s_0(z)`.

After cross-multiplication this is equivalent to

`U^p(1+a z^(p-3))`

` =1+a z^(p-3)U^(p-3)+c z^(p-1)U^(p-1),`

or

`U^p-1+a z^(p-3)(U^p-U^(p-3))-c z^(p-1)U^(p-1)=0.`  (2.1)

Write

`U=1+z^2V`.

Because the characteristic is `p`,

`U^p=1+z^(2p)V^p`.

The left side of (2.1) is divisible by `z^(p-1)`. Dividing by that power gives the formal equation

`Phi(V,z)=z^(p+1)V^p`

` +a z^(-2)[1+z^(2p)V^p-(1+z^2V)^(p-3)]`

` -c(1+z^2V)^(p-1)=0.`  (2.2)

The expression in square brackets is divisible by `z^2`, so `Phi` lies in

`k[a,a^(-1),c][[z,V]].`

At `z=0`, using `p-3=-3` in characteristic `p`,

`Phi(V,0)=3aV-c`,

and

`partial Phi/partial V (V,0)=3a`,

which is a unit because `p>=5` and `a!=0`.

## 3. Formal rigidity theorem

The formal implicit-function theorem applied to (2.2) gives:

### Theorem IFR.1

There is a unique

`V_(a,c)(z) in k[a,a^(-1),c][[z]]`

with

`V_(a,c)(0)=c/(3a)`

such that, for

`U_(a,c)(z)=1+z^2V_(a,c)(z)`,

one has

`boxed( s_c(zU_(a,c)(z))=s_0(z). )`

Equivalently, the finite flat formal covers

`Spf k[c][[y]] -> Spf k[c][[s]]`

defined by `s=s_c(y)` are formally isomorphic, over every finite value of `c`, to the constant family obtained at `c=0`.

The change has initial expansion

`y=z[1+(c/(3a))z^2+O(z^3)].`

## 4. Consequences for local monodromy and nearby cycles

The theorem is stronger than equality of ramification polygons or inertia groups:

1. the completed cover along the finite `c`-line of the divisor `s=0` is formally constant;
2. every geometric local invariant at wild infinity is independent of finite `c`;
3. the nearby-cycle and local Adams-defect classes along that open infinity divisor are geometrically constant;
4. any nonconstant infinity-localization contribution must be supported at the unique compactification corner where `c` also tends to infinity.

The possible arithmetic unramified quadratic at infinity is not contradicted: it is a constant arithmetic twist determined by the coefficient field and `a`, not a geometric variation in finite `c`.

## 5. Revised localization frontier

Combining:

- complete finite-inertia annihilation from `ADAMS_DEFECT_FINITE_COLLISION_THEOREM.md`;
- formal rigidity IFR.1;
- the explicit infinity representation `W=-V+2Q`;

reduces the cyclic-Adams boundary analysis to one place:

`boxed( (c,e)=(infinity,infinity). )`

No generic finite divisor, finite collision, or finite point of the infinity divisor carries a varying primitive class.

This does not yet prove that the global primitive Adams complex has bounded Betti number. It does make the compactification problem terminal: either the single corner resolves into the already known extremal classes plus bounded weight-three cohomology, or the proposed fixed-complexity collapse fails there.

## 6. Audit

`infinity_formal_rigidity_audit.py` constructs the unique truncated series `V(z)` coefficient by coefficient and verifies equation (2.1) exactly modulo high powers of `z`, for both square classes, all finite `c`, and every prime in the audit range.

## 7. Epistemic classification

- local infinity equation: exact algebra;
- divisibility in (2.2): exact formal algebra;
- invertible linear coefficient `3a`: exact;
- existence and uniqueness of the formal coordinate change: formal implicit-function theorem;
- formal constancy along finite `c`: exact;
- reduction of varying boundary data to the corner: exact for formal local invariants;
- identification and boundedness of the corner contribution: open;
- Cyclic-Adams Weight-Three Lemma: open;
- function-field `d=1` crown: open.
