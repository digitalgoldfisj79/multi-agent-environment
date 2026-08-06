# Execution record

**State:** `EXECUTED_AND_VALIDATED`

## L0-L2 — exact freeze and recombination

The normalized local factor and partition Möbius transform were frozen before testing. Exact rational enumeration verifies all order-three residue patterns:

\[
\begin{array}{c|c}
\text{pattern}&\kappa_{3,p}\\ \hline
(a,a,a)&-(p-2)/(p-1)^2\\
(a,a,b)&(p-2)/(p-1)^3\\
(a,b,c)&-2/(p-1)^3
\end{array}
\]

and `kappa_{2,p}(a,a)=1/(p-1)`.

## L3 — pair-tree gate

For the same-residue triple, every labelled tree uses two equal-residue edges. The exact tree budget is `3C^2/(p-1)^2`; the connected coefficient has magnitude `(p-2)/(p-1)^2`. Therefore the ratio is `(p-2)/(3C^2)` and diverges for every fixed `C`.

Outcome: `PAIR_TREE_MAJORANT_REFUTED`.

## L4 — candidate-universe witness

The exact finite witness

\[
X=18,\quad H=324,\quad p=37,\quad (m_1,m_2,m_3)=(89,163,311)
\]

satisfies all frozen restrictions:

- `p>2X`;
- all offsets are prime;
- all offsets exceed `2X`, hence exceed every stratum upper endpoint `U_b<=2X`;
- all offsets are at most `H`;
- all three offsets are congruent to `15 mod 37`.

Here

\[
|\kappa_{3,37}|=35/1296,
\qquad
3\kappa_{2,37}^2=1/432=3/1296.
\]

## L5 — absolute hyperedge ledger

The same-prime `r`-body cluster contributes at local size `O_r(1/p)`. Applying the inherited Brun--Titchmarsh row count to the remaining `r-1` offsets yields

\[
T_r(m)\ll_r X^{r-1}/(\log X)^r.
\]

A radius `X/(log X)^(1+delta)` would require log exponent `(1+delta)(r-1)`. The absolute ledger supplies only `r`; it is sufficient only when

\[
\delta\le 1/(r-1).
\]

No fixed positive `delta` survives to logarithmic order.

Outcome: `ABSOLUTE_HYPEREDGE_RADIUS_INSUFFICIENT`.

## L6-L7 — surviving theorem

No exact signed recombination identity is present in the inherited programme. The smallest honest successor is therefore a signed higher-body collision-cluster theorem preserving partition signs and primewise Euler-product structure before absolute values.

No transfer to `INT-SOCG` is claimed.

## L8 — validation

Workflow run `31081057533` at head `692278db18b389490104ebc8ddd2889efed17316` passed the exact regression, targeted Lean build, full-package Lean build and trust scan under Lean `4.32.0`.
