#!/usr/bin/env python3
"""Independent finite-data verifier for the Airy Gaussian audit.

This script deliberately certifies only finite computational statements:

* calibration of the FFT formula against the nine committed exact T_p values;
* the complete p < 100000 scan by default;
* falsification of the proposed constant C=4;
* scalar covariance diagnostics for the two Adams symmetric-power sums.

It does NOT assert that sup_p |rho_p| is infinite or prove a Gaussian limit law.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np


EXACT_T = {
    5: 0,
    11: 322102,
    17: 11899821517,
    23: -1010446643080743,
    29: -798145148362709627351,
    41: 285608599198466451834837856911313,
    47: -36201375290118292903477796139763762494,
    53: 625211553014678241605175931243651758726469297,
    71: 36727396978062655326395765238086038211050946366161670340353263984,
}


@dataclass(frozen=True)
class ScanResult:
    count: int
    mean: float
    variance: float
    skewness: float
    kurtosis: float
    ks_statistic: float
    ks_critical_5pct: float
    maximum_absolute_rho: float
    maximum_prime: int


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return np.nonzero(sieve)[0].tolist()


def airy_angles(p: int) -> np.ndarray:
    """Return theta_t using the additive-character convention of this script."""
    x = np.arange(p, dtype=np.int64)
    cubes = (x * x % p) * x % p
    trace_values = (
        p * np.fft.ifft(np.exp(2j * np.pi * cubes / p))
    ).real
    return np.arccos(
        np.clip(trace_values / (2.0 * math.sqrt(p)), -1.0, 1.0)
    )


def rho(p: int) -> float:
    """Convention calibrated to the committed exact T_p integers."""
    return (2.0 / math.sqrt(p)) * float(np.cos(p * airy_angles(p)).sum())


def check_calibration() -> None:
    print("[1] exact-value calibration and sign audit")
    worst_plus = 0.0
    worst_minus = 0.0
    for p, exact_t in sorted(EXACT_T.items()):
        exact_rho = exact_t / p ** ((p - 1) // 2)
        computed = rho(p)
        plus_error = abs(computed - exact_rho) / max(abs(exact_rho), 1.0)
        minus_error = abs(-computed - exact_rho) / max(abs(exact_rho), 1.0)
        worst_plus = max(worst_plus, plus_error)
        worst_minus = max(worst_minus, minus_error)
        print(
            f"    p={p:>3} exact={exact_rho:+.12f} "
            f"computed={computed:+.12f} rel={plus_error:.3e}"
        )
    assert worst_plus < 1e-9
    assert worst_minus > 1e-3, "global sign is unexpectedly ambiguous"
    print(f"    PASS: calibrated sign is PLUS; worst relative error={worst_plus:.3e}")
    print("    NOTE: any write-up displaying the opposite sign uses a different convention\n")


def normal_cdf(x: np.ndarray) -> np.ndarray:
    return 0.5 * (1.0 + np.vectorize(math.erf)(x / math.sqrt(2.0)))


def scan(limit: int) -> tuple[list[int], np.ndarray, ScanResult]:
    ps = [p for p in primes_upto(limit - 1) if p % 6 == 5]
    values = np.array([rho(p) for p in ps], dtype=float)
    mean = float(values.mean())
    std_population = float(values.std(ddof=0))
    variance = float(values.var(ddof=1))
    centred = values - mean
    skewness = float((centred**3).mean() / std_population**3)
    kurtosis = float((centred**4).mean() / std_population**4)

    standardized = np.sort(values / math.sqrt(2.0))
    n = len(standardized)
    cdf = normal_cdf(standardized)
    ks = float(
        max(
            np.abs(cdf - np.arange(n) / n).max(),
            np.abs(cdf - np.arange(1, n + 1) / n).max(),
        )
    )
    critical = 1.358 / math.sqrt(n)
    index = int(np.argmax(np.abs(values)))
    result = ScanResult(
        count=n,
        mean=mean,
        variance=variance,
        skewness=skewness,
        kurtosis=kurtosis,
        ks_statistic=ks,
        ks_critical_5pct=critical,
        maximum_absolute_rho=float(abs(values[index])),
        maximum_prime=ps[index],
    )
    return ps, values, result


def report_scan(limit: int) -> None:
    print(f"[2] complete finite scan for p < {limit}, p congruent 5 mod 6")
    ps, values, result = scan(limit)
    print(f"    n={result.count}")
    print(f"    mean={result.mean:+.10f}")
    print(f"    sample variance={result.variance:.10f}")
    print(f"    skewness={result.skewness:+.10f}")
    print(f"    kurtosis={result.kurtosis:.10f}")
    print(
        f"    KS={result.ks_statistic:.10f}; "
        f"nominal 5% critical={result.ks_critical_5pct:.10f}"
    )
    print(
        f"    max |rho|={result.maximum_absolute_rho:.10f} "
        f"at p={result.maximum_prime}"
    )

    sd = math.sqrt(2.0)
    for level in (1.0, 1.5, 2.0, 2.5, 3.0):
        frequency = float((np.abs(values) > level * sd).mean())
        print(f"    P(|rho|>{level:.1f} sqrt(2))={frequency:.10f}")

    assert result.maximum_absolute_rho > 4.0
    print("    PASS: the proposed universal constant C=4 is rigorously falsified")
    print("    NO CLAIM: this finite scan does not disprove every absolute constant\n")

    for bound in (1000, 3000, 10000, 30000, 60000, limit - 1):
        selected = np.array([v for p, v in zip(ps, values) if p <= bound])
        if selected.size:
            print(f"    max |rho| for p<={bound:>6}: {np.abs(selected).max():.10f}")
    print()


def symmetric_power_sums(p: int) -> tuple[float, float]:
    theta = airy_angles(p)
    sine = np.sin(theta)
    safe = np.abs(sine) > 1e-12
    plus = np.zeros(p)
    minus = np.zeros(p)
    plus[safe] = np.sin((p + 1) * theta[safe]) / sine[safe]
    minus[safe] = np.sin((p - 1) * theta[safe]) / sine[safe]
    return float(plus.sum()), float(minus.sum())


def check_adams(limit: int) -> None:
    print(f"[3] scalar Adams covariance diagnostic for p < {limit}")
    ps = [p for p in primes_upto(limit - 1) if p % 6 == 5]
    rows = [symmetric_power_sums(p) for p in ps]
    roots = np.sqrt(np.array(ps, dtype=float))
    plus = np.array([row[0] for row in rows]) / roots
    minus = np.array([row[1] for row in rows]) / roots
    difference = plus - minus
    correlation = float(np.corrcoef(plus, minus)[0, 1])
    rms_plus = float(np.sqrt(np.mean(plus**2)))
    rms_minus = float(np.sqrt(np.mean(minus**2)))
    rms_difference = float(np.sqrt(np.mean(difference**2)))
    print(f"    rms(M_plus/sqrt(p))={rms_plus:.10f}")
    print(f"    rms(M_minus/sqrt(p))={rms_minus:.10f}")
    print(f"    rms(difference/sqrt(p))={rms_difference:.10f}")
    print(f"    sample correlation={correlation:+.10f}")
    assert abs(correlation) < 0.15
    assert rms_difference > 1.2 * max(rms_plus, rms_minus)
    print("    PASS: no gain is visible in the sampled total-trace covariance")
    print("    NO CLAIM: scalar covariance does not prove constituent-level impossibility\n")


def report_characteristic_three_exception() -> None:
    print("[4] singular-locus statement at p=3")
    print("    Tr(x^3)=Tr(x)^3 in characteristic 3")
    print("    hence the restricted cubic is identically zero on ker Tr")
    print("    RESULT: the '[1] for every odd prime' statement is false at p=3")
    print("    CORRECT DOMAIN: p>3\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100000)
    parser.add_argument("--adams-limit", type=int, default=20000)
    args = parser.parse_args()
    if args.limit <= 57653:
        raise SystemExit("--limit must exceed 57653 to certify the C=4 counterexample")

    check_calibration()
    report_scan(args.limit)
    check_adams(args.adams_limit)
    report_characteristic_three_exception()
    print("AIRY_GAUSSIAN_INDEPENDENT_VERIFY: PASS")


if __name__ == "__main__":
    main()
