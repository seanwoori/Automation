import sys
from ase.thermochemistry import HarmonicThermo

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line:
            yield line



with open('OUTCAR') as f:
    lines = f.readlines()
    c = grep(lines, 'THz')
    thz = []
    for i in c:
        thz.append(i.split())

vib_energies = []
for i in thz:
    if 'f' in i:
        v = float(i[-2])/1000
        vib_energies.append(v)

kB = 8.617333262145e-5   # eV/K
T = 298.15

Tl = [x for x in sys.argv if isNumber(x)]
if Tl == []:
    print(f'\nRun the default\nTemperature: {T}K\n')
else:
    T = float(Tl[0])
    print(f'\nTemperature: {T}K\n')
    

h = HarmonicThermo(vib_energies = vib_energies, potentialenergy = 0)

S = h.get_entropy(temperature=T, verbose=0)
ZPE = h.get_ZPE_correction()

print(f'ZPE = {ZPE} eV\nS   = {S} eV/K\nZPE - T*S = {ZPE - T*S} eV')


