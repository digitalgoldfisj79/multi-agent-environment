# Integer Fortune mainline: exact frontier

**Programme:** `FORTUNE_MAINLINE_CLOSEOUT_V1`  
**Status:** exact target isolated; theorem remains open

## 1. Final target

The mainline target is the single centred signed covariance theorem `INT-ISC`.

For the corrected prime-pair detector

\[
Z_j(H)=\sum_{2\le m\le H}1_{\mathbb P}(m)1_{\mathbb P}(P_j+m)
\]

and the explicit deterministic Hardy–Littlewood baseline

\[
\lambda_j^*(H)=\mathfrak S(P_j)
\int_{\ell_j}^{H}\frac{dt}{\log t\log(P_j+t)},
\]

define

\[
C_j(H;d)=\sum_{m+d\le H}
1_{\mathbb P}(m)1_{\mathbb P}(m+d)
1_{\mathbb P}(P_j+m)1_{\mathbb P}(P_j+m+d)
\]

and

\[
\mathcal R_X=\sum_{j<N}\left[
Z_j+2\sum_{d<H}C_j(H;d)
-2\lambda_j^*Z_j+(\lambda_j^*)^2-\lambda_j^*
\right].
\]

### INT-ISC

For fixed `0 < eta < 1`, `H=eta X^2`, and every sufficiently large dyadic prime block, prove

\[
\boxed{\mathcal R_X\ll NXL(X),\qquad L(X)=o(\log X).}
\]

Only an upper bound is required. Absolute-value control would be stronger than necessary.

## 2. Exact implication

The pointwise identity

\[
Z_j^2=Z_j+2\sum_{d<H}C_j(H;d)
\]

gives

\[
\sum_{j<N}|Z_j-\lambda_j^*|^2
=\sum_{j<N}\lambda_j^*+\mathcal R_X.
\]

Since `lambda_j^* asymp X`, INT-ISC yields

\[
\sum_j|Z_j-\lambda_j^*|^2\ll NXL(X).
\]

One failed centre has `Z_j=0` and costs `gg X^2`; because `N asymp X/log X`, the number of failures is `O(L(X)/log X)=o(1)`. Hence every sufficiently large centre succeeds.

The finite algebraic spine is Lean checked in `FortuneFormal/Integer/BlockCriterion.lean`.

## 3. Why this target is preferable

INT-ISC is smaller and more exact than the earlier formulations.

- It combines Paper III conditions C1 and C2 into one signed statement.
- It preserves the centring term and therefore cannot accidentally replace the prime-pair mean by the old short-interval mean.
- It does not require a reciprocal-frame representation.
- It exposes the exact four-prime arithmetic content.
- It records the loss budget `o(log X)` explicitly.

## 4. Structural lane result

The structural lane is complete.

1. Candidate collapse was reconstructed.
2. The exact detector and baseline scale were fixed.
3. The second moment was expanded without dropping any prime factor.
4. The unique signed residual was isolated.
5. The one-failure implication was kernel checked.

No further exact algebraic rewrite reduces the arithmetic complexity. Every expansion of INT-ISC contains either the same aggregated four-prime correlation or an equivalent two-von-Mangoldt sparse-centre covariance.

## 5. Analytic lane result

### 5.1 Direct four-prime route

Expanding INT-ISC requires cancellation in an aggregate of the four forms

\[
m,\quad m+d,\quad P_j+m,\quad P_j+m+d
\]

with `m,d <= H asymp X^2`, averaged over only `N asymp X/log X` exponentially separated centres. This is a Hardy–Littlewood-strength correlation at a prescribed lacunary family, not an ordinary dense average in the centre.

### 5.2 Double-von-Mangoldt route

Paper II gives the exact identity

\[
T_j(H)=\int_0^1A_H(\theta)B_X(\theta)e(-P_j\theta)d\theta.
\]

The resulting block variance has the single-walk kernel

\[
F_X(\beta-\alpha)=\sum_{j<N}e(P_j(\beta-\alpha)).
\]

