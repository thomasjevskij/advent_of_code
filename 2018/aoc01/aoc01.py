# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 10:48:14 2018

@author: Thomas
"""

import time
from collections import defaultdict

t = time.process_time()

with open('in') as f:
    instructions = f.read().replace('\n', ' ').strip()
    
p1 = eval(f'0{instructions}')

print("Problem 1: {}".format(p1))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))

t = time.process_time()

p2 = 0
log = defaultdict(int)
log[p2] += 1

instructions = instructions.split(' ')
while True:
    i = instructions.pop(0)
    p2 = eval(f'{p2}{i}')
    log[p2] += 1
    if log[p2] == 2:
        break
    instructions.append(i)
    
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))