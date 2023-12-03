import re
from collections import defaultdict

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def p1(grid):
    def has_sym(to_check):
        for row, col in to_check:
            c = grid[row][col]
            if not c.isalpha() and c != '.':
                return True
        return False
    
    s = 0
    for row, l in enumerate(grid):
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
            if row < len(grid) - 2:
                for i in range(start, end+1):
                    to_check.append((row + 1, i))
            if has_sym(to_check):
                s += int(n)
            l = l.replace(n, '.'*len(n), 1)
    print(s)


def p2(grid):
    def has_sym(to_check):
        for row, col in to_check:
            c = grid[row][col]
            if c == '*':
                return (row, col)
        return None
    
    gears = defaultdict(list)
    for row, l in enumerate(grid):
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
            if row < len(grid) - 2:
                for i in range(start, end+1):
                    to_check.append((row + 1, i))
            if g := has_sym(to_check):
                gears[g].append(int(n))
            l = l.replace(n, '.'*len(n), 1)

    s = sum(gears[k][0]*gears[k][1] for k in gears if len(gears[k]) == 2)
    print(s)


puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
