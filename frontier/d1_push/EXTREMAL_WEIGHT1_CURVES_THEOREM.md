# Uniform geometric identification of the first weight-one survivor curves

**Date:** 2026-07-22  
**Status:** exact theorem, conditional only on the already audited normal-form cover and its geometric monodromy. It proves that the pair curve `B_q` and the discriminant-twist curve `D_q` observed at `p=5,7` occur uniformly for every prime `p>=5`. It does not prove that these are the complete weight-one survivor list.

## 1. Normalized cover and local systems

Let `p>=5` be prime, `q in F_p^* \ {2}`, and

`f_q(z)=(q z^p+z^3-3z)/(q-2)`.

Let

`U=P^1_t \ {+1,-1,infinity}`

and let `pi:Y=P^1_z -> P^1_t` be `t=f_q(z)`. Over `U`, `pi` is finite etale of degree `p`. Let `P` be its rank-`p` permutation local system and let `V` be the trace-zero standard local system, so

`P = 1 direct_sum V`.

Put `V_i=exterior^i V`. The weight-one part of `H_c^1(U,V_i)` is

`IH^1(V_i):=H^1(P^1_bar,j_*V_i)`.

The boundary theorem in `WEIGHT0_COLLAPSE_THEOREM.md` gives the complementary weight-zero part.

## 2. General finite-cover realization

If `rho:Z->P^1_t` is the normalization of a finite cover whose restriction over `U` corresponds to a finite permutation local system `M`, then

`H^1(Z_bar,Q_l) = H^1(P^1_bar,j_*M)`.

More generally, if a finite group `Gamma` acts on `Z/P^1`, the `tau`-isotypic part of `H^1(Z)` is the intersection cohomology of the corresponding `tau`-isotypic local system on `U`.

This follows from finite proper pushforward and normalization: `rho_*Q_l` is the middle extension of its etale restriction, and `H^1(P^1,rho_*Q_l)=H^1(Z,Q_l)`.

## 3. The pair curve and `V_2`

Over `U`, let `Y^(2)` be the ordered-distinct-pair cover

`{(z_1,z_2): f_q(z_1)=f_q(z_2), z_1!=z_2}`.

The transposition `sigma:(z_1,z_2)->(z_2,z_1)` acts on this cover. The anti-invariant local system in its permutation pushforward is

`exterior^2 P`.

Because `P=1 direct_sum V`,

`exterior^2 P = V direct_sum exterior^2 V = V_1 direct_sum V_2`.

Let `B_q` be the smooth projective normalization of the affine divided-difference curve

`(f_q(z_1)-f_q(z_2))/(z_1-z_2)=0`.

The anti-invariant cohomology of `B_q` therefore satisfies

`H^1(B_q)^- = IH^1(V_1) direct_sum IH^1(V_2)`.

But `IH^1(V_1)=0`: indeed `P=1 direct_sum V_1`, while the compactification of the root cover is `P^1_z`, so

`H^1(P^1_t,j_*P)=H^1(P^1_z,Q_l)=0`,

and `H^1(P^1_t,Q_l)=0`. Hence:

### Theorem EW1.1

`boxed( IH^1(V_2) = H^1(B_q)^-. )`

Thus the weight-one part of the second hook is exactly the anti-invariant Jacobian factor of the pair curve for every `p`.

## 4. Explicit pair-curve model and rank

In characteristic `p`,

`(z_1^p-z_2^p)/(z_1-z_2)=(z_1-z_2)^(p-1)`.

Consequently `B_q` has affine equation

`q(z_1-z_2)^(p-1)+z_1^2+z_1z_2+z_2^2-3=0`.

Put

`s=z_1+z_2`, `d=z_1-z_2`.

Then

`boxed( 3s^2=12-d^2-4q d^(p-1). )`

For `q!=2`, the polynomial on the right is squarefree. Indeed a repeated nonzero root would imply both

