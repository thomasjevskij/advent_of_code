import copy, time

def integral_image(grid):
    integral = []
    for line in grid:
        l = [line[0]]*len(line)
        for i in range(1, len(line)):
            l[i] = l[i-1]+line[i]
        integral.append(l)
    for x in range(len(integral)):
        for i in range(1, len(integral)):
            integral[i][x] += integral[i-1][x]
    return integral

def get_3by3(integral, rowcol):
    row, col = rowcol
    lowrow = max(row - 2, 0)
    lowcol = max(col - 2, 0)
    row = min(row + 1, len(integral) - 1)
    col = min(col + 1, len(integral) - 1)

        
    start = integral[row][col]
    if col > 2:
        start -= integral[row][lowcol]
    if row > 2:
        start -= integral[lowrow][col]
    if row > 2 and col > 2:
        start += integral[lowrow][lowcol]
    return start

def process_grid(grid):
    integral = integral_image(grid)
    new_grid = []
    for row, line in enumerate(grid):
        l = [0] * len(line)
        for col, cell in enumerate(line):
            n = get_3by3(integral, (row, col)) - cell
            #l[col] = n
            if grid[row][col] == 1 and (n == 2 or n == 3):
                l[col] = 1
            if grid[row][col] == 0 and n == 3:
                l[col] = 1
        new_grid.append(l)
    return new_grid

t = time.process_time()
grid = []
p2_grid = []
with open('input.txt') as f:
    for line in f.readlines():
        grid.append(list(map(lambda x: int(x=='#'), line.rstrip())))

p2_grid = copy.deepcopy(grid)
for i in range(100):
    grid = process_grid(grid)
    p2_grid = process_grid(p2_grid)
    p2_grid[0][0] = p2_grid[0][-1] = p2_grid[-1][0] = p2_grid[-1][-1] = 1
p1 = 0
p2 = 0
for i in range(len(grid)):
    p1 += sum(grid[i])
    p2 += sum(p2_grid[i])

t = time.process_time() - t
print("Problem 1: %d"%p1)
print("Problem 2: %d"%p2)
print("Elapsed time: %d ms"%int(t * 1000))
