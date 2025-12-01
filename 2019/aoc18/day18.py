from collections import deque
from itertools import product

def parse_input(file=0):
    with open(file) as f:
        lines = f.read().strip().split('\n')
    grid = {(x, y): c for y, line in enumerate(lines)
            for x, c in enumerate(line) if c != '#'}
    return grid

def get_neighbors(grid, node):
    (x, y), keys = node
    for npos in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        tile = grid.get(npos)
        if tile is None:
            continue
        if (tile.isupper() and tile.lower() in keys) or tile in '.@':
            yield (npos, keys)
        elif tile.islower():
            nkeys = ''.join(sorted(set(keys + tile)))
            yield (npos, nkeys)

def get_neighbors_simple(grid, x, y):
    for pos in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if pos in grid:
            yield pos

def bfs(grid, start, end_keys):
    Q = deque()
    Q.append((start, 0))
    visited = set()
    visited.add(start)
    while Q:
        node, depth = Q.popleft()
        if node[1] == end_keys and end_keys != '':
            return depth
        for neighbor in get_neighbors(grid, node):
            if neighbor not in visited:
                visited.add(neighbor)
                Q.append((neighbor, depth + 1))
    print("Couldn't find the end")

def explore(grid, start):
    Q = deque()
    Q.append(start)
    visited = {}
    visited[start] = grid[start]
    while Q:
        x, y = Q.popleft()
        for neighbor in get_neighbors_simple(grid, x, y):
            if neighbor not in visited:
                visited[neighbor] = grid[neighbor]
                Q.append(neighbor)
    return visited

def p1(grid):
    start = [x for x in grid if grid[x] == '@'][0]
    keys = ''.join(sorted([grid[x] for x in grid if grid[x].islower()]))

    print(bfs(grid, (start, ''), keys))

def p2(grid):
    '''Based off a comment on reddit I tried this. Funny thing is that
    it doesn't work on the examples. So the input is "too" nicely formed
    I guess. Essentially create four sub grids (not assuming they are
    split into quadrants which is why we needed the explore() function),
    set all doors whose keys are in other quadrants to just '.', and
    then sum the sub searches. I suppose the "real" way is to build a
    proper graph with weights on the edges and use Dijsktra.'''
    sx, sy = [x for x in grid if grid[x] == '@'][0]
    keys = ''.join(sorted([grid[x] for x in grid if grid[x].islower()]))
    starts = []
    for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
        if abs(dx) + abs(dy) > 1:
            starts.append((sx + dx, sy + dy))
            grid[(sx + dx, sy + dy)] = '@'
        else:
            grid.pop((sx + dx, sy + dy))

    grids = [explore(grid, start) for start in starts]
    result = 0
    for g, s in zip(grids, starts):
        keys = ''.join(sorted([g[x] for x in g if g[x].islower()]))
        for k in g:
            if g[k].isupper() and g[k].lower() not in keys:
                g[k] = '.'
        result += bfs(g, (s, ''), keys)

    print(result)

grid = parse_input()

p1(grid.copy())
p2(grid.copy())
