def grep(lines, searchtext):
    for line in lines:
        if searchtext in line:
            yield line



with open('INCAR') as f:
    lines = f.readlines()
    ISPIN, LDAUL, LDAUU, LDAUJ = 1, 0, 0, 0
    for i in grep(lines, 'ENCUT'):
        i = i.split()[2]
        ENCUT = i
    for i in grep(lines, 'ISPIN'):
        i = i.split()[2]
        ISPIN = i
    for i in grep(lines, 'MAGMOM'):
        i = i.split()[2:]
        MAGMOM = i
    if ISPIN == '2':
        mag = 0
        for i in MAGMOM:
            mag += int(i.split('*')[0])
    for i in grep(lines, 'LDAUL'):
        LDAUL = i.split()[2:]
    for i in grep(lines, 'LDAUU'):
        LDAUU = i.split()[2:]
    for i in grep(lines, 'LDAUJ'):
        LDAUJ = i.split()[2:]


with open('POTCAR') as f:
    lines = f.readlines()
    TITEL = []
    ENMAX = []
    for i in grep(lines, 'TITEL'):
        i = i.split()[3].split('_')[0]
        TITEL.append(i)
    for i in grep(lines, 'ENMAX'):
        i = i.split(';')[0].split()[2]
        ENMAX.append(i)



with open('POSCAR', 'r') as readfile:
    info = []
    writeinfo = []
    while True:
        line = readfile.readline()
        writeinfo.append(line)
        linesplit = line.split()
        info.append(linesplit)
        if not line: break


def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


atom = """
H He 
Li Be B C N O F Ne 
Na Mg Al Si P S Cl Ar 
K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr 
Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe 
Cs Ba 
La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb 
Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn 
Fr Ra 
Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No 
Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
"""

atom = atom.split()
atom = set(atom)
atomline = 0
for n, i in enumerate(info):
    disc = set(i)
    if disc == disc.intersection(atom) and disc != set():
        atomline = n

atomarr = list(dict.fromkeys(info[atomline]))

unitline = 0
for n, i in enumerate(info):
    if i != [] and isNumber(i[0]):
        test = [len(j) for j in info[n:n+4]]
        if test == [1, 3, 3, 3]:
            unitline = n
            break
unitinfo = writeinfo[unitline:unitline+4]

atomnumberline = 0
coordline = 0
if unitline > atomline:
    atomnumberline = unitline + 4
    for n, i in enumerate(info[atomnumberline+1:]):
        if i == []:
            pass
        elif isNumber(i[0]) and 3 <= len(i):
            coordline = atomnumberline + 1 + n
            break
else:
    atomnumberline = atomline + 1
    for n, i in enumerate(info[atomnumberline+1:]):
        if i == []:
            pass
        elif isNumber(i[0]) and 3 <= len(i):
            coordline = atomnumberline + 1 + n
            break

atoms = 0
for i in info[atomnumberline]:
    atoms += int(i)
writecoordinfo = writeinfo[coordline:coordline+atoms]

tempnumber = 0
coordinfo = []
writecoord = []
for i in info[atomnumberline]:
    coordinfo.append(writecoordinfo[tempnumber:tempnumber+int(i)])
    tempnumber += int(i)
atomcount = ''

for i in atomarr:
    m = 0
    for n, j in enumerate(info[atomline]):
        if i == j:
            writecoord += coordinfo[n]
            m += int(info[atomnumberline][n])
    atomcount += '  '+str(m)
atomcount += '\n'



if TITEL == info[atomline]:
    pass
else:
    raise Exception('The atomic information of POTCAR and POSCAR is different.')
    
if float(ENCUT) >= float(max(ENMAX)):
    pass
else:
    raise Exception('ENCUT is smaller than ENMAX.')

if ISPIN == '2':
    if mag == atoms:
        pass
    else:
        raise Exception('The magnetic moment information of INCAR and POSCAR is different.')

if LDAUL == 0 and LDAUU == 0 and  LDAUJ == 0:
    pass
else:
    if len(info[atomline]) == len(TITEL) == len(LDAUL) == len(LDAUU) == len(LDAUJ):
        pass
    else:
        raise Exception('The DFT+U information of INCAR is wrong.')

