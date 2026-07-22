# Root-cover Koszul descent: exact construction and generic no-go

**Date:** 2026-07-22  
**Status:** exact root-selected contraction proved; descent with boundary-supported or O(p)-rank correction decisively refuted. The post-pushforward semisimple cancellation theorem remains open.

## 1. Setup

Let `E` be a characteristic-zero coefficient field in which `p` is invertible, let

`G=S_p`,

and let `P=E^p` be the permutation representation with basis `e_1,...,e_p`. Put

`1vec=sum_i e_i`,

`V=Std_p={sum_i x_i=0}`.

Then

`P=E*1vec direct_sum V`.

For a fixed-q root cover over the unramified t-line `U`, geometric monodromy is `S_p`. The degree-p root cover

`pi:X -> U`

corresponds generically to the subgroup

`H_i=Stab_G(i) ~= S_(p-1)`.

Pulling the standard local system to `X` distinguishes one geometric root.

## 2. Exact root-selected Koszul contraction

For each root label i define

`v_i=e_i-(1/p)1vec in V`.

The vector `v_i` is nonzero and fixed by `H_i`. With the standard G-invariant bilinear form,

`<v_i,v_i>=(p-1)/p`,

`<v_i,v_j>=-1/p` for `i!=j`.

Define the H_i-invariant covector

`phi_i=(p/(p-1))<v_i,->`,

so that `phi_i(v_i)=1`.

On the exterior algebra `Lambda^bullet V`, put

`d_i(omega)=v_i wedge omega`,

`h_i(omega)=iota_(phi_i)(omega)`.

The standard contraction identity gives

`h_i d_i+d_i h_i=id`.

### Theorem RKD.1

After pullback to the root cover `X`, the alternating hook object

`K(V): 0 -> Lambda^0 V -> Lambda^1 V -> ... -> Lambda^(p-1)V -> 0`

with differential wedge by the tautological vector is canonically contractible. Equivalently,

`lambda_(-1)(V)|_(S_(p-1))=0`

is realised by an explicit H_i-equivariant acyclic Koszul complex, not merely by an identity in the representation ring.

This proves the positive part of the proposed root-cover mechanism.

## 3. The descent obstruction is generic

On the double root cover `X x_U X`, an ordered pair of distinct roots `(i,j)` gives two contractions. Their defining vectors satisfy

`v_j-v_i=e_j-e_i`,

and

`||v_j-v_i||^2=2`.

Thus `v_j-v_i` is nowhere zero on the off-diagonal component. Consequently

`d_j-d_i=(v_j-v_i) wedge -`

and

`h_j-h_i=iota_(phi_j-phi_i)`

are nonzero on the entire ordered-distinct-root component.

That component is finite etale and dominant over the generic t-line. The disagreement is therefore not supported at the branch points `t=+/-1,infinity`, nor at the q-boundaries.

### Theorem RKD.2

The root-selected Koszul differential and contracting homotopy fail the first Cech descent condition on the dominant off-diagonal component of `X x_U X`. The failure is generic over `U`.

In particular, the contraction cannot descend with an error complex supported only on the finite ramification locus.

## 4. No alternative generic parity-reversing descent

For `0<=i<=p-1`,

`Lambda^i V ~= S^((p-i),1^i)`

is an irreducible hook representation of `S_p`. These hooks are pairwise nonisomorphic. Hence

`Hom_G(Lambda^i V,Lambda^j V)=0`

for `i!=j`.

In particular,

`Hom_G(K_even,K_odd)=0`,

where

`K_even=direct_sum_(i even) Lambda^i V`,

`K_odd=direct_sum_(i odd) Lambda^i V`.

### Theorem RKD.3

There is no nonzero G-equivariant parity-reversing map between the generic even and odd hook objects. Therefore no alternative differential on the same generic graded object can descend the root-selected contraction.

