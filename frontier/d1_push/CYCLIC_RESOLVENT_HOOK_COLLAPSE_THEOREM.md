# Cyclic-resolvent collapse of the complete alternating hook object

**Date:** 2026-07-23  
**Status:** exact representation-theoretic and cohomological reduction for every prime `p>=5`. It replaces the full alternating hook list by one cyclic quotient and one rank-one twist. It does not by itself bound the resulting cohomology.

## 1. Setup

Let `G=S_p`, let `P` be its degree-`p` permutation representation, and write

`P=1 direct_sum V`

with `V` the standard trace-zero representation.

The complete alternating hook representation is

`Lambda= lambda_(-1)(V)=sum_(i=0)^(p-1)(-1)^i exterior^i V.`

For a permutation `g`, its character is

`chi_Lambda(g)=det(1-g|V)`.

Let `tau` be a `p`-cycle, `C=<tau>`, and let `psi:C->Q_lbar^*` be any nontrivial character.

## 2. Character of the alternating hook object

If `g` has `r` cycles on `{1,...,p}`, then `1` is an eigenvalue of `g` on `P` with multiplicity `r`, and therefore on `V` with multiplicity `r-1`.

Hence

- if `r>1`, `det(1-g|V)=0`;
- if `r=1`, then `g` is a `p`-cycle and its eigenvalues on `V` are the nontrivial `p`th roots of unity, so

`det(1-g|V)=product_(j=1)^(p-1)(1-zeta_p^j)=p`.

Thus:

### Lemma CRH.1

`boxed(chi_Lambda(g)=p if g is a p-cycle, and 0 otherwise.)`

The value at the identity is zero, as expected from the virtual dimension

`sum_i (-1)^i binom(p-1,i)=0`.

## 3. Induction from a Sylow p-subgroup

For any character `theta` of `C`, the induced-character formula is

`chi_(Ind_C^G theta)(g)`

`=(1/|C|) sum_(x in G, x^(-1)gx in C) theta(x^(-1)gx).`

If `g` is neither the identity nor a `p`-cycle, no conjugate of `g` lies in `C`, so both induced characters vanish.

At the identity, both induced representations have dimension `[G:C]=(p-1)!`, so their difference vanishes.

If `g` is a `p`-cycle, every nonidentity element of `C` is conjugate to `g` in `S_p`. Each such element has exactly `|C_G(g)|=p` conjugators from `g`, and therefore

`chi_(Ind_C^G 1)(g)=p-1`,

while

`chi_(Ind_C^G psi)(g)=sum_(h in C\{1}) psi(h)=-1`.

Their difference is `p`.

### Theorem CRH.2 — cyclic induction identity

In the Grothendieck group of `S_p` representations,

`boxed(lambda_(-1)(V)`

`=Ind_C^(S_p) 1 - Ind_C^(S_p) psi. )`

All nontrivial choices of `psi` give isomorphic induced representations because the normalizer `N_(S_p)(C)=C semidirect F_p^*` acts transitively on the nontrivial characters of `C`.

## 4. Geometric realization

Use the normalized root cover

`Y_q -> U=P^1_t\{1,-1,infinity}`

with geometric monodromy `S_p`, and let

`Ytilde_q -> U`

be its geometric Galois closure. Put

`Z_(C,q)=Ytilde_q/C`.

The residual `C`-cover

`Ytilde_q -> Z_(C,q)`

defines a rank-one local system `L_psi` on the etale locus of `Z_(C,q)` through the character `psi`.

Finite pushforward and Shapiro give

`Ind_C^(S_p)1 = (Z_(C,q)->U)_*1`,

`Ind_C^(S_p)psi = (Z_(C,q)->U)_*L_psi`.

Therefore the complete alternating weight-one object

`W_1(q)=sum_i (-1)^i IH^1(exterior^i V)`

satisfies:

### Theorem CRH.3 — cyclic-resolvent cohomology

`boxed([W_1(q)]`

`=[H^1(Zbar_(C,q),j_*1)]`

` -[H^1(Zbar_(C,q),j_*L_psi)]. )`

The equality is in the Grothendieck group of arithmetic Frobenius modules. It is not merely a trace identity.

## 5. Relation to irreducible fibres

For a geometric Frobenius element `g_t` at an unramified fibre,

`Tr(g_t|lambda_(-1)(V))`

is `p` exactly when the root permutation is a single `p`-cycle, and is zero otherwise. Since the polynomial degree is the prime `p`, this is exactly `p` times the indicator that the fibre polynomial is irreducible.

Thus the cyclic-resolvent difference is the geometric source of the virtual p-cycle detector used throughout the d=1 programme.

## 6. Consequence for the middle frontier

The configuration recursion

`W_1(q)=sum_(k=2)^(p-1)(p-k)(-1)^k C_k(q)`

is therefore equal to the two-term cyclic-resolvent expression in CRH.3. The primitive middle residual is not intrinsically a list of `p-4` unrelated configuration motives; it is the part of one cyclic quotient/twist difference left after subtracting the explicit Kummer, pair and D sectors.

This changes the next geometric task:

1. construct a tractable model of the cyclic resolvent `Z_(C,q)` or its q-averaged total space;
2. compare the constant and `psi`-twisted cohomologies before estimating either separately;
3. remove the already identified extremal summands;
4. prove a weight-three bound for the residual difference.

## 7. Limitations

The degree of `Z_(C,q)->U` is `(p-1)!`, so CRH.3 is not yet a bounded-complexity model. The gain is structural: exponentially many configuration sheets and linearly many hooks are replaced by two isotypic cohomologies on the same quotient, making cancellation canonical rather than conjectural.

The terminal open step remains to show that the q-averaged primitive difference descends to a fixed-complexity weight-three object.

## 8. Audit

`cyclic_resolvent_hook_collapse_audit.py` verifies the character identity on every conjugacy type for all primes through a selected bound and checks agreement with the exterior-character polynomial of the standard representation.
