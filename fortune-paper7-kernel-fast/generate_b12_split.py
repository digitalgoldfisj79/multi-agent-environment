#!/usr/bin/env python3
from __future__ import annotations
import argparse, math, re
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

VARS='ABCU'

def parse_matrix(path):
    txt=path.read_text(); seg=txt.split('B_LIFT_BEGIN',1)[1].split('B_LIFT_END',1)[0]
    out={}; pat=re.compile(r'_\[(\d+),(\d+)\]=([^_]+?)(?=_\[|$)',re.S)
    for m in pat.finditer(seg):
        terms=[]; raw=m.group(3).strip().replace('\n','')
        for tok in re.findall(r'[+-]?[^+-]+',raw):
            mm=re.fullmatch(r'([+-]?)(\d+(?:/\d+)?)?((?:[ABCU]\d*)*)',tok)
            if mm is None: raise ValueError(tok)
            c=(-1 if mm.group(1)=='-' else 1)*(Fraction(mm.group(2)) if mm.group(2) else Fraction(1))
            e={v:0 for v in VARS}
            for z in re.finditer(r'([ABCU])(\d*)',mm.group(3) or ''):
                e[z.group(1)]+=int(z.group(2)) if z.group(2) else 1
            terms.append((c,tuple(e[v] for v in VARS)))
        out[(int(m.group(1)),int(m.group(2)))]=terms
    return out

# exact term dictionaries for f0..f3; Lean rechecks all generated claims.
F=[
 [(-4,(2,1,0,1)),(6,(2,1,0,0)),(-2,(2,0,0,1)),(4,(2,0,0,0)),(4,(1,3,0,0)),(4,(1,2,0,1)),(2,(1,2,0,0)),(4,(1,1,1,1)),(-8,(1,1,1,0)),(-4,(1,0,1,0)),(2,(0,1,2,0)),(2,(0,0,2,1))],
 [(-4,(2,0,0,1)),(4,(2,0,0,0)),(2,(1,2,0,0)),(6,(1,1,0,1)),(-2,(1,1,0,0)),(8,(1,0,1,1)),(-8,(1,0,1,0)),(-2,(0,2,1,0)),(-2,(0,1,1,1)),(-2,(0,1,1,0)),(-4,(0,0,2,1)),(4,(0,0,2,0))],
 [(-2,(2,1,0,0)),(-2,(2,0,0,1)),(-2,(1,3,0,1)),(-1,(1,3,0,0)),(-2,(1,2,0,2)),(-2,(1,2,0,1)),(4,(1,1,1,1)),(4,(1,0,1,2)),(-1,(0,3,1,0)),(-2,(0,2,1,1)),(-4,(0,1,2,1)),(2,(0,1,2,0)),(-4,(0,0,2,2)),(2,(0,0,2,1))],
 [(4,(2,0,0,1)),(-4,(2,0,0,0)),(2,(1,2,0,1)),(-4,(1,2,0,0)),(-2,(1,1,0,2)),(-2,(1,1,0,1)),(-8,(1,0,1,1)),(8,(1,0,1,0)),(-1,(0,4,0,0)),(-2,(0,3,0,1)),(-2,(0,2,1,1)),(4,(0,2,1,0)),(-2,(0,1,1,2)),(6,(0,1,1,1)),(4,(0,0,2,1)),(-4,(0,0,2,0))]
]

def mul(p,q):
    d=defaultdict(Fraction)
    for a,e in p:
        for b,f in q:d[tuple(x+y for x,y in zip(e,f))]+=a*b
    return [(c,e) for e,c in sorted(d.items()) if c]

def scale(p,n): return [(c*n,e) for c,e in p]

def denom_for(M,j):
    d=1
    for i in range(1,5):
        for c,_ in M[(i,j)]:d=math.lcm(d,c.denominator)
    return d

