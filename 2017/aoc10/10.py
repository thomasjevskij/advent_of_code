import time
from collections import deque
from functools import reduce
from operator import xor

t = time.process_time()

with open('in') as f:
    in_string = f.read()

d = deque(range(256))
curpos = 0
lengths = map(int, in_string.split(','))
skip_size = 0

for l in lengths:
    temp = list(d)
    d = deque(list(reversed(temp[:l]))+temp[l:])
    curpos += l + skip_size
    d.rotate(-l-skip_size)
    skip_size += 1
    
d.rotate(curpos%len(d))

print("Problem 1: {}".format(d[0]*d[1]))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))

t = time.process_time()

lengths_2 = list(map(ord, in_string))
lengths_2.extend([17, 31, 73, 47, 23])
curpos = 0
skip_size = 0
d = deque(range(256))

for _ in range(64):
    for l in lengths_2:
        temp = list(d)
        d = deque(list(reversed(temp[:l]))+temp[l:])
        curpos += l + skip_size
        d.rotate(-l-skip_size)
        skip_size += 1
d.rotate(curpos%len(d))

sparse_hash = list(d)
dense_hash = ''.join('{0:02x}'.format(reduce(xor, sparse_hash[i:i+16])) for i in range(0, len(d), 16))

print("Problem 2: {}".format(dense_hash))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
