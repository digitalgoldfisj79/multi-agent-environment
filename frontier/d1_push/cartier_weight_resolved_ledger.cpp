#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
#include <omp.h>
using namespace std;

/*
Exact weight-resolved Cartier survivor ledger.

Usage:
  g++ -O3 -march=native -fopenmp cartier_weight_resolved_ledger.cpp -o ledger
  OMP_NUM_THREADS=$(nproc) ./ledger <prime p> <quadratic nonsquare nr> <max_w:1|4>

For each square class of a, the program evaluates the complete Cartier cofactor
at

  c=c0*t, d=d0*t^2,

for every c0,d0 in F_p and every nonzero t in F_(p^2). Summation over c0,d0
projects exactly to positive c- and d-exponents divisible by p-1. A
multiplicative Fourier transform in t then separates the exact (1,2)-weight.
The extension-field multiplicative order is checked against an exact Hungarian
assignment bound, so the transform has no degree aliasing.
*/

struct Field {
    int p, q, nr;
    vector<uint16_t> mul, inv;

    Field(int prime, int nonsquare)
        : p(prime), q(prime * prime), nr(nonsquare), mul(q * q), inv(q) {
        for (int x = 0; x < q; ++x) {
            int a = x % p, b = x / p;
            for (int y = 0; y < q; ++y) {
                int c = y % p, d = y / p;
                mul[x * q + y] =
                    (a * c + nr * b * d) % p + p * ((a * d + b * c) % p);
            }
        }
        inv[0] = 0;
        for (int x = 1; x < q; ++x) inv[x] = pow(x, q - 2);
    }

    inline int M(int x, int y) const { return mul[x * q + y]; }
    inline int add(int x, int y) const {
        return ((x % p + y % p) % p) + p * ((x / p + y / p) % p);
    }
    inline int sub(int x, int y) const {
        return ((x % p - y % p + p) % p) +
               p * ((x / p - y / p + p) % p);
    }
    inline int neg(int x) const { return sub(0, x); }

    int pow(int x, long long e) const {
        int out = 1;
        while (e) {
            if (e & 1) out = M(out, x);
            x = M(x, x);
            e >>= 1;
        }
        return out;
    }
};

struct Term {
    uint8_t ai, cj, dk;
    uint16_t coeff;
};

int determinant(vector<uint16_t> a, int n, const Field& F) {
    int out = 1;
    for (int c = 0; c < n; ++c) {
        int pivot = c;
        while (pivot < n && !a[pivot * n + c]) ++pivot;
        if (pivot == n) return 0;
        if (pivot != c) {
            for (int j = c; j < n; ++j)
                swap(a[pivot * n + j], a[c * n + j]);
            out = F.neg(out);
        }
        int pv = a[c * n + c];
        out = F.M(out, pv);
        int ipv = F.inv[pv];
        for (int r = c + 1; r < n; ++r) {
            if (!a[r * n + c]) continue;
            int factor = F.M(a[r * n + c], ipv);
            for (int j = c; j < n; ++j) {
                a[r * n + j] =
                    F.sub(a[r * n + j], F.M(factor, a[c * n + j]));
            }
        }
    }
    return out;
}

long long max_assignment(const vector<vector<int>>& weight) {
    int n = (int)weight.size();
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
                long long cur =
                    -(long long)weight[i0 - 1][j - 1] - u[i0] - v[j];
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
    for (int i = 1; i <= n; ++i)
        answer += weight[i - 1][matched[i] - 1];
    return answer;
}

int modpow(int a, int e, int p) {
    long long out = 1, b = a;
    while (e) {
        if (e & 1) out = out * b % p;
        b = b * b % p;
        e >>= 1;
    }
    return (int)out;
}

int legendre(int a, int p) { return modpow((a % p + p) % p, (p - 1) / 2, p); }

