# Fixed-set dynatomic sieve and the true uniformity wall

**Date:** 2026-07-22  
**Branch:** `gpt56/consolidated-fortune-20260721`  
**Status:** rigorous theorem schema for an arbitrary fixed finite set of periods; unconditional for the already certified set `{2,3,4,5}`. The general branch-separation lemma is isolated explicitly rather than silently assumed.

## 1. Setup

Fix a finite set

`S subset {2,3,...}`

and put

`F_(a,c,d)(X)=X^p+aX^3+cX+d`, `a!=0`,

`g_(a,c,d)(X)=-aX^3-cX-d`.

A degree-k irreducible factor of `F` is a Frobenius k-cycle and therefore an exact period-k cycle of `g`.

For every k define

`r_k=(1/k) sum_(m|k) 3^m mu(k/m)`.

The generic exact-period-k polynomial has `r_k` cycles, each containing k marked points. Its maximal permitted marked-cycle group is

`G_k=C_k wr S_(r_k)`.

Let

`E_k=sum_(j=0)^(r_k) (-1/k)^j/j!`.

By inclusion-exclusion in the natural action of `G_k` on the `k r_k` periodic points, `E_k` is exactly the proportion of elements with no fixed point. Equivalently, it is the proportion of Frobenius classes producing no degree-k factor.

## 2. Fixed-set branch-separation package

For a finite set S, let `BS(S)` denote the following finite geometric package over characteristic zero.

1. For every `k in S`, the exact-period-k splitting field of the generic centered cubic has group `G_k`.
2. Splitting fields belonging to distinct periods in S are linearly disjoint.
3. The local cubic

   `H_(a,c,d)(X)=aX^3+(c+1)X+d`

   retains full `S_3` monodromy after adjoining the complete period-S compositum.
4. Every nontrivial raw degree-p discriminant Kummer class remains nonsquare after adjoining the period-S and local-cubic fields.

Items 1 and 2 follow from Morton's full wreath-product and distinct-period linear-disjointness theorem on the unicritical specialization, followed by specialization-to-generic containment.

Items 3 and 4 are branch-separation statements. For any fixed S they reduce to finitely many algebraic checks:

- the generic local discriminant divisor must not be a branch component of any period-k field, `k in S`;
- the raw Kummer branch components `c=0`, `Fplus=0`, `Fminus=0` must not be branch components of the period-S/local compositum.

The existing Sage certificates establish `BS({2,3,4,5})`. A publication-grade theorem for arbitrary fixed S requires either a general generic-parabolic separation lemma or a finite certificate for the chosen S. This note does not promote that remaining lemma by assertion.

## 3. Direct fixed-set theorem

### Theorem FDS.1

Assume `BS(S)`. Then there is a finite exceptional set of rational primes `Sigma_S` such that, for every

- `p notin Sigma_S`,
- `p>max(S)`,
- `a in F_p^*`,

the number of locally admissible positive-discriminant members with no irreducible factor of degree in S satisfies

`N_(a,S,+)(p)`
` = (p^2/6) product_(k in S) E_k + O_S(p^(3/2)).`

The negative-discriminant sector satisfies the same formula.

The error constant depends on S. No uniformity in growing S is asserted.

### Proof

The complete marked period-S cover has geometric monodromy

`product_(k in S) G_k`.

The local cubic is independent and contributes the rootless Frobenius density `1/3`. The degree-p discriminant Kummer cover is independent and splits the surviving family equally between its two signs, contributing `1/2` to either parity sector.

Inside `G_k`, the no-fixed-point proportion is exactly `E_k`. Direct-product monodromy therefore gives total Frobenius density

`(1/3)(1/2) product_(k in S)E_k`.

Chebotarev/Lang-Weil on the resulting fixed finite cover of the coefficient plane gives the stated main term and an `O_S(p^(3/2))` error after excluding the finite bad-reduction set `Sigma_S`.

## 4. Certified case S={2,3,4,5}

The existing ramification and monodromy audits prove the hypotheses for

`S={2,3,4,5}`.

Hence

`N_(a,no2to5,+)(p)`
` = (p^2/6) E_2 E_3 E_4 E_5 + O(p^(3/2))`

outside the finite bad-characteristic set attached to the integral model, with the small characteristics separately machine-checkable.

Numerically,

`(1/6)E_2E_3E_4E_5=0.04600533167213053...`.

This consolidates all mixed factorial moments into one Frobenius-class theorem. The factorial tables are certificates and reproducibility tools, not conceptually necessary once direct-product monodromy is established.

## 5. Large-K density

Since `r_k` grows exponentially in k, the truncated exponential satisfies

`E_k=e^(-1/k)(1+epsilon_k)`

with `epsilon_k` superexponentially small in k. Therefore

`product_(k=2)^K E_k`
` = exp(-sum_(k=2)^K 1/k)(1+o(1))`
` = e^(1-gamma)/K * (1+O(1/K)).`

Formally, at the crown cutoff `K=floor(p/3)`, the positive-sector main term would be

`(p^2/6) product_(k=2)^(p/3) E_k`
` ~ (e^(1-gamma)/2) p`
` =0.7631... p.`

This recovers the correct order of the irreducible population.

## 6. Why fixed-set Chebotarev cannot reach the crown

Even an impossible uniform version of the standard two-dimensional error

`O(p^(3/2))`

would dominate the crown-scale main term `asymp p` when `K=p/3`.

Thus the remaining issue is not merely growth of the Lang-Weil constant with K. The generic square-root error in a two-dimensional coefficient plane is already one factor `sqrt(p)` too large even with constant one.

The crown requires one of the following stronger mechanisms:

1. cancellation or vanishing of the weight-three cohomology for the full-cycle class function;
2. a one-dimensional or boundary-localized trace formula with bounded conductor;
3. an exact determinant/cofactor nonvanishing identity;
4. a genuinely uniform correlation theorem that is stronger than ordinary Chebotarev.

This is the precise sense in which fixed-period independence is consolidation, while the growing-period problem is structural.

## 7. Correct status

- Arbitrary fixed S: reduced to the explicit finite package `BS(S)` and finite bad characteristics.
- S={2,3,4,5}: certified.
- K growing with p: open.
- K=p/3 crown: not approachable by a standard `p^(3/2)` Lang-Weil error, regardless of constant control.
