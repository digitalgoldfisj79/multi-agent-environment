# R4 — exact Heath--Brown source audit

## Frozen identity

Let `mu_{<=z}(n)=mu(n)1_{n<=z}`. For every integer `J>=1` and `n<=z^J`,

\[
\boxed{
\Lambda(n)
=
\sum_{r=1}^{J}(-1)^{r-1}{J\choose r}
\bigl(\mu_{\le z}^{*r}*1^{*(r-1)}*\log\bigr)(n).
}
\]

A direct convolution proof is available. Put `A=mu_{<=z}*1`. Then `delta-A` vanishes at `1` and is supported on integers greater than `z`. Hence `(delta-A)^{*J}` is supported above `z^J`. Expanding

\[
\Lambda*\bigl(\delta-(\delta-A)^{*J}\bigr)
\]

gives the displayed formula because `log=Lambda*1`.

The committed verifier independently checks the identity on exact finite panels.

## Natural logarithmic-order choice

For output size

\[
N_X\asymp P_j=\exp((1+o(1))X)
\]

and the natural choice `J=K_b=Theta(log X)`, the cutoff is

\[
z=N_X^{1/J}
=
\exp\!\left(\Theta\left(\frac{X}{\log X}\right)\right),
\]

which is far larger than the offset length `H=X^2`. The identity therefore introduces truncated divisor variables directly into the one-offset-per-modulus range where interval progression averaging has disappeared.

## Attempt to force the cutoff below H

The condition `z<=H` requires

\[
J\ge J_{\min}:=
\left\lceil\frac{\log N_X}{\log H}\right\rceil
\sim\frac{X}{2\log X}.
\]

The absolute binomial coefficient mass of the identity is exactly

\[
\sum_{r=1}^{J}{J\choose r}=2^J-1.
\]

Thus at `J=J_min` the termwise coefficient mass is

\[
\exp\!\left(\Theta\left(\frac{X}{\log X}\right)\right),
\]

while the RUHL detector margin is only polynomially small, `asymp log X/X`.

Finite scale panels illustrate the dichotomy:

| X | K_b | J_min | J_min/K_b | log10(2^J_min) |
|---:|---:|---:|---:|---:|
| 1,000 | 26 | 73 | 2.81 | 21.98 |
| 10,000 | 36 | 543 | 15.08 | 163.46 |
| 100,000 | 46 | 4,343 | 94.41 | 1,307.37 |
| 1,000,000 | 56 | 36,192 | 646.29 | 10,894.88 |

This does not prove that cancellation among Heath--Brown terms is impossible. It proves that the termwise absolute source strategy loses the identity's essential cancellation before reaching the required modulus range. Preserving the full cancellation simply recombines the source to `Lambda`, returning the original selected-centre residual.

## Ruling

The frozen Heath--Brown identity does not produce a smaller independent norm satisfying RUHL:

- logarithmic order leaves source variables beyond `H`;
- order large enough to force `z<=H` has superpolynomial absolute coefficient mass;
- retaining cancellations returns the original signed prime source;
- the prime-power correction remains too large under the inherited trivial bound.
