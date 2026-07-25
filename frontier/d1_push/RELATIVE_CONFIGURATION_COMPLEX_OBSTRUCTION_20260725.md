# Relative configuration-space face complex: exact construction and obstruction

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** generic fixed `q`, `q notin {0,2}`, in the function-field `d=1` hook programme.  
**Status:** **PROVED THEOREM-LEVEL OBSTRUCTION** to the relative configuration-space route specified in the handover. This does not close the global Fourier--Cayley or direct q-line routes.

## 1. Setup

Let

\[
U=\mathbf P^1_t\setminus\{+1,-1,\infty\}
\]

and let

\[
\pi:C_q\longrightarrow U
\]

be the generic degree-`p` root cover. Put

\[
\mathcal P=\pi_*\mathbf Q_\ell,
\qquad
\mathcal P=\mathbf1\oplus W,
\qquad
V_i=\bigwedge^iW.
\]

The geometric monodromy is `S_p`.

For `0<=r<=p`, let

\[
\operatorname{Conf}_r(C_q/U)
\]

be the relative ordered configuration space of `r` distinct roots. Let `rho_r` be its finite etale map to `U`. Alternating descent under the coordinate-permutation group `S_r` gives the oriented-subset local system

\[
\mathcal A_r
=
\left(\rho_{r!}\mathbf Q_\ell\otimes\operatorname{sgn}_{S_r}\right)^{S_r}.
\]

Its geometric fibre is

\[
\mathcal A_r\simeq\bigwedge^r\mathcal P.
\]

This construction is canonical, `S_p`-equivariant, compatible with base change in `q`, and requires no distinguished root.

## 2. Canonical face differential

The `r` deletion maps on ordered configurations descend, with alternating signs, to

\[
\partial_r:\mathcal A_r\longrightarrow\mathcal A_{r-1}.
\]

On a geometric fibre, if `epsilon:Perm_p -> 1` is the augmentation sending every root basis vector to `1`, then

\[
\partial_r=\iota_\varepsilon:
\bigwedge^r\operatorname{Perm}_p
\longrightarrow
\bigwedge^{r-1}\operatorname{Perm}_p.
\]

Therefore the required relative face complex exists:

\[
\boxed{
0\longrightarrow\mathcal A_p
\xrightarrow{\partial_p}
\mathcal A_{p-1}
\longrightarrow\cdots\longrightarrow
\mathcal A_1
\xrightarrow{\partial_1}
\mathcal A_0
\longrightarrow0.
}
\]

It is the Koszul complex of the nonzero augmentation functional.

## 3. Exactness theorem

Choose the canonical splitting in characteristic zero

\[
\mathcal P=\mathbf1\oplus W.
\]

Then

\[
\mathcal A_r
=
\bigwedge^r\mathcal P
\cong
V_r\oplus V_{r-1},
\]

with the conventions `V_{-1}=V_p=0`.

Under this decomposition,

\[
\partial_r|_{V_r}=0,
\qquad
\partial_r|_{V_{r-1}}:
V_{r-1}\xrightarrow{\sim}V_{r-1}.
\]

Hence

\[
\ker\partial_r=V_r=\operatorname{im}\partial_{r+1}.
\]

Thus:

\[
\boxed{
\mathcal A_\bullet\text{ is exact on }U.
}
\]

The result remains exact after `j_*`, compactly supported derived pushforward, parabolic pushforward, or base change, because it is already the zero object in the derived category of lisse sheaves on `U`.

## 4. First regression: the canonical complex has the wrong Euler object

The irreducibility hook object is

\[
\mathcal L_{\mathrm{hook}}
=
\sum_{i=0}^{p-1}(-1)^iV_i
=
\lambda_{-1}(W).
\]

Its character is

\[
\operatorname{Tr}(g|\mathcal L_{\mathrm{hook}})
=
\det(1-g|W)
=
\begin{cases}
p,&g\text{ is a }p\text{-cycle},\\
0,&\text{otherwise}.
\end{cases}
\]

It is nonzero in the Grothendieck group.

By contrast,

