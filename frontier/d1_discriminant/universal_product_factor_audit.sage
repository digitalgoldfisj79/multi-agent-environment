# Exact audit for UNIVERSAL_PRODUCT_COMPRESSION.md

for p in [5,7,11,13]:
    F = GF(p)
    R.<T> = PolynomialRing(F)

    w = T*(T-1)^(p-1)
    q = T^2+T+1
    s = T^2*q^p-q
    Rp = (w^p-w)^(p-1)-T^2*s^(p-1)

    assert Rp.degree() == p^2*(p-1)

    factorization = Rp.factor()
    degree_metadata = {}
    degree_p_factors = []
    for h,e in factorization:
        assert h.degree() <= p
        degree_metadata[(h.degree(),e)] = degree_metadata.get((h.degree(),e),0)+1
        if h.degree() == p:
            degree_p_factors.append(h)

    expected = {5:5,7:9,11:14,13:8}[p]
    assert len(degree_p_factors) == expected

    norm_exponent = (p^p-1)//(p-1)
    for h in degree_p_factors:
        assert power_mod(T,norm_exponent,h) == 1

    print('p=',p)
    print('degree=',Rp.degree())
    print('squarefree degree=',Rp.squarefree_part().degree())
    print('factor metadata=',sorted(degree_metadata.items()))
    print('degree-p factor count=',len(degree_p_factors))
    print('PASS')
