# Fixed-class first Cartier moment and the cyclotomic tangent wall

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** the frozen simultaneous-residue target for function-field Fortune `d=1`.  
**Status:** the identities and counterexamples below are **PROVED**. The first-moment nonvanishing statement and the crown remain **OPEN**.

## 1. The first moment certificate

For

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad a\ne0,
\]

put

\[
M_a(p)=
\sum_{\substack{c,d\in\mathbf F_p\\F_{a,c,d}\text{ irreducible}}}c
\quad\text{in }\mathbf F_p.
\]

The general Cartier cofactor theorem gives pointwise

\[
C_1(F_{a,c,d})=c\,1_{F_{a,c,d}\text{ irreducible}},
\]

so

\[
\boxed{M_a(p)=\sum_{c,d}C_1(F_{a,c,d}).}
\]

Consequently `M_a != 0` is a sufficient certificate that the fixed class contains an irreducible polynomial. Unlike the count residue, its vanishing is not protected by the free involution `d -> -d`: at `p=5` the square class has `N_+=4` but `M_+=0`.

The exact scan already committed on the predecessor branch found

\[
M_a(p)\ne0
\]

for both square classes at every prime `5<=p<=379`, except the displayed `p=5` square-class case. This remains evidence only.

## 2. Translation-orbit identity

Consider the complete cubic family

\[
F_{a,b,c,d}(X)=X^p+aX^3+bX^2+cX+d.
\]

Translation `X -> X+t` sends a depressed representative `(0,c_0,d_0)` to

\[
b_t=3at,
\qquad
c_t=c_0+3at^2,
\qquad
 d_t=d_0+(c_0+1)t+at^3.
\]

Every irreducible translation orbit contains one depressed representative. On such an orbit,

\[
\sum_{t\in\mathbf F_p}b_t^{p-1}c_t
=
\sum_{t\ne0}(c_0+3at^2)
=-c_0.
\]

Therefore:

### Theorem 2.1 — full-family moment projector

\[
\boxed{
M_a(p)
=-\sum_{b,c,d}b^{p-1}c\,1_{F_{a,b,c,d}\text{ irreducible}}.
}
\]

Using either selected cofactor gives

\[
\boxed{
M_a(p)=-\sum_{b,c,d}b^{p-1}C_1(F_{a,b,c,d}),
}
\]

and

\[
\boxed{
3aM_a(p)=-\sum_{b,c,d}b^{p-1}c\,C_3(F_{a,b,c,d}).
}
\]

Let `C_j^can` be the canonical polynomial function of degree at most `p-1` in each of `b,c,d`. Finite-field orthogonality then yields the exact two-edge coefficient formula

\[
\boxed{
3aM_a(p)=
[b^0c^{p-2}d^{p-1}]C_3^{\rm can}
+
[b^{p-1}c^{p-2}d^{p-1}]C_3^{\rm can}.
}
\]

Equivalently,

\[
\boxed{
M_a(p)=
[b^0c^{p-1}d^{p-1}]C_1^{\rm can}
+
[b^{p-1}c^{p-1}d^{p-1}]C_1^{\rm can}.
}
\]

Thus the first moment is a pair of full-family Cartier boundary coefficients. It is not a single low-degree term of the depressed determinant.

## 3. Exact q-line form

For `c != 0`, use

\[
q=-3/c.
\]

If `A=chi(a)`, the corresponding normal-form reading is

\[
\varepsilon=A\chi(q).
\]

Let `I_epsilon(q)` be the exact irreducible constant-fibre count in that normal-form cell. Since `c=-3/q`, the `c=0` boundary contributes zero and:

### Theorem 3.1 — reciprocal q-line moment

\[
\boxed{
M_A(p)
=-3\sum_{q\in\mathbf F_p^*}q^{-1}I_{A\chi(q)}(q).
}
\]

The unweighted cell main term cancels because

\[
\sum_{q\ne0}q^{-1}=0.
\]

This cancellation does not turn the moment into an ordinary lower-weight `ell`-adic trace. The coefficient `q^{-1}` is an `F_p`-valued Hasse weight, not a rank-one characteristic-zero trace function. Additive or multiplicative Fourier expansion restores full nonzero-frequency support.

## 4. Cyclotomic tangent formula

Let `zeta` be a primitive `p`-th root of unity and put

