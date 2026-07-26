# Hostile audit: global Cartier mass and naive `p^2` lift

**Date:** 2026-07-26  
**Audited result:** `GLOBAL_CARTIER_MASS_AND_P2_LIFT_OBSTRUCTION_20260726.md`  
**Decision:** **PASS WITH STRICT SCOPE**.

## 1. Strongest supported conclusion

The audit supports two exact conclusions.

First, the complete multiplicative Fourier transform in the cubic coefficient `a` contains only the two square-class modes. This follows formally from

\[
C_3(F_{a,c,d})=3a1_{irr}
\]

and the fact that `N_a` depends only on `chi(a)`. Hence complete parameter averaging cannot produce an invariant independent of `N_++N_-` and `N_+-N_-`.

Second, the obvious coefficientwise lift of the Cartier matrix to `Z/p^2` is not a canonical irreducibility indicator. Exact exhaustive counterexamples at `p=5,7` establish reducible contamination, dependence on integer lift choices, and failure of the weighted-mass identity.

These are theorem-level obstructions to the proposed route.

## 2. Checks against overclaim

### 2.1 Does global mod-`p` mass vanishing imply cubic failure?

No. The note correctly rejects that inference. At `p=5` and `p=19`, the class sum is `2p`, so the trivial mass vanishes modulo `p` while both class counts are positive.

### 2.2 Do the two Fourier modes determine the integer counts?

No. They determine the two counts only modulo `p`. Simultaneous vanishing means both counts are multiples of `p`; it does not imply they are zero.

### 2.3 Does the `p^2` experiment refute every Witt lift?

No. It refutes only the naive lift obtained by reusing the coefficient formula over `Z/p^2`. A canonical Witt, crystalline or prismatic construction may contain correction terms and may be lift-independent.

### 2.4 Does it refute the fixed-class ordinary determinant route?

No. The ordinary identity

\[
\sum_{c,d}C_3(F_{a,c,d})=3aN_a\pmod p
\]

remains exact. A structural proof that one class residue is nonzero would still prove the cubic crown.

### 2.5 Is the small-prime counterexample sufficient for a uniform architecture?

Yes. The proposed architecture asserted a canonical identity obtained by the same formula at every prime. One exact prime where reducible contamination or lift dependence occurs refutes that architecture. The `p=5,7` pair provides redundant confirmation.

## 3. Independent arithmetic check

For the global Fourier theorem, write

\[
N_a=A+B\chi(a).
\]

Then

\[
\sum_{a\ne0}a^rN_a
=A\sum a^r+B\sum\chi(a)a^r.
\]

The first power sum is supported only at `r=0 mod p-1`; the second only at `r=(p-1)/2 mod p-1`. The factors and signs in the two boxed formulas are correct.

At `p=5`, `(N_+,N_-)=(4,6)` gives

\[
-\frac32(N_++N_-)=0\pmod5,
\qquad
-\frac32(N_+-N_-)=3\pmod5.
\]

At `p=7`, `(10,8)` gives

\[
-\frac32(18)=1\pmod7,
\qquad
-\frac32(2)=4\pmod7.
\]

These match the verifier output.

## 4. Epistemic classification

### Proved

- complete two-mode Fourier collapse of the global ordinary Cartier mass;
- failure of uniform trivial-mass nonvanishing;
- reducible contamination of the naive `p^2` lift at `p=5,7`;
- integer-lift dependence at `p=5,7`;
- failure of the naive lifted mass identity at `p=5,7`.

### Exact computational theorem

- the exhaustive `p=5,7` regression table produced by `global_cartier_mass_p2_verify.py`.

### Not proved

- impossibility of every canonical higher-Witt construction;
- fixed-class mod-`p` nonvanishing for all primes;
- any archimedean estimate for the class counts;
- the `d=1` crown.

## 5. Strategic ruling

The recommendation to “sum over all `a,c,d`, then lift to `p^2` if necessary” does not define a viable simplification:

1. summing over `a` loses no mystery but gains no new invariant;
2. the first aggregate digit can vanish on positive counts;
3. the next digit is not supplied by the ordinary cofactor formula.

Further Cartier work is justified only if it introduces one of the following genuinely new ingredients:

- a canonical higher-Witt cofactor with its reducible correction complex;
- a transfer-operator formula evaluating one fixed-class residue without subset enumeration;
- a theorem preventing simultaneous vanishing of the two fixed-class residues.

Absent such an ingredient, the programme should move to the invariant q-line nonsaturation or constructive-dynamics fronts rather than repeat parameter averaging.
