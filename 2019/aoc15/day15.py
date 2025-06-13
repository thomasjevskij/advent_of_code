import sys
from collections import deque

sys.path.append('..')
from intcode import IntcodeComputer

def parse_input():
    with open(0) as f:
        lines = eval(f'[{f.read().strip()}]')
    return lines

# Map instructions to cartesian coordinates
dirs = {1: 1j, 2: -1j, 3: -1, 4: 1}
# Map instructions to their reverse instruction
r = {1: 2, 2: 1, 3: 4, 4: 3}

def get_bot_neighbors(bot):
    'The bot will actually try to move, then move back if he succeeds.'
    neighbors = []
    for i in (1, 2, 3, 4):
        bot.run(input_stream=[i])
        if bot.popleft() != 0:
            neighbors.append(i)
            bot.run(input_stream=[r[i]])
            bot.popleft()
    return neighbors

def bfs(bot):
    '''Same here, we move to the node, then back to the start for every step.
    Then we keep exploring the whole space after we found the shortest path, so
    we can fill the whole thing with oxygen after.'''
    Q = deque()
    visited = {}
    visited[0] = '.'
    Q.append((0, []))
    while Q:
        pos, path = Q.popleft()
        bot.run(input_stream=path[:])
        if bot.output_stream:
            response = bot.output_stream[-1]
            bot.output_stream.clear()
            if response == 2:
                visited[pos] = 'O'
                shortest = len(path)
        for n in get_bot_neighbors(bot):
            new_pos = pos + dirs[n]
            if new_pos not in visited:
                visited[new_pos] = '.'
                Q.append((new_pos, path[:] + [n]))
        bot.run(input_stream=[r[c] for c in path[::-1]])
        bot.output_stream.clear()
    return shortest, visited

def get_grid_neighbors(grid, pos):
    'Looking for neighbors for p2 when we have the grid mapped out.'
    return [pos + d for d in dirs.values() if grid.get(pos + d) == '.']

def fill(grid):
    '''Fill grid with oxygen one tick at a time. Keep track of the most
    recently filled cells and check their neighbors every tick.'''
    ticks = 0
    frontier = [key for key in grid if grid[key] == 'O']
    while '.' in grid.values():
        frontier = set(
            n for pos in frontier for n in get_grid_neighbors(grid, pos)
        )
        for pos in frontier:
            grid[pos] = 'O'
        ticks += 1
    return ticks

def p1(opcodes):
    bot = IntcodeComputer(opcodes[:])
    shortest, visited = bfs(bot)
    print(shortest)
    return visited

def p2(grid):
    ticks = fill(grid)
    print(ticks)

opcodes = parse_input()
p2(p1(opcodes))