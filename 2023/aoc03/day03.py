import re
from collections import defaultdict, namedtuple

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]

    Part = namedtuple('Part', ['symbol', 'row', 'col'])
    def has_sym(to_check):
        for row, col in to_check:
            c = lines[row][col]
            if not c.isalpha() and c != '.':
                return Part(c, row, col)
        return None
    
    parts = defaultdict(list)
    for row, l in enumerate(lines):
        numbers = re.findall(r'\d+', l)
        for n in numbers:
            to_check = []
            start = l.find(n)
            end = start + len(n) - 1
            if start > 0:
                start -= 1
                to_check.append((row, start))
            if end < len(l) - 1:
                end += 1
                to_check.append((row, end))
            if row > 0:
                for i in range(start, end+1):
                    to_check.append((row - 1, i))
            if row < len(lines) - 2:
                for i in range(start, end+1):
                    to_check.append((row + 1, i))
            if g := has_sym(to_check):
                parts[g].append(int(n))
            l = l.replace(n, '.'*len(n), 1)
    return parts

def p1(parts):
    s = sum(sum(parts[p]) for p in parts)
    print(s)

def p2(parts):
    s = sum(parts[p][0] * parts[p][1] for p in parts if p.symbol == '*' and len(parts[p]) == 2)
    print(s)

parts = parse_input()

p1(parts.copy())
p2(parts.copy())
