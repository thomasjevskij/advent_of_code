import math, time, functools

def divisors(n):
    lim = math.ceil(math.sqrt(n)) + 1
    div = set()
    div.add(1)
    div.add(n)
    for i in range(2, lim):
        if n % i == 0:
            div.add(i)
            div.add(n / i)
    return div

def presents(d, i):
    return functools.reduce(lambda x,y: x + int(i / y <= 50) * y, d)

t = time.process_time()
with open('input.txt') as f:
    goal = int(f.read())

i = 100
while sum(divisors(i)) * 10 < goal:
    i += 1
t = time.process_time() - t
print("Problem 1: %d"%i)
print("Time elapsed: %f s"%t)
t = time.process_time()

while presents(divisors(i), i) * 11 < goal:
    i += 1
t = time.process_time() - t
print("Problem 2: %d"%i)
print("Time elapsed: %f s"%t)
