#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <vector>
#include <omp.h>
using namespace std;

/*
Exact extraction of the complete filtration coefficient

    [t^25308] det(I-H)(a,c=t,d=t^2)

for p=223.  The determinant is the full (p-1)x(p-1) Cartier minor obtained
by deleting row p and column 3.  max_w=1 keeps only the dominant block;
max_w=4 assembles all Cartier blocks.  Identity selections and all
Cauchy-Binet degree sets are included automatically by the determinant.

The coefficient is recovered by multiplicative Fourier inversion over
F_(223^2)^*.  The determinant degree is checked by an exact maximum-weight
assignment.  Frobenius-conjugate evaluation points are paired, reducing the
number of 222x222 determinant evaluations from 49,728 to 24,975.
*/

static constexpr int P = 223;
static constexpr int Q = P * P;
static constexpr int N = P - 1;
static constexpr int TARGET_WEIGHT = 25308;
static constexpr int NEG_INF = -1000000000;

static int NR;
static int INV_P[P];

struct F2 {
    uint16_t a, b;
};

static inline int modp(int x) {
    x %= P;
    if (x < 0) x += P;
    return x;
}
static inline F2 addf(F2 x, F2 y) {
    int a = x.a + y.a; if (a >= P) a -= P;
    int b = x.b + y.b; if (b >= P) b -= P;
    return {(uint16_t)a, (uint16_t)b};
}
static inline F2 subf(F2 x, F2 y) {
    int a = (int)x.a - (int)y.a; if (a < 0) a += P;
    int b = (int)x.b - (int)y.b; if (b < 0) b += P;
    return {(uint16_t)a, (uint16_t)b};
}
static inline F2 negf(F2 x) {
    return {(uint16_t)(x.a ? P - x.a : 0),
            (uint16_t)(x.b ? P - x.b : 0)};
}
static inline F2 conjf(F2 x) {
    return {(uint16_t)x.a, (uint16_t)(x.b ? P - x.b : 0)};
}
static inline bool zerof(F2 x) { return x.a == 0 && x.b == 0; }
static inline F2 mulf(F2 x, F2 y) {
    int a = modp((int)x.a * y.a + NR * (int)x.b * y.b);
    int b = modp((int)x.a * y.b + (int)x.b * y.a);
    return {(uint16_t)a, (uint16_t)b};
}
static inline F2 invf(F2 x) {
    int norm = modp((int)x.a * x.a - NR * (int)x.b * x.b);
    int ni = INV_P[norm];
    return {(uint16_t)modp((int)x.a * ni),
            (uint16_t)modp(-(int)x.b * ni)};
}
static F2 powf(F2 x, long long e) {
    F2 r{1,0};
    while (e) {
        if (e & 1) r = mulf(r, x);
        x = mulf(x, x);
        e >>= 1;
    }
    return r;
}
static int powp(int x, int e) {
    long long r = 1, b = modp(x);
    while (e) {
        if (e & 1) r = r * b % P;
        b = b * b % P;
        e >>= 1;
    }
    return (int)r;
}
static int legendre(int x) { return powp(x, (P - 1) / 2); }

struct Term {
    uint16_t exponent;
    uint16_t coefficient;
};

static vector<Term> TERMS[N * N];
static bool IDENTITY[N * N];
static int COLS[N];

static F2 determinant(vector<F2>& a) {
    F2 det{1,0};
    for (int c = 0; c < N; ++c) {
        int piv = c;
        while (piv < N && zerof(a[(size_t)piv * N + c])) ++piv;
        if (piv == N) return {0,0};
        if (piv != c) {
            for (int j = c; j < N; ++j)
                swap(a[(size_t)piv * N + j], a[(size_t)c * N + j]);
            det = negf(det);
        }
        F2 pv = a[(size_t)c * N + c];
        det = mulf(det, pv);
        F2 ip = invf(pv);
        const size_t prow = (size_t)c * N;
        for (int r = c + 1; r < N; ++r) {
            size_t rr = (size_t)r * N;
            F2 entry = a[rr + c];
            if (zerof(entry)) continue;
            F2 factor = mulf(entry, ip);
            a[rr + c] = {0,0};
            for (int j = c + 1; j < N; ++j)
                a[rr + j] = subf(a[rr + j], mulf(factor, a[prow + j]));
        }
    }
    return det;
}

