#include <algorithm>
#include <iostream>
#include <map>
#include <random>
#include <vector>
using namespace std;

int mod_rank(vector<vector<int>> a, int p) {
    const int n = a.size(), m = a.empty() ? 0 : a[0].size();
    int rank = 0;
    for (int col = 0; col < m && rank < n; ++col) {
        int pivot = rank;
        while (pivot < n && ((a[pivot][col] % p) + p) % p == 0) ++pivot;
        if (pivot == n) continue;
        swap(a[pivot], a[rank]);
        int value = ((a[rank][col] % p) + p) % p, inverse = 1;
        for (int x = 1; x < p; ++x) if (value * x % p == 1) { inverse = x; break; }
        for (int j = col; j < m; ++j) a[rank][j] = a[rank][j] * inverse % p;
        for (int i = 0; i < n; ++i) if (i != rank) {
            int factor = ((a[i][col] % p) + p) % p;
            if (factor) for (int j = col; j < m; ++j)
                a[i][j] = (a[i][j] - factor * a[rank][j]) % p;
        }
        ++rank;
    }
    return rank;
}

vector<vector<int>> hankel(const vector<int>& lambda, int r, int s, int N) {
    vector<vector<int>> b(r, vector<int>(s));
    for (int i = 1; i <= r; ++i)
        for (int j = 1; j <= s; ++j)
            if (i + j <= N) b[i-1][j-1] = lambda[i+j];
    return b;
}

void exhaustive(int p) {
    int N = p - 4;
    long long total = 1;
    for (int i = 0; i < N; ++i) total *= p;
    vector<int> lambda(N + 1);
    for (int r = 1; r < p; ++r) {
        int s = p - r;
        map<int, long long> distribution;
        for (long long code = 1; code < total; ++code) {
            long long t = code;
            for (int k = 1; k <= N; ++k) { lambda[k] = t % p; t /= p; }
            distribution[mod_rank(hankel(lambda, r, s, N), p)]++;
        }
        cout << "p=" << p << " split=" << r << "+" << s;
        for (auto [rank, count] : distribution) cout << " " << rank << ":" << count;
        cout << "\n";
    }
}

void sample17() {
    const int p = 17, N = 13, r = 8, s = 9;
    mt19937_64 rng(123);
    uniform_int_distribution<int> draw(0, p - 1);
    vector<int> lambda(N + 1);
    map<int, long long> distribution;
    for (int trial = 0; trial < 2000000; ++trial) {
        for (int k = 1; k <= N; ++k) lambda[k] = draw(rng);
        if (!lambda[N]) lambda[N] = 1;
        distribution[mod_rank(hankel(lambda, r, s, N), p)]++;
    }
    cout << "p=17 random conductor13";
    for (auto [rank, count] : distribution) cout << " " << rank << ":" << count;
    cout << "\n";
    for (int m = 1; m <= N; ++m) {
        fill(lambda.begin(), lambda.end(), 0);
        lambda[m] = 1;
        cout << "spike m=" << m << " rank="
             << mod_rank(hankel(lambda, r, s, N), p) << "\n";
    }
}

int main() {
    exhaustive(7);
    exhaustive(11);
    sample17();
}
