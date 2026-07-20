#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
HERE=Path(__file__).resolve().parent
scripts=[
 'validate_pair_sum_fourth_moment.py',
 'validate_one_sided_identity.py',
 'validate_mobius_degree_identity.py',
 'validate_fourier_scale_conservation.py',
 'validate_critical_scale_coherence.py',
]
for script in scripts:
    print(f"\n=== {script} ===", flush=True)
    subprocess.run([sys.executable,str(HERE/script)],check=True)
print("\nALL_CHECKS_PASS")
