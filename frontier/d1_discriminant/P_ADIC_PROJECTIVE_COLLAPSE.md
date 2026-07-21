# Projective collapse of the p-adic determinant modes

**Date:** 2026-07-21  
**Status:** exact reduction proved; the previously proposed aggregate Gross--Koblitz route is shown to be circular.

## 1. Setup

Let

`E=F_(p^p)`, `Q=p^p`, `Tr=Tr_(E/F_p)`,

and write

`<x,y>=Tr(xy)`.

Let

`W=ker Tr`.

For fixed nonzero `a`, let `N_a(p)` count irreducible members

`X^p+aX^3+cX+d`, `(c,d) in F_p^2`.

The additive-character expansion in `P_ADIC_TWO_MODE_EXPANSION.md` introduced

`U_p=sum_(t in W, t!=0) sum_(<t,theta>=0, <t,theta^3>=0)`
`        e_p(<t^(1/p),theta>)`

and

`V_p=sum_(t in W, t!=0) sum_(<t,theta>=0)`
`        chi(<t,theta^3>) e_p(<t^(1/p),theta>)`.

It then gave

`sum_(a!=0) N_a = p^(2-p) U_p-(p-1)`

and

`sum_(a!=0) chi(a)N_a = (p/Q) G_p V_p`,

where `G_p` is the quadratic Gauss sum.

The purpose of this note is to evaluate the projective `F_p^*`-orbits in these sums exactly.

## 2. The unweighted sum

Let `P(W)` denote the projective space of nonzero vectors in `W` modulo `F_p^*`. For a representative `t` and `mu in F_p^*`,

`(mu t)^(1/p)=mu t^(1/p)`.

Therefore

`sum_(mu!=0) e_p(mu v)=p 1_(v=0)-1`.

Also

`<t^(1/p),theta>=<t,theta^p>`.

Hence

### Theorem PPC.1

`U_p=p A_p-B_p`,

where

`A_p=# {([t],theta): <t,theta>=<t,theta^3>=<t,theta^p>=0}`

and

`B_p=# {([t],theta): <t,theta>=<t,theta^3>=0}`.

Put

`Pi_m=(p^m-1)/(p-1)`.

For fixed `theta`, the relevant projective `t`-space is the orthogonal complement of the indicated span.

If `theta in F_p`, then `span(1,theta,theta^3)` has dimension one. If `theta notin F_p`, then `1,theta,theta^3` are independent, since any dependence would give `theta` degree at most three, whereas `[F_p(theta):F_p]=p>=5`. Thus

`B_p=p Pi_(p-1)+(Q-p)Pi_(p-3)`.

For `theta notin F_p`, the four vectors

`1, theta, theta^3, theta^p`

have rank three exactly when there is a unique triple `(a,c,d) in F_p^3` such that

`theta^p+a theta^3+c theta+d=0`.

The case `a=0` contributes exactly `p-1` irreducible polynomials: if `c!=-1`, the polynomial `X^p+cX+d` has an `F_p` root; if `c=-1`, the polynomials `X^p-X+d` are irreducible exactly for `d!=0`.

Let

`S_0=sum_(a!=0)N_a(p)`.

The number of `theta notin F_p` on the rank-three locus is therefore

`R=p(S_0+p-1)`.

Consequently

`A_p=p Pi_(p-1)+R Pi_(p-3)+(Q-p-R)Pi_(p-4)`.

Substitution into Theorem PPC.1 and then into

`S_0=p^(2-p)U_p-(p-1)`

simplifies identically to

`S_0=S_0`.

Thus the unweighted aggregate character expansion is an exact projective rewriting of the original irreducible count. It does not produce an independent lower-complexity invariant.

## 3. The quadratic-character mode

Scale `t` by `mu in F_p^*`. With

`u=<t,theta^3>`, `v=<t^(1/p),theta>=<t,theta^p>`,

one has

`sum_(mu!=0) chi(mu u)e_p(mu v)=G_p chi(uv)`,

with `chi(0)=0`. Hence

`V_p=G_p C_p`,

where

`C_p=sum_([t] in P(W)) sum_(<t,theta>=0)`
`    chi(<t,theta^3><t,theta^p>)`.

Since `G_p^2=chi(-1)p`, the earlier formula becomes

`sum_(a!=0)chi(a)N_a=chi(-1)p^(2-p)C_p`.

We now evaluate `C_p` by fixing `theta`.

Let

`H_theta={t in W:<t,theta>=0}=span(1,theta)^perp`.

On `H_theta` consider the two linear forms

`L_3(t)=<t,theta^3>`, `L_p(t)=<t,theta^p>`.

For a vector space of dimension `m`,

`sum_([t] in P^(m-1)) chi(L_1(t)L_2(t))`

is zero when the two nonzero forms are independent, and equals

`chi(lambda)p^(m-1)`

when `L_2=lambda L_1` with `lambda!=0`. This follows by lifting to the vector space and summing the quadratic character in two independent coordinates, or in one squared coordinate in the proportional case.

For `theta notin F_p`, the restrictions are proportional exactly when

`theta^p-lambda theta^3 in span(1,theta)`.

The case `lambda=0` gives zero contribution. For `lambda!=0`, this is precisely the root relation for a unique family member with

`lambda=-a`.

Since `dim H_theta=p-2`, each such root contributes

`chi(-a)p^(p-3)`.

Every irreducible degree-`p` polynomial contributes its `p` conjugate roots. Therefore

### Theorem PPC.2

`C_p=chi(-1)p^(p-2) sum_(a!=0)chi(a)N_a(p)`.

Substituting this into the character-mode formula again gives the identity

`sum_(a!=0)chi(a)N_a=sum_(a!=0)chi(a)N_a`.

## 4. Strategic verdict

The two aggregate sums `U_p` and `G_pV_p` do not expose new leading Stickelberger or Gross--Koblitz strata. After the natural `F_p^*` projectivisation:

1. the unweighted mode becomes a rank count whose exceptional rank-three locus is exactly the original coefficient incidence;
2. the character mode becomes a quadratic character sum supported exactly on the same proportional-linear-form locus, with weight `chi(a)`.

Therefore the proposed aggregate p-adic route is circular in its present form. A useful p-adic attack would have to retain finer data before summing over `a`, or construct a genuinely smaller cohomological quotient. Applying Gross--Koblitz directly to the two aggregate expressions cannot by itself prove joint nonvanishing of the determinant modes.
