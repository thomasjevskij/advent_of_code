# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 10:48:14 2018

@author: Thomas
"""

import time
from collections import Counter
from itertools import combinations

t = time.process_time()

with open('in') as f:
    #box_ids = f.readlines()
    box_ids = f.read().split('\n')

twos = 0 
threes = 0
p1 = 0
p2 = 0

for ID in box_ids:
    counter = Counter(ID)
    twos += int(2 in counter.values())
    threes += int(3 in counter.values())
    
p1 = twos * threes

print("Problem 1: {}".format(p1))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))

t = time.process_time()
    
for s1, s2 in combinations(box_ids, 2):
    count = 0
    p2 = ''
    for x in range(len(s1)):
        if s1[x] != s2[x]:
            count += 1
        else:
            p2 += s1[x]
    if count == 1:
        break
    
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))