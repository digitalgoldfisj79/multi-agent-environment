# Katz--Tiep rank-four Laurent--Airy applicability audit

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Classification:** published external theorem plus proved specialization.  
**Scope:** Kummer-projected Hayes Adams boulder.

## 1. Identification with the published family

Katz and Tiep define the Laurent--Airy family with trace function

\[
(r,s,t)\longmapsto
-\sum_{x\ne0}
\psi(r/x+s x+t x^a)\chi(x).
\]

Take

\[
a=3,\qquad \chi=\chi_2,\qquad t=1.
\]

Then the two-parameter trace function is

\[
(r,s)\longmapsto
-\sum_{x\ne0}
\psi(r/x+s x+x^3)\chi_2(x),
\]

which is exactly the normalized trace function underlying the repository's sheaf

\[
\mathscr H_B(u,v)
=
H_c^1\left(
\mathbf G_m,
\mathcal L_{\chi_2}(x)
\mathcal L_\psi(x^3+ux+v/x)
\right)
\]

after `(r,s)=(v,u)`.

Thus the universal Hayes sheaf is a published Laurent--Airy local system, not merely analogous to one.

## 2. Published inputs that apply

From Katz--Tiep, *Airy sheaves of Laurent type: an introduction*:

- the one-parameter Laurent--Airy Fourier transform has rank `A+a`; here `A=1`, `a=3`, hence rank four;
- its local monodromy at the Fourier infinity is irreducible with all slopes `1/4`;
- the relevant local systems are geometrically irreducible.

From Katz--Rojas-Leon--Tiep, *On some Airy sheaves of Laurent type*, Lemma 2.10:

- for the two-parameter `t=1` specialization `G(1/x,x,a,chi)`, one has `M_(2,2)<=3`;
- equality holds when `a` is odd and `chi` is trivial or quadratic;
- therefore for `a=3`, `chi=chi_2`,
  \[
  \boxed{M_{2,2}=3.}
  \]
- the same family is geometrically self-dual after the standard Gauss normalization.

Their proof identifies three maximal fourth-moment components: the two permutation diagonals and the additional odd/self-dual plane `y=-x, z=-w`.

## 3. Exact exceptional-case warning

The same introductory paper proves tensor indecomposability in rank four except for

\[
\boxed{(A,B,a)=(1,1,3)}.
\]

Our family has exactly these parameters. Therefore the general tensor-indecomposability and `(S+)` machinery in that paper cannot be invoked to assert a full classical geometric monodromy group for this family.

In particular, the following claims are **not** supplied by the cited literature:

- geometric monodromy is `Sp_4`;
- the `p`-th Adams character has a bounded-rank realization;
- the Kummer-projected Adams complex has bounded Betti numbers;
- the required parameter-plane trace estimate.

## 4. Consequence for the programme

The published results verify that the underlying family has fixed rank, fixed local slopes, self-duality and minimal classical fourth moment. They rule out the concern that the Hayes construction concealed a growing-rank local system.

But they stop exactly before the load-bearing issue: the repository needs a correlation of the `p`-th Frobenius power trace, not a fixed fourth moment. The exceptional rank-four case prevents upgrading the literature to the required Adams theorem by a routine monodromy citation.

## 5. Ruling

### Published and applicable

- exact identification as `G(1/x,x,3,chi_2)` at `t=1`;
- rank four;
- geometric irreducibility and self-duality;
- `M_(2,2)=3`.

### Explicitly not supplied

- full monodromy determination in the exceptional `(1,1,3)` case;
- bounded complexity of the varying `p`-th Adams operation;
- the terminal `d=1` estimate.

The first boulder remains a genuinely new `p`-th Adams/Kummer correlation theorem, now located inside a well-studied but explicitly exceptional Laurent--Airy family.