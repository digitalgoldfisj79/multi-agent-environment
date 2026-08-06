# INT-PSLT Buchstab–factor-band closeout

**Programme:** `FORTUNE_INT_PSLT_BUCHSTAB_FACTOR_BAND_V0_1`  
**Date:** 4 August 2026  
**Branch:** `gpt56/fortune-int-pslt-buchstab-factor-band-v01-20260804`  
**Outcome:** `REDUCED_TO_CRITICAL_FACTOR_INCIDENCE`

## Final ruling

The programme did not prove `INT-PSLT` or Fortune. It achieved three structural reductions and one decisive method obstruction:

1. the failed-centre source threshold was compressed from order `X(log X)^2` to an explicit variable threshold of order `X log X`;
2. the natural primorial recurrence was proved not to propagate admissible defects inside the registered window;
3. the exact least-factor/Buchstab partition was derived;
4. every admissible factor begins beyond `sqrt(H)`, so no classical positive lower sieve can enter the factor range even at the optimistic level `D=H`.

The exact remaining theorem is `INT-PFLI`, a signed aggregate post-level factor-incidence theorem.

## Compressed threshold

For

\[
U_j=P_j+H,
\qquad
K_j=\left\lfloor\frac{\log U_j}{\log2}\right\rfloor,
\]

put

\[
C_j^{\mathrm{pp}}=
\log U_j\sum_{k=2}^{K_j}\frac1k,
\qquad
B_j=2C_j^{\mathrm{pp}}.
\]

At a failed centre,

\[
\Psi_j(H)\le C_j^{\mathrm{pp}}=B_j/2.
\]

Hence a failed row contributes at least `B_j^2/4` to the one-sided source lower tail. Uniformly, `B_j asymp X log X`.

## Exact least-factor identity

For prime candidate offsets

\[
\mathcal A_j=\{m:\ell_j<m\le H,\ m\text{ prime}\},
\]

let `M_j(r)` count those with `P^-(P_j+m)=r`. Then

\[
|\mathcal A_j|
=Z_j(H)+
\sum_{\ell_j<r\le\sqrt{P_j+H}}M_j(r).
\]

Since `H=eta X^2`, `eta<1`, and `ell_j>=X`, every factor satisfies

\[
r>\ell_j>\sqrt H.
\]

## Sieve obstruction

A lower linear sieve with level `D` and cutoff `z` uses

\[
s=\frac{\log D}{\log z}
\]

and requires `s>2` for a positive lower coefficient. Even granting `D=H`, the first permitted cutoff `z>ell_j>sqrt H` gives `s<2`.

Therefore no classical Brun, Selberg, beta-sieve, Bombieri–Vinogradov, or Elliott–Halberstam-level lower-bound implementation confined to the length-`H` variable can peel off a nonempty post-primorial factor band.

## No propagation reduction

The centre recurrence sends offsets by

\[
m\mapsto\ell_{j+1}m.
\]

Every admissible `m>ell_j>=X` is sent beyond `X^2>H`. A failed row therefore does not create a neighbouring registered defect through the natural map.

## Remaining theorem — INT-PFLI

Let

\[
C_j=\sum_RI_j(R)
\]

be the complete dyadic least-factor incidence count and define

\[
\gamma_j=\left\lceil B_j/\log P_j\right\rceil\asymp\log X.
\]

The remaining theorem is

\[
\boxed{
\sum_{j<N}
(C_j-|\mathcal A_j|+\gamma_j)_+^2
=o\!\left((\min_j\gamma_j)^2\right).
}
\]

At a failed row `C_j=|A_j|`, so the row contributes `gamma_j^2`. Thus `INT-PFLI` implies the compressed source lower-tail theorem and eventual Fortune.

`INT-PFLI` is open.

## Why the programme cannot reduce to one dyadic band

There are `Theta(X)` dyadic factor bands but only `Theta(log X)` uncovered prime outputs are required after threshold compression. The average margin per band is `O(log X/X)=o(1)`. An unsigned `O(1)` error in each band accumulates to `Theta(X)`, already larger than the entire one-row margin.

The missing information is signed cancellation across all post-level bands, not a uniform estimate on one isolated factor interval.

## Validation

- static and six-regression sentinel `6a724dbca00abefd4b29284e`: completed with failure count zero;
- targeted formal build `6a724ddda00abefd4b292854`: 8,657 jobs, completed with failure count zero;
- full clean-room closeout `6a724e7a6b79c09949c22885`: Lean 4.32.0, 8,682 jobs, inherited seven-paper and `INT-PSLT` audits, all factor-band regressions, completed with failure count zero;
- terminal sentinel: `FORTUNE_INT_PSLT_FACTOR_BAND_FULL_CLEANROOM_PASS`.

## Closed methods

- natural defect propagation;
- classical positive lower sieves;
- band-by-band absolute estimates;
- generic power-length short-interval theorems;
- dense-centre exceptional-set estimates without a primorial restriction theorem;
- source-orbit/frame geometry already closed in PR #49.

## Explicitly not claimed

- `INT-PFLI`;
- compressed `INT-PSLT`;
- original `INT-PSLT`;
- Fortune's conjecture;
- any function-field-to-integer transfer;
- any theorem limiting perfect-power clustering beyond the explicit harmonic cap.
