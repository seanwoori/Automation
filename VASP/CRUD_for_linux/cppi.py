import os
import sys

for i in sys.argv[1:]:
    os.system(f'scp input.py POSCAR run_vasp.sh {i}')