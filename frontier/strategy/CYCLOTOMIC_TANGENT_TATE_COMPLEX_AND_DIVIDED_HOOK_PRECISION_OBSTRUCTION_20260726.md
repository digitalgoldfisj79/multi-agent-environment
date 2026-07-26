# Cyclotomic tangent Tate complex and the divided-hook precision obstruction

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** first-cyclotomic-moment route for the function-field Fortune `d=1` crown.  
**Status:** the coefficient module, Tate complex, Bockstein, Frobenius ambiguity and precision obstruction below are **PROVED**. Construction and nonvanishing of the required geometric divided secondary trace remain **OPEN**. The crown is not proved.

## 1. Arithmetic target

For

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad a\ne0,
\]

let

\[
N_a=
\#\{(c,d):F_{a,c,d}\text{ irreducible}\}
\]

and

\[
M_a=
\sum_{F_{a,c,d}\text{ irreducible}}c
\quad\text{in }\mathbf F_p.
\]

Let `zeta` be a primitive `p`-th root of unity and put

\[
\pi=\zeta-1.
\]

The coefficient Fourier value is

\[
\mathcal F_a
=
\sum_{c,d}1_{F_{a,c,d}\mathrm{\ irr}}\zeta^c.
\]

Since

\[
\zeta^c=(1+\pi)^c
\equiv1+c\pi\pmod{\pi^2},
\]

one has

\[
\boxed{
\mathcal F_a=N_a+\pi M_a+O(\pi^2).
}
\]

Thus `M_a` is the first cyclotomic tangent of the irreducibility Fourier transform. Nonvanishing of `M_a` in either cubic square class proves the required existence statement.

The purpose of this note is to construct the coefficient-level tangent object and determine whether ordinary modular Smith/Tate data can recover its Frobenius trace.

## 2. Coefficient ring and tangent character

Let

\[
\mathcal O=\mathbf Z_p[\zeta],
\qquad
R=\mathcal O/(\pi^2),
\qquad
k=\mathcal O/(\pi)\cong\mathbf F_p.
\]

Because

\[
v_\pi(p)=p-1,
\]

we have

\[
p=0\quad\text{in }R
\]

for every admitted prime `p>=5`.

Let

\[
C_p=\langle\tau\rangle.
\]

The coefficient Fourier character modulo `pi^2` is the rank-one `R[C_p]`-module

\[
R_{\rm tan}=R,
\qquad
\tau\cdot x=(1+\pi)x.
\]

Since

\[
(1+\pi)^p=1
\quad\text{in }R,
\]

this is a valid `C_p`-module.

The `pi`-adic filtration gives

\[
0\longrightarrow \pi R
\longrightarrow R_{\rm tan}
\longrightarrow R/\pi R
\longrightarrow0.
\]

Both end terms are the trivial one-dimensional `k[C_p]`-module. In the `k`-basis represented by `1,pi`, the generator acts by the Jordan matrix

\[
\boxed{
\tau=
\begin{pmatrix}
1&0\\
1&1
\end{pmatrix}
}
\]

up to the harmless convention interchanging the two basis vectors.

### Theorem 2.1 — coefficient tangent extension

The sequence

\[
\boxed{
0\to k\to R_{\rm tan}\to k\to0
}
\]

is the nonzero class in

\[
\operatorname{Ext}^1_{k[C_p]}(k,k)
\cong H^1(C_p,k)
\cong k.
\]

In particular it is nonsplit.

This is the precise coefficient object suggested by the first-order expansion `zeta^c=1+c pi`.

## 3. Exact Tate complex

The periodic Tate complex for a cyclic module alternates the maps

\[
\tau-1
\quad\text{and}\quad
\mathcal N=1+\tau+\cdots+\tau^{p-1}.
\]

On `R_tan`,

\[
\tau-1=\pi.
\]

Moreover

\[
\mathcal N
=
\sum_{j=0}^{p-1}(1+\pi)^j.
\]

Modulo `pi^2`,

\[
(1+\pi)^j=1+j\pi,
\]

so

\[
\mathcal N
=p+\frac{p(p-1)}2\pi
=0.
\]

