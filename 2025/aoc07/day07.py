from collections import defaultdict

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    splitters = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S':
                start = x + 1j * y
            if c == '^':
                splitters.add(x + 1j * y)
    return splitters, start

def p1(splitters, start):
    current = set([start])
    max_y = max(z.imag for z in splitters)
    d = 1j
    count = 0
    while not any(beam.imag >= max_y for beam in current):
        new = set()
        for beam in current:
            if beam + d in splitters:
                count += 1
                new.add(beam - 1 + d)
                new.add(beam + 1 + d)
            else:
                new.add(beam + d)
        current = new
    print(count)

def p2(splitters, start):
    current = defaultdict(int)
    current[start] = 1
    max_y = max(z.imag for z in splitters)
    d = 1j
    while not any(beam.imag >= max_y for beam in current):
        new = defaultdict(int)
        for beam in current:
            if beam + d in splitters:
                new[beam - 1 + d] += current[beam]
                new[beam + 1 + d] += current[beam]
            else:
                new[beam + d] += current[beam]
        current = new
    print(sum(current.values()))

puzzle_input = parse_input()

p1(*puzzle_input[:])
p2(*puzzle_input[:])