// Exact integer Hungarian algorithm for maximum-weight perfect assignment.
static long long max_assignment(const vector<vector<int>>& weight) {
    int n = (int)weight.size();
    const long long INF = (1LL << 60);
    vector<long long> u(n + 1), v(n + 1);
    vector<int> p(n + 1), way(n + 1);
    for (int i = 1; i <= n; ++i) {
        p[0] = i;
        int j0 = 0;
        vector<long long> minv(n + 1, INF);
        vector<char> used(n + 1, false);
        do {
            used[j0] = true;
            int i0 = p[j0], j1 = 0;
            long long delta = INF;
            for (int j = 1; j <= n; ++j) if (!used[j]) {
                long long cur = -(long long)weight[i0 - 1][j - 1] - u[i0] - v[j];
                if (cur < minv[j]) { minv[j] = cur; way[j] = j0; }
                if (minv[j] < delta) { delta = minv[j]; j1 = j; }
            }
            for (int j = 0; j <= n; ++j) {
                if (used[j]) { u[p[j]] += delta; v[j] -= delta; }
                else minv[j] -= delta;
            }
            j0 = j1;
        } while (p[j0] != 0);
        do {
            int j1 = way[j0]; p[j0] = p[j1]; j0 = j1;
        } while (j0);
    }
    vector<int> match_row(n + 1);
    for (int j = 1; j <= n; ++j) match_row[p[j]] = j;
    long long ans = 0;
    for (int i = 1; i <= n; ++i) ans += weight[i - 1][match_row[i] - 1];
    return ans;
}

