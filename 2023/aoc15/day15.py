from collections import defaultdict

def parse_input():
    with open(0) as f:
        steps = f.read().strip().split(',')
    return steps

def HASH(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h

def p1(steps):
    s = sum(HASH(step) for step in steps)
    print(s)

def p2(steps):
    boxes = defaultdict(list)
    for step in steps:
        if '-' in step:
            label = step.split('-')[0]
            id = HASH(label)
            for i, lens in enumerate(boxes[id]):
                if lens.startswith(label):
                    boxes[id].pop(i)
                    # print(*box)
                    break
        if '=' in step:
            label = step.split('=')[0]
            id = HASH(label)
            i = -1
            for ii, lens in enumerate(boxes[id]):
                if lens.startswith(label):
                    i = ii
                    break
            if i == -1:
                boxes[id].append(step)
            else:
                boxes[id][i] = step
    # Always turn a for loop into a list comprehension if you can
    s = sum((i+1) * j * int(lens.split('=')[1]) for i in range(256) for j, lens in enumerate(boxes[i], start=1))
    print(s)

steps = parse_input()

p1(steps[:])
p2(steps[:])
