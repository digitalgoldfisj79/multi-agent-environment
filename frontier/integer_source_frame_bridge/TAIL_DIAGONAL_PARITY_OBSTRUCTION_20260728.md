# Tail-diagonal parity obstruction

Date: 28 July 2026  
Status: baseline diagonal bounded; hit diagonal shown to be equivalent to controlling balanced least factors.

## 1. Ordered tail increment

For one centre, let

\[
C_j(r^-)
=
\sum_{m\in\mathcal P_{z_j}(H)}
\log(P_j+m)R_H(P_j+m)R_{<r}(P_j+m)
\]

and let `H_j(r)` be the logarithmic weight of the unique candidate offset hit by
`r`, provided it survives every earlier sieve prime; otherwise put `H_j(r)=0`.

The aggregated Buchstab increment is

\[
\boxed{
I_{j,r}
=
V[r,Y_j]
\left(
\frac{C_j(r^-)}{r-2}
-
\frac{r-1}{r-2}H_j(r)
\right),
\qquad H<r\le Y_j.
}
\tag{1.1}

The ordered martingale correction is `sum_r I_{j,r}`.

## 2. Baseline square is below the Fortune scale

Trivially,

\[
C_j(r^-)
\ll
\frac H{\log H}X.
\tag{2.1}

Also

\[
V[r,Y_j]\ll\frac{\log r}{X}.
\tag{2.2}

The prime reciprocal-square estimate gives

\[
\sum_{r>H\atop r\text{ prime}}
\frac{\log^2r}{r^2}
\ll
\frac{\log H}{H}.
\tag{2.3}

Therefore

\[
\begin{aligned}
\sum_{H<r\le Y_j}
\left|
V[r,Y_j]\frac{C_j(r^-)}{r-2}
\right|^2
&\ll
\frac{H^2X^2}{(\log H)^2}
\frac1{X^2}
\frac{\log H}{H}\\
&\ll
\boxed{\frac H{\log H}}.
\end{aligned}
\tag{2.4}

Across the block this is `O(NH/log H)`, far below `NHX`.

Thus the martingale baseline diagonal is harmless.

## 3. Exact hit parametrisation

If `H_j(r)` is nonzero, then `r` is the least prime factor greater than `H` of one
surviving output.  By the one-hit theorem, every `H`-rough composite candidate output
contributes to exactly one such `r`, and every prime output contributes to none.

Consequently

\[
\boxed{
\sum_{H<r\le Y_j}|H_j(r)|^2
=
\sum_{m\in\mathcal P_{z_j}(H)\atop
P_j+m\text{ composite},\ P^-(P_j+m)>H}
\log^2(P_j+m).
}
\tag{3.1
}

This identity is exact.

Since `V[r,Y_j] asymp log r/X`, the weighted hit diagonal is

\[
\boxed{
\sum_{H<r\le Y_j}
V[r,Y_j]^2|H_j(r)|^2
\asymp
\sum_{m\in\mathcal C_j^{\mathrm{bal}}}
\log^2P^-(P_j+m),
}
\tag{3.2}

up to uniform constant factors, where `mathcal C_j^bal` is the balanced
`H`-rough composite sector.

## 4. Why a positive diagonal estimate is parity-hard

A purely positive bound gives only

\[
\sum_{m\in\mathcal C_j^{\mathrm{bal}}}
\log^2P^-(P_j+m)
\le
\frac H{\log H}X^2,
\tag{4.1}
\]

which is of order `X^4/log X` per centre.  The Fortune variance scale is

\[
HX\asymp X^3.
\]

Thus (4.1) is too large by `X/log X`.

Improving (4.1) to the complete-model scale requires proving that balanced least
factors are distributed with the expected `1/r` frequency, or proving an equivalent
signed cancellation with the normalized rough coordinate.  That is precisely the
sieve parity problem isolated by the programme.

## 5. Required treatment

The hit diagonal must not be estimated alone.  In the exact centred detector it is
coupled to:

1. the baseline term in (1.1);
2. the normalized `H`-rough coordinate;
3. cross-prime martingale increments;
4. the smooth-primitive principal subtraction.

The complete product model combines these terms into the exact variance

\[
V(H,Y)(1-V(H,Y)).
\]

The deterministic theorem must preserve the same signed combination.

## 6. Boundary

Proved:

1. baseline-square bound (2.4);
2. exact balanced-hit identity (3.1)--(3.2);
3. quantitative failure of a positive hit-diagonal majorant.

Consequence:

1. there is no remaining routine tail-diagonal estimate to prove;
2. the load-bearing theorem is the joint centred martingale sampling inequality.

Open:

1. balanced least-factor sampling at complete-model scale;
2. covariance with the rough coordinate;
3. Fortune's conjecture.
