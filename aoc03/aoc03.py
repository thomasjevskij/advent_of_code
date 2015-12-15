import time

def move(pos, direction, visited):
    if direction == '^':
        pos = (pos[0], pos[1] + 1)
    elif direction == '>':
        pos = (pos[0] + 1, pos[1])
    elif direction == 'v':
        pos = (pos[0], pos[1] - 1)
    else:
        pos = (pos[0] - 1, pos[1])
    visited.add(pos)
    return pos

t = time.process_time()
reg_pos = (0, 0)
santa_pos = (0, 0)
robo_pos = (0,0)
reg_visited = set()
santa_visited = set()
robo_visited = set()

santa_visited.add(santa_pos)
robo_visited.add(robo_pos)
reg_visited.add(reg_pos)

with open('input.txt') as f:
    route = f.readline().rstrip()

for i, c in enumerate(route):
    if i % 2 == 0:
        santa_pos = move(santa_pos, c, santa_visited)
    else:
        robo_pos = move(robo_pos, c, robo_visited)
    reg_pos = move(reg_pos, c, reg_visited)

t = time.process_time() - t
print("Problem 1: %d" % len(reg_visited))
print("Problem 2: %d" % len(santa_visited | robo_visited))
print("Time elapsed: %d ms"%int(t * 1000))
