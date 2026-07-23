#!/bin/sh
set -eu

# Independent summation-mode check for p223_full_cartier_weight_fourier.cpp.
# It removes Frobenius-orbit pairing and evaluates every one of the 49,728
# nonzero elements of F_(223^2) directly.  The determinant construction and
# exact degree bound remain unchanged.

src=${1:-frontier/d1_push/p223_full_cartier_weight_fourier.cpp}
out=${2:-/tmp/p223_full_cartier_weight_unpaired.cpp}
bin=${3:-/tmp/p223_full_cartier_weight_unpaired}

sed \
  -e 's/if (code > ccode) continue;/\/\/ unpaired verifier: retain every nonzero field element;/' \
  -e 's/b == 0});/true});/' \
  "$src" > "$out"

g++ -O3 -march=native -fopenmp "$out" -o "$bin"
export OMP_NUM_THREADS=${OMP_NUM_THREADS:-$(nproc)}
exec "$bin" 3 4 1
