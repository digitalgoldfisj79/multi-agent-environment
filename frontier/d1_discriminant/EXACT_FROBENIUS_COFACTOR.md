# Exact value of the reduced Frobenius cofactor

**Date:** 2026-07-21  
**Status:** exact theorem proved; this closes the scalar gap in `FROBENIUS_DETERMINANT.md`.

## 1. Setup

Let

`F(X)=X^p+aX^3+cX+d`, with `p>=5` prime and `a!=0`,

and put

`A=F_p[X]/(F)`.

Let `Phi:A->A` be Frobenius and let

`B=Phi-I`

in the power basis `1,X,...,X^(p-1)`. Delete column zero and row `p-3`; call the resulting determinant `J_a(c,d)`.

The earlier determinant note proved that this cofactor is nonzero exactly on irreducible squarefree members, but left its nonzero scalar unspecified. The scalar is exactly one.

## 2. The irreducible case

Assume F is irreducible. Then `A=F_(p^p)`. Frobenius has order p and its fixed space is one-dimensional. Therefore

`N=Phi-I`

is a nilpotent operator of rank `p-1` with one Jordan block of size p.

Its characteristic polynomial is `T^p`. For any matrix N with characteristic polynomial `T^p`, the adjugate identity gives

`adj(-N)=N^(p-1)`

because

`adj(TI-N)=sum_(j=0)^(p-1) T^(p-1-j)N^j`.

In characteristic p,

`(Phi-I)^(p-1)=I+Phi+...+Phi^(p-1)`.

The right side is the field-trace operator:

`x -> Tr_(F_(p^p)/F_p)(x) * 1`.

In the power basis its matrix is exactly

`e_0 t`,

where `e_0` is the constant coordinate column and t is the algebra-trace row. Hence

`adj(-B)=e_0 t`.

The cofactor obtained by deleting column zero and row `p-3` is therefore, with the sign convention used in the committed determinant code,

`J_a(c,d)=t_(p-3)=Tr(X^(p-3))`.

Newton identities give

`Tr(X^(p-3))=3a`.

Thus every irreducible member satisfies

`J_a(c,d)=3a`.

## 3. Reducible and nonreduced members

For an arbitrary finite F_p-algebra of the form `A=F_p[X]/(F)`, every Frobenius-fixed element is reduced: if a nilpotent n satisfies `n^p=n`, then iteration gives `n=0`. Consequently the Frobenius-fixed subspace has one copy of F_p for each distinct irreducible factor of F.

If F has at least two distinct irreducible factors, then

`dim ker(Phi-I)>=2`,

so every `(p-1)`-minor of B vanishes, including `J_a(c,d)`.

The only degree-p polynomial with exactly one distinct irreducible factor that is not itself irreducible would have the form

`F=(X-r)^p=X^p-r^p`,

because p is prime. This is impossible in the present slice since `a!=0`.

Therefore every nonirreducible member has at least two distinct factors and gives `J_a(c,d)=0`.

## 4. Exact indicator theorem

### Theorem EFC.1

For every prime `p>=5`, every nonzero `a in F_p`, and all `c,d in F_p`,

`J_a(c,d)=3a * 1_(F irreducible)`.

No squarefreeness hypothesis is needed.

Consequently

`sum_(c,d) J_a(c,d)=3a N_a(p)`

exactly in F_p, where `N_a(p)` is the number of irreducible members in the fixed-a slice.

This validates the determinant congruence scan and the two-mode reduction without an unproved normalization scalar.