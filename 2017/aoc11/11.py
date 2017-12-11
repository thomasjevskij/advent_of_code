import time

t = time.process_time()

north = 0
east = 0
p2 = 0
distance = lambda n, e: max(int(abs(n)+0.5*abs(e)), abs(e))

with open('in') as f:
    for step in f.read().split(','):
        if step == 'n':
            north += 1
        if step == 's':
            north -= 1
        if step == 'ne':
            north += 0.5
            east += 1
        if step == 'se':
            north -= 0.5
            east += 1
        if step == 'sw':
            north -= 0.5
            east -= 1
        if step == 'nw':
            north += 0.5
            east -= 1
        p2 = max(p2, distance(north, east))

print("Problem 1: {}".format(distance(north, east)))
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
