from time import process_time as pt

def new_code(prev):
    return (prev * 252533) % 33554393

t = pt()
with open('input.txt') as f:
    args = f.readline().rstrip().split()
final_row = int(args[-3].rstrip(','))
final_col = int(args[-1].rstrip('.'))

row = 6
col = 6
p1 = 27995004
while not (row == final_row and col == final_col):
    p1 = new_code(p1)
    if row == 1:
        row += col
        col = 1
        continue
    row -= 1
    col += 1
    
t = pt() - t
print("Problem 1: %d"%p1)
print("Time elapsed: %f s"%t)
