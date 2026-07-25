# Universal rank-four Hayes Laurent sheaf

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** first gate of the final analytic `d=1` programme.  
**Status:** the sheaf realization, generic rank and affine degree-drop ranks are **PROVED**. The `p`-th Adams conductor theorem is **OPEN**.

## 1. Universal family

Let

\[
S=\mathbf A^3_{u,w,v},\qquad
X=\mathbf G_m{}_x\times S,
\]

and let

\[
\pi:X\to S
\]

be projection. Define the rank-one sheaf

\[
\mathcal L_{u,w,v}
=
\mathcal L_\chi(x)
\otimes
\mathcal L_\psi(wx^3+ux+v/x).
\]

Put

\[
\boxed{
\mathscr H=R^1\pi_!\mathcal L_{u,w,v}.
}
\]

For a closed point `P` of `G_m` with root `alpha`, the local Frobenius trace is

\[
\chi(N(alpha))
\psi\left(
\operatorname{Tr}(u\alpha+w\alpha^3+v\alpha^{-1})
\right).
\]

Therefore the Euler product of the fibre `H_(u,w,v)` is exactly the Hayes `L`-function

\[
L(z,\Theta_{u,w,v}).
\]

Thus the previously introduced degree-at-most-four Hayes polynomial is not an abstract coefficient-class construction: it is the ordinary `L`-function of this explicit Kummer--Artin--Schreier sheaf on `G_m`.

## 2. Generic rank

Assume

\[
wv\ne0.
\]

At `x=0`, the phase has a pole of order one, so

\[
\operatorname{Swan}_0(\mathcal L_{u,w,v})=1.
\]

At `x=infinity`, the phase has a pole of order three, so

\[
\operatorname{Swan}_\infty(\mathcal L_{u,w,v})=3.
\]

Both orders are prime to `p` for the admitted primes. The Kummer factor is tame. Grothendieck--Ogg--Shafarevich on `G_m` gives

\[
\chi_c(\mathbf G_m,\mathcal L_{u,w,v})=-(1+3)=-4.
\]

The sheaf is geometrically nontrivial, so `H_c^0=H_c^2=0`. Hence

\[
\boxed{
\dim H_c^1(\mathbf G_m,\mathcal L_{u,w,v})=4
\qquad(wv\ne0).
}
\]

Consequently `H` is a rank-four lisse sheaf on the open torus

\[
S^\circ=\{wv\ne0\}.
\]

The lissity follows from local acyclicity: on this open the pole orders and their leading coefficients remain fixed and nonzero.

## 3. The two parameter-plane slices

The two sums in the terminal theorem come from

\[
\mathscr H_A=\mathscr H|_{v=1}
\quad\text{on }\mathbf A^2_{u,w},
\]

and

\[
\mathscr H_B=\mathscr H|_{w=1}
\quad\text{on }\mathbf A^2_{u,v}.
\]

Their rational-point Frobenius eigenvalues are the `alpha_j` used in the Hayes reduction, and

\[
I_p(u,w,1)=-\frac1p\operatorname{Tr}(F^p|\mathscr H_{A,(u,w)}),
\]

\[
I_p(u,1,v)=-\frac1p\operatorname{Tr}(F^p|\mathscr H_{B,(u,v)}).
\]

Thus the missing parameter-plane estimate is exactly a signed `p`-th Adams trace of two rank-four sheaves.

## 4. Exact affine degree-drop ranks

### Slice A: `v=1`

For `w!=0`, the rank is four.

At `w=0` and `u!=0`, the phase is

\[
ux+x^{-1}.
\]

It has Swan conductor one at both `0` and `infinity`, so

\[
\boxed{\operatorname{rank}\mathscr H_A|_{w=0,u\ne0}=2.}
\]

At `(u,w)=(0,0)`, the phase is `x^{-1}`. The Swan conductor is one at `0` and zero at infinity, hence

\[
\boxed{\dim H_c^1=1.}
\]

### Slice B: `w=1`

For `v!=0`, the rank is four.

At `v=0`, the phase is

\[
x^3+ux.
\]

The Kummer factor is tamely nontrivial at `0`, while the Swan conductor at infinity is three. Hence

\[
\boxed{\operatorname{rank}\mathscr H_B|_{v=0}=3.}
\]

for every `u`.

Thus the two slices have different affine boundary defects:

\[
4\to2\to1
\quad\text{for }\mathscr H_A,
\]

and

\[
4\to3
\quad\text{for }\mathscr H_B.
\]

Any signed Adams cancellation theorem must include these boundary terms explicitly; cancellation of generic virtual ranks alone is insufficient.

## 5. What the generic rank calculation does and does not prove

The family has fixed local state dimension four, independent of `p`. This confirms the first requirement of the fixed-state programme.

However, the target uses

\[
\operatorname{Tr}(F^p|\mathscr H_s),
\]

not the ordinary first Frobenius trace. In the Grothendieck group this is the `p`-th Adams operation

\[
\Psi^p(\mathscr H).
\]

Although Adams operations preserve virtual rank, a standard symmetric-power realization of `Psi^p` has ranks growing polynomially in `p`, and bounded rank of `H` alone does not imply bounded compactly supported Betti numbers for the Adams object.

The next exact gate is therefore:

> Construct a geometric realization of the signed class
> \[
> \chi(-1)\Psi^p(\mathscr H_A)
> +\chi(3)\Psi^p(\mathscr H_B)
> \]
> and compute its generic and boundary inertia. Determine whether its compactly supported complexity is bounded independently of `p`.

## 6. Ruling

### Proved

- the universal rank-one Laurent sheaf realizing every Hayes fibre;
- rank four on `wv!=0`;
- the exact two plane slices producing `A_p` and `B_p`;
- affine rank drops `4->2->1` on slice A and `4->3` on slice B.

### Open

- local monodromy of the `p`-th Adams class at parameter infinity;
- cancellation of the unequal affine boundary defects in the signed combination;
- a bounded-complexity realization of the signed Adams object;
- the terminal correlation estimate.