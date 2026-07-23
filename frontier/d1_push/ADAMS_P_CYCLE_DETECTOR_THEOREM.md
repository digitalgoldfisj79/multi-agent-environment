# The pth Adams operation as the complete p-cycle detector

**Date:** 2026-07-23  
**Status:** exact representation-theoretic and trace-function identity for every prime `p`. It unifies the hook, cyclic-resolvent and root-incidence formulations.

## 1. Representation identity

Let `P` be the permutation representation of `S_p` on `p` letters and let

`P=1 direct_sum V`.

For a representation `R`, the `p`th Adams operation `Psi^p(R)` is defined on characters by

`chi_(Psi^p R)(g)=chi_R(g^p)`.

### Theorem APC.1

In the character ring of `S_p`,

`boxed(lambda_(-1)(V)=Psi^p(P)-P.)`

### Proof

Let `g` have cycle lengths `l_1,...,l_r`. Since `p` is prime and every `l_i<=p`, a point lying in a cycle of length `l_i` is fixed by `g^p` exactly when `l_i` is `1` or `p`.

Therefore

`chi_P(g^p)-chi_P(g)`

is zero unless `g` itself is one `p`-cycle, in which case it equals `p`.

On the other hand,

`chi_(lambda_(-1)(V))(g)=det(1-g|V)`

has the same values: it is zero when `g` has more than one cycle and equals

`product_(j=1)^(p-1)(1-zeta_p^j)=p`

on a `p`-cycle. Hence the characters agree on every conjugacy class.

Combining with `CYCLIC_RESOLVENT_HOOK_COLLAPSE_THEOREM.md` gives

`Psi^p(P)-P=Ind_(C_p)^(S_p)1-Ind_(C_p)^(S_p)psi.`

## 2. Fibrewise root-count identity

Let `f(X)` be a squarefree degree-`p` polynomial over `F_q`, and let `g` be its Frobenius permutation on the geometric roots. Then

`Tr(g|P)=# roots of f in F_q`,

`Tr(g^p|P)=# roots of f in F_(q^p)`.

Thus

`boxed(p 1_(f irreducible)`

`=#Z(f,F_(q^p)) - #Z(f,F_q). )`

Indeed, a root in `F_(q^p)` has degree dividing `p`, hence degree `1` or `p`; a degree-`p` factor of a degree-`p` polynomial is the whole polynomial.

The formula remains valid for the virtual p-cycle character at ramification-free fibres. Repeated-root boundary fibres are handled separately by the established weight-zero/boundary ledger.

## 3. Summed depressed-slice identity

For

`F_(c,d)(X)=X^p+aX^3+cX+d`

over `F_p`, summing APC.1 over `(c,d)` yields

`pN_a(p)`

`=sum_(c,d)[#Z(F_(c,d),F_(p^p)) - #Z(F_(c,d),F_p)].`

The first term is the root-incidence variety. The second is elementary because for each `x,c` there is a unique `d`; it equals `p^2` before the already isolated exceptional corrections. Equivalently, the non-base-field incidence count is exactly `pN_a(p)` as in MRN.1.

Applying the Moore determinant to the first term gives the one-variable semilinear reduction of `MOORE_ROOT_NEGATION_REDUCTIONS_THEOREM.md`.

## 4. Geometric meaning

The complete alternating configuration object is not an arbitrary virtual sum. It is the difference between:

1. the pth Adams operation on the original root permutation sheaf; and
2. the root sheaf itself.

Consequently the primitive middle obstruction is the part of one Adams difference remaining after the exact boundary, Kummer, pair and D contributions are removed.

This gives two equivalent architectures for the next theorem:

- cyclic quotient plus rank-one `C_p` twist;
- Adams-operation root incidence plus Moore/Artin–Schreier descent.

Any fixed-complexity model obtained from either architecture automatically represents the same `E_middle` trace.

## 5. Limitation

Adams operations need not preserve honest low-rank sheaves; `Psi^p(P)` is a virtual construction and can be realized through the pfold cyclic tensor power. APC.1 is therefore a structural compression, not yet a conductor bound.
