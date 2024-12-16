from itertools import product
import heapq
from collections import deque
from more_itertools import consume

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    # Not really needed to switch data structure but it's a bit nicer than
    # having to bother with unpacking positions and [][] all the time.
    grid = {}
    x_lim = len(lines[0])
    y_lim = len(lines)
    for x, y in product(range(x_lim), range(y_lim)):
        grid[(x, y)] = lines[y][x]
        if lines[y][x] == 'S':
            start = (x, y)
        if lines[y][x] == 'E':
            end = (x, y)
    return grid, start, end

# :)
def rotate(tup):
    x, y = tup
    for i in (1, -1):
        new = (x + 1j * y) * 1j * i
        yield (int(new.real), int(new.imag))

# BFS with priority queue: Dijsktra
def find_path(grid, start):
    Q = []
    # Insert nodes as tuples with acc. weight first so heapq can sort for us
    heapq.heappush(Q, (0, start))
    visited = set()
    while Q:
        weight, node = heapq.heappop(Q)
        if grid[node[0]] == 'E':
            return weight
        if node not in visited:
            visited.add(node)
            pos, direction = node
            forward = tuple(x + d for x, d in zip(pos, direction))
            if grid[forward] != '#':
                heapq.heappush(Q, (weight + 1, (forward, direction)))
            for d in rotate(direction):
                heapq.heappush(Q, (weight + 1000, (pos, d)))

# Do DFS and keep track of lowest distance to each node
def find_all_paths(grid, start, lim):
    paths = []
    Q = deque()
    Q.append((0, [start]))
    visited = {}
    while Q:
        weight, path = Q.popleft()
        pos, direction = path[-1]
        if grid[pos] == 'E':
            paths.append((path, weight))
            continue
        if (pos, direction) in visited and visited[(pos, direction)] < weight:
            continue

        visited[(pos, direction)] = weight
        forward = tuple(x + d for x, d in zip(pos, direction))
        if grid[forward] != '#':
            new_path = list([*path, (forward, direction)])
            Q.append((weight + 1, new_path))
        for rot in rotate(direction):
            new_path = list([*path, (pos, rot)])
            Q.append((weight + 1000, new_path))
    return paths

def p1(grid, start, end):
    score = find_path(grid, (start, (1, 0)))
    print(score)
    return score

def p2(grid, start, end, score):
    seats = set()
    # :)
    consume(seats.update(pos for pos, _ in path)
            for path, s in find_all_paths(grid, (start, (1, 0)), score)
            if s == score)
    print(len(seats))

puzzle_input = parse_input()

score = p1(*puzzle_input[:])
p2(*puzzle_input[:], score)
