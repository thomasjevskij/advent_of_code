from operator import add, sub

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

ops = {'R': add, 'L': sub}

def p1(lines):
    cur = 50
    count = 0
    for l in lines:
        d = l[0]
        num = int(l[1:])
        cur = ops[d](cur, num)
        if cur % 100 == 0:
            count += 1
    
    print(count)

def p2(lines):
    cur = 50
    count = 0
    for l in lines:
        d = l[0]
        num = int(l[1:])
        for _ in range(num):
            cur = ops[d](cur, 1) % 100
            if cur == 0:
                count += 1
    print(count)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
