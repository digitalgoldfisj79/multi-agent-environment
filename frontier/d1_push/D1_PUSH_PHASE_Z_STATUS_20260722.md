# d=1 crown push — Phase Z four-route status

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Starting head:** `784bf0fc3921ed916f9f91460e66039e17c3bd80`  
**Status:** natural theorem-level checkpoint. All four replacement routes have produced exact reductions or exact mass theorems. The function-field `d=1` crown remains open.

## 1. Executive assessment

The p=29 counterexample closed the original hard Cartier support cutoff. Phase Z pressed four replacement routes in parallel.

The outcome is not a crown proof, but it is substantive:

1. **Tail-inclusive Cartier:** the complete survivor ledger has a sharply corrected finite support pattern, and the dominant grouped coefficients have been reduced to products of small complementary inverse minors.
2. **Quantized nonvanishing:** parity plus the Cartier residue recovers the exact integer count whenever `N_a<2p`; exact data satisfy the stronger `0<N_a<3p/2` through `p=293`.
3. **Geometric direct image:** upper and lower hooks are exact sign-twist partners on the discriminant cover, halving the primitive families and locating the first unknown hook as an explicit complement in a base-changed ordered-pair cover.
4. **Singular-series/mass:** the complete linear-root distribution and exact first factor masses in degrees two and three are now proved; the quadratic second and linear-mixed moments are also exact.

Each route is now reduced to named proof gates rather than an unspecified search.

## 2. Route 1 — tail-inclusive Cartier assembly

### 2.1 Exact weight-resolved ledger

`cartier_weight_resolved_ledger.cpp` computes the complete torus projection of the Cartier cofactor, resolving every `(1,2)`-weight by exact Fourier inversion over `F_(p^2)^*`. Exact assignment bounds exclude aliasing.

The complete audit through `p=47` shows:

- the old cutoff

  `B_0=(p^2-1)/2`

  is valid through `p=23` and false from `p=29`;
- every audited nonzero coefficient satisfies the corrected bound

  `B_1=(p-1)(p+3)/2`;
- every above-`B_0` tail is supported at the single weight `B_1`;
- lower blocks `w=2,3,4` alter the top coefficient from `p=41`, so the dominant `w=1` object is not sufficient.

The full top-tail residues are:

| p | square | nonsquare |
|---:|---:|---:|
| 29 | 22 | 14 |
| 31 | 10 | 12 |
| 37 | 6 | 18 |
| 41 | 1 | 26 |
| 43 | 39 | 33 |
| 47 | 21 | 6 |

Thus the corrected support target is:

### Conjecture CT1

For every prime `p>=5`, every torus-surviving coefficient of the **complete** Cartier cofactor satisfies

`alpha+2beta <= (p+3)/2.`

CT1 is exact only in the finite audited range.

### 2.2 Complementary-minor theorem

For the dominant `w=1` identity-selected term, let `E` be the omitted falling-factorial rows, `M` the selected degree set, and `R` its complement. Jacobi's identity converts the large Cauchy-Binet product into

`det P_(N,M)det B_(Q,M)`

`=sign * product_(r in R)r!`

` * det(P^(-1))_(R,E union {0})`

` * det(U)_(R,E union {p-3}),`

where

`P_(n,m)=(n)_m`

and `U` is the inverse-substitution matrix associated with the formal inverse `psi+psi^3=X`.

The entries are explicit:

`(P^(-1))_(r,s)=(-1)^(r-s)/(s!(r-s)!),`

and, for `r=s+2h`,

`U_(r,s)=s/r (-1)^h binom(r+h-1,h).`

Lucas gives the exact support band

`U_(r,s)!=0 => r>=s, r=s mod 2, 3r-s<=2p.`

The dominant corrected support theorem is therefore reduced to:

### Lemma CT1-w1

If both complementary minors are nonzero and the torus grading holds, then

`sum R <= 3sum E+2p.`

The p=29 counterexample saturates this inequality exactly.

### 2.3 Route-1 gate

The next proof tasks are:

1. prove CT1-w1 for the two explicit small modular minors;
2. derive the four-shift complementary formula assembling `w=1,2,3,4` before determinant evaluation;
3. evaluate or control the single extra tail layer and the complete low-plus-tail sum.

Route 1 remains live, but support alone will not prove nonvanishing.

## 3. Route 2 — quantized nonvanishing

Let

`S_a=3aN_a mod p`

and let

`r_a=(3a)^(-1)S_a mod p`, `0<=r_a<p`.

