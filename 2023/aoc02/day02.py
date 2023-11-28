import re

def p1(lines):
    rules = {'red': 12, 'green': 13, 'blue': 14}
    s = 0
    for l in lines:
        game = int(re.findall(r'Game \d+', l.strip())[0].split()[-1])
        cubes = re.findall(r'\d+ red|\d+ green|\d+ blue', l.strip())
        for c in cubes:
            num, col = c.split()
            num = int(num)
            if num > rules[col]:
                s -= game
                break
        s += game
    print(s)

def p2(lines):
    s = 0
    for l in lines:
        cubes = re.findall(r'\d+ red|\d+ green|\d+ blue', l.strip())
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for c in cubes:
            num, col = c.split()
            num = int(num)
            min_cubes[col] = max(num, min_cubes[col])
        s += min_cubes["red"]*min_cubes["green"]*min_cubes["blue"]
    print(s)

with open(0) as f:
    lines = f.readlines()

p1(lines.copy())
p2(lines.copy())