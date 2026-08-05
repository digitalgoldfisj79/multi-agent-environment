# M4 — selected-residue Barban–Davenport–Halberstam estimate

**Status:** `PASSED_FROM_CLASSICAL_BDH_AND_COLLISION_THEOREM`

Let `C` be a deterministic microblock with `R asymp X^rho` rows and let

\[
Q=X^{1+\delta},\qquad 0<\delta<1.
\]

For prime `q` with `2X<q<=Q`, every `P_j` is invertible modulo `q`. Put

\[
r_q(a)=\#\{j\in C:-P_j\equiv a\pmod q\}
\]

and

\[
E_q(a)=\vartheta(H;q,a)-\frac{H}{q-1}.
\]

The lower candidate cutoff contributes `O(Q(log X)^2)` after averaging and is negligible in the retained exponent range.

Classical Barban–Davenport–Halberstam gives

\[
\sum_{q\le Q}\sum_{(a,q)=1}|E_q(a)|^2
\ll H Q\log H
\]

in the range used here.

For two rows at index distance `d`, a collision modulo a prime `q>2X` implies

\[
q\mid \prod_{t=1}^{d}\ell_{j+t}-1.
\]

The number of such prime divisors exceeds neither

\[
\frac{\log(\prod_{t=1}^{d}\ell_{j+t}-1)}{\log(2X)}
\le (1+o(1))d.
\]

Summing over row pairs yields the exact-scale multiplicity estimate

\[
\sum_{2X<q\le Q}\sum_{a\bmod q}r_q(a)^2
\ll \frac{RQ}{\log Q}+R^3.
\]

Cauchy–Schwarz therefore gives

\[
\frac1R\left|
\sum_{2X<q\le Q}\log q
\sum_a r_q(a)E_q(a)
\right|
\ll
\frac{\log Q}{R}
\left(\frac{RQ}{\log Q}+R^3\right)^{1/2}
(HQ\log H)^{1/2}.
\]

Relative to the desired main scale `H log X`, the diagonal and collision pieces are respectively

\[
X^{\delta-\rho/2+o(1)}
\quad\text{and}\quad
X^{(\rho+\delta-1)/2+o(1)}.
\]

Both tend to zero exactly when

\[
\boxed{2\delta<\rho<1-\delta.}
\]

This is the registered selected-residue BDH range.