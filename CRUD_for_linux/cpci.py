# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:12:58 2022

@author: cjw
"""


import os
import sys

for i in sys.argv[1:]:
    os.system(f'scp input.py CONTCAR run_vasp.sh {i}')