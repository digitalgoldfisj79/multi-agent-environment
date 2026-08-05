# O6 — conditional Poisson and singular-series benchmark

This gate constructs a benchmark, not an unconditional proof.

## Conditional first-order scale

For the pair of forms

\[
m,\qquad P_j+m,
\]

the Hardy–Littlewood singular series contains the primorial factor

\[
\prod_{p\mid P_j}(1-1/p)^{-1}\asymp\log X.
\]

Combined with

\[
\int_2^H\frac{dt}{\log t\log(P_j+t)},
\]

this predicts

\[
\mu_j=\mathbb E[Z_j]\asymp X
\]

uniformly over a registered block. The exact main term and constants must be inherited from the mainline prime-pair detector rather than rederived heuristically.

## RUHL hypothesis template

Define a row-uniform growing-tuple Hardy–Littlewood hypothesis `RUHL(K,E)` asserting that for every registered row `j`, every admissible distinct candidate tuple `M={m_1,...,m_k}` with `k<=K`,

\[
\sum_{m\text{-configuration}}
\prod_{a=1}^{k}\Lambda(P_j+m_a)
\]

has the predicted singular-series main term with aggregate error at most `E_k(X)` after summing over all tuples used by the detector.

The execution must replace this schematic statement by an exact formula. The crucial object is the aggregate tuple error, not an error for one fixed tuple multiplied naively by `M_X^k`.

## Required implication

Prove a conditional theorem of one of the following forms:

1. `RUHL(K(X),E) => INT-CCB`, where `K(X)` and the connected tail are explicit;
2. `RUHL(all orders with summable aggregate error) => INT-AOD`;
3. a conditional Poisson or compound-Poisson Laplace transform
   \[
   G_X(e^{-\tau_X})
   =\exp(-\mu_X(1-e^{-\tau_X})+R_X)
   \]
   with
   \[
   \mu_X(1-e^{-\tau_X})-R_X>(1+\varepsilon)\log N.
   \]

## Literature interfaces

- Pintz supplies growing-set control for averages of singular-series constants when the shift range is sufficiently large relative to tuple size.
- Kuperberg gives growing-set singular-series estimates and conditional prime-tail applications under a uniform Hardy–Littlewood conjecture.
- Jha gives a recent conditional Poisson-tail framework using extremal sieve estimates and concentration inequalities.

None supplies `RUHL` on the selected primorial rows. The programme must state that missing input verbatim in any conditional closeout.

## Stop rule

If the weakest sufficient `RUHL` already requires rowwise prime-tuple asymptotics of arity and accuracy essentially equivalent to `INT-AOD`, record the conditional benchmark but do not promote it as a reduction.