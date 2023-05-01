with open('POSCAR', 'r') as readfile:
    info = []
    while True:
        line = readfile.readline()
        linesplit = line.split()
        info.append(linesplit)
        if not line: break

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def isInteger(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def LatticeConstant(l):
    r = 0
    for i in l:
        r += float(i)**2
    return r**0.5

def Dot(x, y):
    d = 0
    for i in range(len(x)):
        d += float(x[i])*float(y[i])
    return abs(d)

unitline = 0
for n, i in enumerate(info):
    if i != [] and isNumber(i[0]):
        test = [len(j) for j in info[n:n+4]]
        if test == [1, 3, 3, 3]:
            unitline = n
            break
unitinfo = info[unitline:unitline+4]
multiple = float(unitinfo[0][0])
a = LatticeConstant(unitinfo[1])*multiple
b = LatticeConstant(unitinfo[2])*multiple
c = LatticeConstant(unitinfo[3])*multiple

ab = Dot(unitinfo[1], unitinfo[2])
cosab = ab/(a*b)
sinab = (1 - cosab**2)**0.5

A = a*b*sinab
print(f'Surface area: {A}')
