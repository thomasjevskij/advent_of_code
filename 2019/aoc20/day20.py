
from collections import defaultdict, deque
#%%
def parse_input(file=0):
    with open(file) as f:
        lines = [' ' + l + ' ' for l in f.read().strip('\n').split('\n')]
    grid = {}
    portals = defaultdict(list)
    s = ' ' * len(lines[0])
    lines.insert(0, s)
    lines.append(s)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '.':
                grid[(x - 1, y - 1)] = c
            if c.isupper():
                left, right = line[x - 1], line[x + 1]
                up, down = lines[y - 1][x], lines[y + 1][x]
                if left.isupper():
                    label = left + c
                elif up.isupper():
                    label = up + c
                elif right.isupper():
                    label = c + right
                elif down.isupper():
                    label = c + down
                if any(x == '.' for x in [left, right, up, down]):
                    grid[(x - 1, y - 1)] = label
                    portals[label].append((x - 1, y - 1))

    real_grid = defaultdict(list)
    for x, y in grid:
        if grid[(x, y)] == '.':
            for npos in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if npos not in grid:
                    continue
                if grid[npos] == '.':
                    real_grid[(x, y)].append(npos)
                elif grid[npos] not in ('AA', 'ZZ'):
                    nx, ny = [p for p in portals[grid[npos]] if p != npos][0]
                    warp = [
                        p for p in [(nx - 1, ny), (nx, ny - 1), (nx + 1, ny), (nx, ny + 1)]
                        if p in grid
                    ][0]
                    real_grid[(x, y)].append(warp)
                elif grid[npos] == 'AA':
                    start = (x, y)
                elif grid[npos] == 'ZZ':
                    end = (x, y)
    return real_grid, start, end

#%%
def get_neighbors(grid, portals, pos):
    x, y = pos
    for npos in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
        if npos in grid:
            tile = grid[npos]
            if tile in ('.', 'ZZ'):
                yield npos, tile
            elif tile == 'AA':
                continue
            else:
                warp = [x for x in portals[tile] if x != npos][0]
                yield warp, tile

# %%
def bfs(grid, start, end):
    Q = deque([(start, 0)])
    visited = set([start])
    while Q:
        node, depth = Q.popleft()
        if node == end:
            return depth
        for neighbor in grid[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                Q.append((neighbor, depth + 1))
# %%
