# An Exact Conditional Criterion for Fortune's Conjecture and Barriers to Standard Prime-Detection Mechanisms

## Abstract

Let `P_n=p_n#` and let `F_n` be the least integer `m>1` for which `P_n+m` is prime. Below the square threshold, a composite candidate offset cannot be least: if `m<p_{n+1}^2` and `P_n+m` is prime, then `m` is prime. Thus eventual Fortune reduces to detecting a prime pair `(m,P_j+m)` in every sufficiently large primorial row within a Cramér-scale window.

This paper isolates an exact finite sufficient condition for that detection. A deterministic stratification and an even-Bonferroni expansion convert rowwise occupancy into factorial moments through order `Theta(log X)`. If their signed error against a registered Hardy--Littlewood model lies below an explicit one-row margin, then the adaptive detector is less than one and every row succeeds. For `epsilon=0.10` and model-mean ratio `U_b/L_b<=1.10`, the truncation choice `K_b=ceil(5 log(n_bB))_even` is sufficient.

The criterion is unconditional as a finite implication but its arithmetic hypothesis is open. We then give exact barriers explaining why several natural implementations do not currently provide that hypothesis. The termwise absolute envelope already demands additive `O(1)` accuracy for a selected-centre mean of order `X`. Pairwise local dependency graphs fail at third order because one same-residue triple contributes order `1/p`, while every pair-tree budget is order `1/p^2`. Absolute higher-body aggregation loses every fixed logarithmic saving at order `Theta(log X)`. Fixed-order squarefree-composite collision bounds are valid but lack a source coefficient contract. An exact Heath--Brown identity exhibits a cutoff dichotomy and an exponentially weighted residual requirement; coefficient growth alone is not an impossibility theorem.

The result is therefore a conditional theorem with a rigorously scoped obstruction ring, not progress toward an unconditional proof. The remaining direct input is a jointly signed selected-centre prime-tuple estimate through logarithmic order.

## 1. Scope and status

Fortune's conjecture states that the least positive offset producing a prime above a primorial is itself prime. Write

\[
P_n=\prod_{r\le n}p_r,
\qquad
F_n=\min\{m>1:P_n+m\in\mathbb P\}.
\]

The present work does not prove Fortune's conjecture. It proves an exact implication from a finite factorial-moment condition to eventual Fortune and records verified obstructions to standard attempts at proving that condition.

The logical spine is

\[
\mathrm{RUHL\!-\!FM}
\Longrightarrow
\mathrm{INT\!-\!AOD}
\Longrightarrow
\text{eventual Fortune}.
\]

The first arrow is the conditional arithmetic input formalized below. The second is an exact detector implication. No function-field theorem, random-order model or Paper VII endpoint-incidence statement is used in this chain.

## 2. Candidate collapse and row occupancy

Fix a large dyadic terminal-prime block `X<=p_{j+1}<2X` and a window `H` below the next square threshold, with the registered scale `H asymp X^2`. If `m<p_{j+1}^2` is composite, it has a prime divisor `r<p_{j+1}`. Since `r|P_j`, primality of `P_j+m` would force `r|(P_j+m)`, a contradiction. Therefore every successful candidate in the window is itself prime.

For a deterministic terminal-prime stratum `B_b`, let `M_b` be the common prime-offset universe and define

\[
I_{j,m}=1_{\mathbb P}(m)1_{\mathbb P}(P_j+m),
\qquad
Z_j=\sum_{m\in\mathcal M_b}I_{j,m}.
\]

The row fails precisely when `Z_j=0`. The adaptive occupancy detector evaluates

\[
G_b(1-q_b)
=\frac1{n_b}\sum_{j\in B_b}(1-q_b)^{Z_j},
\qquad 0<q_b\le1.
\]

Every failed row contributes one. Hence

\[
G_b(1-q_b)<\frac1{n_bB}
\]

in every stratum excludes all failed rows after aggregation over the `B` strata.

## 3. Exact finite Bonferroni criterion

Define factorial moments

\[
M_{b,k}=\frac1{n_b}\sum_{j\in B_b}(Z_j)_k
\]

and deterministic model means `lambda_j` satisfying

\[
0<L_b\le\lambda_j\le U_b.
\]

Set

\[
E_{b,k}=M_{b,k}-\frac1{n_b}\sum_{j\in B_b}\lambda_j^k.
\]

Let `K_b` be even. Since the binomial expansion terminates for every integer `z>=0`, its even Bonferroni partial sum is an upper bound:

\[
(1-q_b)^z
\le
\sum_{k=0}^{K_b}\frac{(-q_b)^k}{k!}(z)_k.
\]

Averaging and substituting the model gives

\[
G_b(1-q_b)
\le
\frac1{n_b}\sum_{j\in B_b}
\sum_{k=0}^{K_b}\frac{(-q_b\lambda_j)^k}{k!}
+
\mathcal E_{b,K_b},
\]

where

