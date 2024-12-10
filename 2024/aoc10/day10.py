from itertools import product
from collections import deque

def parse_input(filename=0):
    with open(filename) as f:
        grid = [[int(c) for c in l.strip()] for l in f.readlines()]
    return grid

def get_next(grid, x, y):
    candidates = [
        (xn, yn) for xn, yn in 
        ((x-1, y), (x, y-1), (x+1, y), (x, y+1))
        if 0 <= xn < len(grid[0]) and 0 <= yn < len(grid)
        and grid[yn][xn] == grid[y][x] + 1
    ]
    return candidates

def p1(grid):
    trailheads = [(x, y) for x, y in
        product(range(len(grid[0])), range(len(grid)))
        if grid[y][x] == 0]
    score = 0
    for head in trailheads:
        stack = []
        stack.append(head)
        visited = set()
        while stack:
            v = stack.pop(0)
            if v not in visited:
                visited.add(v)
                stack.extend(get_next(grid, *v))
        score += sum(grid[y][x] == 9 for x, y in visited)
    print(score)

def p2(grid):
    trailheads = [(x, y) for x, y in
        product(range(len(grid[0])), range(len(grid)))
        if grid[y][x] == 0]
    rating = 0
    for head in trailheads:
        queue = deque()
        queue.append([head])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if grid[y][x] == 9:
                rating += 1
            for adjacent in get_next(grid, x, y):
                new_path = list([*path, adjacent])
                queue.append(new_path)
    print(rating)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
