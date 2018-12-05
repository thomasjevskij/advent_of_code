# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:30:14 2018

@author: Thomas
"""

import time
from collections import defaultdict
from itertools import product

t = time.process_time()

with open('in') as f:
    claims = f.read().split('\n')

fabric = defaultdict(int)

for c in claims:
    dims = c.split('@')[1]
    start, size = dims.split(': ')
    start_x, start_y = map(int, start.split(','))
    width, height = map(int, size.split('x'))
    for (x, y) in product(range(start_x, start_x + width), range(start_y, start_y + height)):    
        fabric[(x, y)] += 1
            
p1 = sum(x > 1 for x in fabric.values())

print("Problem 1: {}".format(p1))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))

t = time.process_time()

for c in claims:
    ID, dims = c.split('@')
    start, size = dims.split(': ')
    start_x, start_y = map(int, start.split(','))
    width, height = map(int, size.split('x'))
    counter = sum(fabric[(x, y)] for (x, y) in product(range(start_x, start_x + width), range(start_y, start_y + height)))
    if counter == width * height:
        p2 = ID[1:].strip()
        break
    
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))