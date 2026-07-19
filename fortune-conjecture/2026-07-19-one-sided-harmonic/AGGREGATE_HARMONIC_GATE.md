# Aggregate-harmonic gate

Let

\[
m_a=\sum_{q\sim Q}p_{q,a}.
\]

For the normalized symmetric row measure,

\[
\sum_{a\ge1}m_a=\frac12,
\qquad
\Phi_X(L)=2\Re\sum_{a\ge1}\Psi_a(L).
\]

Weighted Cauchy--Schwarz gives

\[
\boxed{
|\Phi_X(L)|^2
\le
2\sum_{a\ge1}\frac{|\Psi_a(L)|^2}{m_a}.
}
\]

Hence

\[
\boxed{
\mathrm{PC\!-
FROB2}
\le
2\sum_{a\ge1}\frac{\mathcal E_a}{m_a}.
}
\]

A valid exact no-truncation aggregate target is

\[
\sum_{a\ge1}\frac{\mathcal E_a}{m_a}\ll MX^{o(1)}.
\tag{WAHF2}
\]

This does not create cancellation between harmonics: every \(\mathcal E_a\) is nonnegative. For the actual Gaussian weights \(p_{q,a}\propto\exp(-(Ha/q)^2/2)\), \(q/H\in[1,2]\), the positive harmonic mass has effective dimension 2.40; the unweighted aggregate kernel has effective dimension 1.10--2.15; and the weighted-Cauchy kernel has effective dimension 1.20--4.32. At most nine harmonics contain 99.99% of the weighted-kernel mass.

The aggregate reduction is a cleaner theorem boundary, but it is asymptotically a bounded-harmonic problem rather than a long numerator average.
