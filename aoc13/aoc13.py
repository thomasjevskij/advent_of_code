from itertools import permutations

def comp_max(guests, edges):
    max_route = -1
    for r in permutations(guests):
        route = 0
        for i in range(len(r) - 1):
            route += edges[r[i]+r[i+1]] + edges[r[i+1]+r[i]]
        route += edges[r[0]+r[-1]] + edges[r[-1]+r[0]]
        max_route = max(max_route,route)
    return max_route

with open('input.txt') as f:
    rel = f.readlines()

guests = set()
edges = {}

for r in rel:
    args = r.strip().split()
    
    val = 0
    if args[2] == 'gain':
        val = int(args[3])
    else:
        val = -int(args[3])
    guests.add(args[0])
    edges[args[0]+args[-1].rstrip('.')] = val

print("Problem 1: %d"%comp_max(guests, edges))

for g in guests:
    edges['Me'+g] = 0
    edges[g+'Me'] = 0
guests.add('Me')

print("Problem 2: %d"%comp_max(guests, edges))
