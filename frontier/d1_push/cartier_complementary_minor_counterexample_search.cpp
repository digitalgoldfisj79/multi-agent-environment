#include <algorithm>
#include <atomic>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
#include <omp.h>
using namespace std;

/*
Adversarial randomized search for a counterexample to CT1-w1.

For a prime p, sample only torus-grading pairs (gamma,beta) with
beta>=gamma+4, generate exact-sum subsets E and R, and evaluate

det(P^-1)_(R,E union {0}) det(U)_(R,E union {p-3}) mod p.

A nonzero product is an exact counterexample.  Absence of a hit is evidence,
not a proof.

Usage: ./search <prime p> <trials per admissible (gamma,beta)> <seed>
*/

static int modp(long long x,int p){x%=p;if(x<0)x+=p;return (int)x;}
static int modpow(int a,long long e,int p){long long o=1,b=modp(a,p);while(e){if(e&1)o=o*b%p;b=b*b%p;e>>=1;}return (int)o;}

static int detmod(vector<int> a,int n,int p){
    int out=1;
    for(int c=0;c<n;c++){
        int piv=c; while(piv<n&&a[piv*n+c]==0)piv++;
        if(piv==n)return 0;
        if(piv!=c){for(int j=c;j<n;j++)swap(a[piv*n+j],a[c*n+j]);out=modp(-out,p);}
        int pv=a[c*n+c],ip=modpow(pv,p-2,p); out=(long long)out*pv%p;
        for(int r=c+1;r<n;r++)if(a[r*n+c]){
            int f=(long long)a[r*n+c]*ip%p;
            for(int j=c;j<n;j++)a[r*n+j]=modp(a[r*n+j]-(long long)f*a[c*n+j],p);
        }
    }
    return out;
}

static bool sample_subset(const vector<int>& vals,int k,int target,mt19937_64& rng,vector<int>& out){
    out.clear(); int start=0, rem=target, n=(int)vals.size();
    for(int pos=0;pos<k;pos++){
        int left=k-pos-1;
        vector<int> cand;
        for(int idx=start;idx<n;idx++){
            if(n-idx-1<left)break;
            int v=vals[idx];
            long long minsum=0,maxsum=0;
            for(int j=0;j<left;j++)minsum+=vals[idx+1+j];
            for(int j=0;j<left;j++)maxsum+=vals[n-1-j];
            int nr=rem-v;
            if(nr>=minsum&&nr<=maxsum)cand.push_back(idx);
        }
        if(cand.empty())return false;
        int idx=cand[rng()%cand.size()];
        out.push_back(vals[idx]); rem-=vals[idx]; start=idx+1;
    }
    return rem==0;
}

static vector<int> feasible_sizes(const vector<int>& vals,int target){
    vector<int> ans; int n=vals.size();
    vector<long long> pre(n+1),suf(n+1);
    for(int i=0;i<n;i++)pre[i+1]=pre[i]+vals[i];
    for(int k=1;k<=n;k++){
        long long mn=pre[k],mx=0;for(int j=0;j<k;j++)mx+=vals[n-1-j];
        if(mn<=target&&target<=mx)ans.push_back(k);
    }
    return ans;
}

