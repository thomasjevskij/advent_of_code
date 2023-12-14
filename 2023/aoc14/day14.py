def parse_input():
    with open(0) as f:
        rocks = [list(l.strip()) for l in f.readlines()]
    return rocks

def roll_north(rocks, row, col):
    while True:
        if rocks[row-1][col] == '.' and row > 0:
            rocks[row][col] = '.'
            rocks[row-1][col] = 'O'
            row -= 1
        else:
            break
def roll_south(rocks, row, col):
    while True:
        if row < len(rocks) - 1 and rocks[row+1][col] == '.':
            rocks[row][col] = '.'
            rocks[row+1][col] = 'O'
            row += 1
        else:
            break
def roll_west(rocks, row, col):
    while True:
        if col > 0 and rocks[row][col-1] == '.':
            rocks[row][col] = '.'
            rocks[row][col-1] = 'O'
            col -= 1
        else:
            break
def roll_east(rocks, row, col):
    while True:
        if col < len(rocks[row]) - 1 and rocks[row][col+1] == '.':
            rocks[row][col] = '.'
            rocks[row][col+1] = 'O'
            col += 1
        else:
            break

def tilt_cycle(rocks):
    # ROLL NORTH
    for col in range(len(rocks[0])):
        for row in range(1, len(rocks)):
            if rocks[row][col] == 'O':
                roll_north(rocks, row, col)
    # ROLL WEST
    for row in range(len(rocks)):
        for col in range(1, len(rocks[0])):
            if rocks[row][col] == 'O':
                roll_west(rocks, row, col)
    # ROLL SOUTH
    for col in range(len(rocks[0])):
        for row in range(len(rocks)-2, -1, -1):
            if rocks[row][col] == 'O':
                roll_south(rocks, row, col)
    # ROLL EAST
    for row in range(len(rocks)):
        for col in range(len(rocks[0])-2, -1, -1):
            if rocks[row][col] == 'O':
                roll_east(rocks, row, col)

def flatten(r):
        return tuple(tuple(line) for line in r)

def p1(rocks):
    for col in range(len(rocks[0])):
        for row in range(1, len(rocks)):
            if rocks[row][col] == 'O':
                roll_north(rocks, row, col)
    s = sum(r.count('O')*(len(r)-i) for i, r in enumerate(rocks))
    print(s)

def p2(rocks):
    visited = []
    s = flatten(rocks)
    while True:
        visited.append(s)
        tilt_cycle(rocks)
        s = flatten(rocks)  
        if s in visited:
            start = visited.index(s)
            cycle_length = len(visited) - start            
            break
    i = (1_000_000_000 - start) % cycle_length + start
    print(sum(r.count('O')*(len(r)-i) for i, r in enumerate(visited[i])))

rocks = parse_input()

p1(rocks[:])
p2(rocks[:])