Therefore the exact Tate complex is

\[
\boxed{
\cdots
\xrightarrow{0}R
\xrightarrow{\pi}R
\xrightarrow{0}R
\xrightarrow{\pi}R
\xrightarrow{0}\cdots.
}
\]

Since

\[
\ker(\pi)=\pi R=\operatorname{im}(\pi),
\]

one obtains one copy of `k` in each Tate parity:

\[
\boxed{
\widehat H^{\rm even}(C_p,R_{\rm tan})\cong k,
\qquad
\widehat H^{\rm odd}(C_p,R_{\rm tan})\cong k.
}
\]

## 4. Bockstein

Lift the quotient generator `1 in R/pi R` to `1 in R`. Applying `tau-1` gives

\[
(\tau-1)1=\pi.
\]

After dividing by `pi` and reducing modulo `pi`, the resulting class is `1`. Thus the coefficient Bockstein is

\[
\boxed{
\beta_{\tau}=1:k\longrightarrow k.
}
\]

The norm already vanishes modulo `pi^2`, so its corresponding first Bockstein is zero.

The tangent extension and its nonzero Bockstein are therefore completely explicit. This is the strongest coefficient-only information available at first cyclotomic order.

## 5. Frobenius tangent ambiguity

The coefficient module does not determine the required arithmetic tangent.

For any

\[
\lambda\in k,
\]

define an `R`-linear Frobenius lift

\[
\Phi_\lambda(x)=(1+\lambda\pi)x.
\]

Every `Phi_lambda`:

1. commutes with `tau`;
2. induces the identity on `R/pi R`;
3. induces the identity on `pi R`;
4. induces the identity on both Tate groups;
5. preserves the same nonsplit extension and the same Bockstein.

Nevertheless its ordinary trace on the rank-one `R`-module is

\[
\operatorname{Tr}(\Phi_\lambda)
=1+\lambda\pi.
\]

The first-order trace coefficient is the arbitrary scalar `lambda`.

### Theorem 5.1 — tangent Smith blindness

The following data do not determine the first cyclotomic Frobenius tangent:

- the reduction modulo `pi`;
- the two Tate groups;
- the nonsplit coefficient extension;
- the coefficient Bockstein;
- compatibility of Frobenius with the cyclic action.

Indeed all these data are identical for the family `Phi_lambda`, while the first-order trace coefficient ranges over every element of `F_p`.

Thus a mod-`pi^2` Smith/Tate construction cannot prove `M_a != 0` unless it carries an additional secondary Frobenius invariant.

The required invariant is naturally a divided group-ring or Hattori--Stallings trace on the free cyclic part, not the trace on the modular Tate object alone.

## 6. Two distinct cyclic directions

There are two `C_p` structures in the problem and they must not be conflated.

### Coefficient Fourier direction

The additive coefficient `c in F_p` is weighted by

\[
c\longmapsto\zeta^c.
\]

Its first-order reduction is the tangent extension constructed above.

### Root-cycle/Adams direction

The alternating hook character on the roots has value

\[
p
\]

on a single `p`-cycle and zero on every other Frobenius cycle type. It therefore gives the undivided irreducibility indicator

\[
p\,1_{\rm irr}.
\]

The raw Fourier-hook trace is consequently

\[
\boxed{
\mathcal H_a=p\mathcal F_a.
}
\]

The coefficient tangent acts in the first direction, while division by `p` is required in the second direction. The actual geometric object is therefore bi-equivariant; a one-directional mod-`pi^2` module does not perform the required division.

## 7. Exact precision obstruction

The cyclotomic identity

\[
\Phi_p(1+\pi)=0
\]

or, equivalently, the product formula for `p`, gives

\[
\boxed{
p=u\pi^{p-1}}
\]

for a unit `u in O^*`.

Combining this with

\[
\mathcal F_a=N_a+\pi M_a+O(\pi^2)
\]

gives

\[
\boxed{
\mathcal H_a
=u\pi^{p-1}N_a
+u\pi^pM_a
+O(\pi^{p+1}).
}
\]

Therefore:

