# End-to-end audit of Chuang arXiv:2607.05757 against the d=1 Airy target

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-collapse-integration-20260723`  
**Scope:** function-field `d=1` Fortune sibling only.

## 0. Verdict

The paper does **not** prove the required absolute bound, and its advertised zero-trace theorem is not the missing step for the pair `k=p` and `k=p-2`.

It does, however, give a real structural reduction:

- for `p == 2 mod 3`, arithmetic Frobenius has zero trace on the non-trivial `mu_3` eigenspaces;
- after Chuang's `A'` comparison and the unique `k=p` Picard--Lefschetz correction are included, the two remaining trace spaces have the same rank

\[
 r_p=\frac{p-5}{6};
\]

- the exact target becomes a Frobenius correlation between these two equal-rank `mu_3`-invariant spaces.

This improves the elementary linear-loss bound by a factor of three, but the rank still grows linearly with `p`.

## 1. Target and notation

Let `A=Ai_{x^3}` and, for `p == 2 mod 3`, put

\[
V_p=H_c^1(\mathbb A^1_{\overline{\mathbb F}_p},\operatorname{Sym}^p A),
\]

\[
W_p=H_c^1(\mathbb A^1_{\overline{\mathbb F}_p},\det(A)\otimes\operatorname{Sym}^{p-2}A).
\]

With the determinant normalization already checked in this branch,

\[
\operatorname{Tr}(F_p\mid W_p)
=p\operatorname{Tr}\!\left(F_p\mid H_c^1(\operatorname{Sym}^{p-2}A)\right).
\]

The collapse identity gives

\[
\operatorname{Tr}(F_p\mid V_p)-\operatorname{Tr}(F_p\mid W_p)=-pT_p.
\]

## 2. Exact specialization of Chuang's correction terms

Chuang's Theorem 4.18 treats the `A'` motive for odd `k`. Its Picard--Lefschetz correction is indexed by odd integers

\[
1\le a\le k/p.
\]

Chuang's Theorems 4.21--4.22 treat the `A''` motive. The vanishing-cycle contribution `E` is indexed by the same odd integers, while its inertia-invariant part `E'` requires

\[
v_p(a)\equiv5\pmod6.
\]

Specializing:

| `k` | `A'` correction indices | `A''` vanishing indices | inertia-invariant `E'` |
|---:|---:|---:|---:|
| `p` | `{1}` | `{1}` | empty, since `v_p(1)=0` |
| `p-2` | empty | empty | empty |

Consequences:

1. At `k=p`, the two-dimensional `A''` vanishing-cycle space exists but is ramified and contributes nothing to inertia invariants.
2. At `k=p-2`, there is no vanishing correction.
3. Chuang's statement that `Tr(Frob_p|E')=0` for `p == 2 mod 3` is therefore vacuous for both members of our pair: `E'` is already zero.

Thus the explicit Jacobi-sum characteristic polynomial in Theorems 4.22 and 4.24 does not evaluate the trace we need.

## 3. Frobenius kills the non-trivial mu_3 trace

Over `\overline{\mathbb F}_p`, decompose any `mu_3`-equivariant space as

\[
H=H_1\oplus H_\chi\oplus H_{\chi^{-1}}.
\]

For `p == -1 mod 3`, arithmetic Frobenius sends `\chi` to `\chi^p=\chi^{-1}`. Hence it interchanges `H_\chi` and `H_{\chi^{-1}}`. Its matrix on their direct sum is block off-diagonal, so

\[
\operatorname{Tr}(F_p\mid H_\chi\oplus H_{\chi^{-1}})=0.
\]

Therefore, for every `k`,

\[
\operatorname{Tr}\!\left(F_p\mid H_c^1(\operatorname{Sym}^k A)\right)
=
\operatorname{Tr}\!\left(F_p\mid H_c^1(\operatorname{Sym}^k A)^{\mu_3}\right).
\]

This is an exact trace identity, not a dimension heuristic.

## 4. The boundary term in Proposition 4.14 has zero trace

Chuang's Proposition 4.14 gives a short exact sequence

\[
0\to B_k\to M'_k(\mathbb F_p)\to
H_c^1(\operatorname{Sym}^k A)^{\mu_3}\to0,
\]

where

\[
B_k=
\left(\operatorname{Sym}^k H_c^1(\mathbb A^1,\mathcal L_{\psi(x^3/3)})\right)^{\mu_3}.
\]

For `p == 2 mod 3`, Frobenius interchanges the two non-trivial `mu_3` eigenlines in the underlying two-dimensional cubic exponential cohomology. On an odd symmetric power, it sends a monomial of bidegree `(j,k-j)` to one of bidegree `(k-j,j)`. Since odd `k` has no fixed index `j=k-j`, the trace on `B_k` is zero.

Both `k=p` and `k=p-2` are odd. Hence

