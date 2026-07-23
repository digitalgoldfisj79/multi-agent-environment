# Application-ledger audit and route exhaustion

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** dependency audit complete; the missing application is a theorem, not bookkeeping.

## 1. Two exact reductions, no proved bridge

The general crown reduction in `D1_ATTACK.md` is an exact irreducible-count ledger. Its live sufficient condition is Lemma L, an inequality for aggregate incidence sums `R_a`.

The later `p ≡ 2 (mod 3)` Airy route proves a different exact reduction:

\[
D_b=-T_p/p\quad(b\ne0),\qquad D_0=(p-1)T_p/p,
\]

where `D_b` measures the distribution of the cubic trace on the trace-zero hyperplane.

Both are correct. What is absent is a proved morphism, equality, or spectral-sequence ledger identifying this Airy deviation with the load-bearing component of Lemma L or with the final hook/q-line irreducibility count.

## 2. Why the punctual trace identity is insufficient

The equality

\[
D_0=-(p-1)D_{b\ne0}
\]

is an equality of trace-function values. It does not imply that the corresponding nearby-cycle complex has no additional punctual constituents, nor that a punctual class appears with the sign and Tate normalization required by the global irreducibility ledger.

Numerical equality of total first traces cannot identify objects in a Grothendieck group: nonisomorphic complexes can have the same first trace and different higher traces, monodromy, weights or boundary maps. A categorical comparison is load-bearing.

## 3. Exact missing obligations

A complete application theorem must provide all of the following.

1. **Object-level identification.** Construct the functorial map from the cubic trace-zero/Airy complex to the post-pushforward even--odd hook complex controlling the irreducible-fibre count.
2. **Main/Tate/Artin--Schreier subtraction.** Identify exactly which constant line and excluded Artin--Schreier orbit have already been counted, with the correct sign and Tate twist.
3. **Punctual transport.** Prove that `D_0=-(p-1)D_*` supplies the required nearby-fibre subtraction at the level of complexes or characteristic cycles, not only one numerical trace.
4. **Arithmetic twist at infinity.** Carry the parameter-dependent unramified quadratic extension of arithmetic monodromy identified in the hook audit. Geometric inertia alone does not fix the Frobenius sign.
5. **Boundary cells.** Include both the `q=2` cell and the `q=∞` (`c=0`) boundary, which exact finite-prime assemblies show can contribute nontrivially.
6. **Final positivity implication.** Derive explicitly that the resulting trace estimate forces, for at least one square class `a`, the exact certificate condition `N_a notin 2p Z_{>=0}` and hence an irreducible quadratic or cubic offset.

No existing file proves this chain. Several explicitly label it pending.

## 4. Status of the Airy estimate

The estimate

\[
|T_p|\le C p^{(p-1)/2}
\]

is a clean, genuine open theorem. It proves the stated bound for the trace-zero cubic deviation. It is presently a **candidate analytic input** to the `p ≡ 2 (mod 3)` crown, not a proved sufficient condition for `FF-Fortune(p,1)`.

Conversely, the crown might require less if the missing categorical ledger contains additional cancellation. No such slack has been proved. Weakening the Airy target would therefore be speculative.

## 5. Route audit after the new spectra

### A. Common Frobenius-factor collapse

Tested exactly through invariant ranks `1--4`. Only `p=23` has a common central factor; `p=11,17,29` do not. Closed as a uniform wholesale-cancellation mechanism.

### B. Root-of-unity or bounded-period phases

Refuted by the exact `p=17` normalized trace `29/17`: a root-of-unity phase would have algebraic-integral `y+y^{-1}`. Closed.

### C. Uniform Newton-slope pairing

Refuted by `p=17`: slopes of `U_17` are `(8,10)`, while those of `pU_15` are `(9,9)`. Closed in its literal slope-by-slope form.

### D. Characteristic-zero cross-`k` correspondence

Closed by disjoint Hodge spectra. Any successful map must be special to `k=char=p`.

### E. Canonical mod-`p` Adams lift

The principal characteristic-zero defect has full rank after the exact `mu_3` projection. Closed as a bounded-cone argument.

### F. Local Swan/conductor collapse

Proved locally, but the global Adams class has negative irreducible multiplicity and at least six residual eigenvalues already at `p=11`. Local rank two does not globalize. Closed as a direct proof.

### G. Bare cyclic-shift localization

The target is `sigma Frob`, not `sigma`; the former reconstructs the original extension-field locus. Closed.

### H. Gaussian-period bounded-degree reduction

Both parameter sectors have full orbit degree `(p-1)/2` and maximal Dickson remainder degree at tested primes. Closed as a bounded-degree period reduction.

### I. Larger prime sweeps

Statistically nondecisive. Useful only to test a proposed identity. Not a proof route.

### J. Existing literature

Haessig's effective decomposition works for `k<p` and explicitly identifies denominators as the obstruction at `k>=p`. Haessig--Rojas-Leon compute degrees, local factors and weights, not the required cross-`k` correlation. Sabbah--Yu and Qin determine Hodge data, which obstruct rather than furnish a characteristic-zero pairing. Chuang's 2026 arithmetic Picard--Lefschetz formula supplies explicit local vanishing-cycle information but does not evaluate the surviving global component in this boundary pair. Fu--Wan and quantitative sheaf theory control local factors or complexity for fixed objects, not an absolute trace constant in a family whose rank grows linearly with `p`.

No transferable theorem closing either the Airy estimate or the application ledger was found.

## 6. Genuine terminal boundary

After the corrected spectral computation, every remaining path requires one of two new theorems:

1. **Analytic theorem:** an absolute-constant Frobenius correlation between `U_p` and `U_{p-2}(-1)` at `k=p`;
2. **Application theorem:** an object-level nearby-cycle/hook ledger transporting that bound into the exact irreducibility certificate.

These are logically independent. Neither is a computation, a sign convention, a missing low-prime test, nor an application of a located theorem. Further autonomous computation without a proposed structural identity would only enlarge tables.
