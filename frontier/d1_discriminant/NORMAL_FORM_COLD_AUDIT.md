# Cold audit of the critical-value normal form

**Date:** 2026-07-22  
**Status:** independent algebraic audit complete. The normal-form reduction, fixed-a reconstruction, q-boundary inertia and virtual q-infinity conductor are verified. The previously stated global sign quotient requires correction by a q-Kummer factor.

## 1. Scope and epistemic status

This audit independently rederives the five inputs requested for the final-mile function-field crown programme:

1. reduction from `(a,c)` to `(q,epsilon)`;
2. reconstruction of `N_a` from the four universal q-sums;
3. inertia at `q=0,2,infinity`;
4. the virtual Artin conductor at `q=infinity`;
5. the discriminant square class of the normalized two-variable cover.

Items 1--4 are confirmed as exact theorems. Item 5 is corrected below.

Throughout, `p>=5` is prime and

`P_(q,t)(X)=qX^p+X^3-3X-(q-2)t`.

## 2. Reduction to the two universal q-families

Start from

`F_(a,c,d)(X)=X^p+aX^3+cX+d`, with `a c !=0`.

Choose `r` in the quadratic closure with

`r^2=-c/(3a)`

and put

`epsilon=r^(p-1)=chi(-c/(3a)) in {+1,-1}`.

Since `r^p=epsilon r`, substitution `X=rz` gives

`F_(a,c,d)(rz)=a r^3 [qz^p+z^3-3z+d/(ar^3)]`,

where

`q=r^(p-3)/a=epsilon/(ar^2)=-3epsilon/c`.

The sign choice `r -> -r` does not change q. This verifies the basic normal form.

### Split type

If `epsilon=+1`, write `r^2=lambda^2` with `lambda in F_p^*`. Scaling by `lambda` sends the coefficient pair to

`a'=1/q`, `c'=-3/q`.

Hence the fixed-c irreducible count is

`n_+(q)=#{d: X^p+q^(-1)X^3-3q^(-1)X+d is irreducible}`.

### Nonsplit type

Fix a nonsquare `eta`. If `epsilon=-1`, write

`r^2=eta lambda^2`, `lambda in F_p^*`.

Scaling by `lambda` sends the coefficient pair to

`a'=-1/(eta q)`, `c'=3/q`.

Hence the fixed-c irreducible count is

`n_-(q)=#{d: X^p-(eta q)^(-1)X^3+3q^(-1)X+d is irreducible}`.

Replacing eta by another nonsquare changes lambda by an `F_p`-scaling and does not change the count.

## 3. Reconstruction of a fixed-a slice

Let

`A=chi(a)`, `delta=chi(-1)`.

For the split family, `c=-3/q`; the condition

`chi(-c/(3a))=+1`

is equivalent to

`chi(q)=A`.

For the nonsplit family, `c=3/q`; the condition

`chi(-c/(3a))=-1`

is equivalent to

`chi(q)=-delta A`.

Therefore

`N_a=N_(a,0)`

` + sum_(q!=0, chi(q)=A)n_+(q)`

` + sum_(q!=0, chi(q)=-delta A)n_-(q)`.

Writing

`S_+^0=sum_(q!=0)n_+(q)`,

`S_+^chi=sum_(q!=0)chi(q)n_+(q)`,

`S_-^0=sum_(q!=0)n_-(q)`,

`S_-^chi=sum_(q!=0)chi(q)n_-(q)`,

gives the exact identity

`boxed(N_a=N_(a,0)`

` +(1/2)(S_+^0+A S_+^chi)`

` +(1/2)(S_-^0-delta A S_-^chi).)`

All signs in `CRITICAL_VALUE_NORMAL_FORM.md` are confirmed.

## 4. q-boundary inertia

The following checks are over an algebraically closed coefficient field and at generic t.

### q=0

The three bounded roots reduce to the simple roots of

`X^3-3X+2t`.

The other roots satisfy to leading order

`qX^p+X^3=0`, hence `X^(p-3)=-q^(-1)`.

The Newton slope is `-1/(p-3)` and tame inertia acts as one `(p-3)`-cycle, leaving the three bounded roots fixed. Thus the generator has type

`(p-3)(1)(1)(1)`.

### q=2

At `q=2`,

`G(X)=2X^p+X^3-3X`

