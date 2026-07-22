#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

/*
Exact cubic-pair and mixed-factor ledger for

    F_(c,d)(X)=X^p+aX^3+cX+d.

Usage:
    g++ -O3 -march=native cubic_mixed_mass_audit.cpp -o cubic_mixed
    ./cubic_mixed <prime p>

For each square class of a, the program computes:

  sum Q_3,
  sum binom(Q_3,2),
  sum binom(Q_3,3),
  sum L Q_3,
  sum Q_2 Q_3,

where L,Q_2,Q_3 count irreducible factors of degrees 1,2,3.

Cubic factors are enumerated efficiently through the unique trace-zero member
of each additive translation orbit.  Thus only p^2 trace-zero cubics are
examined, rather than all p^3 monic cubics.  All arithmetic is exact.
*/

struct Poly3 {
    int c0, c1, c2;
};

static int modp(long long x, int p) {
    x %= p;
    if (x < 0) x += p;
    return (int)x;
}

static int modpow(int a, long long e, int p) {
    long long out = 1;
    long long b = modp(a, p);
    while (e) {
        if (e & 1) out = out * b % p;
        b = b * b % p;
        e >>= 1;
    }
    return (int)out;
}

static int invmod(int a, int p) {
    return modpow(a, p - 2, p);
}

static int chi(int a, int p) {
    a = modp(a, p);
    if (a == 0) return 0;
    return modpow(a, (p - 1) / 2, p) == 1 ? 1 : -1;
}

// Quotient by X^3 + S X - N, i.e. X^3 = -S X + N.
static Poly3 mul_trace_zero(Poly3 x, Poly3 y, int S, int N, int p) {
    long long raw[5] = {0, 0, 0, 0, 0};
    int xv[3] = {x.c0, x.c1, x.c2};
    int yv[3] = {y.c0, y.c1, y.c2};
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
            raw[i + j] += (long long)xv[i] * yv[j];

    for (int degree = 4; degree >= 3; --degree) {
        int coefficient = modp(raw[degree], p);
        raw[degree] = 0;
        int shift = degree - 3;
        raw[shift] += (long long)coefficient * N;
        raw[shift + 1] -= (long long)coefficient * S;
    }

    return Poly3{
        modp(raw[0], p), modp(raw[1], p), modp(raw[2], p)
    };
}

static Poly3 x_to_p_trace_zero(int S, int N, int p) {
    Poly3 out{1, 0, 0};
    Poly3 base{0, 1, 0};
    int exponent = p;
    while (exponent) {
        if (exponent & 1)
            out = mul_trace_zero(out, base, S, N, p);
        base = mul_trace_zero(base, base, S, N, p);
        exponent >>= 1;
    }
    return out;
}

static bool irreducible_trace_zero_cubic(int S, int N, int p) {
    for (int x = 0; x < p; ++x) {
        long long value = (long long)x * x % p * x + (long long)S * x - N;
        if (modp(value, p) == 0) return false;
    }
    return true;
}

struct Row {
    int p;
    int a;
    int square_class;
    long long cubic_incidence;
    long long cubic_second;
    long long cubic_third;
    long long linear_cubic;
    long long quadratic_cubic;
    long long centered_linear_cubic;
    long long cubic_support_members;
    int max_q3;
    string q3_distribution;
};

