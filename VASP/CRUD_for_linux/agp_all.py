import os

a = ''
for i in os.listdir(os.getcwd()):
    if os.path.isdir(i) and os.path.isfile(os.getcwd()+'/'+i+'/POSCAR'):
        a += i+'/POSCAR '
os.system(f'ase gui {a}')