`2q d^(p-3)=1`

and

`d^2=4`,

which force `q=2`; `d=0` is not a root for `p>=5`.

Therefore

`g(B_q)=(p-3)/2`.

The swap involution is `d->-d`. Its quotient has equation

`3s^2=12-r-4q r^((p-1)/2)`, `r=d^2`.

This polynomial is also squarefree for `q!=2`: a repeated nonzero root gives `2q r^((p-3)/2)=1`; combining this with the equation gives `r=4`, and hence `q=2`. Its genus is

`g(B_q/sigma)=floor(((p-1)/2-1)/2)`.

Hence the anti-invariant rank is

`boxed( dim H^1(B_q)^- = 2 floor((p-1)/4). )`

This reproduces rank `2` at `p=5,7`, and predicts ranks `4,6,...` at `p=11,13,...`.

## 5. The discriminant double cover and `V_(p-2)`

Let `S` be the sign local system of the root permutation. Its quadratic cover is

`C_q: y^2=u_q(t^2-1)`,

where `Disc_z P_(q,t)=u_q(t^2-1)` in square classes. This curve has genus zero, so

`IH^1(S)=H^1(C_q)^-=0`.

For the standard representation,

`V_(p-2)=exterior^(p-2)V = V^* tensor det(V) = V_1 tensor S`,

because `V` is self-dual and `det(V)=sgn`.

Now form the normalized fibre product

`Z_q=Y times_(P^1_t) C_q`.

Over `U`, the anti-invariant part of its permutation local system under the quadratic deck involution is

`P tensor S = S direct_sum (V_1 tensor S)`.

The quotient of `Z_q` by that involution is the root curve `Y=P^1_z`, so the invariant part of `H^1(Z_q)` is zero. Therefore

`H^1(Z_q)=H^1(Z_q)^-=IH^1(S) direct_sum IH^1(V_1 tensor S)=IH^1(V_(p-2))`.

The pullback equation is

`y^2=u_q(f_q(z)^2-1)`.

Write

`qz^p+z^3-3z-(q-2)=q(z-1)^2g_(q,+)(z)`,

`qz^p+z^3-3z+(q-2)=q(z+1)^2g_(q,-)(z)`.

After removing the square factor `q^2(z^2-1)^2/(q-2)^2`, the normalization is the hyperelliptic curve

`D_q: w^2=u_q g_(q,+)(z)g_(q,-)(z)`.

The residual factors have degree `p-2`; they are separately squarefree and have no common root because the only critical points are `+/-1` with distinct critical values. Thus their product is squarefree of degree `2p-4`.

### Theorem EW1.2

`boxed( IH^1(V_(p-2)) = H^1(D_q). )`

Moreover,

`boxed( g(D_q)=p-3,  dim H^1(D_q)=2p-6. )`

This proves uniformly the genus-2 curve at `p=5` and genus-4 curve at `p=7` found in the spectra package.

## 6. Combined consequence

For every `p>=5` and every generic `q`, two pieces of the post-pushforward weight-one survivor list are now exact:

- even side: `H^1(B_q)^-`, rank `2 floor((p-1)/4)`;
- odd side: `H^1(D_q)`, rank `2p-6`.

Together with the proved single weight-zero Kummer class, these account for an explicit `O(p)` subsystem of the surviving object.

They do not establish completeness. For `p>=7`, middle configuration hooks can contribute further weight-one factors, as the `p=7` spectra already indicate.

## 7. Epistemic classification

- Finite-cover/isotypic cohomology realization: exact standard finite-pushforward formalism, with hypotheses checked.
- `V_2` pair-curve identification: exact theorem.
- Pair-curve equations, smoothness and genus: exact algebraic calculation.
- `V_(p-2)` discriminant-twist identification: exact theorem.
- `D_q` equation, squarefreeness and genus: exact algebraic calculation.
- Completeness of the full weight-one survivor list: open.
- Function-field crown: open.
