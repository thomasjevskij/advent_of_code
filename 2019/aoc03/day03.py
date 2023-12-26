def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def p1(wire1, wire2):
    deltas = {'R': complex(1, 0), 'L': complex(-1, 0),
              'U': complex(0, 1), 'D': complex(0, -1)}
    v = {}
    pos = complex(0, 0)
    steps = 0
    for move in wire1.split(','):
        d = move[0]
        for _ in range(int(move[1:])):
            pos += deltas[d]
            steps += 1
            v[pos] = steps
    crossings = {}
    pos = complex(0, 0)
    steps = 0
    for move in wire2.split(','):
        d = move[0]
        for _ in range(int(move[1:])):
            pos += deltas[d]
            steps += 1
            if pos in v:
                crossings[pos] = (steps, v[pos])
    s = int(min(abs(z.real) + abs(z.imag) for z in crossings))
    print(s)
    return crossings

def p2(crossings):
    s = min(sum(x) for x in crossings.values())
    print(s)

p2(p1(*parse_input()))
