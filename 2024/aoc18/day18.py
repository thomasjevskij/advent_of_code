from itertools import product
from collections import deque

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    b_list = [tuple(int(x) for x in l.split(',')) for l in lines]
    return b_list

def get_neighbors(pos):
    for d in [(1, 0), (0, 1)]:
        yield tuple(x + y for x, y in zip(pos, d))
        yield tuple(x - y for x, y in zip(pos, d))

def bfs(grid, start, goal):
    # Vanilla BFS
    visited = set()
    Q = deque()
    visited.add(start)
    Q.append((start, 0)) # Schema: (x, y), (steps from start)
    while Q:
        node, dist = Q.popleft()
        if node == goal:
            break
        n_list = (n for n in get_neighbors(node) if grid[n] == '.')
        for neighbor in n_list:
            if neighbor not in visited:
                visited.add(neighbor)
                Q.append((neighbor, dist + 1))
    if goal in visited:
        return dist
    return None

def p1(b_list):
    lim = 7 if len(b_list) == 25 else 71
    grid = {}
    for pos in product(range(lim), repeat=2):
        grid[pos] = '.'
    for pos in range(lim):
        grid[(-1, pos)] = '#'
        grid[(lim, pos)] = '#'
        grid[(pos, -1)] = '#'
        grid[(pos, lim)] = '#'
    num = 12 if len(b_list) == 25 else 1024
    for pos in b_list[:num]:
        grid[pos] = '#'
    c = bfs(grid, (0, 0), (lim - 1, lim - 1))
    print(c)

    return grid, b_list[num:]

def p2(grid, b_list):
    lim = 7 if len(b_list) == 25 - 12 else 71
    pos = b_list.pop(0)
    grid[pos] = '#'
    while bfs(grid, (0, 0), (lim - 1, lim - 1)):
        pos = b_list.pop(0)
        grid[pos] = '#'
    print(','.join(map(str, pos)))

puzzle_input = parse_input()


p2(*p1(puzzle_input[:]))
