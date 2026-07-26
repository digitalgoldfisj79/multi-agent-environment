#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using Poly = std::vector<int>;

static int modp(long long x, int p) {
    x %= p;
    if (x < 0) x += p;
    return static_cast<int>(x);
}

static Poly mul_mod(const Poly& u, const Poly& v, const Poly& g, int p) {
    const int n = p;
    std::vector<int> tmp(2 * n - 1, 0);
    for (int i = 0; i < n; ++i) if (u[i]) {
        for (int j = 0; j < n; ++j) if (v[j]) {
            tmp[i + j] = modp(tmp[i + j] + static_cast<long long>(u[i]) * v[j], p);
        }
    }
    // x^p = g(x), with deg(g)<=3. Descending reduction is exact.
    for (int k = 2 * n - 2; k >= n; --k) {
        int c = tmp[k];
        if (!c) continue;
        tmp[k] = 0;
        int shift = k - n;
        for (int j = 0; j <= 3; ++j) {
            tmp[shift + j] = modp(tmp[shift + j] + static_cast<long long>(c) * g[j], p);
        }
    }
    tmp.resize(n);
    return tmp;
}

static bool has_fp_root(int p, int a, int b, int c, int d) {
    for (int x = 0; x < p; ++x) {
        long long x2 = 1LL * x * x % p;
        long long x3 = x2 * x % p;
        // x^p=x in F_p.
        if (modp(x + 1LL * a * x3 + 1LL * b * x2 + 1LL * c * x + d, p) == 0) return true;
    }
    return false;
}

static bool irreducible_special(int p, int a, int b, int c, int d) {
    if (has_fp_root(p, a, b, c, d)) return false;

    // In F_p[x]/(f), x^p = g(x) = -(a x^3+b x^2+c x+d).
    Poly g(p, 0);
    g[0] = modp(-d, p);
    g[1] = modp(-c, p);
    g[2] = modp(-b, p);
    g[3] = modp(-a, p);

    // Precompute g^i, the Frobenius images of x^i.
    std::vector<Poly> gpows(p, Poly(p, 0));
    gpows[0][0] = 1;
    for (int i = 1; i < p; ++i) gpows[i] = mul_mod(gpows[i - 1], g, g, p);

    Poly y(p, 0);
    y[1] = 1; // x
    for (int step = 0; step < p; ++step) {
        Poly next(p, 0);
        for (int i = 0; i < p; ++i) if (y[i]) {
            for (int j = 0; j < p; ++j) if (gpows[i][j]) {
                next[j] = modp(next[j] + static_cast<long long>(y[i]) * gpows[i][j], p);
            }
        }
        y.swap(next);
    }
    // Degree p is prime. No F_p root plus x^(p^p)=x implies irreducible.
    if (y[1] != 1) return false;
    for (int i = 0; i < p; ++i) if (i != 1 && y[i] != 0) return false;
    return true;
}

struct Expected { int p; long long I4; };

int main(int argc, char** argv) {
    std::vector<Expected> tests = {{5,124}, {7,426}, {11,1660}, {13,1572}};
    if (argc > 1 && std::string(argv[1]) == "--extended") {
        tests.push_back({17,4640});
        tests.push_back({23,9636});
    }

    for (const auto& test : tests) {
        const int p = test.p;
        long long total = 0, a0 = 0, square = 0, nonsquare = 0;
        for (int a = 0; a < p; ++a) {
            bool sq = a != 0 && [&]() {
                for (int x = 1; x < p; ++x) if (x * x % p == a) return true;
                return false;
            }();
            for (int b = 0; b < p; ++b)
            for (int c = 0; c < p; ++c)
            for (int d = 0; d < p; ++d) {
                if (!irreducible_special(p, a, b, c, d)) continue;
                ++total;
                if (a == 0) ++a0;
                else if (sq) ++square;
                else ++nonsquare;
            }
        }
        std::cout << "p=" << p << " I4=" << total << " a0=" << a0
                  << " square=" << square << " nonsquare=" << nonsquare << "\n";
        if (total != test.I4) {
            std::cerr << "expected I4=" << test.I4 << "\n";
            return 1;
        }
    }
    std::cout << "P_CYCLE_FIXED_POINT_CENSUS_VERIFY: PASS\n";
    return 0;
}
