#include <array>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
#include <omp.h>

using namespace std;

constexpr int P = 29;
constexpr int FF = P * P;
constexpr int DIM = P - 1;
constexpr int WT = 448;
constexpr int CDEG = 224;

static uint16_t mul_table[FF][FF];
static uint16_t inv_table[FF];
static int nr;
static int columns[DIM];

struct Term {
    uint8_t ai, cj, dk;
    uint16_t coeff;
};
static vector<Term> entry_terms[DIM][DIM];

inline int addf(int x, int y) {
    return ((x % P + y % P) % P) + P * ((x / P + y / P) % P);
}
inline int subf(int x, int y) {
    return ((x % P - y % P + P) % P) + P * ((x / P - y / P + P) % P);
}
inline int negf(int x) { return subf(0, x); }

int powf(int x, long long e) {
    int out = 1;
    while (e) {
        if (e & 1) out = mul_table[out][x];
        x = mul_table[x][x];
        e >>= 1;
    }
    return out;
}

int det28(array<array<uint16_t, DIM>, DIM> a) {
    int out = 1;
    for (int c = 0; c < DIM; ++c) {
        int pivot = c;
        while (pivot < DIM && a[pivot][c] == 0) ++pivot;
        if (pivot == DIM) return 0;
        if (pivot != c) {
            swap(a[pivot], a[c]);
            out = negf(out);
        }
        int pv = a[c][c];
        out = mul_table[out][pv];
        int ip = inv_table[pv];
        for (int r = c + 1; r < DIM; ++r) {
            if (!a[r][c]) continue;
            int factor = mul_table[a[r][c]][ip];
            for (int j = c; j < DIM; ++j) {
                a[r][j] = subf(a[r][j], mul_table[factor][a[c][j]]);
            }
        }
    }
    return out;
}

long long max_assignment(const vector<vector<int>>& w) {
    int n = (int)w.size();
    const long long INF = numeric_limits<long long>::max() / 4;
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
                long long cur = -(long long)w[i0 - 1][j - 1] - u[i0] - v[j];
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
    vector<int> matched(n + 1);
    for (int j = 1; j <= n; ++j) matched[p[j]] = j;
    long long answer = 0;
    for (int i = 1; i <= n; ++i) answer += w[i - 1][matched[i] - 1];
    return answer;
}

int legendre(int x) {
    int r = 1;
    int b = (x % P + P) % P;
    int e = (P - 1) / 2;
    while (e) {
        if (e & 1) r = (long long)r * b % P;
        b = (long long)b * b % P;
        e >>= 1;
    }
    return r;
}

void init_field(int nonsquare) {
    nr = nonsquare;
    for (int x = 0; x < FF; ++x) {
        int a = x % P, b = x / P;
        for (int y = 0; y < FF; ++y) {
            int c = y % P, d = y / P;
            int real = (a * c + nr * b * d) % P;
            int imag = (a * d + b * c) % P;
            mul_table[x][y] = real + P * imag;
        }
    }
    inv_table[0] = 0;
    for (int x = 1; x < FF; ++x) inv_table[x] = powf(x, FF - 2);
}

struct Extraction {
    int square_coeff;
    int nonsquare_coeff;
    long long t_bound;
    long long c_bound;
};

