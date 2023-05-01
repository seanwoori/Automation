import os
import sys

file = sys.argv[1]
pwd = os.getcwd()
a = ''
for i in os.listdir(pwd):
    if os.path.isdir(i) and os.path.isfile(pwd+'/'+i+'/'+file):
        a += i+'/'+file+' '

os.system(f'ase gui {a}')