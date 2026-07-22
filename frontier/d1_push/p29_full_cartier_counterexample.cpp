#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

/*
Exact p=29 audit of the first Cartier support-law counterexample.

Build:
  g++ -O3 -march=native -fopenmp p29_full_cartier_counterexample.cpp -o p29_audit
Run independently in two quadratic field models and in the w=1/full modes:
  OMP_NUM_THREADS=$(nproc) ./p29_audit 2 1
  OMP_NUM_THREADS=$(nproc) ./p29_audit 2 4
  OMP_NUM_THREADS=$(nproc) ./p29_audit 3 1
  OMP_NUM_THREADS=$(nproc) ./p29_audit 3 4

The argument nr must be a quadratic nonsquare modulo 29. The program works in
F_29[s]/(s^2-nr), whose multiplicative group has order 840. It extracts
[c^224 d^112] det(I-H) by setting c=c0*t, d=t^2 and applying exact
multiplicative Fourier inversion first in t (weight 448), then in c0.

The max_w argument is 1 for the dominant filtration block or 4 for the full
Cartier matrix. The exact tropical assignment bounds printed by the program
verify that the relevant degrees are below 840, so there is no aliasing.
*/

static const int P = 29;
static const int Q = P * P;
static const int N = P - 1;
static const int TARGET_WEIGHT = 448;
static const int TARGET_C_DEGREE = 224;

static int NR;
static uint16_t MUL[Q][Q], INVF[Q];
static int cols[N];

struct Term {
    uint8_t i, j, k, w;
    uint16_t coeff;
};
static vector<Term> terms[N][N];

inline int addf(int x, int y) {
    return ((x % P + y % P) % P) + P * ((x / P + y / P) % P);
}
inline int subf(int x, int y) {
    return ((x % P - y % P + P) % P) +
           P * ((x / P - y / P + P) % P);
}
inline int negf(int x) { return subf(0, x); }

int powf(int x, long long e) {
    int r = 1;
    while (e) {
        if (e & 1) r = MUL[r][x];
        x = MUL[x][x];
        e >>= 1;
    }
    return r;
}

int det_field(array<array<uint16_t, N>, N> A) {
    int det = 1;
    for (int c = 0; c < N; ++c) {
        int piv = c;
        while (piv < N && A[piv][c] == 0) ++piv;
        if (piv == N) return 0;
        if (piv != c) {
            swap(A[piv], A[c]);
            det = negf(det);
        }
        int pv = A[c][c];
        det = MUL[det][pv];
        int ip = INVF[pv];
        for (int r = c + 1; r < N; ++r) {
            if (!A[r][c]) continue;
            int factor = MUL[A[r][c]][ip];
            for (int j = c; j < N; ++j) {
                A[r][j] = subf(A[r][j], MUL[factor][A[c][j]]);
            }
        }
    }
    return det;
}

// Exact integer Hungarian algorithm for a maximum-weight perfect assignment.
long long max_assignment(const vector<vector<int>>& weight) {
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
                if (cur < minv[j]) {
                    minv[j] = cur;
                    way[j] = j0;
                }
                if (minv[j] < delta) {
                    delta = minv[j];
                    j1 = j;
                }
            }
            for (int j = 0; j <= n; ++j) {
                if (used[j]) {
                    u[p[j]] += delta;
                    v[j] -= delta;
                } else {
                    minv[j] -= delta;
                }
            }
            j0 = j1;
        } while (p[j0] != 0);
        do {
            int j1 = way[j0];
            p[j0] = p[j1];
            j0 = j1;
        } while (j0);
    }
    vector<int> match_row(n + 1);
    for (int j = 1; j <= n; ++j) match_row[p[j]] = j;
    long long ans = 0;
    for (int i = 1; i <= n; ++i) ans += weight[i - 1][match_row[i] - 1];
    return ans;
}

