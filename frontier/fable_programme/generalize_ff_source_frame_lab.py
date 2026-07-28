#!/usr/bin/env python3
"""Generate the cross-field M7 laboratory from the frozen q=3 source.

The original source used the diagonal pair sum P+P for the single phase. That is
harmless over F_3 for absolute-square statistics but degenerates over F_2. This
script separates the single-centre and pair-sum residues and makes the prime
field and run sizes command-line parameters.
"""

from pathlib import Path
import sys

if len(sys.argv) != 3:
    raise SystemExit("usage: generalize_ff_source_frame_lab.py INPUT.cpp OUTPUT.cpp")

source = Path(sys.argv[1]).read_text(encoding="utf-8")

start = source.index(
    "    vector<vector<unsigned char>> res(shells.size(),vector<unsigned char>(SZ*SZ,255));"
)
end = source.index("    vector<vector<int>> orders;", start)
source = source[:start] + r'''    // Precompute pair-sum and single-centre residues separately.
    vector<vector<unsigned char>> res(shells.size(),vector<unsigned char>(SZ*SZ,255));
    vector<vector<unsigned char>> single_res(shells.size(),vector<unsigned char>(SZ,255));
    for(int h=0;h<(int)shells.size();++h){
        for(int a=1;a<SZ;++a) single_res[h][a]=residue_inf(P[a],shells[h]);
        for(int a=1;a<SZ;++a)for(int b=1;b<SZ;++b){
            if((a&b)==a || (a&b)==b){
                Poly S=addp(P[a],P[b]);
                res[h][a*SZ+b]=residue_inf(S,shells[h]);
            }
        }
    }
''' + source[end:]

start = source.index(
    "        long double sumk=0,sumk2=0,sums=0,sums2=0,sumsrc=0;"
)
end = source.index("        }pairv.push_back", start)
source = source[:start] + r'''        long double sumk=0,sumk2=0,sums=0,sums2=0,sumsrc=0;
        auto abs2_counts=[&](const vector<long double>&v){
            if(Q==2) return (v[0]-v[1])*(v[0]-v[1]);
            if(Q==3) return v[0]*v[0]+v[1]*v[1]+v[2]*v[2]
                -v[0]*v[1]-v[0]*v[2]-v[1]*v[2];
            long double re=0,im=0;
            const long double pi=acosl(-1.0L);
            for(int j=0;j<Q;++j){
                re+=v[j]*cosl(2*pi*j/Q);
                im+=v[j]*sinl(2*pi*j/Q);
            }
            return re*re+im*im;
        };
        for(auto [u,v]:sp){
            vector<long double> c(Q,0);
            for(auto [a,b]:pairs){
                int z=(int)res[u][a*SZ+b]-(int)res[v][a*SZ+b];
                z%=Q;if(z<0)z+=Q;c[z]++;
            }
            long double abs2=abs2_counts(c);
            long double kk=abs2-(int)pairs.size();
            sumk+=kk;sumk2+=kk*kk;

            vector<long double> sct(Q,0);
            for(int a:path){
                int z=(int)single_res[u][a]-(int)single_res[v][a];
                z%=Q;if(z<0)z+=Q;sct[z]++;
            }
            long double sa=abs2_counts(sct);
            long double sk=sa-K;
            sums+=sk;sums2+=sk*sk;

            vector<long double> wc(Q,0);
            for(int ii=0;ii<K;++ii){
                int a=path[ii];
                int z=(int)single_res[u][a]-(int)single_res[v][a];
                z%=Q;if(z<0)z+=Q;wc[z]+=weights[ii];
            }
            sumsrc+=abs2_counts(wc);
''' + source[end:]

source = source.replace(
    'cout<<"  \\"q\\": 3, \\"d\\": "<<r.d',
    'cout<<"  \\"q\\": "<<Q<<", \\"d\\": "<<r.d',
)

main_start = source.rfind("int main(){")
if main_start < 0:
    raise SystemExit("main function anchor not found")
source = source[:main_start] + r'''int main(int argc,char**argv){
    if(argc<3){
        cerr<<"usage: ff_source_frame_lab Q D [max_orders] [shell_pairs]\n";
        return 2;
    }
    Q=stoi(argv[1]);
    int d=stoi(argv[2]);
    int max_orders=(argc>3?stoi(argv[3]):1000000);
    int shell_pairs=(argc>4?stoi(argv[4]):1000000);
    auto result=runlab(d,max_orders,shell_pairs);
    cout<<"[\n";
    printres(result);
    cout<<"\n]\n";
}
'''

Path(sys.argv[2]).write_text(source, encoding="utf-8")
