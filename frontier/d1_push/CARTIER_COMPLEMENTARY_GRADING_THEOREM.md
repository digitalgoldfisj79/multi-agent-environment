# Cartier complementary torus grading and the one-level tail

> **Superseded in part on 2026-07-22.** The grading formulas `CCG.1`–`CCG.3` remain exact. The proposed support lemma `CT1-w1`, equivalently `beta<=gamma+2` for every nonzero complementary-minor product, is refuted at `p=223`. See `P223_CT1_W1_COUNTEREXAMPLE.md` and `p223_ct1_w1_counterexample_verify_results.json`.

**Date:** 2026-07-22  
**Status:** exact arithmetic grading theorem for every dominant `w=1` Cauchy-Binet term. The former reduction to `CT1-w1` is retained for provenance, but that lemma is now false.

## 1. Complementary notation

Use the notation of `CARTIER_COMPLEMENTARY_MINOR_REDUCTION.md`.

Let

`E subset {1,...,p-1}`, `p-3 notin E`,

`N={1,...,p-1}\E`,

`Q=(N\{p-3}) union {0}`.

For a Cauchy-Binet degree set `M subset {0,...,p-1}`, put

`R={0,...,p-1}\M`.

The two complements have equal size:

`C_0=E union {0}`, `C_1=E union {p-3}`.

Write the monomial attached to the term as

`a^I c^J d^K`.

## 2. Exact complementary degrees

The total cubic-factor count is

`I=(sum R-sum E-(p-3))/2.`

Since

`sum N=p(p-1)/2-sum E`,

`sum Q=p(p-1)/2-sum E-(p-3)`,

the linear and constant degrees are

`J=sum Q-3I`

and

`K=sum N-sum Q+2I`.

Substitution gives:

### Theorem CCG.1 — complementary degree formulas

`boxed( K=sum R-sum E, )`

`boxed( J=(p^2-3+sum E-3sum R)/2. )`

These identities are independent of whether the two complementary minors vanish.

## 3. Torus survivor equation

For a torus survivor, write

`J=alpha(p-1)`,

`K=beta(p-1)`,

with integers `alpha,beta>=0` in the positive-exponent projection.

The formula for `K` gives

`sum R=sum E+beta(p-1).`

Insert this into the formula for `J`:

`2alpha(p-1)`

` =p^2-3-2sum E-3beta(p-1).`

Reducing modulo `p-1` gives

`2(sum E+1)=0 mod (p-1).`

Therefore define the integer

`boxed( gamma=2(sum E+1)/(p-1). )`

The full equality then becomes:

### Theorem CCG.2 — torus grading simplex

Every dominant torus-surviving term satisfies

`boxed( 2alpha+3beta+gamma=p+1. )`

Thus the identity subset contributes a third nonnegative grading coordinate. The possible survivor triples lie on one finite integral simplex.

## 4. Filtration weight

The `(1,2)`-filtration weight is

`W=(alpha+2beta)(p-1).`

Using CCG.2,

`2(alpha+2beta)=p+1+beta-gamma.`

Hence:

### Corollary CCG.3 — excess formula

`boxed( W=(p^2-1)/2 + ((beta-gamma)/2)(p-1). )`

In particular `beta-gamma` is even. Therefore there is no survivor level halfway between consecutive multiples of `p-1`.

The old boundary corresponds to

`beta<=gamma`.

The first possible excess has

`beta=gamma+2`

and weight

`boxed( W=(p-1)(p+3)/2. )`

This is exactly the single extra level found in the complete ledgers for `29<=p<=47`.

## 5. Former corrected support lemma — refuted

The proposed complementary inequality was

`sum R<=3sum E+2p.`

Using

`sum R=sum E+beta(p-1)`

and

`2sum E=gamma(p-1)-2`,

this is equivalent to

`boxed( beta<=gamma+2. )`

The statement was called `CT1-w1`.

It is false. At `p=223`,

`E={5,7,8,12,13,14,16,17,18}`

and

`R={49,71,94,119,122,126,130,141,148,220}`

give

`gamma=1`, `beta=5=gamma+4`,

while

`det(P^(-1))_(R,E union {0})=86 mod 223`

and

`det(U)_(R,E union {220})=169 mod 223`.

The original `213x213` Cauchy-Binet determinant product is independently `114 mod 223`, also nonzero.

Thus an individual dominant term can occur at the second extra level

`W=(p-1)(p+5)/2`,

one full multiple of `p-1` above the former corrected boundary.

## 6. What remains exact and what changes

The grading still proves:

- support levels differ from the old boundary by integral multiples of `p-1`;
- `beta-gamma` is even;
- the first extra level is `beta=gamma+2`;
- the second extra level is `beta=gamma+4`.

What fails is the claim that nonzero individual complementary-minor products exclude the second and higher levels.

The `p=223` witness does not determine the **fully grouped** coefficient. Cancellation may still occur after summing degree sets, identity sets, and the four `w` blocks.

## 7. Correct replacement target

Route 1 can no longer proceed by bounding each Cauchy-Binet product separately. The correct object is the fully assembled torus coefficient:

1. sum all degree sets `M` for each identity set;
2. sum all identity sets contributing to the same monomial;
3. assemble `w=1,2,3,4` before asserting support or nonvanishing.

Any future support theorem must be a theorem about that complete assembly.

## 8. Epistemic classification

- Complementary degree formulas: exact.
- Integrality of `gamma`: exact consequence of torus orthogonality.
- Grading simplex and excess formula: exact.
- Spacing of possible filtration levels: exact.
- `CT1-w1` / `beta<=gamma+2`: refuted at `p=223`.
- Fully grouped dominant coefficient at the witness weight: open.
- Full Cartier support and nonvanishing: open.
- Function-field `d=1` crown: open.
