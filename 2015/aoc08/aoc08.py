import re, time

t = time.process_time()
characters = 6202 # I used Microsoft Word :)

l = 0
l2 = 0
with open('input.txt') as f:
    for line in f.readlines():
        b = eval(line)
        l += len(b)
        l2 += len(re.escape(line))

t = time.process_time() - t
print("Problem 1: %d"%(characters - l))
print("Problem 2: %d"%(l2 - characters))
print("Time elapsed: %d ms"%int(t * 1000))
