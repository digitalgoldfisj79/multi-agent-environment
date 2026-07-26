# Exact `p=11` cyclotomic lift for `C_wedge` and the sign-hook overage

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Target:** aggregate `h=4` Betti programme for function-field Fortune at `d=1`.  
**Status:** the reduction to one shuffle operator and the characteristic-zero nullity profile below are **PROVED**. The matrix ranks are an **EXACT COMPUTER-ASSISTED THEOREM** with symbolic certificates. The geometric removal of the final sign class is **OPEN**.

## 0. Result

Let `zeta=zeta_11` be a primitive eleventh root of unity and put

\[
\eta=-\zeta^{-1},
\]

which has order `22`. Let

\[
\Omega_{1,10}(\eta)
=\sum_{j=1}^{11}\eta^{j-1}\sigma_j,
\qquad
\sigma_j=(j\ j-1\ \cdots\ 1),
\]

act on the hook representation

\[
\bigwedge^r\operatorname{Std}_{11}.
\]

The exact kernel dimensions over `Q(zeta_11)` are

\[
\boxed{
(d_0,d_1,\ldots,d_{10})
=(0,0,1,1,1,3,3,1,0,0,1).
}
\]

Consequently

\[
\boxed{
\sum_{r=0}^{10}d_r=11=6\text{ even-hook dimensions}+5\text{ odd-hook dimensions}.
}
\]

Since

\[
C_\wedge^{\otimes11}
\cong
\bigoplus_{r=0}^{10}
\left(\bigwedge^r\operatorname{Std}_{11}\right)^{\oplus2},
\]

the complete terminal first bar homology is

\[
\boxed{
\dim H_1\left(B_{11},(C_\wedge)_\zeta^{\otimes11}\right)=22.
}
\]

The stable modular value `22` in `CWEDGE_TERMINAL_BAR_PROBE_20260726.md` is therefore genuine characteristic-zero homology, not auxiliary-characteristic rank loss.

## 1. Why the full indecomposable quotient reduces to one operator

Let

\[
A=A\!\left((C_\wedge^*)_{-\bar\zeta}\right)
\]

be the relevant quantum shuffle algebra. In total degree `11`, reduced first bar homology is the indecomposable quotient

\[
H_1(B_{11}(A))
=
A_{11}\Big/\sum_{a=1}^{10}A_aA_{11-a}.
\]

The twist parameter in the shuffle operator is `eta=-zeta^{-1}`, of order `22`.

Ma's shuffle-isomorphism criterion says that a product

\[
\tau_{u,v}:A_u\otimes A_v\longrightarrow A_{u+v}
\]

is an isomorphism unless the twist order divides `i(i-1)` for some `i<=u+v`. For every

\[
2\le i\le10,
\]

one has

\[
22\nmid i(i-1).
\]

Thus, for every `2<=a<=10`,

\[
A_a=A_1A_{a-1}.
\]

By associativity, for every split `a+(11-a)`,

\[
A_aA_{11-a}
=(A_1A_{a-1})A_{11-a}
\subseteq A_1A_{10}.
\]

The reverse inclusion is one of the summands in the decomposable subspace. Hence

\[
\boxed{
\sum_{a=1}^{10}A_aA_{11-a}=A_1A_{10}.
}
\]

Therefore

\[
\boxed{
H_1(B_{11}(A))=\operatorname{coker}\tau_{1,10}.
}
\]

On any `S_11` representation, `tau_{1,10}` is the one-sided shuffle operator `Omega_{1,10}(eta)`. This proves that the hook calculation below determines the **full** terminal `H_1`, not merely an upper bound obtained from one selected multiplication map.

## 2. Hook decomposition by Hamming weight

The weight-`k` binary-word sector of `C_wedge^{tensor 11}` is the signed permutation module

\[
\operatorname{Ind}_{S_{11-k}\times S_k}^{S_{11}}
(\mathbf1\boxtimes\operatorname{sgn}).
\]

The Pieri rule gives

\[
\boxed{
M_k
\cong
\bigwedge^{k-1}\operatorname{Std}_{11}
\oplus
\bigwedge^k\operatorname{Std}_{11},
}
\]

with nonexistent boundary terms omitted. Hence, if `h_k` is the weight-`k` first-homology dimension,

\[
\boxed{h_k=d_{k-1}+d_k.}
\]

The exact profile is therefore

| Hamming weight `k` | `dim H_1` |
|---:|---:|
| 2 | 1 |
| 3 | 2 |
| 4 | 2 |
| 5 | 4 |
| 6 | 6 |
| 7 | 4 |
| 8 | 1 |
| 10 | 1 |
| 11 | 1 |

and zero in the omitted sectors. This reproduces every entry of the earlier three-prime modular profile.

## 3. Exact cyclotomic certificate

The verifier `p11_cwedge_cyclotomic_lift_verify.py` works hook by hook.

For each of the five rational primes

\[
1013,\ 2003,\ 3037,\ 4027,\ 4049
\qquad(\equiv1\pmod{22}),
\]

it performs the following steps.

