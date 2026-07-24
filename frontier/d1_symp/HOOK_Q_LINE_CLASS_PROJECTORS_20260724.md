# Exact q-line projectors for the two arithmetic coefficient classes

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** finite q-line assembly in the function-field `d=1` application theorem.  
**Status:** the identities below are **PROVED**. They reduce the final arithmetic assembly to two explicit q-line Frobenius traces plus `q=2` and `q=infinity` boundary counts.

## 0. Cell notation

For `q in F_p^*` and `epsilon in {+1,-1}`, let

\[
I_\varepsilon(q)
\]

be the number of irreducible constant fibres in the split or nonsplit normal-form cell from `NORMAL_FORM_CELL_LEDGER_20260724.md`.

For `q!=2`, let

\[
\mathcal H_{q,\varepsilon}
=
\sum_{i=0}^{p-1}(-1)^i
H_c^1(U_{q,\overline{F}_p},\mathcal L_{i,\varepsilon})
\]

be the post-fixed-`q` alternating hook `H^1` virtual module on

\[
U_q=\mathbf P^1_t\setminus\{+1,-1,\infty\}.
\]

Put

\[
E_\varepsilon(q)
=
\operatorname{Tr}(F|\mathcal H_{q,\varepsilon}).
\]

## 1. Exact fixed-cell trace formula

The virtual hook local system has trace `p` on a `p`-cycle and zero on every other Frobenius cycle type. Therefore

\[
\sum_{t\in U_q(F_p)}
\operatorname{Tr}(F_t|\mathcal L_{hook,\varepsilon})
=pI_\varepsilon(q).
\]

The virtual local system has generic rank zero. Its only geometric invariant line is the `V_0` line, so

\[
H_c^2(U_q,\mathcal L_{hook,\varepsilon})
=\mathbf Q_\ell(-1)
\]

virtually, with Frobenius trace `p`; `H_c^0` vanishes. Grothendieck--Lefschetz gives

\[
\boxed{
pI_\varepsilon(q)
=p-E_\varepsilon(q)
\qquad(q\ne2).
}
\]

This is the general exact form of the small-prime formula used in the hook spectra.

## 2. Arithmetic-class selection

Let

\[
A=\chi(a)\in\{+1,-1\}
\]

be the square class of the cubic coefficient in

\[
X^p+aX^3+cX+d.
\]

The normal-form cell ledger proves that at `q=-3/c`, the required reading is

\[
\varepsilon=A\chi(q).
\]

Define the two boundary counts

\[
B_A
=
I_A(\infty)+I_{A\chi(2)}(2).
\]

Then

\[
N_A(p)
=B_A+
\sum_{q\in F_p^*\setminus\{2\}}
I_{A\chi(q)}(q).
\]

Using the fixed-cell trace formula,

\[
\boxed{
N_A(p)
=(p-2)+B_A
-
\frac1p
\sum_{q\in F_p^*\setminus\{2\}}
E_{A\chi(q)}(q).
}
\]

This is the exact generic-plus-boundary q-line ledger for either arithmetic class.

## 3. Constant and quadratic q-line projectors

Define

\[
S_0
=
\sum_{q\in F_p^*\setminus\{2\}}
\left(E_+(q)+E_-(q)\right)
\]

and

\[
S_\chi
=
\sum_{q\in F_p^*\setminus\{2\}}
\chi(q)
\left(E_+(q)-E_-(q)\right).
\]

For `A=+1` or `-1`,

\[
E_{A\chi(q)}(q)
=
\frac12\left(E_+(q)+E_-(q)\right)
+
\frac{A\chi(q)}2
\left(E_+(q)-E_-(q)\right).
\]

Therefore

\[
\boxed{
\sum_{q\ne0,2}E_{A\chi(q)}(q)
=
\frac12\left(S_0+A S_\chi\right).
}
\]

Hence

\[
\boxed{
N_A(p)
=(p-2)+B_A
-
\frac{S_0+A S_\chi}{2p}.
}
\]

The two arithmetic Fortune classes are therefore the constant and quadratic-character projectors of one two-reading q-line hook system.

## 4. Geometric meaning

Over `Fbar_p`, the split and nonsplit cells are isomorphic by root scaling. Their difference is arithmetic descent by the quadratic character. Consequently:

- `S_0` is the Frobenius trace on the invariant q-line assembly of the two readings;
- `S_chi` is the trace on the quadratic anti-invariant assembly;
- the class `A` selects `S_0+A S_chi`.

This is the exact location of the unramified arithmetic quadratic twist flagged in the hook audit. It is not an additional unknown family.

## 5. Final certificate in q-line form

The proved parity certificate says that the crown holds at `p` if, for at least one `A`,

\[
N_A(p)\notin2p\mathbf Z_{\ge0}.
\]

Using the exact q-line ledger, this becomes

\[
\boxed{
(p-2)+B_A
-
\frac{S_0+A S_\chi}{2p}
\notin2p\mathbf Z_{\ge0}
}
\]

for at least one sign `A`.

Thus the remaining application theorem need not reconstruct each fixed-`q` hook spectrum. It must transport the Airy virtual module into the two global projectors `S_0` and `S_chi`, and attach the two explicit boundary counts `B_A`.

## 6. Exact remaining comparison

The nested sparse-root theorem identifies the geometric source of the q-line hook system. The required vanishing-cycle comparison can now be stated componentwise:

1. identify the pure middle trace of the invariant projector `S_0`;
2. identify the pure middle trace of the quadratic projector `S_chi`;
3. compute the lower-weight and punctual cones contributing to `B_A` and the main term `p-2`;
4. insert the transported trace bound into the boxed certificate.

The arithmetic assembly after these traces are known is complete.

## 7. Verification

The formula is checked by the already committed per-cell counts at `p=5,7,11`. `hook_q_line_projector_verify.py` independently reconstructs `N_+` and `N_-` from the cell counts, the fixed-cell identity and the two projector sums.

This is a structural regression of the ledger, not a new prime sweep.