1. the raw hook object is zero modulo `pi^2` for every `p>=5`;
2. modulo `pi^p`, the first visible coefficient is `N_a` at order `p-1`;
3. the first moment `M_a` occurs at order `p`;
4. recovering `M_a mod p` from the undivided hook trace requires precision
   \[
   \boxed{\mathcal O/(\pi^{p+1})}.
   \]

### Theorem 7.1 — divided-hook precision obstruction

A literal construction of the root-cycle Fourier object only modulo `pi^2` is formally incapable of detecting either the fixed-class count or its first coefficient moment.

The proposed phrase “mod-`pi^2` cyclic Fourier complex” is valid only after a canonical derived division by the root-cycle factor `p`. Without that division, the relevant information is shifted from orders `0,1` to orders `p-1,p`.

## 8. Corrected object

Let `K_a` denote an integral, bi-equivariant Fourier/Adams complex whose raw Frobenius trace is `H_a=p F_a`. The object actually required by the programme is not

\[
K_a\otimes^L\mathcal O/(\pi^2).
\]

It is a **divided tangent trace** with the following properties:

1. it canonically divides the root-cycle hook trace by `p`;
2. after division, it retains the coefficient-character filtration through `pi^2`;
3. it records the Hattori--Stallings/group-ring Frobenius trace on free `O[C_p]` summands;
4. its reduction gives
   \[
   N_a+\pi M_a\pmod{\pi^2};
   \]
5. it is compatible with Fourier pushforward and the wild-infinity compactification.

Equivalently, one may avoid derived division and construct the raw integral complex through precision `pi^(p+1)`, then extract the coefficients at orders `p-1` and `p`.

These are two formulations of the same missing theorem.

## 9. Relation to the previous Smith obstruction

The previously proved pure-free-orbit counterexample showed that modular Smith localization can kill a free cyclic lattice carrying an arbitrary characteristic-zero Frobenius trace defect.

The present theorem is the first-order cyclotomic version of the same issue:

- the tangent Tate object sees the nontrivial extension;
- the Bockstein sees its coefficient class;
- neither sees the scalar `lambda` in the Frobenius lift;
- that scalar is exactly the type of datum needed for the first moment.

Thus passing from semisimple reduction to the tangent extension does not, by itself, cross the free-orbit Frobenius wall.

## 10. Ruling

### Built and proved

1. The coefficient Fourier character modulo `pi^2` is the unique nonsplit self-extension of the trivial `F_p[C_p]`-module.
2. Its Tate complex is explicitly `... -> R --pi--> R --0--> R -> ...`.
3. Both Tate groups are one-dimensional.
4. The coefficient Bockstein is nonzero.
5. Tate groups plus Bockstein do not determine the Frobenius tangent.
6. The undivided hook factor `p=u pi^(p-1)` shifts the count and first moment to cyclotomic orders `p-1` and `p`.
7. Raw precision `mod pi^(p+1)` is necessary to recover the first moment without derived division.

### Not proved

1. Existence of a canonical geometric divided-hook functor in the required integral Fourier category.
2. A formula for its Hattori--Stallings Frobenius tangent on the actual Airy free-orbit complex.
3. Nonvanishing of that tangent in either cubic square class.
4. The function-field `d=1` crown.

## 11. Exact next theorem

The programme has reached the following single target:

> **Divided cyclotomic Fourier theorem.** Construct a Frobenius-compatible integral model of the bi-equivariant root-cycle/coefficient-Fourier complex, together with a canonical division of its hook trace by `p`. Prove that its first coefficient Bockstein trace is the Cartier moment `M_a`, and compute the free-orbit Hattori--Stallings contribution sufficiently to show that the two square-class tangents cannot both vanish.

Any construction that supplies only modular Tate localization, the coefficient extension or its Bockstein is insufficient by Theorem 5.1.

## 12. Verification

Run

```bash
python frontier/strategy/cyclotomic_tangent_tate_precision_verify.py
```

The frozen output is

`frontier/strategy/cyclotomic_tangent_tate_precision_results_20260726.json`.

The verifier checks the dual-number model, the Tate complex, the Bockstein, the full family of invisible Frobenius tangents and the cyclotomic precision ledger for representative admitted primes.
