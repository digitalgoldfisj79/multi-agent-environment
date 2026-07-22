#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <omp.h>
using namespace std;

/* Exact odd-locus cubic-factor ledger for
     F_(c,0)(X)=X^p+aX^3+cX=X H_c(X^2).
   Usage: g++ -O3 -march=native -fopenmp odd_locus_cubic_mass.cpp -o odd
          ./odd <prime p>
   Cubic factors are enumerated through trace-zero additive orbits. */

struct Poly3 { int c0, c1, c2; };
static int modp(long long x, int p){ x%=p; if(x<0)x+=p; return (int)x; }
static int modpow(int a,long long e,int p){ long long o=1,b=modp(a,p); while(e){if(e&1)o=o*b%p;b=b*b%p;e>>=1;}return (int)o; }
static int invmod(int a,int p){ return modpow(a,p-2,p); }
static int chi(int a,int p){ a=modp(a,p); if(!a)return 0; return modpow(a,(p-1)/2,p)==1?1:-1; }

static Poly3 mul3(Poly3 x, Poly3 y, int S, int N, int p){
    long long r[5]={0,0,0,0,0}; int xv[3]={x.c0,x.c1,x.c2}, yv[3]={y.c0,y.c1,y.c2};
    for(int i=0;i<3;i++)for(int j=0;j<3;j++)r[i+j]+=(long long)xv[i]*yv[j];
    for(int d=4;d>=3;--d){ int z=modp(r[d],p); r[d]=0; int sh=d-3; r[sh]+=(long long)z*N; r[sh+1]-=(long long)z*S; }
    return {modp(r[0],p),modp(r[1],p),modp(r[2],p)};
}
static Poly3 xp(int S,int N,int p){ Poly3 o{1,0,0},b{0,1,0}; int e=p; while(e){if(e&1)o=mul3(o,b,S,N,p);b=mul3(b,b,S,N,p);e>>=1;}return o; }
static bool irred(int S,int N,int p){ for(int x=0;x<p;x++) if(modp((long long)x*x%p*x+(long long)S*x-N,p)==0)return false; return true; }

static void run_class(int p,int a){
    int T=omp_get_max_threads();
    vector<vector<int>> local(T,vector<int>(p,0));
    long long total_irred=0;
    #pragma omp parallel reduction(+:total_irred)
    {
        int tid=omp_get_thread_num(); auto &q=local[tid];
        int inv3a=invmod(modp(3LL*a,p),p);
        #pragma omp for schedule(dynamic)
        for(int S=0;S<p;S++) for(int N=0;N<p;N++){
            if(!irred(S,N,p))continue;
            ++total_irred;
            Poly3 f=xp(S,N,p);
            int u=modp(-(long long)f.c2*inv3a,p);
            int s=modp((long long)S+3LL*u*u,p);
            int n=modp((long long)N+(long long)S*u+(long long)u*u%p*u,p);
            int A=modp((long long)f.c0-(long long)f.c1*u+(long long)f.c2*u%p*u+u,p);
            int B=modp((long long)f.c1-2LL*f.c2*u,p);
            int c=modp((long long)a*s-B,p);
            int d=modp(-(long long)A-(long long)a*n,p);
            if(d==0) ++q[c];
        }
    }
    vector<int> q3(p,0); for(auto &v:local)for(int c=0;c<p;c++)q3[c]+=v[c];
    long long qinc=0,qpair=0,qtriple=0,rinc=0,rpair=0,rtriple=0,support=0; int mx=0; map<int,long long> dist;
    for(int c=0;c<p;c++){
        int q=q3[c]; if(q&1){ cerr<<"odd Q3 at p="<<p<<" a="<<a<<" c="<<c<<"\n"; exit(3); }
        int r=q/2; qinc+=q; qpair+=(long long)q*(q-1)/2; qtriple+=(long long)q*(q-1)*(q-2)/6;
        rinc+=r; rpair+=(long long)r*(r-1)/2; rtriple+=(long long)r*(r-1)*(r-2)/6;
        if(q)support++; mx=max(mx,q); dist[q]++;
    }
    if(total_irred!=((long long)p*p-1)/3){ cerr<<"mass mismatch\n"; exit(4); }
    string ds; for(auto [k,v]:dist){if(!ds.empty())ds+=';';ds+=to_string(k)+":"+to_string(v);}
    cout<<p<<','<<a<<','<<chi(a,p)<<','<<qinc<<','<<qpair<<','<<qtriple<<','<<rinc<<','<<rpair<<','<<rtriple<<','<<support<<','<<mx<<",\""<<ds<<"\"\n";
}

int main(int argc,char**argv){
    if(argc!=2){cerr<<"usage: odd <prime p>\n";return 2;} int p=stoi(argv[1]);
    int ns=2; while(ns<p&&chi(ns,p)!=-1)++ns;
    cout<<"prime,a,square_class,odd_Q3_incidence,odd_Q3_second,odd_Q3_third,R3_incidence,R3_second,R3_third,support,max_Q3,multiplicity_distribution\n";
    run_class(p,1); run_class(p,ns); return 0;
}