\[
\mathcal E_{b,K_b}
=
\sum_{k=0}^{K_b}\frac{(-q_b)^k}{k!}E_{b,k}.
\]

For even `K` and `x>=0`, Taylor's theorem gives

\[
0\le
\sum_{k=0}^{K}\frac{(-x)^k}{k!}-e^{-x}
\le
\frac{x^{K+1}}{(K+1)!}.
\]

Therefore

\[
G_b(1-q_b)
\le
 e^{-q_bL_b}
+
\frac{(q_bU_b)^{K_b+1}}{(K_b+1)!}
+
\mathcal E_{b,K_b}.
\]

### Theorem 3.1 — sharp finite detector criterion

If every stratum satisfies

\[
e^{-q_bL_b}
+
\frac{(q_bU_b)^{K_b+1}}{(K_b+1)!}
+
\mathcal E_{b,K_b}
<\frac1{n_bB},
\tag{3.1}
\]

then every sufficiently large registered primorial row contains a successful prime offset. Consequently eventual Fortune follows.

A sufficient absolute form replaces the signed error by

\[
\mathcal A_{b,K_b}
=
\sum_{k=0}^{K_b}\frac{q_b^k}{k!}|E_{b,k}|.
\]

The signed condition is weaker, but it is close to the truncated detector discrepancy itself and must not be advertised as an independent simplification without a prime-tuple theorem implying it.

## 4. Explicit logarithmic truncation

Put

\[
M_b^*=n_bB,
\qquad
q_b=(1+3\varepsilon)\frac{\log M_b^*}{L_b},
\qquad
K_b=\lceil\beta\log M_b^*\rceil_{\rm even},
\]

and `rho_b=U_b/L_b`. Stirling's lower bound yields

\[
\frac{(q_bU_b)^{K_b+1}}{(K_b+1)!}
\le
(M_b^*)^{-\alpha_b},
\]

where

\[
\alpha_b
=
\beta\log\!\left(
\frac{\beta}{e(1+3\varepsilon)\rho_b}
\right).
\]

For

\[
\varepsilon=0.10,
\qquad
\rho_b\le1.10,
\qquad
\beta=5,
\]

we obtain

\[
\alpha_b
=5\log\!\left(\frac5{e\cdot1.30\cdot1.10}\right)
=1.258817\ldots>1.20.
\]

The ratio assumption `rho_b<=1.10` is part of this numerical certificate and must accompany it whenever quoted.

The frozen geometry is consistent: `n_b asymp X/(log X)^(5/2)` and `B asymp (log X)^(3/2)`, hence

\[
M_b^*=n_bB\asymp X/\log X.
\]

## 5. Exact arithmetic interface

The factorial-moment identity is

\[
M_{b,k}
=\frac1{n_b}
\sum_{j\in B_b}
\sum_{\mathbf m\in\mathcal M_b^{\underline k}}
\prod_{a=1}^k I_{j,m_a}.
\]

For a registered tuple model `H_{j,k}(\mathbf m)`, define

\[
A_{b,k}
=
\frac1{n_b}\sum_j\sum_{\mathbf m}
\left(\prod_a I_{j,m_a}-H_{j,k}(\mathbf m)\right)
\]

and

\[
S_{b,k}
=
\frac1{n_b}\sum_j\sum_{\mathbf m}H_{j,k}(\mathbf m)
-
\frac1{n_b}\sum_j\lambda_j^k.
\]

Then the exact decomposition is

\[
\boxed{E_{b,k}=A_{b,k}+S_{b,k}.}
\]

Boundary, support and prime-power corrections must be incorporated into the observed term or model before this split. Appending an additional correction after both differences have been formed would double-count it.

The missing analytic theorem is uniform control of the jointly signed aggregate of `A_{b,k}` and `S_{b,k}` through `k=Theta(log X)` at the one-row scale in (3.1).

## 6. First-order strength inversion

The absolute envelope contains

\[
q_b|E_{b,1}|\le\mathcal A_{b,K_b}.
\]

Since the remaining detector margin `Delta_b` and `q_b` both have scale `log X/X`, the absolute theorem requires

\[
|E_{b,1}|<\Delta_b/q_b=O(1).
\]

The selected-centre mean has scale `X`. Thus termwise-absolute RUHL requires additive constant model accuracy, which is stronger than a positive linear lower bound such as `INT-SCME`.

The signed criterion retains one-sided slack. Writing

\[
\mathcal E_{b,K_b}
=-q_bE_{b,1}+R_{b,\ge2},
\]

an excess actual mean helps. The weakest signed implication is a lower bound on `E_{b,1}` depending on the signed higher-order remainder, not a two-sided absolute estimate. A successful future theorem must exploit this structure rather than discard it prematurely.

## 7. Collision geometry and squarefree moduli

For one post-terminal prime modulus, the primorial path has a sharp collision geometry: a pair of rows can collide only for primes dividing their primorial difference, and the number of such large prime divisors is bounded by the row separation. This gives the prime-modulus energy estimate used throughout the programme.