int main(int argc, char** argv) {
    if (argc != 4) {
        cerr << "usage: " << argv[0] << " <quadratic nonsquare nr> <max_w:1|4> <a in F_223>\n";
        return 2;
    }
    NR = stoi(argv[1]);
    int max_w = stoi(argv[2]);
    int abase = modp(stoi(argv[3]));
    if (legendre(NR) != P - 1 || (max_w != 1 && max_w != 4) || abase == 0) {
        cerr << "invalid nr, max_w, or a\n";
        return 2;
    }

    INV_P[0] = 0;
    for (int x = 1; x < P; ++x) INV_P[x] = powp(x, P - 2);

    int fac[P], ifac[P], apow[P];
    fac[0] = 1;
    for (int i = 1; i < P; ++i) fac[i] = (long long)fac[i - 1] * i % P;
    ifac[P - 1] = powp(fac[P - 1], P - 2);
    for (int i = P - 1; i >= 1; --i) ifac[i - 1] = (long long)ifac[i] * i % P;
    apow[0] = 1;
    for (int i = 1; i < P; ++i) apow[i] = (long long)apow[i - 1] * abase % P;

    int ci = 0;
    for (int v = 1; v <= P; ++v) if (v != 3) COLS[ci++] = v;

    vector<vector<int>> max_t(N, vector<int>(N, NEG_INF));
    int max_entry_exp = 0;
    long long term_count = 0;
    for (int ui = 0; ui < N; ++ui) {
        int urow = ui + 1;
        for (int cj = 0; cj < N; ++cj) {
            int vcol = COLS[cj];
            int idx = ui * N + cj;
            if (urow == vcol) {
                IDENTITY[idx] = true;
                max_t[ui][cj] = 0;
            }
            for (int w = 1; w <= min(max_w, urow); ++w) {
                int n = P - 1 - urow + w;
                int target = P * w - vcol;
                if (target < 0) continue;
                int imax = min(n, target / 3);
                for (int i = 0; i <= imax; ++i) {
                    int j = target - 3 * i;
                    int k = n - i - j;
                    if (k < 0) continue;
                    int coeff = fac[n];
                    coeff = (long long)coeff * ifac[i] % P;
                    coeff = (long long)coeff * ifac[j] % P;
                    coeff = (long long)coeff * ifac[k] % P;
                    coeff = (long long)coeff * apow[i] % P;
                    if (n & 1) coeff = coeff ? P - coeff : 0;
                    int exponent = j + 2 * k;
                    TERMS[idx].push_back({(uint16_t)exponent, (uint16_t)coeff});
                    max_t[ui][cj] = max(max_t[ui][cj], exponent);
                    max_entry_exp = max(max_entry_exp, exponent);
                    ++term_count;
                }
            }
        }
    }

    long long degree_bound = max_assignment(max_t);
    if (TARGET_WEIGHT > degree_bound || degree_bound >= Q - 1) {
        cerr << "degree/aliasing check failed: target=" << TARGET_WEIGHT
             << " bound=" << degree_bound << " order=" << Q - 1 << "\n";
        return 3;
    }

    struct EvalPoint { F2 t; F2 character; bool fixed; };
    vector<EvalPoint> points;
    points.reserve((Q - 1 + P - 1) / 2);
    for (int a = 0; a < P; ++a) for (int b = 0; b < P; ++b) {
        if (a == 0 && b == 0) continue;
        F2 t{(uint16_t)a, (uint16_t)b};
        F2 tc = conjf(t);
        int code = a + P * b;
        int ccode = tc.a + P * tc.b;
        if (code > ccode) continue;
        points.push_back({t, powf(invf(t), TARGET_WEIGHT), b == 0});
    }

    cout << "prime=" << P
         << " nr=" << NR
         << " max_w=" << max_w
         << " a=" << abase
         << " target_weight=" << TARGET_WEIGHT
         << " degree_bound=" << degree_bound
         << " multiplicative_order=" << Q - 1
         << " max_entry_exponent=" << max_entry_exp
         << " term_count=" << term_count
         << " frobenius_orbits=" << points.size()
         << " threads=" << omp_get_max_threads() << "\n";
    cout.flush();

    atomic<long long> completed{0};
    auto start = chrono::steady_clock::now();
    vector<F2> thread_sums(omp_get_max_threads(), F2{0,0});

    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        vector<F2> matrix((size_t)N * N);
        vector<F2> tp(max_entry_exp + 1);
        F2 local{0,0};

        #pragma omp for schedule(dynamic,1)
        for (size_t qi = 0; qi < points.size(); ++qi) {
            F2 t = points[qi].t;
            tp[0] = {1,0};
            for (int e = 1; e <= max_entry_exp; ++e) tp[e] = mulf(tp[e - 1], t);

            for (int idx = 0; idx < N * N; ++idx) {
                F2 h{0,0};
                for (const Term& tr : TERMS[idx]) {
                    F2 z = tp[tr.exponent];
                    z.a = (long long)z.a * tr.coefficient % P;
                    z.b = (long long)z.b * tr.coefficient % P;
                    h = addf(h, z);
                }
                F2 value = negf(h);
                if (IDENTITY[idx]) value = addf(value, {1,0});
                matrix[idx] = value;
            }

            F2 dv = determinant(matrix);
            F2 z = mulf(dv, points[qi].character);
            if (points[qi].fixed) local = addf(local, z);
            else {
                // z + Frobenius(z) = 2 Re(z).
                int twice = z.a + z.a; if (twice >= P) twice -= P;
                local = addf(local, {(uint16_t)twice, 0});
            }

            long long done = ++completed;
            if (tid == 0 && done % 1000 == 0) {
                double sec = chrono::duration<double>(chrono::steady_clock::now() - start).count();
                cerr << "progress=" << done << "/" << points.size()
                     << " elapsed_seconds=" << sec << "\n";
            }
        }
        thread_sums[tid] = local;
    }

    F2 sum{0,0};
    for (F2 z : thread_sums) sum = addf(sum, z);
    // (Q-1)^(-1) = -1 in characteristic P.
    F2 coefficient = negf(sum);
    double seconds = chrono::duration<double>(chrono::steady_clock::now() - start).count();

    cout << "{\n"
         << "  \"status\": \"PASS\",\n"
         << "  \"prime\": " << P << ",\n"
         << "  \"quadratic_nonresidue\": " << NR << ",\n"
         << "  \"max_w\": " << max_w << ",\n"
         << "  \"a\": " << abase << ",\n"
         << "  \"target_weight\": " << TARGET_WEIGHT << ",\n"
         << "  \"degree_bound\": " << degree_bound << ",\n"
         << "  \"multiplicative_order\": " << Q - 1 << ",\n"
         << "  \"frobenius_orbits\": " << points.size() << ",\n"
         << "  \"coefficient_real\": " << coefficient.a << ",\n"
         << "  \"coefficient_imag\": " << coefficient.b << ",\n"
         << "  \"nonzero\": " << (coefficient.a || coefficient.b ? "true" : "false") << ",\n"
         << "  \"elapsed_seconds\": " << seconds << "\n"
         << "}\n";
    return coefficient.b == 0 ? 0 : 4;
}