Extraction extract(int max_w) {
    for (int r = 0; r < DIM; ++r)
        for (int c = 0; c < DIM; ++c)
            entry_terms[r][c].clear();

    int fac[P], ifac[P];
    fac[0] = 1;
    for (int i = 1; i < P; ++i) fac[i] = (long long)fac[i - 1] * i % P;
    ifac[P - 1] = P - 1;
    for (int i = P - 1; i >= 1; --i) ifac[i - 1] = (long long)ifac[i] * i % P;

    int idx = 0;
    for (int v = 1; v <= P; ++v) if (v != 3) columns[idx++] = v;

    vector<vector<int>> max_t(DIM, vector<int>(DIM, -1000000));
    vector<vector<int>> max_c(DIM, vector<int>(DIM, -1000000));

    for (int ui = 0; ui < DIM; ++ui) {
        int u = ui + 1;
        for (int ci = 0; ci < DIM; ++ci) {
            int v = columns[ci];
            if (u == v) {
                max_t[ui][ci] = 0;
                max_c[ui][ci] = 0;
            }
            for (int w = 1; w <= min(max_w, u); ++w) {
                int n = P - 1 - u + w;
                int target = P * w - v;
                for (int ai = 0; ai <= min(n, target / 3); ++ai) {
                    int cj = target - 3 * ai;
                    int dk = n - ai - cj;
                    if (cj < 0 || dk < 0) continue;
                    int coeff = fac[n];
                    coeff = (long long)coeff * ifac[ai] % P;
                    coeff = (long long)coeff * ifac[cj] % P;
                    coeff = (long long)coeff * ifac[dk] % P;
                    if (n & 1) coeff = (P - coeff) % P;
                    entry_terms[ui][ci].push_back(
                        Term{(uint8_t)ai, (uint8_t)cj, (uint8_t)dk, (uint16_t)coeff}
                    );
                    max_t[ui][ci] = max(max_t[ui][ci], cj + 2 * dk);
                    max_c[ui][ci] = max(max_c[ui][ci], cj);
                }
            }
        }
    }

    long long t_bound = max_assignment(max_t);
    long long c_bound = max_assignment(max_c);
    if (t_bound >= FF - 1 || c_bound >= FF - 1) {
        cerr << "aliasing bound failed: " << t_bound << " " << c_bound << "\n";
        exit(3);
    }

    static uint16_t t_character[FF], c_character[FF];
    for (int z = 1; z < FF; ++z) {
        t_character[z] = powf(inv_table[z], WT);
        c_character[z] = powf(inv_table[z], CDEG);
    }

    int answers[2] = {0, 0};
    int abase_values[2] = {1, 2};

    for (int which = 0; which < 2; ++which) {
        int abase = abase_values[which];
        vector<uint16_t> first_transform(FF);

        #pragma omp parallel for schedule(dynamic)
        for (int c0 = 1; c0 < FF; ++c0) {
            int accum = 0;
            for (int t = 1; t < FF; ++t) {
                int cval = mul_table[c0][t];
                int dval = mul_table[t][t];

                int ap[P], cp[P], dp[P];
                ap[0] = cp[0] = dp[0] = 1;
                for (int e = 1; e < P; ++e) {
                    ap[e] = mul_table[ap[e - 1]][abase];
                    cp[e] = mul_table[cp[e - 1]][cval];
                    dp[e] = mul_table[dp[e - 1]][dval];
                }

                array<array<uint16_t, DIM>, DIM> matrix{};
                for (int ui = 0; ui < DIM; ++ui) {
                    for (int ci = 0; ci < DIM; ++ci) {
                        int h = 0;
                        for (const Term& term : entry_terms[ui][ci]) {
                            int z = term.coeff;
                            z = mul_table[z][ap[term.ai]];
                            z = mul_table[z][cp[term.cj]];
                            z = mul_table[z][dp[term.dk]];
                            h = addf(h, z);
                        }
                        int value = negf(h);
                        if (ui + 1 == columns[ci]) value = addf(value, 1);
                        matrix[ui][ci] = value;
                    }
                }

                int determinant_value = det28(matrix);
                accum = addf(accum, mul_table[determinant_value][t_character[t]]);
            }
            first_transform[c0] = negf(accum);
        }

        int accum = 0;
        for (int c0 = 1; c0 < FF; ++c0) {
            accum = addf(accum, mul_table[first_transform[c0]][c_character[c0]]);
        }
        answers[which] = negf(accum);
    }

    return Extraction{answers[0], answers[1], t_bound, c_bound};
}

int main(int argc, char** argv) {
    if (argc != 2) {
        cerr << "usage: " << argv[0] << " <quadratic nonsquare mod 29>\n";
        return 2;
    }
    int nonsquare = stoi(argv[1]);
    if (legendre(nonsquare) != P - 1) {
        cerr << "parameter is not a nonsquare mod 29\n";
        return 2;
    }

    init_field(nonsquare);
    for (int max_w : {1, 4}) {
        Extraction e = extract(max_w);
        cout << "nr=" << nonsquare
             << " max_w=" << max_w
             << " t_bound=" << e.t_bound
             << " c_bound=" << e.c_bound
             << " a1=" << e.square_coeff
             << " a1_real=" << e.square_coeff % P
             << " a1_imag=" << e.square_coeff / P
             << " a2=" << e.nonsquare_coeff
             << " a2_real=" << e.nonsquare_coeff % P
             << " a2_imag=" << e.nonsquare_coeff / P
             << "\n";
    }
    return 0;
}
