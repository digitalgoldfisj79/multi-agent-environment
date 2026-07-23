# Cohomological audit of the Airy boundary defect

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** the target-cohomology rank statement is **PROVED** from Haessig's explicit effective decomposition for `k=p-2`. It closes the naive form of the boundary-lifting route.

## 1. Input from the near-intertwiner

From `AIRY_BOUNDARY_NEAR_INTERTWINER.md`, the integral lift

\[
P_p:\operatorname{Sym}^p\longrightarrow
\det\otimes\operatorname{Sym}^{p-2}
\]

has connection defect

\[
P_p\partial_p-\partial_{p-2}P_p
=-p\pi\left(aJ_p-\frac{(p-1)a^2}{3}E_p\right).
\]

The principal map is

\[
J_p(q_i)=r_i\quad(0\le i\le p-2),
\]

where

\[
q_i=v^{p-i}w^i,
\qquad
r_i=v^{p-2-i}w^i.
\]

## 2. Explicit target primitive cohomology

Set `k=p-2`. This is odd and strictly below `p`, so Haessig's effective decomposition theorem applies without the boundary denominator problem.

His explicit primitive cohomology basis is

\[
\boxed{
P H^1_{p-2}
=
\bigoplus_{j=0}^{(p-3)/2}
\mathbf C_p\,[a r_{2j}].
}
\]

It has dimension

\[
\frac{p-1}{2},
\]

agreeing with the exact degree of the determinant-twisted `Sym^(p-2)` Airy L-function.

## 3. PROVED: maximal projection of the principal defect

For every `j=0,...,(p-3)/2`,

\[
aJ_p(q_{2j})=a r_{2j}.
\]

Therefore the images of the even source monomials under the principal defect project to the full displayed basis of target primitive cohomology.

Hence

\[
\boxed{
\operatorname{rank}
\left(
M_p\stackrel{aJ_p}{\longrightarrow}M_{p-2}
\longrightarrow P H^1_{p-2}
\right)
=rac{p-1}{2}.
}
\]

The endpoint term `E_p` acts only on `q_p` and cannot remove these independent even-index classes.

## 4. Consequence

The stronger sufficient statement proposed in the first lifting note,

> the raw defect factors through `O(1)` top-weight cohomology classes after Dwork reduction,

is **FALSE**. Its direct projection already spans the entire linearly growing target primitive cohomology.

This does not logically exclude every possible corrected chain map. A correction may mix the source differential, higher p-adic filtration terms and Frobenius. But it proves that such a correction would have to cancel a maximally nontrivial family of target cohomology classes. It cannot be a bounded-rank perturbation of the canonical quotient map.

## 5. Revised verdict on the mod-p boundary mechanism

### PROVED and useful

- the mod-p Adams/Frobenius exact sequence explains the special `k=p` boundary;
- it explains why the two adjacent symmetric powers are p-adically correlated;
- its canonical lift has an exactly p-divisible defect.

### CLOSED naive route

The direct characteristic-zero lift does not yield a bounded cone:

- its module defect has full target rank `p-1`;
- its principal projection to target primitive cohomology has rank `(p-1)/2`.

### Remaining possibility

A successful Dwork proof would need a new Frobenius-equivariant cancellation acting simultaneously on the source differential and these `(p-1)/2` target classes. That is essentially the original global cross-symmetric-power correlation theorem in a more explicit basis, not a routine consequence of the modular exact sequence.

## 6. Scientific value

This phase identified a real structural mechanism and then tested it through both the connection and cohomology levels. The outcome is a precise failure certificate:

\[
\text{mod-p rank-two collapse}
\not\Rightarrow
\text{bounded characteristic-zero top-weight defect}.
\]

The absolute-constant `T_p` bound remains open. Further progress now requires either:

1. a genuinely Frobenius-dependent identity on the explicit Dwork basis; or
2. a valid Jacobi-sum decomposition of the `sigma Frob_p` trace on the cubic linear section.
