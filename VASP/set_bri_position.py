import sys

bpinfo = sys.argv[1:]

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

atomarr = info[atomline]

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

# userarr = input('Enter the desired atomic arrangement: ').split()
# if set(atomarr) == set(userarr):
#     atomarr = userarr
# elif userarr == []:
#     pass
# else:
#     print('Wrong atomic arrangement\nRun the default')

atoms = 0
for i in info[atomnumberline]:
    atoms += int(i)
writecoordinfo = writeinfo[coordline:coordline+atoms]

from decimal import Decimal

def position(l, n):
    p = l[n].split()[:3]
    p = [Decimal(i) for i in p]
    return p
    
def distance(p1, p2 = [Decimal(0), Decimal(0), Decimal(0)]):
    s = 0
    for i in range(3):
        s += (p1[i] - p2[i])**2
    return Decimal.sqrt(s)

def diffvector(p1, p2):
    dv = []
    for i in range(3):
        d = p2[i] - p1[i]
        dv.append(d)
    return dv

def internal_division(p1, p2, n, m):
    o = []
    for i in range(3):
        k = (n*p2[i] + m*p1[i])/(n + m)
        o.append(k)
    return o

def cross(A, B):
    C1 = A[1]*B[2] - A[2]*B[1]
    C2 = A[2]*B[0] - A[0]*B[2]
    C3 = A[0]*B[1] - A[1]*B[0]
    return [C1, C2, C3]

def bridge(p1, p2, ra, rb):
    dis = distance(p1, p2)
    if dis > ra + rb:
        raise Exception('dis > ra + rb')
    a = ((ra**2-rb**2)/dis + dis)/Decimal(2)
    b = dis - a
    r = Decimal.sqrt(ra**2 - a**2)
    cen = internal_division(p1, p2, a, b)
    
    n = diffvector(p1, p2)
    n1, n2, n3 = n[0], n[1], n[2]
    r1, r2, r3 = cen[0], cen[1], cen[2]
    
    u1_t1 = n1*n3*r/Decimal.sqrt((n1*n3)**2 + (n2*n3)**2 + (n1**2 + n2**2)**2) + r1
    u1_t2 = -n1*n3*r/Decimal.sqrt((n1*n3)**2 + (n2*n3)**2 + (n1**2 + n2**2)**2) + r1
    
    u3_t1 = -(n1**2 + n2**2)*r/Decimal.sqrt((n1*n3)**2 + (n2*n3)**2 + (n1**2 + n2**2)**2) + r3
    u3_t2 = (n1**2 + n2**2)*r/Decimal.sqrt((n1*n3)**2 + (n2*n3)**2 + (n1**2 + n2**2)**2) + r3
    
    if u3_t1 > u3_t2:
        u1 = u1_t1
        u3 = u3_t1
    else:
        u1 = u1_t2
        u3 = u3_t2
        
    u2 = n2/n1*(u1-r1) + r2

    return [float(u1), float(u2), float(u3)]

def fold(p1, p2, p3, ra, rb, rc):
    
    n1 = diffvector(p1, p2)
    n2 = diffvector(p2, p3)
    u = cross(n1, n2)
    
    A = (ra**2 - rb**2 - distance(p1)**2 + distance(p2)**2)/2
    B = (rb**2 - rc**2 - distance(p2)**2 + distance(p3)**2)/2
    
    r1 = (A/n1[1] - B/n2[1])/(n1[0]/n1[1] - n2[0]/n2[1])
    r2 = A/n1[1] - n1[0]/n1[1]*r1
    
    p = (u[0]*(r1-p1[0]) + u[1]*(r2-p1[1]) - u[2]*p1[2])/distance(u)**2
    q = ((r1-p1[0])**2 + (r2-p1[1])**2 + p1[2]**2 - ra**2)/distance(u)**2
    
    t_1 = -p + Decimal.sqrt(p**2 - q)
    t_2 = -p - Decimal.sqrt(p**2 - q)
    
    if u[2]*t_1 > u[2]*t_2:
        t = t_1
    else:
        t = t_2
    
    x = float(u[0]*t + r1)
    y = float(u[1]*t + r2)
    z = float(u[2]*t)
    
    return [x, y, z]


# atomnumber = int(input('Enter the number of atom to change position: '))
# an = input('Atomic position number: ')
# rn = input('Distance from each atoms: ')


atomnumber = int(bpinfo[0])
an = bpinfo[1:3]
rn = bpinfo[3:5]

n1 = int(an[0])
n2 = int(an[1])
# n3 = int(an[2])

ra = float(rn[0])
rb = float(rn[1])
# rc = float(rn[2])

p1 = position(writecoordinfo, n1)
p2 = position(writecoordinfo, n2)
# p3 = position(writecoordinfo, n3)

ra = Decimal(ra)
rb = Decimal(rb)
# rc = Decimal(rc)

# fp = fold(p1, p2, p3, ra, rb, rc)
pos = bridge(p1, p2, ra, rb)


# coor = ''
# for i in fd:
#     if i > 10:
#         inter = ' '
#     else:
#         inter = '  '
#     coor += inter + str(round(i, 16))
# print(coor)

pos = f'{pos[0]:20.16f}{pos[1]:20.16f}{pos[2]:20.16f}'
print(pos)
writeinfo[coordline+atomnumber] = '   '.join([pos]+writeinfo[coordline+atomnumber].split()[3:])+'\n'

with open('POSCAR', 'w') as writefile:
    for linenumber, data in enumerate(writeinfo):
        writefile.write(data)