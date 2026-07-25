# Weight-one hook end pieces: pair Prym and discriminant twist

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** generic fixed `q`, `q notin {0,2}`, in the function-field `d=1` normal-form root cover.  
**Status:** **PROVED** for every odd prime `p>=5`, subject only to the already established generic smoothness and inertia statements for the root cover.

## 1. Root cover and hooks

Let

\[
f_q(z)=\frac{qz^p+z^3-3z}{q-2}
\]

and let

\[
\pi:C_q\longrightarrow\mathbf P^1_t
\]

be the degree-`p` root cover `t=f_q(z)`, restricted over

\[
U=\mathbf P^1_t\setminus\{+1,-1,\infty\}.
\]

The compactification of `C_q` is `P^1_z`. Let

\[
\operatorname{Perm}=\pi_*\mathbf Q_\ell,
\qquad
W=\operatorname{Std}=\operatorname{Perm}-\mathbf1,
\qquad
V_i=\bigwedge^iW.
\]

After the weight-zero boundary quotient proved in `WEIGHT_ZERO_HOOK_COLLAPSE_THEOREM_20260725.md`, the remaining object is the pure weight-one parabolic cohomology

\[
H^1(\mathbf P^1_{\bar{\mathbf F}_p},j_*V_i).
\]

## 2. The first hook has no weight-one part

By finite pushforward,

\[
H^1(\mathbf P^1,j_*\operatorname{Perm})
\cong H^1(\overline C_q,\mathbf Q_\ell).
\]

Since `Cbar_q=P^1_z`, the right side is zero. The trivial summand also has zero parabolic `H^1` on `P^1`. Therefore

\[
\boxed{
H^1(\mathbf P^1,j_*V_1)=0.
}
\]

Thus the large `H_c^1(U,V_1)` found in the hook ledger is entirely weight zero and is already cancelled by the preceding theorem.

## 3. The top hook has no weight-one part

The top hook is

\[
V_{p-1}=\det W=\operatorname{sgn}.
\]

Its sign character is the discriminant Kummer cover

\[
y^2=u_q(t^2-1).
\]

This is a genus-zero double cover of `P^1_t`. Hence

\[
\boxed{
H^1(\mathbf P^1,j_*V_{p-1})=0.
}
\]

Its sole contribution is the rank-one weight-zero Kummer line already isolated.

## 4. The second hook is an explicit Prym

The identity

\[
\bigwedge^2\operatorname{Perm}
\cong V_2\oplus V_1
\]

identifies `wedge^2 Perm` with the signed permutation sheaf on ordered pairs of distinct roots. Its geometric cover is the ordered-pair curve

\[
C_q^{(2)}:
\frac{P_q(z_1)-P_q(z_2)}{z_1-z_2}=0,
\qquad z_1\ne z_2,
\]

where

\[
P_q(z)=qz^p+z^3-3z.
\]

The transposition `z_1 <-> z_2` acts on the compactified curve. The sign in `wedge^2 Perm` selects the anti-invariant cohomology. Since `V_1` has no weight-one part,

\[
\boxed{
H^1(\mathbf P^1,j_*V_2)
\cong H^1(\overline C_q^{(2)})^{-}.
}
\]

### Explicit equation

Put

\[
s=z_1+z_2,
\qquad
\delta=z_1-z_2.
\]

In characteristic `p`,

\[
\frac{z_1^p-z_2^p}{z_1-z_2}=\delta^{p-1}.
\]

Also

\[
z_1^2+z_1z_2+z_2^2=\frac{3s^2+\delta^2}{4}.
\]

Therefore the pair curve is

\[
\boxed{
3s^2=12-\delta^2-4q\delta^{p-1}.
}
\]

It is hyperelliptic of genus

\[
g(C_q^{(2)})=(p-3)/2.
\]

The exchange involution is `delta -> -delta`. Its quotient, with `y=delta^2`, is

\[
3s^2=12-y-4qy^{(p-1)/2}
\]

and has genus

\[
\left\lfloor\frac{p-3}{4}\right\rfloor.
\]

Consequently the anti-invariant Prym has dimension

\[
\boxed{
\dim\operatorname{Prym}(C_q^{(2)}/(C_q^{(2)}/\langle\delta\mapsto-\delta\rangle))
=\left\lfloor\frac{p-1}{4}\right\rfloor.
}
\]

Thus

\[
\boxed{
\dim H^1(\mathbf P^1,j_*V_2)
=2\left\lfloor\frac{p-1}{4}\right\rfloor.
}
\]

This recovers the elliptic factor observed at `p=5` and `p=7` and predicts ranks `4,6,...` at `p=11,13,...`.

## 5. The penultimate hook is the discriminant-twist curve

Because `W` is self-dual,

\[
V_{p-2}
\cong W\otimes\det W
=\operatorname{Std}\otimes\operatorname{sgn}.
\]

Moreover

\[
\operatorname{Perm}\otimes\operatorname{sgn}
\cong\operatorname{sgn}\oplus(V_{p-2}).
\]

Pulling the sign Kummer cover back to `C_q=P^1_z` gives the double cover determined by the discriminant of the root polynomial as a function of `z`. At the two finite critical values,

\[
P_q(z)-(q-2)=q(z-1)^2g_{q,+}(z),
\]

\[
P_q(z)+(q-2)=q(z+1)^2g_{q,-}(z),
\]

where `g_(q,+)` and `g_(q,-)` have degree `p-2`. Removing the square factors gives the smooth hyperelliptic curve

\[
\boxed{
D_q:
 w^2=u_q\,g_{q,+}(z)g_{q,-}(z).
}
\]

The polynomial on the right has degree `2p-4`, so

\[
g(D_q)=p-3.
\]

The genus-zero sign summand contributes no weight-one cohomology. Therefore

\[
\boxed{
H^1(\mathbf P^1,j_*V_{p-2})
\cong H^1(D_q),
}
\]

and

\[
\boxed{
\dim H^1(\mathbf P^1,j_*V_{p-2})=2p-6.
}
\]

This proves the genus-2 and genus-4 identifications previously obtained by exact point counts at `p=5,7`.

## 6. What is now effective in general

The following weight-one pieces are explicit for every `p`:

- `V_1`: zero;
- `V_2`: the pair-curve Prym of rank `2 floor((p-1)/4)`;
- `V_(p-2)`: `H^1(D_q)` of rank `2p-6`;
- `V_(p-1)`: zero.

Together with the weight-zero Kummer theorem, this identifies an unconditional `O(p)` portion of the post-cancellation object.

## 7. Exact remaining middle-hook theorem

The unresolved weight-one virtual class is

\[
\boxed{
\mathcal M_q
=
\sum_{i=3}^{p-3}(-1)^i
H^1(\mathbf P^1,j_*V_i),
}
\]

with the understood adjustment that `V_(p-3)=V_2 tensor sgn` is itself a sign-twisted pair-configuration object.

At `p=5` the interval is empty, explaining the complete pair/D description. At `p=7` it contains the observed `V_3-V_4` middle block. The next load-bearing theorem is to pair this middle complex down to `O(p)` rank and then assemble it over the q-line.
