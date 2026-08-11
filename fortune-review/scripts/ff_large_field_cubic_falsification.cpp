#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// Independent exact cubic census for scalar bilateral endpoint incidences.
// A monic cubic is x^3+a2*x^2+a1*x+a0, stored as a0,a1,a2.
namespace {
int q;
struct Poly { int a[3]; };
using V = std::array<int, 3>;

int modq(long long x) { x %= q; if (x < 0) x += q; return static_cast<int>(x); }
int inverse_scalar(int a) {
    long long result = 1, base = modq(a), exponent = q - 2;
    while (exponent) {
        if (exponent & 1) result = result * base % q;
        base = base * base % q;
        exponent >>= 1;
    }
    return static_cast<int>(result);
}
long long key(const Poly& p) { return p.a[0] + 1LL*q*p.a[1] + 1LL*q*q*p.a[2]; }
bool has_root(const Poly& p) {
    for (int x = 0; x < q; ++x)
        if (modq(((1LL*x + p.a[2])*x + p.a[1])*x + p.a[0]) == 0) return true;
    return false;
}
V scale(V x, int c) { for (int& v : x) v = modq(1LL*v*c); return x; }
V difference(const Poly& a, const Poly& b) {
    return {modq(a.a[0]-b.a[0]), modq(a.a[1]-b.a[1]), modq(a.a[2]-b.a[2])};
}
V multiply_mod(V x, V y, const Poly& modulus) {
    long long z[5] = {};
    for (int i=0;i<3;++i) for (int j=0;j<3;++j) z[i+j] += 1LL*x[i]*y[j];
    for (int degree=4; degree>=3; --degree) {
        int c = modq(z[degree]);
        z[degree] = 0;
        z[degree-1] -= 1LL*c*modulus.a[2];
        z[degree-2] -= 1LL*c*modulus.a[1];
        z[degree-3] -= 1LL*c*modulus.a[0];
    }
    return {modq(z[0]), modq(z[1]), modq(z[2])};
}
V power_mod(V base, long long exponent, const Poly& modulus) {
    V result = {1,0,0};
    while (exponent) {
        if (exponent & 1) result = multiply_mod(result, base, modulus);
        base = multiply_mod(base, base, modulus);
        exponent >>= 1;
    }
    return result;
}
Poly affine_transform(const Poly& p, int lambda, int shift) {
    const int il = inverse_scalar(lambda);
    const int il2 = modq(1LL*il*il);
    const int il3 = modq(1LL*il2*il);
    Poly out;
    out.a[2] = modq((3LL*shift + p.a[2])*il);
    out.a[1] = modq((3LL*shift*shift + 2LL*p.a[2]*shift + p.a[1])*il2);
    out.a[0] = modq((1LL*shift*shift*shift + 1LL*p.a[2]*shift*shift +
                     1LL*p.a[1]*shift + p.a[0])*il3);
    return out;
}
struct Seed { int p, s, pp, sp, lambda, rho; };
struct Census { int p_orbits; int seed_orbits; long long incidences; };

Census run_census(int field_q) {
    q = field_q;
    std::vector<Poly> band;
    std::unordered_map<long long,int> index;
    index.reserve(static_cast<size_t>(q)*q*q*2);
    for (int a2=0;a2<q;++a2) for (int a1=0;a1<q;++a1) for (int a0=0;a0<q;++a0) {
        Poly p{{a0,a1,a2}};
        if (!has_root(p)) { index[key(p)] = static_cast<int>(band.size()); band.push_back(p); }
    }
    const int n = static_cast<int>(band.size());
    if (n != (q*q*q-q)/3) throw std::runtime_error("irreducible cubic count mismatch");

    std::vector<V> lmod(n), linv(n);
    const V x = {0,1,0};
    for (int i=0;i<n;++i) {
        lmod[i] = power_mod(x, q, band[i]);
        lmod[i][1] = modq(lmod[i][1]-1); // x^q-x mod P
        linv[i] = power_mod(lmod[i], 1LL*q*q*q-2, band[i]);
    }

    // One representative of every AGL(1,q)-orbit of irreducible cubics.
    std::vector<int> representatives;
    std::unordered_set<long long> seen;
    for (int i=0;i<n;++i) {
        if (seen.count(key(band[i]))) continue;
        long long minimum = INT64_MAX;
        for (int lambda=1;lambda<q;++lambda) for (int shift=0;shift<q;++shift) {
            const long long k = key(affine_transform(band[i],lambda,shift));
            seen.insert(k);
            if (k < minimum) minimum = k;
        }
        representatives.push_back(index.at(minimum));
    }

    std::vector<Seed> seeds;
    for (int ip : representatives) for (int ipp=0; ipp<n; ++ipp) {
        if (ip == ipp) continue;
        const V pp_mod_p = difference(band[ipp], band[ip]);
        const V p_mod_pp = scale(pp_mod_p,-1);
        for (int lambda=1; lambda<q; ++lambda) {
            // P | L S-lambda P' determines S.
            const V s_mod_p = multiply_mod(linv[ip], scale(pp_mod_p,lambda), band[ip]);
            Poly s = band[ip];
            for (int j=0;j<3;++j) s.a[j] = modq(s.a[j]+s_mod_p[j]);
            auto is_it = index.find(key(s));
            if (is_it == index.end() || is_it->second == ip) continue;
            const int is = is_it->second;

            // P' | L S'+lambda P determines S'.
            const V sp_mod_pp = multiply_mod(linv[ipp], scale(p_mod_pp,-lambda), band[ipp]);
            Poly sp = band[ipp];
            for (int j=0;j<3;++j) sp.a[j] = modq(sp.a[j]+sp_mod_pp[j]);
            auto isp_it = index.find(key(sp));
            if (isp_it == index.end() || isp_it->second == ipp || isp_it->second == is) continue;
            const int isp = isp_it->second;

            // Solve S | L P+rho S', then test S' | L P'-rho S.
            const V p_mod_s = difference(band[ip], band[is]);
            const V lp_mod_s = multiply_mod(lmod[is], p_mod_s, band[is]);
            const V sp_mod_s = difference(band[isp], band[is]);
            int rho = 0;
            for (int j=0;j<3;++j) if (sp_mod_s[j]) {
                rho = modq(-1LL*lp_mod_s[j]*inverse_scalar(sp_mod_s[j]));
                break;
            }
            if (!rho) continue;
            bool ok = true;
            for (int j=0;j<3;++j)
                if (modq(lp_mod_s[j]+1LL*rho*sp_mod_s[j])) ok=false;
            if (!ok) continue;
            const V pp_mod_sp = difference(band[ipp], band[isp]);
            const V lpp_mod_sp = multiply_mod(lmod[isp], pp_mod_sp, band[isp]);
            const V s_mod_sp = difference(band[is], band[isp]);
            for (int j=0;j<3;++j)
                if (modq(lpp_mod_sp[j]-1LL*rho*s_mod_sp[j])) ok=false;
            if (!ok) continue;
            seeds.push_back({ip,is,ipp,isp,lambda,rho});
        }
    }

    std::set<std::array<long long,4>> incidence_quads;
    for (const Seed& seed : seeds)
        for (int lambda=1;lambda<q;++lambda) for (int shift=0;shift<q;++shift)
            incidence_quads.insert({
                key(affine_transform(band[seed.p],lambda,shift)),
                key(affine_transform(band[seed.s],lambda,shift)),
                key(affine_transform(band[seed.pp],lambda,shift)),
                key(affine_transform(band[seed.sp],lambda,shift))
            });

    return {static_cast<int>(representatives.size()), static_cast<int>(seeds.size()),
            static_cast<long long>(incidence_quads.size())};
}
} // namespace

