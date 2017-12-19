import time

t = time.process_time()
     
with open('in') as f:
    diagram = f.read().split('\n')

direction = (1, 0)
row = 0
col = diagram[row].find('|')
log = ''
counter = 1

while True:
    counter += 1
    row += direction[0]
    col += direction[1]
    pos = diagram[row][col]
    if pos.isalpha():
        log += pos
    if pos == '+':
        newdirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        newdirs.remove(direction) # Can't turn forward
        newdirs.remove((-direction[0], -direction[1])) # Can't turn backward
        for r, c in newdirs: # Look ahead
            test_row = row+r
            test_col = col+c
            if test_row < 0 or test_col < 0 or test_row >= len(diagram) or test_col >= len(diagram[row]):
                continue # If this direction takes us out of bounds we don't wanna check the array
            if diagram[test_row][test_col] != ' ':
                direction = (r, c)
                break
        continue
    test_row, test_col = row+direction[0], col+direction[1]
    if test_row < 0 or test_col < 0 or test_row >= len(diagram) or test_col >= len(diagram[row]):
        break # If this direction takes us out of bounds we don't wanna check the array
    if diagram[test_row][test_col] == ' ': # If there's no plus but next step is a whitespace we're done
        break
    

t = time.process_time() - t
print(f"Problem 1: {log}")
print(f"Problem 2: {counter}")
print(f"Time elapsed: {t:.2f} s")