# Direct von Mangoldt route for function-field d=1

**Date:** 24 July 2026  
**Status:** exact reformulation and exact finite rank audits proved; current rank/Vaughan technology fails by an exponential factor.  
**Scope:** function-field Fortune sibling only.

## 1. The exact signed detector

Let

\[
\mathcal I_p=\{T^p+aT^3+bT^2+cT+d:a,b,c,d\in\mathbf F_p\}.
\]

For a monic polynomial `f` of degree `p`, put

\[
f^*(z)=z^p f(1/z).
\]

Writing `N=p-4`, membership in the full four-dimensional sparse interval is exactly

\[
f\in\mathcal I_p\iff f^*(z)\equiv1\pmod {z^{N+1}}.
\]

Define

\[
A_p=\sum_{f\in\mathcal I_p}\Lambda(f).
\]

Because `p` is prime, a proper prime power of degree `p` is a `p`-th power of a monic linear polynomial. In characteristic `p`,

\[
(T-\alpha)^p=T^p-\alpha,
\]

so all `p` such polynomials lie in `\mathcal I_p` and each has function-field von Mangoldt weight one. Every irreducible degree-`p` member has weight `p`. Thus, if `I_4` is the number of irreducible members of `\mathcal I_p`,

\[
\boxed{A_p=pI_4+p.}
\]

The `(a,b)=(0,0)` irreducibles are exactly the `p-1` excluded Artin--Schreier polynomials. If `I_{\rm target}` denotes the number with `(a,b)\ne(0,0)`, then

\[
\boxed{A_p=pI_{\rm target}+p^2.}
\]

Consequently

\[
\boxed{FF\text{-}Fortune(p,1)\iff A_p>p^2.}
\]

This is an exact signed prime detector with no prime-power error term.

## 2. Truncated logarithmic characters

Put

\[
R_N=\mathbf F_p[z]/(z^{N+1}),\qquad I_N=zR_N.
\]

Since `N=p-4<p`, every denominator `1,2,...,N` is invertible in `\mathbf F_p`. The finite series

\[
\log(1+u)=\sum_{j=1}^{N}(-1)^{j+1}\frac{u^j}{j},
\qquad
\exp(v)=\sum_{j=0}^{N}\frac{v^j}{j!}
\]

are mutually inverse group isomorphisms

\[
1+I_N\longleftrightarrow I_N.
\]

For `\lambda=(\lambda_1,...,\lambda_N)\in\mathbf F_p^N`, define

\[
\chi_\lambda(f)
=e_p\!\left(\sum_{j=1}^{N}\lambda_j[ z^j]\log f^*\right).
\]

Then `\chi_\lambda(fg)=\chi_\lambda(f)\chi_\lambda(g)` whenever `f,g` are monic, and additive orthogonality gives

\[
\boxed{
A_p=p^{-N}\sum_{\lambda\in\mathbf F_p^N}
\Psi_p(\lambda),
\qquad
\Psi_p(\lambda)=\sum_{\deg f=p}\Lambda(f)\chi_\lambda(f).
}
\]

The zero character contributes exactly `p^p`, hence the expected main term `p^4` after division by `p^N`.

## 3. Conductor and the low-conductor range

For nonzero `\lambda`, let

\[
m(\lambda)=\max\{j:\lambda_j\ne0\}.
\]

The character is primitive at depth `m`. For every degree `d\ge m`, the first `m` reverse coefficients of a monic degree-`d` polynomial are uniformly distributed, so the complete coefficient sum of `\chi_\lambda` vanishes. Equivalently its local Dirichlet L-function is a polynomial of degree at most `m-1`.

Function-field RH therefore gives the safe individual estimate

\[
|\Psi_p(\lambda)|\le (m-1)p^{p/2}.
\]

There are `(p-1)p^{m-1}` characters of exact conductor `m`. Hence the total normalized contribution from conductors at most `M` is

\[
\ll M p^{M-p/2+4}.
\]

