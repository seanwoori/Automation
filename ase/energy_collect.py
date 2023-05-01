import os
import sys
import numpy as np


def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

tl = [x for x in sys.argv if isNumber(x)]
if tl == []:
    depth = -1
else:
    depth = int(tl[0])

enpath = []
energy = []
encon = []

def walklevel(some_dir, level=depth):
    if depth == -1:
        for root, dirs, files in os.walk(some_dir):
            yield root, dirs, files
    else:
        some_dir = some_dir.rstrip(os.path.sep)
        assert os.path.isdir(some_dir)
        num_sep = some_dir.count(os.path.sep)
        for root, dirs, files in os.walk(some_dir):
            yield root, dirs, files
            num_sep_this = root.count(os.path.sep)
            if num_sep + level <= num_sep_this:
                del dirs[:]
            
en_key = 'E0='
en_num = '5'
ec_key = '"reached required accuracy"'
unit = 'eV'
f_type = 1

if 'vasp' in sys.argv or 'v' in sys.argv:
    en_key = 'E0='
    en_num = '5'
    ec_key = '"reached required accuracy"'
    unit = 'eV'
    f_type = 1
if 'vasp_thermal_correction' in sys.argv or 'vt' in sys.argv:
    en_key = 'E0='
    en_num = '5'
    ec_key = '"Finite differences POTIM=  "'
    unit = 'eV'
    f_type = 0
if 'orca' in sys.argv or 'o' in sys.argv:
    en_key = 'FINAL'
    en_num = '5'
    ec_key = '"ORCA TERMINATED NORMALLY"'
    unit = 'Eh'
    f_type = 1
if 'orca_thermal_correction' in sys.argv or 'ot' in sys.argv:
    en_key = 'G-E'
    en_num = '3'
    ec_key = '"ORCA TERMINATED NORMALLY"'
    unit = 'Eh'
    f_type = 1
if 'orca_ts' in sys.argv or 'ots' in sys.argv:
    en_key = 'imaginary'
    en_num = '2'
    ec_key = '"ORCA TERMINATED NORMALLY"'
    unit = 'cm^-1'
    f_type = 3

if f_type == 1:
    for path, direct, files in walklevel(os.getcwd(), level=depth):
        if 'stdout.log' in files:
            en = os.popen(f"cd {path} && grep {en_key} stdout.log | tail -1 | awk '{{print ${en_num}}}'").read()
            ec = os.popen(f'cd {path} && grep {ec_key} stdout.log').read()
            if en == '':
                pass
            else:
                en = float(en)
                enpath.append(path)
                energy.append(en)
                encon.append(ec)

elif f_type == 0:
    for path, direct, files in walklevel(os.getcwd(), level=depth):
        if 'stdout.log' in files:
            ec = os.popen(f'cd {path} && grep {ec_key} stdout.log').read()
            if ec != '':
                en = os.popen(f"cd {path} && python3 /home/cjw/jinucode/frequency_energy.py | tail -1 | awk '{{print ${en_num}}}'").read()
                en = float(en)
                enpath.append(path)
                energy.append(en)
                encon.append(ec)
            else:
                en = 0

elif f_type == 3:
    for path, direct, files in walklevel(os.getcwd(), level=depth):
        if 'stdout.log' in files:
            en = os.popen(f"cd {path} && grep {en_key} stdout.log | tail -1 | awk '{{print ${en_num}}}'").read()
            ec = os.popen(f'cd {path} && grep {ec_key} stdout.log').read()
            if en == '':
                pass
            else:
                en = float(en)
                enpath.append(path)
                energy.append(en)
                encon.append(ec)

if 'ranking' in sys.argv or 'r' in sys.argv:
    r = np.array(energy).argsort()
else:
    r = range(len(enpath))

if 'converge' in sys.argv or 'c' in sys.argv:
    c = 1
else:
    c = 0

if 'not_converge' in sys.argv or 'nc' in sys.argv:
    nc = 1
else:
    nc = 0


if c == 1:
    for i in r:
        if encon[i] != '':
            print(f'path: {enpath[i]}')
            print(f'energy: {energy[i]} {unit}\n')
elif nc == 1:
    for i in r:
        if encon[i] == '':
            print(f'path: {enpath[i]}')
            print(f'energy: {energy[i]} {unit}\n')
else:
    for i in r:
        if encon[i] != '':
            print(f'path: {enpath[i]}')
            print(f'energy: {energy[i]} {unit}')
            print(f'converge: {True}\n')
        else:
            print(f'path: {enpath[i]}')
            print(f'energy: {energy[i]} {unit}')
            print(f'converge: {False}\n')