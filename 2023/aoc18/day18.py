import numpy as np

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def find_area(lines):
    cur = np.array([0, 0])
    xy_list = [cur]
    edge = 0
    dirs = {'R': np.array([1, 0]), 'L': np.array([-1, 0]), 
            'U': np.array([0, -1]), 'D': np.array([0, 1])}
    for dir, amt in lines:
        dir = dirs[dir]
        amt = int(amt)
        edge += amt
        cur = cur + dir*amt
        xy_list.append(cur)
    s = sum(
        row1 * col2 - row2 * col1
        for (row1, col1), (row2, col2) in zip(xy_list, xy_list[1:])
    ) / 2
    return(int(abs(s)-0.5*edge+1)+edge)

def p1(lines):
    vertices = []
    for l in lines:
        dir, amt, _ = l.split()
        vertices.append((dir, amt))
    print(find_area(vertices))

def p2(lines):
    vertices = []
    for l in lines:
        _, _, num = map(lambda x: x.strip('(#)'), l.split())
        amt = int(num[:-1], base=16)
        dirs = 'RDLU'
        vertices.append((dirs[int(num[-1])], amt))
    print(find_area(vertices))


puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
