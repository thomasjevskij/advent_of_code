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

#t = time.process_time()

puzzle_input = 'ugkiagan'
squares = 0
grid = list()
for i in range(128):
    kh = knot_hash('{0}-{1}'.format(puzzle_input, i))
    bit_string = ''.join(map(lambda x: '{0:04b}'.format(int(x, 16)), kh))
    squares+= bit_string.count('1')
    grid.append(bit_string)

#t = time.process_time() - t
#print("Problem 1: {}".format(squares))
#print("Time elapsed: {0:.2f} s".format(t))
#t = time.process_time()

for i in range(128*128):
    s = '{} <-> {}'.format(i, i)
    row = i // 128
    col = i % 128
    if grid[row][col] == '1':
        dirs = [(row-1,col), (row,col-1)]
        for d in dirs:
            row, col = d
            if row >= 0 and row < 128 and col >= 0 and col < 128:
                if grid[row][col] == '1':
                    s += ', {}'.format(row*128+col)
        print(s)
        
    
#t = time.process_time() - t    

#print("Problem 2: {}".format(len(islands)))
#print("Time elapsed: {0:.2f} s".format(t))
