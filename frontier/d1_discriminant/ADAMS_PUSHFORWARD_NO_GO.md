# Adams-through-pushforward audit: exact no-go

**Date:** 2026-07-22  
**Status:** exact trace-level obstruction proved; targeted literature transplant rejected. The crown remains open.

## 1. Proposed mechanism

After the Cyclic Airy pre-cohomology shortcut failed, the remaining possible shortcut was to move the p-th Adams operation through compactly supported t-cohomology:

`R Gamma_c(U, psi^p L)  ?=  psi^p(R Gamma_c(U,L))`

up to a small Adams--Riemann--Roch correction supported at the ramification points.

Here `L` is the rank-p root local system on

`U=P^1_t minus {+1,-1,infinity}`.

If such a formula had an `O(p)` correction, it could pair the exponentially large even/odd hook cohomologies after pushforward.

## 2. The two sides have different exact trace formulae

Let `k=F_Q`, let `k_p=F_(Q^p)`, and let `F` be arithmetic Frobenius.

For a rational point `t in U(k)`, the Adams trace is

`Tr(F_t | psi^p L_t)=Tr(F_t^p | L_t).`

Therefore Grothendieck--Lefschetz gives

### Theorem APN.1

`boxed(Tr(F | R Gamma_c(U_bar,psi^p L))`
` =sum_(t in U(k)) Tr(F_t^p | L_t).)`

By contrast, applying the Adams operation after cohomology gives

`Tr(F | psi^p R Gamma_c(U_bar,L))`
` =Tr(F^p | R Gamma_c(U_bar,L))`.

A second application of Grothendieck--Lefschetz gives

### Theorem APN.2

`boxed(Tr(F | psi^p R Gamma_c(U_bar,L))`
` =sum_(t in U(k_p)) Tr(F_t^p | L_t).)`

The first sum is over base-field points only. The second is over all degree-p extension points.

Hence:

### Corollary APN.3

`R Gamma_c(U,psi^p L)` and `psi^p R Gamma_c(U,L)` cannot be identified by a correction supported only at the finitely many ramification points.

Their trace discrepancy contains the global contribution

`sum_(t in U(k_p) minus U(k)) Tr(F_t^p | L_t),`

whose support ranges over the full degree-p extension of the open curve.

## 3. Cyclic fixed points reproduce the same obstruction

The cyclic formula for `psi^p R Gamma_c(U,L)` uses the action of a p-cycle on

`R Gamma_c(U^p,L^(box p)).`

The fixed points of `F composed tau` are

`(t,Ft,...,F^(p-1)t)`,  `t in U(k_p)`.

They are not the geometric diagonal over `U(k)`. Thus the equivariant Lefschetz calculation gives Theorem APN.2, not Theorem APN.1.

Selecting only the rational diagonal would discard exactly the degree-p closed points responsible for the mismatch.

## 4. Why published Adams--Riemann--Roch theorems do not apply

The targeted literature audit found:

1. Pink--Roessler, *On the Adams--Riemann--Roch theorem in positive characteristic* (Math. Z. 270, 2012; arXiv:0812.0254), proves the p-th Adams--Riemann--Roch formula in algebraic K-theory for smooth projective morphisms in characteristic p.

2. Koeck, *The Grothendieck--Riemann--Roch theorem for group scheme actions* (Ann. Sci. ENS 31, 1998), treats equivariant algebraic K-theory of locally free coherent modules and projective schemes.

3. Maxim--Schuermann, *Plethysm and cohomology representations of external and symmetric products* (arXiv:1602.06546), gives cyclic and Schur-operation formulae for external products and virtual cohomology in suitable symmetric monoidal categories.

These results do not identify pointwise Adams on a constructible l-adic local system with Adams after the same-space compact-support pushforward.

The first two concern coherent/vector-bundle K-theory and Bott cannibalistic classes, not Weil trace functions of constructible l-adic sheaves. The third correctly produces external powers on `U^p`; its cyclic fixed-point formula therefore sums over `U(k_p)`, in agreement with Theorem APN.2.

No hypothesis adjustment converts that extension-point sum into the base-point sum of Theorem APN.1.

## 5. Consequence for the crown programme

The following route is closed:

> Commute the p-th Adams operation through t-cohomology and absorb the failure into an `O(p)` local tangent or boundary class.

The failure is not local. It is the arithmetic distinction

`U(F_Q)  versus  U(F_(Q^p)).`

Any successful derived cancellation theorem must therefore include a global projector selecting base-field points inside the degree-p extension trace formula, or an equivalent cancellation across degree-p closed points.

## 6. Exact surviving wall

The function-field crown still reduces to controlling

`R Gamma_c(U_bar, Lambda_p(L))`

as a virtual q-family. The canonical hook model has exponential even/odd dimensions, and neither of the two natural cyclic shortcuts removes them:

- Adams before pushforward: correct object, exponential effectivity;
- Adams after pushforward: smaller formal location, but wrong arithmetic point set.

The missing theorem can now be stated as:

### Base-point Adams cancellation theorem

Construct an explicit derived correspondence that transforms

`sum_(t in U(F_Q)) Tr(F_t^p | L_t)`

into an effective q-line complex of total rank `O(p)`, while cancelling the contribution of degree-p closed points that appears in ordinary cyclic Adams pushforward.

No theorem found in the targeted Adams--Riemann--Roch or constructible-sheaf symmetric-power literature provides this operation.

## 7. Stopping conclusion

The Airy/cyclic/Adams crown attack has reached a genuine theorem-level obstruction. Further manipulation of standard Adams operations, cyclic diagonals, or coherent Adams--Riemann--Roch formulae will reproduce one of the two exact failures above.

A materially new ingredient must distinguish base-field points from degree-p extension points inside a geometric pushforward, without paying exponential hook complexity.