For squarefree moduli of fixed support order `r`, with every prime factor greater than `2X` and weights satisfying

\[
0\le\beta(q)q\le U_r,
\]

the fixed-order collision radius obeys

\[
R_\beta\le U_r{n-1\choose r+1}.
\]

Consequently

\[
E_\beta(a)
\le
\left(D_\beta+U_r{n-1\choose r+1}\right)\|a\|_2^2.
\]

This is a valid finite-order theorem. It does not transfer to RUHL because no actual source decomposition in the repository supplies the required coefficient family, conductor partition and row-preserving map into this energy.

## 8. Failure of pair-tree connected domination

For three offsets in one residue class modulo a post-terminal prime `p`, the normalized connected local coefficient is

\[
\kappa_{3,p}
=-\frac{p-2}{(p-1)^2},
\]

while the equal-residue pair coefficient is

\[
\kappa_{2,p}=\frac1{p-1}.
\]

A spanning-tree majorant with fixed edge constant `C` has total three-tree budget

\[
\frac{3C^2}{(p-1)^2}.
\]

The ratio is

\[
\frac{p-2}{3C^2},
\]

which is unbounded. Hence no fixed pair-edge constant can dominate every local connected coefficient.

An actual candidate witness occurs at

\[
X=18,\quad H=324,\quad p=37,\quad m\in\{89,163,311\},
\]

where all three prime offsets are congruent modulo `37`. Exact rational regressions now exercise connected-local recombination through order eight; Lean kernel checks the order-three obstruction and its deterministic consequence.

## 9. Absolute higher-body radius

The same-prime `r`-body absolute aggregation gives only

\[
T_r(m)\ll_r\frac{X^{r-1}}{(\log X)^r},
\]

corresponding to

\[
D_r\asymp
\frac{X}{(\log X)^{1+1/(r-1)}}.
\]

At `r=Theta(log X)`, the extra exponent tends to zero. Therefore an absolute hyperedge ledger cannot supply one fixed `delta>0` in

\[
D_r\ll X/(\log X)^{1+\delta}
\]

through all required orders. This does not refute signed higher-body recombination.

## 10. Heath--Brown scale and weighted-accuracy requirement

For the exact truncated identity

\[
\Lambda
=
\sum_{r=1}^{J}(-1)^{r-1}{J\choose r}
\mu_{\le z}^{*r}*1^{*(r-1)}*\log
\]

on `n<=z^J`, logarithmic `J` gives `z` exponentially larger than `H`. Forcing `z<=H` requires

\[
J\sim X/(2\log X)
\]

and binomial mass `2^J-1=exp(Theta(X/log X))`.

If `R_r` denotes the normalized residual for the `r`th source term, a triangle-inequality implementation must prove

\[
\sum_{r=1}^{J}{J\choose r}|R_r|<\Delta_b.
\]

The coefficient count proves this weighted-accuracy requirement, not impossibility. Residuals could in principle decay rapidly enough. No theorem in the present package proves such decay, and no universal closure of Heath--Brown or Vaughan methods is claimed.

## 11. Formalization and evidence classes

The formal package uses Lean 4.32.0. Claims are assigned one of five evidence classes:

1. `KERNEL_CHECKED`: the stated implication is proved in Lean without `sorry`, `admit` or hidden axioms;
2. `DERIVED_WITH_LEDGERED_AXIOM`: Lean derives the claim from one explicit external certificate boundary;
3. `EXACT_COMPUTATIONAL`: exact rational, integer, polynomial or finite-field verification, but not a Lean proof of the uniform theorem;
4. `MANUSCRIPT_PROVED`: a reviewed written proof not yet fully formalized;
5. `OPEN_OR_CONDITIONAL`: explicitly excluded from the proved chain.

Lean compliance means every load-bearing statement is mapped to one of these classes and no manuscript claims more formal support than exists. It does not mean every theorem in the seven-paper corpus has been fully formalized.

The current package kernel-checks the corrected detector implications, centred moment identities, selected Paper VII algebra, fixed-order collision criteria, the local tree obstruction, the RUHL first-order implications and the exact telescoping arithmetic interface. One Paper VII normalization/certificate axiom remains explicitly ledgered.

## 12. Final frontier

The exact conditional theorem is useful because its missing input is now unambiguous. The direct integer problem is:

> Prove a jointly signed selected-centre prime-tuple estimate through order `Theta(log X)` whose weighted aggregate satisfies (3.1) uniformly in every registered stratum.

Current methods do not supply this theorem. Pair-only dependency graphs, termwise absolute factorial moments and uninstantiated squarefree collision bounds do not replace it. The conditional implication and the barriers are the final supported result of this programme.

## 13. Nonclaims

This paper does not claim:

- an unconditional proof of RUHL-FM, `INT-AOD` or Fortune;
- a universal impossibility theorem for divisor identities or signed prime-tuple methods;
- that random-order results control the increasing primorial order;
- a function-field-to-integer transfer;
- that all seven prior papers are fully formalized;
- journal peer review or publication acceptance.
