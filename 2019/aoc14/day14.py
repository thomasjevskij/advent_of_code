import re
from math import ceil
from collections import defaultdict

def parse_input():
    '''Returns a dict where each ingredient string maps to its recipe as a
    (amount, [(sub_ingredient_amt, sub_ingredient), ...]) tuple.
    '''
    with open(0) as f:
        recipes = {}
        for lhs, rhs in [line.strip().split(' => ') for line in f.readlines()]:
            amt, result = rhs.split()
            recipe = [
                (int(a), b) for a, b in map(str.split, re.findall(r'\d+ \w+', lhs))
            ]
            recipes[result] = (int(amt), recipe)
    return recipes

def produce(recipes, key, amount, inventory):
    '''Returns amount of ore needed to produce amount of key according to
    ingredients. Inventory is a dict that maps each ingredient to an integer.
    It is only used inside the function but is passed as argument since it
    needs to persist throughout the recursion.
    '''
    makes, recipe = recipes[key]
    # Use any leftovers first
    r = min(amount, inventory[key])
    amount -= r
    inventory[key] -= r
    # Source needed material
    result = [(n * ceil(amount / makes), ing) for n, ing in recipe]
    # Store leftovers
    inventory[key] += amount % makes
    if len(result) == 1 and result[0][1] == 'ORE':
        return result[0][0]
    return sum(produce(recipes, ing, n, inventory) for n, ing in result)

def p1(recipes):
    total = produce(recipes, 'FUEL', 1, defaultdict(int))
    print(total)

def p2(recipes):
    'Just a binary search.'
    target = 1_000_000_000_000
    left, right = 1, target
    while left <= right:
        num_fuel = left + (right - left) // 2
        num_ore = produce(recipes, 'FUEL', num_fuel, defaultdict(int))
        if num_ore < target:
            left = num_fuel + 1
        elif num_ore > target:
            right = num_fuel - 1
        else:
            break
    print(num_fuel)

recipes = parse_input()

p1(recipes)
p2(recipes)
