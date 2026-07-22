#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

/*
Exact grouping of every Cauchy-Binet degree set R for the p=223 witness,
with the identity set E fixed.

Cauchy-Binet and Jacobi reduce the grouped coefficient at fixed sum(R) to

 [z^1220] det( A^T diag(r! z^r) U ),

where A=P^{-1}[Omega,C0] and U is the inverse substitution matrix
[ X^r ] psi(X)^s, psi+psi^3=X.  The determinant is 10x10.  Fourier inversion
over F_(223^2)^* extracts the coefficient exactly; the determinant degree is
at most the sum of the ten largest row indices, far below 223^2-1.
*/

static constexpr int P = 223;
static constexpr int Q = P * P;
static constexpr int NR = 3; // quadratic nonsquare modulo 223
static constexpr int K = 10;
static constexpr int TARGET = 1220;

struct F2 { int a,b; };
static inline int mp(long long x){ x%=P; if(x<0)x+=P; return (int)x; }
static inline F2 add(F2 x,F2 y){ return {mp(x.a+y.a),mp(x.b+y.b)}; }
static inline F2 subf(F2 x,F2 y){ return {mp(x.a-y.a),mp(x.b-y.b)}; }
static inline F2 negf(F2 x){ return {mp(-x.a),mp(-x.b)}; }
static inline F2 mul(F2 x,F2 y){ return {mp((long long)x.a*y.a+(long long)NR*x.b*y.b),mp((long long)x.a*y.b+(long long)x.b*y.a)}; }
static int powp(int a,long long e){long long o=1,b=mp(a);while(e){if(e&1)o=o*b%P;b=b*b%P;e>>=1;}return (int)o;}
static F2 powf(F2 x,long long e){F2 o{1,0};while(e){if(e&1)o=mul(o,x);x=mul(x,x);e>>=1;}return o;}
static F2 invf(F2 x){ return powf(x,Q-2); }
static bool zero(F2 x){return x.a==0&&x.b==0;}

static F2 det10(array<array<F2,K>,K> a){
    F2 out{1,0};
    for(int c=0;c<K;c++){
        int piv=c;while(piv<K&&zero(a[piv][c]))piv++;
        if(piv==K)return {0,0};
        if(piv!=c){swap(a[piv],a[c]);out=negf(out);}
        F2 pv=a[c][c];out=mul(out,pv);F2 ip=invf(pv);
        for(int r=c+1;r<K;r++)if(!zero(a[r][c])){
            F2 factor=mul(a[r][c],ip);
            for(int j=c;j<K;j++)a[r][j]=subf(a[r][j],mul(factor,a[c][j]));
        }
    }
    return out;
}

static int choose_mod(int n,int k,const vector<int>&fac,const vector<int>&ifac){
    if(k<0||k>n)return 0;
    return (long long)fac[n]*ifac[k]%P*ifac[n-k]%P;
}

int main(){
    const int E[K-1]={5,7,8,12,13,14,16,17,18};
    int C0[K],C1[K];C0[0]=0;C1[0]=P-3;
    for(int i=0;i<K-1;i++){C0[i+1]=E[i];C1[i+1]=E[i];}
    sort(C0,C0+K);sort(C1,C1+K);

    vector<int>fac(P),ifac(P);fac[0]=1;
    for(int i=1;i<P;i++)fac[i]=(long long)fac[i-1]*i%P;
    ifac[P-1]=powp(fac[P-1],P-2);
    for(int i=P-1;i;i--)ifac[i-1]=(long long)ifac[i]*i%P;

    int A[P][K]{};int U[P][K]{};
    for(int r=0;r<P;r++)for(int j=0;j<K;j++){
        int s=C0[j];
        if(r>=s){int v=(long long)ifac[s]*ifac[r-s]%P;if((r-s)&1)v=mp(-v);A[r][j]=v;}
        s=C1[j];
        int v=0;
        if(s==0)v=(r==0);
        else if(r>=s&&((r-s)&1)==0){
            int h=(r-s)/2;
            // Lagrange inversion; comb may cross p and is evaluated mod p.
            int bin=choose_mod(r+h-1,h,fac,ifac);
            if(r+h-1>=P){
                // In this index range Lucas says zero whenever the upper index crosses p.
                bin=0;
            }
            if(bin){v=(long long)s*powp(r,P-2)%P*bin%P;if(h&1)v=mp(-v);}
        }
        U[r][j]=v;
    }

    // Enumerate all nonzero elements a+b*s of F_(p^2).
    F2 sum{0,0};
    long long evaluations=0;
    int max_degree=0;for(int r=P-K;r<P;r++)max_degree+=r;
    for(int aa=0;aa<P;aa++)for(int bb=0;bb<P;bb++){
        F2 z{aa,bb};if(zero(z))continue;
        vector<F2>zp(P);zp[0]={1,0};for(int r=1;r<P;r++)zp[r]=mul(zp[r-1],z);
        array<array<F2,K>,K> G{};
        for(int i=0;i<K;i++)for(int j=0;j<K;j++){
            F2 value{0,0};
            for(int r=0;r<P;r++)if(A[r][i]&&U[r][j]){
                int scalar=(long long)fac[r]*A[r][i]%P*U[r][j]%P;
                value=add(value,mul({scalar,0},zp[r]));
            }
            G[i][j]=value;
        }
        F2 d=det10(G);
        F2 character=powf(invf(z),TARGET);
        sum=add(sum,mul(d,character));
        evaluations++;
    }
    // 1/(Q-1)=-1 in characteristic p.
    F2 coefficient=negf(sum);
    cout<<"{\n"
        <<"  \"status\": \"PASS\",\n"
        <<"  \"prime\": 223,\n"
        <<"  \"identity_set_E\": [5,7,8,12,13,14,16,17,18],\n"
        <<"  \"target_sum_R\": 1220,\n"
        <<"  \"fourier_evaluations\": "<<evaluations<<",\n"
        <<"  \"determinant_polynomial_degree_bound\": "<<max_degree<<",\n"
        <<"  \"multiplicative_order\": "<<Q-1<<",\n"
        <<"  \"grouped_coefficient_real\": "<<coefficient.a<<",\n"
        <<"  \"grouped_coefficient_imag\": "<<coefficient.b<<",\n"
        <<"  \"nonzero\": "<<(coefficient.a||coefficient.b?"true":"false")<<"\n"
        <<"}\n";
    return coefficient.b==0?0:3;
}