1. Choose a primitive eleventh root `z` in the auxiliary prime field.
2. Compute the canonical left kernel of `Omega_{1,10}(-z^{-a})` for every Galois embedding `a=1,...,10`.
3. Interpolate those ten evaluations into the power basis `1,zeta,...,zeta^9`.
4. Combine the five reductions coefficientwise by the Chinese remainder theorem.
5. Apply unique rational reconstruction.
6. Clear a common denominator and verify the lifted vectors exactly in
   \[
   \mathbf Z[\zeta_{11}]=\mathbf Z[x]/(1+x+\cdots+x^{10}).
   \]

The reconstructed certificate denominators are

| hook degree | nullity | common denominator |
|---:|---:|---:|
| 2 | 1 | 11 |
| 3 | 1 | 1 |
| 4 | 1 | 49841 |
| 5 | 3 | 22517 |
| 6 | 3 | 253 |
| 7 | 1 | 43 |

For each hook, the normalized free-coordinate block is diagonal, proving independence of the lifted kernel vectors.

A nonzero maximal minor modulo `1013` proves the opposite inequality on the characteristic-zero rank. Thus the exact lifted kernel and the modular minor meet, proving each displayed nullity.

For hook degrees `1,8,9`, the operator is already invertible modulo `1013`, hence is invertible over `Q(zeta_11)`. The trivial hook has eigenvalue

\[
\sum_{e=0}^{10}\eta^e=\frac{1-\eta^{11}}{1-\eta}=\frac2{1-\eta}\ne0.
\]

On the sign hook,

\[
\eta^e\operatorname{sgn}(\sigma_{e+1})
=(-\zeta^{-1})^e(-1)^e
=\zeta^{-e},
\]

so the eigenvalue is

\[
\sum_{e=0}^{10}\zeta^{-e}=0.
\]

This proves the complete profile.

## 4. The former excess two dimensions are the doubled sign class

The multiplicity-one aggregate hook kernel has total dimension

\[
11.
\]

The exact Sawin budget is

\[
p-1=10.
\]

The final hook

\[
\bigwedge^{10}\operatorname{Std}_{11}=\operatorname{sgn}
\]

contributes exactly one dimension. Removing that one hook contribution leaves

\[
\boxed{
\sum_{r=0}^{9}d_r=10=p-1.
}
\]

Because `C_wedge^{tensor 11}` contains two copies of every hook, the full rank-two bar model contains two sign classes. Thus

\[
22-2=20=2(p-1).
\]

The modular overage `22>20` has therefore been identified representation-theoretically: it is exactly accounted for by the two copies of the unique sign-hook terminal class.

This does **not** yet prove that the sign class is removed from Sawin's aggregate interval cohomology. It proves that no other hook sector exceeds the doubled budget.

## 5. Arithmetic meaning of the sign class

For a squarefree polynomial, the sign of its Frobenius permutation is the quadratic character of its discriminant. Hence the terminal sign-hook class is the discriminant-character sector of the factorization detector.

This aligns with the committed discriminant calculations in

`BOUNDARY_DISCRIMINANT_AND_FOURIER_CALIBRATION_20260725.md`,

which already use the Frobenius-sign/discriminant criterion to prove exact boundary vanishings. It does not follow from those boundary results that the global sign-isotypic compactly supported class vanishes or can be discarded.

The next comparison theorem must decide one of two possibilities.

1. **Geometric removal.** The sparse Fourier--Cayley/Rees construction kills the terminal sign class by an additional differential, quotient or weight exclusion.
2. **Explicit arithmetic extraction.** The sign/discriminant trace is evaluated separately and removed from the absolute Betti error budget before applying the aggregate Sawin estimate.

Either mechanism would leave the remaining terminal associated-graded mass exactly at the required budget `p-1` in the first load-bearing case.

## 6. Revised programme

### Completed

- corrected aggregate Sawin target `B_Lambda<=p-1`;
- virtual-to-Betti no-go;
- reduction of terminal `H_1` to `coker Omega_{1,10}`;
- exact characteristic-zero hook-nullity profile at `p=11`;
- exact identification of the two-copy overage with the sign hook.

### Active theorem

> **Sign/discriminant absorption theorem.** Construct the parity-separated sparse Fourier--Cayley/Rees comparison at the terminal order-`p` resonance and prove that the sign-hook terminal class is either killed in the sparse interval complex or splits off as an explicitly evaluable discriminant trace. Preserve actual cohomological dimensions, not only the signed Grothendieck class.

### After that theorem

1. determine the remaining associated-graded hook mass for general `p`;
2. prove it is at most `p-1` after sign extraction;
3. descend from the doubled `C_wedge` model to the multiplicity-one Sawin complexes;
4. conclude `B_Lambda<=p-1` and the `d=1` crown.

## 7. Ruling

The `p=11` uncertainty is closed:

\[
\boxed{
\dim H_1(C_\wedge)=22\text{ exactly over characteristic zero.}
}
\]

The literal unmodified rank-two bar page misses its doubled budget, but only by the two copies of one canonical representation: `sgn`. The proof programme has therefore moved from a diffuse excess-homology problem to a single discriminant-class theorem.
