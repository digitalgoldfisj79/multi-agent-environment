# d=1 crown push — Phase X status

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Base:** Claude commit `aede75b7590555d843322fd24de2ca958ecd25ee`

## 1. Crown status

The function-field `d=1` crown remains open. It is machine-certified for every prime below `1200`; no uniform general-prime proof is claimed here.

This phase nevertheless closes every previously unidentified extremal term and converts the Cartier support conjecture into a precise modular determinant lemma.

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

After the weighted scaling `c->tc`, `d->t^2d`, coefficients become falling-factorial polynomials in the row parameter `n=p-u`. A nonzero determinant is a binomial/factorial-Schur minor.

The survivor grading imposes

`sum i = 1 mod (p-1)/2.`

The exact remaining lemma is:

### Modular filtered-minor lemma

Every identity-selected binomial/falling-factorial alternant satisfying the survivor grading and contributing nontrivially modulo `p` has `(1,2)`-weight at most

`(p^2-1)/2.`

The elementary assignment bound is insufficient: its first apparent excess occurs at `p=23`. The corresponding leading alternant vanishes modulo `23`. This is the concrete modular cancellation that must be proved uniformly.

The problem is now a finite determinant-divisibility statement. It is naturally expressible using binomial minors, factorial Schur functions and hook-content/product formulae.

## 4. What is closed

Closed without a new ingredient:

- further fixed-q hook-spectrum fitting;
- treating `C_3` or any single configuration degree as an `O(p)` survivor;
- using configuration recursion alone to derive positivity;
- further extremal Kummer/pair/D point-count work;
- searching for another growing-genus obstruction in the extremal sector.

## 5. Highest-value next move

Prove the modular filtered-minor lemma by:

1. writing each leading coefficient as a binomial determinant;
2. applying the general binomial-minor/Schur evaluation;
3. converting nonvanishing modulo `p` into a hook-content divisibility criterion;
4. showing that every partition above the survivor boundary contains a factor divisible by `p`;
5. checking that lower `w=2,3,4` terms cannot evade the same filtration criterion.

Success proves the Cartier survivor-support law uniformly. The next task would then be evaluation or nonvanishing of the boundary survivor sum.

## 6. Audits

- Weight-zero group audit: exact.
- Pair q-average audit: exact through `p=199`.
- Split D/K3 audit: exact through `p=199`.
- Split/nonsplit extremal audit: exact through `p=199`.
- Nonsplit discriminant-40 audit: exact through `p=499`.
- Cartier dominant-block audit: `176/176` exact determinant comparisons through `p=199`.

## 7. Epistemic classification

- All completed results above: exact theorems with stated dependencies.
- Modular filtered-minor lemma: open.
- Cartier survivor-sum nonvanishing: open.
- General-prime function-field crown: open.
