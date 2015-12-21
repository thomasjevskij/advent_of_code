from time import process_time as tt
from itertools import product

def fight(eq_list, enemy):
    damage = sum(e['damage'] for e in eq_list)
    armor = sum(e['armor'] for e in eq_list)
    hero_dps = max(damage-enemy['armor'], 1)
    enemy_dps = max(enemy['damage']-armor, 1)
    
    return hero_dps >= enemy_dps

t = tt()
with open('weapons.txt') as f:
    weapons = []
    for line in f.readlines():
        args = line.rstrip().split()
        w = {}
        w['cost'] = int(args[-3])
        w['damage'] = int(args[-2])
        w['armor'] = int(args[-1])
        weapons.append(w)
with open('armor.txt') as f:
    armors = []
    for line in f.readlines():
        args = line.rstrip().split()
        a = {}
        a['cost'] = int(args[-3])
        a['damage'] = int(args[-2])
        a['armor'] = int(args[-1])
        armors.append(a)
with open('rings.txt') as f:
    rings = []
    for line in f.readlines():
        args = line.rstrip().split()
        r = {}
        r['cost'] = int(args[-3])
        r['damage'] = int(args[-2])
        r['armor'] = int(args[-1])
        rings.append(r)
n = {'cost':0, 'damage':0, 'armor':0}
armors.append(n)
rings.append(n)
rings.append(n)
with open('input.txt') as f:
    boss = {}
    f.readline()
    boss['damage'] = int(f.readline().rstrip().split()[-1])
    boss['armor'] = int(f.readline().rstrip().split()[-1])

max_cost = -1
min_cost = 10000
for eq_list in product(weapons, armors, rings, rings):
    if len(eq_list) == 4:
        if eq_list[2]['cost'] > 0 and eq_list[2]['cost'] == eq_list[3]['cost']:
            continue
    if fight(eq_list, boss):
        min_cost = min(min_cost, sum(e['cost'] for e in eq_list))
    else:
        max_cost = max(max_cost, sum(e['cost'] for e in eq_list))

t = tt() - t      
print("Problem 1: %d"%min_cost)
print("Problem 2: %d"%max_cost)
print("Time elapsed: %d µs"%int(t*1000000))