The proved involution gives `N_a` even. Hence:

### Theorem DSQ.1

If

`0<=N_a<2p`,

then

`N_a=r_a` if `r_a` is even, and

`N_a=r_a+p` if `r_a` is odd.

In particular, under this bound,

`S_a=0 mod p iff N_a=0.`

Thus the Cartier residue becomes a complete integer certificate under one sharp size estimate.

The exact existing dataset gives, for both square classes separately,

`0<N_a<3p/2`

for every prime `5<=p<=293`. An independent sparse Rabin implementation reproduced the range through `p=199` and additional primes including:

- `p=211`: `(184,190)`;
- `p=251`: `(224,222)`;
- `p=307`: `(282,232)`.

A `p=401` continuation was cancelled after the CPU-XL job exceeded its allotted useful runtime; no `p=401` result is claimed from that job.

### Route-2 gate

The exact uniform target is now:

### Bound QNV

For every prime and at least one square class,

`0<N_a<2p.`

The finite evidence supports the stronger `N_a<3p/2`, but neither inequality is proved uniformly. Geometrically, QNV is the constant battle in the known estimate `N_a=p+O(p)`.

## 4. Route 3 — geometric direct-image remainder

Let `S=det(V)` be the sign local system and let

`pi:C_q^o -> U`

be the discriminant double cover.

### Theorem PHS.1

For every hook,

`V_(p-1-i)=V_i tensor S.`

### Theorem PHS.2

Projection formula on the sign cover gives an equality of Frobenius modules

`H^1(C_q,j_*pi^*V_i)`

`=IH^1(V_i) direct_sum IH^1(V_(p-1-i)).`

Thus only the lower half of the hook families is independent.

For `i=1`, this recovers the proved D curve. For the discriminant-base-changed ordered-pair cover `Z_(2,q)`, anti-swap cohomology gives:

### Theorem PHS.3

`H^1(Z_(2,q))^-`

`=H^1(D_q) direct_sum H^1(B_q)^- direct_sum IH^1(V_(p-3)).`

Therefore the first unresolved upper hook is the explicit semisimple complement

`IH^1(V_(p-3))`

inside one concrete cover, after removing the known D and pair factors.

The central hook splits into two conjugate `A_p` constituents on the discriminant cover, and split/nonsplit readings are exact root-negation eigenspace traces of the same geometric object.

### Route-3 gate

The next geometric target is the total space of `Z_(2,q)` over the q-line:

1. determine its reducible/constant factors;
2. subtract the known B and D motives;
3. compute or bound the transcendental rank of the remaining total-space motive;
4. repeat recursively for the lower-half ordered configuration covers.

The route now has explicit varieties, but no uniform primitive-rank or positivity theorem yet.

## 5. Route 4 — singular-series and mass formula

### 5.1 Complete linear-root distribution

For

`L(c,d)=#{x in F_p:F_(c,d)(x)=0}`, `0<=L<=3`,

the complete distribution is:

`#{L=0}=(p^2-1)/3,`

`#{L=1}=(p^2-p+2)/2,`

`#{L=2}=p-1,`

`#{L=3}=(p-1)(p-2)/6.`

### 5.2 Quadratic-factor theorem

For `Q_2(c,d)` the number of irreducible quadratic factors:

`sum Q_2=p(p-1)/2,`

`sum binom(Q_2,2)=binom((p-chi(a))/2,2),`

`sum LQ_2=p(p-1)/2.`

Every irreducible quadratic `X^2-tX+n` divides exactly one slice member:

`c=1-a(t^2-n),`

`d=t(an-1).`

The complete `Q_2` distribution is reduced to one explicit third factorial moment, a two-dimensional additive correlation of six translated quadratic-character lines.

### 5.3 Cubic-factor theorem

For `Q_3(c,d)` the number of irreducible cubic factors:

`boxed(sum Q_3=(p^2-1)/3.)`

This is independent of `a`.

If `theta^p=A+Btheta+Ctheta^2` and the minimal polynomial is

`X^3-tX^2+sX-n`,

divisibility is equivalent to

`C+at=0`,

with unique

`c=as-B, d=-A-an.`

Translation `theta->theta+u` preserves `C` and sends `t->t+3u`, so every additive translation orbit of degree-three elements contains exactly one satisfying root. Dividing the `p^2-1` satisfying roots by the three roots of each irreducible cubic gives the mass theorem.

### 5.4 Rigorous low-degree singular series

The normalized first factor masses are exactly

`1, (p-1)/(2p), (p^2-1)/(3p^2)`

