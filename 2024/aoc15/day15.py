from itertools import pairwise

def parse_input(filename=0):
    with open(filename) as f:
        lines, moves = f.read().split('\n\n')
    grid = {}
    lines = lines.split('\n')
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x + 1j * y] = c
            if c == '@':
                start = x + 1j * y
    return grid, start, ''.join(moves.split('\n'))

def peek(grid, pos, direction):
    result = []
    while True:
        result.append(pos)
        if grid[pos] == '#':
            return []
        if grid[pos] == '.':
            break
        pos += direction
    return result

def move(grid, pos_list):
    for p1, p2 in pairwise(pos_list[::-1]):
        temp = grid[p2]
        grid[p2] = grid[p1]
        grid[p1] = temp

def expand_grid(grid):
    new_grid = {}
    for pos in grid:
        npos = 2 * pos.real + 1j * pos.imag
        match grid[pos]:
            case 'O':
                new_grid[npos] = '['
                new_grid[npos + 1] = ']'
            case '@':
                new_grid[npos] = '@'
                new_grid[npos + 1] = '.'
                start = npos
            case _:
                new_grid[npos] = grid[pos]
                new_grid[npos + 1] = grid[pos]
    return new_grid, start

def peek_vertical(grid, pos, direction):
    result = [set([pos])]
    while True:
        next_row = set()
        to_look = [p + direction for p in result[-1] if grid[p] in '[]@']
        for p in to_look:
            next_row.add(p)
            if grid[p] == '[':
                next_row.add(p + 1)
            if grid[p] == ']':
                next_row.add(p - 1)
            if grid[p] == '#':
                return []
        result.append(next_row)
        if all(grid[p] == '.' for p in next_row):
            break
    return result

def move_vertical(grid, pos_list, direction):
    for row, nrow in pairwise(pos_list[::-1]):
        for p in row:
            if p-direction in nrow:
                temp = grid[p]
                grid[p] = grid[p - direction]
                grid[p - direction] = temp

def p1(grid, start, moves):
    pos = start
    dirs = {'<': -1, '^': -1j, '>': 1, 'v': 1j}
    for m in moves:
        d = dirs[m]
        pos_list = peek(grid, pos, d)
        if pos_list:
            move(grid, pos_list)
            pos += d
    score = int(sum(100*z.imag + z.real for z in grid if grid[z] == 'O'))
    print(score)

def p2(grid, start, moves):
    pos = start
    dirs = {'<': -1, '^': -1j, '>': 1, 'v': 1j}
    for m in moves:
        d = dirs[m]
        if m in '<>':
            pos_list = peek(grid, pos, d)
            if pos_list: 
                move(grid, pos_list)
                pos += d
        else:
            pos_list = peek_vertical(grid, pos, d)
            if pos_list:
                move_vertical(grid, pos_list, d)
                pos += d
    score = int(sum(100*z.imag + z.real for z in grid if grid[z] == '['))
    print(score)

grid, start, moves = parse_input()
new_grid, new_start = expand_grid(grid)

p1(grid, start, moves)
p2(new_grid, new_start, moves)
