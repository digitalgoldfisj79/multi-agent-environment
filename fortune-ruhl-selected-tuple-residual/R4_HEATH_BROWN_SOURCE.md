# R4 — exact Heath--Brown source audit

## Frozen identity

Let `mu_{<=z}(n)=mu(n)1_{n<=z}`. For every integer `J>=1` and `n<=z^J`,

\[
\boxed{
\Lambda(n)
=\sum_{r=1}^{J}(-1)^{r-1}{J\choose r}
\bigl(\mu_{\le z}^{*r}*1^{*(r-1)}*\log\bigr)(n).
}
\]

Put `A=mu_{<=z}*1`. Then `delta-A` vanishes at `1` and is supported on integers greater than `z`, so `(delta-A)^{*J}` is supported above `z^J`. Expanding

\[
\Lambda*\bigl(\delta-(\delta-A)^{*J}\bigr)
\]

gives the identity because `log=Lambda*1`. The committed verifier checks it on exact finite panels.

## Source-scale dichotomy

For output size

\[
N_X\asymp P_j=\exp((1+o(1))X)
\]

and `J=K_b=Theta(log X)`, the cutoff is

\[
z=N_X^{1/J}
=\exp\!\left(\Theta\left(\frac{X}{\log X}\right)\right),
\]

far larger than `H=X^2`. The identity therefore introduces divisor variables into the one-offset-per-modulus range where interval progression averaging is absent.

Forcing `z<=H` requires

\[
J\ge J_{\min}
=\left\lceil\frac{\log N_X}{\log H}\right\rceil
\sim\frac{X}{2\log X}.
\]

The absolute binomial coefficient mass is

\[
\sum_{r=1}^{J}{J\choose r}=2^J-1
=\exp\!\left(\Theta\left(\frac{X}{\log X}\right)\right)
\]

at `J=J_min`, while the RUHL detector margin is only polynomially small.

| X | K_b | J_min | J_min/K_b | log10(2^J_min) |
|---:|---:|---:|---:|---:|
| 1,000 | 26 | 73 | 2.81 | 21.98 |
| 10,000 | 36 | 543 | 15.08 | 163.46 |
| 100,000 | 46 | 4,343 | 94.41 | 1,307.37 |
| 1,000,000 | 56 | 36,192 | 646.29 | 10,894.88 |

## Correct termwise-absolute requirement

Let `R_r` be the normalized residual attached to the `r`th convolution term after all row and tuple averaging. A triangle-inequality implementation must prove

\[
\sum_{r=1}^{J}{J\choose r}|R_r|<\Delta_b.
\tag{HB}
\]

The coefficient mass alone does **not** prove that (HB) is impossible: the individual residuals might decay rapidly with `r` or `J`. What the scale ledger proves is the required accuracy burden. Coefficient-uniform or merely polynomially decaying term estimates cannot suffice once `J\asymp X/\log X`; a successful absolute source proof would need compensating `r`-dependent decay strong enough to overcome the binomial weights.

Preserving all signs recombines the identity algebraically to `Lambda`. This does not prove that signed source analysis is impossible. It means that any gain must come from a genuinely new estimate made before full recombination, not from the identity or its coefficient count alone.

## Ruling

The audited Heath--Brown calculation establishes:

- logarithmic order leaves source variables beyond `H`;
- forcing all truncated variables below `H` creates exponentially weighted residual control of the form (HB);
- no such residual theorem is supplied by the present programme;
- no universal impossibility theorem for termwise or signed Heath--Brown methods is claimed.

The correct terminal label is

`SOURCE_IDENTITY_REQUIRES_EXPONENTIALLY_WEIGHTED_RESIDUAL_CONTROL`.
