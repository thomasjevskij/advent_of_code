# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 07:48:33 2018

@author: Thomas
"""

import time
import re

t = time.process_time()

with open('in') as f:
    o_polymer = f.read().strip()

polymer = o_polymer
reg = re.compile(r'(.)(?!\1)(?i:\1)')

while True:
    old = len(polymer)
    polymer = reg.sub('', polymer)
    if old == len(polymer):
        p1 = len(polymer)
        break

print("Problem 1: {}".format(p1))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))

t = time.process_time()

o_polymer = polymer
p2 = len(o_polymer)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for c in alphabet:
    polymer = o_polymer.replace(c, '').replace(c.upper(), '')
    while True:
        old = len(polymer)
        polymer = reg.sub('', polymer)
        if old == len(polymer):
            p2 = min(p2, len(polymer))
            break
    
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))