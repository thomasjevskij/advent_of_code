import time

t = time.process_time()
     
with open('in') as f:
    diagram = f.read().split('\n')

direction = 1 + 0j
row = 0
col = diagram[row].find('|')
pos = row + col*1j
log = ''
counter = 1

while True:
    counter += 1
    pos += direction
    row, col = map(int, (pos.real, pos.imag))
    c = diagram[row][col]
    if c.isalpha():
        log += c
    if c == '+':
        newdirs = [direction * 1j, direction * -1j]
        for nd in newdirs: # Look ahead
            test_pos = pos + nd
            test_row, test_col = map(int, (test_pos.real, test_pos.imag))
            if test_row < 0 or test_col < 0 or test_row >= len(diagram) or test_col >= len(diagram[row]):
                continue # If this direction takes us out of bounds we don't wanna check the array
            if diagram[test_row][test_col] != ' ':
                direction = nd
                break
        continue
    test_row, test_col = map(int, ((pos + direction).real, (pos + direction).imag))
    if test_row < 0 or test_col < 0 or test_row >= len(diagram) or test_col >= len(diagram[row]):
        break # If this direction takes us out of bounds we don't wanna check the array
    if diagram[test_row][test_col] == ' ': # If there's no plus but next step is a whitespace we're done
        break
    

t = time.process_time() - t
print(f"Problem 1: {log}")
print(f"Problem 2: {counter}")
print(f"Time elapsed: {t:.2f} s")