def li(n):return str(n) if n>=0 else f'({n})'
def listdef(name,p):
    s=[f'def {name} : List Term := [']
    for c,e in p:
        assert c.denominator==1
        s.append(f'  ⟨{li(c.numerator)}, {e[0]}, {e[1]}, {e[2]}, {e[3]}⟩,')
    s.append(']'); return '\n'.join(s)

HEAD='''import Mathlib\nset_option autoImplicit false\nset_option maxRecDepth 1000000\nset_option maxHeartbeats 0\nnoncomputable section\nnamespace FortuneFormal\nnamespace Quadratic\nnamespace B12Split\nopen MvPolynomial\nabbrev P := MvPolynomial (Fin 4) ℤ\ndef a:P:=X 0\ndef b:P:=X 1\ndef c:P:=X 2\ndef u:P:=X 3\nstructure Term where coeff:ℤ; eA eB eC eU:ℕ\ndef term(t:Term):P:=C t.coeff*a^t.eA*b^t.eB*c^t.eC*u^t.eU\ndef poly(ts:List Term):P:=ts.foldl (fun z t=>z+term t) 0\ndef f0:P:=-4*a^2*b*u+6*a^2*b-2*a^2*u+4*a^2+4*a*b^3+4*a*b^2*u+2*a*b^2+4*a*b*c*u-8*a*b*c-4*a*c+2*b*c^2+2*c^2*u\ndef f1:P:=-4*a^2*u+4*a^2+2*a*b^2+6*a*b*u-2*a*b+8*a*c*u-8*a*c-2*b^2*c-2*b*c*u-2*b*c-4*c^2*u+4*c^2\ndef f2:P:=-2*a^2*b-2*a^2*u-2*a*b^3*u-a*b^3-2*a*b^2*u^2-2*a*b^2*u+4*a*b*c*u+4*a*c*u^2-b^3*c-2*b^2*c*u-4*b*c^2*u+2*b*c^2-4*c^2*u^2+2*c^2*u\ndef f3:P:=4*a^2*u-4*a^2+2*a*b^2*u-4*a*b^2-2*a*b*u^2-2*a*b*u-8*a*c*u+8*a*c-b^4-2*b^3*u-2*b^2*c*u+4*b^2*c-2*b*c*u^2+6*b*c*u+4*c^2*u-4*c^2\ndef g:P:=u*a*(b^2-4*c)*b\n'''

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input',type=Path);ap.add_argument('--target',type=int,choices=[1,2],required=True);ap.add_argument('--output',type=Path,required=True);a0=ap.parse_args()
    M=parse_matrix(a0.input);j=a0.target;D=denom_for(M,j)
    ms=[];ps=[]
    for i in range(4):
        m=scale(M[(i+1,j)],D);p=mul(F[i],m);ms.append(m);ps.append(p)
    target=['u-1','b+2'][j-1]
    out=[HEAD,f'def denominator:ℤ:={D}\ndef target:P:={target}\n']
    for i in range(4):out += [listdef(f'm{i}',ms[i]),listdef(f'p{i}',ps[i]),f'''theorem expand{i}: f{i}*poly m{i}=poly p{i} := by\n  simp [poly,m{i},p{i},term,f{i},a,b,c,u]\n  ring\n''']
    out.append('''theorem cancel : C denominator*g^3*target = poly p0+poly p1+poly p2+poly p3 := by\n  simp [poly,p0,p1,p2,p3,term,denominator,target,g,a,b,c,u]\n  ring\n\ntheorem certificate : C denominator*g^3*target = f0*poly m0+f1*poly m1+f2*poly m2+f3*poly m3 := by\n  rw [expand0,expand1,expand2,expand3]\n  exact cancel\n\nend B12Split\nend Quadratic\nend FortuneFormal\n''')
    text='\n'.join(out);a0.output.write_text(text)
    print('FAST_GENERATED',j,'denom',D,'source_terms',sum(len(x) for x in ms),'expanded_terms',sum(len(x) for x in ps),'bytes',len(text))
if __name__=='__main__':main()
