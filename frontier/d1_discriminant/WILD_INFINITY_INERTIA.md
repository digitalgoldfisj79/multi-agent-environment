# Wild inertia at infinity for the cubic degree-p cover

**Date:** 2026-07-22  
**Status:** exact local inertia group, lower jump, and virtual Artin/Swan conductors proved.

## 1. Local extension

Fix `a!=0` and c, and consider

`phi_c(x)=x^p+a x^3+c x`.

The fibre equation is `phi_c(x)=t`. At infinity put

`y=1/x`, `s=1/t`.

Then the induced local degree-p extension is

`s=y^p/(1+a y^(p-3)+c y^(p-1))`.

It is separable and totally ramified of degree p.

## 2. Exact different exponent

Differentiate in characteristic p:

`ds/dy`
` = y^(2p-4)(3a+c y^2)/(1+a y^(p-3)+c y^(p-1))^2`.

Since `a!=0`, the unit factor has nonzero constant term. Therefore

`v_y(ds/dy)=2p-4`.

### Theorem WII.1

The different exponent of the original degree-p local extension is

`boxed(d(E/K)=2p-4.)`

## 3. Shape of the normal-closure inertia

Let L be the normal closure. A transitive solvable subgroup of `S_p` has Frobenius form, and local wild inertia in a separable degree-p extension is cyclic of order p. Hence

`I=Gal(L/K)=C_p semidirect C_m`

for some `m|p-1`, with faithful action of `C_m` on `C_p`.

There is one positive lower ramification jump j:

`I_0=I`,

`I_1=...=I_j=C_p`,

`I_(j+1)=1`.

Let P be the p-point permutation representation of I. The original degree-p field is the fixed field of the tame complement, so the Artin conductor of P equals its different exponent. Since both I and `C_p` act transitively on the p points,

`a(P)=(p-1)+j(p-1)/m`.

Using Theorem WII.1 gives

`j/m=(p-3)/(p-1)`.

The tame action on the ramification quotient

`I_j/I_(j+1)=C_p`

is the j-th power of the fundamental tame character. Because the semidirect action is faithful, this character has order m. Thus

`gcd(j,m)=1`.

The reduced fraction of `(p-3)/(p-1)` has denominator `(p-1)/2`, so:

### Theorem WII.2

`boxed(m=(p-1)/2,  j=(p-3)/2.)`

Consequently

`boxed(I_infinity = C_p semidirect C_((p-1)/2))`

with one lower jump `(p-3)/2`.

## 4. Restriction of the p-cycle virtual character

Let

`Lambda_p=sum_(i=0)^(p-1)(-1)^i exterior^i(Perm_p-1)`.

Its character is p on p-cycles and zero on every other permutation.

Within I:

- every nonidentity element of the wild subgroup `C_p` is a p-cycle;
- every element outside `C_p` is an affine transformation with a fixed point and is not a p-cycle.

Therefore

`Tr(g|Lambda_p)=p` for `g in C_p-{1}`,

and zero otherwise.

In the rational representation ring of I this is

`boxed(Lambda_p|_I`
` = (p/m) Ind_(C_p)^I(1) - (1/m) Reg_I.)`

On restriction to the wild subgroup alone,

`boxed(Lambda_p|_(C_p)=p*1-Reg_(C_p).)`

## 5. Virtual invariants and conductor

The virtual dimension of `Lambda_p` is zero. Character averaging gives

`dim Lambda_p^I=(p-1)/m=2`,

`dim Lambda_p^(C_p)=p-1`.

Hence its virtual Artin conductor at infinity is

`a_infinity(Lambda_p)`
` = -2 + j*(1/m)(-(p-1))`
` = -2-2j`
` = -(p-1).`

The wild part is

`Swan_infinity(Lambda_p)`
` = j*(1/m)(-(p-1))`
` = -2j`
` = -(p-3).`

### Theorem WII.3

`boxed(a_infinity(Lambda_p)=-(p-1),)`

`boxed(Swan_infinity(Lambda_p)=-(p-3).)`

The negative signs are legitimate because `Lambda_p` is a virtual representation. They record cancellation between its exterior-power constituents.

For the normalized p-cycle indicator `rho_p=Lambda_p/p`, the corresponding virtual conductors are

`-(p-1)/p` and `-(p-3)/p`,

which are bounded in absolute value independently of p.

## 6. Strategic consequence

At finite branch points the inertia contains no p-cycle, so the p-cycle virtual character restricts to zero. All local virtual conductor is therefore concentrated at wild infinity, and after normalization it is bounded.

This is the first rigorous indication that the full-cycle indicator may admit a bounded-complexity cohomological realization despite its exponentially large exterior-power presentation.

It is not yet a global trace bound: a virtual conductor does not automatically bound the absolute dimensions of separate cohomology groups. The next task is to construct a derived or Fourier-transform realization in which the local cancellation occurs before applying Deligne's weight estimate.

## 7. Next target

For the projection in the t-variable, determine the compactly supported derived pushforward of the normalized p-cycle complex and show that it is represented by a bounded-rank complex on the c-line.

An absolute conductor/rank bound for that descended complex would give

`N_a(p)=p+O(sqrt(p))`

and prove the cubic d=1 crown after finite verification.