int main(int argc,char**argv){
    if(argc!=4){cerr<<"usage: search <prime p> <trials_per_pair> <seed>\n";return 2;}
    int p=stoi(argv[1]); long long trials=stoll(argv[2]); uint64_t seed=stoull(argv[3]);
    vector<int> fac(p),ifac(p);fac[0]=1;for(int i=1;i<p;i++)fac[i]=(long long)fac[i-1]*i%p;
    ifac[p-1]=modpow(fac[p-1],p-2,p);for(int i=p-1;i;i--)ifac[i-1]=(long long)ifac[i]*i%p;
    vector<vector<int>> binom(p,vector<int>(p));for(int n=0;n<p;n++){binom[n][0]=binom[n][n]=1;for(int k=1;k<n;k++)binom[n][k]=modp(binom[n-1][k-1]+binom[n-1][k],p);}
    vector<int> evals;for(int x=1;x<p;x++)if(x!=p-3)evals.push_back(x);
    vector<int> rvals(p);iota(rvals.begin(),rvals.end(),0);

    struct Pair{int gamma,beta,se,alpha;vector<int> ks;}; vector<Pair> pairs;
    for(int gamma=1;4*gamma<=p-11;gamma++){
        int se=gamma*(p-1)/2-1;
        auto ks=feasible_sizes(evals,se);
        for(int beta=gamma+4;3*beta+gamma<=p+1;beta+=2){
            int alpha=(p+1-3*beta-gamma)/2;
            if(alpha<0)continue;
            vector<int> good;
            for(int k:ks){int sr=se+beta*(p-1);int kr=k+1;auto rk=feasible_sizes(rvals,sr);if(find(rk.begin(),rk.end(),kr)!=rk.end())good.push_back(k);}
            if(!good.empty())pairs.push_back({gamma,beta,se,alpha,good});
        }
    }
    cerr<<"p="<<p<<" admissible_violation_pairs="<<pairs.size()<<" trials_per_pair="<<trials<<" threads="<<omp_get_max_threads()<<"\n";
    atomic<bool> found(false); atomic<long long> sampled(0),pnonzero(0),unonzero(0),both(0);
    string witness;
    #pragma omp parallel
    {
        int tid=omp_get_thread_num();mt19937_64 rng(seed+0x9e3779b97f4a7c15ULL*(tid+1));
        vector<int>E,R,C0,C1;
        #pragma omp for schedule(dynamic)
        for(size_t pi=0;pi<pairs.size();pi++){
            auto pr=pairs[pi];
            for(long long tr=0;tr<trials&&!found.load(memory_order_relaxed);tr++){
                int ke=pr.ks[rng()%pr.ks.size()]; int kr=ke+1; int sr=pr.se+pr.beta*(p-1);
                if(!sample_subset(evals,ke,pr.se,rng,E))continue;
                if(!sample_subset(rvals,kr,sr,rng,R))continue;
                sampled++;
                C0=E;C0.push_back(0);sort(C0.begin(),C0.end());
                C1=E;C1.push_back(p-3);sort(C1.begin(),C1.end());
                bool triangular=true;for(int i=0;i<kr;i++)if(R[i]<C0[i]){triangular=false;break;}if(!triangular)continue;
                vector<int>A(kr*kr),U(kr*kr);
                for(int i=0;i<kr;i++)for(int j=0;j<kr;j++){
                    int r=R[i],s=C0[j];
                    if(r>=s){int z=(long long)ifac[s]*ifac[r-s]%p;if((r-s)&1)z=modp(-z,p);A[i*kr+j]=z;}
                    r=R[i];s=C1[j];
                    int z=0;
                    if(s==0)z=(r==0);
                    else if(r>=s&&((r-s)&1)==0&&3*r-s<=2*p){int h=(r-s)/2;z=(long long)s*modpow(r,p-2,p)%p*binom[r+h-1][h]%p;if(h&1)z=modp(-z,p);}
                    U[i*kr+j]=z;
                }
                int da=detmod(A,kr,p);if(da)pnonzero++;
                int du=detmod(U,kr,p);if(du)unonzero++;
                if(da&&du){
                    both++; bool expected=false;
                    if(found.compare_exchange_strong(expected,true)){
                        string w="COUNTEREXAMPLE p="+to_string(p)+" gamma="+to_string(pr.gamma)+" beta="+to_string(pr.beta)+" alpha="+to_string(pr.alpha)+" detP="+to_string(da)+" detU="+to_string(du)+" E=";
                        for(int x:E)w+=to_string(x)+":";w+=" R=";for(int x:R)w+=to_string(x)+":";witness=w;
                    }
                }
            }
        }
    }
    cout<<"RESULT p="<<p<<" pairs="<<pairs.size()<<" sampled="<<sampled.load()<<" detP_nonzero="<<pnonzero.load()<<" detU_nonzero="<<unonzero.load()<<" product_nonzero="<<both.load()<<" status="<<(found?"COUNTEREXAMPLE":"NO_HIT")<<"\n";
    if(found)cout<<witness<<"\n";
    return found?1:0;
}
