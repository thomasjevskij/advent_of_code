import time

t = time.process_time()

aFactor = 16807
bFactor = 48271
divider = 2147483647
bitMask = 65535

with open('in') as f:
    aStart = int(f.readline().split()[-1])
    bStart = int(f.readline().split()[-1])

a = aStart
b = bStart
#a = 65
#b = 8921

p1 = 0
for _ in range(int(4e7)):
    a = (a * aFactor) % divider
    b = (b * bFactor) % divider
    if a & bitMask == b & bitMask:
        p1 += 1

t = time.process_time() - t    

print("Problem 1: {}".format(p1))
print("Time elapsed: {0:.2f} s".format(t))

t = time.process_time()

a = aStart
b = bStart
#a = 65
#b = 8921

p2 = 0
for _ in range(int(5e6)):
    a = (a * aFactor) % divider
    while a % 4 != 0:
        a = (a * aFactor) % divider
    b = (b * bFactor) % divider
    while b % 8 != 0:
        b = (b * bFactor) % divider
    if a & bitMask == b & bitMask:
        p2 += 1

t = time.process_time() - t    

print("Problem 2: {}".format(p2))
print("Time elapsed: {0:.2f} s".format(t))
