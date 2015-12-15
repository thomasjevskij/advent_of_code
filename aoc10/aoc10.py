import time

def look_say(s):
    current = s[0]
    count = 0
    new = ''
    for c in s:
        if c != current:
            new += str(count) + current
            current = c
            count = 0
        count += 1
    new += str(count) + current
    return new

t = time.process_time()
with open('input.txt') as f:
    s = f.readline().rstrip()
for i in range(40):
    s = look_say(s)
t = time.process_time() - t
print("Problem 1: %d"%len(s))
print("Time elapsed: %d ms"%int(t * 1000))

t = time.process_time()
for i in range(10):
    s = look_say(s)
t = time.process_time() - t
print("Problem 2: %d"%len(s))
print("Time elapsed: %d ms"%int(t * 1000))
