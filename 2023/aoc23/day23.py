from collections import deque, defaultdict
from sys import setrecursionlimit
import re

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def get_neighbors(grid, point):
    x, y = point
    n = []
    match grid[y][x]:
        case '^':
            n.append((x, y-1))
        case '>':
            n.append((x+1, y))
        case 'v':
            n.append((x, y+1))
        case '<':
            n.append((x-1, y))
        case '.':
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x+dx, y+dy
                if ny > 0 and ny < len(grid) and grid[ny][nx] != '#':
                    n.append((nx, ny))
    return n

def make_graph(grid):
    sy = 0
    sx = grid[sy].find('.')
    ey = len(grid)-1
    ex = grid[ey].find('.')
    end = (ex, ey)
    graph = defaultdict(set)
    cur = (sx, sy)
    v = set()
    v.add(cur)
    q = deque()
    q.append(cur)
    while q:
        x, y = q.popleft()
        for n in get_neighbors(grid, (x, y)):
            node = find_next(grid, (x, y), n, end)
            if node is not None:
                dist, n_xy = node
                graph[(x, y)].add((dist, n_xy))
                if not n_xy in graph:
                    q.append(n_xy)
    return graph

def find_next(grid, prev, start, end):
    steps = 0
    q = deque()
    q.append(start)
    v = set()
    v.add(prev)
    while q:
        steps += 1
        (x, y) = q.popleft()
        v.add((x, y))
        if (x, y) == end:
            return (steps, (x, y))
        neighbors = get_neighbors(grid, (x, y))
        if prev in neighbors:
            neighbors.remove(prev)
        if len(neighbors) > 1:
            return (steps, (x, y))
        if len(neighbors) == 0:
            return None
        q.append(neighbors[0])
        prev = (x, y)

def dfs(graph, node, end, lens, v=set(), path=0):
    w, xy = node
    xy = node[1]
    v.add(xy)
    if xy == end:
        lens.append(path)
    else:
        for w, n_xy in graph[xy]:
            if not n_xy in v:
                dfs(graph, (w, n_xy), end, lens, v, path+w)
    if xy in v:
        v.remove(xy)

def p1(grid):
    start_y = 0
    start_x = grid[start_y].find('.')
    end_y = len(grid)-1
    end_x = grid[end_y].find('.')
    lens = []
    graph = make_graph(grid)
    dfs(graph, (0, (start_x, start_y)), (end_x, end_y), lens)
    print(max(lens))

def p2(grid):
    new_grid = [re.sub(r'[\<\^\>v]', '.', l) for l in grid]
    start_y = 0
    start_x = grid[start_y].find('.')
    end_y = len(grid)-1
    end_x = grid[end_y].find('.')
    lens = []
    graph = make_graph(new_grid)

    dfs(graph, (0, (start_x, start_y)), (end_x, end_y), lens)
    print(max(lens))

setrecursionlimit(1000000)
grid = parse_input()

p1(grid[:])
p2(grid[:])
