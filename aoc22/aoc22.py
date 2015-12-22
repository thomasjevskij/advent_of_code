
def missile(hero, boss):
    hero['mana'] -= 53
    boss['hp'] -= 4
    print('Hero cast Magic Missile for 4 damage!')
def drain(hero, boss):
    hero['mana'] -= 73
    boss['hp'] -= 2
    hero['hp'] += 2
    print('Hero Drained 2 damage!')
def shield(hero, boss):
    hero['mana'] -= 113
    hero['shield'] = 6
    print('Hero cast Shield!')
def poison(hero, boss):
    hero['mana'] -= 173
    boss['poison'] = 6
    print('Hero poisoned enemy!')
def recharge(hero, boss):
    hero['mana'] -= 229
    hero['recharge'] = 5
    print('Hero cast Recharge!')

def validate(s, spells, mana):
    return s in spells.keys() and mana >= spells[s]['cost']

def fight(hero, boss, spells):
    mana_spent = 0
    while True:
        if boss['poison'] > 0:
            boss['hp'] -= 3
            boss['poison'] -= 1
            print('Boss takes 3 damage from poison and is poisoned for %d more turns!'%boss['poison'])
        if hero['shield'] > 0:
            hero['shield'] -= 1
            hero['armor'] = 7
            print('Shield is active for %d more turns!'%hero['shield'])
        if hero['recharge'] > 0:
            hero['mana'] += 101
            hero['recharge'] -= 1
            print('Hero gains 101 mana! Recharge is active for %d more turns!'%hero['recharge'])
        if hero['mana'] < 53:
            print('Out of mana, you lose!')
            return False
        print('Your hp: %d, your mana: %d, boss hp: %d!'%(hero['hp'], hero['mana'], boss['hp']))
        s = input('What do you do?')
        while not validate(s, spells, hero['mana']):
            s = input('Illegal action!')
        

spells = {}
spells['missile'] = {'cost': 53, 'function': missile}
spells['drain'] = {'cost': 73, 'function': drain}
spells['shield'] = {'cost': 113, 'function': shield}
spells['poison'] = {'cost': 173, 'function': poison}
spells['recharge'] = {'cost': 229, 'function': recharge}
#992
with open('input.txt') as f:
    boss = {}
    boss['hp'] = f.readline().rstrip().split()[-1]
    boss['damage'] = f.readline().rstrip().split()[-1]
boss['poison'] = 0
hero = {'hp': 50, 'mana': 500, 'armor': 0, 'shield': 0, 'recharge': 0}
print(hero)
print(boss)
