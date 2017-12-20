import time

t = time.process_time()

aGen = lambda a: (a * 16807) % 2147483647
bGen = lambda b: (b * 48271) % 2147483647
divider = 2147483647
bitMask = 0b1111111111111111

with open('in') as f:
    aStart = int(f.readline().split()[-1])
    bStart = int(f.readline().split()[-1])

a = aStart
b = bStart
aList = []
bList = []

p1 = 0
for _ in range(4*10**7):
    a = aGen(a)
    b = bGen(b)
    if a & bitMask == b & bitMask:
        p1 += 1
    if a % 4 == 0 and len(aList) < 5*10**6:
        aList.append(a)
    if b % 8 == 0 and len(bList) < 5*10**6:
        bList.append(b)

t = time.process_time() - t    

print(f"Problem 1: {p1}")
print(f"Time elapsed: {t:.2f} s")

t = time.process_time()

while len(bList) < 5*10**6:
    b = bGen(b)
    while b % 8 != 0:
        b = bGen(b)
    bList.append(b)

t = time.process_time() - t    
print(f"Problem 2: {sum(aa & bitMask == bb & bitMask for aa, bb in zip(aList, bList))}")
print("Time elapsed: {0:.2f} s".format(t))
