from itertools import product

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    grid = {}
    x_lim, y_lim = (len(lines[0]), len(lines))
    for x, y in product(range(x_lim), range(y_lim)):
        grid[(x, y)] = lines[y][x]
        if lines[y][x] == 'S':
            start = (x, y)
        if lines[y][x] == 'E':
            goal = (x, y)
    return grid, start, goal

def get_neighbors(pos):
    for d in [(1, 0), (0, 1)]:
        npos = tuple(x + y for x, y in zip(pos, d))
        yield npos
        npos = tuple(x - y for x, y in zip(pos, d))
        yield npos

# Vanilla, save the whole path
def bfs(grid, start, goal):
    Q = []
    visited = set()
    visited.add(start)
    Q.append([start])
    valid = lambda n: n not in visited and grid[n] != '#'
    for path in Q:
        node = path[-1]
        if node == goal:
            break
        for neighbor in filter(valid, get_neighbors(node)):
            visited.add(neighbor)
            new_path = list([*path, neighbor])
            Q.append(new_path)
    return path

# Get points on the circumference of a circle around pos
# (circle as defined with Manhattan distance)
def get_circle(pos, radius=2):
    s = set()
    for i in range(radius + 1):
        x, y = (i, radius - i)
        s.update([(x, y), (-x, -y), (x, -y), (-x, y)])
    for d in s:
        yield tuple(x + y for x, y in zip(pos, d))

# Assumes that every point on the original path is always the closest
# i.e., we can't cheat to an unexplored path that is closer to the goal
def p1(grid, start, goal):
    path_list = bfs(grid, start, goal)
    path = {pos: i for i, pos in enumerate(path_list)}
    c = 0
    # Checking if it's the example input or no
    lim = 2 if len(path_list) == 85 else 100
    for i, pos in enumerate(path_list):
        # path[n] - i - 2 is how much closer to the goal we 
        # end up. 2 because if we stay on the path after 2
        # steps, we end up 2 steps closer
        valid = lambda n: n in path and path[n] - i - 2 >= lim
        c += sum(valid(n) for n in get_circle(pos))
    print(c)

    return path_list, path

def p2(path_list, path):
    c = 0
    # If example input
    lim = 50 if len(path_list) == 85 else 100
    for i, pos in enumerate(path_list):
        for steps in range(2, 21):
            valid = lambda n: n in path and path[n] - i - steps >= lim
            c += sum(valid(n) for n in get_circle(pos, steps))
    print(c)

puzzle_input = parse_input()

p2(*p1(*puzzle_input[:]))
