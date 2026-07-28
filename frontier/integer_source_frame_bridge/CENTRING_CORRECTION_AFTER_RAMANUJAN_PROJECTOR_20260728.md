# Centring correction after the Ramanujan projector

Date: 28 July 2026  
Status: exact distinction and local-factor calculation proved; the Hardy--Littlewood source asymptotic remains conjectural/open at the required uniformity.

## 1. Two different objects

The exact Möbius--log/additive decomposition produces the zero-frequency term

\[
\mu_P^{(0)}
=-W_H\sum_{d\le P+H}\frac{\mu(d)\log d}{d}
=W_H+o(W_H).
\tag{1.1}
\]

Equation (1.1) is an exact algebraic Fourier zero mode followed by a classical
Mertens evaluation.  It is **not automatically the complete major-arc principal
term** of the shifted prime detector.

At the Cramer physical scale `H asymp (log P)^2`, coherent nonzero rational
frequencies can contribute a deterministic term of order `H`.  The primitive
Ramanujan projector makes this visible.

Therefore the earlier strategic identification

\[
\text{zero frequency}=\text{correct analytic centring}
\]

is retracted.  The exact identities using `mu_P^(0)` remain true, but a
Fortune-scale variance estimate around that centring is not expected unless the
coherent nonzero-frequency principal part is also removed.

## 2. Prime-pair singular series for a primorial gap

Let

\[
P=\prod_{r\le z}r.
\]

For the pair of linear forms

\[
m,
\qquad
P+m,
\]

the Hardy--Littlewood local factor at a prime `r` is

\[
\frac{1-\nu_r/r}{(1-1/r)^2},
\]

where `nu_r` is the number of distinct forbidden residues modulo `r`.

If `r|P`, the two forbidden residues coincide, so `nu_r=1`.  If `r` does not
divide `P`, then `nu_r=2`.  Hence the singular series is exactly

\[
\boxed{
\mathfrak S(P)
=
\prod_{r\le z}\frac r{r-1}
\prod_{r>z}\left(1-\frac1{(r-1)^2}\right).
}
\tag{2.1}
\]

Equivalently,

\[
\mathfrak S(P)
=2C_2
\prod_{3\le r\le z}
\frac{r-1}{r-2},
\tag{2.2}
\]

where `C_2` is the twin-prime constant.

The tail product in (2.1) tends to one, while Mertens' product theorem gives

\[
\prod_{r\le z}\frac r{r-1}
\sim e^\gamma\log z.
\]

Thus

\[
\boxed{
\mathfrak S(P)
\sim e^\gamma\log z.
}
\tag{2.3}
\]

This local-factor calculation and asymptotic are unconditional.  They do not
prove the corresponding prime-pair asymptotic.

## 3. Correct one-sided major-arc model

Prime outputs in the interval `P<m+P<=P+H` require the offset `m` to be prime in
the candidate range.  The Hardy--Littlewood model therefore predicts

\[
\boxed{
\mu_P^{\mathrm{HL}}(H)
=
\mathfrak S(P)
\int_z^H\frac{dt}{\log t}
}
\tag{3.1}
\]

for the one-sided von Mangoldt detector

\[
\sum_{2\le m\le H}\Lambda(P+m),
\]

up to lower-order endpoint and prime-power terms.

With

\[
H=\eta X^2,
\qquad
z\asymp X,
\qquad 0<\eta<1,
\]

one has

\[
\int_z^H\frac{dt}{\log t}
=\frac H{\log H}(1+o(1))
=\frac H{2\log X}(1+o(1)).
\]

Combining with (2.3) yields

\[
\boxed{
\mu_P^{\mathrm{HL}}(H)
=
\left(\frac{e^\gamma}{2}+o(1)\right)H.
}
\tag{3.2}
\]

Equation (3.2) is the correct local Hardy--Littlewood principal model.  Its use as
an asymptotic for every primorial centre is open.

## 4. Where the missing constant resides

The exact zero mode (1.1) is asymptotic to `H`, whereas (3.2) is asymptotic to

\[
\frac{e^\gamma}{2}H\approx0.890536\,H.
\]

The difference

\[
\left(\frac{e^\gamma}{2}-1\right)H
\]

is of main-term size.  It is supplied by coherent nonzero primitive rational
frequencies in the identity

\[
R_P
=
\sum_q\Gamma_{P+H}(q)
\sum_{(a,q)=1}\widehat w_q(a)e(aP/q).
\]

Consequently those low primitive frequencies are part of the principal term and
must not be estimated as random error individually.

## 5. Corrected smooth-subtracted baseline

The deterministic smooth divisor sector satisfies

\[
G_P(H)=(\log2+o(1))H.
\]

Subtracting it exactly leaves the same detector residual provided the principal
term is reduced by the same amount.  Using the correct local model gives

\[
\boxed{
\mu_P^{\mathrm{red,HL}}(H)
=
\mu_P^{\mathrm{HL}}(H)-G_P(H)
=
\left(
\frac{e^\gamma}{2}-\log2+o(1)
\right)H.
}
\tag{5.1}
\]

Numerically,

\[
\frac{e^\gamma}{2}-\log2
\approx0.197389>0.
\tag{5.2}
\]

Thus the smooth subtraction still leaves a positive main term, but the previously
recorded constant `1-log 2` is not the correct major-arc constant.

## 6. Correct residual target

The load-bearing residual must be centred by an explicit major-arc/Ramanujan
principal term `mu_P^pr` satisfying

\[
\mu_P^{\mathrm{pr}}
=
\mu_P^{\mathrm{HL}}+o(H)
\]

uniformly over the block.  The required variance theorem is

\[
\boxed{
\sum_j
\left|
\sum_{m\le H}\Lambda(P_j+m)-\mu_{P_j}^{\mathrm{pr}}
\right|^2
\ll NHX\,L(X),
\qquad L(X)=o(\log X).
}
\tag{6.1}
\]

The exact source-to-frame identity remains valid for any specified centring.  The
new obligation is to construct `mu_P^pr` from the coherent primitive frequencies,
not merely from the additive zero mode.

## 7. Consequences for earlier files

The following statements remain exact:

1. the Möbius--log source identity;
2. the additive zero-mode formula;
3. the smooth-sector identity and `log 2` asymptotic;
4. the primitive rational-frequency collapse;
5. the Ramanujan candidate projector.

The following strategic statements are corrected:

1. `mu_P^(0)=H+o(H)` is a zero-frequency baseline, not the full analytic
   principal term;
2. the smooth-subtracted major-arc constant is
   `e^gamma/2-log 2`, not `1-log 2`;
3. a variance estimate must retain the coherent low primitive frequencies inside
   the principal subtraction.

## 8. Boundary

Proved:

1. the singular-series formula (2.1)--(2.2);
2. the asymptotic (2.3);
3. the distinction between exact zero mode and full major-arc centring;
4. positivity of the corrected reduced constant (5.2).

Conjectural/open:

1. the uniform one-sided Hardy--Littlewood asymptotic (3.1) for every primorial
   centre;
2. construction and control of an explicit finite Ramanujan principal term with
   error `o(H)`;
3. the centred variance theorem (6.1);
4. Fortune's conjecture.
