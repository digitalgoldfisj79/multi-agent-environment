# Exact target and obstruction

## Intended tree theorem

The intended `INT-LCSK-TG` theorem was a pointwise prime-local spanning-tree domination of the connected coefficient, followed by the inherited pair row-sum bound.

For order three with all three offsets in one residue class modulo `p`, the normalized moments are

\[
G_p(1)=1,
\qquad
G_p(12)=\frac{p}{p-1},
\qquad
G_p(123)=\frac{p^2}{(p-1)^2}.
\]

Partition Möbius inversion gives

\[
\kappa_{3,p}
=G_p(123)-3G_p(12)+2
=-\frac{p-2}{(p-1)^2}.
\tag{TG1}
\]

The exact pair coefficient is

\[
\kappa_{2,p}=G_p(12)-1=\frac1{p-1}.
\tag{TG2}
\]

There are three labelled spanning trees on three vertices. With edge constant `C`, their total budget is

\[
\frac{3C^2}{(p-1)^2}.
\tag{TG3}
\]

Hence

\[
\frac{|\kappa_{3,p}|}{3(C/(p-1))^2}
=\frac{p-2}{3C^2}.
\tag{TG4}
\]

For every fixed `C`, this ratio is unbounded as `p` grows. The intended pair-tree theorem is therefore false.

## Corrected higher-body target

The surviving object is an anchored connected collision-cluster sum. For the same-residue `r`-body contribution define schematically

\[
T_r(m)=
\sum_{p>2X}|\kappa_{r,p}|
\#\{m_2,\ldots,m_r\in\mathcal M_b:
 m_i\equiv m\pmod p\}.
\]

For fixed `r` and `p` large compared with `r`, `|kappa_{r,p}|` is of order `1/p`. Inserting the Brun--Titchmarsh bound

\[
N_p(m)\ll \frac{H}{p\log(H/p)}
\]

and `H asymp X^2` gives the absolute ledger

\[
T_r(m)
\ll_r
\frac{X^{r-1}}{(\log X)^r}.
\tag{TG5}
\]

Its effective radius is

\[
D_r\asymp
\frac{X}{(\log X)^{r/(r-1)}}
=
\frac{X}{(\log X)^{1+1/(r-1)}}.
\tag{TG6}
\]

For `r=Theta(log X)`, the additional exponent `1/(r-1)` tends to zero. Thus this absolute ledger cannot supply the fixed `delta>0` required by `INT-LCSK`.

This is a method obstruction, not a proof that the signed connected kernel violates `INT-LCSK`.