for degrees `1,2,3`, tending to the random-permutation cycle means

`1,1/2,1/3`.

This is now a theorem, not a probabilistic fit.

### Route-4 gate

The next exact masses are:

1. the quadratic third factorial moment;
2. `sum binom(Q_3,2)`;
3. mixed moments `sum LQ_3` and `sum Q_2Q_3`;
4. a cycle-index or sieve assembly with a signed or bounded remainder for factor degrees `>=4`.

The quadratic third moment appears computationally to be governed by a fixed six-line double-cover surface, but no uniform formula is claimed in this status.

## 6. Verification questions

### Does any route now prove the crown?

No. Routes 1–4 have exact new reductions and mass theorems, but no uniform positivity or nonvanishing theorem.

### Was the p=29 failure merely a local accident?

No. Nonzero above-old-bound tails persist at every audited prime `29<=p<=47`. They occupy one extra orthogonality level in the current data.

### Can the lower Cartier filtration blocks be ignored?

No. They alter the top tail coefficient at `p=41,43,47`.

### Does the Cartier residue contain enough information in principle?

Yes, conditional on `N_a<2p`: parity then recovers the exact count from the residue.

### Is Route 4 merely heuristic singular-series work?

No. The degree-one distribution and the quadratic/cubic first masses are exact finite-field theorems. The missing step is all-degree assembly.

## 7. Revised priority order

The four routes are not equally mature.

1. **Route 4:** evaluate the quadratic third moment and the first cubic mixed moments. These are fixed-dimensional exact character-sum surfaces and are the most immediate theorem targets.
2. **Route 1:** prove the small complementary-minor inequality CT1-w1 and derive the four-block analogue.
3. **Route 3:** construct and analyse the total q-space of `Z_(2,q)` after removing B and D.
4. **Route 2:** use outputs from Routes 1 or 3 to prove the constant bound `N_a<2p`; the quantization lemma will then convert residue information into exact counts.

The routes now interact: Route 1 supplies exact residues, Route 3 seeks the trace constant, Route 4 seeks a positive main term, and Route 2 explains precisely when either becomes a complete certificate.

## 8. Evidence files

Programme and status:

- `D1_PHASE_Z_FOUR_ROUTE_PROGRAMME_20260722.md`
- `D1_PUSH_PHASE_Z_STATUS_20260722.md`

Route 1:

- `cartier_weight_resolved_ledger.cpp`
- `cartier_weight_resolved_full_results.csv`
- `CARTIER_ONE_LEVEL_TAIL_AUDIT.md`
- `CARTIER_COMPLEMENTARY_MINOR_REDUCTION.md`

Route 2:

- `depressed_slice_irreducible_count.cpp`
- `depressed_slice_quantization_results.csv`
- `depressed_slice_large_prime_spot_checks.csv`
- `DEPRESSED_SLICE_QUANTIZATION_REDUCTION.md`

Route 3:

- `PRIMITIVE_HOOK_SIGN_COVER_THEOREM.md`
- `hook_sign_pairing_audit.py`
- `hook_sign_pairing_audit_results.json`

Route 4:

- `QUADRATIC_FACTOR_MASS_THEOREM.md`
- `quadratic_factor_mass_audit.py`
- `quadratic_factor_mass_audit_results.csv`
- `CUBIC_FACTOR_MASS_THEOREM.md`
- `cubic_factor_mass_audit.py`
- `cubic_factor_mass_audit_results.csv`
- `LOW_DEGREE_FACTOR_MASS_LEDGER.md`

## 9. Epistemic classification

Exact general-prime theorems:

- Cartier complementary-minor formula and inverse-substitution support band;
- depressed-slice quantization lemma conditional on `N_a<2p`;
- hook sign-cover pairing and explicit first primitive complement;
- complete linear-root distribution;
- quadratic first, second and linear-mixed factor masses;
- cubic first factor mass.

Exact finite computations:

- complete Cartier weight ledgers through `p=47`;
- exact depressed-slice counts through `p=293` from the existing dataset, with independent Phase-Z checks;
- quadratic mass audits through `p=101`;
- cubic mass audits through `p=29`;
- hook-character audits through `p=47`.

Open:

- CT1 and its four-block complementary proof;
- top-tail and total Cartier nonvanishing;
- uniform `0<N_a<2p`;
- bounded-rank/positive primitive geometric remainder;
- higher and all-degree factor-mass assembly;
- general-prime function-field `d=1` crown;
- integer Fortune conjecture.
