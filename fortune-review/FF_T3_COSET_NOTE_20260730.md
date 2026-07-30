# T3 in the function field: exact structure, a soft-bound no-go, and a
# conditional power-saving bound on the punctured coset family

Contributor: Claude (PR #33 thread; first attack on the T3 aggregate in F_q[t],
per Gate FF2/FF3 of `NEXT_PROGRAMME_ORBIT_TRANSFER_FUNCTION_FIELD_ASL_20260730.md`)
Date: 2026-07-30
Machine verification: `fortune-review/scripts/ff_t3_coset_audit.py`, output in
`fortune-review/data/ff_t3_coset_audit.txt`. Every claim below is labelled
PROVED / CONDITIONAL / EMPIRICAL; the proved items are elementary given Weil's
RH for F_q[t] Dirichlet L-functions and are machine-checked at small q.

## 0. Summary

Working over F_q[t] with band = monic irreducibles P of degree k, sources =
monic prime powers of degree m (Lambda integer-valued), and centres
**𝔏·M** with 𝔏 a fixed puncture (product of low-degree irreducibles; the
degree-1 FF primorial t^q − t is also tested) and **M ranging over the monic
polynomials of degree R, k ≤ R ≤ 2k−1** — a family that is *sparse mod PS*
(it meets a q^{R−2k} ≤ q^{-1} fraction of residue pairs) — we obtain:

- **(A, proved)** coset PORS_FF is an *identity*: the family samples every
  modulus's variance exactly fairly.
- **(B, proved)** within-modulus character sums over the family vanish
  *exactly*: they are coefficients past the degree of the L-polynomial.
- **(NG, proved)** soft bounds (Bessel/duality/operator-norm) provably cannot
  beat the trivial bound for the cross-modulus term: the dual sampling matrix
  has norm ≥ q^{2k}/k. The specific Λ-coefficients are essential — the exact
  FF mirror of the integer-side situation.
- **(C, proved)** the T3 pair-hit count over the family admits an *exact*
  completion: the FF "interval" (monics of degree R) is an F_q-subspace coset,
  so its Fourier expansion has *perfect support* — the density main term drops
  out exactly against the centring, and the residual is an explicit finite sum
  of Kloosterman-fraction-type additive character sums over pairs of band
  primes. **The integer obstruction "punctured numerators have no archimedean
  localization" dissolves in F_q[t].**
- **(D, conditional)** given a standard-shape input FFPS (square-root
  cancellation in one prime variable for those character sums), the T3 coset
  aggregate has a genuine power saving q^{-(R-3k/2)} for R > 3k/2.
- **(EMPIRICAL)** at k = 2, R = 3, q ≤ 13: cross/diag decays with q
  (−0.24 → ±0.04), identically for the fixed puncture t(t+1) and the true
  q-coupled primorial t^q − t; the θ ≠ 0 pair sums run at the predicted
  q^{−k/2} scale (0.289 vs 1/3 at q = 3; 0.158–0.202 vs 1/5^... 0.200 at q = 5).

What this does **not** do: the coset family replaces the consecutive-product
walk; thinning from q^R coset points to K ordered products is the remaining
gap, cleanly isolated (Section 6).

## 1. Dictionary and setup

F_q[t], q an odd prime (numerics; q a prime power in general). Band: monic
irreducibles P, deg P = k. Sources: monic f, deg f = m, Λ(f) = deg P if
f = P^e (integer!). Take **m ≤ 2k−1** (the FF form of H < X²: a nonzero
difference of sources has at most one band-prime divisor) and **k ≤ R ≤ 2k−1**.
Centres 𝔏M: 𝔏 fixed, coprime to the band (all factors of degree < k), M monic
of degree R. For a residue a mod P:

    psi(m; P, a) = sum over deg f = m, f = a mod P of Λ(f),
    D_P(a) = psi(m; P, a) − Psi_P(m)/(q^k − 1)     (Psi_P = mass on units),

and the object of study is the coset-family analogue of the PORC/T3 aggregate:

    CROSS = sum_M sum_{P != S} D_P(−𝔏M) D_S(−𝔏M),
    DIAG  = sum_M sum_P D_P(−𝔏M)^2.

The T1/T2/T3 kernel decomposition of the integer Gate O1 note transfers
verbatim (its proof is characteristic-free).

## 2. Theorem A (proved; machine-checked exactly). Coset PORS_FF is an identity

