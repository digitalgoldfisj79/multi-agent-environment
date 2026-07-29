# Next programme: full-band primorial-orbit Type-II dispersion

Date: 29 July 2026  
Repository: `digitalgoldfisj79/multi-agent-environment`  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`  
Starting head: `ac2235abc32166197f926074c35036e362ebc0dd`

## Status

**PROGRAMME BUILT; NOT YET CLAIMED AS A THEOREM.**

The preceding programme proved:

1. an exact inverse-orbit Type-II factorisation;
2. a bounded centre-plus-one-Type-II-variable frame on blocks `K << log X`;
3. a small complete-model frame for conductors containing at least two first-band primes;
4. a hard loss `X^{1-o(1)}/log X` when the remaining Type-II variable is separated by generic Cauchy.

The next programme therefore does **not** apply another arbitrary-coefficient frame to `POTD(X)`. It reinserts the complete Euler band before `TT^*`, removes the source-product diagonal exactly, and attacks only the genuinely off-source-diagonal bilinear tensor.

The intended endpoint is a full-band theorem which simultaneously contains:

- physical prime-modulus dispersion;
- the semiprime and higher one-point conductor terms;
- their signed covariance;
- the actual arithmetic Type-I/II/III coefficients.

Fortune's conjecture remains **OPEN**.

## 1. Strategic change

For one dyadic first physical band, let

\[
g_R(x)
=
V_R^{-1}\mathbf 1_{x_p\ne1\ {\rm for\ all}\ p\in\mathcal P_R}-1.
\]

For a critical bilinear cell, put

\[
b(n)=(\alpha*\gamma)(n)
=
\sum_{uv=n}\alpha_u\gamma_v
\]

and define the complete band amplitude

\[
\mathcal F_{j,R}(\alpha,\gamma)
=
\sum_{u,v}\alpha_u\gamma_v\,
g_R(-uvP_j^{-1}).
\tag{1.1}
\]

The previous route expanded only first order and then attempted to estimate the physical moduli before the one-point conductors were restored. The new route keeps (1.1) intact until after the source-product diagonal has been extracted.

This is forced by the exact identity

\[
|\mathcal F_{j,R}|^2
=
\sum_n |b(n)|^2 |g_R(-nP_j^{-1})|^2
+
\sum_{n\ne n'}b(n)\overline{b(n')}
g_R(-nP_j^{-1})\overline{g_R(-n'P_j^{-1})}.
\tag{1.2}
\]

The first term is where the physical cross-modulus diagonal and the semiprime/higher one-point conductors meet. It should be controlled **after** all Euler orders have recombined, not term by term.

The second term is the genuine deterministic pair-sampling problem.

## 2. Exact starting geometry

At the Fortune scale

\[
H=\eta X^2,\qquad 0<\eta<1,
\]

and on the first physical band every prime satisfies `p > X`.

For distinct products `n,n' <= H`, two different first-band primes cannot both divide `n-n'`, because

\[
pq>X^2>H>|n-n'|.
\]

Hence:

\[
\boxed{
n\ne n'
\quad\Longrightarrow\quad
\#\{p\in\mathcal P_R:p\mid n-n'\}\le1.
}
\tag{2.1}
\]

This is the central simplification of the new programme. In the off-source-diagonal tensor, the two forbidden source residues coincide at no band prime or at exactly one band prime. There is no multi-collision source geometry.

The complete-CRT covariance is therefore restricted to two explicit cases:

\[
\mathcal K_R(n,n')
=
A_R-1
\]

when no band prime divides `n-n'`, and

