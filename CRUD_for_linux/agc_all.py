import os

a = ''
for i in os.listdir(os.getcwd()):
    if os.path.isdir(i) and os.path.isfile(os.getcwd()+'/'+i+'/CONTCAR'):
        a += i+'/CONTCAR '
os.system(f'ase gui {a}')