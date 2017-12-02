from itertools import permutations
import time

t = time.process_time()
cities = set()
ways = {}

with open('input.txt') as f:
    for d in f.readlines():
        a = d.split()
        cities.add(a[0])
        cities.add(a[2])
        ways[a[0]+a[2]] = int(a[-1])
        ways[a[2]+a[0]] = int(a[-1])

p1 = 100000
p2 = -1
for r in permutations(cities):
    route = 0
    for i in range(len(r) - 1):
        route += ways[r[i]+r[i+1]]
    p1 = min(p1, route)
    p2 = max(p2,route) 

t = time.process_time() - t 
print("Problem 1: %d"%p1)
print("Problem 2: %d"%p2)
print("Time elapsed: %d ms"%int(t * 1000))
