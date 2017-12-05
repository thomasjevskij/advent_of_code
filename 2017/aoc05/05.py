import time

with open('in') as f:
    instructions = list(map(int, f.readlines()))

#instructions = [0, 3, 0, 1, -3]
instructions_2 = instructions[:]
t = time.process_time()

current = 0
steps = 0

while current < len(instructions):
    previous = current
    current += instructions[current]
    instructions[previous] += 1
    steps += 1
print('Problem 1: {0}'.format(steps))
t = time.process_time() - t
print("Time elapsed: {0} ms".format(int(t * 1000)))
t = time.process_time()

current = 0
steps = 0
while current < len(instructions_2):
    previous = current
    current += instructions_2[current]
    if instructions_2[previous] >= 3:
        instructions_2[previous] -= 1
    else:
        instructions_2[previous] += 1
    steps += 1
print('Problem 2: {0}'.format(steps))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
