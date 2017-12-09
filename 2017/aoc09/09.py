import time

t = time.process_time()

with open('in') as f:
    stream = f.read()

i = 0
depth = 0
p1 = 0
p2 = 0
ignore = False
while i < len(stream):
    c = stream[i]
    if c == '!':
        i += 2
        continue
    if not ignore:
        if c == '{':
            depth += 1
        if c == '}':
            p1 += depth
            depth -= 1
        if c == '<':
            ignore = True
    else:
        if c == '>':
            ignore = False
        else:
            p2 += 1
    i += 1

print("Problem 1: {}".format(p1))
print("Problem 2: {}".format(p2))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
