#!/usr/bin/env python3
"""Exact arithmetic checks for the odd-extension Airy/primitive bridge."""

FIRST = {
    11: {
        "T": 322102,
        "up": 1771561,
        "low": -161051,
    },
    17: {
        "T": 11899821517,
        "up": 202296965789,
        "low": 0,
    },
    23: {
        "T": -1010446643080743,
        "up": -9735230135207515,
        "low": 587175767636938,
    },
    29: {
        "T": -798145148362709627351,
        "up": -17221580757743000101634,
        "low": 204297536026744106605,
    },
}

THIRD = {
    11: (
        5559917313492231481,
        -4177248169415651,
    ),
    17: (
        -255944298171217376101202104309234,
        0,
    ),
    23: (
        24420035557874291486685783320490312291163556150933,
        1811942529812491726048499913466581810789054457,
    ),
    29: (
        -624252554084396763440186646610590357883743693997978553242566200210,
        52044691388847887475857027569042615828726415261418059755550020,
    ),
}


def verify_first():
    for p, data in FIRST.items():
        airy = data["up"] - p * data["low"]
        assert airy == p * data["T"], (p, airy, p * data["T"])
        assert data["T"] % (p * p) == 0
        primitive = data["T"] // (p * p)
        assert airy == p**3 * primitive
    print("PASS: r=1 Airy/primitive bridge at p=11,17,23,29.")


def verify_third():
    quotients = {}
    for p, (up, low) in THIRD.items():
        airy = up - p**3 * low
        assert airy % p**9 == 0, (p, airy % p**9)
        quotients[p] = airy // p**9
    print("PASS: p^9 divisibility of all certified r=3 bridge traces.")
    for p in sorted(quotients):
        print(f"p={p}: Tr(F^3 | D_p) = {quotients[p]}")


def main():
    verify_first()
    verify_third()


if __name__ == "__main__":
    main()
