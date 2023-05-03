import numpy as np

a = """
     5.9571180000000004    0.0000000000000000    0.0000000000000000
    -2.9785599999999999    5.1590160000000003    0.0000000000000000
     0.0000000000000000    0.0000000000000000    9.1585000000000001
"""
a = a.split()
a = [float(i) for i in a]

A = np.array(a).reshape(3,3)


d = """
  0.1666665000000000  0.3333335000000000  0.0035505000000000
  0.1666665000000000  0.3333335000000000  0.5035505000000000
  0.1666665000000001  0.8333335000000001  0.0035505000000000
  0.1666665000000001  0.8333335000000001  0.5035505000000000
  0.6666665000000000  0.3333335000000000  0.0035505000000000
  0.6666665000000000  0.3333335000000000  0.5035505000000000
  0.6666665000000000  0.8333335000000001  0.0035505000000000
  0.6666665000000000  0.8333335000000001  0.5035505000000000
  0.3333335000000000  0.1666665000000000  0.2217815000000000
  0.3333335000000000  0.1666665000000000  0.7217815000000000
  0.3333335000000000  0.6666664999999999  0.2217815000000000
  0.3333335000000000  0.6666664999999999  0.7217815000000000
  0.8333335000000001  0.1666665000000000  0.2217815000000000
  0.8333335000000001  0.1666665000000000  0.7217815000000000
  0.8333335000000002  0.6666664999999999  0.2217815000000000
  0.8333335000000002  0.6666664999999999  0.7217815000000000
  0.0000000000000000  0.0000000000000000  0.3952660000000000
  0.3333335000000000  0.1666665000000000  0.1144170000000000
  0.0000000000000000  0.0000000000000000  0.8952660000000000
  0.3333335000000000  0.1666665000000000  0.6144170000000000
  0.0000000000000000  0.5000000000000000  0.3952660000000000
  0.3333335000000000  0.6666664999999999  0.1144170000000000
  0.0000000000000000  0.5000000000000000  0.8952660000000000
  0.3333335000000000  0.6666664999999999  0.6144170000000000
  0.5000000000000000  0.0000000000000000  0.3952660000000000
  0.8333335000000001  0.1666665000000000  0.1144170000000000
  0.5000000000000000  0.0000000000000000  0.8952660000000000
  0.8333335000000001  0.1666665000000000  0.6144170000000000
  0.5000000000000000  0.5000000000000000  0.3952660000000000
  0.8333335000000002  0.6666664999999999  0.1144170000000000
  0.5000000000000000  0.5000000000000000  0.8952660000000000
  0.8333335000000002  0.6666664999999999  0.6144170000000000
"""

d = d.split()
d = [float(i) for i in d]

d = np.array(d).reshape(32,3)

v = d@A

for i in v:
    k = ''
    for j in i:
        k += '  '+str(j)
    print(k)