has exactly two double roots, `X=+1` and `X=-1`, and all other roots are simple. Writing `q=2+e`, the two local expansions are quadratic in a common parameter `sqrt(e)`. Geometric inertia therefore acts simultaneously on the two pairs, with type

`(2)(2)(1)^(p-4)`.

### q=infinity

Put `r=q^(-1)`, make the radicial base change `t=tau^p`, and set `X=tau+Z`. The equation becomes

`Z^p+r[Z^3+3tau Z^2+(3tau^2-3)Z+H(tau)]=0`,

`H(tau)=tau^3-3tau+2tau^p`.

At generic tau this is Eisenstein in r. With `v_L(r)=p`, its derivative has valuation p, so the different exponent of the degree-p local extension is exactly p.

In the normal closure the inertia group has form

`C_p semidirect C_m`, `m|(p-1)`.

If j is its single positive lower jump, the different formula for the degree-p subextension is

`p=(p-1)+j(p-1)/m`.

Hence `m=p-1` and `j=1`. Therefore

`boxed(I_infinity=C_p semidirect C_(p-1), j=1.)`

The inertia conclusions of `Q_LINE_BOUNDARY_INERTIA.md` are confirmed.

## 5. Virtual conductor at q=infinity

Let `Lambda_p` be p times the indicator of a p-cycle. Its virtual rank is zero.

In `I=C_p semidirect C_(p-1)`, the p-cycles are precisely the `p-1` nonidentity translations. Therefore

`dim Lambda_p^I=(p(p-1))/(p(p-1))=1`,

while

`dim Lambda_p^(C_p)=p(p-1)/p=p-1`.

With the single lower jump j=1,

`Swan_infinity(Lambda_p)`

`=(1/(p-1))(0-(p-1))=-1`.

The Artin conductor is

`a_infinity=rank-dim invariants+Swan=0-1-1=-2`.

Thus

`boxed(Swan_infinity(Lambda_p)=-1, a_infinity(Lambda_p)=-2.)`

This confirms the constant virtual boundary conductor. It remains only a virtual conductor statement and does not imply numerator-plus-denominator effectivity.

## 6. Correct discriminant and sign quotient

Because `p=0` in characteristic p,

`P'_(q,t)(X)=3(X^2-1)`.

The resultant is therefore evaluated at the two critical points:

`Res_X(P,P')=3^p P(1)P(-1)`.

Now

`P(1)=(q-2)(1-t)`,

`P(-1)=-(q-2)(1+t)`.

Hence

`Res_X(P,P')=3^p(q-2)^2(t^2-1)`.

For a degree-p polynomial of leading coefficient q,

`Disc_X(P)=(-1)^(p(p-1)/2)q^(-1)Res_X(P,P')`.

Therefore the exact formula is

`boxed(Disc_X(P_(q,t))`

`=(-1)^(p(p-1)/2) 3^p q^(-1)(q-2)^2(t^2-1).)`

Modulo squares in `F_p(q,t)^*`, this is

`boxed(kappa_p q (t^2-1),)`

where `kappa_p=(-1)^((p-1)/2)3`; `q^(-1)` and q have the same square class.

### Consequence

For each fixed geometric q-fibre, the constant factor is a square after extending the constant field, so the sign cover of the t-line is geometrically isomorphic to

`y^2=t^2-1`.

But over the full two-variable `(q,t)` base, the sign quotient is not the pullback of that fixed t-cover. It contains the nontrivial q-Kummer factor:

`y^2=kappa_p q(t^2-1)`.

Equivalently, the claimed global q-independent sign quotient becomes correct only after the Kummer pullback `q=s^2` (and, arithmetically, a constant quadratic extension if kappa_p is nonsquare).

Thus the proposed global two-point reduction after only adjoining `sqrt(t^2-1)` is not valid as stated. The corrected sign cover is also ramified at `q=0` and `q=infinity`.

This correction does not alter the root-cover inertia calculations in Sections 4--5. It does alter any argument that attempts to remove all finite transposition monodromy uniformly over q without simultaneously accounting for the q-Kummer cover.

## 7. Revised final-mile wall

The precise wall remains an effectivity theorem for the rank-zero direct image, but the sign-cover subroute must use the corrected base change

`y^2=kappa_p q(t^2-1)`

or first pass to `q=s^2`.

No crown claim can rely on the q-independent sign quotient in the unpulled-back q-family.
