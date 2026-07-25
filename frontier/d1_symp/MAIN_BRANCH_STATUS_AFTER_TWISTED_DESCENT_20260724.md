# Main-branch status after the twisted-descent theorem

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only.

## Route discipline

Only two research branches remain admissible:

1. **Analytic branch:** prove the absolute normalized Frobenius trace bound.
2. **Application branch:** transport the resulting motive/trace into the exact hook and irreducibility ledger.

The coefficient-level `k=p` Dwork resonance investigation has been stopped. It produced a valid two-divisor theorem and explicit inverse residue, but the exact `mu_3` sector retains linearly many Laurent classes before Dwork reduction. No bounded Frobenius block follows. Further work on that subroute without the actual Frobenius operator would be a diversion.

## New proved main-branch results

### 1. Scheme-level descent

The Artin--Schreier trace model

\[
X_p^{AS}=\{\operatorname{Tr}(x^2)=\operatorname{Tr}(x^3)=0\}
\subset\mathbf P(\ker\operatorname{Tr}/\mathbf F_p)
\]

is an `F_p`-form of the split cyclic permutation complete intersection

\[
X_p^{perm}=\{\sum x_i=\sum x_i^2=\sum x_i^3=0\}/(1,\ldots,1).
\]

Its Frobenius descent is the cyclic-Frobenius operator, with the two cyclic orientations conjugate.

### 2. Exact primitive trace

For `p=2 mod 3`,

\[
\#X_p^{AS}(\mathbf F_p)
=
\#\mathbf P^{p-5}(\mathbf F_p)+T_p/p^2,
\]

hence

\[
T_p
=
p^2\operatorname{Tr}
\left(
F_{p,geom}
\mid H^{p-5}_{prim}(X_p^{AS})
\right).
\]

This closes the object identification and the projective/Tate subtraction on the analytic branch.

### 3. Exact primitive rank

\[
\dim H^{p-5}_{prim}(X_p)
=
\frac{2^{p-1}-1}{3}.
\]

Thus the analytic theorem is genuinely an exponential-rank trace cancellation. The smooth complete intersection itself is not the conjectural `O(p)` hook survivor.

## Exact remaining targets

### Analytic main branch

Prove

\[
\left|
\operatorname{Tr}
\left(
\sigma^{\pm1}F_{p,geom}
\mid H^{p-5}_{prim}(X_p^{perm})
\right)
\right|
\le C p^{(p-5)/2}
\]

with absolute `C`.

A valid next step must give an explicit cyclic-descent decomposition, virtual cancellation, or Frobenius correlation. More point counts, prime sweeps, fixed-locus calculations for bare `sigma`, and generic complete-intersection bounds are closed or non-decisive.

### Application main branch

Construct a virtual correspondence or spectral-sequence comparison from the primitive cyclic-Frobenius motive to the zero-frequency/post-pushforward hook complex. It must explicitly include:

- the `q=2` cell;
- the `q=infinity` cell;
- the arithmetic quadratic twist at infinity;
- main/Tate and Artin--Schreier subtraction;
- the endpoint/punctual term;
- the final implication to the parity-protected irreducibility certificate.

A direct injection or equality of actual motives is ruled out as the intended mechanism: the primitive source has exponential rank, while the hook target seeks cancellation to a virtual `O(p)` survivor.

## Stop rule

Do not continue by constructing another surrogate invariant. Resume only with one of:

1. an explicit formula for the cyclic-descent action on primitive cohomology;
2. an explicit virtual map into the hook complex;
3. a specialist theorem that supplies either of those objects.
