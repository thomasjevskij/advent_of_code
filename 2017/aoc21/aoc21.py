import time
import numpy as np

def lookup(rules, arr):
    if flat_arr(arr) in rules:
        return rules[flat_arr(arr)]
    for _ in range(3):
        arr = np.rot90(arr)
        if flat_arr(arr) in rules:
            return rules[flat_arr(arr)]
    arr = np.flip(arr, 1)
    if flat_arr(arr) in rules:
        return rules[flat_arr(arr)]
    for _ in range(3):
        arr = np.rot90(arr)
        if flat_arr(arr) in rules:
            return rules[flat_arr(arr)]
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

for rule in rule_input:
    before, after = map(lambda x: x.replace('.', '0').replace('#', '1'), rule.strip().split(' => '))
    bList = []
    for line in before.split('/'):
        bList.append(list(map(int, line)))
    aList = []
    for line in after.split('/'):
        aList.append(list(map(int, line)))
    rules[flat_arr(np.array(bList))] = np.array(aList)
    
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