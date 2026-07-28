# New-part Ramanujan-chaos collapse

Date: 28 July 2026  
Status: exact new-part identity and first-order/higher-order split proved; signed covariance estimate open.

## 1. Exact new-modulus residual

Use the exact smooth-primitive centring

\[
\mu_P^{\mathrm{prim}}(w)
=
\mu_P^{(0)}+
\sum_{q\mid P\atop q>1}
\Gamma_Z(q)
\sum_mw_mc_q(m),
\qquad Z=P+H.
\]

The centred source is exactly

\[
\mathcal E_P^{\mathrm{new}}(w)
=
\sum_{q\le Z\atop q\nmid P}
\Gamma_Z(q)
\sum_mw_mc_q(P+m).
\tag{1.1}
\]

Only squarefree `q` contribute.

## 2. Unique smooth/new factorisation

For every squarefree `q` in (1.1), write uniquely

\[
q=q_0q_1,
\qquad
q_0=(q,P),
\qquad
q_0\mid P,
\qquad
(q_1,P)=1.
\tag{2.1}
\]

Since `q` does not divide `P`, one has `q_1>1`.  Ramanujan sums are
multiplicative, and `q_0|P`, so

\[
c_q(P+m)=c_{q_0}(m)c_{q_1}(P+m).
\tag{2.2}
\]

For squarefree `q_1>1` coprime to `P`, define the exact smooth-completed
coefficient

\[
\boxed{
\mathcal G_{P,Z}(q_1;m)
=
\sum_{q_0\mid P\atop q_0q_1\le Z}
\Gamma_Z(q_0q_1)c_{q_0}(m).
}
\tag{2.3}
\]

## 3. Exact new-part identity

### Theorem 3.1

One has exactly

\[
\boxed{
\mathcal E_P^{\mathrm{new}}(w)
=
\sum_{q_1>1\atop(q_1,P)=1}
\sum_m
w_m c_{q_1}(P+m)
\mathcal G_{P,Z}(q_1;m),
}
\tag{3.1}
\]

where the outer sum is restricted implicitly by `q_1<=Z` and squarefreeness.

### Proof

Apply the unique factorisation (2.1) to every primitive denominator in (1.1), use
(2.2), and interchange the finite sums over `q_0` and `m`.  The inner `q_0` sum
is exactly (2.3).  \(\square\)

This is an exact identity: all smooth factors attached to the same genuinely new
part have already recombined before estimation.

## 4. Bulk candidate projection

Fix `delta>0`.  In the long-complementary range

\[
q_0q_1\le P^{1-\delta},
\]

the primitive coefficient satisfies

\[
\Gamma_Z(q_0q_1)
=
\frac{\mu(q_0q_1)}{\varphi(q_0q_1)}+	ext{negligible error}.
\]

For `q_1<=P^{1-3delta}`, the complete `q_0` sum can be restored with a
pointwise negligible tail.  The exact primorial projector then gives

\[
\boxed{
\mathcal G_{P,Z}(q_1;m)
=
\frac P{\varphi(P)}
\mathbf1_{(m,P)=1}
\frac{\mu(q_1)}{\varphi(q_1)}
+	ext{negligible error}.
}
\tag{4.1}
\]

In the physical range, `(m,P)=1` is exactly the candidate-prime condition.
Therefore the bulk of (3.1) is

\[
\boxed{
\frac P{\varphi(P)}
\sum_{z<m\le H\atop m\text{ prime}}w_m
\sum_{q_1>1\atop(q_1,P)=1}
\frac{\mu(q_1)}{\varphi(q_1)}c_{q_1}(P+m),
}
\tag{4.2}
\]

with the stated bulk cutoff and a rigorously controlled coefficient/projector
error.

## 5. Centred local factor

For a new prime `r>z`, define

\[
\boxed{
\lambda_r(n)
=
\frac1{r-1}
-
\frac r{r-1}\mathbf1_{r\mid n}.
}
\tag{5.1}
\]

Then

\[
\lambda_r(n)
=
\frac{\mu(r)}{\varphi(r)}c_r(n).
\tag{5.2}
\]

Indeed, if `r` does not divide `n`, both sides equal `1/(r-1)`; if `r|n`, both
sides equal `-1`.

For squarefree `q_1` with all prime factors new,

\[
\boxed{
\frac{\mu(q_1)}{\varphi(q_1)}c_{q_1}(n)
=
\prod_{r\mid q_1}\lambda_r(n).
}
\tag{5.3}
\]

Thus the new-modulus source is a signed multiplicative chaos built from locally
centred divisibility coordinates.

## 6. First-order versus sparse higher order

Assume

\[
H<(z^+)^2.
\]

### Theorem 6.1

Every squarefree `q_1<=H` coprime to `P` is either `1` or a single prime
`r>z`.

### Proof

Every prime factor of `q_1` is at least `z^+`.  Two such factors would give
`q_1>=(z^+)^2>H`.  \(\square\)

The `q_1=1` component has already been absorbed into the exact principal term.
Therefore the nontrivial polynomial new-part range is exactly the first-order
chaos

\[
\boxed{
\sum_{z<r\le H\atop r\text{ prime}}
\lambda_r(P+m).
}
\tag{6.1}
\]

Every higher-order new part has

\[
q_1>H.
\]

For fixed `(P,q_1)`, divisibility in the physical interval is then a one-point
condition.  Across the primorial block, the shrinking-target theorem controls the
centre multiplicity at exponential scales.

## 7. Correct signed architecture

After exact principal subtraction, the residual has two algebraic components:

1. **first-order new-prime chaos**, supported on prime denominators
   `z<r<=H`;
2. **higher-order sparse chaos**, supported on squarefree new products `q_1>H`.

These are not independent positive sectors.  For a composite output, the
higher-order terms cancel the first-order factor hits according to the exact
Ramanujan/Möbius expansion.  A proof must retain their cross covariance.

The required block estimate is therefore a joint signed chaos estimate:

\[
\boxed{
\sum_j
\left|
\mathcal E_{P_j}^{(1)}+
\mathcal E_{P_j}^{(\ge2)}+
\mathcal T_{P_j}
\right|^2
\ll NHX\,L(X),
\qquad L(X)=o(\log X),
}
\tag{7.1}
\]

where `mathcal T` is the top short-complementary coefficient tail.  The exact
definitions are inherited from (3.1) by partitioning `q_1` according to its number
of new prime factors and the coefficient-validity range.

## 8. Boundary

Proved exactly:

1. unique smooth/new denominator factorisation;
2. exact new-part identity (3.1);
3. centred local factor (5.1)--(5.3);
4. first-order classification for `q_1<=H`;
5. one-point nature of every higher-order new part.

Proved in the long-complementary bulk using previous theorems:

1. candidate-projected coefficient formula (4.1)--(4.2).

Open:

1. the joint first-order/higher-order signed covariance estimate;
2. the top coefficient tail;
3. the Fortune variance theorem and Fortune's conjecture.
