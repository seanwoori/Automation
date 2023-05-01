import sys

file = sys.argv[1]

with open(file, 'r') as readfile:
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

userarr = input('Enter the desired atomic arrangement: ').split()
if set(atomarr) == set(userarr):
    atomarr = userarr
elif userarr == []:
    pass
else:
    print('Wrong atomic arrangement\nRun the default')

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

writeatomarr = atomarr[0]
for i in range(len(atomarr)-1):
    writeatomarr += '  ' + atomarr[i+1]
print('Atomic arrangement:', writeatomarr)
writeatomarr += '\n'

with open(file, 'w') as writefile:
    for linenumber, data in enumerate(writeinfo):
        if linenumber == atomline:
            writefile.write(writeatomarr)
            
        elif linenumber == atomnumberline:
            writefile.write(atomcount)
            
        elif unitline <= linenumber <= unitline+4:
            writefile.write(unitinfo[linenumber-unitline])
            
        elif coordline <= linenumber <= coordline+atoms-1:
            writefile.write(writecoord[linenumber-coordline])
            
        else:
            writefile.write(data)