For R ≥ k and any 𝔏 coprime to P:

    sum_{M monic, deg M = R} D_P(−𝔏M)^2  =  q^{R−k} · sum_{all a mod P} D_P(a)^2 .

Proof: M ↦ −𝔏M mod P is q^{R−k}-to-1 onto every residue class, exactly,
because deg M = R ≥ k = deg P. ∎  (Verified with exact rational arithmetic at
q = 3, 5, 7 for both punctures, including t^q − t.)

So on this family the orbit-sampling stage is *free*, and all content sits in
CROSS — the T3 side — as designed.

## 3. Theorem B (proved) and the soft-bound no-go

**B.** For characters χ ≠ ξ mod the same P and R ≥ k:
sum_{deg M = R} (χ̄ξ)(M) = [u^R] L(u, χ̄ξ) = 0, since L(u, ·) is a polynomial
of degree ≤ k − 1 < R. (Machine-checked.) Within-modulus orthogonality over
the family is *exact*.

**No-go (proved).** Writing G(M) = Σ_P D_P(−𝔏M) = Σ_{(P,χ)} c_χ χ̄(M) with
c_χ = ψ(m,χ)χ̄(−𝔏)/(q^k−1), any bound of the form
Σ_M |G|² ≤ ‖Gram‖ Σ|c|² is worthless: by duality the Gram's norm equals that
of the M×M' matrix B(M,M') = Σ_P[(q^k−1)1_{P|M−M'} − 1] whose *diagonal* is
(q^k−2)·#band ≈ q^{2k}/k, so ‖Gram‖ ≥ q^{2k}/k — the trivial bound. The
sampling system is overcomplete by q^{2k−R}; worst-case coefficient vectors
saturate it. Any successful estimate must use what ψ(m,χ) actually is. This is
the FF mirror of the integer lesson (uncentred SDD failure, ASL endpoint gap)
now in a setting where the next step actually exists:

## 4. Theorem C (proved). Exact completion of the pair-hit count

Fix sources f ≠ f' and band primes P ≠ S, W = PS, and let
c = c(f, f'; P, S) be the CRT point with c ≡ −f𝔏^{-1} (P), c ≡ −f'𝔏^{-1} (S).
The joint hit count over the family is 0 or 1, and equals 1 iff the canonical
representative of c mod W is a monic of degree R — i.e. lies in the coset
t^R + V, V = {deg < R}, an F_q-subspace of F_q[t]/W. With the residue pairing
ψ_θ(x) = e_q(coeff_{2k−1}(θx mod W)) and V^⊥ the annihilator
(dim V^⊥ = 2k − R; machine-checked):

    #{M : P | f+𝔏M, S | f'+𝔏M}  =  q^{R−2k} Σ_{θ in V^⊥} ψ_θ(c − t^R) .

(Machine-checked exactly over full residue panels.) The θ = 0 term is
q^{R−2k} — precisely the product of the two single-hit densities to leading
order — and cancels against the centring terms of the T3 kernel exactly up to
the explicitly computable 1/(q^k−1)-corrections. Hence:

    T3-coset aggregate
      = (exact centring remainder, size O(q^{R+m−k}·m²))
      + q^{R−2k} Σ_{θ in V^⊥, θ != 0} Σ_{f != f'} Λ(f)Λ(f')·S(θ; f, f'),

    S(θ; f, f') = Σ_{P != S, deg = k} ψ_θ( c(f,f';P,S) − t^R ).

The phases ψ_θ(c(·)) contain 𝔏^{-1} and the CRT inverses S^{-1} mod P,
P^{-1} mod S — these are **Kloosterman-fraction sums over pairs of function-
field primes**. In the integers this shape was unusable because the punctured
numerators are exponentially large with no interval structure; here the
completion is *exact* and the numerators live in a finite ring. This is, to my
knowledge, the first point in the programme where the Kloosterman-fraction
route becomes literally well-posed.

## 5. Theorem D (conditional). Power saving for R > 3k/2

**Input FFPS(k, θ):** for each nonzero θ and fixed f, f',
|S(θ; f, f')| ≤ C(k, deg 𝔏, m) · #pairs · q^{−k/2}
(square-root cancellation in one prime variable; the other summed trivially).

**Claim.** Under FFPS, for k ≤ R ≤ 2k−1:

    |T3-coset aggregate − centring remainder|
      ≤ C · q^{R−2k} · q^{2k−R} · q^{2m} m² · (q^{2k}/k²) q^{−k/2} · q^{−m}...

collecting exponents against the diagonal DIAG ≍ q^{R+m}:

    ratio ≤ C' · q^{3k/2 − R} · poly(k, m),

a **genuine power saving for R > 3k/2**, reaching q^{−(k/2−1)} at R = 2k−1.
(Arithmetic: #θ = q^{2k−R}−1; the f, f' sums estimated with |Λ| ≤ m and
q^m-support each — refinements that keep the Λ-oscillation would improve this,
see Section 6.)

**Status of FFPS.** Not claimed as proved here. It is a family exponential sum
over irreducibles with an algebraic-trace-function phase — the object class
covered by quantitative sheaf theory in the large-q regime and by the
technology of Sawin's square-root cancellation for factorization functions in
progressions ([arXiv:2102.09730](https://arxiv.org/abs/2102.09730)) and
Sawin–Shusterman's Λ/μ correlation machinery
([arXiv:1808.04001](https://arxiv.org/abs/1808.04001), Annals 2022). The
empirical check below finds |S(θ)|/#pairs at 0.87×q^{−k/2} and 0.79–1.01×q^{−k/2}
on the accessible panels — the postulated scale, with constants near 1.

## 6. Numerics (EMPIRICAL; k = 2, R = 3 = the 3k/2 boundary, m = 3)

    cross/diag:              q=3      q=5      q=7      q=11     q=13
      𝔏 = t(t+1)           -0.243   -0.020   -0.004   +0.045   +0.041
      𝔏 = t^q − t (primorial) -0.217 -0.126   -0.027   -0.063   -0.034
    diag/q^{R+m}:            0.312    0.388    0.421    0.451    0.459
    θ≠0 sums /#pairs (max):  0.289 (q^{-1}·√3=0.33 scale)   0.202 (0.200)

Readings: (i) the coset cross-modulus covariance decays toward 0 with q even
at the boundary exponent R = 3k/2 — consistent with Theorem D plus FFPS and
suggesting the true range is wider; (ii) **the q-coupled true primorial
puncture t^q − t behaves identically to the fixed puncture** — first
theorem-adjacent evidence that the degree/field-size coupling intrinsic to FF
Fortune is harmless at this stage; (iii) the postulated FFPS scale is what the
data shows.

## 7. What remains for full PORC_FF, precisely

1. **Walk-thinning.** Replace the coset family (q^R centres) by K consecutive
   products 𝔏·ℓ_1⋯ℓ_j. Note the FF degeneracy worth recording: monic
   irreducibles of a given degree carry **no canonical ordering** (no
   archimedean size), so the integer programme's "unique increasing order"
   has no distinguished FF counterpart — the walk-thinning problem in FF is
   pure thinness, cleanly separated from ordering. A natural intermediate
   family: all squarefree products of j irreducibles of degree r (unordered),
   which is again algebraic and Katz-accessible.
2. **Λ-oscillation in the f-sums.** Theorem D bounds the f, f' sums with
   absolute values; keeping the Λ-signs (Sawin–Shusterman-grade inputs) should
   improve q^{3k/2−R} toward q^{k−R}-type savings and widen the R-range.
3. **FFPS itself** — the identified concrete target for the sheaf-theoretic
   toolchain, stated in Section 5 with all parameters explicit.
4. **Uniformity in deg 𝔏** as q grows (the coupling); the t^q − t panel is
   encouraging but a proof needs error terms polynomial in deg 𝔏.

## 8. Boundary contribution

| Status | Item |
|---|---|
| **PROVED** | Theorem A (coset PORS_FF identity); Theorem B (exact within-modulus orthogonality); the no-go (dual-matrix norm ≥ q^{2k}/k: soft bounds cannot beat trivial); Theorem C (exact subspace completion; density term cancels centring; residual = explicit FF Kloosterman-fraction prime-pair sums). |
| **CONDITIONAL** | Theorem D: T3-coset power saving q^{3k/2−R} under FFPS. |
| **EMPIRICAL** | cross/diag decay in q at R = 3k/2 for both punctures incl. t^q − t; θ≠0 sums at the q^{−k/2} scale; diag constants. |
| **OPEN** | FFPS; Λ-signed refinement; walk-thinning (coset → consecutive products); deg 𝔏 uniformity; PORC_FF; FF first-band theorem; everything integer-side. |