int main(int argc, char** argv) {
    if (argc != 4) {
        cerr << "usage: " << argv[0] << " <prime p> <nonsquare nr> <max_w:1|4>\n";
        return 2;
    }

    int p = stoi(argv[1]);
    int nr = stoi(argv[2]);
    int max_w = stoi(argv[3]);
    if (legendre(nr, p) != p - 1 || (max_w != 1 && max_w != 4)) {
        cerr << "nr must be a quadratic nonsquare and max_w must be 1 or 4\n";
        return 2;
    }

    Field F(p, nr);
    int q = F.q;
    int n = p - 1;

    vector<int> columns;
    for (int v = 1; v <= p; ++v) if (v != 3) columns.push_back(v);

    vector<vector<vector<Term>>> terms(n, vector<vector<Term>>(n));
    vector<vector<int>> max_t(n, vector<int>(n, -1000000));

    vector<int> fac(p), ifac(p);
    fac[0] = 1;
    for (int i = 1; i < p; ++i) fac[i] = (long long)fac[i - 1] * i % p;
    ifac[p - 1] = modpow(fac[p - 1], p - 2, p);
    for (int i = p - 1; i >= 1; --i)
        ifac[i - 1] = (long long)ifac[i] * i % p;

    for (int ui = 0; ui < n; ++ui) {
        int u = ui + 1;
        for (int cj = 0; cj < n; ++cj) {
            int v = columns[cj];
            if (u == v) max_t[ui][cj] = 0;
            for (int w = 1; w <= min(max_w, u); ++w) {
                int row_power = p - 1 - u + w;
                int target = p * w - v;
                for (int ai = 0; ai <= min(row_power, target / 3); ++ai) {
                    int c_degree = target - 3 * ai;
                    int d_degree = row_power - ai - c_degree;
                    if (c_degree < 0 || d_degree < 0) continue;

                    int coeff = fac[row_power];
                    coeff = (long long)coeff * ifac[ai] % p;
                    coeff = (long long)coeff * ifac[c_degree] % p;
                    coeff = (long long)coeff * ifac[d_degree] % p;
                    if (row_power & 1) coeff = (p - coeff) % p;

                    terms[ui][cj].push_back(
                        Term{(uint8_t)ai, (uint8_t)c_degree,
                             (uint8_t)d_degree, (uint16_t)coeff});
                    max_t[ui][cj] =
                        max(max_t[ui][cj], c_degree + 2 * d_degree);
                }
            }
        }
    }

    long long degree_bound = max_assignment(max_t);
    cerr << "prime=" << p
         << " field_order=" << q
         << " max_w=" << max_w
         << " degree_bound=" << degree_bound
         << " multiplicative_order=" << q - 1
         << " threads=" << omp_get_max_threads() << "\n";

    if (degree_bound >= q - 1) {
        cerr << "Fourier aliasing bound failed\n";
        return 3;
    }

    int nonsquare_a = 2;
    while (legendre(nonsquare_a, p) != p - 1) ++nonsquare_a;

    for (int abase : {1, nonsquare_a}) {
        vector<uint16_t> scaled_sum(q);

        #pragma omp parallel for schedule(dynamic)
        for (int t = 1; t < q; ++t) {
            int sum = 0;
            int t2 = F.M(t, t);

            for (int c0 = 0; c0 < p; ++c0) {
                int c = F.M(c0, t);
                for (int d0 = 0; d0 < p; ++d0) {
                    int d = F.M(d0, t2);

                    vector<int> ap(p), cp(p), dp(p);
                    ap[0] = cp[0] = dp[0] = 1;
                    for (int e = 1; e < p; ++e) {
                        ap[e] = F.M(ap[e - 1], abase);
                        cp[e] = F.M(cp[e - 1], c);
                        dp[e] = F.M(dp[e - 1], d);
                    }

                    vector<uint16_t> matrix(n * n);
                    for (int ui = 0; ui < n; ++ui) {
                        for (int cj = 0; cj < n; ++cj) {
                            int h = 0;
                            for (const Term& term : terms[ui][cj]) {
                                int z = term.coeff;
                                z = F.M(z, ap[term.ai]);
                                z = F.M(z, cp[term.cj]);
                                z = F.M(z, dp[term.dk]);
                                h = F.add(h, z);
                            }
                            int value = F.neg(h);
                            if (ui + 1 == columns[cj]) value = F.add(value, 1);
                            matrix[ui * n + cj] = value;
                        }
                    }
                    sum = F.add(sum, determinant(matrix, n, F));
                }
            }
            scaled_sum[t] = sum;
        }

        vector<pair<int, int>> nonzero;
        int low_sum = 0;
        int tail_sum = 0;
        int total_sum = 0;
        long long boundary = ((long long)p * p - 1) / 2;

        for (int weight = 0; weight <= degree_bound; ++weight) {
            int fourier_sum = 0;
            for (int t = 1; t < q; ++t) {
                int character = F.pow(F.inv[t], weight);
                fourier_sum =
                    F.add(fourier_sum, F.M(scaled_sum[t], character));
            }
            // 1/(q-1) = -1 in characteristic p.
            int coefficient = F.neg(fourier_sum);
            if (coefficient / p != 0) {
                cerr << "non-base-field coefficient at weight " << weight
                     << ": " << coefficient << "\n";
                return 4;
            }
            int value = coefficient % p;
            if (!value) continue;

            nonzero.push_back({weight, value});
            total_sum = (total_sum + value) % p;
            if (weight <= boundary)
                low_sum = (low_sum + value) % p;
            else
                tail_sum = (tail_sum + value) % p;
        }

        cout << "RESULT prime=" << p
             << " max_w=" << max_w
             << " a=" << abase
             << " square_class=" << (abase == 1 ? "square" : "nonsquare")
             << " degree_bound=" << degree_bound
             << " boundary=" << boundary
             << " total=" << total_sum
             << " low=" << low_sum
             << " tail=" << tail_sum
             << " nonzero_weight_count=" << nonzero.size()
             << " weights=";
        for (auto [weight, value] : nonzero)
            cout << weight << ":" << value << ",";
        cout << "\n";
    }

    return 0;
}
