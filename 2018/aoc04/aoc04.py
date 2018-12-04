# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 07:45:39 2018

@author: Thomas
"""

import time
from collections import defaultdict
from datetime import datetime

def sort_key(s):
    timestamp = s[1:].split(']')[0]
    date, clock = timestamp.split(' ')
    year, month, day = map(int, date.split('-'))
    hour, minute = map(int, clock.split(':'))
    
    #return year * 100000 + month * 100000 + day * 1000 + 0.01 * minute + 10 * hour
    return datetime(year, month, day, hour, minute)

t = time.process_time()

with open('in') as f:
    observations = f.read().split('\n')

observations.sort(key = sort_key)
guards = defaultdict(lambda: defaultdict(int))
p1 = 0

plan = observations.copy()
current_guard = 0
while len(plan) > 0:
    i = plan.pop(0)
    print(i)
    timestamp, action = i[1:].split('] ')
    if action.startswith('Guard'):
        current_guard = int(action.split(' ')[1][1:])
    else:
        clock = timestamp.split(' ')[1]
        start_hour, start_minute = map(int, clock.split(':'))
        if start_hour != 0:
            start_minute = 0
        stop_i = plan.pop(0)
        print(stop_i)
        stop_stamp = stop_i[1:].split(']')[0]
        clock = stop_stamp.split(' ')[1]
        stop_hour, stop_minute = map(int, clock.split(':'))
        if stop_hour != 0:
            stop_minute = 59
        for m in range(start_minute, stop_minute):
            guards[current_guard][m] += 1
            
sleepy_guard = max(guards.items(), key = lambda x: len(x[1]))
max_minute = max(sleepy_guard[1].items(), key = lambda x: x[1])[0]
p1 = max_minute * sleepy_guard[0]

print("Problem 1: {}".format(p1))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))

t = time.process_time()

p2 = 0
    
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))