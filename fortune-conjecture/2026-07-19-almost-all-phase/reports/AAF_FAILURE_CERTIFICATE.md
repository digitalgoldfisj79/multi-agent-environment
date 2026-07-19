# AAF failure certificate

## Status

**THEOREM.** This is an exact deterministic implication for all sufficiently large indices. It does not prove an almost-all result by itself.

Let

\[
P_n=p_n\#,
\qquad
y_n=p_{n+1}^2-2,
\qquad
h_n=y_n/2.
\]

If the fortunate number \(F_n\) is composite, then

\[
F_n\ge p_{n+1}^2.
\]

Hence none of \(P_n+2,\ldots,P_n+p_{n+1}^2-1\) is prime.

Define

\[
J_n=\int_{P_n+1}^{P_n+1+y_n/4}
|\psi(x+h_n)-\psi(x)-h_n|^2\,dx.
\]

Then, for all sufficiently large \(n\),

\[
\boxed{F_n\ \text{composite}\Longrightarrow J_n\ge y_n^3/64.}
\]

Consequently

\[
\boxed{
\#\{n\le N:F_n\text{ composite}\}
\le 64\sum_{n\le N}\frac{J_n}{y_n^3}+O(1).
}
\]

For each exponent \(k\ge2\), consecutive \(k\)-th powers near \(P_n\) are separated by \(\gg P_n^{1-1/k}\ge P_n^{1/2}\), which exceeds \(h_n\asymp(\log P_n)^2\). Thus the interval contains at most one \(k\)-th power. Its von Mangoldt weight is at most \(\log(2P_n)/k\), so total prime-power contamination is

\[
\ll \log P_n\log\log P_n=o(h_n).
\]

The integration range has length \(y_n/4\) and the error magnitude is at least \(h_n/2=y_n/4\), giving \(J_n\ge y_n^3/64\).

The shipped finite audit records the rigorous prime-power envelope divided by \(h_n\); it falls from approximately \(0.150\) at \(n=10\) to \(2.19\times10^{-4}\) at \(n=10{,}000\).
