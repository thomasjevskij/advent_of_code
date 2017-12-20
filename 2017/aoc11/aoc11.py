import time

t = time.process_time()

north = 0
east = 0
p2 = 0
distance = lambda n, e: max(int(abs(n)+0.5*abs(e)), abs(e))
directions = {'n': lambda n, e: (n + 1, e), 's': lambda n, e: (n - 1, e),
              'ne': lambda n, e: (n + 0.5, e + 1), 'se': lambda n, e: (n - 0.5, e + 1),
              'nw': lambda n, e: (n + 0.5, e - 1), 'sw': lambda n, e: (n - 0.5, e - 1)}

with open('in') as f:
    for step in f.read().split(','):
        north, east = directions[step](north, east)
        p2 = max(p2, distance(north, east))

print("Problem 1: {}".format(distance(north, east)))
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
