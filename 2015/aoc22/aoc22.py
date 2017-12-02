from copy import deepcopy
from random import sample
from time import process_time as pt

def missile(hero, boss):
    hero['mana'] -= 53
    boss['hp'] -= 4
    #print('Hero cast Magic Missile for 4 damage!')
def drain(hero, boss):
    hero['mana'] -= 73
    boss['hp'] -= 2
    hero['hp'] += 2
    #print('Hero Drained 2 damage!')
def shield(hero, boss):
    if hero['shield'] > 0:
        #print('You wasted your spell.')
        return
    hero['mana'] -= 113
    hero['shield'] = 6
    #print('Hero cast Shield!')
def poison(hero, boss):
    if boss['poison'] > 0:
        #print('You wasted your spell.')
        return
    hero['mana'] -= 173
    boss['poison'] = 6
    #print('Hero poisoned enemy!')
def recharge(hero, boss):
    if hero['recharge'] > 0:
        #print('You wasted your spell.')
        return
    hero['mana'] -= 229
    hero['recharge'] = 5
    #print('Hero cast Recharge!')

def validate(s, spells, mana):
    return s in spells.keys() and mana >= spells[s]['cost']

def fight(hero, boss, spells):
    mana_spent = 0
    turn = 0
    while True:
        if boss['hard'] and turn % 2 == 0:
            hero['hp'] -= 1
        if hero['mana'] < 53 or hero['hp'] <= 0:
            return (False, mana_spent)
        if boss['poison'] > 0:
            boss['hp'] -= 3
            boss['poison'] -= 1
            if boss['hp'] <= 0:
                return (True, mana_spent)
        if hero['shield'] > 0:
            hero['shield'] -= 1
            hero['armor'] = 7
        if hero['recharge'] > 0:
            hero['mana'] += 101
            hero['recharge'] -= 1
            
        if turn % 2 == 0:
            s = sample(spells.keys(), 1)[0]
            while not validate(s, spells, hero['mana']):
                s = sample(spells.keys(), 1)[0]
            spells[s]['function'](hero, boss)
            mana_spent += spells[s]['cost']
            if boss['hp'] <= 0:
                return (True, mana_spent)
        else:        
            hero['hp'] -= max(boss['damage'] - hero['armor'], 1)
            if hero['hp'] <= 0:
                return (False, mana_spent)
        # Cleanup
        hero['armor'] = 0
        turn += 1

t = pt()
spells = {}
spells['missile'] = {'cost': 53, 'function': missile}
spells['drain'] = {'cost': 73, 'function': drain}
spells['shield'] = {'cost': 113, 'function': shield}
spells['poison'] = {'cost': 173, 'function': poison}
spells['recharge'] = {'cost': 229, 'function': recharge}
#992
with open('input.txt') as f:
    boss = {}
    boss['hp'] = int(f.readline().rstrip().split()[-1])
    boss['damage'] = int(f.readline().rstrip().split()[-1])
boss['poison'] = 0
boss['hard'] = False
hero = {'hp': 50, 'mana': 500, 'armor': 0, 'shield': 0, 'recharge': 0}

with open('p1.txt') as f:
    p1 = int(f.readline().rstrip())
for i in range(1):
    result, mana = fight(deepcopy(hero), deepcopy(boss), spells)
    if result:
        p1 = min(p1, mana)
print("Problem 1: %d"%p1)
with open('p1.txt', 'w') as f:
    f.write("%d"%p1)
t = pt() - t
print("Time elapsed: %d ms"%int(t * 1000))

t = pt()
boss['hard'] = True
with open('p2.txt') as f:
    p2 = int(f.readline().rstrip())
for i in range(1):
    result, mana = fight(deepcopy(hero), deepcopy(boss), spells)
    if result:
        p2 = min(p2, mana)
print("Problem 2 so far: %d"%p2)
with open('p2.txt', 'w') as f:
    f.write("%d"%p2)
t = pt() - t
print("Time elapsed: %f s"%t)
