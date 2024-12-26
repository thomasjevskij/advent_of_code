from itertools import product

def parse_input(filename=0):
    with open(filename) as f:
        schematics = f.read().split('\n\n')
    locks = []
    keys = []
    for schematic in schematics:
        t = tuple(column.count('#') - 1
                  for column in zip(*schematic.split('\n')))
        if schematic.startswith('#'):
            locks.append(t)
        else:
            keys.append(t)
    return locks, keys

def fit(lock, key):
    return all(l + k < 6 for l, k in zip(lock, key))

def p1(locks, keys):
    s = sum(fit(lock, key) for lock, key in product(locks, keys))
    print(s)

puzzle_input = parse_input()

p1(*puzzle_input[:])
