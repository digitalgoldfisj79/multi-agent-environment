# Terminal order-`p` quantum bar two-line theorem

**Date:** 2026-07-25  
**Branch:** `gpt56/airy-gaussian-independent-audit-20260725`  
**Scope:** the scalar quantum-shuffle skeleton at the first order-`p` resonance.  
**Status:** the bar-homology theorem below is **PROVED**. Its identification with the actual wild Fourier--Cayley nearby cycles remains **OPEN**.

## 1. One-dimensional quantum shuffle algebra

Let `K` be a characteristic-zero field containing a primitive `p`-th root of unity

\[
 \zeta,
\]

where `p` is an odd prime. Let `A_zeta` be the quantum shuffle algebra of the one-dimensional braided vector space on which a positive crossing acts by `zeta`.

Its degree-`n` piece has basis `e_n`, and multiplication is

\[
 \boxed{
 e_a*e_b={a+b\brack a}_\zeta e_{a+b},
 }
\]

where the coefficient is the Gaussian binomial.

The weight-`n` reduced bar complex `B_n(A_zeta)` has a one-dimensional basis vector for every composition

\[
 \lambda=(\lambda_1,\ldots,\lambda_r),
 \qquad
 \lambda_i>0,
 \qquad
 \sum_i\lambda_i=n.
\]

Its differential merges adjacent parts, with coefficient

\[
 {\lambda_i+\lambda_{i+1}\brack\lambda_i}_\zeta
\]

and the usual alternating sign.

## 2. Complete nonresonance below `p`

### Theorem 2.1

For every

\[
 2\le n<p,
\]

the reduced weight-`n` bar complex is exact.

### Proof

For every `1<=j<n<p`,

\[
 [j]_\zeta\ne0.
\]

Hence every Gaussian binomial occurring in a merge of a composition of `n` is nonzero. Rescaling the basis vector attached to a composition by the product of its quantum factorials conjugates every merge coefficient to `1`.

Compositions of `n` are in bijection with subsets of the `n-1` possible cut positions. Under this identification, the bar differential is the signed operation of deleting a cut. The resulting complex, including the empty cut set, is the augmented simplicial chain complex of an `(n-2)`-simplex and is exact. \(\square\)

Thus the scalar quantum-shuffle system has no lower resonance.

## 3. The first resonance at total degree `p`

For `0<a<p`,

\[
 {p\brack a}_\zeta=0,
\]

because `[p]_zeta=0` while all denominator quantum factorials are nonzero.

If a composition of `p` has at least three parts, merging any adjacent pair produces a sum strictly below `p`, so that merge coefficient remains nonzero. The only vanishing bar maps are therefore the final maps

\[
 (a,p-a)\longrightarrow(p).
\]

### Theorem 3.1 — two-line theorem

The weight-`p` bar homology is exactly

\[
 \boxed{
 \dim H_r(B_p(A_\zeta))=
 \begin{cases}
 1,&r=1,\\
 1,&r=2,\\
 0,&r\ge3,
 \end{cases}
 }
\]

where `r` denotes composition length, equivalently two adjacent bar degrees survive.

### Proof

As below degree `p`, rescale every composition of length at least two so that all merges whose target still has length at least two have coefficient `1`.

The subcomplex on compositions of length at least two is then the ordinary simplicial chain complex on the nonempty subsets of the `p-1` cut positions, with no augmentation to the empty subset. This is the unaugmented chain complex of a simplex. It has one-dimensional homology in degree zero and no higher homology. In composition-length grading this is the single line at length two.

The singleton composition `(p)` is isolated because every incoming Gaussian binomial is zero. It supplies the second line at length one. No other homology survives. \(\square\)

## 4. Interpretation

The terminal scalar resonance is neither a large uncontrolled bar complex nor an exact complex. It is the virtual difference of two one-dimensional terminal classes in adjacent degrees.

This is the precise combinatorial shape of a punctured oscillator:

\[
 \boxed{
 \text{Tate line}-\text{trivial line}.
 }
\]

The theorem itself does not assign Frobenius weights. If the length-one class receives the oscillator Tate normalization `(-m)`, with

\[
 m=\frac{p-7}{2},
\]

and the adjacent class remains untwisted, its virtual realization is exactly

\[
 \mathbf Q_\ell(-m)-\mathbf Q_\ell,
\]

which is the actual Pascal oscillator class proved independently.

## 5. Independent alignment with the repository

Three separate calculations now have the same terminal two-step shape:

1. the modular normal Jordan block has one Tate line in each parity;
2. the Dwork/Hasse elimination has two terminal elementary `p`-divisors;
3. the order-`p` scalar quantum bar complex has two adjacent one-dimensional homology groups.

This alignment is structural evidence for a common terminal resonance. It is not yet an identification theorem.

## 6. Exact remaining comparison

A successful bar-complex route must construct a functorial comparison

\[
 \boxed{
 \text{wild Artin--Schreier divided-power nearby cycles}
 \longrightarrow
 B_p(A_\zeta)
 }
\]

that:

1. sends the two terminal bar lines to the actual Pascal punctured oscillator;
2. preserves Frobenius and supplies the Tate gap `m`;
3. intertwines the cyclic trivial-minus-nontrivial projector;
4. identifies the nonscalar `C_wedge` and sparse-section pieces with the invariant/quadratic q-line residual and finite boundary cones.

The scalar theorem proves that no additional combinatorial homology is hidden at the first resonance. The remaining difficulty is geometric realization and control of the nonscalar residual.

## 7. Ruling

### Proved

- exactness of the scalar quantum bar complex in every total degree below `p`;
- exactly two one-dimensional terminal classes at total degree `p`;
- uniqueness of the first scalar order-`p` resonance.

### Not proved

- identification with the wild Fourier--Cayley complex;
- Frobenius weights of the two lines;
- cancellation of the middle-hook `C_wedge` residual;
- the crown.

The theorem reduces the candidate quantum-bar mechanism to a two-line terminal skeleton, but the new geometric comparison remains theorem-level mathematics.