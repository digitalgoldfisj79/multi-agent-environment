# d=1 crown push — Phase Z5 bridge-audit status

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** all launched compute and exact finite audits are complete. No jobs remain running. The bridge phase produced a genuine fixed-complexity collapse for the extremal `D` sector and two exact finite reductions, but it did not prove the uniform middle-residual bound or the general-prime `d=1` crown.

## 1. Completion statement

The Phase Z4 four-route campaign is complete, and the subsequently launched bridge-audit jobs have also completed. Duplicate confirmation jobs were cancelled only after their earlier completed counterparts and logs were recovered.

The computational programme is therefore finished at its intended natural stopping point. The mathematical programme is not finished: the function-field `d=1` crown and the integer Fortune conjecture remain open.

## 2. Moore / Artin–Schreier one-variable reduction

For `K=F_(p^p)` and nonzero `u`, define

`Xi_a(u)=[v^2-u w-a u v(2u^2+3uv+v^2)]/[3a u v(u+v)]`,

where `v=u^p`, `w=u^(p^2)`.

The proposed exact reduction is

`p N_a(p)=#{u in K^*: Xi_a(u)^p-Xi_a(u)=u}`.

Exact exhaustive audits gave:

- `p=5`, square class `a=1`: root count `20`, hence `N=4`;
- `p=5`, nonsquare class `a=2`: root count `30`, hence `N=6`;
- `p=7`, square class `a=1`: root count `70`, hence `N=10`;
- `p=7`, nonsquare class `a=3`: root count `56`, hence `N=8`.

In all four cases the denominator was nonzero for every nonzero `u`, and the recovered values agree with the independent irreducibility census. This is an exact finite audit of the semilinear one-variable formulation. A publication-grade general proof and a usable trace bound are not yet frozen.

## 3. Extension-field trace census

For fixed characteristic `p`, `q=p^r`, define

`A_r(a)=p N_a(q)-q^2`.

Exact Sage censuses were completed for both base square classes at:

- `p=5`, `1<=r<=5`;
- `p=7`, `1<=r<=4`;
- `p=11`, `1<=r<=3`;
- `p=13`, `1<=r<=3`.

The exact traces are:

### p=5

- square: `[-5,25,-125,625,-3125]`;
- nonsquare: `[5,25,125,625,3125]`.

Thus this small characteristic exhibits the exact pattern `A_r=+-q`.

### p=7

- square: `[21,-189,1029,-2205]`;
- nonsquare: `[7,-189,343,-2205]`.

### p=11

- square: `[33,-473,-7293]`;
- nonsquare: `[33,1815,3399]`.

### p=13

- square: `[-39,-325,22269]`;
- nonsquare: `[-91,-325,-27859]`.

Across these exact cases, the largest observed `|A_r|/q^(3/2)` is `1.941451`. The data are compatible with a fixed-complexity weight-three trace, but do not determine an L-polynomial or prove a uniform bound.

## 4. Exact collapse of the extremal D sector

For every audited prime and every admissible `q`, the high-genus `D_q` trace satisfies the pointwise identity

`a_D(q)=a_C*(q)-2 chi((3 kappa/2)q(q-2))`,

where `a_C*(q)` is the character sum of the fixed sextic

`kappa q (z^2-1)(z^4+(2q-5)z^2+(q-2)^2)`.

The pointwise identity and the complete q-average identity passed exhaustively for every prime `5<=p<=199`.

Together with `QUADRATIC_DESCENT_EXTREMAL_ASSEMBLY.md`, this removes the growing-genus ambiguity from the Kummer, pair and `D` extremal sectors. The nonsplit unweighted `D` average is controlled by one fixed elliptic K3 surface with Neron–Severi rank at least 19 and transcendental rank at most 3, giving an effective `O(p)` extremal contribution.

This is the principal structural result of Phase Z5.

## 5. Root-negation quadratic descent

For `m=(p-1)/2`, write

`F_d(X)=X^p+aX^3+cX+d`,

`H_c(Y)=Y^m+aY+c`,

`G_e(Y)=Y H_c(Y)^2-e`.

The proposed descent is

`F_d irreducible <=> F_(-d) irreducible <=> G_(d^2) irreducible`,

and hence

`N_a=2 #{(c,e): e is a nonzero square and G_e is irreducible}`.

Exact factorisation audits passed for both square classes at every prime `5<=p<=43`, with no mismatches. For example at `p=43`, the square class gives `N_F=42`, `N_G=21`, and the nonsquare class gives `N_F=36`, `N_G=18`.

This is an exact finite audit and a useful lower-dimensional reformulation. It does not by itself supply a uniform positivity or trace estimate.

## 6. Primitive middle residual

After subtracting the complete exact extremal ledger from the selected generic split/nonsplit virtual trace, define `E_middle` as in `middle_configuration_residual_probe.py`.

The exact probe through every prime `5<=p<=199` found

`max |E_middle|/p^(3/2)=4.4928084207...`,

attained at `p=167` in the square class with `E_middle=9696`.

This is consistent with the terminal target

`E_middle=O(p^(3/2))`,

which, after the exact normalization by `p`, would yield

`N_a-p=O(sqrt(p))`.

It is not a proof. The same data reject an `O(p)` interpretation of the unsubtracted middle residual and show that the missing object is genuinely weight-three rather than an elementary curve trace.

## 7. Final scientific result

The bridge proposal has succeeded in one important sense and failed in the terminal sense.

It succeeded because the previously growing-genus extremal geometry has been replaced by explicit fixed-complexity character sums and a rank-at-most-three K3 trace. Routes Q, M and G therefore do share a concrete common geometric mechanism in the extremal sector.

It failed to close the theorem because the primitive middle-configuration residual has not yet been represented by a fixed surface or sheaf with a proved Betti/conductor bound. The desired square-root law for `N_a-p` remains a finite-data conjecture.

The single remaining breakthrough theorem is now:

> Construct the fixed-complexity weight-three object whose Frobenius trace is `E_middle`, and prove an absolute bound `|E_middle|<=C p^(3/2)` with an explicit constant.

Combined with the exact extremal ledger, quantization and the finite census, that theorem would give `N_a=p+O(sqrt p)` and close the depressed-slice `d=1` crown after a finite check.

## 8. Epistemic classification

### Exact algebra already frozen

- sign-paired hook decomposition;
- complete Kummer/pair/D extremal ledger;
- fixed K3 reduction of the nonsplit `D` average;
- fixed sextic pointwise reduction of `D_q`.

### Exact finite computation

- Moore/Artin–Schreier recurrence at `p=5,7`;
- extension-field censuses at `p=5,7,11,13` in the stated ranges;
- fixed-sextic `D_q` identity through `p=199`;
- root-negation descent through `p=43`;
- middle-residual probe through `p=199`;
- all Phase Z4 large-prime counts, cubic moments and bounded-height dynamics sweeps.

### Still open

- a general proof in frozen theorem form for the Moore and root-negation formulations;
- identification and bounded complexity of the middle residual;
- a uniform `N_a=p+O(sqrt p)` theorem;
- the function-field `d=1` crown;
- the integer Fortune conjecture.
