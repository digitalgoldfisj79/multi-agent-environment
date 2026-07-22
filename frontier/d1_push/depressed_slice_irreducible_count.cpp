#include <algorithm>
#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;

/*
Exact irreducible counts for the two depressed cubic square classes:

  F_(a,c,d)(X)=X^p+aX^3+cX+d.

For prime degree p, Rabin's criterion reduces to

  gcd(F, X^p-X)=1,
  X^(p^p)=X mod F.

The code builds the Frobenius matrix from the sparse relation

  X^p=-(aX^3+cX+d)

and iterates it exactly p times. It uses no floating-point arithmetic and no
external algebra library.

Build and run:
  g++ -O3 -march=native -fopenmp depressed_slice_irreducible_count.cpp -o count
  OMP_NUM_THREADS=$(nproc) ./count <prime p>
*/

int modpow(int a, int e, int p) {
    long long out = 1;
    long long b = (a % p + p) % p;
    while (e) {
        if (e & 1) out = out * b % p;
        b = b * b % p;
        e >>= 1;
    }
    return (int)out;
}

int legendre(int a, int p) {
    if (a % p == 0) return 0;
    return modpow(a, (p - 1) / 2, p) == 1 ? 1 : -1;
}

void trim(vector<int>& f) {
    while (!f.empty() && f.back() == 0) f.pop_back();
}

vector<int> polynomial_remainder(vector<int> a, const vector<int>& b, int p) {
    vector<int> divisor = b;
    trim(a);
    trim(divisor);
    if (divisor.empty()) abort();

    int divisor_degree = (int)divisor.size() - 1;
    int inverse_lead = modpow(divisor.back(), p - 2, p);

    while (!a.empty() && (int)a.size() - 1 >= divisor_degree) {
        int degree = (int)a.size() - 1;
        int quotient = (long long)a.back() * inverse_lead % p;
        int shift = degree - divisor_degree;
        for (int j = 0; j <= divisor_degree; ++j) {
            a[shift + j] =
                (a[shift + j] - (long long)quotient * divisor[j]) % p;
            if (a[shift + j] < 0) a[shift + j] += p;
        }
        trim(a);
    }
    return a;
}

int gcd_degree(vector<int> a, vector<int> b, int p) {
    trim(a);
    trim(b);
    while (!b.empty()) {
        vector<int> remainder = polynomial_remainder(a, b, p);
        a = move(b);
        b = move(remainder);
    }
    return a.empty() ? -1 : (int)a.size() - 1;
}

vector<int> multiply_mod_f(
    const vector<int>& x,
    const vector<int>& y,
    int p,
    int a,
    int c,
    int d
) {
    int n = p;
    vector<int> product(2 * n - 1);

    for (int i = 0; i < n; ++i) if (x[i]) {
        for (int j = 0; j < n; ++j) if (y[j]) {
            product[i + j] =
                (product[i + j] + (long long)x[i] * y[j]) % p;
        }
    }

    // Descending reduction using X^p=-(aX^3+cX+d).
    for (int k = 2 * n - 2; k >= n; --k) {
        int coefficient = product[k] % p;
        if (!coefficient) continue;
        product[k] = 0;
        int shift = k - n;
        product[shift] =
            (product[shift] - (long long)coefficient * d) % p;
        product[shift + 1] =
            (product[shift + 1] - (long long)coefficient * c) % p;
        product[shift + 3] =
            (product[shift + 3] - (long long)coefficient * a) % p;
        for (int index : {shift, shift + 1, shift + 3}) {
            if (product[index] < 0) product[index] += p;
        }
    }

    product.resize(n);
    return product;
}

bool is_irreducible(int p, int a, int c, int d) {
    vector<int> polynomial(p + 1);
    polynomial[p] = 1;
    polynomial[3] = a;
    polynomial[1] = c;
    polynomial[0] = d;

    // Modulo F, X^p-X=-(aX^3+(c+1)X+d). The sign is irrelevant to gcd.
    vector<int> linear_factor_test(4);
    linear_factor_test[3] = a;
    linear_factor_test[1] = (c + 1) % p;
    linear_factor_test[0] = d;
    if (gcd_degree(polynomial, linear_factor_test, p) > 0) return false;

    // R_j=(X^p)^j mod F are the columns of the Frobenius map.
    vector<vector<int>> frobenius_columns(p, vector<int>(p));
    frobenius_columns[0][0] = 1;

    vector<int> x_to_p(p);
    x_to_p[0] = (p - d) % p;
    x_to_p[1] = (p - c) % p;
    x_to_p[3] = (p - a) % p;

    for (int j = 1; j < p; ++j) {
        frobenius_columns[j] = multiply_mod_f(
            frobenius_columns[j - 1], x_to_p, p, a, c, d
        );
    }

    vector<int> value(p);
    value[1] = 1;
    for (int step = 0; step < p; ++step) {
        vector<int> next(p);
        for (int j = 0; j < p; ++j) if (value[j]) {
            for (int k = 0; k < p; ++k) {
                next[k] = (
                    next[k] +
                    (long long)value[j] * frobenius_columns[j][k]
                ) % p;
            }
        }
        value.swap(next);
    }

    for (int k = 0; k < p; ++k) {
        if (value[k] != (k == 1)) return false;
    }
    return true;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        cerr << "usage: " << argv[0] << " <prime p>\n";
        return 2;
    }

    int p = stoi(argv[1]);
    int nonsquare = 2;
    while (legendre(nonsquare, p) != -1) ++nonsquare;

    for (int a : {1, nonsquare}) {
        long long count = 0;

        #pragma omp parallel for reduction(+:count) schedule(dynamic)
        for (int c = 0; c < p; ++c) {
            for (int d = 0; d < p; ++d) {
                if (is_irreducible(p, a, c, d)) ++count;
            }
        }

        cout << "prime=" << p
             << " a=" << a
             << " square_class=" << (a == 1 ? "square" : "nonsquare")
             << " N=" << count
             << " residue_mod_p=" << count % p
             << " below_2p=" << (count < 2LL * p ? "true" : "false")
             << "\n";
    }

    return 0;
}
