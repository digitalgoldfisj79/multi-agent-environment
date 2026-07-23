# Critical parabola: exact main/Kummer decomposition

**Date:** 2026-07-23  
**Status:** exact finite étale decomposition for every prime `p>=5` and every `a!=0`. It identifies the complete punctured `A_1` fixed-diagonal family with the already removed main and Kummer sectors. The only primitive fixed-diagonal support is therefore the isolated `A_2` point at `c=0`, subject to the cyclic Thom–Sebastiani bridge.

## 1. Critical map

The cyclic fixed-diagonal theorem gives the critical parabola

`Gamma_a: c=-3a x^2.`

Remove its cusp/branch point and put

`Gamma_a^o=Gamma_a-{x=0}`.

The projection to the coefficient line is

`rho_a:Gamma_a^o -> G_m,c`,

`rho_a(x)=-3a x^2.`

This is a finite étale double cover.

## 2. Trace function

For `c in F_q^*`, the fibre cardinality is

`#rho_a^(-1)(c)`

`=#{x in F_q^*:x^2=-c/(3a)}`

`=1+chi_q(-c/(3a)).`

Therefore the permutation sheaf of the cover has the exact decomposition

### Theorem CPK.1

`boxed(rho_(a,! ) Q_l = Q_l direct_sum L_(chi(-c/(3a))))`

on `G_m,c`.

The first summand is constant/main. The second is the quadratic Kummer sheaf attached to the square class of `-c/(3a)`.

## 3. Relation to the extremal ledger

The fixed-q hook and quadratic-descent analyses already isolate exactly one surviving weight-zero Kummer class. Under the normal-form change of variables, its square-class character is the same quadratic cover as `rho_a`, up to the already tracked constant scalar twist depending on `a` and `p`.

Thus the punctured `A_1` fixed-diagonal family contributes no new primitive sheaf:

`A_1 family = main/Tate + known Kummer.`

Both terms have already been subtracted in `E_a^prim`.

## 4. Branch point and A2 correction

The compactification of `rho_a` has one ramification point above `c=0`, namely `x=0`. At this point the normal root-difference germ changes from `A_1` to `A_2`:

`phi_(a,0)(h)=h^3(a+h^(p-3)).`

The local vanishing-cycle dimension is `2`. Hence, after removal of the main and Kummer summands, every finite fixed-diagonal contribution is punctual at `c=0` and has underlying local dimension at most `2` before applying the Adams defect.

For the virtual difference

`Psi^p(V_A2)-V_A2`,

an effective presentation has total dimension at most `4`. Fourier transform sends a punctual complex at `c=0` to a geometrically constant complex on the dual affine line, preserving this effective dimension.

Consequently the finite fixed-diagonal part of the primitive Fourier transform has effective generic rank at most `4`.

## 5. Remaining issue

To turn the preceding rank statement into a theorem for `FT_c(E_a^prim)`, one must still prove that the cyclic Thom–Sebastiani localization identifies the complete finite contribution with the `A_1/A_2` fixed-diagonal complexes and that the only wild excess is the explicit Artin–Schreier/Tate weighted-corner class.

No further finite family remains to be classified.

## 6. Epistemic classification

### Exact

- quadratic critical map `c=-3a x^2`;
- finite étale degree-two cover on `G_m`;
- trace function `1+chi(-c/(3a))`;
- sheaf decomposition into constant plus Kummer;
- support of the residual finite term at `c=0`;
- local `A_2` dimension `2`;
- effective dimension `<=4` for its Adams difference.

### Open

- global cyclic Thom–Sebastiani identification;
- equality of wild excess with the known Artin–Schreier/Tate corner class;
- rank-four local Fourier theorem;
- conductor-defect lemma and `d=1` crown.
