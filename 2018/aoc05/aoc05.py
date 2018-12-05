# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 07:48:33 2018

@author: Thomas
"""

import time

def react(p):
    couples = []
    for i in range(1, len(p)):
        if abs(ord(p[i]) - ord(p[i - 1])) == 32:
            couples.append(p[i - 1] + p[i])
    for c in couples:
        p = p.replace(c, '')
    return len(couples), p

t = time.process_time()

with open('in') as f:
    o_polymer = f.read().strip()

polymer = o_polymer
alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:
    changes, polymer = react(polymer)
    if changes == 0:
        p1 = len(polymer)
        break

print("Problem 1: {}".format(p1))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))

t = time.process_time()

o_polymer = polymer
p2 = len(o_polymer)

for c in alphabet:
    polymer = o_polymer.replace(c, '').replace(c.upper(), '')
    while True:
        changes, polymer = react(polymer)
        if changes == 0:
            p2 = min(p2, len(polymer))
            break
    
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))