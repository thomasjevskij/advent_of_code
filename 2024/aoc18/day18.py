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

def bfs(obstacles, start, goal):
    # Vanilla BFS
    lim = goal[0]
    visited = set()
    Q = deque()
    visited.add(start)
    Q.append((start, 0)) # Schema: (x, y), (steps from start)
    # Put the filter here so the if statement below is less ugly
    valid = lambda n: n not in obstacles \
                      and 0 <= n[0] <= lim and 0 <= n[1] <= lim \
                      and n not in visited
    while Q:
        node, dist = Q.popleft()
        if node == goal:
            break
        # Just messing around with filter instead of generator expression
        # Actually if I didn't use filter, I'd have to put the generator
        # expression on its own row, or put if statements _in_ the for
        # loop
        for neighbor in filter(valid, get_neighbors(node)):
            visited.add(neighbor)
            Q.append((neighbor, dist + 1))
    if goal in visited:
        return dist
    return None

def p1(b_list):
    lim, num = (7, 12) if len(b_list) == 25 else (71, 1024)
    c = bfs(set(b_list[:num]), (0, 0), (lim - 1, lim - 1))
    print(c)

def p2(b_list):
    lim, L = (7, 12) if len(b_list) == 25 else (71, 1024)
    R = len(b_list) - 1
    # Binary search for SPEED (linear search worked just fine)
    # Avoid final iteration (usually condition is L <= R) because
    # we already know we will find an answer here
    while L < R:
        num = (L + R) // 2
        if bfs(set(b_list[:num]), (0, 0), (lim - 1, lim - 1)):
            L = num + 1
        else:
            R = num - 1
    print(','.join(map(str,b_list[(L + R) // 2])))

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
