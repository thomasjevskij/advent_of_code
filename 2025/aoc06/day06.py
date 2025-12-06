from functools import reduce
import re

def parse_input(filename=0):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def p1(lines):
    lines[:-1] = [
        [int(n) for n in l.split()] for l in lines[:-1]
    ]
    guide = lines[-1].split()

    ops = {'*': lambda x, y: x*y, '+': lambda x, y: x+y}
    s = sum(
        reduce(
            ops[op],
            [l[i] for l in lines[:-1]]
        ) for i, op in enumerate(guide)
    )
    print(s)

def p2(lines):
    ops = {'*': lambda x, y: x*y, '+': lambda x, y: x+y}
    guide = lines[-1]
    current = 0
    total = 0
    while current < len(guide):
        # Look ahead on the operator line to know the number
        # of digits
        if m := re.search(r'[*+]', guide[current + 1:]):
            digits = m.start()
        else:
            digits = len(guide) - current
        
        # Take corresponding slice of each row and reverse
        # it (since it's right to left)
        numbers = [l[current:current + digits][::-1] for l in lines[:-1]]
        # Transpose it (since it's read column wise)
        numbers = list(zip(*numbers))
        # Finally turn into numbers
        numbers = [int(''.join(x)) for x in numbers]
        total += reduce(ops[guide[current]], numbers)
        current += digits + 1
    print(total)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
