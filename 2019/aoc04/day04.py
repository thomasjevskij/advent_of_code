from itertools import pairwise

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines[0]

def p1(r):
    def valid(password):
        pair = False
        for f, s in pairwise(password):
            if f > s:
                return 0
            if f == s:
                pair = True
        return int(pair)
    start, stop = (int(x) for x in r.split('-'))
    s = sum(valid(f'{x}') for x in range(start, stop+1))
    print(s)

def p2(r):
    def valid(password):
        pair = False
        for f, s, in pairwise(password):
            if f > s:
                return 0
            if f == s and f*3 not in password:
                pair = True
        return int(pair)
    start, stop = (int(x) for x in r.split('-'))
    s = sum(valid(f'{x}') for x in range(start, stop+1))
    print(s)

puzzle_input = parse_input()

p1(puzzle_input)
p2(puzzle_input)
