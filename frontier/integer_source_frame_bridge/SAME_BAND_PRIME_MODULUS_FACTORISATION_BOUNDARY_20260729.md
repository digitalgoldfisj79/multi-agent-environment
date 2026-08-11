# Same-band prime-modulus factorisation boundary

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: after restoring the correct first-band diagonal boundary, the actual lower-band obstruction is the coherent sum across physical prime moduli. Its exact character representation is non-factorized. Every scalar source/centre split incurs at least the full square of the number of moduli, so sequential large-sieve/frame arguments necessarily reproduce the previously observed modulus-count loss. The lower physical band also lies strictly above the square-root level of the source interval. A genuinely joint moving-residue cross-modulus theorem remains open. Fortune's conjecture remains **OPEN**.

## 1. Restored target

For the frozen first physical band, the one-residue coordinate is exactly

\[
E_{j,p}=-a_{j,p}.
\]

The diagonal

\[
\sum_{j,p}|E_{j,p}|^2
\]

is already controlled. The open quantity is

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{p\in\mathcal P_R}E_{j,p}
\right|^2.
}
\]

Equivalently, this is the signed same-band covariance theorem `SBD(X)`.

## 2. Exact first-order character synthesis

For the common prime source, put

\[
S_p(\chi)=\sum_{m\in\mathcal M_Z\setminus\{p\}}\chi(m).
\]

The one-residue identity gives

\[
E_{j,p}
=-\frac{\beta_j}{p-2}
\sum_{\substack{\chi\bmod p\\\chi\ne\chi_0}}
\overline{\chi(-P_j)}S_p(\chi).
\]

Hence the complete band is

\[
\sum_{p\in\mathcal P_R}E_{j,p}
=-\beta_j
\sum_{p\in\mathcal P_R}
\frac1{p-2}
\sum_{\chi\ne\chi_0\bmod p}
\overline{\chi(-P_j)}S_p(\chi).
\]

The source transform and the primorial-centre phase share the coefficient `1/(p-2)`. The same-band theorem requires their joint action before either side is diagonalized positively.

## 3. Exact scalar factorisation no-go

Suppose one attempts a scalar split

\[
\frac1{p-2}=u_pv_p
\]

and then applies separate source and centre Cauchy inequalities.

The character multiplicity at `p` is `p-2`. The two diagonal masses are therefore

\[
\mathfrak C(u)=
\sum_{p\in\mathcal P_R}(p-2)|u_p|^2,
\qquad
\mathfrak S(v)=
\sum_{p\in\mathcal P_R}(p-2)|v_p|^2.
\]

Put

\[
x_p=(p-2)|u_p|^2.
\]

Since `u_pv_p=1/(p-2)`, one has

\[
(p-2)|v_p|^2=x_p^{-1}.
\]

Thus, with `M_R=|\mathcal P_R|`, Cauchy gives the sharp lower bound

\[
\boxed{
\mathfrak C(u)\mathfrak S(v)
=
\left(\sum_px_p\right)
\left(\sum_px_p^{-1}\right)
\ge M_R^2.
}
\]

Equality occurs when all `x_p` are equal.

Consequently every scalar redistribution of the coefficient reproduces at least the complete modulus-count loss

\[
M_R\asymp\frac R{\log R}
\]

at the norm level. This is the additive first-order analogue of the multiplicative all-Euler factorisation no-go already proved on the branch.

## 4. Square-root-level geometry

At Fortune scale

\[
H=\eta X^2,
\qquad 0<\eta<1,
\]

and on the first physical band `p>X`. Therefore

\[
\boxed{p>X>\sqrt H.}
\]

The moving-residue progression problem is not inside the usual Bombieri--Vinogradov range `Q\le\sqrt H/(\log H)^B`. It sits at a fixed factor beyond the square-root barrier.

This does not prove that `SBD(X)` is as strong as Elliott--Halberstam. It does show why a mechanical appeal to the classical level-`1/2` theorem cannot cover the relevant band.

## 5. Why the known diagonal technologies do not close the theorem

A sparse-modulus large sieve or a Barban--Davenport--Halberstam theorem controls expressions of the form

\[
\sum_p|E_{j,p}|^2
\quad\text{or}\quad
\sum_p\sum_{a\bmod p}|E(p,a)|^2.
\]

Those are positive conductorwise or residuewise energies. The branch already controls the actual frozen diagonal more strongly.

The required expression instead contains

\[
2\Re\sum_{p<s}E_{j,p}\overline{E_{j,s}},
\]

followed by the average over the sparse primorial centres. The scalar no-go above proves that one cannot recover this signed covariance by splitting the source and centre systems and then applying the available diagonal estimates independently.

## 6. Conditional calibration

Two standard conjectural mechanisms would be sufficient in stronger forms:

1. an Elliott--Halberstam-type `L^1` estimate extending beyond `H^{1/2}` uniformly in the residue class would directly control the modulus sum for every `P_j`;
2. a Montgomery-strength individual progression estimate, at the expected square-root-per-residue scale and with uniform logarithmic control, would also make the coherent prime-modulus sum small enough.

By contrast, GRH combined only with triangle inequality over the `\asymp X/\log X` physical primes remains polynomially too large. The missing ingredient is average cancellation between distinct moduli, not merely individual control of each progression.

These conditional comparisons are calibration only. No conjectural input is used elsewhere in this note.

## 7. Correct next theorem

The lower-band theorem should be kept in its non-factorized form.

### `MRPMD(X)` — moving-residue prime-modulus dispersion

For the actual frozen prime source and primorial block, prove

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{p\in\mathcal P_R}
\frac{p-1}{p-2}
\left(
N_{P_j,Z}(p)-\frac{M_Z-1}{p-1}
\right)
\right|^2
\ll
D_{B,R}+E_{B,R},
}
\]

with a Fortune-scale dyadically summable error.

`MRPMD(X)` is exactly `SBD(X)` in the one-residue spectral coordinates. It is not an additional theorem.

A proof must exploit at least one genuinely joint feature:

- cancellation of prime-progression errors across distinct prime moduli;
- the primorial evolution of the moving residues `-P_j\pmod p`;
- the common prime source before character or modulus diagonalization;
- cancellation with higher survivor orders in the complete normalized band.

## 8. Verification

The committed exact verifier checks:

1. several scalar splits of `1/(p-2)`;
2. the identity between the local centre/source masses;
3. the sharp lower bound `\mathfrak C\mathfrak S\ge M_R^2`;
4. the strict geometry `\sqrt H<X` for representative rational `\eta<1`.

## 9. Boundary

**PROVED EXACTLY**

1. first-order character synthesis;
2. scalar source/centre factorisation lower bound `M_R^2`;
3. strict placement of the first physical band above `\sqrt H`.

**CLOSED**

1. sequential source and centre Cauchy/large-sieve estimates with a scalar coefficient split;
2. treating sparse-modulus BDH as though it controlled the coherent all-ones modulus vector;
3. classical Bombieri--Vinogradov as a black box for the actual first physical band.

**OPEN**

1. `MRPMD(X)` / `SBD(X)`;
2. a full-band normalized-survivor alternative preserving higher-order cancellation;
3. `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.
