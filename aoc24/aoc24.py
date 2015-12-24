from itertools import combinations
from functools import reduce
from time import process_time as pt

t = pt()
with open('input.txt') as f:
    packages = list(map(int, f.readlines()))

all_loads = sum(packages)
p1_loads = []
p2_loads = []
done = False
i = 1
while not done:
    for c in combinations(packages, i):
        if sum(c) * 4 == all_loads:
            p2_loads.append(c)
        if sum(c) * 3 == all_loads:
            p1_loads.append(c)
            done = True        
    i += 1
p1 = 2**63
for l in p1_loads:
    p1 = min(p1, reduce(lambda x, y: x * y, l))
print("Problem 1: %d"%p1)
p2 = 2**63
for l in p2_loads:
    p2 = min(p2, reduce(lambda x, y: x * y, l))
t = pt() - t
print("Problem 2: %d"%p2)
print("Time elapsed: %d ms"%int(t * 1000))
