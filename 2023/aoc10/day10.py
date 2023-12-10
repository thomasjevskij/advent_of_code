def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def get_xy(z):
    return (int(z.real), int(z.imag))

def p1(pipes):
    for y, p in enumerate(pipes):
        if (x := p.find('S')) != -1:
            start = x + y*1j
            break
    visited = set()
    possible = []
    if x - 1 >= 0 and pipes[y][x-1] in '-LF':
        possible.append(-1 + 0j)
    if x + 1 < len(pipes[y]) and pipes[y][x+1] in '-J7':
        possible.append(1 + 0j)
    if y - 1 >= 0 and pipes[y-1][x] in '|F7':
        possible.append(-1j)
    if y + 1 < len(pipes) and pipes[y+1][x] in '|JL':
        possible.append(1j)
    current = start
    deltas = {'|': (1j, -1j), '-': (1+0j, -1+0j), 'L': (-1j, 1+0j),
              'J': (-1j, -1+0j), '7': (1j, -1+0j), 'F': (1j, 1+0j),
              'S': tuple(possible)}
    visited.add(possible[1])
    while True:
        visited.add(current)
        x, y = get_xy(current)
        c = pipes[y][x]
        togo = [d for d in deltas[c] if not d+current in visited]
        if len(togo) == 0:
            break
        current += togo[0]
    print(len(visited) // 2)
    return visited

def bfs(v, pipes, root):
    v.add(root)
    q = [root]
    while q:
        node = q.pop(0)
        for n in (1+0j, -1+0j, 1j, -1j):
            neighbor = node+n
            x, y = get_xy(neighbor)
            if pipes[y][x] == '.' and neighbor not in v:
                q.append(neighbor)
                v.add(neighbor)

def p2(pipes, visited):
    # First change all useless pipes to '.'
    for y in range(len(pipes)):
        s = ''
        for x, c in enumerate(pipes[y]):
            if x+y*1j in visited:
                s += c
            else:
                s += '.'
        pipes[y] = '.'+s+'.' # padding
    
    # Add padding. This will break some example inputs. Code relies on the path having
    # just one space between itself and top left
    # With this we also guarantee no need to boundcheck in bfs
    pipes.insert(0, '.'*(len(pipes[0])))
    pipes.append('.'*len(pipes[0]))
    # Walk through the whole thing again but this time we will look to the sides
    for y, p in enumerate(pipes):
        if (x := p.find('S')) != -1:
            start = x + y*1j
            break
    side1 = set()
    side2 = set()
    visited = set()
    possible = []
    # This is just to figure out what the starting node is
    if pipes[y][x-1] in '-LF':
        possible.append(-1 + 0j)
    if pipes[y][x+1] in '-J7':
        possible.append(1 + 0j)
    if pipes[y-1][x] in '|F7':
        possible.append(-1j)
    if pipes[y+1][x] in '|JL':
        possible.append(1j)
    current = start
    deltas = {'|': (1j, -1j), '-': (1+0j, -1+0j), 'L': (-1j, 1+0j),
              'J': (-1j, -1+0j), '7': (1j, -1+0j), 'F': (1j, 1+0j),
              'S': tuple(possible)}
    prev = possible[1] # this sets direction, can pick any
    visited.add(prev)

    # We do a lookaround with complex rotations. One side will
    # be inside, one will be outside. Let's not worry which is 
    # which yet
    def look_around(cur, dir):
            xl, yl = get_xy(cur + dir * -1j)
            xr, yr = get_xy(cur + dir * 1j)
            if pipes[yl][xl] == '.':
                side1.add(xl + yl*1j)
            if pipes[yr][xr] == '.':
                side2.add(xr + yr*1j)
    while True:
        visited.add(current)
        x, y = get_xy(current)
        c = pipes[y][x]
        togo = [d for d in deltas[c] if not d+current in visited]
        if len(togo) == 0:
            break
        d = togo[0]
        # Here comes the first look around
        look_around(current, d)
        # We need to update the direction we are facing, then do the same thing again
        prev = current
        current += d
        d = current - prev
        look_around(current, d)

    # To figure out which side is which, I use the knowledge that my input
    # (before padding) had the loop on the top row. So with padding,
    # there will for sure be some outside nodes on row 0
    if any(z.imag == 0 for z in side1):
        inside = side2
    else:
        inside = side1
    v = set()
    # For every inside node we have, do a flood fill to find their neighbors.
    # We can be sure that an inside node is either adjacent to a pipe, or
    # adjacent to other inside nodes
    for z in inside:
        bfs(v, pipes, z)
    print(len(v))

puzzle_input = parse_input()

visited = p1(puzzle_input[:])
p2(puzzle_input[:], visited)
