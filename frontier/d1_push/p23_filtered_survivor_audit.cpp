#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

/*
Exact p=23 audit of every orthogonality-surviving Cartier coefficient
strictly above the proposed support boundary.

The C_3 Cartier minor is evaluated over F_{23^2}=F_23[s]/(s^2-5).
Under c=c0*t and d=t^2, multiplicative Fourier inversion first extracts
the exact t-weight, then the c-exponent.  Since

  deg_t <= 344 < 528 = |F_{23^2}^*|,
  deg_c <= 253 < 528,

there is no aliasing.  The only possible survivor weights above
(p^2-1)/2=264 are 286, 308 and 330.  For each weight the code extracts
every coefficient c^{22 alpha} d^{22 beta} with alpha,beta >= 1.

The proved a-grading law says each such coefficient is
a(A+B*chi(a)), so the representatives a=1 and a=5 (a non-square mod 23)
cover all a != 0.

Build:
  g++ -O3 -march=native -fopenmp p23_filtered_survivor_audit.cpp -o audit
Run:
  OMP_NUM_THREADS=$(nproc) ./audit
*/

static const int P=23, Q=P*P, NR=5, N=22;
static uint16_t MUL[Q][Q], INVF[Q];

inline int addf(int x,int y){
    int a=(x%P+y%P)%P, b=(x/P+y/P)%P;
    return a+P*b;
}
inline int subf(int x,int y){
    int a=(x%P-y%P+P)%P, b=(x/P-y/P+P)%P;
    return a+P*b;
}
inline int negf(int x){ return subf(0,x); }
int powf(int x,long long e){
    int r=1;
    while(e){
        if(e&1) r=MUL[r][x];
        x=MUL[x][x];
        e>>=1;
    }
    return r;
}

struct Term { uint8_t i,j,k; uint16_t coeff; };
static vector<Term> terms[N][N];
static int cols[N];

int det22(array<array<uint16_t,N>,N> A){
    int det=1;
    for(int c=0;c<N;c++){
        int piv=c;
        while(piv<N && A[piv][c]==0) piv++;
        if(piv==N) return 0;
        if(piv!=c){
            swap(A[piv],A[c]);
            det=negf(det);
        }
        int pv=A[c][c];
        det=MUL[det][pv];
        int ip=INVF[pv];
        for(int r=c+1;r<N;r++) if(A[r][c]){
            int f=MUL[A[r][c]][ip];
            for(int j=c;j<N;j++)
                A[r][j]=subf(A[r][j],MUL[f][A[c][j]]);
        }
    }
    return det;
}

int main(){
    // F_{23^2}=F_23[s]/(s^2-5), encoded as a+23*b.
    for(int x=0;x<Q;x++) for(int y=0;y<Q;y++){
        int a=x%P,b=x/P,c=y%P,d=y/P;
        int re=(a*c+NR*b*d)%P;
        int im=(a*d+b*c)%P;
        MUL[x][y]=re+P*im;
    }
    INVF[0]=0;
    for(int x=1;x<Q;x++) INVF[x]=powf(x,Q-2);

    int fac[P],ifac[P];
    fac[0]=1;
    for(int i=1;i<P;i++) fac[i]=fac[i-1]*i%P;
    auto modpow=[&](int a,int e){
        long long r=1,b=a;
        while(e){
            if(e&1) r=r*b%P;
            b=b*b%P;
            e>>=1;
        }
        return (int)r;
    };
    ifac[P-1]=modpow(fac[P-1],P-2);
    for(int i=P-1;i>=1;i--) ifac[i-1]=ifac[i]*i%P;

    int ci=0;
    for(int v=1;v<=P;v++) if(v!=3) cols[ci++]=v;

    // Exact trinomial formula for H_{u,v}; M=I-H.
    for(int ui=0;ui<N;ui++){
        int u=ui+1;
        for(int cj=0;cj<N;cj++){
            int v=cols[cj];
            for(int w=1;w<=min(4,u);w++){
                int n=P-1-u+w;
                int target=P*w-v;
                for(int i=0;i<=min(n,target/3);i++){
                    int j=target-3*i;
                    if(j<0) break;
                    int k=n-i-j;
                    if(k<0) continue;
                    int cf=fac[n];
                    cf=(long long)cf*ifac[i]%P;
                    cf=(long long)cf*ifac[j]%P;
                    cf=(long long)cf*ifac[k]%P;
                    if(n&1) cf=(P-cf)%P;
                    terms[ui][cj].push_back(
                        Term{(uint8_t)i,(uint8_t)j,(uint8_t)k,(uint16_t)cf}
                    );
                }
            }
        }
    }

    const int KNUM=3;
    int targetW[KNUM]={286,308,330};
    static uint16_t tw[KNUM][Q], cw[16][Q];
    for(int z=1;z<Q;z++)
        for(int h=0;h<KNUM;h++)
            tw[h][z]=powf(INVF[z],targetW[h]);
    for(int alpha=1;alpha<=15;alpha++)
        for(int z=1;z<Q;z++)
            cw[alpha][z]=powf(INVF[z],22*alpha);

    for(int abase: {1,5}){
        vector<array<uint16_t,KNUM>> Pcoef(Q);

        // First Fourier inversion: exact t-weight coefficient for each c0.
        #pragma omp parallel for schedule(dynamic)
        for(int c0=1;c0<Q;c0++){
            int sums[KNUM]={0,0,0};
            for(int t=1;t<Q;t++){
                int c=MUL[c0][t];
                int d=MUL[t][t];
                int ap[23],cp[23],dp[23];
                ap[0]=cp[0]=dp[0]=1;
                for(int e=1;e<23;e++){
                    ap[e]=MUL[ap[e-1]][abase];
                    cp[e]=MUL[cp[e-1]][c];
                    dp[e]=MUL[dp[e-1]][d];
                }

                array<array<uint16_t,N>,N> A{};
                for(int ui=0;ui<N;ui++) for(int cj=0;cj<N;cj++){
                    int hval=0;
                    for(const auto &tr: terms[ui][cj]){
                        int z=tr.coeff;
                        z=MUL[z][ap[tr.i]];
                        z=MUL[z][cp[tr.j]];
                        z=MUL[z][dp[tr.k]];
                        hval=addf(hval,z);
                    }
                    int val=negf(hval);
                    if((ui+1)==cols[cj]) val=addf(val,1);
                    A[ui][cj]=val;
                }

                int dv=det22(A);
                for(int h=0;h<KNUM;h++)
                    sums[h]=addf(sums[h],MUL[dv][tw[h][t]]);
            }
            for(int h=0;h<KNUM;h++) Pcoef[c0][h]=negf(sums[h]);
        }

        cout << "a=" << abase << "\n";
        for(int h=0;h<KNUM;h++){
            int m=targetW[h]/22;
            cout << "weight=" << targetW[h] << "\n";
            // Second Fourier inversion: exact c^{22 alpha} coefficient.
            for(int beta=1;2*beta<m;beta++){
                int alpha=m-2*beta;
                int sum=0;
                for(int c0=1;c0<Q;c0++)
                    sum=addf(sum,MUL[Pcoef[c0][h]][cw[alpha][c0]]);
                int coeff=negf(sum);
                cout << "  alpha=" << alpha
                     << " beta=" << beta
                     << " coeff=" << coeff
                     << " (re=" << (coeff%P)
                     << ",im=" << (coeff/P) << ")\n";
            }
        }
    }
    return 0;
}
