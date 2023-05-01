import os

for i in os.listdir(os.getcwd()):
    if os.path.isdir(i):
        os.system(f'scp input.py CONTCAR run_vasp.sh {i}')