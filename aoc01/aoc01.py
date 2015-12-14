with open('input.txt') as f:
    d = f.read().rstrip()

floor = 0
look = -1
for i, c in enumerate(d):
    if c == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1 and look == -1:
        look = i + 1
print("Problem 1: %d"%floor)
print("Problem 2: %d"%look)


