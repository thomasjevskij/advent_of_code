# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 07:45:39 2018

@author: Thomas
"""

import time
from collections import defaultdict
import re

t = time.process_time()

with open('in') as f:
    plan = sorted(f.read().split('\n'))

guards = defaultdict(lambda: defaultdict(int))
current_guard = 0
while len(plan) > 0:
    i = plan.pop(0)
    time_pattern = r'\[\d+-\d+-\d+ (\d+):(\d+)\]'
    start_hour, start_minute = map(int, re.findall(time_pattern, i)[0])
    
    guard_pattern = r'\[.+\] (\S+) (\S+)'
    action, arg = re.findall(guard_pattern, i)[0]
    if action == 'Guard':
        current_guard = int(arg[1:])
    else:
        stop_i = plan.pop(0)
        stop_hour, stop_minute = map(int, re.findall(time_pattern, stop_i)[0])
        for m in range(start_minute, stop_minute):
            guards[current_guard][m] += 1
            
sleepy = max(guards.items(), key = lambda x: sum(x[1].values()))
max_minute = max(sleepy[1].items(), key = lambda x: x[1])[0]
p1 = max_minute * sleepy[0]

print("Problem 1: {}".format(p1))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))

t = time.process_time()

sleepy = max(guards.items(), key = lambda x: max(x[1].values()))
max_minute = max(sleepy[1].items(), key = lambda x: x[1])[0]

p2 = max_minute * sleepy[0]
    
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))