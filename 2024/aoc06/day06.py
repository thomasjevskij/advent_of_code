from itertools import product

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def get_xy(z):
    return int(z.real), int(z.imag)

def p1(grid):
    xlim = (0, len(grid[0]) - 1)
    ylim = (0, len(grid) - 1)
    visited = set()
    direction = -1j
    obstacles = set()
    for y, x in product(range(len(grid)), range(len(grid[0]))):
        if grid[y][x] == '^':
            pos = x + 1j*y
        elif grid[y][x] != '.':
            obstacles.add(x + 1j*y)
    
    def inside(z):
        x, y = get_xy(z)
        return x >= xlim[0] and x <= xlim[1] and y >= ylim[0] and y <= ylim[1]
    
    turning_points = []
    while inside(pos):
        visited.add(pos)
        xn, yn = get_xy(pos + direction)    
        if xn + 1j*yn in obstacles:
            direction *= 1j
            turning_points.append((pos, direction))
        pos += direction
    print(len(visited))

    return turning_points, obstacles

# TODO: Stega igenom och för varje steg, titta till höger och se om det finns
# ett redan besökt hinder i line of sight.
def p2(turning_points, obstacles):
    num = 0
    corners = []
    for c1, c2, c3 in zip(turning_points, turning_points[1:], turning_points[2:]):
        pos, direction = c3
        target = c1[0]
        while True:
            zn = pos + direction
            if zn in obstacles:
                break
            if zn.real == target.real or zn.imag == target.imag:
                num += 1
                corners.append(zn)
                break
            pos += direction
    print(num, *(get_xy(z) for z in corners))


puzzle_input = parse_input()


p2(*p1(puzzle_input[:]))