\[
\operatorname{Tr}(F_p\mid B_p)=
\operatorname{Tr}(F_p\mid B_{p-2})=0.
\]

The relevant Airy traces are therefore exactly the traces on the special-fibre `A'` quotients.

## 5. Equal-rank reduction

Write `p=6r+5`. Chuang's Lemma 4.17 gives

\[
\dim M'_k=\left\lfloor\frac{k+1}{2}\right\rfloor.
\]

Theorem 4.18 removes one Tate line from the special fibre when `k=p`, because the correction index set is `{1}`. It removes nothing when `k=p-2`. Thus

\[
\dim M'_p(\mathbb F_p)=\frac{p-1}{2}
=\dim M'_{p-2}(\mathbb F_p).
\]

The boundary dimensions from Proposition 4.14 are

\[
\dim B_k=\left\lfloor\frac{k}{3}\right\rfloor+1-\mathbf 1_{k\equiv1\ (3)}.
\]

For `p=6r+5`,

\[
\dim B_p=\dim B_{p-2}=2r+2.
\]

Therefore, defining

\[
U_k=H_c^1(\operatorname{Sym}^k A)^{\mu_3},
\]

we obtain the exact equality

\[
\boxed{\dim U_p=\dim U_{p-2}=r=\frac{p-5}{6}.}
\]

The target is now

\[
\boxed{
-pT_p=
\operatorname{Tr}(F_p\mid U_p)
-p\operatorname{Tr}(F_p\mid U_{p-2}).
}
\]

After the Tate twist, both terms have weight `p+1`.

## 6. Improved unconditional bound

Purity now gives

\[
|pT_p|
\le 2r\,p^{(p+1)/2}.
\]

Hence

\[
\boxed{
|T_p|\le \frac{p-5}{3}\,p^{(p-1)/2}.
}
\]

This improves the previous coefficient `p-3` by an asymptotic factor of three. It does not give an absolute constant.

## 7. Focused exact first-trace audit

The companion script `chuang_specialization_audit.py` computes the first traces exactly in `Z[zeta_p]` and verifies the specialization data.

Let the displayed entries be divided by `p^((p+1)/2)`; the second entry already includes the determinant/Tate factor `p`.

| `p` | rank `r` | `Tr(U_p)` | `p Tr(U_{p-2})` | virtual trace |
|---:|---:|---:|---:|---:|
| 11 | 1 | `-1` | `1` | `-2` |
| 17 | 2 | `-29/17` | `0` | `-29/17` |
| 23 | 3 | `235/529` | `-326/529` | `561/529` |
| 29 | 4 | `48674/24389` | `-16745/24389` | `65419/24389` |

At `p=11`, the two equal-rank one-dimensional pieces are maximally anti-correlated, not equal or sharing a Frobenius factor. This rules out the strongest possible interpretation of the equal-rank coincidence.

## 8. Why the paper stops here

Chuang's explicit Jacobi-sum formula applies to the inertia-invariant vanishing-cycle component `E'`. For our two values of `k`, that component is empty.

The surviving geometric component is the cohomology of

\[
A'_k:\quad
\sum_{i=1}^k\left(\frac{y_i^3}{3}-y_i\right)=0
\]

in the sign isotypic sector. This is not the diagonal hypersurface treated by the paper's general Jacobi-sum trace theorem: the linear terms are essential. The paper supplies no cross-`k` correspondence between the geometric components for `k=p` and `k=p-2`.

## 9. Exact remaining theorem after the audit

The smallest remaining theorem is now sharper than the previous full-Air y formulation:

> For `p == 2 mod 3`, prove an absolute bound for the difference of Frobenius traces on two equal-rank spaces `U_p` and `U_{p-2}(-1)`, each of rank `(p-5)/6`.

Equivalently, construct one of:

1. a Frobenius-equivariant cross-`k` correspondence between the two `A'` sign-isotypic special-fibre motives with bounded trace defect;
2. an exact character/Jacobi decomposition of the global geometric `A'` component, not merely its local vanishing cycles;
3. a Dwork operator identity that cancels the explicit `mu_3`-invariant defect classes.

## 10. Status classification

- **PROVED:** the correction-index specialization and emptiness of `E'`.
- **PROVED:** zero trace on the non-trivial `mu_3` sector for `p == 2 mod 3`.
- **PROVED:** zero trace on the Proposition 4.14 boundary terms for odd `k`.
- **PROVED:** equal rank `(p-5)/6` of the two surviving trace spaces.
- **PROVED:** the improved coefficient `(p-5)/3` in the unconditional bound.
- **VERIFIED COMPUTATIONALLY:** the exact first traces at `p=11,17,23,29`.
- **OPEN:** an absolute-constant bound for their trace difference.

The paper is highly relevant, but it does not contain the missing global correlation theorem.