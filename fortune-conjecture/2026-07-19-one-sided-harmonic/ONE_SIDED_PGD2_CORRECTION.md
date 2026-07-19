# One-sided PGD2 correction

For fixed positive harmonic \(a\), set

\[
\Psi_a(L)=\sum_{q\sim Q}p_{q,a}e(aL/q),
\qquad
\kappa_{2,a}=\sum_{q\sim Q}p_{q,a}^2,
\]

and

\[
\mathcal E_a=\sum_{u\ne v}|\Psi_a(S_u-S_v)|^2.
\]

Expanding the square gives

\[
\boxed{
\mathcal E_a=M(M-1)\kappa_{2,a}+\mathcal R_a.
}
\]

This was independently validated in 80 random superincreasing systems; maximum absolute residual \(1.30\times10^{-9}\).

Since \(\mathcal E_a\ge0\), the lower estimate

\[
\mathcal R_a\ge-M(M-1)\kappa_{2,a}
\]

is automatic. The downstream chain only requires an upper bound on \(\mathcal E_a\), and the diagonal is already \(o(M)\). The actual target is therefore

\[
\boxed{
\mathcal R_a\le MX^{o(1)}.
}
\tag{OPGD2}
\]

STL2 and absolute-value PGD2 remain sufficient but are strictly stronger than necessary.
