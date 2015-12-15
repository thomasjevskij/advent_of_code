import re
import functools

def generate_weights():
    for i in range(101):
        for j in range(101):
            for k in range(101):
                for l in range(101):
                    if i+j+k+l == 100:
                        yield (i, j, k, l)

with open('input.txt') as f:
    inp = f.readlines()

ing = []

for i in inp:
    args = re.search(r'capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$', i.rstrip()).groups()
    vals = map(int, args)
    ing.append(tuple(vals))
    
p1 = -1
p2 = -1
for weights in generate_weights():
    tot = [0, 0, 0, 0, 0]
    for i, item in enumerate(ing):
        for j, prop in enumerate(item):
            tot[j] += weights[i] * prop
    score = functools.reduce(lambda x,y: max(x,0)*max(y,0), tot[:-1])
    p1 = max(p1, score)
    p2 = max(p2, int(tot[-1] == 500) * score)

print("Problem 1: %d"%p1)
print("Problem 2: %d"%p2)
