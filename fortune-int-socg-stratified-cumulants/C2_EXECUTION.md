# C2 execution — first cumulant

**Status:** `MEAN_LOWER_BOUND_IS_PRIMARY_OBSTRUCTION`

## Correct weighted object

For the common candidate universe `M_b`, define

\[
T_b=
\frac1{n_b}
\sum_{j\in B_b}
\sum_{m\in\mathcal M_b}
1_{\mathbb P}(m)\log m\,\Lambda(P_j+m).
\]

Using a symmetric `Lambda(m)Lambda(P_j+m)` source is inefficient here: proper prime powers on the source side consume the target scale under a trivial subtraction. Restricting the source offset to actual primes removes that problem.

## Output-prime-power cap

Assume the registered large-`X` range in which `H<2 sqrt(P_j)`. For each exponent `a>=2`, the interval `(P_j,P_j+H]` contains at most one `a`-th power. If `P_j+m=q^a`, then

\[
\Lambda(P_j+m)=\log q
\le\frac{\log(P_j+H)}a.
\]

Consequently the total contribution of proper output prime powers in one row is at most

\[
E_j^{pp}
\le
\log H\,\log(P_j+H)
\sum_{a=2}^{\lfloor\log(P_j+H)/\log2\rfloor}\frac1a
=
O\!\left(X(\log X)^2\right).
\]

This is negligible relative to the required weighted main scale `X^2 log X`.

For actual prime pairs, each summand is at most

\[
\log H\,\log(P_j+H)=O(X\log X).
\]

Therefore the following theorem is sufficient.

## INT-SCME — selected-centre mean estimate

There is a fixed `kappa>0` such that every sufficiently large registered stratum satisfies

\[
\boxed{
T_b\ge \kappa X^2\log X.
}
\]

Then

\[
c_{1,b}
\ge
\frac{T_b-O(X(\log X)^2)}
     {\log H\,\max_{j\in B_b}\log(P_j+H)}
\ge c_0X
\]

for a fixed `c_0>0`.

## Literature and method ruling

Generic short-interval prime theorems concern intervals of power length in the centre and do not reach `H asymp (log P_j)^2`. Average singular-series theorems control local constants over offset sets but do not estimate prime incidence on the sparse deterministic primorial-centre path. Standard dense-shift or almost-all-centre theorems do not transfer to the selected rows.

No established theorem located in the registered literature audit proves `INT-SCME`, and the direct asymptotic-sieve/source routes still meet the actual-prime parity and post-`H` sparse-hyperbola barrier.

Because `c_{1,b}>=c_0X` is a mandatory hypothesis of `INT-SOCG`, no higher-cumulant theorem can complete the programme without `INT-SCME` or an equivalent selected-centre mean lower bound. C2 is therefore the primary frontier.
