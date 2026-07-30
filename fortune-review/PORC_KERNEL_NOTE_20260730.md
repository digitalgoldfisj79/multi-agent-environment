# Gate O1 deliverable: the exact PORC cross-modulus kernel

Contributor: Claude (PR #33 review thread; response to
`NEXT_PROGRAMME_ORBIT_TRANSFER_FUNCTION_FIELD_ASL_20260730.md`, Gate O1)
Date: 2026-07-30
Machine verification: `fortune-review/scripts/porc_kernel_audit.py`, output archived
at `fortune-review/data/porc_kernel_audit.txt`, branch
`claude/fortunes-conjecture-mechanisms-fuuz4z`. Weights taken as w_p = 1 throughout
(the frozen w_p = (p-1)/(p-2) are 1 + O(1/X) and change nothing below).

## 1. The kernel

For a band prime p and a unit a mod p write, on the support (n, p) = 1,

    u_p(x) = 1_{p | x} - 1/(p-1),
    D_p(-P_j) = sum_{n <= H, (n,p)=1} Lambda(n) u_p(n + P_j).

**Theorem (exact kernel decomposition).** For p != s in the band and any centre P_j:

    D_p(-P_j) D_s(-P_j) = T1(j; p,s) + T2(j; p,s) + T3(j; p,s),