static Row audit_class(int p, int a) {
    const int size = p * p;
    vector<int> q2(size, 0), q3(size, 0), linear(size, 0);

    // Exact quadratic-factor parametrisation.
    for (int t = 0; t < p; ++t) {
        for (int n = 0; n < p; ++n) {
            int discriminant = modp((long long)t * t - 4LL * n, p);
            if (chi(discriminant, p) != -1) continue;
            int c = modp(1LL - (long long)a * (modp((long long)t * t - n, p)), p);
            int d = modp((long long)t * (modp((long long)a * n - 1, p)), p);
            ++q2[c * p + d];
        }
    }

    // Complete rational-root count.
    for (int c = 0; c < p; ++c) {
        for (int d = 0; d < p; ++d) {
            int count = 0;
            for (int x = 0; x < p; ++x) {
                int value = modp(
                    (long long)a * x % p * x % p * x
                    + (long long)(c + 1) * x + d,
                    p
                );
                if (value == 0) ++count;
            }
            linear[c * p + d] = count;
        }
    }

    // Every additive translation orbit of irreducible cubics has a unique
    // trace-zero representative X^3+S X-N.  If
    // X^p=A+B X+C X^2 in that quotient, translation by
    // u=-C/(3a) gives t=3u and hence C+a t=0, the exact slice condition.
    int inv_3a = invmod(modp(3LL * a, p), p);
    long long trace_zero_irreducibles = 0;
    for (int S = 0; S < p; ++S) {
        for (int N = 0; N < p; ++N) {
            if (!irreducible_trace_zero_cubic(S, N, p)) continue;
            ++trace_zero_irreducibles;

            Poly3 frob = x_to_p_trace_zero(S, N, p);
            int u = modp(-(long long)frob.c2 * inv_3a, p);

            int t = modp(3LL * u, p);
            int s = modp((long long)S + 3LL * u * u, p);
            int n = modp((long long)N + (long long)S * u
                         + (long long)u * u % p * u, p);

            int A = modp((long long)frob.c0 - (long long)frob.c1 * u
                         + (long long)frob.c2 * u % p * u + u, p);
            int B = modp((long long)frob.c1 - 2LL * frob.c2 * u, p);
            int C = frob.c2;
            if (modp((long long)C + (long long)a * t, p) != 0) {
                cerr << "translation condition failed\n";
                exit(3);
            }

            int c = modp((long long)a * s - B, p);
            int d = modp(-(long long)A - (long long)a * n, p);
            ++q3[c * p + d];
        }
    }

    long long expected_cubic_mass = ((long long)p * p - 1) / 3;
    if (trace_zero_irreducibles != expected_cubic_mass) {
        cerr << "trace-zero cubic mass mismatch at p=" << p << "\n";
        exit(4);
    }

    long long incidence = 0;
    long long second = 0;
    long long third = 0;
    long long linear_cubic = 0;
    long long quadratic_cubic = 0;
    long long support = 0;
    int maximum = 0;
    map<int, long long> distribution;

    for (int index = 0; index < size; ++index) {
        int q = q3[index];
        incidence += q;
        second += (long long)q * (q - 1) / 2;
        third += (long long)q * (q - 1) * (q - 2) / 6;
        linear_cubic += (long long)linear[index] * q;
        quadratic_cubic += (long long)q2[index] * q;
        if (q) ++support;
        maximum = max(maximum, q);
        ++distribution[q];
    }

    if (incidence != expected_cubic_mass) {
        cerr << "cubic incidence mismatch at p=" << p << "\n";
        exit(5);
    }

    string distribution_text;
    for (auto [multiplicity, count] : distribution) {
        if (!distribution_text.empty()) distribution_text += ";";
        distribution_text += to_string(multiplicity) + ":" + to_string(count);
    }

    return Row{
        p,
        a,
        chi(a, p),
        incidence,
        second,
        third,
        linear_cubic,
        quadratic_cubic,
        linear_cubic - incidence,
        support,
        maximum,
        distribution_text,
    };
}

static void print_row(const Row& row) {
    cout << row.p << ','
         << row.a << ','
         << row.square_class << ','
         << row.cubic_incidence << ','
         << row.cubic_second << ','
         << row.cubic_third << ','
         << row.linear_cubic << ','
         << row.quadratic_cubic << ','
         << row.centered_linear_cubic << ','
         << row.cubic_support_members << ','
         << row.max_q3 << ','
         << '"' << row.q3_distribution << '"' << '\n';
}

int main(int argc, char** argv) {
    if (argc != 2) {
        cerr << "usage: " << argv[0] << " <prime p>\n";
        return 2;
    }
    int p = stoi(argv[1]);
    if (p < 5) {
        cerr << "p must be an odd prime >=5\n";
        return 2;
    }

    int nonsquare = 2;
    while (nonsquare < p && chi(nonsquare, p) != -1) ++nonsquare;
    if (nonsquare == p) {
        cerr << "failed to find a nonsquare\n";
        return 2;
    }

    cout << "prime,a,square_class,cubic_incidence,cubic_second,cubic_third,"
            "linear_cubic,quadratic_cubic,centered_linear_cubic,"
            "cubic_support_members,max_Q3,multiplicity_distribution\n";
    print_row(audit_class(p, 1));
    print_row(audit_class(p, nonsquare));
    return 0;
}
