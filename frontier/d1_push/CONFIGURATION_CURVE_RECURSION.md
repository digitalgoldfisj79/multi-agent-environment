# Exact configuration-curve recursion for all weight-one hook cohomologies

**Date:** 2026-07-22  
**Status:** exact theorem. This gives a complete geometric presentation of every weight-one hook object in terms of oriented configuration curves. It does not prove that the resulting alternating presentation has `O(p)` effective rank.

## 1. Setup

Use the normalized degree-`p` root cover

`pi:Y=P^1_z -> P^1_t`, `t=f_q(z)`,

and `U=P^1_t \ {+1,-1,infinity}` as in `EXTREMAL_WEIGHT1_CURVES_THEOREM.md`.

Let `P` be the rank-`p` permutation local system on the roots and `V` its standard trace-zero summand:

`P=1 direct_sum V`.

Put

`H_i(q)=H^1(P^1_bar,j_* exterior^i V)`.

These are exactly the weight-one parts of the hook cohomologies.

## 2. Oriented configuration curves

For `0<=k<=p`, let `Conf_k(Y/U)` be the finite etale cover whose geometric fibre is the set of ordered `k`-tuples of distinct roots. The symmetric group `S_k` acts by permuting the tuple positions.

Let `X_(k,q)` be the smooth projective normalization of its compactification over `P^1_t`, and define the oriented configuration cohomology

`C_k(q)=H^1(X_(k,q),Q_l)^(sgn S_k)`.

Equivalently, one may first quotient the ordered configuration cover by `S_k` and retain the orientation local system. Over `U`, the corresponding local system is

`exterior^k P`.

Finite proper pushforward therefore gives

`C_k(q)=H^1(P^1_bar,j_* exterior^k P)`.

## 3. Exact two-step decomposition

Since `P=1 direct_sum V`, exterior algebra gives an actual local-system decomposition

`exterior^k P = exterior^k V direct_sum exterior^(k-1)V`.

Consequently:

### Theorem CCR.1

For every `0<=k<=p`,

`boxed( C_k(q)=H_k(q) direct_sum H_(k-1)(q), )`

with the conventions `H_(-1)=H_p=0`.

The endpoint terms satisfy

`H_0=H_1=0`:

- `H_0=H^1(P^1,Q_l)=0`;
- `P=1 direct_sum V`, while the compactified root curve is `P^1_z`, so `H^1(P^1,j_*P)=0`, forcing `H_1=0`.

Thus `C_0=C_1=0` and `C_2=H_2`, recovering the pair-curve theorem.

## 4. Recursive reconstruction

In the Grothendieck group of semisimple Frobenius modules,

`boxed( [H_i]=sum_(k=2)^i (-1)^(i-k)[C_k]. )`

Therefore every weight-one hook object is determined by explicit oriented configuration curves.

The full alternating weight-one survivor is

`W_1(q)=sum_(i=0)^(p-1)(-1)^i[H_i(q)]`.

Substituting the recursion and reversing the finite sums gives:

### Theorem CCR.2

`boxed( W_1(q)=sum_(k=2)^(p-1)(p-k)(-1)^k[C_k(q)]. )`

This is an exact complete geometric presentation of the post-pushforward weight-one door.

## 5. Complement duality

The complement of a `k`-subset of the `p` roots gives

`exterior^(p-k)P = exterior^k P tensor det(P)`.

Since `det(P)` is the sign local system `S`,

`boxed( C_(p-k)(q)=IH^1(exterior^k P tensor S). )`

Thus the configuration list is paired by quadratic sign twist. This is the general representation-theoretic source of the split/nonsplit and even-extension twist relations observed computationally.

## 6. Relation to the explicit `B_q` and `D_q` curves

- `C_2=H_2=H^1(B_q)^-` is the pair-curve anti-invariant factor.
- The extremal hook `H_(p-2)=H^1(D_q)` is obtained more economically from the discriminant fibre product in `EXTREMAL_WEIGHT1_CURVES_THEOREM.md`.
- For `p>=7`, the remaining middle hooks are recursively the primitive differences between successive `C_k` objects. These are precisely the higher configuration factors visible in the `p=7` spectra.

## 7. What this resolves and what it does not

Resolved exactly:

- every weight-one hook has an explicit configuration-curve realization;
- the survivor list is complete at the level of a finite geometric formula;
- the pair curve is the first primitive configuration term;
- complement/sign-twist duality is uniform.

Still open:

- proving that the alternating configuration expression cancels to effective rank `O(p)`;
- identifying the primitive middle factors by low-degree curves or correspondences;
- bounding the assembled q-line trace with a constant sufficient for positivity;
- the function-field crown.

The precise next lemma is therefore no longer “find a geometric model.” It is:

**Primitive configuration cancellation.** Pair the common semisimple constituents of the oriented configuration cohomologies in Theorem CCR.2, leaving `O(p)` total unmatched rank and q-conductor.

## 8. Epistemic classification

- Configuration-cover realization: exact finite-pushforward theorem.
- Two-step decomposition: exact exterior-algebra identity.
- Recursive and total formulas: exact finite algebra.
- Complement duality: exact representation-theoretic theorem.
- `O(p)` cancellation of the primitive configuration terms: open.