In particular, conductors below `p/2-O(1)` are harmless. The obstruction is confined to conductors comparable with `p`.

The identities `A_5=625=5\cdot124+5` and `A_7=2989=7\cdot426+7`, the character average, and the coefficient-sum vanishing were independently checked in Hugging Face job `6a63a5e6db23d7a7ec1cadeb`.

## 4. Raw-coefficient Fourier and the Hankel phase

The logarithmic characters are multiplicative and separate on a factorisation. A different, triangularly equivalent Fourier basis is obtained by detecting directly the first `N` reverse coefficients. In that basis a factorisation

\[
f=gh,\qquad \deg g=r,\quad\deg h=s,\quad r+s=p,
\]

produces the bilinear phase

\[
\sum_{i=1}^{r}\sum_{j=1}^{s}\lambda_{i+j}x_i y_j,
\]

where `x_i,y_j` are reverse coefficients and `\lambda_k=0` for `k>N`. The phase matrix is the truncated Hankel matrix

\[
\boxed{B_\lambda(i,j)=\lambda_{i+j}.}
\]

The logarithmic and raw-coefficient bases must not be conflated: the former gives a family of L-functions, while the latter exposes the Type I/II partition-rank geometry.

## 5. Exact rank audits

The complete distributions were enumerated for all nonzero frequencies and all splits at `p=7` and `p=11` in job `6a63a3c9db23d7a7ec1cadbf`.

For the balanced split `5+6` at `p=11`, the rank distribution is

\[
0:10,\quad1:110,\quad2:1210,\quad3:13310,
\quad4:146410,\quad5:19326120.
\]

Thus almost every frequency has full possible rank five, while exact low-rank conductor strata remain.

At `p=17`, split `8+9`, two million random conductor-13 frequencies gave

\[
\operatorname{rank}6:27,\qquad
\operatorname{rank}7:6990,\qquad
\operatorname{rank}8:1992983.
\]

However the single-spike frequency `\lambda_m\ne0`, all other entries zero, has ranks

\[
0,1,2,3,4,5,6,7,8,8,7,6,5
\]

for `m=1,...,13`. Therefore maximal conductor does not imply large rank; the four absent terminal anti-diagonals create rank-five spike frequencies.

The exhaustive and sampled results are reproduced by `hankel_rank_audit.cpp`.

## 6. Quantitative obstruction to present rank technology

For a complete bilinear phase of rank `\rho`, the unweighted sum over `\mathbf F_p^r\times\mathbf F_p^s` has magnitude `p^{p-\rho}`. With arbitrary Vaughan weights, Cauchy--Schwarz gives at best the square-root rank saving `p^{p-\rho/2}`.

After averaging the `p^N` Fourier frequencies and dividing by `p^N`, a generic balanced rank `\rho\sim p/2` therefore yields, even under the optimistic complete-sum estimate,

\[
p^{p-\rho}\asymp p^{p/2},
\]

and under the arbitrary-weight estimate

\[
p^{p-\rho/2}\asymp p^{3p/4}.
\]

Both are exponentially larger than the required polynomial error `O(p^4)`, let alone the positivity threshold `p^2`. Rank stratification does not repair this: the generic full-rank stratum alone already has the fatal scale, while low-rank spike strata make uniform estimates worse.

### Ruling

- **PROVED:** exact von Mangoldt criterion; truncated-log character formula; conductor cutoff; raw-coefficient Hankel phase.
- **VERIFIED EXACTLY:** all finite identities at `p=5,7`; complete rank distributions at `p=7,11`; two-million-frequency rank sample at `p=17`.
- **CLOSED WITH CURRENT INPUTS:** a proof using only characterwise RH plus triangle inequality, or only Vaughan decomposition plus individual Hankel-rank bounds.
- **OPEN:** cancellation across the high-conductor character family, or a higher-order identity that couples frequencies before absolute values are taken.

This route remains a useful exact reformulation, but it does not bypass the growing-dimension cancellation wall with present rank technology.
