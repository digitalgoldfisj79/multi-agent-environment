# CRT de-tensorisation phase report

## Objective

Test whether the apparent conductor

\[
m=q_1q_2q_3q_4\asymp X^8
\]

in the Gauss-character bridge can be split into four useful shell-prime averages, with character orthogonality reducing the problem to divisors of consecutive-prime interval products.

## Outcome

The proposed shell-divisor statistic is exceptionally sparse and admits an elementary short/medium interval bound. However, it belongs only to the character-diagonal and divisor-correction sectors. The unequal-character sector, which carries the signed reciprocal fluctuation, collapses exactly back to the original additive kernel.

Therefore:

\[
\boxed{\text{CRT factorisation is exact but does not de-tensorise the load-bearing sector.}}
\]

PGD2 and Fortune's conjecture remain unproved.

## Exact results

### Composite character diagonal

For squarefree `m`,

\[
\mathfrak D_m=
\sum_{i,j<N}
\prod_{q\mid m}
\frac{q\mathbf1_{P_i\equiv P_j\pmod q}-1}{q-1}.
\]

This term is independent of the reciprocal sign pattern. With no off-diagonal collisions and four prime factors, it equals

\[
N+\frac{N(N-1)}{\varphi(m)}=N+o(1).
\]

### Character-ratio collapse

Grouping unequal character pairs by their ratio and summing the base character gives one zero-aware Gauss expansion in `P_i-P_j`. Summing the ratio character gives the original additive phase. Applying this locally at four CRT factors reconstructs

\[
e_m(A(P_i-P_j))
\]

exactly.

### Shell-divisor sparsity

For interval length `ell`,

\[
\nu_X(i,j)<\frac{\ell\log(2X)}{2\log X}.
\]

Hence four shell divisors are impossible for `ell<=7` once `X>128`, and the fourth moment over all intervals of length at most `C log X` is `O_C(N log^5 X)`.

Exact residue-walk panels through `X=1500` found `max nu=2` and

\[
\sum_{i<j}\binom{\nu_X(i,j)}4=0
\]

in every panel.

## Why the statistic is non-load-bearing

The full character expansion is

\[
|F_m(A)|^2=\mathfrak D_m+\mathfrak O_m(A).
\]

In a validated four-prime toy system with `N=8`,

\[
\mathfrak D_m=8.1375,
\qquad
\operatorname{Re}\mathfrak O_m(A)=-7.22115\ldots,
\qquad
|F_m(A)|^2=0.91635\ldots.
\]

The diagonal can be almost entirely cancelled by the off-diagonal sector. A strong shell-divisor estimate therefore leaves the main fluctuation untouched.

## Route decisions

- CRT/Gauss factorisation: exact and retained as anatomy.
- Short/medium shell-divisor theorem: proved, but non-load-bearing.
- Long-interval SPDM4/ICM4 campaign: not launched, because even an optimal theorem would control only the diagonal/divisor sector.
- CRT de-tensorisation as a PGD2 proof route: stopped.

## Revised frontier

Further progress requires a signed, cross-character, cross-conductor estimate that keeps the Gauss phases and consecutive-prime factors coupled before any norm separation. In the current basis that object is equivalent to the original reciprocal-frame theorem.
