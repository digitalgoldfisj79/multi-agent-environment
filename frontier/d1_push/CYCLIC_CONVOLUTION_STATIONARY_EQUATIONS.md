# Interior stationary equations for the cyclic Fourier convolution

**Date:** 2026-07-23  
**Status:** exact stationary-point calculation for every prime `p>=5`. At nonzero total c-frequency there are no generic interior stationary points. The only interior exceptions are the zero-critical-value collision strata already annihilated by the Adams character. Consequently the complete nonzero-frequency primitive Fourier contribution is forced to the weighted boundary.

## 1. Rank-one Fourier kernel

By `ROOT_SHEAF_FULL_FOURIER_LINE_THEOREM.md`, on dual d-frequency `lambda!=0` the Fourier transform of the root sheaf is the rank-one phase

`S(kappa,lambda)`

`=-kappa^p/lambda^(p-1)-a kappa^3/lambda^2.`

Put

`t=kappa/lambda`.

Then

`S=-lambda f_a(t)`,

where

`f_a(t)=t^p+a t^3.`

The p-fold convolution at total dual coordinate `(K,L)` has constraints

`sum_i lambda_i=L`,

`sum_i lambda_i t_i=K`.

The c-pencil is the slice

`L=0`,  `K!=0`.

## 2. Lagrange equations

Introduce multipliers `alpha,beta` and phase

`Phi=-sum_i lambda_i f_a(t_i)`

`    +alpha sum_i lambda_i`

`    +beta(sum_i lambda_i t_i-K).`

At an interior point `lambda_i!=0`, stationarity gives

`partial Phi/partial lambda_i=0`:

`f_a(t_i)-beta t_i=alpha`,

and

`partial Phi/partial t_i=0`:

`f_a'(t_i)=beta.`

Since the derivative of `t^p` is zero,

`f_a'(t)=3a t^2.`

Thus there is an `x` such that

`beta=3a x^2`

and every `t_i` belongs to `{x,-x}`.

## 3. The two critical values

For `t=x`,

`f_a(x)-beta x=x^p-2a x^3.`

For `t=-x`,

`f_a(-x)-beta(-x)=-(x^p-2a x^3).`

Put

`B_a(x)=x^p-2a x^3.`

The common-alpha equation therefore permits both signs only when

`B_a(x)=0.`

### Theorem CCS.1 — generic sign rigidity

If `B_a(x)!=0`, every interior stationary configuration has

`t_0=...=t_(p-1)=x`

or

`t_0=...=t_(p-1)=-x`.

## 4. No nonzero-frequency interior stationary point

For a constant-sign configuration,

`sum_i lambda_i t_i`

`=t sum_i lambda_i`

`=t L.`

On the c-pencil `L=0`, this gives

`K=0`.

### Corollary CCS.2

`boxed(For L=0 and K!=0, the p-fold convolution has no generic interior stationary point.)`

Hence every nonzero c-frequency contribution is supported at:

1. a boundary where some `lambda_i=0`;
2. a boundary where some `t_i=infinity`;
3. the exceptional zero-critical-value locus `B_a(x)=0`.

## 5. The zero-critical-value exceptions

The equation

`B_a(x)=x^p-2a x^3=0`

is

`x^3(x^(p-3)-2a)=0.`

These are precisely the points where the two finite critical values of the root polynomial collide at `d=0`.

Their local multiplicity types are the already classified:

- the persistent triple collision;
- the nonzero quadruple collisions.

The complete finite-collision theorem proves that no local inertia element at these strata is a p-cycle. Therefore the Adams defect is zero there.

The exceptional interior stationary configurations make no primitive contribution.

## 6. The lambda=0 boundary

RFF.2 proves that the original Fourier kernel at

`lambda=0,kappa!=0`

is zero. Its only `lambda=0` contribution is the punctual origin `(kappa,lambda)=(0,0)`, which is the convolution identity/main Tate term.

After the main and lower-length boundary pieces are removed, this boundary contributes no primitive nonzero c-frequency class.

## 7. Remaining boundary

The only surviving source is therefore

`t_i=infinity`,

equivalently the root-at-infinity boundary of the rank-one Legendre kernel. This is exactly the weighted corner analyzed in:

- `INFINITY_FORMAL_RIGIDITY_THEOREM.md`;
- `WEIGHTED_CORNER_ARTIN_SCHREIER_THEOREM.md`;
- `WEIGHTED_CORNER_ENDPOINT_LOCALIZATION_THEOREM.md`;
- `DESCENDED_CRITICAL_FACTORIZATION_THEOREM.md`.

Thus the local Fourier rank-four bridge is now entirely a boundary stationary-phase calculation. There is no missing affine critical point and no unclassified finite stationary family.

## 8. Strategic consequence

The remaining proof can be carried out locally at infinity in the explicit coordinates of the weighted Artin–Schreier deformation. A global characteristic-cycle computation is no longer necessary to discover where the Fourier rank comes from.

The terminal assertion is:

> after removing the explicit Artin–Schreier/Tate orbit, the boundary stationary-phase complex at `t=infinity` is the effective rank-at-most-four A2 Adams difference.

## 9. Epistemic classification

### Exact

- rank-one phase in `(lambda,t)` coordinates;
- Lagrange equations;
- two critical roots and opposite critical values;
- sign rigidity away from `B_a(x)=0`;
- absence of interior stationary points on `L=0,K!=0`;
- identification of exceptional points with known collisions;
- Adams annihilation of all exceptional finite strata;
- reduction to the infinity boundary.

### Open

- explicit local stationary phase at the infinity boundary;
- AS/Tate subtraction in the cyclic convolution category;
- rank-four and conductor theorems.
