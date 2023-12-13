import numpy as np

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    patterns = []
    pattern = []
    while lines:
        p = lines.pop(0)
        if p != '':
            pattern.append(tuple(p))
        else:
            patterns.append(np.array(pattern))
            pattern = []
    patterns.append(np.array(pattern))
    return patterns

def p1(patterns):
    s = 0
    for m in patterns:
        rows, cols = m.shape
        for row in range(rows):
            shortest = min(row, rows-row) # so we don't compare matrix segments out of bounds
            if np.all(m[row:row+shortest,:] == np.flipud(m[row-shortest:row,:])):
                s += row * 100
        for col in range(cols):
            shortest = min(col, cols-col)
            if np.all(m[:,col:col+shortest] == np.fliplr(m[:,col-shortest:col])):
                s += col
    print(s)


def p2(patterns):
    s = 0
    for m in patterns:
        rows, cols = m.shape
        for row in range(rows):
            shortest = min(row, rows-row) 
            matches = np.count_nonzero(m[row:row+shortest,:] == np.flipud(m[row-shortest:row,:]))
            if matches == shortest * cols - 1:
                s += row * 100
        for col in range(cols):
            shortest = min(col, cols-col)
            matches = np.count_nonzero(m[:,col:col+shortest] == np.fliplr(m[:,col-shortest:col]))
            if matches == rows * shortest - 1:
                s += col
    print(s)

patterns = parse_input()

p1(patterns[:])
p2(patterns[:])
