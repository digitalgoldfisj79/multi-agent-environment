from pathlib import Path

p = Path('publications/fortune-papers-ii-vi-20260724/paper6_secondary_quotients_replacement/manuscript.md')
s = p.read_text()

old = '''From \\(\\sigma(y)=y+1\\),
\\[
\\sigma(g)=(y+1)^p-(y+1)=y^p-y=g
\\]
in characteristic \\(p\\).  Thus \\(g\\) descends to \\(Y_a\\).  The equation
\\(T^p-T=g\\) has the translation action \\(T\\mapsto T+1\\); pulling it back
along the invariant function \\(g:Y_a\\to\\mathbf A^1\\) yields the same free
\\(C_p\\)-torsor because \\(y\\) is a coordinate on each root-cycle fibre.
Finally, \\(t/a\\) has cyclic trace one, which is the stated trace-surjectivity.
\\(\\square\\)
'''
new = '''From \\(\\sigma(y)=y+1\\),
\\[
\\sigma(g)=(y+1)^p-(y+1)=y^p-y=g
\\]
in characteristic \\(p\\), so \\(g\\) descends to \\(Y_a\\).  We now justify the
Artin--Schreier presentation globally rather than only fibrewise.  On the free
root-cycle locus the quotient map is finite étale of degree \\(p\\), hence its
coordinate algebra is locally free of rank \\(p\\) over the invariant algebra.
The element \\(y\\) satisfies the monic relation
\\[
T^p-T-g=0.
\\]
Moreover its translates \\(y,y+1,\\ldots,y+p-1\\) are pairwise distinct on every
geometric fibre, because the \\(C_p\\)-action is free.  Therefore the induced
map
\\[
\\mathcal O_{Y_a}[T]/(T^p-T-g)\\longrightarrow\\mathcal O_{X_a},
\\qquad T\\longmapsto y,
\\]
is an isomorphism on every geometric fibre between locally free modules of the
same rank \\(p\\), and hence is an isomorphism.  Thus the quotient is represented
globally in the root-cycle direction by the displayed Artin--Schreier equation.
Finally, \\(t/a\\) has cyclic trace one, which is the stated trace-surjectivity.
\\(\\square\\)
'''
assert old in s, 'Theorem 9.2 proof block not found'
s = s.replace(old, new, 1)

old = '''Let \\(R\\) be the squarefree product of the distinct root factors, so
\\(\\deg R\\le3\\).  In reduced form the logarithmic derivative is
\\[
\\frac{f'}f=\\frac PR,
\\qquad P\\ne0,
\\]
because \\(f'=3aX^2+c\\) is nonzero when \\(a\\ne0\\).  After cancelling all
common factors, the reduced numerator \\(P\\) is therefore nonzero.  Hence
\\[
f'R=Pf.
\\]
'''
new = '''After cancelling common factors in the logarithmic derivative, write
\\[
\\frac{f'}f=\\frac PR
\\]
in lowest terms.  The reduced denominator \\(R\\) divides the squarefree product
of the distinct root factors, so \\(\\deg R\\le3\\).  The reduced numerator is
nonzero because \\(f'=3aX^2+c\\) is nonzero when \\(a\\ne0\\).  Thus
\\[
f'R=Pf,
\\qquad P\\ne0.
\\]
'''
assert old in s, 'Theorem 10.1 denominator block not found'
s = s.replace(old, new, 1)

old = '''Thus the two coefficient classes are not universally quadratic sign twists.
Let $D_p$ be the full $\\mu_n$-quotient of the $g=1$ level and let $U_p$ be the
quotient of the complete fixed-cubic root-cycle open.  A rational quotient point
has lifts in exactly one of the two arithmetic forms, and the number of rational
lifts is
\\[
\\operatorname{card}\\mu_n(\\mathbf F_p)=2.
\\]
'''
new = '''Thus the two coefficient classes are not universally quadratic sign twists.
Let $D_p$ be the full $\\mu_n$-quotient of the $g=1$ level and let $U_p$ be the
quotient of the complete fixed-cubic root-cycle open.  The $\\mu_n$-action on the
irreducible $g=1$ locus is free.  Indeed, a stabilizing dilation $\\lambda\\in
\\mu_n$ fixes the nonzero constant coefficient $d$ of an irreducible degree-$p$
polynomial, so $\\lambda^3=1$; but
\\[
\\gcd(3,n)=\\gcd(3,p-3)=1
\\]
for the admitted primes $p>5$, hence $\\lambda=1$.  Consequently every geometric
fibre of $D_p$ is a genuine $\\mu_n$-torsor.  A rational quotient point has lifts
in exactly one of the two arithmetic forms, and the number of rational lifts is
\\[
\\operatorname{card}\\mu_n(\\mathbf F_p)=2.
\\]
'''
assert old in s, 'Theorem 11.2 freeness insertion point not found'
s = s.replace(old, new, 1)

p.write_text(s)
print('PAPER6_PROOF_REPAIRS_APPLIED')
