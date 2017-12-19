import time

t = time.process_time()
     
with open('in') as f:
    diagram = f.read().split('\n')

direction = 1 + 0j
pos = 0
pos += 1j*diagram[0].find('|')
log = ''
counter = 1
getRowCol = lambda z: map(int, (z.real, z.imag))
outOfBounds = lambda row, col, diagram: row < 0 or col < 0 or row >= len(diagram) or col >= len(diagram[row])
while True:
    counter += 1
    pos += direction
    row, col = getRowCol(pos)
    c = diagram[row][col]
    if c.isalpha():
        log += c
    if c == '+':
        for nd in (direction * 1j, direction * -1j): # Look ahead, multiplication with 1j is rotation
            row, col = getRowCol(pos + nd)
            if outOfBounds(row, col, diagram):
                continue # If this direction takes us out of bounds we don't wanna check the array
            if diagram[row][col] != ' ':
                direction = nd
                break
        continue
    row, col = getRowCol(pos + direction)
    if outOfBounds(row, col, diagram):
        break # If this direction takes us out of bounds we don't wanna check the array
    if diagram[row][col] == ' ': # If there's no plus but next step is a whitespace we're done
        break
    
t = time.process_time() - t
print(f"Problem 1: {log}")
print(f"Problem 2: {counter}")
print(f"Time elapsed: {t:.2f} s")