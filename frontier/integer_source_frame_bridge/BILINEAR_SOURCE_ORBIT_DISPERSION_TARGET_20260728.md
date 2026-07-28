# Bilinear source--orbit dispersion target

Date: 28 July 2026  
Status: exact additive expansion and negligible deterministic correction proved; bilinear cross-modulus estimate open.

## 1. Local discrepancy

For a primorial centre `P_j`, prime modulus `z_j<r<=H`, candidate set
`mathcal P_{z_j}(H)`, and natural Euler weight `b_{j,m}`, put

\[
B_j=\sum_{m\in\mathcal P_{z_j}(H)}b_{j,m},
\]

\[
T_{j,r}(a)=
\sum_{m\in\mathcal P_{z_j}(H)}b_{j,m}e(am/r),
\]

and

\[
\Delta_{j,r}
=
\sum_{r\mid P_j+m}b_{j,m}
-
\frac1{r-1}
\sum_{m\ne r}b_{j,m}.
\]

Additive orthogonality gives

\[
\sum_{r\mid P_j+m}b_{j,m}
=
\frac1r
\sum_{a\bmod r}T_{j,r}(a)e(aP_j/r).
\]

### Theorem 1.1

One has exactly

\[
\boxed{
\Delta_{j,r}
=
\frac1r
\sum_{a=1}^{r-1}
T_{j,r}(a)e(aP_j/r)
+
\frac{rb_{j,r}-B_j}{r(r-1)}.
}
\tag{1.1}

Here `b_{j,r}=0` when `r` lies outside the candidate source.

### Proof

The zero additive mode is `B_j/r`, while

\[
\frac1{r-1}\sum_{m\ne r}b_{j,m}
=
\frac{B_j-b_{j,r}}{r-1}.
\]

Subtract and simplify.  \(\square\)

## 2. Fourier and deterministic pieces

Define

\[
U_{j,r}
=
\frac{r-1}{r(r-2)}
\sum_{a=1}^{r-1}
T_{j,r}(a)e(aP_j/r)
\tag{2.1}
\]

and

\[
C_{j,r}
=
\frac{rb_{j,r}-B_j}{r(r-2)}.
\tag{2.2}
\]

Then the locally centred first-order contribution satisfies

\[
\frac{r-1}{r-2}\Delta_{j,r}=U_{j,r}+C_{j,r}.
\tag{2.3}

The physical first-order term is the negative sum of (2.3).

## 3. The deterministic correction is negligible

The natural weights obey

\[
|b_{j,m}|\ll\log X,
\qquad
|B_j|\ll H.
\]

The prime reciprocal estimates

\[
\sum_{X<r\le H}\frac1r\ll1,
\qquad
\sum_{r>X}\frac1{r^2}\ll\frac1{X\log X}
\]

give

\[
\begin{aligned}
\left|\sum_{z_j<r\le H}C_{j,r}\right|
&\ll
\sum_{X<r\le H}\frac{|b_{j,r}|}{r}
+
|B_j|\sum_{r>X}\frac1{r^2}\\
&\ll
\log X+
\frac{H}{X\log X}\\
&\ll
\frac X{\log X}.
\end{aligned}
\tag{3.1}

Therefore

\[
\boxed{
\sum_{j<N}
\left|\sum_rC_{j,r}\right|^2
\ll
\frac{NX^2}{(\log X)^2}
=o(NHX).
}
\tag{3.2}

The correction is not part of the load-bearing estimate.

## 4. Exact cross-modulus Fourier form

Let

\[
U_j=\sum_{z_j<r\le H}U_{j,r}.
\]

Then

\[
\sum_j|U_j|^2
=
\sum_j\sum_{r,s}U_{j,r}\overline{U_{j,s}}.
\]

The diagonal `r=s` is controlled by the first-order diagonal theorem.  The
off-diagonal is exactly

\[
\boxed{
\begin{aligned}
\mathcal O_{X,\mathrm{Fourier}}^{(1)}
={}&
\sum_j
\sum_{\substack{z_j<r,s\le H\\r\ne s}}
\frac{(r-1)(s-1)}{rs(r-2)(s-2)}\\
&\times
\sum_{a=1}^{r-1}
\sum_{b=1}^{s-1}
T_{j,r}(a)\overline{T_{j,s}(b)}
 e\!\left(P_j\left(\frac ar-\frac bs\right)\right).
\end{aligned}
}
\tag{4.1}

This is the exact bilinear source--orbit dispersion form.

## 5. Expanded source form

Inserting the definitions of `T` gives

\[
\boxed{
\begin{aligned}
\mathcal O_{X,\mathrm{Fourier}}^{(1)}
={}&
\sum_j
\sum_{r\ne s}
\frac{(r-1)(s-1)}{rs(r-2)(s-2)}\\
&\times
\sum_{m,n}
b_{j,m}\overline{b_{j,n}}
\sum_{a=1}^{r-1}
\sum_{b=1}^{s-1}
 e\!\left(
\frac{a(P_j+m)}r-
\frac{b(P_j+n)}s
\right).
\end{aligned}
}
\tag{5.1
}

All source sums are over candidate primes.  The additive sums in (5.1) are
centred complete residue indicators; expanding them before preserving the
subtractions recreates the positive-sieve loss.

## 6. Dyadic target

For dyadic `R,S` with

\[
X<R,S\le H,
\]

let `mathcal O_X(R,S)` be the part of (4.1) with `r asymp R` and `s asymp S`.
The required physical first-order theorem is

\[
\boxed{
\sum_{R,S}\mathcal O_X(R,S)
\ll
NHX\,L_1(X),
\qquad
L_1(X)=o(\log X).
}
\tag{6.1}

The sum must be recombined with its signs; an absolute dyadic sum is stronger and
is not required.

## 7. Parameter boundary

The source length is

\[
H\asymp X^2,
\]

while the moduli occupy the full range

\[
H^{1/2}<R,S\le H.
\]

Classical Bombieri--Vinogradov reaches the lower endpoint.  Current fixed-depth
bilinear and trilinear Kloosterman-fraction estimates provide savings in selected
dyadic subranges but do not directly cover the entire form (4.1), because:

1. the source is restricted to a microscopic prime interval;
2. the residue class moves along the primorial prefix orbit;
3. both modulus variables must remain coupled;
4. the signed centring is load-bearing.

## 8. Relation to the martingale route

Equation (4.1) is the physical first-order component of the broader deterministic
Buchstab-martingale sampling theorem.  Proving (6.1) would close that component,
but the normalized `H`-rough coordinate and the ordered tail increments would
still have to be reinserted with their cross covariance.

Conversely, a direct proof of the full martingale sampling theorem would subsume
(6.1) and is now the preferred final architecture.

## 9. Boundary

Proved exactly:

1. additive decomposition (1.1);
2. negligible deterministic correction (3.2);
3. bilinear source--orbit form (4.1)--(5.1).

Already proved:

1. the `r=s` diagonal is `O(NHX/log X)`.

Open:

1. the signed cross-modulus bound (6.1);
2. its coupling to the rough coordinate and tail martingale;
3. Fortune's conjecture.
