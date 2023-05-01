import os


for path, direct, files in os.walk(os.getcwd()):
    if 'run_slurm.sh' in files:
        os.system(f'cd {path} && sbatch run_slurm.sh')
