# Primitive hook pairing on the discriminant sign cover

**Date:** 2026-07-22  
**Status:** exact geometric reduction for every prime `p>=5`. This advances Phase Z, Route 3. It halves the unknown hook families and identifies the next primitive complement on one explicit sign-cover construction. It does not bound the remaining traces or prove the d=1 crown.

## 1. Setup

Use the normalized degree-p root cover

`f_q(z)=(qz^p+z^3-3z)/(q-2)`

over

`U=P^1_t\{1,-1,infinity}`.

Let `P=1 direct_sum V` be the rank-p permutation local system and its rank-`p-1` standard summand. Put

`V_i=exterior^i V`, `0<=i<=p-1`,

and

`IH^1_U(V_i)=H^1(P^1_bar,j_*V_i)`.

Let `S=det(V)` be the sign local system. Its double cover is the discriminant cover

`pi:C_q^o -> U`,

`C_q: y^2=u_q(t^2-1)`.

The smooth compactification `C_q` has genus zero, but the pullbacks of the nontrivial root local systems need not have zero cohomology.

## 2. Hook duality

For any rank-r vector space `W`,

`exterior^(r-i)W = (exterior^i W)^* tensor det(W)`.

Here `r=p-1`, `V` is self-dual, and `det(V)=S`. Therefore:

### Theorem PHS.1 — sign-paired hooks

For every `0<=i<=p-1`,

`boxed( V_(p-1-i) = V_i tensor S. )`

Consequently the hook ledger is determined by the lower half

`0<=i<=(p-1)/2`

together with the sign-cover descent data.

## 3. Discriminant-cover cohomology identity

Because `pi` is the quadratic cover associated with `S`,

`pi_* 1 = 1 direct_sum S`

on `U`. For every `V_i`, projection formula gives

`pi_* pi^*V_i = V_i direct_sum (V_i tensor S)`

`               = V_i direct_sum V_(p-1-i).`

Let `j_C:C_q^o -> C_q` be the open immersion into the smooth compactification. Finite pushforward commutes with middle extension in this setting. Hence:

### Theorem PHS.2 — paired intersection cohomology

`boxed( H^1(C_q_bar, j_(C,*) pi^*V_i)`

`       =IH^1_U(V_i) direct_sum IH^1_U(V_(p-1-i)). )`

This is an equality of arithmetic Frobenius modules, not merely an equality of dimensions or traces.

Equivalently, the two sign-paired hooks are the invariant and anti-invariant parts under the deck involution of one object on the discriminant cover.

## 4. Recovery of the known D curve

For `i=1`, PHS.2 gives

`H^1(C_q,j_*pi^*V_1)`

` =IH^1(V_1) direct_sum IH^1(V_(p-2)).`

The root-cover compactification is `P^1_z`, so `IH^1(V_1)=0`. The base-changed root cover is the hyperelliptic discriminant-twist curve `D_q` already constructed in `EXTREMAL_WEIGHT1_CURVES_THEOREM.md`. Thus PHS.2 recovers exactly

`IH^1(V_(p-2))=H^1(D_q).`

The D-family theorem is therefore the first nontrivial instance of a general sign-cover pairing.

## 5. The next primitive complement

Let `Y_q^(2)` be the ordered-distinct-pair cover of `U`, with swap involution `sigma`. Its anti-invariant local system is

`exterior^2 P=V_1 direct_sum V_2`.

After pullback to `C_q^o`, let `Z_(2,q)` be the smooth projective normalization of the resulting fibre product. The anti-swap cohomology satisfies

`H^1(Z_(2,q))^-`

` =H^1(C_q,j_*pi^*V_1) direct_sum H^1(C_q,j_*pi^*V_2).`

Using the D-curve identification for the first term and PHS.2 for the second gives:

### Theorem PHS.3 — explicit home for the next primitive hook

`boxed( H^1(Z_(2,q))^-`

`       =H^1(D_q)`

`        direct_sum H^1(B_q)^-`

`        direct_sum IH^1(V_(p-3)). )`

Here

`IH^1(V_2)=H^1(B_q)^-`

is the known pair-curve factor. Therefore the first unresolved upper hook is the exact semisimple complement

