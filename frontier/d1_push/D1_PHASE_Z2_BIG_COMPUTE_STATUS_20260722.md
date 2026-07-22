# d=1 crown push — Phase Z2 big-compute status

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** natural stopping point reached by an exact counterexample. Large compute has materially advanced and corrected the programme, but has not proved the function-field `d=1` crown.

## 1. Executive result

The big-compute campaign did not brute-force a crown proof. It did something scientifically decisive instead:

1. it found and independently verified an exact `p=223` counterexample to the proposed dominant one-level Cartier minor bound `CT1-w1`;
2. it proved that the counterexample survives complete Cauchy-Binet grouping over all degree sets for its fixed identity set;
3. it completed broad exact cubic mixed-moment data through `p<500` and odd-locus cubic data through `p<700`;
4. it showed that the next cubic residuals behave as fixed-rank Frobenius terms rather than elementary polynomials;
5. it closed the termwise and fixed-identity support versions of Route 1.

The complete identity-set and four-block Cartier coefficient may still cancel. That question remains open.

## 2. Decisive Route-1 counterexample

At

`p=223`,

use

`E={5,7,8,12,13,14,16,17,18}`

and

`R={49,71,94,119,122,126,130,141,148,220}`.

The exact grading is

`gamma=1`, `beta=5`, `alpha=104`,

so

`beta-gamma=4`.

The proposed bound required `beta-gamma<=2`.

The two exact complementary minors are

`det(P^(-1))=86 mod 223`,

`det(U)=169 mod 223`.

The complementary product, including factorial and Jacobi factors, is

`114 mod 223`.

An independent direct calculation of the original `213x213` matrices gives

`det P=86 mod 223`,

`det B=48 mod 223`,

`det P det B=114 mod 223`.

The associated monomial is

`a^445 c^23088 d^1110`

with filtration weight

`W=25308`.

The former corrected one-level boundary is

`B_1=25086`,

so

`W=B_1+(p-1)`.

This definitively refutes `CT1-w1`.

## 3. The counterexample survives degree-set grouping

For the displayed identity set `E`, the sum over all Cauchy-Binet degree sets with the required grading is

`[z^1220] det(A^T diag(r!z^r)U)`.

This is a `10x10` determinant polynomial. Exact Fourier inversion over all `49,728` nonzero elements of `F_(223^2)` gives

`boxed(114 mod 223)`.

The determinant degree bound is `2,175`, below the multiplicative order `49,728`, so no aliasing is possible. The quadratic-field imaginary component is zero.

Therefore cancellation among degree sets for this fixed identity set does not restore the one-level bound.

Possible cancellation remains only after:

1. summing other identity sets with the same monomial grading;
2. assembling the `w=2,3,4` blocks with `w=1`.

## 4. What the support searches established

Two exact CP-SAT programmes separated support feasibility from modular determinant cancellation.

### Inverse-substitution support

For every prime `31<=p<200`:

- forbidden torus support matchings are impossible through `p=47`;
- support matchings exist from `p=53` onward.

### Complementary substitution support

- forbidden complementary support matchings are impossible at `p=31,37`;
- support matchings exist from `p=41` onward.

Thus neither entrywise support nor Hall matching can prove the former bound uniformly.

The randomized determinant adversary then tested more than twenty million exact torus-graded configurations across the prime range. Almost all companion `P^(-1)` minors were nonzero, while the `U` minors vanished until the exact `p=223` survivor was found. This demonstrates that the obstruction was genuine modular determinant cancellation, not simply missing support.

## 5. Route-4 cubic compute

### Cubic mixed moments

The exact trace-zero cubic parametrisation was evaluated for both square classes at all `69` primes

`103<=p<500`.

The computed moments were

`M_33=sum binom(Q_3,2)`,

`M_13=sum LQ_3`,

`M_23=sum Q_2Q_3`.

The data continue to show:

- `M_33` has leading scale `p^2/18` with non-polynomial lower terms;
- `M_13-(p^2-1)/3` has observed scale `O(p)`;
- `M_23-(p^2-1)/6` has observed scale `O(p)`;
- neither residual is an elementary polynomial in `p` and the square class.

This is consistent with the committed interpretation as traces of fixed-dimensional surfaces. It is finite evidence, not a uniform trace theorem.

### Odd-locus cubic factors

The exact odd-locus ledger was evaluated for both square classes at all `123` primes

`5<=p<700`.

The theorem

`Q_3(c,0)=2R_3(c)`

was confirmed pointwise throughout. In the computed range:

- `Q_3(c,0)` is always even;
- the maximum observed `Q_3(c,0)` is `8`;
- equivalently the maximum observed projected count `R_3(c)` is `4`;
- first, second and third odd-locus factorial moments fluctuate arithmetically rather than following one elementary polynomial.

The odd locus is therefore a small one-dimensional arithmetic component, but still carries nontrivial Frobenius information.

## 6. What has been closed

The following proposed mechanisms are now closed:

1. the old hard Cartier cutoff;
2. the corrected one-extra-level bound for each dominant Cauchy-Binet term;
3. the corrected one-extra-level bound after grouping degree sets for each fixed identity set;
4. proofs based only on support matching of the inverse-substitution matrix;
5. an elementary polynomial formula for the first cubic mixed residuals.

## 7. What remains live

### Route 1 — complete Cartier assembly

The only meaningful Cartier object now is the complete coefficient after summing:

- every identity set;
- every degree set;
- all four `w` blocks.

The immediate test is the full coefficient at the `p=223` witness grading. A nonzero result would refute the complete corrected support conjecture. A zero result would expose a new global identity-set or four-block cancellation.

### Route 4 — fixed-dimensional motives and all-degree sieve

The cubic pair and mixed moments remain explicit fixed-dimensional surfaces. The next theorem task is to identify their primitive motives or prove effective `O(p)` trace bounds, then insert these masses into an all-degree cycle-index or signed sieve.

### Routes 2 and 3

The quantized residue conversion and geometric direct-image pairing remain valid, but neither currently supplies the missing uniform positivity bound.

## 8. Compute and evidence

The complete job and source manifest is

`D1_PHASE_Z2_BIG_COMPUTE_MANIFEST_20260722.json`.

Core evidence files:

- `P223_CT1_W1_COUNTEREXAMPLE.md`;
- `p223_ct1_w1_counterexample_verify.py`;
- `p223_ct1_w1_counterexample_verify_results.json`;
- `p223_fixed_identity_grouped_fourier.cpp`;
- `p223_fixed_identity_grouped_fourier_results.json`;
- `cartier_complementary_minor_counterexample_search.cpp`;
- `cartier_u_support_cpsat.py`;
- `cartier_t_complement_support_cpsat.py`;
- `odd_locus_cubic_mass.cpp`;
- `cubic_mixed_mass_audit.cpp`.

No floating-point arithmetic is used for determinant, grading or counterexample claims.

## 9. Honest bottom line

Large compute did not finish the crown. It prevented the programme from spending further effort proving a false lemma, and it moved the Cartier frontier from a termwise support question to the genuinely correct complete-assembly question.

The strongest new result is negative but exact:

`CT1-w1` and fixed-identity one-level support are false at `p=223`.

The function-field `d=1` crown remains open. The integer Fortune conjecture remains open.
