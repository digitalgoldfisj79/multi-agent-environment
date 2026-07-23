# Exact hook multiplicities in the cyclic cubic Milnor algebra

**Date:** 2026-07-23  
**Status:** exact representation-theoretic theorem for every odd prime `p>=5`, over characteristic zero or characteristic prime to `6p`. It refines the scalar cyclic trace identity. The Milnor algebra has exactly one hook multiplicity line in every graded degree: trivial in even degrees and standard in odd degrees. Thus the ordinary p-cycle trace `1` is an alternating sum of `p` lines, not an effective rank-one object.

## 1. Setup

Let

`H=Std_p`

be the standard representation of `S_p`, and let

`f=sum_i x_i^3 | H`.

The gradient quadrics form an `S_p`-equivariant regular sequence isomorphic to `H^*`. Hence the graded Milnor algebra

`M=Sym(H^*)/(partial f)`

has equivariant character

`[M](t)=Sym_t(H^*) lambda_(-t^2)(H^*)`.

For a permutation `g` of cycle type `lambda`,

`Tr(g|M;t)=det(1-t^2 g|H)/det(1-tg|H)`.

The hook Specht representation `(p-r,1^r)` is `wedge^r H`, and

`sum_(r=0)^(p-1) u^r Tr(g|wedge^r H)=det(1+u g|H)`.

## 2. Cycle-index average

Define the bivariate hook-multiplicity series

`A_p(t,u)=sum_(d,r) mult(wedge^r H,M_d)t^d u^r`.

By character orthogonality,

`A_p(t,u)`

`=1/p! sum_(g in S_p)`

` [det(1-t^2g|H)/det(1-tg|H)] det(1+ug|H).`

For a permutation with cycle lengths `l`, the three factors combine to

`1/[(1+t)(1+u)] product_cycles (1+t^l)(1-(-u)^l).`

The cycle-index exponential formula therefore gives

`sum_(p>=0) (1+t)(1+u) A_p(t,u) z^p`

`=exp(sum_(l>=1) ((1+t^l)(1-(-u)^l)/l) z^l)`

`=((1+uz)(1+tuz))/((1-z)(1-tz)).`

Extracting the coefficient of `z^p` and simplifying for odd `p` yields:

### Theorem CCHM.1 — complete hook multiplicity formula

`boxed(A_p(t,u)`

` = (1+t^2+...+t^(p-1))`

`   +u(t+t^3+...+t^(p-2)).)`

Equivalently:

- `M_(2j)` contains exactly one copy of the trivial representation;
- `M_(2j+1)` contains exactly one copy of the standard representation;
- no hook `wedge^r H` with `r>=2` occurs in any grade.

Non-hook representations account for the rest of the exponentially large Milnor algebra.

## 3. Recovery of the p-cycle trace

A p-cycle has hook character

`Tr(sigma|wedge^r H)=(-1)^r`.

Therefore CCHM.1 gives

`Tr(sigma|M;t)`

`=(1+t^2+...+t^(p-1))-(t+t^3+...+t^(p-2))`

`=(1+t^p)/(1+t),`

recovering `CYCLIC_CUBIC_MILNOR_TRACE_THEOREM.md`.

At `t=1`, there are `(p+1)/2` positive lines and `(p-1)/2` negative lines, so the scalar trace is `1`.

## 4. Frobenius consequence

Suppose the cubic model is defined over a finite field and Frobenius commutes with `S_p`. Write

`L_d=Hom_(S_p)(1,M_d)` for even `d`,

`L_d=Hom_(S_p)(H,M_d)` for odd `d`.

Each `L_d` is one-dimensional, but the Frobenius-twisted cyclic trace is

`boxed(Tr(sigma Frob|M)`

` =sum_(d even) Tr(Frob|L_d)`

`  -sum_(d odd) Tr(Frob|L_d).)`

There are exactly `p` multiplicity lines. The identity `Tr(sigma|M)=1` says only that their dimensions alternate to one. It does not identify their Frobenius eigenvalues or provide an effective rank-one presentation.

Consequently a direct Weil bound from this decomposition has a constant proportional to `p`, not an absolute constant, unless one proves additional Frobenius-equivariant cancellations or shows that the explicit boundary subtractions remove all but boundedly many `L_d`.

### Corollary CCHM.2 — failure certificate for the scalar-trace shortcut

The ordinary cyclic trace collapse

`Tr(sigma|M)=1`

does **not** imply that the Frobenius-equivariant local term has effective rank one or bounded absolute rank. Any proof using the cubic lift must construct pairings or explicit subtractions among the `p` multiplicity lines.

## 5. Relation to the endpoint programme

This theorem does not prove that all `p` lines occur in the actual post-Artin–Schreier endpoint complex. That identification remains the wild specialization problem.

It does prove that if the complete cyclic cubic Milnor object is inserted without further cancellation, the hoped rank-four conclusion is false: its hook-trace multiplicity object has linear effective size.

The next valid question is therefore not whether the cubic trace equals one, but which of the `L_d` survive the exact main/Kummer, Artin–Schreier/Tate and endpoint specialization subtractions.

## 6. Audit

`cyclic_cubic_hook_multiplicity_audit.py` computes the exact class-function inner products over all conjugacy classes and verifies CCHM.1 for selected primes. It uses integer polynomial arithmetic and rational character inner products; no random sampling or floating point is used.

## 7. Epistemic classification

### Exact

- equivariant complete-intersection character;
- cycle-index generating function;
- complete hook multiplicity formula;
- one trivial/standard hook line in alternating grades;
- absence of all higher hooks;
- linear number `p` of Frobenius multiplicity lines;
- invalidity of the scalar-trace-to-rank-one inference.

### Open

- which lines survive the actual wild endpoint specialization;
- Frobenius-equivariant cancellations among the surviving lines;
- absolute conductor-defect bound and crown.
