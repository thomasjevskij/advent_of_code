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
with open('input.txt') as f:
    boss = {}
    f.readline()
    boss['damage'] = int(f.readline().rstrip().split()[-1])
    boss['armor'] = int(f.readline().rstrip().split()[-1])

max_cost = -1
min_cost = 10000
for w in weapons:
    eq_list = [w]
    if fight(eq_list, boss):
        min_cost = min(min_cost, sum(e['cost'] for e in eq_list))
    else:
        max_cost = max(max_cost, sum(e['cost'] for e in eq_list))
    for a in armors:
        eq_list = [w, a]
        if fight(eq_list, boss):
            min_cost = min(min_cost, sum(e['cost'] for e in eq_list))
        else:
            max_cost = max(max_cost, sum(e['cost'] for e in eq_list))
        for r1 in rings:
            eq_list = [w, r1]
            if fight(eq_list, boss):
                min_cost = min(min_cost, sum(e['cost'] for e in eq_list))
            else:
                max_cost = max(max_cost, sum(e['cost'] for e in eq_list))
            eq_list.append(a)
            if fight(eq_list, boss):
                min_cost = min(min_cost, sum(e['cost'] for e in eq_list))
            else:
                max_cost = max(max_cost, sum(e['cost'] for e in eq_list))
                
            for r2 in rings:
                if r1['cost'] == r2['cost']:
                    continue
                eq_list = [w, r1, r2]
                if fight(eq_list, boss):
                    min_cost = min(min_cost, sum(e['cost'] for e in eq_list))
                else:
                    max_cost = max(max_cost, sum(e['cost'] for e in eq_list))
                eq_list.append(a)
                if fight(eq_list, boss):
                    min_cost = min(min_cost, sum(e['cost'] for e in eq_list))
                else:
                    max_cost = max(max_cost, sum(e['cost'] for e in eq_list))

t = tt() - t      
print("Problem 1: %d"%min_cost)
print("Problem 2: %d"%max_cost)
print("Time elapsed: %d µs"%int(t*1000000))
