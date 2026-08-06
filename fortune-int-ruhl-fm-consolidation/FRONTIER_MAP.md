# Review-corrected frontier map

## Proved implication

The finite Bonferroni argument proves

\[
\mathrm{RUHL\!-\!FM}
\Longrightarrow
\mathrm{INT\!-\!AOD}
\Longrightarrow
\text{eventual Fortune}.
\]

The first arrow is a conditional theorem. The second arrow is inherited and formally checked.

## Relationship to the INT-SOCG programme

`RUHL-FM` and `INT-SOCG` are alternative sufficient lanes, not successive proved reductions.

### RUHL-FM lane

Assume factorial moments through order

\[
K_b=\Theta(\log X)
\]

with one-row-scale aggregate error, and close the detector by a finite even Bonferroni polynomial.

This lane requires no infinite cumulant expansion or zero-free region, but assumes high-arity prime-tuple information directly.

### INT-SOCG lane

Prove a positive first cumulant and all-orders connected bounds

\[
|c_{k,b}|\le c_{1,b}k!D_b^{k-1}
\]

with `tau_bD_b=o(1)`, and close the detector through an absolutely convergent Laplace/cumulant expansion.

This lane decomposes into at least three coequal arithmetic inputs:

- `INT-SCME`: positive selected-centre weighted prime-pair mean;
- `INT-LCSK`: all-orders connected local-factor control;
- `INT-PWOC`: weighted squarefree-composite primorial-walk control.

## What RUHL-FM does not prove

`RUHL-FM` bypasses the three inputs above by assuming their combined high-order consequence. It does not establish any of them separately.

In particular:

- it does not turn the selected-centre mean theorem into a solved problem;
- it does not prove the all-orders tree or hypergraph estimate;
- it does not extend the prime-modulus walk theorem to composite moduli;
- it does not show exact phase control is the unique route to Fortune.

## Strength audit

The exact signed RUHL-FM condition is close to an upper bound on the truncated detector discrepancy itself. It is logically sufficient but should not be advertised as a deep reduction.

The absolute tuple-decomposed condition is more recognisably arithmetic. Its hard component is the selected-centre prime-tuple residual through order `Theta(log X)` at aggregate accuracy comparable with one row in one stratum.

That requirement is substantially beyond ordinary fixed-tuple Hardy--Littlewood asymptotics and beyond existing dense-shift singular-series averages. It may be of comparable practical difficulty to the occupancy theorem it implies.

## Unconditional progress ruling

The consolidation improves the precision and weakens the stated sufficient error budget. It does not provide a new unconditional estimate for primes on the selected primorial path.

Therefore the honest current ruling is:

\[
\boxed{\text{conditional architecture sharpened; unconditional distance to Fortune unchanged}.}
\]

## Next high-value target

Do not launch another detector-equivalent phase or signed-error project.

The next worthwhile mathematical target is a source-to-factorial-moment proposition that proves a nontrivial portion of (A5) without assuming the detector conclusion. The cleanest candidate is one of:

1. a fixed small-arity selected-centre prime-tuple theorem with an error that remains summable under the Bonferroni weights;
2. a composite-modulus extension of the primorial-walk energy strong enough to control the prime-tuple residual after a registered source decomposition;
3. an all-orders connected local-factor theorem that feeds the alternative `INT-SOCG` lane.

Any next build must state which of these it attacks and must include a proved implication to either (A5) or `INT-SOCG` before computation begins.
