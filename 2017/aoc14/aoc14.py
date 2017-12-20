import time
from collections import deque
from operator import xor
from functools import reduce

def knot_hash(string):
    lengths = list(map(ord, string))
    lengths.extend([17, 31, 73, 47, 23])
    curpos = 0
    skip_size = 0
    d = deque(range(256))

    for _ in range(64):
        for l in lengths:
            temp = list(d)
            d = deque(list(reversed(temp[:l]))+temp[l:])
            curpos += l + skip_size
            d.rotate(-l-skip_size)
            skip_size += 1
    d.rotate(curpos)
    return ''.join('{0:02x}'.format(reduce(xor, list(d)[i:i+16])) for i in range(0, len(d), 16))

def explore(grid, start):
    row, col = start
    to_visit = list()
    visited = [128*row+col]
    dirs = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    oob = lambda row, col: row >= 0 and row < 128 and col >= 0 and col < 128
    for row, col in dirs:
        if oob(row, col):
            if grid[row][col] == '1':
                to_visit.append((row, col))
                visited.append(128*row+col)
    while to_visit:
        row, col = to_visit.pop()
        dirs = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for row, col in dirs:
            if oob(row, col):
                if grid[row][col] == '1' and 128*row+col not in visited:
                    to_visit.append((row, col))
                    visited.append(128*row+col)
    return ','.join('{0:05d}'.format(i) for i in sorted(visited))
    

t = time.process_time()

puzzle_input = 'ugkiagan'
squares = 0
grid = list()
for i in range(128):
    kh = knot_hash('{0}-{1}'.format(puzzle_input, i))
    bit_string = ''.join(map(lambda x: '{0:04b}'.format(int(x, 16)), kh))
    squares+= bit_string.count('1')
    grid.append(bit_string)

t = time.process_time() - t
print("Problem 1: {}".format(squares))
print("Time elapsed: {0:.2f} s".format(t))
t = time.process_time()

islands = []
for i in range(128*128):
    row = i // 128
    col = i % 128
    if any('{0:05d}'.format(i) in isle for isle in islands) or grid[row][col] == '0':
        continue
    islands.append(explore(grid, (row, col)))
t = time.process_time() - t    

print("Problem 2: {}".format(len(islands)))
print("Time elapsed: {0:.2f} s".format(t))