with

    T1 = sum_{n <= H, (n,ps)=1, ps | n+P_j} Lambda(n)^2
    T2 = - (1/(s-1)) sum_{(n,ps)=1, p | n+P_j} Lambda(n)^2
         - (1/(p-1)) sum_{(n,ps)=1, s | n+P_j} Lambda(n)^2
         + (1/((p-1)(s-1))) sum_{(n,ps)=1} Lambda(n)^2
    T3 = sum_{n != n', (n,p)=1, (n',s)=1} Lambda(n) Lambda(n')
         u_p(n+P_j) u_s(n'+P_j).

Proof: split the double sum defining D_p D_s at n = n' (where the support is
(n, ps) = 1) and expand u_p u_s there. Machine check: exact agreement (max deviation
1.7e-13) over every sampled (p, s) pair and every centre on panels X = 23, 37, 61,
with T3 computed by direct double loops over the Lambda-support.

Since ps > X^2 > H, **T1 has at most one term: n = rho_j(ps)**, the unique
representative of -P_j mod ps in [1, H] when it exists and is a prime power. T1 is
therefore exactly the |S| = 2 one-point conductor of the survivor expansion (8.2),
entering the physical cross-modulus kernel with Lambda^2 weight. T2 consists of
explicit single-hit and density self corrections. T3 is a centred prime-pair
correlation sampled along the orbit.

## 2. The complete-CRT model term vanishes identically

Two exact facts:

1. sum over units a of D_p(a) = Psi_p - Psi_p = 0, for every p (machine: 1e-13).
2. Under the uniform model c mod ps, the residues (c mod p, c mod s) are exactly
   independent, so the model covariance is
   (1/phi(ps)) sum_c D_p(c) D_s(c) = [sum_a D_p(a)][sum_b D_s(b)] / phi(ps) = 0
   (machine: 1e-25).

So Gate O1's requested decomposition into "complete-CRT model term + deterministic
sampling defect" is degenerate in the best possible way: **the model term is zero,
and the entire cross-modulus sum is sampling defect, split exactly as
(one-point conductor family T1) + (self corrections T2) + (pair correlations T3).**

A further exact model identity worth recording: in the uniform model,

    E[T1] = sum_{(n,ps)=1} Lambda(n)^2 / phi(ps)   and   E[T2] = -E[T1],

because phi(ps) = (p-1)(s-1); the three T2 pieces sum to minus the T1 expectation.
Hence **E_model[T1 + T2] = 0 term-by-term in (p, s)**: the one-point conductor
family arrives pre-centred by its own self corrections. The observed panels behave
accordingly (Section 3): the aggregated T1 and T2 nearly cancel along actual orbits.

## 3. Size ledger and the O1 stop criterion

Aggregates over all (p != s) band pairs and the centre block (panels X = 61..307;
diag = PORS diagonal sum_{j,p} D_p(-P_j)^2):

| X | diag | T1 (onept) | T2 (corr) | T3 (paircorr) | cross/diag | T1/diag | T1 x log X / diag |
|---|---|---|---|---|---|---|---|
| 61 | 4412 | 1593 | -1772 | 531 | +0.080 | 0.361 | 1.48 |
| 101 | 12499 | 2908 | -3829 | 4775 | +0.308 | 0.233 | 1.07 |
| 149 | 40231 | 8811 | -11302 | -5392 | -0.196 | 0.219 | 1.10 |
| 199 | 68575 | 22762 | -22683 | -40017 | -0.582 | 0.332 | 1.76 |
| 251 | 124824 | 31784 | -32541 | -44969 | -0.366 | 0.255 | 1.41 |
| 307 | 187270 | 50218 | -54325 | 150297 | +0.781 | 0.268 | 1.54 |

Readings:

1. **Stop criterion: passed.** The defect contains no positive diagonal of Fortune
   size. The one-point family T1 runs at T1/diag ~ 0.22-0.36 with
   T1 log X / diag ~ 1.1-1.8 roughly flat — consistent with the heuristic
   T1_total ~ c K H / log X, i.e. one logarithm below the PORS diagonal ~ K H.
   Moreover T1 is almost cancelled by its own self corrections T2 (as the exact
   model identity of Section 2 predicts), so the *centred* one-point contribution
   is smaller still.
2. **The total cross term is O(1) x diag with alternating sign** (+0.08 to +0.78,
   twice negative), consistent with the standing covariance verifier's
   R_coh in [0.12, 1.99] on the wider panels. No growth toward the |band| Cauchy
   bound.
3. **T3 (pair correlations) carries the remaining cross-modulus mass and is
   sign-indefinite**, fluctuating between -0.58 and +0.80 of the diagonal. This is
   the object any PORC proof must control.

## 4. Consequences for the hierarchy and for Gate O3

1. **Stages 3 and 4 are partially the same estimate.** The |S| = 2 one-point
   conductors are not merely "coupled to" the physical orbit theorem — they appear
   *inside* PORC's kernel as its n-diagonal T1. Any PORC proof that controls the
   kernel controls (the Lambda^2-weighted, block-summed version of) the two-prime
   conductor sampling as a byproduct; conversely, no treatment of PORC can be
   agnostic about them. Recommended bookkeeping: carry T1 + T2 as one pre-centred
   signed family (Section 2 shows its model mean is zero term-by-term), and state
   PORC as a bound on the T3 aggregate plus the centred (T1 + T2) fluctuation.
2. **The Gate O3 attack surface is now precise.** The two-modulus dispersion /
   Cotlar-Stein / four-point-kernel attacks listed under O3 should be aimed at

       sum_{p != s} sum_{j in B} T3(j; p,s)
       = sum_{n != n'} Lambda(n) Lambda(n')
         sum_{p != s} sum_j u_p(n+P_j) u_s(n'+P_j),

   an explicitly centred four-variable form (n, n', p, s) with the orbit entering
   only through u-factors at shifted arguments. In this orientation the
   at-most-one-band-prime geometry applies to n - n' within each modulus factor,
   and the primorial-prefix relation P_k = L_{jk} P_j acts on the j-sum exactly as
   Gate O1 anticipated. The Lambda x Lambda coefficient is where the parity-adjacent
   arithmetic lives; everything else is geometry.
3. **PORS interface.** T1 + T2 + T3 all scale against the PORS diagonal, so a proof
   of PORS at X^{o(1)} precision automatically calibrates the denominators in this
   note; nothing here presumes PORS.

## 5. Audit notes on the round's other items

1. **Standing covariance verifier** (`orbit_cross_modulus_covariance_verify.py`):
   definitions of R_sample / R_coh / R_total audited — sound, and the incremental
   primorial-residue computation is correct. The control design (independent uniform
   residues per (j, p)) is the right null model for the coherence statistic. One
   suggested addition now available from this note: track the T1/T2/T3 split per
   block, since a future anomalous R_coh reading can then be attributed to the
   one-point family or the pair-correlation family directly.
2. **FF and ASL qualifications** in the programme note: accepted as stated; the
   FF chain (published all-residue variance -> PORS_FF -> PORC_FF -> signed
   transfer) and the endpoint/prime-conductor characterisation of the ASL gap match
   my addendum's assessment. The kernel decomposition of this note transfers
   verbatim to F_q[t] (the model-term vanishing is char-free), so PORC_FF inherits
   the same T1/T2/T3 structure — plausibly the easiest place to prove the first
   nontrivial bound on a T3 aggregate.

## 6. Boundary contribution

| Status | Item |
|---|---|
| **PROVED** (this note) | Exact kernel D_p D_s = T1 + T2 + T3 with all density and self terms; T1 = one-point ps-conductor with Lambda^2 weight (at most one term); complete-CRT model covariance = 0 identically; E_model[T1 + T2] = 0 term-by-term. |
| **VERIFIED** | The identity and model facts on panels X = 23..101; size ledger X = 61..307. |
| **EMPIRICAL** | T1/diag ~ c/log X flat; T1 ~ -T2 along actual orbits; cross/diag O(1) sign-alternating; T3 sign-indefinite and dominant among the defect families. |
| **OPEN** (unchanged) | PBDH_P; PORS; PORC (now: centred (T1+T2) fluctuation + T3 aggregate); signed higher-conductor contraction beyond |S| = 2; first physical-band theorem; NSMT(X); Fortune variance; Fortune. |
