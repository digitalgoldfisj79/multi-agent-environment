# Applicability audit: geometric Weil kernels versus the wild-infinity Smith defect

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Classification:** published external theory plus an exact applicability boundary.  
**Status:** the published theorem supplies the oscillator kernel after realization; it does not supply the required wild nearby-cycle realization.

## 1. Published external theorem

For a finite-dimensional symplectic vector space over a finite field of odd characteristic, Gurevich and Hadani construct a canonical system of intertwining kernels between oriented Lagrangian models of the Heisenberg representation and its `ell`-adic geometrization. Their categorical refinement proves the compatibility/sign theorem for convolution of these kernels.

References:

1. S. Gurevich and R. Hadani, *The Geometric Weil Representation*, arXiv:math/0610818.
2. S. Gurevich and R. Hadani, *The Categorical Weil Representation*, arXiv:1108.0351.

The explicit normalizations are products of one-dimensional Gauss sums and the orientation pairing of the Lagrangians. Thus, once a sheaf is identified with the canonical intertwining kernel of a finite symplectic/Lagrangian correspondence, its weight, rank, Frobenius normalization and metaplectic sign are governed by published theory.

## 2. Linear data now available in the d=1 programme

The branch proves:

- the sparse coefficient space `V_p` is symplectic for the wild residue form `omega_p`;
- the high Pascal coefficient--normal matrix `D` is anti-symplectic;
- its graph `Gamma_D` is Lagrangian in `(V_p direct-sum V_p, omega_p direct-sum omega_p)`;
- the intrinsic lower monodromy half is a canonical oriented Lagrangian after choosing its natural ordered monomial basis;
- the required open-sector Airy class is
  \[
  \mathcal D_p(-(p-7)/2)-\mathcal D_p.
  \]

These are precisely the finite linear ingredients from which a geometric Weil kernel can be formed.

## 3. What the published theorem would settle

Assume the Airy-isotypic wild-infinity nearby-cycle sheaf is identified with the canonical geometric intertwining kernel attached to the proved Lagrangian data. Then published geometric Weil theory supplies:

1. the oscillator/Gauss normalization of size `q^((p-7)/2)`;
2. the `ell`-adic purity and perverse shift of the kernel;
3. the orientation-dependent quadratic character;
4. multiplicative compatibility of successive polarizations;
5. the absence of an unresolved metaplectic associativity sign.

The remaining sign can also be calibrated at the cubic origin by the proved affine torsor and Kummer-averaging identities.

## 4. What the published theorem does not settle

The Smith-defect phase is not initially a linear symplectic Fourier kernel. It is a wild Artin--Schreier family on the formal completion of the cyclic diagonal at root infinity, with:

- a maximally nonsplit characteristic-`p` Jordan normal filtration;
- nonlinear power-sum terms;
- a degree-drop specialization at the cubic origin;
- a cyclic trivial-minus-nontrivial projector;
- discriminant and affine quotient boundaries.

Geometric Weil theory does not prove that this nonlinear wild nearby-cycle complex is the canonical kernel attached to `Gamma_D`.

Likewise, standard local Fourier-transform calculations for individual meromorphic sheaves do not automatically identify this positive-dimensional family with the required kernel while preserving the cyclic projector and the global q-line boundary ledger.

## 5. Exact applicability boundary

The external theorem begins **after** the following new geometric statement has been proved:

> the Airy-isotypic formal wild-infinity Smith-defect phase is integrally linearizable, in the derived nearby-cycle category, to the canonical Lagrangian correspondence `Gamma_D`, with every non-Airy graded piece equal to the committed q-line/discriminant/Tate/affine boundary complex.

Before that realization, invoking the Weil representation would be circular: it would replace the missing nearby-cycle identification with an oscillator having the desired normalization.

After that realization, recomputing Gauss sums or constructing an ad hoc metaplectic normalization would be unnecessary.

## 6. Ruling

### Supplied by published theory

The canonical oscillator kernel and its normalization for the proved finite symplectic/Lagrangian data.

### New mathematics still required

The wild-infinity realization of the actual Smith-defect nearby cycles as that kernel, together with the complementary boundary identification.

This is the precise boundary between existing geometric Weil theory and the function-field `d=1` problem.
