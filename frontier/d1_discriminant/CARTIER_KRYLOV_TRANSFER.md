# Cartier--Krylov transfer and its exact Frobenius collapse

**Date:** 2026-07-22  
**Status:** exact theorem proved; the natural principal-part transfer route is shown to be algebraically equivalent to the existing Frobenius/Berlekamp indicator.

## 1. Setup

Let

`F(X)=X^p+h(X)`, `h(X)=aX^3+cX+d`,

where `p>=5` is prime and `a!=0`. Put

`A=F_p[X]/(F)`

and let `ell:A->F_p` be the coefficient of `X^(p-1)` in the unique representative of degree below p.

Use the signed power basis

`e_m=(-1)^m X^m`, `0<=m<=p-1`,

and the differential basis

`omega_v=X^(v-1)dX/F(X)`, `1<=v<=p`.

Let Q be the row-action matrix of Frobenius on A in the basis `e_m`, and let H be the full Cartier matrix

`H_(u,v)=[X^(pu-v)]F^(p-1)`.

## 2. Sparse residue Gram matrix

Define

`G_(m,v)=ell(e_m X^(v-1))`.

Equivalently,

`G_(m,v)=-Res_infinity(e_m omega_v)`.

Because `m+v-1<=2p-2`, at most one reduction by

`X^p=-aX^3-cX-d`

is required. The constant coefficient d cannot reach degree `p-1`. Hence:

### Theorem CKT.1

For `0<=m<=p-1` and `1<=v<=p`,

`G_(m,v)=(-1)^m (`

`  1_(m+v=p)`

` -a 1_(m+v=2p-3)`

` -c 1_(m+v=2p-1) ).`

Thus G is a signed anti-diagonal matrix with only two lower boundary diagonals. Reversing the columns makes it triangular. The reversal sign and the product of its signed diagonal entries cancel, giving

`boxed(det G=1).`

Its inverse R is equally sparse. In one-based row and column indices,

`R_(u,p-u+1)=(-1)^(p-u)`

for all u, together with the four additional entries

`R_(1,1)=c`, `R_(1,3)=a`, `R_(2,2)=-a`, `R_(3,1)=a`.

All other entries vanish.

## 3. Krylov matrix

Define

`K_(m,v)=[X^(-v)] h(X)^m/F(X)`

using the Laurent expansion at infinity.

Polynomial division and the residue pairing give

`K_(m,v)=ell(h^m X^(v-1))`.

In A one has `h=-X^p`, so

`h^m=(-1)^m X^(pm)=Phi(e_m)`.

Therefore

`K_(m,v)=ell(Phi(e_m)X^(v-1))`.

If Q is the Frobenius matrix in the signed power basis, this is the exact matrix identity

`boxed(K=QG).`

The rows of K are a genuine Krylov sequence. Multiplication by h on principal parts sends row m to row m+1. The resulting single-step operator is sparse, and its characteristic polynomial is

`-F(-Z)=Z^p+aZ^3+cZ-d`.

This explains the initially observed transfer structure.

## 4. Cartier--Frobenius adjunction

Frobenius on functions and Cartier on differentials are adjoint under the residue pairing. Since all coefficients lie in F_p,

`<Phi(q),omega>=<q,C(omega)>`

for the displayed bases. In matrices this is

`QG=GH`.

Combining this with `det G=1` gives:

### Theorem CKT.2

`boxed(H=G^(-1)QG=RK).`

Consequently

`boxed(I-H=G^(-1)(I-Q)G).`

This identity holds for every coefficient pair `(c,d)`, including singular members. No squarefreeness assumption is used.

## 5. Exact interpretation of the attempted transfer operator

The full Cartier matrix can also be recovered directly from the finite geometric expansion. Put `k=p-1-u` and `z=h/X^p`. Then

`H_(u,v)=(-1)^k [X^(-v)] h^k sum_(q=1)^u (-z)^q`.

The sum truncates at u because the binomial expansion of `F^(p-1)` contains at most `p-1` copies of h. Its geometric-series boundary term is exactly what produces the four corrections in R.

Thus the sparse transfer observed experimentally is not accidental. However, Theorem CKT.2 shows that it is simply the Frobenius operator written in the residue-dual basis.

## 6. No-go consequence for the crown programme

The ordinary Cartier cofactor and the exact Frobenius cofactor are related by determinant-one sparse changes of basis. In particular,

`adj(I-H)=G^(-1) adj(I-Q) G`.

Therefore a principal-part or Krylov transfer that retains the complete p-dimensional state cannot provide an independent evaluation of the crown sum. It preserves exactly the same rank-one-versus-corank-two distinction as the Berlekamp/Frobenius matrix.

This does **not** invalidate the Cartier cofactor theorem: the Cartier presentation remains the simplest pointwise coefficient formula. It does close the proposed transfer route in its natural form:

1. the transfer state has dimension p;
2. its Krylov matrix is `QG`;
3. the boundary matrix is `G^(-1)`;
4. their product is exactly H;
5. summing the selected cofactor still requires the same global cancellations as the Frobenius indicator.

A genuinely new transfer method would have to quotient the p-dimensional Frobenius module or sum coefficient orbits before constructing this Gram-conjugate operator. Merely reorganising powers of h cannot reduce the obstruction.

## 7. Verification

`cartier_krylov_transfer_check.py` is standard-library only. It checks:

- the explicit sparse formula for G;
- `det G=1`;
- the Frobenius matrix Q by direct polynomial reduction;
- the Cartier matrix H by direct expansion of `F^(p-1)`;
- the identity `H=G^(-1)QG`.

The verifier is exhaustive for every `a!=0,c,d` at `p=5,7` and checks a representative coefficient grid at `p=11`.