Any complex that becomes exact on the root cover but descends to `U` must acquire generic auxiliary terms; the failure cannot be repaired solely by local vanishing cycles.

## 5. Exponential lower bound for any generic correction

The virtual character

`Lambda_p=sum_i (-1)^i Lambda^i V`

has irreducible expansion with coefficient `+1` on every even hook and `-1` on every odd hook.

Because irreducible character expansion is unique, any semisimple effective presentation

`Lambda_p=[A]-[B]`

must contain at least every even hook in `A` and every odd hook in `B`, up to adding common summands. Therefore

`dim A >= sum_(i even) binomial(p-1,i)=2^(p-2)`,

`dim B >= sum_(i odd) binomial(p-1,i)=2^(p-2)`.

### Theorem RKD.4

Any generic residual object that repairs root-cover descent has total effective rank at least

`boxed(2^(p-1)).`

Thus root-cover Koszul descent cannot produce an `O(p)` generic correction. This is independent of the local conductor calculations.

## 6. Arithmetic interpretation

Restriction from `S_p` to `S_(p-1)` forgets every conjugacy class with no fixed point. In particular,

`Res_(S_(p-1))^(S_p)(Lambda_p)=0`,

because `S_(p-1)` contains no p-cycle.

More generally, the kernel of restriction contains class functions supported on all derangement cycle types, not only p-cycles. Selecting a root therefore erases precisely the arithmetic fibres on which Frobenius has no fixed root. Irreducible degree-p fibres are among those erased fibres.

The root-selected contraction is consequently strongest exactly where the target indicator is invisible. Recovering the p-cycle contribution requires descent through a Frobenius orbit of length p. That is the global degree-p trace-fibre/Adams problem already isolated in `CYCLIC_AIRY_FORMALISM_AND_NO_GO.md` and `ADAMS_PUSHFORWARD_NO_GO.md`.

### Theorem RKD.5

The obstruction to root-cover descent is not a boundary defect. It is the global fixed-point-free Frobenius sector containing the p-cycle class itself.

## 7. Relation to the branching cancellation

The exact branching rule is

`Res_(S_(p-1))^(S_p)(Lambda^i V)`

` =Lambda^i Std_(p-1) direct_sum Lambda^(i-1) Std_(p-1)`.

In the alternating sum, each `Lambda^j Std_(p-1)` occurs twice with opposite signs. This explains the acyclicity on the root cover.

It does not imply cancellation after descent: the two copies arise from different root choices, and their transition mismatch is the generic root-difference cocycle of Theorem RKD.2.

## 8. Strategic verdict

The proposed Root-Cover Koszul Descent Audit reaches the **refutation** stop rule.

Closed without a materially new ingredient:

- descent of the tautological Koszul contraction;
- a correction supported only at `t=+/-1,infinity` or `q=0,2,infinity`;
- an O(p)-rank effective generic residual obtained from the root cover;
- a Cech/root-choice averaging argument that ignores fixed-point-free Frobenius classes.

Not closed:

- cancellation after taking fixed-q `H_c^1` and then semisimplifying on the q-line;
- a genuinely new correspondence acting on the post-pushforward even and odd hook cohomologies;
- an arithmetic mechanism that directly handles length-p Frobenius orbits rather than selecting a fixed root.

The precise surviving theorem remains the one in `CYCLIC_AIRY_PHASE_STATUS_2026-07-22.md`: pair the common semisimple q-line constituents of the even and odd hook cohomologies, leaving only `O(p)` unmatched rank and conductor.

## 9. Epistemic classification

- Root-selected Koszul contraction: exact theorem.
- Generic off-diagonal descent failure: exact theorem.
- Absence of a generic G-equivariant parity map: exact representation-theoretic theorem.
- Exponential minimum residual rank: exact representation-theoretic theorem.
- Numerical audit: machine-certified finite exact arithmetic.
- Post-pushforward parity correspondence: open claim.
- Function-field d=1 crown: open.
