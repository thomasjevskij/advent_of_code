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
    while Q:
        node, dist = Q.popleft()
        if node == goal:
            break
        n_list = (n for n in get_neighbors(node) if n not in obstacles and
        0 <= n[0] <= lim and 0 <= n[1] <= lim)
        for neighbor in n_list:
            if neighbor not in visited:
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
    lim, num_start = (7, 12) if len(b_list) == 25 else (71, 1024)
    for num in range(num_start, len(b_list)):
        if not bfs(set(b_list[:num]), (0, 0), (lim - 1, lim - 1)):
            print(','.join(map(str,b_list[num - 1])))
            break

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
