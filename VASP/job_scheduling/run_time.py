def grep(lines, searchtext):
    for line in lines:
        if searchtext in line:
            yield line

with open('OUTCAR') as f:
    lines = f.readlines()
    c = grep(lines, 'LOOP+')
    t = []
    for i in c:
        i = [i[21:31], i[42:52]]
        t.append(i)

cputime = 0
realtime = 0
for i in t:
    cputime += float(i[0])
    realtime += float(i[1])
    

print(f'Total CPU time:{cputime:>12.2f} sec')
print(f'{round(cputime/60, 2):>27.2f} min')
print(f'{round(cputime/3600, 2):>27.2f} hour\n')
print(f'Elapsed time:{round(realtime, 2):>14.2f} sec')
print(f'{round(realtime/60, 2):>27.2f} min')
print(f'{round(realtime/3600, 2):>27.2f} hour')


