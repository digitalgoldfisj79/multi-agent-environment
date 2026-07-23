# Linear–cubic surface as a quartic cover

**Date:** 2026-07-23  
**Status:** exact birational reduction and discriminant factorisation over `Q`; trace bounds remain open.

## 1. Starting surface

Use the trace-zero cubic coordinates from `CUBIC_PAIR_MIXED_SURFACE_REDUCTION.md`. The linear–cubic incidence surface `X_13,a` is cut out by

`D^2+4S^3+27N^2=0`

and

`2Da y^3+6S y^2+(2DSa+3D+9N)y+4S^2-2DNa=0`.

On the open divisor

`2aD-9y != 0`,

the second equation is linear in `N` and gives

`N=(2DSay+2Day^3+3Dy+4S^2+6Sy^2)/(2aD-9y)`.

Substituting into the discriminant equation produces a quartic equation

`Q_a(S,D,y)=0`

of degrees `4`, `4`, `6` in `D`, `S`, `y`, respectively. This is a birational quartic-cover presentation of the generic linear–cubic incidence surface.

## 2. Quartic discriminant

Exact symbolic elimination gives

`disc_D Q_a`

`=27 S^2 a^2`

` *(8aS^2+30aSy^2+18ay^4+27y^2)^2`

` *R_a(S,y)`.

Thus two visible branch components occur with even multiplicity. The primitive branch information is concentrated in `R_a`.

For both representatives `a=1` and `a=2`, exact factorisation over `Q` gives:

- `deg_S R_a=10`;
- `deg_y R_a=18`;
- total degree `19`;
- `R_a` irreducible over `Q`.

The complete polynomial is generated reproducibly by `x13_birational_quartic_reduction.py` and preserved in `x13_birational_quartic_results.json`.

## 3. Consequence

The linear–cubic primitive surface is not explained by splitting the quartic branch locus into a few obvious rational or elliptic components over `Q`. This agrees with the independent large-prime trace fingerprint, which found no stable low-height elliptic decomposition.

The next geometric tasks are now concrete:

1. resolve the excluded divisor `2aD-9y=0` and the affine boundary;
2. compactify the quartic cover;
3. resolve singularities of the primitive branch curve `R_a=0`;
4. calculate the resulting algebraic and transcendental Betti contributions;
5. derive an effective Frobenius trace bound for `M_13`.

This reduction does not itself prove an `O(p)` trace bound, the all-degree sieve, or the d=1 crown.
