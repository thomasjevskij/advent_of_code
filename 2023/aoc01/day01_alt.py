def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def analyze(line, t):
    q = []
    i = 0
    while not q:
        s = line[i:]
        for k in t:
            if s.startswith(k):
                q.append(t[k])
        i += 1
    f = -1
    for i in range(len(line)):
        for k in t:
            if line[i:].startswith(k):
                f = t[k]
    return 10*q[0]+f

def p1(lines):
    t = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    s = sum(analyze(l, t) for l in lines)
    print(s)

def p2(lines):
    t = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
            'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6,
            'seven':7, 'eight':8, 'nine':9}
    s = sum(analyze(l, t) for l in lines)
    print(s)


lines = parse_input()

p1(lines)
p2(lines)