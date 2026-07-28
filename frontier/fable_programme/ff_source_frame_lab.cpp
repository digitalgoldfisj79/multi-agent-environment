#include <bits/stdc++.h>
using namespace std;

struct Poly { vector<int> a; };
static int Q=3;
static Poly norm(Poly f){ while(f.a.size()>1 && ((f.a.back()%Q)+Q)%Q==0) f.a.pop_back(); for(int &x:f.a){x%=Q;if(x<0)x+=Q;} if(f.a.empty()) f.a={0}; return f; }
static int deg(const Poly&f){return (int)f.a.size()-1;}
static bool eq(const Poly&a,const Poly&b){return a.a==b.a;}
static Poly addp(const Poly&a,const Poly&b){ Poly c; c.a.assign(max(a.a.size(),b.a.size()),0); for(size_t i=0;i<c.a.size();++i)c.a[i]=((i<a.a.size()?a.a[i]:0)+(i<b.a.size()?b.a[i]:0))%Q; return norm(c);}
static Poly subp(const Poly&a,const Poly&b){ Poly c; c.a.assign(max(a.a.size(),b.a.size()),0); for(size_t i=0;i<c.a.size();++i)c.a[i]=((i<a.a.size()?a.a[i]:0)-(i<b.a.size()?b.a[i]:0)+Q)%Q; return norm(c);}
static Poly mulp(const Poly&a,const Poly&b){ Poly c; c.a.assign(a.a.size()+b.a.size()-1,0); for(size_t i=0;i<a.a.size();++i) if(a.a[i]) for(size_t j=0;j<b.a.size();++j) if(b.a[j]) c.a[i+j]=(c.a[i+j]+a.a[i]*b.a[j])%Q; return norm(c);}
static int invint(int x){x%=Q;if(x<0)x+=Q;for(int y=1;y<Q;++y)if(x*y%Q==1)return y;throw runtime_error("no inv");}
static Poly modp(Poly a,const Poly&m){a=norm(a);int dm=deg(m);int il=invint(m.a.back());while(deg(a)>=dm && !(a.a.size()==1&&a.a[0]==0)){int coeff=a.a.back()*il%Q;int sh=deg(a)-dm;if(coeff){for(size_t i=0;i<m.a.size();++i){a.a[sh+i]=(a.a[sh+i]-coeff*m.a[i])%Q;if(a.a[sh+i]<0)a.a[sh+i]+=Q;}}a=norm(a);}return a;}
static Poly mulmod(const Poly&a,const Poly&b,const Poly&m){return modp(mulp(a,b),m);} 
static Poly powmod(Poly a,long long e,const Poly&m){Poly r{{1}};a=modp(a,m);while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static Poly gcdp(Poly a,Poly b){while(!(b.a.size()==1&&b.a[0]==0)){Poly r=modp(a,b);a=b;b=r;}if(a.a.size()==1&&a.a[0]==0)return a;int il=invint(a.a.back());for(int&x:a.a)x=x*il%Q;return norm(a);} 
static vector<int> prime_divs(int n){vector<int>v;for(int p=2;p*p<=n;++p)if(n%p==0){v.push_back(p);while(n%p==0)n/=p;}if(n>1)v.push_back(n);return v;}
static bool irreducible(const Poly&f){int n=deg(f);if(n<=0||f.a.back()!=1)return false;if(n==1)return true;Poly x{{0,1}},h=x;vector<Poly> vals(n+1);for(int k=1;k<=n;++k){h=powmod(h,Q,f);vals[k]=h;}if(!eq(subp(vals[n],x),Poly{{0}}))return false;for(int r:prime_divs(n)){if(!eq(gcdp(subp(vals[n/r],x),f),Poly{{1}}))return false;}return true;}
static vector<Poly> monic_irreds(int n){vector<Poly> out; long long total=1;for(int i=0;i<n;++i)total*=Q;for(long long code=0;code<total;++code){long long z=code;Poly f;f.a.assign(n+1,0);for(int i=0;i<n;++i){f.a[i]=z%Q;z/=Q;}f.a[n]=1;if(irreducible(f))out.push_back(f);}return out;}
static int residue_inf(const Poly&S,const Poly&H){ Poly r=modp(S,H); int h=deg(H); return (h-1<(int)r.a.size()?r.a[h-1]:0)%Q; }
static long double pearson(const vector<long double>&x,const vector<long double>&y){long double mx=accumulate(x.begin(),x.end(),(long double)0)/x.size();long double my=accumulate(y.begin(),y.end(),(long double)0)/y.size();long double a=0,b=0,c=0;for(size_t i=0;i<x.size();++i){long double dx=x[i]-mx,dy=y[i]-my;a+=dx*dy;b+=dx*dx;c+=dy*dy;}return (b&&c)?a/sqrt(b*c):0;}
static vector<long double> ranks(const vector<long double>&x){int n=x.size();vector<int>idx(n);iota(idx.begin(),idx.end(),0);stable_sort(idx.begin(),idx.end(),[&](int i,int j){return x[i]<x[j];});vector<long double>r(n);int i=0;while(i<n){int j=i+1;while(j<n&&x[idx[j]]==x[idx[i]])++j;long double rr=((i+1)+j)/2.0;for(int k=i;k<j;++k)r[idx[k]]=rr;i=j;}return r;}
static long double spearman(const vector<long double>&x,const vector<long double>&y){return pearson(ranks(x),ranks(y));}
static long double percentile(const vector<long double>&x,long double v){int le=0;for(auto z:x)if(z<=v)++le;return 100.0L*le/x.size();}

struct LabResult{int d,K,orders,shells,shell_pairs,offsets; long double corr_pair,corr_pair2,corr_single,corr_single2,corr_source,spear_pair,spear_pair2,spear_single,spear_single2,spear_source;long double id_det,id_pair,id_pair2,id_single,id_single2;long double id_pct_det,id_pct_pair,id_pct_pair2,id_pct_single,id_pct_single2;vector<long double> baseline;};

static LabResult runlab(int d,int max_orders,int shell_pair_limit){
    auto block=monic_irreds(d);int K=block.size();
    Poly A{{1}};for(int e=1;e<d;++e)for(auto &f:monic_irreds(e))A=mulp(A,f);
    int SZ=1<<K;vector<Poly>P(SZ);P[0]=A;for(int mask=1;mask<SZ;++mask){int bit=__builtin_ctz(mask);P[mask]=mulp(P[mask^(1<<bit)],block[bit]);}
    vector<Poly> offsets;for(int e=d;e<2*d;++e){auto v=monic_irreds(e);offsets.insert(offsets.end(),v.begin(),v.end());}
    vector<int>Z(SZ,0);for(int mask=1;mask<SZ;++mask){for(auto&m:offsets)if(irreducible(addp(P[mask],m)))Z[mask]++;}
    vector<long double> base(K+1,0);vector<int>cnt(K+1,0);for(int mask=1;mask<SZ;++mask){int s=__builtin_popcount((unsigned)mask);base[s]+=Z[mask];cnt[s]++;}for(int s=1;s<=K;++s)base[s]/=cnt[s];
    auto shells=monic_irreds(2*d);vector<pair<int,int>> sp;for(int i=0;i<(int)shells.size();++i)for(int j=i+1;j<(int)shells.size();++j)sp.push_back({i,j});
    unsigned long long seed=20260728+d; if(const char*e=getenv("LAB_SEED")) seed=stoull(e)+d; mt19937_64 rng(seed);shuffle(sp.begin(),sp.end(),rng);if((int)sp.size()>shell_pair_limit)sp.resize(shell_pair_limit);
    vector<vector<unsigned char>> res(shells.size(),vector<unsigned char>(SZ*SZ,255));
    for(int h=0;h<(int)shells.size();++h){for(int a=1;a<SZ;++a)for(int b=1;b<SZ;++b){if((a&b)==a || (a&b)==b){Poly S=addp(P[a],P[b]);res[h][a*SZ+b]=residue_inf(S,shells[h]);}}}
    vector<vector<int>> orders; vector<int> perm(K);iota(perm.begin(),perm.end(),0);int total=1;for(int i=2;i<=K;++i)total*=i;
    if(total<=max_orders){do{orders.push_back(perm);}while(next_permutation(perm.begin(),perm.end()));}
    else{set<vector<int>> seen;seen.insert(perm);orders.push_back(perm);while((int)orders.size()<max_orders){shuffle(perm.begin(),perm.end(),rng);if(seen.insert(perm).second)orders.push_back(perm);}}
    vector<long double> detv,pairv,pair2v,singv,sing2v,sourcev;
    for(auto &ord:orders){vector<int> path;vector<long double> weights;int mask=0;long double dv=0;for(int s=1;s<=K;++s){mask|=1<<ord[s-1];path.push_back(mask);long double e=Z[mask]-base[s];weights.push_back(e);dv+=e*e;}detv.push_back(dv);
        vector<pair<int,int>> pairs;for(int i=0;i<K;++i)for(int j=i;j<K;++j)pairs.push_back({path[i],path[j]});
        long double sumk=0,sumk2=0,sums=0,sums2=0,sumsrc=0;for(auto [u,v]:sp){int c[3]={0,0,0};for(auto [a,b]:pairs){int z=(int)res[u][a*SZ+b]-(int)res[v][a*SZ+b];z%=3;if(z<0)z+=3;c[z]++;}long long abs2=1LL*c[0]*c[0]+1LL*c[1]*c[1]+1LL*c[2]*c[2]-1LL*c[0]*c[1]-1LL*c[0]*c[2]-1LL*c[1]*c[2];long long kk=abs2-(int)pairs.size();sumk+=kk;sumk2+=(long double)kk*kk;
            int sct[3]={0,0,0};for(int a:path){int z=(int)res[u][a*SZ+a]-(int)res[v][a*SZ+a];z%=3;if(z<0)z+=3;sct[z]++;}long long sa=1LL*sct[0]*sct[0]+1LL*sct[1]*sct[1]+1LL*sct[2]*sct[2]-1LL*sct[0]*sct[1]-1LL*sct[0]*sct[2]-1LL*sct[1]*sct[2];long long sk=sa-K;sums+=sk;sums2+=(long double)sk*sk;
            long double wc[3]={0,0,0};for(int ii=0;ii<K;++ii){int a=path[ii];int z=(int)res[u][a*SZ+a]-(int)res[v][a*SZ+a];z%=3;if(z<0)z+=3;wc[z]+=weights[ii];}long double src=wc[0]*wc[0]+wc[1]*wc[1]+wc[2]*wc[2]-wc[0]*wc[1]-wc[0]*wc[2]-wc[1]*wc[2];sumsrc+=src;
        }pairv.push_back(sumk/sp.size());pair2v.push_back(sumk2/sp.size());singv.push_back(sums/sp.size());sing2v.push_back(sums2/sp.size());sourcev.push_back(sumsrc/sp.size());}
    LabResult R;R.d=d;R.K=K;R.orders=orders.size();R.shells=shells.size();R.shell_pairs=sp.size();R.offsets=offsets.size();R.corr_pair=pearson(detv,pairv);R.corr_pair2=pearson(detv,pair2v);R.corr_single=pearson(detv,singv);R.corr_single2=pearson(detv,sing2v);R.corr_source=pearson(detv,sourcev);R.spear_pair=spearman(detv,pairv);R.spear_pair2=spearman(detv,pair2v);R.spear_single=spearman(detv,singv);R.spear_single2=spearman(detv,sing2v);R.spear_source=spearman(detv,sourcev);R.id_det=detv[0];R.id_pair=pairv[0];R.id_pair2=pair2v[0];R.id_single=singv[0];R.id_single2=sing2v[0];R.id_pct_det=percentile(detv,R.id_det);R.id_pct_pair=percentile(pairv,R.id_pair);R.id_pct_pair2=percentile(pair2v,R.id_pair2);R.id_pct_single=percentile(singv,R.id_single);R.id_pct_single2=percentile(sing2v,R.id_single2);R.baseline=base;return R;
}

static void printres(const LabResult&r){cout<<fixed<<setprecision(8);cout<<"{\n";cout<<"  \"q\": 3, \"d\": "<<r.d<<", \"K\": "<<r.K<<", \"orders\": "<<r.orders<<", \"shells\": "<<r.shells<<", \"shell_pairs\": "<<r.shell_pairs<<", \"offsets\": "<<r.offsets<<",\n";cout<<"  \"pearson\": {\"pair_mean\": "<<(double)r.corr_pair<<", \"pair_square_mean\": "<<(double)r.corr_pair2<<", \"single_mean\": "<<(double)r.corr_single<<", \"single_square_mean\": "<<(double)r.corr_single2<<", \"weighted_source_energy\": "<<(double)r.corr_source<<"},\n";cout<<"  \"spearman\": {\"pair_mean\": "<<(double)r.spear_pair<<", \"pair_square_mean\": "<<(double)r.spear_pair2<<", \"single_mean\": "<<(double)r.spear_single<<", \"single_square_mean\": "<<(double)r.spear_single2<<", \"weighted_source_energy\": "<<(double)r.spear_source<<"},\n";cout<<"  \"identity\": {\"detector_variance\": "<<(double)r.id_det<<", \"pair_mean\": "<<(double)r.id_pair<<", \"pair_square_mean\": "<<(double)r.id_pair2<<", \"single_mean\": "<<(double)r.id_single<<", \"single_square_mean\": "<<(double)r.id_single2<<", \"percentiles\": {\"detector\": "<<(double)r.id_pct_det<<", \"pair_mean\": "<<(double)r.id_pct_pair<<", \"pair_square_mean\": "<<(double)r.id_pct_pair2<<", \"single_mean\": "<<(double)r.id_pct_single<<", \"single_square_mean\": "<<(double)r.id_pct_single2<<"}},\n";cout<<"  \"rank_baselines\": [";for(int i=1;i<=r.K;++i){if(i>1)cout<<", ";cout<<(double)r.baseline[i];}cout<<"]\n}";}
int main(){auto a=runlab(2,100000,100000);auto b=runlab(3,40320,2048);cout<<"[\n";printres(a);cout<<",\n";printres(b);cout<<"\n]\n";}
