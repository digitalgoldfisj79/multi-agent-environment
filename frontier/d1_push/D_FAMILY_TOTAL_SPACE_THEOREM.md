# The D-family total q-trace: exact singular-K3 formula

**Date:** 2026-07-22  
**Status:** exact theorem for every prime `p>=5`. It evaluates the complete generic-q Frobenius trace of the genus-`p-3` curves `D_q` from `EXTREMAL_WEIGHT1_CURVES_THEOREM.md`.

## 1. Statement

Let `chi=chi_p` be the quadratic character of `F_p`, extended by `chi(0)=0`, and put

`eps_p = chi( (-1)^((p-1)/2) * 3 ).`

For `q in F_p^* \ {2}`, let

`D_q: w^2 = u_q g_(q,+)(z) g_(q,-)(z)`

be the smooth projective curve of genus `p-3` from EW1.2. In square classes,

`chi(u_q)=eps_p chi(q)`.

Let `a_p(f_24)` denote the p-th coefficient of the rational weight-three CM newform `24.3.h.a`. Equivalently, for `p>3`,

- `a_p(f_24)=0` if `chi(-6)=-1`;
- if `p=x^2+6y^2`, then `a_p(f_24)=2(x^2-6y^2)`;
- if `p=2x^2+3y^2`, then `a_p(f_24)=-2(2x^2-3y^2)`.

Then

### Theorem DTA.1

`sum_(q in F_p^*\{2}) Tr(Frob_p | H^1(D_q))`

` = eps_p * ( -chi(-6)p - a_p(f_24) - chi(-1) - 2chi(2) + 2chi(6) ).`

In particular,

`|sum_q Tr(Frob_p|H^1(D_q))| <= 3p+5`,

and the only non-elementary term is one fixed rank-two CM motive, independent of `p` and `q`.

## 2. Prime-field compression

Over `F_p`, the residual critical factors satisfy

`g_(q,+)(z)=q(z-1)^(p-2)+z+2`,

`g_(q,-)(z)=q(z+1)^(p-2)+z-2`.

For `z != +/-1`,

`g_(q,+)g_(q,-)`

` = ((q+z^2+z-2)(q+z^2-z-2))/(z^2-1).`

At `z=+/-1`, both products equal `3(q-2)/2`.

Since the product has even degree `2p-4` and leading coefficient of square class `u_q`,

`a_p(D_q) = -chi(u_q) - sum_z chi(u_q g_(q,+)(z)g_(q,-)(z)).`

Define the fixed two-variable character sum

`S_p = sum_(z,q in F_p) chi( (z^2-1) q`

`       * (q+z^2+z-2)(q+z^2-z-2) ).`

The omitted `q=2`, `z=+/-1`, and infinity contributions are elementary:

`sum_(q!=0,2) a_p(D_q)/eps_p`

` = (p-2)chi(2)+2chi(6)-S_p.`

## 3. Bielliptic decomposition

Put `r=z^2`. The even sextic

`C_q: y^2=q(z^2-1)((q+z^2-2)^2-z^2)`

has two elliptic quotients

`E_(1,q): y^2=q(r-1)((q+r-2)^2-r)`,

`E_(2,q): y^2=q r(r-1)((q+r-2)^2-r)`.

For every q, the character identity underlying the standard bielliptic splitting gives

`a(C_q)=a(E_(1,q))+a(E_(2,q))`

whenever the curves are smooth, and the corresponding raw character identity remains valid at the singular parameters. Consequently

`S_p = -A_1(p)-A_2(p)`,

where `A_i(p)=sum_(q in F_p) a(E_(i,q))`, with the displayed character-sum definition at singular q.

## 4. The rational elliptic contribution

Writing `x=r-1` and then `x=qu` gives

`A_1(p)=-sum_(q,x) chi(qx(x^2+(2q-3)x+q(q-2)))`

`=-sum_(u,q!=0) chi(q u (q(u+1)^2-(3u+2))).`

For generic `u`, the inner quadratic character sum equals `-1`. The two exceptional values are

- `u=-1`, where the inner sum is `0`;
- `u=-2/3`, where it is `p-1`.

Thus

### Lemma DTA.2

`A_1(p) = -chi(-6)p - chi(-1).`

## 5. The singular elliptic K3 contribution

The second quotient is the quartic family

`E_(2,q): y^2=q r(r-1)(r^2+(2q-5)r+(q-2)^2).`

Its binary-quartic invariants are

`I=q^2(q-3)(q^3-3q^2+3q-3)`,

`J=-q^3(2q^2-6q+3)(q^4-6q^3+12q^2-18)`,

and

`4I^3-J^2=-27 q^8(q-2)^6(4q-9).`

The Jacobian model `Y^2=X^3-27IX-27J` is an elliptic K3 surface with fibres

- `I_2^*` at `q=0`;
- `I_6` at `q=2`;
- `I_1` at `q=9/4`;
- `I_3^*` at `q=infinity`.

The reducible-fibre root lattice is `D_6+A_5+D_7`, of rank 18. Together with fibre and zero section it has rank 20. The quartic supplies a rational 2-torsion section; the fibre component groups exclude any larger torsion. Therefore

`rho=20`, `MW=Z/2`, and `disc(NS)=-24`.

The surface is a singular K3. Its transcendental Galois representation is the rank-two CM representation attached to the weight-three form `24.3.h.a`; the fibre model fixes the untwisted form. The trace is `a_p(f_24)`.

For the point-count ledger, write the unspecified splitting signs of the two starred fibres as `delta_0,delta_infinity in {+/-1}`. Their values cancel from the final formula. The Neron-Severi trace is

`Tr(Frob|NS(1))=16+delta_0+delta_infinity+2chi(2)`.

The corrections from the singular quartic models to the resolved K3 fibres are

- at `q=0`: `p(5+delta_0)`;
- at `q=2`: `p(3+chi(2))`;
- at infinity: `1+p(7+delta_infinity)`.

Applying Lefschetz to the resolved K3 and cancelling the two starred-fibre signs gives

### Lemma DTA.3

`A_2(p) = -chi(2)p - a_p(f_24).`

## 6. Assembly

Combining DTA.2 and DTA.3,

`S_p = chi(-6)p+chi(-1)+chi(2)p+a_p(f_24).`

Substitution into the prime-field compression identity yields DTA.1.

## 7. Epistemic classification

- Prime-field critical-factor identities and boundary corrections: exact elementary algebra.
- Bielliptic character decomposition: exact.
- `A_1` evaluation: exact quadratic-character summation.
- K3 fibre configuration, Mordell-Weil torsion and NS discriminant: exact Tate/Shioda-Tate calculation.
- Modularity: standard modularity theorem for singular K3 surfaces; the discriminant and model identify the CM form `24.3.h.a`.
- Machine audit: exact direct character sums and CM coefficient formula over all primes in the committed range.
- General function-field crown: still open.