This identity is exact, but available norm inequalities lose the signed baseline cancellation. Cauchy–Schwarz or a raw operator norm bounds the uncentred source and is too large at the one-failure scale.

### 5.3 Recentered shifted-detector route

Candidate collapse means the shifted detector already encodes offset primality after proper-prime-power removal. A viable theorem would have to rebuild the principal Buchstab/sieve component at the square-root boundary and then prove a centred sparse-orbit estimate. No such derivation is present in Papers I–IV.

### 5.4 Existing machinery audit

- Paper I's collision and Smith-form theorems do not act on the corrected detector.
- Paper III's Lebesgue tail theorem has no arithmetic sampling theorem for the reciprocal atoms.
- Paper IV averages over permutations and does not control the increasing primorial order.
- Dense short-interval mean-square or exceptional-set results average over an ambient interval of exponentially many centres, whereas the primorial block contains only polynomially many prescribed centres.
- Sieve upper bounds do not create the signed four-prime asymptotic needed here; the parity obstruction is present at the square threshold.

## 6. Falsification lane result

The supplied framework is insufficient to prove INT-ISC. Three exact countermodels/no-go mechanisms establish this.

### 6.1 First-moment preservation with one failure

For `N>1` and a constant baseline `lambda>0`, set

\[
Z_0=0,\qquad
Z_j=\lambda+\frac{\lambda}{N-1}\quad(j>0).
\]

Then `sum Z_j=N lambda` exactly, but one centre fails and

\[
\sum_j(Z_j-\lambda)^2=\lambda^2\left(1+\frac1{N-1}\right).
\]

Thus a correct block first moment, even exactly, cannot replace INT-ISC.

### 6.2 Dense-average invisibility

Let the ambient centre range have length `Y` and let the selected primorial windows have total volume at most `NH`. Altering every value in one selected window changes a normalized dense average by at most `O(H/Y)`. Here `Y` is exponential in `X` while `N,H` are polynomial in `X`, so even altering every selected window is invisible to a dense average: `NH/Y -> 0`.

Therefore no theorem stated only as an averaged exceptional-set bound over all centres can imply success at the prescribed primorial centres without an additional distribution theorem for that sequence.

### 6.3 Lebesgue-small sets can contain all reciprocal atoms

A set of arbitrarily small positive Lebesgue measure can contain any finite set of sampling atoms. Paper III's reciprocal support has only polynomially many atoms. Consequently its Lebesgue tail estimate cannot control the arithmetic sampling measure without a discrepancy, large-sieve or equidistribution theorem specific to those atoms.

The executable finite regressions are in `scripts/finite_obstruction_checks.py`.

## 7. Research stopping theorem

The completed analytic audit yields the following rigorous programme-level obstruction.

> **Mainline obstruction.** The exact results proved in Papers I–IV, together with generic dense-centre mean-square information, first-moment calibration, Lebesgue tail bounds and random-order averaging, do not imply INT-ISC. Any proof must introduce a new theorem controlling a centred prime-pair or four-prime correlation on the actual increasing primorial sequence.

This is an insufficiency theorem about the current programme, not a disproof of INT-ISC or Fortune.

## 8. What a successful new ingredient must look like

A future theorem must supply at least one of:

1. a sparse-centre Hardy–Littlewood covariance theorem directly proving INT-ISC;
2. a centred dispersion/large-sieve inequality exploiting a special arithmetic orthogonality of the primorial walk, with total loss `o(log X)`;
3. a deterministic source-to-orbit identity with a positive-semidefinite remainder whose diagonal is the baseline sum and whose off-diagonal admits the required saving;
4. a new sieve input that breaks the four-form parity barrier in this aggregate setting.

Anything weaker than control at the exact selected centres, or anything that discards the sign of the baseline subtraction, does not close the programme.

## 9. Final integer status

- Candidate collapse: proved.
- Correct detector and exact covariance identity: proved.
- One-failure implication: Lean checked.
- Source identities and structural kernels: proved.
- INT-ISC: open.
- Fortune: open.

The integer programme is therefore complete as a reduction and obstruction analysis. Its next step is not another reformulation; it is a genuinely new sparse-centre covariance theorem.
