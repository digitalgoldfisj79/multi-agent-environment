# Disposition of the final hostile review — Paper I

## Exact objects

- Model: `Qwen/Qwen3-14B-AWQ`
- Hugging Face job: `6a638c45db23d7a7ec1cabd8`
- Publication commit: `401dff3b96525cdef6bd1b54d18f4450e5785ac8`
- Manuscript SHA-256: `0e0f8a0d89209b8f4dd8c589526a89d57bd536f4889fdcd9c902a09b1a62f157`

The review finds no fatal or major defect. It records high confidence in the results and raises two minor reproducibility/presentation reservations. Both are disposed against the deposited exact checks.

## 1. Theorem 5.2 template and transport constants

**Review reservation.** The main paper states the finite constants

```text
template counts: 70, 140, 90, 20
transport sums: 280, 480, 252, 40
```

without printing all finite templates in the body.

**Disposition: resolved by the exact deposited audit.** The theorem explicitly identifies the calculation as finite and the reproducibility section points to the complete supplementary archive. The live Zenodo archive contains both the production enumerator and an independently written reconstruction.

The direct Zenodo rerun in job `6a638a047ef3c0846496797f` obtained:

```text
templates={0:70,1:140,2:90,3:20}
T_k={0:280,1:480,2:252,3:40}
gap identity=True
```

The independent code did not reuse the production table. The counts are therefore not unsupported empirical values; they are finite exact constants with two implementations and a complete archive trail.

No manuscript repair is required. Printing all 320 oriented templates in the paper would reduce readability without strengthening the proof package.

## 2. Proposition 5.4 matrix eigenvalues

**Review reservation.** The paper states the eigenvalues of

\[
M=\begin{pmatrix}
3&4&4&4\\
4&3&4&4\\
4&4&8&4\\
4&4&4&8
\end{pmatrix}
\]

without displaying the characteristic-polynomial arithmetic.

**Disposition: resolved.** This is an elementary exact computation from a displayed `4 x 4` integer matrix. The independent audit recomputed the matrix and its spectrum symbolically and returned `M matches=True; eigs match=True`. The full bilinear identity was also tested independently at `r=101`, with residual `2.66e-15`.

The eigenvalues

\[
-1,\quad 4,\quad \frac{19-\sqrt{281}}2,\quad \frac{19+\sqrt{281}}2
\]

are correct. The omitted four-line determinant expansion is a presentational compression, not a logical dependency or mathematical gap.

No manuscript repair is required.

## Other claim boundaries

The review correctly recognises that the following remain open and are not promoted to theorems:

- HTE4;
- HWF4;
- FBHE4;
- RQHE4;
- the signed sieve or von Mangoldt prime-detection bridge;
- any prime-offset theorem; and
- Fortune's conjecture.

## Gate conclusion

**Fresh exact-hash hostile-review gate: passed after disposition.**

No source change is required. This does not constitute human specialist review, journal acceptance or proof of any explicitly open estimate.
