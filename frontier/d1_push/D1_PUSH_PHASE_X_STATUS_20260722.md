# d=1 crown push — Phase X status

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Base:** Claude commit `aede75b7590555d843322fd24de2ca958ecd25ee`

## 1. Crown status

The function-field `d=1` crown remains open. It is machine-certified for every prime below `1200`; no uniform general-prime proof is claimed here.

This phase nevertheless closes every previously unidentified extremal term and converts the Cartier support conjecture into a precise modular determinant problem.

## 2. Results completed in this continuation

### 2.1 Weight-zero collapse

The complete weight-zero hook ledger cancels to the single arithmetic Kummer class. This is uniform in `p`.

### 2.2 Uniform extremal curves

The pair family and discriminant-twist family occur for every prime:

`IH^1(V_2)=H^1(B_q)^-,`

`IH^1(V_(p-2))=H^1(D_q),`

with ranks `2 floor((p-1)/4)` and `2p-6` respectively.

### 2.3 Split D total-space theorem

The generic-q trace of the genus-`p-3` split `D_q` family is one elementary linear term plus the fixed rank-two weight-three CM coefficient of discriminant `24`.

### 2.4 Nonsplit D total-space theorem

The last rank-at-most-three placeholder is now exact. The controlling K3 surface has

- a nontorsion section over `Q(sqrt(2))`;
- Mordell-Weil group `Z direct_sum Z/2` geometrically;
- Neron-Severi discriminant `-40`;
- a rank-two CM transcendental motive over `Q(sqrt(-10))`.

Its affine character sum is

`U_1(p)=2chi_p(2)p+a_p(f_(-40)).`

Thus every split/nonsplit Kummer, pair and D term is explicit.

### 2.5 Configuration trace cancellation

For every fibre permutation `sigma`,

`sum_k(p-k)(-1)^k Tr(sigma|exterior^k P)
 =p*1_(sigma is a p-cycle).`

After finite and infinite boundary subtraction this gives

`Tr(Frob|W_1(q))=p-pI(q)-kappa_q.`

This proves the exact cancellation of the individually large configuration-degree Tate terms. It also proves that the generating-function route by itself is circular: after adding weight zero it is exactly the original irreducibility detector.

### 2.6 Cartier dominant-block theorem

For

`G(X)=aX^3+cX+d`

and the coefficient matrix

`A_p(G)=([X^e]G^n)_(1<=n<=p-1, e in {0,...,p-1}\{p-3}),`

one has

`det A_p(G)
 =-c^(p(p-3)/2)d^(p-3)((p-3)ad^2-c^3).`

The dominant no-identity Cartier block therefore already satisfies the empirical survivor-support bound.

## 3. Exact surviving gap

Expanding the Cartier cofactor by identity selections reduces the full support law to minors with

`R={1,...,p-1}\S,`

`C=(R\{3}) union {p}.`

After the weighted scaling `c->tc`, `d->t^2d`, coefficients become falling-factorial polynomials in the row parameter `n=p-u`. The survivor grading imposes

`sum i = 1 mod (p-1)/2.`

The previous provisional formulation claimed that every individual above-boundary falling-factorial alternant must vanish modulo `p`. Exact reconstruction at `p=23` disproves that formulation.

For the identity set

`S={16,17,18,21,22}`

there is an explicit dominant `w=1` assignment with

`sum i=34,  sum j=110,  sum k=88,`

and weight

`110+2*88=286 > 264=(p^2-1)/2.`

Its falling-factorial determinant is `3 mod 23`, its factorial scalar is `10 mod 23`, and its signed individual contribution is `7 mod 23`. Thus an individual above-boundary alternant can be nonzero.

The complete coefficient still vanishes. For this identity-selected minor, all `332,192` compatible distinct-degree assignments group into `18` falling-factorial degree sets. For every degree set, the factorial-weighted signed sum of column choices is `0 mod 23`, before multiplication by the corresponding alternant. The aggregate p=23 Fourier audit independently verifies all weights `286,308,330` for both square classes of `a`, including `w=1,2,3,4`.

Analogous raw excess assignments already occur at `p=17` and `p=19`, so the wording “the assignment bound first exceeds the boundary at p=23” is not correct for this natural dominant-`w=1` assignment model.

The corrected open theorem is:

### Factorial-weighted filtered-coefficient lemma

For every prime `p`, every identity-selected minor, every survivor exponent above the proposed boundary, and every fixed falling-factorial degree set `M`, the factorial-weighted signed sum of all column choices producing `M` vanishes modulo `p`, unless the associated alternant itself vanishes.

This coefficient-level statement is strong enough to imply the support law. It is strictly subtler than a hook-content divisibility theorem for individual alternants.

## 4. What is closed

Closed without a new ingredient:

- further fixed-q hook-spectrum fitting;
- treating `C_3` or any single configuration degree as an `O(p)` survivor;
- using configuration recursion alone to derive positivity;
- further extremal Kummer/pair/D point-count work;
- searching for another growing-genus obstruction in the extremal sector;
- claiming that all above-boundary individual factorial-Schur alternants vanish.

## 5. Highest-value next move

Prove the factorial-weighted filtered-coefficient lemma by:

1. fixing an identity subset and a falling-factorial degree set `M`;
2. writing its scalar coefficient as a signed sum of products `1/(i!j!)`;
3. converting that sum to a coefficient or determinant identity in binomial generating functions;
4. proving modular vanishing above the survivor boundary;
5. only then applying factorial-Schur or hook-content formulae to any residual degree sets;
6. checking that the lower `w=2,3,4` terms satisfy the same grouped cancellation.

Success proves the Cartier survivor-support law uniformly. The next task would then be evaluation or nonvanishing of the boundary survivor sum.

## 6. Audits

- Weight-zero group audit: exact.
- Pair q-average audit: exact through `p=199`.
- Split D/K3 audit: exact through `p=199`.
- Split/nonsplit extremal audit: exact through `p=199`.
- Nonsplit discriminant-40 audit: exact through `p=499`.
- Cartier dominant-block audit: `176/176` exact determinant comparisons through `p=199`.
- p=23 filtered-survivor audit: all `38/38` above-boundary coefficient checks vanish exactly over `F_(23^2)` for both square classes of `a`; Hugging Face CPU-XL job `6a61048b13e6ef894d54c19f`.
- p=23 leading-assignment reconstruction: one explicit nonzero weight-286 assignment, `332,192` compatible assignments, `18/18` grouped scalar coefficients zero modulo `23`.

## 7. Epistemic classification

- All completed geometric and extremal results above: exact theorems with stated dependencies.
- p=23 full support law: exact finite verification.
- p=23 leading-assignment reconstruction and grouped cancellation: exact finite verification.
- Previous individual-alternant filtered-minor lemma: refuted.
- Factorial-weighted filtered-coefficient lemma: open.
- Cartier survivor-sum nonvanishing: open.
- General-prime function-field crown: open.
