import os
import sys

file = sys.argv[1]

for path, direct, files in os.walk(os.getcwd()):
    os.system(f'scp {file} {path}')
