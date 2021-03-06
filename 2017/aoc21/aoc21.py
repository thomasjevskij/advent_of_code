import time
import numpy as np

def lookup(rules, arr):
    cases = [arr, np.rot90(arr), np.rot90(arr, 2), np.rot90(arr, 3),
             np.flip(arr, 1), np.rot90(np.flip(arr, 1)),
             np.rot90(np.flip(arr, 1), 2), np.rot90(np.flip(arr, 1), 3)]
    for c in cases:
        f = flat_arr(c)
        if f in rules:
            return rules[f]

def zoom(rules, grid):
    if len(grid) % 2 == 0:
        new_grid = np.zeros((3 * len(grid) // 2, 3 * len(grid) // 2), dtype=int)
        for row in range(len(grid) // 2):
            for col in range(len(grid) // 2):
                new_grid[row*3:row*3+3, col*3:col*3+3] = lookup(rules, grid[row*2:row*2+2, col*2:col*2+2])
        return new_grid[:]
    else:
        new_grid = np.zeros((4 * len(grid) // 3, 4 * len(grid) // 3), dtype=int)
        for row in range(len(grid) // 3):
            for col in range(len(grid) // 3):
                new_grid[row*4:row*4+4, col*4:col*4+4] = lookup(rules, grid[row*3:row*3+3, col*3:col*3+3])
        return new_grid[:]

t = time.process_time()

with open('in') as f:
    rule_input = f.read().split('\n')

rules = dict()
flat_arr = lambda arr: tuple(tuple(a) for a in arr)
parse_grid = lambda s, c: np.array(list(map(lambda x: list(map(int, x)), s.split(c))))

for rule in rule_input:
    before, after = map(lambda x: x.replace('.', '0').replace('#', '1'), rule.strip().split(' => '))
    aList = parse_grid(after, '/')
    bList = parse_grid(before, '/')
    rules[flat_arr(bList)] = aList
    
grid = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]], dtype = int)

for _ in range(5):
    grid = zoom(rules, grid)

print(f"Problem 1: {np.sum(grid)}")
t = time.process_time() - t
print(f"Time elapsed: {t:.2f} s")
t = time.process_time()

for _ in range(13):
    grid = zoom(rules, grid)
    
print(f"Problem 2: {np.sum(grid)}")
t = time.process_time() - t
print(f"Time elapsed: {t:.2f} s")