\[
\pi=\zeta-1.
\]

Define the coefficient Fourier value

\[
\mathcal F_a
=
\sum_{c,d}1_{F_{a,c,d}\text{ irreducible}}\zeta^c.
\]

Since

\[
\zeta^c=1+c\pi\pmod{\pi^2},
\]

one has:

### Theorem 4.1 — first cyclotomic tangent

\[
\boxed{
\frac{\mathcal F_a-N_a(p)}{\pi}
\equiv M_a(p)\pmod\pi.
}
\]

The first moment is therefore the first integral cyclotomic derivative of the nonzero-frequency Fourier transform of the `p`-cycle indicator.

Geometrically, nonzero coefficient frequency is the cubic Airy transform, but irreducibility is represented by the `p`-fold cyclic convolution/Adams class. The tangent modulo `pi^2` depends on the integral lattice and extension data discarded by semisimplified Fourier cancellation. Hence the first-moment route lands on the already isolated integral cyclic Smith-defect wall; it does not reduce to the rank-two Airy trace alone.

## 5. Three-mode form including the Artin--Schreier boundary

Extend the moment function to `a=0` using the same cofactor sum. For

\[
X^p+cX+d,
\]

the only irreducible members are

\[
c=-1,
\qquad d\ne0,
\]

so

\[
M_0(p)=1
\quad\text{in }\mathbf F_p.
\]

For `a != 0`, scaling shows that `M_a` depends only on `chi(a)`. Therefore its canonical polynomial function in `a` has the exact form

\[
\boxed{
M(a)=1+U_pa^{p-1}+V_pa^{(p-1)/2}.
}
\]

The two class values are

\[
M_+=1+U_p+V_p,
\qquad
M_-=1+U_p-V_p.
\]

Thus simultaneous first-moment vanishing is equivalent to

\[
\boxed{U_p=-1,\qquad V_p=0,}
\]

or, equivalently, to the canonical function identity

\[
\boxed{M(a)=1-a^{p-1}.}
\]

This sharpens the moment failure condition but does not exclude it.

## 6. Weighted discriminant parity does not isolate the moment

One possible shortcut was that locally admissible reducible members with an odd number of factors might have zero total `c`-moment modulo `p`. Then the explicit discriminant-parity mass could isolate `M_a`.

This is false in both classes at every tested prime

\[
p=11,17,23,29,41,47,53.
\]

For example, the odd reducible `c`-moments are

\[
p=17:\quad16,14,
\]

\[
p=23:\quad19,14,
\]

\[
p=53:\quad32,50.
\]

All are nonzero in `F_p`. The corresponding odd reducible counts are also not generally divisible by `p`.

Therefore neither the unweighted nor first-moment discriminant parity mass separates irreducibles from the odd reducible strata.

## 7. Ruling

The first moment remains a valid sufficient certificate and a credible empirical target, but the currently available simplifications do not prove it.

### Proved

1. The full-family translation projector.
2. The two-edge canonical Cartier coefficient formula.
3. The reciprocal q-line formula.
4. The cyclotomic tangent formula.
5. The three-mode canonical form in the cubic coefficient.
6. Exact counterexamples to cancellation of weighted odd reducible strata.

### Closed as shortcuts

1. Extracting the moment from discriminant parity.
2. A natural cross-ratio pairing of q-line cells.
3. Treating the reciprocal weight as a bounded-rank `ell`-adic character.
4. Using the refuted small-prime Cartier support cutoff or a unique extremal assignment.

### Exact remaining theorem

A first-moment proof now requires an integral Fourier statement of the form

\[
\frac{\mathcal F_a-N_a}{\pi}\not\equiv0\pmod\pi
\]

for at least one cubic square class, or an equivalent direct nonvanishing theorem for the two Cartier boundary coefficients in Theorem 2.1.

That is a genuinely new first-order cyclotomic/Smith theorem. It is narrower than the full archimedean q-line trace estimate, but it is not supplied by ordinary semisimple Airy cancellation, parity, parameter averaging or the known Cartier support laws.

## 8. Verification

Run

```bash
python frontier/strategy/fixed_class_first_moment_verify.py
```

with `python-flint` installed. Frozen output:

`frontier/strategy/fixed_class_first_moment_results_20260726.json`.
