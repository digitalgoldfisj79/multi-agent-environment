# P1–P5 execution — exact kernel and fixed-order theorem

**Status:** `FIXED_ORDER_COMPOSITE_EXTENSION_PROVED`

## P1 exact weighted kernel

For

\[
S_q(c)=\sum_j a_j e(cP_j/q),
\]

additive-character orthogonality gives

\[
\sum_{c\bmod q}|S_q(c)|^2
=q\sum_{j,k:\,P_j\equiv P_k\pmod q}a_j\overline{a_k}.
\]

Multiplying by `beta(q)` and summing over the finite modulus family gives exactly

\[
\mathcal E_\beta(a)=\sum_{j,k}a_j\overline{a_k}K_\beta(j,k),
\qquad
K_\beta(j,k)=\sum_{q\mid P_j-P_k}\beta(q)q.
\]

The finite direct-character regressions and kernel computation agree on every registered panel.

## P3 collision support

For `j<k`, put `d=k-j` and

\[
\Delta_{j,k}=P_k/P_j-1
=\prod_{t=j+1}^{k}\ell_t-1.
\]

Since `0<Delta_{j,k}<(2X)^d`, the integer `Delta_{j,k}` has at most `d-1` distinct prime divisors exceeding `2X`. Every order-`r` supported collision modulus is the product of an `r`-subset of those divisors. Therefore

\[
\#\{q:\omega(q)=r,\ q\mid\Delta_{j,k}\}
\le {d-1\choose r}.
\tag{1}
\]

## PWOC-SF1 theorem

Assume the frozen `W1(r,U_r)` contract

\[
0\le \beta(q)q\le U_r.
\]

Then (1) gives the pair bound

\[
K_\beta(j,k)\le U_r{ |j-k|-1\choose r}.
\tag{2}
\]

For a fixed row `j`, summing separately to the left and right and applying the hockey-stick identity yields

\[
\sum_{k\ne j}K_\beta(j,k)
\le U_r\left[{j\choose r+1}+{n-1-j\choose r+1}\right]
\le U_r{n-1\choose r+1}.
\tag{3}
\]

The last inequality is sharp as a coefficient-uniform endpoint bound. Consequently

\[
\boxed{
R_\beta\le U_r{n-1\choose r+1}
}
\tag{SF1}
\]

and the kernel energy satisfies

\[
\boxed{
\mathcal E_\beta(a)
\le\left(D_\beta+U_r{n-1\choose r+1}\right)
\sum_j|a_j|^2.
}
\tag{4}
\]

This is a genuine fixed-order squarefree-composite extension of the prime-modulus collision argument. It is coefficient-uniform and keeps the subset growth explicit.

## W0 falsifier

Suppose one supported modulus `q_0` divides one nonzero gap `P_j-P_k`. Choose

\[
\beta(q_0)=1/q_0,
\qquad \beta(q)=0\ (q\ne q_0).
\]

Then `D_beta=1` and `R_beta>=1`. Thus no theorem uniform over unrestricted nonnegative weights can prove `R_beta=o(D_beta)`. The W0 absolute-value lane is closed.

## Multiplicative majorant

If

\[
\beta(q)q\le\prod_{p\mid q}u_p,
\]

then for one pair

\[
K_\beta(j,k)
\le
\prod_{\substack{p\mid\Delta_{j,k}\\p>2X}}(1+u_p)-1.
\]

This does not give a subcritical row bound without an additional uniform constraint on the `u_p`. No such source-compatible constraint is presently committed.

## P5 decision

- `W0`: refuted as a route to uniform subcriticality.
- `W1`: PWOC-SF1 proved with exact radius `U_r * choose(n-1,r+1)`.
- `W2/W3`: unavailable.

No cancellation hypothesis is used in SF1.