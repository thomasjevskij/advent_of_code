import time
from collections import defaultdict

def makeGrid(sGrid):
    grid = defaultdict(lambda: '.')
    mid = len(sGrid) // 2
    for row in range(len(sGrid)):
        for col in range(len(sGrid)):
            grid[(col-mid, -(row-mid))] = sGrid[row][col]
    return grid
def burst(grid, rules, iterations): 
    pos = 0 + 0*1j
    direction = 0 + 1j
    infections = 0
    for _ in range(iterations):
        xy = tuple(map(int, (pos.real, pos.imag)))
        newCell, newDir, newInf = rules[grid[xy]]
        grid[xy] = newCell
        direction *= newDir
        infections += newInf
        pos += direction
    return infections
t = time.process_time()

with open('in') as f:
    sGrid = f.read().split('\n')

grid = makeGrid(sGrid)
rules = {'#': ('.', -1j, 0), '.': ('#', 1j, 1)}

print(f"Problem 1: {burst(grid, rules, 10**4)}")
t = time.process_time() - t
print(f"Time elapsed: {t:.2f} s")
t = time.process_time()

grid = makeGrid(sGrid)
rules = {'#': ('F', -1j, 0), '.': ('W', 1j, 0),
         'W': ('#', 1, 1), 'F': ('.', -1, 0)}
    
print(f"Problem 2: {burst(grid, rules, 10**7)}")
t = time.process_time() - t
print(f"Time elapsed: {t:.2f} s")