int legendre(int a) {
    long long r = 1, b = (a % P + P) % P;
    int e = (P - 1) / 2;
    while (e) {
        if (e & 1) r = r * b % P;
        b = b * b % P;
        e >>= 1;
    }
    return (int)r;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        cerr << "usage: " << argv[0] << " <quadratic-nonsquare nr> <max_w:1|4>\n";
        return 2;
    }
    NR = stoi(argv[1]);
    int max_w = stoi(argv[2]);
    if (legendre(NR) != P - 1 || (max_w != 1 && max_w != 4)) {
        cerr << "nr must be a nonsquare mod 29 and max_w must be 1 or 4\n";
        return 2;
    }

    for (int x = 0; x < Q; ++x) for (int y = 0; y < Q; ++y) {
        int a = x % P, b = x / P, c = y % P, d = y / P;
        MUL[x][y] = (a * c + NR * b * d) % P +
                    P * ((a * d + b * c) % P);
    }
    INVF[0] = 0;
    for (int x = 1; x < Q; ++x) INVF[x] = powf(x, Q - 2);

    int fac[P], ifac[P];
    fac[0] = 1;
    for (int i = 1; i < P; ++i) fac[i] = (long long)fac[i - 1] * i % P;
    auto modpow = [](int a, int e) {
        long long r = 1, b = a;
        while (e) {
            if (e & 1) r = r * b % P;
            b = b * b % P;
            e >>= 1;
        }
        return (int)r;
    };
    ifac[P - 1] = modpow(fac[P - 1], P - 2);
    for (int i = P - 1; i >= 1; --i) ifac[i - 1] = (long long)ifac[i] * i % P;

    int ci = 0;
    for (int v = 1; v <= P; ++v) if (v != 3) cols[ci++] = v;

    vector<vector<int>> max_t(N, vector<int>(N, -1000000));
    vector<vector<int>> max_c(N, vector<int>(N, -1000000));

    for (int ui = 0; ui < N; ++ui) {
        int urow = ui + 1;
        for (int cj = 0; cj < N; ++cj) {
            int vcol = cols[cj];
            if (urow == vcol) {
                max_t[ui][cj] = 0;
                max_c[ui][cj] = 0;
            }
            for (int w = 1; w <= min(max_w, urow); ++w) {
                int n = P - 1 - urow + w;
                int target = P * w - vcol;
                for (int i = 0; i <= min(n, target / 3); ++i) {
                    int j = target - 3 * i;
                    if (j < 0) break;
                    int k = n - i - j;
                    if (k < 0) continue;
                    int cf = fac[n];
                    cf = (long long)cf * ifac[i] % P;
                    cf = (long long)cf * ifac[j] % P;
                    cf = (long long)cf * ifac[k] % P;
                    if (n & 1) cf = (P - cf) % P;
                    terms[ui][cj].push_back(
                        Term{(uint8_t)i, (uint8_t)j, (uint8_t)k,
                             (uint8_t)w, (uint16_t)cf}
                    );
                    max_t[ui][cj] = max(max_t[ui][cj], j + 2 * k);
                    max_c[ui][cj] = max(max_c[ui][cj], j);
                }
            }
        }
    }

    long long t_degree_bound = max_assignment(max_t);
    long long c_degree_bound = max_assignment(max_c);
    if (t_degree_bound >= Q - 1 || c_degree_bound >= Q - 1) {
        cerr << "Fourier aliasing bound failed\n";
        return 3;
    }

    static uint16_t tw[Q], cw[Q];
    for (int z = 1; z < Q; ++z) {
        tw[z] = powf(INVF[z], TARGET_WEIGHT);
        cw[z] = powf(INVF[z], TARGET_C_DEGREE);
    }

    cout << "prime=" << P
         << " nr=" << NR
         << " max_w=" << max_w
         << " field_order=" << Q
         << " multiplicative_order=" << Q - 1
         << " t_degree_bound=" << t_degree_bound
         << " c_degree_bound=" << c_degree_bound
         << " threads=" << omp_get_max_threads() << "\n";

    for (int abase : {1, 2}) {
        vector<uint16_t> t_coeff(Q);

        #pragma omp parallel for schedule(dynamic)
        for (int c0 = 1; c0 < Q; ++c0) {
            int sum = 0;
            for (int t = 1; t < Q; ++t) {
                int c = MUL[c0][t];
                int d = MUL[t][t];
                int ap[P], cp[P], dp[P];
                ap[0] = cp[0] = dp[0] = 1;
                for (int e = 1; e < P; ++e) {
                    ap[e] = MUL[ap[e - 1]][abase];
                    cp[e] = MUL[cp[e - 1]][c];
                    dp[e] = MUL[dp[e - 1]][d];
                }

                array<array<uint16_t, N>, N> A{};
                for (int ui = 0; ui < N; ++ui) {
                    for (int cj = 0; cj < N; ++cj) {
                        int hval = 0;
                        for (const auto& tr : terms[ui][cj]) {
                            int z = tr.coeff;
                            z = MUL[z][ap[tr.i]];
                            z = MUL[z][cp[tr.j]];
                            z = MUL[z][dp[tr.k]];
                            hval = addf(hval, z);
                        }
                        int val = negf(hval);
                        if ((ui + 1) == cols[cj]) val = addf(val, 1);
                        A[ui][cj] = val;
                    }
                }
                int dv = det_field(A);
                sum = addf(sum, MUL[dv][tw[t]]);
            }
            t_coeff[c0] = negf(sum);
        }

        int sum = 0;
        for (int c0 = 1; c0 < Q; ++c0) {
            sum = addf(sum, MUL[t_coeff[c0]][cw[c0]]);
        }
        int coeff = negf(sum);
        cout << "a=" << abase
             << " coefficient=" << coeff
             << " real=" << coeff % P
             << " imag=" << coeff / P << "\n";
    }
    return 0;
}