int main() {
    const std::map<int,std::pair<int,long long>> expected = {
        {5,{0,0}}, {7,{0,0}}, {11,{2,220}}, {13,{0,0}}, {17,{2,544}},
        {19,{2,684}}, {23,{0,0}}, {29,{2,1624}}, {31,{2,1860}},
        {37,{4,5328}}, {41,{6,9840}}, {43,{6,10836}}, {47,{2,4324}},
        {53,{6,16536}}, {59,{4,13688}}
    };
    bool ok = true;
    std::cout << "status=EMPIRICAL-EXACT FINITE PANEL / FALSIFICATION\n";
    std::cout << "q k P_orbits defect_orbits incidences expected\n";
    for (const auto& [field_q,want] : expected) {
        const Census got = run_census(field_q);
        const bool row_ok = got.seed_orbits == want.first && got.incidences == want.second;
        ok = ok && row_ok;
        std::cout << field_q << " 3 " << got.p_orbits << " " << got.seed_orbits << " "
                  << got.incidences << " " << (row_ok ? "PASS" : "FAIL") << "\n";
    }
    if (!ok) return 1;
    std::cout << "PASS q>k emptiness is falsified by exact cubic panels\n";
    std::cout << "PASS nonzero-defect incidence counts are unions of full AGL(1,q) orbits\n";
    return 0;
}
