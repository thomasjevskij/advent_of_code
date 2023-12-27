from collections import defaultdict

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def p1(lines):
    parents = {}
    for l in lines:
        parent, child = l.split(')')
        parents[child] = parent
    def count_parents(child):
        result = 0
        while child in parents:
            result += 1
            child = parents[child]
        return result
    
    s = sum(count_parents(c) for c in parents)
    print(s)
    return parents

def p2(parents):
    my_list = []
    x = 'YOU'
    while parents[x] in parents:
        my_list.append(parents[x])
        x = parents[x]
    x = 'SAN'
    s = -1
    while x not in my_list:
        s += 1
        x = parents[x]
    print(s+my_list.index(x))

puzzle_input = parse_input()

p2(p1(puzzle_input[:]))