\[
\sum_{r=0}^{p}(-1)^r[\mathcal A_r]
=
\lambda_{-1}(\mathcal P)
=
\lambda_{-1}(\mathbf1)\lambda_{-1}(W)
=
0.
\]

Therefore the canonical face complex cannot have alternating Euler characteristic equal to the irreducibility hook object.

The tempting operation of taking

\[
V_r=\ker(\partial_r:\mathcal A_r\to\mathcal A_{r-1})
\]

recovers the hook terms, but the induced differential between successive kernels is identically zero. It restates the exterior-algebra identity and supplies no parity-reversing cancellation.

## 5. Generic Grothendieck-group obstruction

The hooks

\[
V_0,V_1,\ldots,V_{p-1}
\]

are pairwise nonisomorphic irreducible `S_p` representations.

Let `K` be any bounded complex of semisimple lisse `S_p`-local systems on `U` whose Euler class is

\[
[K]=\sum_{i=0}^{p-1}(-1)^i[V_i].
\]

For each `i`, the even-minus-odd multiplicity of `V_i` in the cohomology of `K` is `(-1)^i`. Hence at least one copy of every `V_i` survives in the generic cohomology. Consequently,

\[
\boxed{
\sum_n\operatorname{rank}\mathcal H^n(K)
\ge
\sum_{i=0}^{p-1}\dim V_i
=
2^{p-1}.
}
\]

In particular:

1. no complex with Euler class `L_hook` can be exact on the interior `U`;
2. its failure of exactness cannot be supported only at `t=+1,-1,infinity`;
3. no `O(p)` generic survivor can be obtained from such a complex before pushforward.

This is a formal `K_0` obstruction, not a low-prime observation.

## 6. Canonical face maps cannot create the post-pushforward hook pairing

Every deletion map, insertion transfer, and incidence correspondence between the relative configuration spaces is `S_p`-equivariant. Therefore it preserves the `S_p`-isotypic decomposition.

By Schur's lemma,

\[
\operatorname{Hom}_{S_p}(V_i,V_j)=0
\qquad(i\ne j).
\]

The canonical face operator only pairs the copy of `V_i` in

\[
\mathcal A_i=V_i\oplus V_{i-1}
\]

with the copy of the same `V_i` in

\[
\mathcal A_{i+1}=V_{i+1}\oplus V_i.
\]

After projecting to the hook kernels, the differential is zero. Applying parabolic cohomology does not change this: maps induced by these `S_p`-equivariant face correspondences still preserve the hook label.

Thus canonical relative deletion/insertion maps cannot produce a differential

\[
H^1(\mathbf P^1,j_*V_i)
\longrightarrow
H^1(\mathbf P^1,j_*V_{i+1})
\]

that cancels adjacent hook parities.

A construction that descends without a distinguished root must be `S_p`-equivariant. Therefore the two Phase-1 requirements

- descend canonically without choosing a root; and
- pair different hook labels by relative face maps

are incompatible.

## 7. Exact virtual-rank theorem

Although the relative face complex does not prove semisimple effectivity, the established local monodromy determines the signed parabolic rank exactly.

Let

\[
h_i=\dim H^1(\mathbf P^1,j_*V_i).
\]

Grothendieck--Ogg--Shafarevich gives

\[
h_i
=
2\dim V_i^{S_p}
+\dim V_i
+\operatorname{Sw}_\infty(V_i)
-2\dim V_i^{\langle\tau\rangle}
-\dim V_i^{I_\infty},
\]

where `tau` is a transposition and

\[
I_\infty=C_p\rtimes C_{(p-1)/2}.
\]

The proved penultimate-hook theorem gives

\[
h_{p-2}=2p-6.
\]

Since `V_(p-2)=W tensor sgn`, the sign is trivial on the geometric infinity inertia, the two finite invariant spaces each have dimension one, and the infinity invariant space is zero. The formula therefore yields

\[
\operatorname{Sw}_\infty(W)=p-3.
\]

The wild inertia has one break. Since `W` has wild codimension `p-1`, the break in Swan normalization is

\[
\beta=\frac{p-3}{p-1}.
\]

Now use the p-cycle detector:

