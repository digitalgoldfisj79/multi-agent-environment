# Weighted corner reduction to an Artin–Schreier family

**Date:** 2026-07-23  
**Status:** exact birational/formal reduction for every prime `p>=5` and every `a!=0`. The unique unresolved compactification corner of the depressed root cover has an explicit weighted blow-up whose exceptional family is linearized Artin–Schreier. The cubic perturbation enters through one tame normal monomial `u^(p-3)`.

## 1. Corner coordinates

Use the depressed root cover

`X^p+aX^3+cX=t`.

This is the Kummer lift of the root-negation descended cover on the square-value sector, so it carries the same irreducibility detector after pairing `d` and `-d`.

At the simultaneous corner `c=infinity`, `t=infinity`, put

`r=1/c`,  `s=1/t`,  `y=1/X`.

The equation becomes

`s(1+a y^(p-3)+r^(-1)y^(p-1))=y^p`,

or, after multiplying by `r`,

`r s+a r s y^(p-3)+s y^(p-1)=r y^p.`  (1.1)

The natural weights are

`wt(r)=p-1`,  `wt(s)=p`,  `wt(y)=1`.

They are forced by the scaling of the three terms `rs`, `s y^(p-1)`, and `r y^p`.

## 2. Weighted blow-up

On the standard stacky chart of the weighted blow-up, write

`r=u^(p-1)R`,

`s=u^p S`,

`y=u z`.

Every term in (1.1), except the cubic perturbation, has common factor `u^(2p-1)`. Dividing by that factor gives the strict transform

### Theorem WCAS.1 — exact corner equation

`boxed( R z^p-S z^(p-1)-RS-a u^(p-3)RS z^(p-3)=0. )`  (2.1)

The dependence on the normal coordinate occurs only through

`v=u^(p-3)`.

Since `p-3` is prime to `p`, passage from `u` to `v` is tame.

## 3. Exceptional Artin–Schreier family

On the exceptional divisor `u=0`, equation (2.1) is

`R z^p-S z^(p-1)-RS=0.`  (3.1)

On the open chart `R S z!=0`, put `x=1/z`. Multiplying (3.1) by `x^p` and dividing by `RS` gives

### Theorem WCAS.2 — linearized exceptional cover

`boxed( x^p+R^(-1)x-S^(-1)=0. )`  (3.2)

After the tame Kummer scaling that sends the nonzero coefficient `R^(-1)` to `-1`, this is the universal Artin–Schreier cover

`w^p-w=b.`

Thus the open exceptional divisor carries a `C_p`-cover of fixed Artin–Schreier complexity, not a new degree-growing geometric object.

## 4. The full normal deformation

On the same reciprocal chart, the complete strict transform (2.1) is

`boxed( x^p+a u^(p-3)x^3+R^(-1)x-S^(-1)=0. )`  (4.1)

Hence the original depressed family appears at the corner as a tame one-parameter cubic deformation of a linearized Artin–Schreier family.

The central fibre `u=0` is separable wherever `R!=0`, because its derivative with respect to `x` is `R^(-1)`. Therefore the open exceptional divisor has no geometric vanishing cycles in the finite `x` chart. Nontrivial boundary behaviour can occur only at its two endpoints, where it meets the strict transforms of `c=infinity` and `t=infinity`.

## 5. Adams class on the Artin–Schreier centre

For the universal Artin–Schreier permutation sheaf on

`w^p-w=b`,

the geometric monodromy is `C_p`. The Adams defect character is `0` at the identity and `p` at each nonidentity translation. In the representation ring of `C_p`,

`boxed( W_AS=p*1-Reg_(C_p). )`

Equivalently,

`W_AS=(p-1)*1-sum_(psi!=1)L_psi`,

where `L_psi` are the nontrivial Artin–Schreier character sheaves.

On the affine `b`-line, every nontrivial linear Artin–Schreier sheaf has zero compactly supported cohomology. Consequently

`RGamma_c(A^1_b,W_AS)=(p-1) Q_l(-1)`

in the Grothendieck group. This is an explicit Tate/main-term contribution; it is not a primitive middle motive.

## 6. Consequence for the localization programme

The compactification boundary now has the following exact structure:

1. every finite branch and finite collision is Adams-annihilated;
2. the finite part of `t=infinity` is formally constant in `c`;
3. the weighted bridge across the corner is the explicit Artin–Schreier family (3.2);
4. its open exceptional contribution is elementary Tate/Artin–Schreier;
5. only the two endpoint attachments to the strict transforms of `c=infinity` and `t=infinity` require local gluing bookkeeping.

The corner therefore does not introduce an unidentified high-degree surface. The remaining task is to prove that the two endpoint gluing classes are exhausted by the already identified main, Kummer, pair, and `D` extremal sectors, or to isolate any residual weight-three class explicitly.

## 7. Audit

`weighted_corner_artin_schreier_audit.py` verifies the weighted substitution, strict-transform equation, reciprocal equation, and Artin–Schreier character identity exactly for symbolic prime parameters and by finite-field tests in the audited prime range.

## 8. Epistemic classification

- weighted strict transform: exact algebra;
- exceptional Artin–Schreier model: exact algebra after tame charting;
- tame normal exponent `p-3`: exact;
- absence of finite-x vanishing cycles on the open exceptional divisor: Jacobian criterion;
- Artin–Schreier Adams representation and affine cohomology: exact;
- endpoint gluing into the known extremal ledger: open;
- Cyclic-Adams Weight-Three Lemma: open;
- function-field `d=1` crown: open.