`boxed( IH^1(V_(p-3))`

`       =H^1(Z_(2,q))^- minus H^1(D_q) minus H^1(B_q)^-. )`

This converts an abstract middle hook into a concrete factor of one explicit discriminant-base-changed ordered-pair cover.

The same construction continues: the pullback of the ordered-distinct-k cover contains the paired hooks `V_i,V_(p-1-i)` for `i<=k`, and previously identified lower factors can be removed recursively.

## 6. Central hook

Put

`h=(p-1)/2`.

PHS.1 gives

`V_h=V_h tensor S`.

Hence its character vanishes on every odd permutation. The hook partition

`((p+1)/2,1^((p-1)/2))`

is self-conjugate. Its restriction from `S_p` to `A_p`, the geometric monodromy group on the discriminant cover, splits into two inequivalent conjugate irreducibles:

`V_h|_(A_p)=V_h^+ direct_sum V_h^-.`

The deck involution exchanges the two constituents. Thus the central hook is not an additional unpaired family: it is the single split middle object on the same discriminant cover.

## 7. Split/nonsplit readings as involution eigenspaces

The root-negation involution

`iota:(z,t)->(-z,-t)`

commutes with the discriminant deck action and with the configuration involutions. The nonsplit normal-form reading is `iota Frob`, while the split reading is `Frob`.

For every paired or primitive residual module `M=M^+ direct_sum M^-` under `iota`,

`Tr(Frob|M)+Tr(iota Frob|M)=2Tr(Frob|M^+),`

`Tr(Frob|M)-Tr(iota Frob|M)=2Tr(Frob|M^-).`

Therefore the split/nonsplit q-averages do not represent unrelated geometric families. They exactly isolate the two root-negation eigenspaces of one sign-cover object.

## 8. Primitive remainder recursion

Define `P_(i,q)` recursively on the discriminant cover by removing from

`H^1(C_q,j_*pi^*V_i)`

all lower configuration factors already identified through ordered-distinct covers. Then:

1. `P_(1,q)=H^1(D_q)`;
2. the paired `i=2` object contains `H^1(B_q)^-` and `IH^1(V_(p-3))` as in PHS.3;
3. only `1<=i<=(p-1)/2` must be constructed;
4. the upper hooks are recovered by deck eigenspaces;
5. split/nonsplit traces are recovered by `iota` eigenspaces.

This is a canonical geometric location and recursion for the primitive middle remainder. It eliminates duplication between upper/lower hooks and between split/nonsplit readings.

## 9. What this proves and what it does not

Exact consequences:

- the number of independent hook families is halved;
- every upper hook is a sign-cover partner of a lower hook;
- the D curve is the `i=1` sign-cover object;
- the first unresolved upper hook is a concrete complement in `Z_(2,q)`;
- the central hook splits over `A_p` and is controlled by the same cover;
- split/nonsplit averages isolate involution eigenspaces of one geometric object.

Still open:

- a uniform rank formula for the primitive complements;
- bounded transcendental rank of their total spaces;
- a sign or positivity theorem for their q-averaged traces;
- completeness of an O(p)-rank survivor list for all hooks;
- the function-field d=1 crown.

## 10. Audit

`hook_sign_pairing_audit.py` enumerates every conjugacy type of `S_p`, computes the complete exterior-character polynomial of the standard representation from the cycle type, and verifies

`chi_(p-1-i)(sigma)=sgn(sigma)chi_i(sigma)`

for every hook and every conjugacy type. It also verifies that the central-hook character vanishes on every odd type.

The audit is exact for every prime `5<=p<=47`.

## 11. Epistemic classification

- Hook duality: exact linear algebra and symmetric-group representation theory.
- Sign-cover pushforward identity: exact finite-cover projection formula.
- Middle-extension cohomology decomposition: exact.
- D-curve recovery: exact compatibility with the committed theorem.
- Pair-cover complement PHS.3: exact finite-pushforward/isotypic decomposition.
- Central-hook split over `A_p`: exact Clifford theory for self-conjugate partitions.
- Root-negation eigenspace formulas: exact commuting-involution algebra.
- Bounded-rank or positivity consequence: not proved.
