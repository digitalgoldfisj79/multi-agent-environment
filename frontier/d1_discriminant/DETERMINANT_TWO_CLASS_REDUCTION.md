# Two-mode reduction of the determinant top coefficient

**Date:** 2026-07-21  
**Status:** exact finite-field reduction proved.

## 1. The determinant sum

For nonzero `a in F_p`, put

`T_p(a)=sum_(c,d) J_a(c,d)=3a N_a(p)`.

Here `N_a(p)` counts irreducible members of

`X^p+aX^3+cX+d`.

The function-field cubic-slice crown follows if `T_p(a)` is nonzero for at least one nonzero a.

## 2. Square-class invariance

For `lambda in F_p^*`, substitute `X=lambda Y` and divide by lambda. Since `lambda^p=lambda`, this sends

`X^p+aX^3+cX+d`

to

`Y^p+(a lambda^2)Y^3+cY+d/lambda`.

The map `(c,d) -> (c,d/lambda)` is a bijection. Therefore

`N_(a lambda^2)(p)=N_a(p)`.

Hence `N_a(p)` depends only on `chi(a)`.

Let

`N_+=N_1(p)`

and let `N_-` be the count for any nonsquare a. In F_p define

`A_p=(N_++N_-)/2`,

`B_p=(N_+-N_-)/2`.

Then for every nonzero a,

`N_a(p)=A_p+B_p chi(a)`.

## 3. Canonical two-mode form

Since `chi(a)=a^((p-1)/2)` on `F_p^*`,

`T_p(a)=3A_p a+3B_p a^((p+1)/2)`.

Thus the determinant top coefficient has only two square-class modes as a function of a.

Write

`alpha_p=3A_p`, `beta_p=3B_p`.

Then

`T_p(a)=alpha_p a+beta_p a^((p+1)/2)`.

The two class values are

`T_p(1)=alpha_p+beta_p=3N_+`,

`T_p(nu)/nu=alpha_p-beta_p=3N_-`

for any nonsquare nu, after dividing by nu.

### Theorem DTC.1

The determinant nonvanishing architecture proves the cubic-slice function-field crown whenever

`(alpha_p,beta_p) != (0,0)`.

Equivalently, this architecture succeeds whenever the square and nonsquare slice counts are not both divisible by p.

A zero residue in one class does not kill this architecture; the other class may still prove the theorem.

If both modes vanish, the congruence architecture is inconclusive: the integer counts `N_+` and `N_-` could still be positive multiples of p. Thus simultaneous vanishing does not disprove the cubic-slice crown itself.

## 4. Orthogonality extraction

The two modes can be extracted without choosing representatives:

`S_0=sum_(a != 0) a^(-1) T_p(a)`,

`S_chi=sum_(a != 0) chi(a) a^(-1) T_p(a)`.

Using

`sum_(a != 0) 1=-1`,

`sum_(a != 0) chi(a)=0`

in F_p, one gets

`S_0=-alpha_p`,

`S_chi=-beta_p`.

Therefore the determinant route reduces to proving that the two global orthogonality sums are not both zero.

In terms of counts,

`S_0=-(3/2)(N_++N_-)`,

`S_chi=-(3/2)(N_+-N_-)`.

## 5. Algebraic targets

The two sums suggest distinct coefficient calculations:

1. an unweighted a-average after normalizing J_a by a;
2. a quadratic-character-weighted a-average after the same normalization.

Finite-field orthogonality in a, c, and d converts these to two selected coefficient classes in the raw determinant expansion. The scaling reduction guarantees that no other a-modes can survive canonically.

Neither mode is universally nonzero in the initial data:

- at p=5 the class sum is zero, so alpha_p=0;
- at p=11 the class difference is zero, so beta_p=0.

The correct target is therefore joint nonvanishing, not a claim that either fixed aggregate always survives.

## 6. Relation to the incidence variety

Let C_a count pairs `(theta,c,d)` with theta in `F_(p^p)` satisfying

`theta^p+a theta^3+c theta+d=0`.

A degree-p root forces irreducibility, while every theta in F_p contributes to the linear-root incidence. Hence

`C_a=p N_a+p^2`.

Thus

`N_a mod p != 0`

is equivalent to

`v_p(C_a)=1`.

The determinant top coefficient may therefore also be viewed as the first p-adic point-count coefficient, or Hasse-type invariant, of the fixed-a incidence variety. This supplies a second route to the same two-mode target through p-adic point counting rather than determinant expansion.
