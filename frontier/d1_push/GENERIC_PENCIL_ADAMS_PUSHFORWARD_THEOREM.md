# Generic-pencil Adams pushforward and the one-point conductor frontier

**Date:** 2026-07-23  
**Status:** exact in the Grothendieck group for every prime `p>=5` and every `a in F_p^*`, using the already proved Adams character, finite-collision annihilation and wild-inertia theorem. It replaces the remaining surface complex by one virtual sheaf on the coefficient line. Uniform effective cohomology remains open.

## 1. Projection to the linear coefficient

Put

`f_(a,c)(x)=x^p+a x^3+c x`

and let `U_a` be the etale locus of the root cover

`f_(a,c)(x)+d=0`

over `A^2_(c,d)`. Let

`pi:U_a -> A^1_c`

be the projection and let

`W_a=Psi^p(P_a)-P_a`

be the Adams p-cycle detector. For every finite extension `F_q/F_p` and every `c in F_q`, define

`n_a(c;q)=#{d in F_q: x^p+a x^3+c x+d is irreducible over F_q}`.

The fibrewise trace formula is

`sum_d Tr(Frob_(c,d)|W_a)=p n_a(c;q)`.

## 2. Fibre cohomology

For generic `c`, the `d`-line root cover has two finite simple branch values and one wild point at infinity. Its geometric monodromy is `S_p`.

The Adams class has exactly one `S_p`-invariant constituent. Hence

`H_c^2(U_(a,c),W_a)=Q_l(-1)`

in the Grothendieck group.

Let

`E_a=R^1 pi_! W_a`

on the generic finite `c`-line. Then fibrewise

`p n_a(c;q)=q-Tr(Frob_c|E_a)`.

Equivalently,

`Tr(Frob_c|E_a)=q-p n_a(c;q)`.

For `q=p`, this is the exact pointwise error `p-p n_a(c)` used in the additive Fourier probe.

## 3. Exact virtual rank

At wild `d=infinity`, the inertia group is

`I=C_p semidirect C_m`,  `m=(p-1)/2`,

with lower jump

`j=(p-3)/2`.

The proved restriction is

`W|I=-V+2Q`,

where `V` is the standard representation and `Q` is the inflated regular representation of the tame quotient.

On the lower ramification filtration,

- `I_0=I`;
- `I_i=C_p` for `1<=i<=j`;
- `I_i=1` for `i>j`.

The restriction of `V` to `C_p` is `Reg_(C_p)-1`, so `V^(C_p)=0`. Therefore

`Swan(V)=j*(|C_p|/|I|)*(p-1)`

`        =((p-3)/2)*(2/(p-1))*(p-1)`

`        =p-3.`

The representation `Q` is tame, hence

`Swan(W)=-(p-3).`

The Grothendieck-Ogg-Shafarevich formula on the generic punctured `d`-line gives

`chi_c(U_(a,c),W)=p-3`,

because `rank(W)=0` and every finite Swan term vanishes. Since the degree-two class has virtual dimension one,

`chi_c=-rank(E_a)+1`,

and hence

### Theorem GPA.1 — generic-pencil rank

`boxed(rank(E_a)=4-p.)`

This reproduces the virtual survivor rank `4-p` found independently in the fixed-q hook spectra.

## 4. No finite singular support

The finite branch divisors have transposition inertia. At every finite collision the local multiplicity partitions are

- `3,2^((p-3)/2)`;
- `1,4,2^((p-5)/2)`.

No local inertia element is a p-cycle. By the complete finite Adams-annihilation theorem, the finite vanishing-cycle class of `E_a` is zero in the Grothendieck group. Thus the middle extension of `E_a` has no finite characteristic-cycle component on the `c`-line.

All nonconstant local data of `E_a` are concentrated at `c=infinity`.

## 5. Exact global error formula

Summing the fibre identity over `c in F_q` gives

`p N_a(q)=q^2-Tr(Frob_q|RGamma_c(A^1_c,E_a)).`

Therefore

### Theorem GPA.2 — one-dimensional error complex

`boxed(p N_a(p^r)-p^(2r)`

`      =-Tr(Frob_p^r|RGamma_c(A^1_c,E_a)).)`

This is the Leray form of the previously proved two-degree Adams complex. The surface problem is now a one-point conductor problem on the affine `c`-line.

## 6. Primitive subtraction

Let `E_a^prim` be the virtual middle extension obtained after removing the already explicit pieces:

- the fibrewise Tate/main class;
- Kummer;
- pair;
- split and nonsplit D/CM;
- the Artin-Schreier corner class;
- the two endpoint classes.

The pointwise primitive trace is exactly the function computed by `qline_pointwise_middle_probe.py` after passage to the split/nonsplit normal-form cells and the two-class projector.

The remaining theorem can be stated on a curve:

### Generic-pencil conductor-defect lemma

There are absolute constants `C_inv,C_def` such that, for at least one square class,

`dim_eff (E_a^prim)^(pi_1(A^1_bar)) <= C_inv`

and

`Swan_infinity(E_a^prim)-rank(E_a^prim) <= C_def`

in an honest effective presentation of the virtual class.

By Grothendieck-Ogg-Shafarevich and Poincare duality, these two bounds give absolute bounds for the effective degrees of `H_c^1(A^1,E_a^prim)` and `H_c^2(A^1,E_a^prim)`, hence the Primitive effective-degree lemma of Phase Z6.

## 7. Strategic consequence

The growing virtual rank `4-p` is not itself an obstruction. Airy and Artin-Schreier sheaves can have rank and Swan conductor growing together while their compactly supported cohomology remains bounded or zero. The decisive quantity is the conductor defect

`Swan_infinity-rank`,

not the generic rank.

The weighted corner exponent `p-3` and the Artin-Schreier exceptional family make a bounded conductor defect plausible. The next exact task is to calculate the local Fourier transform of `E_a^prim` at infinity, rather than to estimate the original surface Betti numbers directly.

## 8. Epistemic classification

- fibrewise Adams trace formula: exact;
- unique fibrewise degree-two Tate class: exact;
- wild restriction and lower jump: previously proved exact;
- Swan calculation and virtual rank `4-p`: exact;
- finite vanishing-cycle class: exact in the Grothendieck group from finite Adams annihilation;
- one-dimensional global error formula: exact Leray/Grothendieck-Lefschetz identity;
- effective conductor-defect bound: open;
- function-field `d=1` crown: open.
