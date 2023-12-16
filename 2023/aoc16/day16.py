def get_xy(z):
    return int(z.real), int(z.imag)

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def illuminate(grid, start):
    visited = set() # Just to count energized
    splits = set() # Loop detection
    start_pos, start_dir = start
    beams = [[start_pos, start_dir]] # Add new beams here when split
    while beams: # While we still have beams to trace
        pos, dir = beams.pop(0)
        while True:
            col, row = get_xy(pos)
            if col < 0 or col >= len(grid[0]) or \
               row < 0 or row >= len(grid): # Out of bounds
                break
            visited.add((col, row))
            c = grid[row][col]
            if c == '/': # Reflection, linear algebra :)
                dir = -dir.imag - dir.real * 1j
            if c == '\\':
                dir = dir.imag + dir.real * 1j
            if c == '-' and dir.imag != 0:
                if pos in splits: # If we've already made a split, no need to make it again
                    break
                splits.add((pos))
                dir = 1+0j
                beams.append([pos, -1+0j])
            if c == '|' and dir.real != 0:
                if pos in splits:
                    break
                splits.add((pos))
                dir = 1j
                beams.append([pos, -1j])
            pos += dir
    return len(visited)

def p1(grid):
    s = illuminate(grid, (0+0j, 1+0j))
    print(s)
            

def p2(grid):
    cols = len(grid[0])
    rows = len(grid)
    s = []
    s.append(max(illuminate(grid, (0+row*1j, 1+0j)) for row in range(rows)))
    s.append(max(illuminate(grid, (cols-1+row*1j, -1+0j)) for row in range(rows)))
    s.append(max(illuminate(grid, (col+0j, 1j)) for col in range(cols)))
    s.append(max(illuminate(grid, (col+(rows-1)*1j, -1j)) for col in range(cols)))
    print(max(s))

grid = parse_input()

p1(grid[:])
p2(grid[:])
