from itertools import product
from collections import deque

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    x_lim = len(lines[0])
    y_lim = len(lines)
    grid = {(x, y): lines[y][x] for x, y in product(range(x_lim),
                                                    range(y_lim))}
    # Pad :)
    for y in range(-1, y_lim + 1):
        grid[(-1, y)] = '.'
        grid[(x_lim, y)] = '.'
    for x in range(-1, x_lim + 1):
        grid[(x, -1)] = '.'
        grid[(x, y_lim)] = '.'

    return grid, x_lim, y_lim

def get_neighbors(pos):
    x, y = pos
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

# Return lists of the three cells that surround every corner of a cell
# Probably some fancy way to generate, but ordering is important for the
# code in p2, diagonal needs to be in the middle
def get_corner_neighbors(pos):
    x, y = pos
    yield [(x - 1, y), (x - 1, y - 1), (x, y - 1)]
    yield [(x, y - 1), (x + 1, y - 1), (x + 1, y)]
    yield [(x + 1, y), (x + 1, y + 1), (x, y + 1)]
    yield [(x, y + 1), (x - 1, y + 1), (x - 1, y)]

# Just BFS but also counting perimeter
def fill_plot(grid, start):
    Q = deque([start])
    visited = set()
    c = grid[start]
    visited.add(start)
    perimeter = 0
    while Q:
        v = Q.popleft()
        for vn in get_neighbors(v):
            if grid[vn] != c:
                perimeter += 1
            elif vn not in visited:
                visited.add(vn)
                Q.append(vn)
    return perimeter, visited

def p1(grid, x_lim, y_lim):
    visited = set()
    price = 0
    # Safest to go through every cell to take into accounts disjoint plots
    # with same ID
    for pos in product(range(x_lim), range(y_lim)):
        if pos not in visited:
            perimeter, plot = fill_plot(grid, pos)
            visited.update(plot)
            price += perimeter * len(plot)
    print(price)

# Corner cases:
# ABB XAA
# BBB ABB
# BBB ABB
# X can be either B or something else then look for this for every corner
def p2(grid, x_lim, y_lim):
    visited = set()
    price = 0
    for pos in product(range(x_lim), range(y_lim)):
        if pos not in visited:
            _, plot = fill_plot(grid, pos)
            visited.update(plot)
            c = grid[pos]
            # The trick is that number of corners == number of sides
            # But IMO corners are easier to find especially if we assume
            # the plots aren't convex
            corners = 0
            for plot_pos in plot:
                # Have a look at this BEAUTIFUL list comprehension we use
                # to avoid nested ifs and fors
                corners += sum(
                    all(grid[cn] != c for cn in cn_list[::2])
                    or (all(grid[cn] == c for cn in cn_list[::2])
                    and grid[cn_list[1]] != c) for cn_list
                    in get_corner_neighbors(plot_pos)
                )
            price += corners * len(plot)
    print(price)

puzzle_input = parse_input()

p1(*puzzle_input[:])
p2(*puzzle_input[:])
