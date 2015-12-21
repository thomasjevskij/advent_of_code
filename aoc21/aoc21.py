from time import process_time as tt
from itertools import product
from math import ceil

def fight(eq_list, enemy):
    damage = sum(e['damage'] for e in eq_list)
    armor = sum(e['armor'] for e in eq_list)
    hero_dps = max(damage-enemy['armor'], 1)
    enemy_dps = max(enemy['damage']-armor, 1)
    hero_times = ceil(enemy['hp'] / hero_dps)
    enemy_times = ceil(100 / enemy_dps)
    
    return hero_times <= enemy_times

def make_shop(s):
    with open(s) as f:
        items = []
        for line in f.readlines():
            args = line.rstrip().split()
            i = {}
            i['cost'] = int(args[-3])
            i['damage'] = int(args[-2])
            i['armor'] = int(args[-1])
            items.append(i)
    return items

t = tt()
weapons = make_shop('weapons.txt')
armors = make_shop('armor.txt')
rings = make_shop('rings.txt')
n = {'cost':0, 'damage':0, 'armor':0}
armors.append(n)
rings.append(n)
with open('input.txt') as f:
    boss = {}
    boss['hp'] = int(f.readline().rstrip().split()[-1])
    boss['damage'] = int(f.readline().rstrip().split()[-1])
    boss['armor'] = int(f.readline().rstrip().split()[-1])

max_cost = -1
min_cost = 10000
for eq_list in product(weapons, armors, rings, rings):
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