\[
\mathcal K_R(n,n')
=
A_R\frac{p-2}{p-3}-1
\]

when the unique collision prime is `p`.

The deterministic point still contains the nontrivial dilation spectrum. The purpose of (2.1) is not to replace that spectrum by its complete average; it is to make the exact completion sparse enough to analyse with the actual bilinear coefficients.

## 3. Target theorem

### `FBPOTD(X)` — full-band primorial-orbit Type-II dispersion

For every logarithmic block `B`, every first physical dyadic band, and every actual Type-II coefficient cell arising from the frozen prime-source identity, prove

\[
\boxed{
\sum_{j\in B}
|\mathcal F_{j,R}(\alpha,\gamma)|^2
\ll
\sum_{j\in B}\sum_n
|b(n)|^2|g_R(-nP_j^{-1})|^2
+
E^{\rm fb}_{B,R},
}
\tag{3.1}
\]

with errors which are summable over:

1. dyadic source cells;
2. physical prime bands;
3. logarithmic centre blocks;
4. the signed Type-I/II/III identity.

The right-hand term is the exact source-product diagonal, not a complete-model substitute.

A sufficient diagonal estimate is

\[
\sum_n|b(n)|^2
\le
\max_n r_{\mathcal U,\mathcal V}(n)\,
\|\alpha\|_2^2\|\gamma\|_2^2,
\tag{3.2}
\]

where `r_{\mathcal U,\mathcal V}(n)` is the number of representations `n=uv`. On dyadic divisor-bounded cells this is `X^{o(1)}`. After the frozen Fortune weights are restored, this diagonal lies below the Fortune block allowance by a polynomial margin.

Thus (3.1) asks for a Bessel estimate only on the off-source-diagonal tensor.

If proved with the required signed cell recombination, `FBPOTD(X)` replaces the separate pair `POTD(X)` plus deterministic one-point conductor sampling for the first physical band.

## 4. Phase A — exact prime-source identity

### A1. Fix one exact identity

Use a finite Heath--Brown identity, provisionally with three Möbius variables and cutoff

\[
Y=H^{1/3}<X.
\]

The implementation must reconstruct `Lambda(n)` exactly for every `n <= H` before any analytic grouping is accepted.

No asymptotic or symbolic shorthand is sufficient. The committed verifier must compare the full convolution identity with the exact von Mangoldt function on complete finite panels.

### A2. Preserve the small Möbius variables

For every Möbius variable `d <= Y`, nonzero `mu(d)` implies that `d` is squarefree and

\[
\boxed{d\mid P_j}
\tag{4.1}
\]

for every centre in the block, because every prime factor of `d` is below `X`.

The variables satisfying (4.1) must remain explicit in the dyadic ledger. They may not be absorbed prematurely into an arbitrary Type-II coefficient.

### A3. Cell classification

Every dyadic cell must be labelled as:

- Type I;
- balanced Type II;
- Type III or higher multilinear;
- negligible by support;
- merged only by an exact symmetry.

For each cell record:

- support lengths;
- coefficient formula;
- `L^1`, `L^2` and divisor-energy bounds;
- which Möbius variables divide every centre;
- the exact sign and multiplicity in the prime-source identity.

### Gate A

Pass only when:

1. the source identity reconstructs `Lambda` exactly;
2. every critical cell is explicitly listed;
3. no synthetic coefficient class is substituted for the actual arithmetic coefficients.

Failure at this gate means the present `POTD(X)` calibration was not tied closely enough to the real prime source.

## 5. Phase B — full-band lift and source diagonal

For every critical cell:

1. form the exact convolution `b=alpha*gamma`;
2. verify the direct `(u,v)` sum equals the compressed product sum;
3. construct the complete survivor amplitude (1.1);
4. split its square by `n=n'` and `n\ne n'`;
5. prove the divisor-multiplicity estimate (3.2);
6. restore the frozen coefficient `beta_j` and verify that the diagonal is inside the Fortune block budget.

The source-product diagonal must include all physical and one-point Euler orders automatically through `g_R`.

### Gate B

Pass if the complete source-product diagonal is Fortune-admissible for every actual critical cell.

If it is not, the full-band route fails before any new dispersion theorem is attempted.

## 6. Phase C — exact off-diagonal spectral completion

For `n\ne n'`, insert the already-proved signed dilation completion

\[
g_R(x)\overline{g_R(y)}
=
\mathcal K_R(xy^{-1})
+
\sum_{\theta\ne1}
\mathcal D_\theta(xy^{-1})\theta(y).
\tag{6.1}
\]

Do not replace the second term by complete-dilation energy.

Use (2.1) to derive exact formulae for:

1. no-collision pairs;
2. pairs with one collision prime;
3. conductor-`p` modes;
4. conductors containing at least two first-band primes.

The output must be an exact quadratic form in the actual source products, with the source diagonal already absent.

### Required decomposition

The conductor-`p` layer must be stratified by:

- `uv=u'v'` — already removed;
- `u=u'`, `v\ne v'`;
- `v=v'`, `u\ne u'`;
- genuinely off-diagonal `u\ne u'`, `v\ne v'`.

The one-variable strata are the natural place to reuse the bounded inverse-orbit frame. The genuinely off-diagonal stratum is the only place where a new bilinear contraction is allowed to remain.

### Gate C

Pass if the exact completion reduces the physical problem to one explicit off-diagonal bilinear kernel with no hidden positive conductor sum.

A failure means that the all-order recombination has not actually removed the one-point obstruction.

## 7. Phase D — primorial-divisor collapse

For every small Möbius variable satisfying (4.1), use

\[
P_j\overline d\equiv P_j/d\pmod p
\tag{7.1}
\]

inside the low-mode phases.

This removes one modular inverse **using the actual source arithmetic**, not an arbitrary coefficient estimate.

The programme must test three possible consequences in order:

### D1. Punctured-primorial orbit

Compute the full-band Gram for

\[
(j,d)\longmapsto P_j/d\pmod p
\]

against the actual Möbius coefficients, after subtracting the source diagonal.

### D2. One-variable diagonal contraction

Use (7.1), the existing inverse-orbit frame and the fact that the source product diagonal is absent to close the `u=u'` and `v=v'` strata.

### D3. Genuine determinant kernel

For the remaining stratum derive the exact nonzero determinant or difference controlling collisions. The expected form is a congruence such as

\[
p\mid uv-u'v'
\tag{7.2}
\]

with `uv-u'v' != 0`, together with the consecutive-primorial phase.

Only after the exact kernel is fixed may Poisson summation, dispersion, Kloosterman-fraction estimates or a double large sieve be invoked.

### Gate D

The phase passes if the one-variable strata close and the generic stratum is reduced to a single named bilinear incidence theorem with the exact saving required.

It fails if all reorderings still lose `X/log X` on the actual coefficients.

## 8. Phase E — the critical analytic theorem

The generic off-diagonal kernel must save the factor

\[
X^{1-o(1)}/\log X
\]

lost by source Cauchy in the preceding programme.

The analytic attempts are ordered:

1. exact dispersion in the two source products;
2. completion of the shorter variable;
3. Weil bounds for the resulting complete sums;
4. bilinear Kloosterman-fraction technology with the literal parameters;
5. a primorial-specific divisor/exponential-sum theorem if the generic technology mismatches.

Every attempt must be evaluated against the Fortune block budget, not merely shown to give a power saving.

### Hard verdict

- **PASS:** the generic off-diagonal kernel is bounded by the source diagonal plus a summable error.
- **PARTIAL:** all but one explicit determinant/Kloosterman theorem close.
- **FAIL:** exact finite spectra with the actual coefficients grow at the generic `X/log X` barrier and no signed all-order cancellation remains available.

## 9. Phase F — high modes after source-diagonal removal

For conductors `Q` containing at least two first-band primes:

1. retain the exact unique representative `rho_{j,Z}(Q)`;
2. exclude the already-controlled source-product diagonal;
3. apply the complement-divisor Plancherel identity before any absolute values;
4. preserve the sign between the physical and high-conductor terms;
5. prove an off-source-diagonal candidate-sampling estimate.

The previous small high-conductor centre frame remains valid input, but it is not by itself deterministic sampling.

### Gate F

Pass only if the complete nontrivial dilation spectrum, summed over all conductor orders, satisfies the same full-band Bessel estimate as the low modes.

## 10. Phase G — signed source-cell recombination

Reinsert:

- Type I;
- every Type-II cell;
- Type III cells;
- the exact Heath--Brown coefficients and signs;
- self coordinates;
- the zeroth coordinate.

No triangle inequality may be taken across source cells unless the resulting loss is explicitly inside the Fortune budget.

The output is a first-physical-band theorem of the normalized-survivor form.

## 11. Phase H — cross-band martingale transfer

Only after the first physical band is closed:

1. repeat the full-band argument for later survivor-weighted bands;
2. retain the previous-band weight inside the source coefficients;
3. prove cross-band covariance rather than applying outer Cauchy;
4. join the physical bands to the one-point tail;
5. derive `NSMT(X)` and then the Fortune variance theorem.

## 12. Execution order

The programme is to be run in this order:

1. exact Heath--Brown reconstruction and cell ledger;
2. full-band product compression and source-diagonal budget;
3. one-collision theorem and exact finite verification;
4. actual-coefficient spectral diagnostics;
5. low-mode off-source-diagonal algebra;
6. one-variable strata;
7. generic determinant kernel;
8. high-conductor off-source-diagonal completion;
9. signed cell recombination;
10. cross-band `NSMT(X)`.

The first three steps are mandatory before literature or large-compute searches.

## 13. Prohibited regressions

The programme must not:

1. return to arbitrary-weight point evaluation;
2. prove only the conductor diagonal;
3. separate physical and one-point conductors positively;
4. replace the actual prime-source coefficients with a generic logarithmic source;
5. use the complete-CRT model as deterministic sampling;
6. claim success from finite bounded ratios;
7. introduce a new theorem name without an exact formula and scale comparison.

## 14. Deliverables

### Exact source layer

- `prime_source_heath_brown_verify.py`
- `prime_source_heath_brown_results.json`
- a complete dyadic coefficient ledger

### Full-band Type-II layer

- `full_band_typeii_programme_verify.py`
- `full_band_typeii_programme_results.json`
- exact source-diagonal and one-collision checks

### Spectral layer

- `full_band_wigner_offdiagonal_verify.py`
- exact low/high mode reconstruction
- actual-coefficient operator spectra

### Analytic layer

- a theorem note for the generic off-diagonal kernel;
- a literal parameter comparison with every invoked external theorem;
- a pass/partial/fail scale ledger.

### Reinsertion layer

- first-band normalized-survivor theorem or an exact obstruction;
- updated `NSMT(X)` dependency graph;
- authoritative programme-status note.

## 15. Decisive stopping rule

Do not stop because the next lemma is identifiable.

Stop only at one of:

1. an unconditional proof of the full-band theorem;
2. a rigorous counterexample to the proposed Bessel estimate;
3. one explicit new arithmetic theorem after all exact reductions and applicable classical inputs have been exhausted;
4. an operational failure which prevents the committed verifier or source identity from being executed.

## Boundary at construction time

**AVAILABLE INPUT**

- exact inverse-orbit Type-II factorisation;
- bounded logarithmic-block centre-plus-one-variable frame;
- exact signed dilation completion;
- complete-CRT survivor Gram;
- complement-divisor Plancherel identity;
- small high-conductor complete-model centre frame;
- primorial-prefix rigidity.

**FIRST NEW EXACT TARGETS**

- full-band Type-II compression;
- source-product diagonal extraction;
- at-most-one collision prime for distinct products;
- actual Heath--Brown coefficient ledger.

**MAIN OPEN TARGET**

\[
\boxed{
\text{off-source-diagonal full-band bilinear survivor dispersion}.
}
\]

If that theorem closes with signed source-cell recombination, the first physical-band component of `NSMT(X)` is complete.
