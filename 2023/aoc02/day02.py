import re
from collections import namedtuple
from collections import namedtuple

def parse_input():
    with open(0) as f:
        lines = f.readlines()
    result = []
    Game = namedtuple('Game', ['num', 'red', 'green', 'blue'])
    for l in lines:
        num = int(re.findall(r'Game \d+', l.strip())[0].split()[-1])
        reds = list(map(lambda x: int(x.split()[0]), re.findall(r'\d+ red', l.strip())))
        greens = list(map(lambda x: int(x.split()[0]), re.findall(r'\d+ green', l.strip())))
        blues = list(map(lambda x: int(x.split()[0]), re.findall(r'\d+ blue', l.strip())))
        result.append(Game(num, max(reds), max(greens), max(blues)))
    return result
        

def p1(puzzle_input):
    red, green, blue = 12, 13, 14
    s = sum(g.num for g in puzzle_input if g.red <= red and g.green <= green and g.blue <= blue)
    print(s)

def p2(puzzle_input):
    s = sum(g.red * g.green * g.blue for g in puzzle_input)
def p2(puzzle_input):
    s = sum(g.red * g.green * g.blue for g in puzzle_input)
    print(s)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])