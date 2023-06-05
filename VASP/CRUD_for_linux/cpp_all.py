import os


for i in os.listdir(os.getcwd()):
    if os.path.isdir(i):
        os.system(f'scp KPOINTS INCAR POSCAR POTCAR run_slurm.sh {i}')