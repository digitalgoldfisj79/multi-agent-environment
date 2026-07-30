#!/usr/bin/env python3
"""Finite audit of the inverse-free cross-modulus incidence equations."""
import json
from ff_sampled_diagonal_discriminator import irreducibles_upto,mu_value,padd,pmul,pmod,psub,primorial

def deg(a): return len(a)-1 if a else -1
def smul(c,a,q): return pmul((c,),a,q)
def pairs(q,k,L):
    band=irreducibles_upto(k,q)[k]
    return [(P,S,mu_value(P,S,L,1,q),mu_value(S,P,L,1,q)) for P in band for S in band if P!=S]
def mu_witness(a,b,c,L,q):
    P,S,_,_=a;Pp,Sp,_,_=b
    return not pmod(padd(smul(c,pmul(L,S,q),q),Pp,q),P,q) and not pmod(psub(smul(c,pmul(L,Sp,q),q),P,q),Pp,q)
def nu_witness(a,b,c,L,q):
    P,S,_,_=a;Pp,Sp,_,_=b
    return not pmod(padd(smul(c,pmul(L,P,q),q),Sp,q),S,q) and not pmod(psub(smul(c,pmul(L,Pp,q),q),S,q),Sp,q)
def panel(q,k):
    L=primorial(q); rows=pairs(q,k,L); ci=di=both=0
    for a in rows:
      for b in rows:
        P,S,mu,nu=a;Pp,Sp,mup,nup=b
        Em=psub(pmul(mu,Pp,q),pmul(mup,P,q),q); En=psub(pmul(nu,Sp,q),pmul(nup,S,q),q)
        Im=deg(Em)<=0; In=deg(En)<=0
        cs=[] if P==Pp else [c for c in range(q) if mu_witness(a,b,c,L,q)]
        ds=[] if S==Sp else [c for c in range(q) if nu_witness(a,b,c,L,q)]
        if P!=Pp:
            assert bool(cs)==Im
            if Im: assert cs==[Em[0] if Em else 0]
        if S!=Sp:
            assert bool(ds)==In
            if In: assert ds==[En[0] if En else 0]
        ci+=Im and P!=Pp;di+=In and S!=Sp;both+=Im and In and P!=Pp and S!=Sp
    return {'q':q,'k':k,'m':2*k-1,'ordered_prime_pairs':len(rows),'pair_of_pairs':len(rows)**2,'scope':'cross-modulus P!=Pprime and S!=Sprime','mu_incidences':ci,'nu_incidences':di,'simultaneous_incidences':both,'mu_divisibility_witnesses':ci,'nu_divisibility_witnesses':di,'equivalence_and_uniqueness_verified':True}
def main():
    print(json.dumps({'status':'MACHINE-VERIFIED IDENTITY supporting an exact algebraic proof','theorem':'Endpoint scalar-frequency incidence is equivalent to four inverse-free polynomial divisibilities.','panels':[panel(3,2),panel(5,2),panel(7,2),panel(3,3),panel(3,4)]},indent=2,sort_keys=True))
if __name__=='__main__': main()
