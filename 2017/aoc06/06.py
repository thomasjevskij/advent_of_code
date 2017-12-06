import time

def forever(start = 0):
    i = start
    while True:
        yield i
        i += 1

with open('in') as f:
    banks = list(map(int, f.readline().split()))

t = time.process_time()

c2 = 0
visited = list()
visited.append(tuple(banks))
for c in forever(1):
    i, v = max(enumerate(banks), key=lambda x: x[1])
    banks[i] = 0
    while v > 0:
        i += 1
        i %= len(banks)
        banks[i] += 1
        v -= 1
    state = tuple(banks)
    if state in visited:
        c2 = c-visited.index(state)
        break
    visited.append(state)

print("Problem 1: {0}".format(c))
print("Problem 2: {0}".format(c2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
