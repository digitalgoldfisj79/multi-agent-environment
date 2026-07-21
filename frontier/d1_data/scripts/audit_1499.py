from flint import nmod_poly
import numpy as np, time
from audit_zero_verify import verify_zero
# reuse staged machinery but collect irreducibles for p=1499
p = 1499
t = time.time()
stats, irr = verify_zero(p)
print(f'p=1499: irreducible d list = {irr}; stats={stats} [{time.time()-t:.0f}s]')
