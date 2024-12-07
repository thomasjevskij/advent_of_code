from itertools import product, pairwise

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def get_xy(z):
    return int(z.real), int(z.imag)

def inside(z, grid):
    x, y = get_xy(z)
    xlim = (0, len(grid[0]) - 1)
    ylim = (0, len(grid) - 1)
    return x >= xlim[0] and x <= xlim[1] and y >= ylim[0] and y <= ylim[1]

def p1(grid):
    obstacles = set()
    for y, x in product(range(len(grid)), range(len(grid[0]))):
        if grid[y][x] == '^':
            start_pos = x + 1j*y
        elif grid[y][x] != '.':
            obstacles.add(x + 1j*y)

    _, visited = walk(grid, start_pos, -1j, obstacles)
    visited = set(p for p, _ in visited)
    print(len(visited))

    return grid, obstacles, start_pos, visited

def walk(grid, start_pos, start_dir, obstacles):
    pos = start_pos
    direction = start_dir
    visited = set()
    while inside(pos, grid):
        if (pos, direction) in visited:
            return True, visited
        visited.add((pos, direction))
        while pos + direction in obstacles:
            direction *= 1j
        pos += direction
    return False, visited

def p2(grid, obstacles, start_pos, visited):
    pos = start_pos
    direction = -1j
    visited.remove(pos)
    valid = set()
    for p in visited:
        loop, _ = walk(grid, pos, direction, obstacles | {p})
        if loop:
            valid.add(p)
    print(len(valid))

puzzle_input = parse_input()


p2(*p1(puzzle_input[:]))