\[
\sum_i(-1)^i\dim V_i=0,
\]

\[
\sum_i(-1)^i\dim V_i^{\langle\tau\rangle}=0,
\]

\[
\sum_i(-1)^i\dim V_i^{I_\infty}=2,
\]

\[
\sum_i(-1)^i\dim V_i^{C_p}=p-1,
\]

and the only global invariant is `V_0`. Hence

\[
\sum_i(-1)^i\operatorname{Sw}_\infty(V_i)
=
\beta(0-(p-1))
=
-(p-3).
\]

Substitution gives

\[
\boxed{
\sum_{i=0}^{p-1}(-1)^i h_i
=
-(p-3).
}
\]

After removing the proved end pieces

\[
h_1=h_{p-1}=0,
\qquad
h_2=2\left\lfloor\frac{p-1}{4}\right\rfloor,
\qquad
h_{p-2}=2p-6,
\]

the middle object

\[
\mathcal M_q
=
\sum_{i=3}^{p-3}(-1)^i
H^1(\mathbf P^1,j_*V_i)
\]

has exact virtual rank

\[
\boxed{
\operatorname{vrank}\mathcal M_q
=
p-3-2\left\lfloor\frac{p-1}{4}\right\rfloor.
}
\]

Equivalently,

\[
\operatorname{vrank}\mathcal M_q
=
\begin{cases}
(p-5)/2,&p\equiv1\pmod4,\\
(p-3)/2,&p\equiv3\pmod4.
\end{cases}
\]

This gives the exact regressions

\[
p=5:\ 0,
\qquad
p=7:\ 2,
\qquad
p=11:\ 4.
\]

It proves only a signed rank identity. It does not prove that the even and odd Frobenius modules share all but this many eigenvalues.

## 8. Regression tests

### Weight-zero Kummer theorem

The canonical face complex is exact and has zero derived pushforward. It therefore predicts zero, not the proved discriminant Kummer line. It fails this regression.

### Complete `p=5` decomposition

The proved parabolic ranks are

\[
(h_0,\ldots,h_4)=(0,0,2,4,0),
\]

so the hook object is the nonzero virtual module

\[
H^1(B_q)-H^1(D_q)
\]

together with the separately proved weight-zero Kummer line. The canonical face complex again predicts zero. It fails this regression.

### `p=7` middle block

The proved local data give

\[
(h_0,\ldots,h_6)=(0,0,2,10,12,8,0)
\]

and

\[
\operatorname{vrank}(V_3-V_4)=2.
\]

The block is nonzero. Since

\[
\operatorname{Hom}_{S_7}(V_3,V_4)=0,
\]

the canonical face maps cannot supply its cancellation. It fails this regression.

## 9. Ruling

The relative configuration-space chain complex requested in Phase 1 has been constructed exactly. It is the canonical Koszul face complex and is exact.

It cannot satisfy the required irreducibility-hook Euler identity. More generally, the generic `K_0` obstruction and Schur-label obstruction prove that no parity-reversing complex built solely from canonical relative deletion/insertion maps can reduce the middle hook object to `O(p)` effective rank.

Therefore:

\[
\boxed{
\text{the relative configuration-space face-map route is closed.}
}
\]

This reaches stopping condition 4 of the handover: a theorem-level obstruction closing the specified configuration-space route.

The surviving main-branch options require a genuinely different mechanism:

1. the global Fourier--Cayley complex of the sparse ordered-root section;
2. a direct invariant/quadratic q-line trace theorem;
3. a Frobenius/Adams correspondence that is not a canonical configuration face differential.

## 10. Verification

`relative_configuration_complex_verify.py` independently checks:

- the p-cycle detector for every conjugacy class at `p=5,7,11,13,17`;
- pairwise orthogonality of the hook characters;
- `wedge^r Perm = V_r + V_(r-1)`;
- exactness of the canonical face matrices at `p=5,7`;
- the complete parabolic rank vectors;
- total virtual rank `-(p-3)`;
- middle virtual rank `p-3-2 floor((p-1)/4)`.

The deterministic output ends with `ALL CHECKS PASSED`.
