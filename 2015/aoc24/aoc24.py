from itertools import combinations
from functools import reduce
from time import process_time as pt

t = pt()
with open('input.txt') as f:
    packages = list(map(int, f.readlines()))

all_loads = sum(packages)
done = False
i = 1
p1 = p2 = 2**63
while not done:
    for c in combinations(packages, i):
        if sum(c) * 4 == all_loads:
            p2 = min(p2, reduce(lambda x, y: x * y, c))
        if sum(c) * 3 == all_loads:
            p1 = min(p1, reduce(lambda x, y: x * y, c))
            done = True        
    i += 1
t = pt() - t
print("Problem 1: %d"%p1)
print("Problem 2: %d"%p2)
print("Time elapsed: %d ms"%int(t * 1000))
