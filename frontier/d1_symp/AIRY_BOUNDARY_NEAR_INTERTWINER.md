# The Airy k=p near-intertwiner and its full-rank defect

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** the connection-matrix identity below is **PROVED** and symbolically verified. It shows both why the mod-p exact sequence is relevant and why its naive characteristic-zero lift does not finish the theorem.

## 1. Airy connection matrices

Use Haessig's Airy frame `v=x`, `w=x^2`. On the `k`-th symmetric power, write

\[
q_i=v^{k-i}w^i,\qquad0\le i\le k.
\]

The connection is

\[
\partial_k=a\frac d{da}-G_k,
\]

where, writing

\[
A=\pi a,\qquad B=-\frac{\pi a^2}{3},
\]

one has

\[
G_kq_i=A(k-i)q_{i+1}+Bi q_{i-1}.
\]

This is the tridiagonal matrix displayed in Haessig's effective-decomposition calculation.

## 2. Integral lift of the modular quotient

Let `r_j=v^(p-2-j)w^j`, `0<=j<=p-2`, be the basis of `det tensor Sym^(p-2)`; the determinant connection is trivial in this trace-zero Airy frame.

Lift the characteristic-p quotient map to the integral map

\[
P_p:\operatorname{Sym}^p\longrightarrow
\det\otimes\operatorname{Sym}^{p-2}
\]

by

\[
P_p(q_i)=i r_{i-1}\quad(1\le i\le p-1),
\qquad
P_p(q_0)=P_p(q_p)=0.
\]

Modulo `p`, this is exactly the quotient in the canonical sequence

\[
0\to F^*E\to\operatorname{Sym}^pE
\to\det(E)\otimes\operatorname{Sym}^{p-2}E\to0.
\]

## 3. PROVED: exact defect formula

Define

\[
J_p(q_i)=r_i\quad(0\le i\le p-2),
\qquad
J_p(q_{p-1})=J_p(q_p)=0,
\]

and define the endpoint map

\[
E_p(q_p)=r_{p-2},
\qquad E_p(q_i)=0\ (i<p).
\]

Then

\[
\boxed{
P_pG_p-G_{p-2}P_p
=pA J_p+p(p-1)B E_p.
}
\]

Equivalently,

\[
\boxed{
P_p\partial_p-\partial_{p-2}P_p
=-p\pi a J_p
+\frac{p(p-1)\pi a^2}{3}E_p.
}
\]

### Proof

For `1<=i<=p-2`, the `A`-part gives

\[
P_p(A(p-i)q_{i+1})
-Ai(p-1-i)r_i
=pA r_i.
\]

The `B`-part cancels exactly for the interior monomials:

\[
P_p(Bi q_{i-1})
-Bi(i-1)r_{i-2}=0.
\]

At the endpoint `q_p`, the source `B`-term is `pBq_{p-1}`, which maps to `p(p-1)Br_{p-2}` and has no target counterpart. All other endpoint terms agree with the displayed formula.

The complete matrix identity and the rank calculation are checked by `airy_boundary_intertwiner_verify.py`.

## 4. What the identity proves

### PROVED

1. The modular rank-two exact sequence is not an unrelated representation-theoretic coincidence. It is exactly the reduction modulo `p` of a natural map between the two Airy symmetric-power differential modules.
2. The failure of that lift to be a chain map is divisible by `p`.
3. The principal defect map `J_p` has rank `p-1`, the full dimension of the target module.

This supplies a concrete explanation for the high p-adic divisibility of the first virtual trace while simultaneously showing why divisibility does not imply bounded complex trace.

## 5. Failure of the naive lifting theorem

The hoped-for argument

> lift the mod-p rank-two sequence and obtain a bounded characteristic-zero cone

fails at the connection level. The first lift has a defect of full target rank. It is not a bounded-rank perturbation.

Changing the integral lifts of the coefficients cannot produce an honest `GL_2` intertwiner in characteristic zero: `Sym^p` and `det tensor Sym^(p-2)` are distinct irreducibles, and their difference is genuinely virtual.

Thus any successful boundary-Adams argument must use the **cohomological reduction**, not merely the differential modules. It must show that the full-rank operator

\[
aJ_p-\frac{(p-1)a^2}{3}E_p
\]

is null-homotopic, lower-weight, or bounded-trace after passage to the Dwork quotient and Frobenius action.

## 6. Smallest remaining lifting theorem

### OPEN cohomological-defect theorem

Let

\[
\mathcal D_p:=aJ_p-\frac{(p-1)a^2}{3}E_p.
\]

Prove that the Frobenius trace carried by the image of `mathcal D_p` in the mapping cone of the two Dwork complexes is `O(p^((p+1)/2))` with an absolute constant, or reduce it to a uniformly bounded top-weight quotient.

A sufficient stronger statement would be that `mathcal D_p` is chain-homotopic, after Dwork completion, to an operator factoring through `O(1)` top-weight cohomology classes.

## 7. Verdict

The mod-p sequence is a real global mechanism, not yet a proof. The first characteristic-zero lift has now been completely audited:

- it is canonical enough to identify the boundary phenomenon;
- its defect is exactly computable and p-divisible;
- the defect is full-rank before cohomological reduction.

The next work, if this route is pursued, is no longer vague: calculate the class of `mathcal D_p` in the explicit Dwork cohomology quotient and determine its top-weight Frobenius rank.
