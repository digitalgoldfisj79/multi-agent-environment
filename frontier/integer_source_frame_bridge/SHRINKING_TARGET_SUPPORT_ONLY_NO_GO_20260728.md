# Shrinking-target support-only no-go

Date: 28 July 2026  
Status: abstract obstruction proved; arithmetic covariance remains the required new ingredient.

## 1. Context

The Buchstab-martingale identity writes the tail correction as a sum of prime-indexed
increments

\[
T_j=\sum_{H<r\le Y_j}M_{j,r}.
\]

The primorial shrinking-target theorem controls the number of centres at which a fixed
large divisor column can hit the physical interval.  It does not, by itself, provide
orthogonality between different prime columns.

This note records the exact limitation of any argument using only column supports and
column norms.

## 2. Abstract support lemma

### Proposition 2.1

Let `v_1,...,v_K in C^N`.  Suppose only that

\[
|\operatorname{supp}(v_k)|\le S_k
\]

and

\[
\|v_k\|_2=a_k.
\]

Then no inequality stronger than

\[
\boxed{
\left\|\sum_{k=1}^K v_k\right\|_2^2
\le
\left(\sum_{k=1}^K a_k\right)^2
}
\tag{2.1}
\]

can follow from these data alone.  In particular, the square-sum estimate

\[
\left\|\sum_kv_k\right\|_2^2
\ll
\sum_k\|v_k\|_2^2
\tag{2.2}
\]

is false without additional phase, sign or overlap information.

### Proof

Choose one coordinate contained in every permitted support and take

\[
v_k=a_ke_1.
\]

Then every support and norm condition is satisfied, while equality holds in (2.1):

\[
\left\|\sum_kv_k\right\|_2^2
=
\left(\sum_ka_k\right)^2.
\]

The ratio to the right side of (2.2) can be as large as `K`.  \(\square\)

The same example works on a common support of any admissible positive size.

## 3. Why the near-physical tail gives no support saving

For a fixed divisor `d>H`, the shrinking-target visit gap is

\[
\Delta_X(d)
=
\left\lceil
\frac{\log(d/H)}{\log(2X)}
\right\rceil.
\]

Hence for the full range

\[
H<d\le2XH
\]

one has

\[
\Delta_X(d)=1.
\]

The corresponding support bound is only

\[
|V_d|\le N,
\]

which is the trivial full-block bound.  More generally, for

\[
H(2X)^{k-1}<d\le H(2X)^k,
\]

support sparsity improves only to approximately `N/k`.

Thus the polynomial ranges nearest to `H`—precisely where the Buchstab increment
weights are still logarithmic and numerous—cannot be controlled by column support
alone.

## 4. The baseline part is not sparse

The ordered increment has the form

\[
M_{j,r}
=
V[r,Y_j]
\left[
\frac{C_j(r^-)}{r-2}
-
\frac{r-1}{r-2}H_j(r)
\right],
\tag{4.1}
\]

where `C_j(r^-)` is the weighted count surviving earlier tail primes and `H_j(r)`
is the one-point divisor hit.  The hit term is a shrinking-target column, but the
baseline term `C_j(r^-)/(r-2)` is present at every centre.  Consequently even a
strong support theorem for the hits does not supply support sparsity for the centred
increment itself.

The baseline and hit must be kept together as a discrepancy.

## 5. Quantitative consequence

The complete-model quadratic variation gives the correct coefficient budget

\[
\sum_{j,r}\mathbb E|M_{j,r}|^2\ll NHX.
\]

A support-only Cauchy--Schwarz argument can multiply this budget by the number of
active prime scales or by a full-block support factor.  Either loss is much larger
than the permitted `o(log X)` loss.

Therefore the shrinking-target theorem is necessary for the far tail but is not a
standalone transference theorem.

## 6. Required replacement theorem

The missing input must use at least one of the following genuinely arithmetic
features:

1. cancellation of the locally centred prime-progression discrepancies;
2. multiplicative character phases `chi(P_j)` along the primorial prefix orbit;
3. reciprocal-difference cancellation between distinct prime moduli;
4. martingale conditional cancellation after averaging over the actual source grid;
5. an equivalent signed pair-correlation theorem.

Support size and coefficient mass alone cannot provide the result.

## 7. Boundary

Proved:

1. the abstract support-only obstruction;
2. absence of nontrivial support saving in the near-physical tail;
3. nonsparsity of the martingale baseline coordinate.

Still viable:

1. shrinking-target sparsity as one component of a signed arithmetic sampling proof;
2. far-tail column estimates where the visit gap tends to infinity.

Open:

1. the deterministic martingale sampling theorem;
2. the physical first-order cross-modulus covariance;
3. Fortune's conjecture.
