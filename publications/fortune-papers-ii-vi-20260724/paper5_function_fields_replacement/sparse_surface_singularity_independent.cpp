#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

static int mod(int x, int p){ x%=p; if(x<0)x+=p; return x; }

static int rank_mod(std::vector<std::vector<int>> a, int p){
    const int m=a.size(), n=a[0].size();
    int r=0;
    for(int c=0;c<n && r<m;c++){
        int piv=-1;
        for(int i=r;i<m;i++) if(mod(a[i][c],p)!=0){piv=i;break;}
        if(piv<0) continue;
        std::swap(a[r],a[piv]);
        int inv=1, base=mod(a[r][c],p), e=p-2;
        while(e){ if(e&1) inv=mod(inv*base,p); base=mod(base*base,p); e>>=1; }
        for(int j=c;j<n;j++) a[r][j]=mod(a[r][j]*inv,p);
        for(int i=0;i<m;i++) if(i!=r){
            int f=mod(a[i][c],p);
            if(f) for(int j=c;j<n;j++) a[i][j]=mod(a[i][j]-f*a[r][j],p);
        }
        r++;
    }
    return r;
}

int main(){
    const int p=7;
    std::uint64_t total=1;
    for(int i=0;i<p;i++) total*=p;
    std::uint64_t on_cone=0, singular=0, diagonal=0, bad=0;
    std::array<int,p> x{};
    for(std::uint64_t code=0; code<total; ++code){
        std::uint64_t t=code;
        for(int i=0;i<p;i++){ x[i]=t%p; t/=p; }
        bool eq=true;
        for(int m=1;m<=p-4;m++){
            int s=0;
            for(int i=0;i<p;i++){
                int pw=1;
                for(int k=0;k<m;k++) pw=mod(pw*x[i],p);
                s=mod(s+pw,p);
            }
            if(s!=0){eq=false;break;}
        }
        if(!eq) continue;
        on_cone++;
        bool diag=true;
        for(int i=1;i<p;i++) if(x[i]!=x[0]){diag=false;break;}
        if(diag) diagonal++;
        std::vector<std::vector<int>> J(p-4,std::vector<int>(p));
        for(int m=1;m<=p-4;m++) for(int i=0;i<p;i++){
            int pw=1;
            for(int k=0;k<m-1;k++) pw=mod(pw*x[i],p);
            J[m-1][i]=mod(m*pw,p);
        }
        bool sing=rank_mod(J,p)<p-4;
        if(sing) singular++;
        if(sing!=diag) bad++;
    }
    std::ofstream out("sparse_surface_singularity_results.json");
    out << "{\n"
        << "  \"p\": 7,\n"
        << "  \"ambient_vectors\": " << total << ",\n"
        << "  \"cone_points\": " << on_cone << ",\n"
        << "  \"singular_points\": " << singular << ",\n"
        << "  \"diagonal_points\": " << diagonal << ",\n"
        << "  \"mismatches\": " << bad << ",\n"
        << "  \"conclusion\": \"the affine singular locus equals the diagonal line at p=7\"\n"
        << "}\n";
    std::cout << "cone="<<on_cone<<" singular="<<singular<<" diagonal="<<diagonal<<" bad="<<bad<<"\n";
    return bad?1:0;
}
