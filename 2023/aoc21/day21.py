from collections import deque

def parse_input():
    with open(0) as f:
        lines = tuple(l.strip() for l in f.readlines())
    return lines

def walk(grid, steps, start):
    x, y = start
    v = {(x, y): 0}
    dist = 0
    q = deque()
    q.append((x, y))
    result = []
    while dist < max(steps):
        dist += 1
        q2 = deque()
        while q:
            x, y = q.popleft()    
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = dx + x, dy + y
                tx, ty = nx % len(grid[0]), ny % len(grid)
                if grid[ty][tx] != '#' and (nx, ny) not in v:
                    v[(nx, ny)] = dist
                    q2.append((nx, ny))
        q = q2
        if dist in steps:
            result.append(len([x for x in v.values() if x % 2 == dist % 2]))
    return result

def p1(grid):
    for y, l in enumerate(grid):
        for x, c in enumerate(l):
            if c == 'S':
                break
        if c == 'S':
            break
    s = walk(grid, [64], (x, y))[0]
    print(s)

def p2(grid):
    # Grid is quadratic (SIDE x SIDE) (131 x 131)
    # We start in the middle (65, 65)
    # filled area increase will cycle with a period of SIDE
    # So we can fit a 2nd degree polynomial f(n)
    # Let n=0 be SIDE // 2 steps, n=1 is SIDE // 2 + SIDE
    # n=3 is SIDE // 2 + 2*SIDE
    # 26501365 - 65 happens to be divisible by 131
    for y, l in enumerate(grid):
        for x, c in enumerate(l):
            if c == 'S':
                break
        if c == 'S':
            break
    SIDE = len(grid)
    HALF = x
    f0, f1, f2 = walk(grid, (HALF, HALF+SIDE, HALF+2*SIDE), (x, y))
    # System of equations:
    # f(0) = a*0**2 + b*0 + c = f0, so c = f0
    # f(1) = a*1**2 + b*1 + c = f1, so  a +  b = f1 - f0
    # f(2) = a*2**2 + b*2 + c = f2, so 4a + 2b = f2 - f0
    # Gauss elimination gives:         2a      = f2 - f0 - 2*(f1 - f0) = f2 - 2f1 + f0
    # This gives:                            b = f1 - f0 - a
    c = f0
    a = (f2 - 2*f1 + f0) // 2 # Don't worry this is an integer :-)
    b = f1 - f0 - a
    # Now we have our polynomial!
    f = lambda n: a*n**2 + b*n + c
    N = (26501365 - HALF) // SIDE
    print(f(N))

grid = parse_input()

p1(grid[:])
p2(grid[:])
