import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from itertools import combinations
import matplotlib.colors as mcolors
import random



kB = 8.617333262145e-5   # eV/K
T = 298.15               # K
k = kB*T*np.log(10)


plt.figure(dpi = 400)
location = 'lower left'

pHmin = 0
pHmax = 14
Vmin = -k*14-0.2
Vmax = 2
Vmin = -1
# Vmax = 1.5
ref_V = 0

a = """
$Ni^{2+}$	0	2	-0.815796748
$Ni$	0	0	0
$NiO_2$	4	4	2.5039092
$NiOOH$	3	3	0.6777674
$Ni(OH)_2$	2	2	-0.7854334

"""

a = a.split()
A = np.array(a).reshape(len(a)//4, 4)

label = A[:, 0]
a = -k*A[:, 1].astype(np.float64)
b = -A[:, 2].astype(np.float64)
c = A[:, 3].astype(np.float64)
c = c -ref_V*b

colors = mcolors.CSS4_COLORS
colors = list(colors)
color = ['blue', 'dodgerblue', 'darkturquoise', 'lightgreen', 'lightsalmon', 'orangered']

cmap = plt.get_cmap('Paired')
color = list(cmap(list(range(20))))
# Paired Paired_r Pastel1 Pastel1_r Pastel2 Pastel2_r

# color = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

over_V = 1.6
over = 1
oer = 1
her = 1
fill = 1

# pH = x, V = y, G = z

###############################################################################
#                                                                             #
#                                                                             #
#                                                                             #
#                       No need to touch the code below                       #
#                                                                             #
#                                                                             #
#                                                                             #
###############################################################################


aref = a.max()+k
bref = b.max()+1
label = np.append(label, ['x_ref', 'y_ref'])
a = np.append(a, [aref, 0])
b = np.append(b, [0, bref])
c = np.append(c, [-pHmin*aref, -Vmin*bref])
for i in c:
    color.append(random.choice(colors))

def G(i, x, y):
    return a[i]*x + b[i]*y + c[i]

def mG(arr, x, y):
    g = [G(i, x, y) for i in arr]
    return min(g), arr[g.index(min(g))], label[arr[g.index(min(g))]]

def V(i, j, x):
    if b[j]-b[i] == 0:
        return np.nan*x
    else:
        return ((a[i]-a[j])/(b[j]-b[i]))*x + ((c[i]-c[j])/(b[j]-b[i]))

def pH(i, j, y):
    if a[j]-a[i] == 0:
        return np.nan*y
    else:
        return ((b[i]-b[j])/(a[j]-a[i]))*y + ((c[i]-c[j])/(a[j]-a[i]))

def intersection_point(i, j, k):
    A1 = a[i] - a[j]
    A2 = a[j] - a[k]
    B1 = b[i] - b[j]
    B2 = b[j] - b[k]
    C1 = c[i] - c[j]
    C2 = c[j] - c[k]
    if A1*B2 - A2*B1 == 0:
        x = np.nan
        y = np.nan
    else:
        x = (B1*C2 - B2*C1)/(A1*B2 - A2*B1)
        y = (A1*C2 - A2*C1)/(A2*B1 - A1*B2)
    return x, y

if len(a) == len(b) == len(c) <= len(label) <= len(color):
    pass
else:
    raise Exception('You must check len(a) == len(b) == len(c) <= len(label) <= len(color)')

arr = list(range(len(a)))
com = list(combinations(arr, 3))
inp = []
inpc = []
inpx = [pHmin, pHmax]
inpy = [Vmin, Vmax]
# inpx = []
# inpy = []
tl = []
gl = []
el = []
ch = 0

for p in arr:
    q = a[p], b[p], c[p]
    r = a[p], b[p]
    tl.append(q)
    gl.append(r)

if len(tl) != len(set(tl)):
    raise Exception('There is a problem with the coefficient.')

if len(set(gl)) == 1:
    ch = -1
    e = mG(arr, 0, 0)[1]
    el.append(e)
    if fill == 1:
        plt.fill_between([pHmin,pHmax], [Vmin,Vmin], [Vmax,Vmax], color = color[e])
elif len(arr) == 2:
    inpc.append(tuple(arr))
elif len(arr) > 2:
    for p in com:
        xp, yp = intersection_point(*p)
        if sum([G(i, xp, yp) == mG(arr, xp, yp)[0] for i in p]):
            inp.append(p)
            inpx.append(xp)
            inpy.append(yp)
            # plt.plot(xp, yp, 'o')
            # print(p, xp, yp)
    if inp == []:
        inp = list(combinations(arr, 3))
    for q in inp:
        for r in list(combinations(q, 2)):
            inpc.append(r)

inpx = list(set(inpx))
inpx.sort()
inpy = list(set(inpy))
inpy.sort()

if ch == 0:
    xml = []
    yml = []
    dic = {}
    for p in range(len(inpx)-1):
        xs = inpx[p]
        xt = inpx[p+1]
        xm = (xs+xt)/2
        xml.append(xm)
        for r in inpc:
            ym = V(*r, xm)
            if sum([G(i, xm, ym) == mG(arr, xm, ym)[0] for i in r]):
                # plt.plot([xs,xt], [V(*r, xs),V(*r, xt)], c=color[r[0]])
                o = xm, ym
                dic[o] = r, [xs,xt], [V(*r, xs),V(*r, xt)]
                yml.append(ym)

if ch == 0 and dic == {}:
    ch = 1

if ch == 1:
    xml = []
    yml = []
    dic = {}
    for p in range(len(inpy)-1):
        ys = inpy[p]
        yt = inpy[p+1]
        ym = (inpy[p]+inpy[p+1])/2
        yml.append(ym)
        for r in inpc:
            xm = pH(*r, ym)
            if sum([G(i, xm, ym) == mG(arr, xm, ym)[0] for i in r]):
                # plt.plot([pH(*r, ys),pH(*r, yt)], [ys,yt], c=color[r[0]])
                o = xm, ym
                dic[o] = r, [pH(*r, ys),pH(*r, yt)], [ys,yt]
                xml.append(xm)

if ch == 0:
    for xt in list(reversed(xml)):
        d = {}
        for key, value in dic.items():
            xm, ym = key
            if xm == xt:
                r, xl, yl = value
                d[ym] = xm, ym, xl, yl
                if fill == 0:
                    plt.plot(xl, yl, c=color[r[0]])
        d = sorted(d.items())
        ym = d[0][0]
        xm, yms, xl, ylmin = d[0][1]
        xm, ymt, xl, ylmax = d[-1][1]
        emin = mG(arr, xm, yms-1)[1]
        emax = mG(arr, xm, ymt+1)[1]
        el.append(emin)
        el.append(emax)
        if fill == 1:
            plt.fill_between(xl, [Vmin,Vmin], ylmin, color = color[emin])
        for i in range(len(d)-1):
            xm, yms, xl, ylmin = d[i][1]
            xm, ymt, xl, ylmax = d[i+1][1]
            e = mG(arr, xm, (yms+ymt)/2)[1]
            el.append(e)
            if fill == 1:
                plt.fill_between(xl, ylmin, ylmax, color = color[e])
        if fill == 1:
            plt.fill_between(xl, ylmax, [Vmax,Vmax], color = color[emax])

if ch == 1:
    for yt in list(reversed(yml)):
        d = {}
        for key, value in dic.items():
            xm, ym = key
            if ym == yt:
                r, xl, yl = value
                d[xm] = xm, ym, xl, yl
                if fill == 0:
                    plt.plot(xl, yl, c=color[r[0]])
        d = sorted(d.items())
        xm = d[0][0]
        xms, ym, xlmin, yl = d[0][1]
        xmt, ym, xlmax, yl = d[-1][1]
        emin = mG(arr, (xms+pHmin)/2, ym)[1]
        emax = mG(arr, (xms+pHmax)/2, ym)[1]
        el.append(emin)
        el.append(emax)
        if fill == 1:
            plt.fill_betweenx(yl, [pHmin,pHmin], xlmin, color = color[emin])
        for i in range(len(d)-1):
            xms, ym, xlmin, yl = d[i][1]
            xmt, ym, xlmax, yl = d[i+1][1]
            e = mG(arr, (xms+xmt)/2, ym)[1]
            el.append(e)
            if fill == 1:
                plt.fill_betweenx(yl, xlmin, xlmax, color = color[e])
        if fill == 1:
            plt.fill_betweenx(yl, xlmax, [pHmax,pHmax], color = color[emax])

el = list(set(el))
matches = []
for i in el:
    if label[i] != 'x_ref' and label[i] != 'y_ref':
        matches.append(mpatches.Patch(color = color[i], label = label[i]))
plt.legend(loc = location, handles = matches)
if over == 1:
    plt.plot([pHmin, pHmax], [ref_V+over_V-k*pHmin, ref_V+over_V-k*pHmax], c='black', linestyle='--')
if oer == 1:
    plt.plot([pHmin, pHmax], [ref_V+1.23-k*pHmin, ref_V+1.23-k*pHmax], c='black', linestyle='--')
if her == 1:
    plt.plot([pHmin, pHmax], [ref_V-k*pHmin, ref_V-k*pHmax], c='black', linestyle='--')
plt.xlim(pHmin, pHmax)
plt.ylim(Vmin, Vmax)
plt.xlabel('$pH$')
plt.ylabel('$U (V)$')
plt.show()