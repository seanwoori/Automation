import os
import sys

for i in sys.argv[1:]:
    os.system(f'scp KPOINTS INCAR POSCAR POTCAR run_slurm.sh {i}')