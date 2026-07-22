# d=1 crown — end-to-end continuation status

**Date:** 2026-07-22  
**Base:** Claude commit `aede75b7590555d843322fd24de2ca958ecd25ee`  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`

## Scientific verdict

The function-field d=1 crown remains open, but the end-to-end run completed the entire extremal post-pushforward programme and reduced the remaining proof to one scalar averaged middle-configuration lemma.

The previous target, the D-family total-space theorem, is solved exactly. Both split and nonsplit D-readings are controlled by fixed elliptic K3 surfaces; the growing genus p-3 no longer creates a growing-motive ambiguity. Weight zero, pair curves, Kummer signs, quadratic descent, and all extremal q-averages are now exact.

## Results completed in this continuation

### 1. General weight-zero collapse

For every p>=5 and generic q,

`sum_i (-1)^i Gr^W_0 H_c^1(U,V_i)=kappa_q`.

All weight-zero constituents cancel except the single q-Kummer class.

### 2. Uniform extremal curves

For every p,

`IH^1(V_2)=H^1(B_q)^-`,

`IH^1(V_(p-2))=H^1(D_q)`.

The exact ranks are

`dim H^1(B_q)^-=2 floor((p-1)/4)`,

`g(D_q)=p-3`, `dim H^1(D_q)=2p-6`.

### 3. Complete configuration presentation

Every middle hook has a geometric configuration-curve model. If C_k is the sign-isotypic H^1 of the ordered distinct k-root configuration curve, then

`C_k=H_k direct_sum H_(k-1)`

and

`sum_i (-1)^i H_i=sum_(k=2)^(p-1)(p-k)(-1)^k C_k`.

### 4. Pair-family q-average

The unweighted generic-q trace of H^1(B_q)^- has an exact Legendre-symbol formula and absolute value at most 3. The weighted trace is also exact and at most p+2.

### 5. Ordinary D-family theorem

Let `epsilon=chi((-1)^((p-1)/2)3)`. Then

`sum_(q!=0,2) Tr(Frob|H^1(D_q))`

`=epsilon[-chi(-6)p-a_p(24.3.h.a)-chi(-1)-2chi(2)+2chi(6)].`

The proof compresses the genus-p family to a singular elliptic K3 with fibres

`I_2^*, I_6, I_1, I_3^*`,

Neron-Severi discriminant -24, and rank-two CM transcendental motive.

The weighted D-sum is elementary:

`D_+^chi=epsilon[-chi(-1)p-3]`.

### 6. Nonsplit quadratic descent

Nonsplit Frobenius is split Frobenius composed with root negation. This gives exact Kummer and pair signs and exact weighted D-sums.

The unweighted nonsplit D-sum is controlled by the fixed K3

`Y^2=rq[r(r-q-3)^2-(q-2)^2]`,

whose Jacobian elliptic surface has fibres

`I_1^*, I_6, I_1, I_1, I_3^*`.

Its Neron-Severi rank is at least 19, so its transcendental rank is at most 3. Thus the complete nonsplit D contribution is O(p) with an effective absolute constant.

### 7. Exact middle residual diagnostic

After subtracting Kummer, pair and D sectors, the primitive middle traces through p=31 are:

| p | plus class | minus class |
|---:|---:|---:|
| 5 | 0 | 0 |
| 7 | 0 | -26 |
| 11 | -80 | 24 |
| 13 | 49 | 77 |
| 17 | -51 | 151 |
| 19 | 22 | -10 |
| 23 | 148 | 54 |
| 29 | -210 | 22 |
| 31 | 196 | -360 |

The maximum observed absolute ratio is below 11.62. This strongly supports a direct Cp bound, but is not a proof.

## Final remaining theorem

For A=chi(a), let E_mid(A) be the selected generic-q primitive middle-configuration trace after the exact extremal ledger is removed.

### Middle Averaged Trace Lemma (MATL)

Prove that, for every p and at least one square class A,

`|E_mid(A)| <= C p`

for an explicit absolute constant C.

The selected generic irreducible count satisfies

`p I_A=p M_A-E_ext(A)-E_mid(A)`,

with `M_A>=p-3`. The extremal term already has an explicit fixed linear bound. Therefore any usable absolute MATL constant proves the crown beyond a finite threshold; the existing certificate covers p<1200 and can be extended if necessary.

MATL is weaker than the former semisimple-collapse target: it asks for one scalar q-averaged trace, not an effective O(p) model before averaging.

## Parallel Cartier formulation

The same cancellation appears in the Cartier determinant. The only possible survivor-support violation seen at p=11,13 is

`(alpha,beta)=((p-9)/2,3)`,

and its coefficient cancels separately in three structural strata. The relevant leading matrices are coefficient matrices of powers of the depressed cubic `aX^3+cX+d`; the missing X^2 term produces a derivative recurrence and a likely nonintersecting-path cancellation.

A uniform proof would establish the empirical support law

`alpha+2beta <= (p+1)/2`,

but that support law alone does not evaluate the Cartier sum. MATL remains the direct crown target.

## External bypass audit

Known prescribed-coefficient existence theorems do not apply: this sparse family fixes almost all intermediate coefficients to zero, rather than prescribing a bounded or small-density subset. No external theorem found bypasses MATL.

## Reproducibility

New theorem and audit files include:

- `WEIGHT0_COLLAPSE_THEOREM.md`
- `EXTREMAL_WEIGHT1_CURVES_THEOREM.md`
- `CONFIGURATION_CURVE_RECURSION.md`
- `PAIR_CURVE_Q_AVERAGE_THEOREM.md`
- `D_FAMILY_TOTAL_SPACE_THEOREM.md`
- `QUADRATIC_DESCENT_EXTREMAL_ASSEMBLY.md`
- `MIDDLE_CONFIGURATION_AVERAGED_FRONTIER.md`
- exact audit scripts and JSON result ledgers for each stage.

The ordinary D audit and quadratic-descent audit each pass for every prime 5<=p<=199. The middle residual table is exact through p=31.

## Natural stopping point

The requested end-to-end programme has completed every identified extremal phase. Further fixed-q spectral fitting, more K3 point counts, or generic hook-by-hook estimates would not address the remaining theorem. The next genuine advance must be a global cancellation argument for the alternating primitive configuration space after q-averaging, or an equivalent uniform Cartier determinant identity.

The general-p function-field crown is not yet proved. The integer Fortune conjecture remains separate and open.
