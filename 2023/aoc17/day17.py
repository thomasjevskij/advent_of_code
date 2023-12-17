from collections import namedtuple
import heapq

def parse_input():
    with open(0) as f:
        grid = {(x, y): int(c) for x, l in enumerate(f.read().split('\n')) for y, c in enumerate(l)}
    return grid

# They will not actually be x and y compared to example visualization. Doesn't matter
# Bit overkill with namedtuple. Prettier debugging
Node = namedtuple('Node', ['x', 'y', 'dx', 'dy'])

def dijkstra(grid, start, end, p):
    # Put what you want to sort on first in the tuple in your q
    q = [(0, Node(*start, 0, 0))]
    visited = set()
    while q:
        heat, n = heapq.heappop(q)
        if (n.x, n.y) == end:
            return heat
        if n in visited:
            continue
        visited.add(n)
        # Only examine turns. Not using complex rotations since complex doesn't have < for heapq
        dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)} - {(n.dx, n.dy), (-n.dx, -n.dy)}
        for dx, dy in dirs:
            tx, ty, t_heat = n.x, n.y, heat
            # Add x steps forward at once
            for i in range(p[1]):
                tx += dx
                ty += dy
                if (tx, ty) in grid:
                    t_heat += grid[(tx, ty)]
                    # This is for part 2, we don't add nodes where we can't turn
                    if i >= p[0]: 
                        heapq.heappush(q, (t_heat, Node(tx, ty, dx, dy)))

def p1(grid):
    s = dijkstra(grid, (0, 0), max(grid), (0, 3))
    print(s)

def p2(grid):
    s = dijkstra(grid, (0, 0), max(grid), (3, 10))
    print(s)

grid = parse_input()

p1(grid.copy())
p2(grid.copy())
