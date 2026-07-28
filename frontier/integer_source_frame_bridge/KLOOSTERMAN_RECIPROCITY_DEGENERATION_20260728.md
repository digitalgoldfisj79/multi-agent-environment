# Kloosterman-reciprocity degeneration of the quotient phases

Date: 28 July 2026  
Status: exact reciprocity identity and current-theorem parameter mismatch proved.

## 1. Phase from the rough-quotient sawtooth

The Fourier expansion of the exact quotient sawtooth produces phases

\[
e\!\left(\frac{h(P+t)}{qd}\right),
\qquad d\mid P,
\qquad (q,P)=1,
\qquad t\in\{z,H\}.
\tag{1.1}
\]

Separating the endpoint perturbation gives

\[
e\!\left(\frac{h(P+t)}{qd}\right)
=
e\!\left(\frac{h(P/d)}q\right)
 e\!\left(\frac{ht}{qd}\right).
\tag{1.2}
\]

Since `d` is invertible modulo `q`,

\[
P/d\equiv P\overline d\pmod q,
\]

and the first factor superficially has the form of a Kloosterman fraction.

## 2. Exact reciprocity degeneration

For coprime positive integers `d,q`, additive reciprocity gives

\[
\frac{\overline d}{q}
+
\frac{\overline q}{d}
\equiv
\frac1{dq}\pmod1.
\tag{2.1}
\]

### Theorem 2.1

If `d|P` and `(q,P)=1`, then for every integer `h`,

\[
\boxed{
 e\!\left(\frac{hP\overline d}{q}\right)
 =
 e\!\left(\frac{hP}{dq}\right).
}
\tag{2.2}
\]

### Proof

Multiply (2.1) by `hP`.  The term

\[
\frac{hP\overline q}{d}
\]

is an integer because `d|P`.  Its exponential is therefore one, leaving
(2.2).  \(\square\)

Thus the inverse phase is exactly the original hyperbolic phase; reciprocity does
not create an independent oscillatory variable.

## 3. Consequence for generic trilinear-fraction bounds

The Bettin--Chandee trilinear theorem applies to phases of the form

\[
e\!\left(\vartheta a\overline m/n\right)
\]

and contains the conductor factor

\[
\left(1+\frac{|\vartheta|A}{MN}\right)^{1/2},
\tag{3.1}
\]

where `m~M`, `n~N`, and `a~A`.

The literal identification for (2.2) is

\[
\vartheta=P,
\qquad m=d,
\qquad n=q,
\qquad a=h.
\]

On the physical polynomial ranges `d<=poly(X)`, `q<=H=poly(X)` and any nonzero
Fourier range `A>=1`, one has

\[
\frac{PA}{MN}=\exp((1+o(1))X),
\tag{3.2}
\]

up to polynomial factors.  The conductor factor in (3.1) therefore overwhelms
any power saving in the theorem.

One cannot replace `P` by a single small residue: the residue `P mod q` changes
with the denominator `q`, whereas the trilinear theorem requires one fixed
integer numerator parameter.

For divisor blocks large enough that `dq` is comparable to `P`, the conductor
factor ceases to be exponentially large, but those blocks belong to the
short-complementary/one-point quotient regime.  They do not provide the long,
dense coefficient ranges to which the generic trilinear theorem is designed to
apply.

## 4. Status of the 2026 fraction results

The following results do not directly close the present source:

1. Bettin--Chandee gives a valid arbitrary-coefficient trilinear bound, but the
   literal primorial numerator incurs (3.2).
2. Dong--Robles--Zeindler treats arbitrary bilinear coefficients, but the current
   arXiv record reports a missing factor in the claimed improvement; in any case
   the same fixed-numerator conductor mismatch remains.
3. Wright's partially fixed-modulus theorem concerns long dyadic convolutions
   with a Siegel--Walfisz coefficient sequence.  The quotient source instead has
   a microscopic hyperbolic strip, Möbius-supported primorial divisors and a
   one-point top tail.

These are technology-applicability statements, not assertions that no future
Kloosterman method can work.

## 5. Revised analytic target

Any useful reciprocal-fraction argument must exploit at least one feature absent
from the generic theorems:

1. the exact divisor relation `d|P`;
2. cancellation across the complete Möbius divisor system;
3. the consecutive-primorial centre average;
4. endpoint differencing in (1.1);
5. recombination with the sparse Euler/Buchstab tail.

Applying a generic arbitrary-coefficient fraction estimate to each divisor block
separately is not sufficient.

## 6. Boundary

Proved exactly:

1. reciprocity degeneration (2.2);
2. the exponential conductor mismatch (3.2) on polynomial divisor blocks;
3. the distinction between dense polynomial blocks and the one-point top tail.

Closed as a direct black-box route:

1. literal application of the currently stated generic bilinear or trilinear
   Kloosterman-fraction theorems to the sawtooth phase.

Open:

1. a primorial-specific signed reciprocal theorem;
2. deterministic centred sampling of the full quotient system;
3. Fortune's conjecture.
